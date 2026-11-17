const fs=require('fs'),path=require('path'),http=require('http'),cp=require('child_process');
const root=path.resolve('dist'),qa=path.resolve('qa');
const types={'.html':'text/html','.css':'text/css','.js':'text/javascript','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.woff2':'font/woff2','.pdf':'application/pdf'};
const server=http.createServer((req,res)=>{try{let p=path.join(root,decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(!p.startsWith(root))throw Error();if(fs.existsSync(p)&&fs.statSync(p).isDirectory())p=path.join(p,'index.html');if(!fs.existsSync(p)){res.writeHead(404);res.end('Not found');return;}res.setHeader('Content-Type',types[path.extname(p)]||'application/octet-stream');let body=fs.readFileSync(p);if(req.url.includes('qa-many=1')&&p.endsWith('hospitality-presentations/index.html'))body=Buffer.from(body.toString().replace(/(<article class="research-card"[^>]*>[\s\S]*?<\/article>)/,m=>m.repeat(13)));if(req.url.includes('qa-dates=1')&&p.endsWith('hospitality-presentations/index.html')){let n=0;body=Buffer.from(body.toString().replace(/data-published(?:="[^"]*")?/g,()=>`data-published="${['2026-01-15','2026-02-15',''][n++]||''}"`));}res.end(body);}catch{res.writeHead(400);res.end();}});
(async()=>{await new Promise(r=>server.listen(4317,'127.0.0.1',r));const profile=fs.mkdtempSync('/tmp/dj-editorial-browser-');const browser=cp.spawn('chromium',['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--remote-debugging-port=9249','--user-data-dir='+profile,'about:blank'],{stdio:'ignore'});let ws;try{let pages;for(let i=0;i<100;i++){try{pages=await(await fetch('http://127.0.0.1:9249/json')).json();break}catch{await new Promise(r=>setTimeout(r,100));}}if(!pages)throw Error('Browser unavailable');ws=new WebSocket(pages[0].webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);let id=0,pending=new Map(),errors=[],requests=[];ws.onmessage=e=>{let m=JSON.parse(e.data);if(m.id){const p=pending.get(m.id);pending.delete(m.id);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result);}else if(m.method==='Runtime.exceptionThrown')errors.push(m.params.exceptionDetails.text);else if(m.method==='Network.requestWillBeSent')requests.push(m.params.request.url);};const call=(method,params={})=>new Promise((resolve,reject)=>{let n=++id;pending.set(n,{resolve,reject});ws.send(JSON.stringify({id:n,method,params}));});const ev=async expression=>{let r=await call('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};await call('Page.enable');await call('Runtime.enable');await call('Network.enable');
const wait=async exp=>{for(let i=0;i<100;i++){if(await ev(exp))return;await new Promise(r=>setTimeout(r,50));}throw Error('Timeout '+exp)};
const navigate=async url=>{await ev('window.__qaLeaving=true');await call('Page.navigate',{url});await wait('!window.__qaLeaving && document.readyState==="complete"');};
const reload=async()=>{await ev('window.__qaLeaving=true');await call('Page.reload');await wait('!window.__qaLeaving && document.readyState==="complete"');};
const results=[];
for(const [label,width,height] of [['desktop',1440,1000],['mobile',390,844],['small-mobile',320,740]]){await call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:width<700});await navigate('http://127.0.0.1:4317/hospitality-presentations/?qa-many=1');
await wait('document.readyState==="complete" && !!document.querySelector(".library-tools") && !document.querySelector(".library-tools").hidden');
if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===12`))throw Error('Pagination first page');
await ev(`document.querySelector('#library-next').click()`);
if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===3&&location.search.includes('page=2')`))throw Error('Pagination next page');
await reload();await wait('document.readyState==="complete" && !!document.querySelector(".library-tools") && !document.querySelector(".library-tools").hidden');
if(!await ev(`document.querySelector('#library-page').textContent==='Page 2 of 2'`))throw Error('Pagination URL restore');
await navigate('http://127.0.0.1:4317/');await wait('document.readyState==="complete" && !!document.querySelector(".hero")');await ev('document.fonts.ready');const metrics=await ev(`(()=>{const c=document.querySelector('.header-cta').getBoundingClientRect();return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,pageHeight:document.documentElement.scrollHeight,viewport:innerHeight,primaryCTAVisible:c.bottom<innerHeight&&c.top>=0,logoLoaded:document.querySelector('.logo img').naturalWidth>0}})()`);if(metrics.scrollWidth>width+1||!metrics.primaryCTAVisible||!metrics.logoLoaded)throw Error(label+' layout '+JSON.stringify(metrics));
if(width<700){await ev(`document.querySelector('.menu-toggle').click()`);if(!await ev(`document.querySelector('.menu-toggle').getAttribute('aria-expanded')==='true'&&getComputedStyle(document.querySelector('#main-navigation')).display!=='none'`))throw Error('Menu open');await call('Input.dispatchKeyEvent',{type:'keyDown',key:'Escape',code:'Escape'});if(!await ev(`document.querySelector('.menu-toggle').getAttribute('aria-expanded')==='false'`))throw Error('Escape menu');}
if(!await ev(`document.querySelectorAll('#main-navigation a').length===5&&!document.querySelector('.service-menu')`))throw Error('Direct service navigation');
if(width>1000&&!await ev(`document.querySelector('#enquiry-form .submit-btn').getBoundingClientRect().bottom<innerHeight`))throw Error('Enquiry below fold on desktop');
await ev(`document.querySelector('#help-with').value='Audit'`);await ev(`document.querySelector('#name').value='Local QA';document.querySelector('#email').value='qa@example.com';document.querySelector('#issue').value='Local preview test only';document.querySelector('#enquiry-form').requestSubmit()`);await wait('!document.querySelector("#form-status").hidden');if(!await ev(`document.querySelector('#form-status').textContent.includes('nothing has been sent')`))throw Error('Local form safeguard');await ev(`document.querySelector('#enquiry-form').reset();document.querySelector('#form-status').hidden=true;document.activeElement.blur();document.documentElement.style.scrollBehavior='auto';scrollTo(0,0)`);await new Promise(r=>setTimeout(r,400));let shot=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width,height:await ev('document.documentElement.scrollHeight'),scale:1}});fs.writeFileSync(path.join(qa,label+'.png'),Buffer.from(shot.data,'base64'));results.push({label,...metrics,localForm:true});}
const interiorResults=[];
for(const route of ['profile','hospitality-presentations','privacy','ai-search','services','services/growth-marketing','services/platforms-analytics']){
 for(const [label,width,height] of [['desktop',1440,1000],['mobile',390,844],['small-mobile',320,740]]){
 await call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:width<700});
 await navigate('http://127.0.0.1:4317/'+route+'/');
 await wait('document.readyState==="complete" && !!document.querySelector(".interior")');await ev('document.fonts.ready');
 const metrics=await ev(`({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,headings:document.querySelectorAll('h1').length,font:getComputedStyle(document.querySelector('h1')).fontFamily,logoLoaded:document.querySelector('.logo img').naturalWidth>0,nav:[...document.querySelectorAll('#main-navigation a')].map(a=>a.getAttribute('href'))})`);
 if(metrics.scrollWidth>width+1||metrics.headings!==1||!metrics.logoLoaded||!metrics.font.includes('Outfit'))throw Error(route+' '+label+' '+JSON.stringify(metrics));
 if(width<700){await ev(`document.querySelector('.menu-toggle').click()`);if(!await ev(`document.querySelector('#main-navigation').getBoundingClientRect().height>0`))throw Error('Inner mobile menu');await call('Input.dispatchKeyEvent',{type:'keyDown',key:'Escape',code:'Escape'});}
 if(route==='hospitality-presentations'){
 await wait('!document.querySelector(".library-tools").hidden');
 await ev(`document.querySelector('.month-dropdown summary').click()`);
 if(!await ev(`document.querySelectorAll('.calendar-months button:not(:disabled)').length===1&&!document.querySelector('[data-month-number="11"]').disabled&&document.querySelectorAll('.deck-actions time[datetime="2026-11-16"]').length===3`))throw Error('Month availability or date labels');
 const calendar=await ev(`(()=>{const r=document.querySelector('.month-panel').getBoundingClientRect();return {left:r.left,right:r.right,width:innerWidth}})()`);
 if(calendar.left<0||calendar.right>calendar.width+1)throw Error('Calendar overflow '+JSON.stringify(calendar));
 await ev(`document.querySelector('[data-month-number="11"]').click()`);
 if(!await ev(`document.querySelector('#publication-month').value==='2026-11'&&document.querySelectorAll('.library-results article:not([hidden])').length===3`))throw Error('Calendar month selection');
 await ev(`document.querySelector('#clear-library').click()`);
 const controlPosition=await ev(`document.querySelector('#presentation-search').getBoundingClientRect().top`);
 if(controlPosition>420)throw Error('Search too far down '+controlPosition);
 await ev(`document.querySelector('.subject-dropdown summary').click()`);
 const panel=await ev(`(()=>{const r=document.querySelector('.subject-panel').getBoundingClientRect();return {left:r.left,right:r.right,width:innerWidth}})()`);
 if(panel.left<0||panel.right>panel.width+1)throw Error('Subject panel overflow '+JSON.stringify(panel));
 await ev(`document.querySelector('[data-subject="search"]').click()`);
 if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===1&&location.search.includes('subject=search')`))throw Error('Subject filter');
 await ev(`document.querySelector('#subject-search').value='technical';document.querySelector('#subject-search').dispatchEvent(new Event('input'))`);
 if(!await ev(`document.querySelectorAll('[data-subject-group]:not([hidden])').length===1`))throw Error('Subject search');
 await call('Input.dispatchKeyEvent',{type:'keyDown',key:'Escape',code:'Escape'});
 if(await ev(`document.querySelector('.subject-dropdown').open`))throw Error('Dropdown Escape');
 await ev(`document.querySelector('#clear-library').click();document.querySelector('#publication-month').value='2026-01';document.querySelector('#publication-month').dispatchEvent(new Event('change'))`);
 if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===0`))throw Error('Exclude undated from month search');
 await ev(`document.querySelector('#clear-library').click();document.activeElement.blur()`);

 const previews=await ev(`[...document.querySelectorAll('.deck-preview')].map(el=>{const r=el.getBoundingClientRect();return {width:r.width,height:r.height,ratio:r.width/r.height}})`);
 if(previews.length!==3||previews.some(p=>Math.abs(p.ratio-16/9)>.01))throw Error('Widescreen ratio '+JSON.stringify(previews));
 await ev(`document.querySelector('.deck-preview').scrollIntoView()`);
 await wait(`[...document.querySelectorAll('.deck-preview img')].every(img=>img.complete&&img.naturalWidth>0)`);
 await ev(`document.documentElement.style.scrollBehavior='auto';scrollTo(0,0)`);

 await wait('!!document.querySelector(".library-tools") && !document.querySelector(".library-tools").hidden');
 await ev(`document.querySelector('[data-tag="Conversion"]').click()`);
 if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===1&&location.search.includes('tag=Conversion')`))throw Error('Tag filter');
 await ev(`document.querySelector('[data-tag="Technical SEO"]').click()`);
 if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===2`))throw Error('Multiple tags');
 await ev(`document.querySelector('#presentation-search').value='nonexistent-qa';document.querySelector('#presentation-search').dispatchEvent(new Event('input'))`);
 if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===0&&!document.querySelector('.library-empty').hidden`))throw Error('Empty search');
 await ev(`document.querySelector('#clear-library').click();document.querySelector('#presentation-search').value='economics';document.querySelector('#presentation-search').dispatchEvent(new Event('input'))`);
 if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===3`))throw Error('Keyword search');
 await ev(`document.querySelector('#clear-library').click();document.activeElement.blur()`);
 if(!await ev(`!location.search&&document.querySelectorAll('.library-results article:not([hidden])').length===3`))throw Error('Reset filters');
}
if(await ev(`!!document.querySelector('a[href*="substack"]')`))throw Error('Substack remains');
const urls=await ev(`[...document.querySelectorAll('a[href]')].map(a=>a.href).filter(x=>x.startsWith(location.origin))`);
 for(const url of [...new Set(urls)]){const u=new URL(url),response=await fetch(url);if(!response.ok)throw Error('Broken internal link '+url);if(u.hash&&u.pathname==='/'+route+'/'){if(!await ev('!!document.getElementById('+JSON.stringify(decodeURIComponent(u.hash.slice(1)))+')'))throw Error('Broken fragment '+url);}}
 if(label!=='small-mobile'){const shot=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width,height:Math.min(await ev('document.documentElement.scrollHeight'),6500),scale:1}});fs.writeFileSync(path.join(qa,route.replaceAll('/','-')+'-'+label+'.png'),Buffer.from(shot.data,'base64'));}
 interiorResults.push({route,label,...metrics});
 }
}
await navigate('http://127.0.0.1:4317/');await wait('document.readyState==="complete" && !!document.querySelector(".hero")');
// Dated records are a test-server fixture, never production publication claims.
await navigate('http://127.0.0.1:4317/hospitality-presentations/?qa-dates=1');
await wait('!document.querySelector(".library-tools").hidden');
await ev(`document.querySelector('#publication-month').value='2026-01';document.querySelector('#publication-month').dispatchEvent(new Event('change'))`);
if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===1 && location.search.includes('month=2026-01')`))throw Error('Month filter');
await reload();await wait('!document.querySelector(".library-tools").hidden');
if(!await ev(`document.querySelector('#publication-month').value==='2026-01'&&document.querySelectorAll('.library-results article:not([hidden])').length===1`))throw Error('Month URL restore');
await ev(`document.querySelector('#publication-month').value='2026-02';document.querySelector('#publication-month').dispatchEvent(new Event('change'))`);
if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===1 && document.querySelector('.library-results article:not([hidden])').dataset.published==='2026-02-15'`))throw Error('Month switch');
await ev(`document.querySelector('.active-library-filters button').click()`);
if(!await ev(`!document.querySelector('#publication-month').value && document.querySelectorAll('.library-results article:not([hidden])').length===3`))throw Error('Remove month chip');
await navigate('http://127.0.0.1:4317/');
// Verify real client-side navigation, repeated visits and browser history.
await ev(`window.__transitionProbe='same-document';window.__pageLoads=0;document.addEventListener('astro:page-load',()=>window.__pageLoads++)`);
const clickPage=async(selector,page)=>{
 const previous=await ev('window.__pageLoads');
 await ev('document.querySelector('+JSON.stringify(selector)+').click()');
 await wait('document.body.dataset.page==='+JSON.stringify(page)+' && window.__pageLoads>'+previous);
 if(!await ev(`window.__transitionProbe==='same-document'`))throw Error('Unexpected full page reload');
};
for(let visit=0;visit<2;visit++){
 await clickPage('#main-navigation a[href="/profile/"]','profile');
 await ev(`document.querySelector('.profile-background summary').click()`);
 if(!await ev(`document.querySelector('.profile-background details').open`))throw Error('Profile disclosure after transition');
 await clickPage('#main-navigation a[href="/hospitality-presentations/"]','hospitality-presentations');
 await wait('!document.querySelector(".library-tools").hidden');
 await ev(`document.querySelector('[data-tag="Conversion"]').click()`);
 if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===1`))throw Error('Filters after transition');
 await clickPage('#main-navigation a[href="/services/growth-marketing/"]','growth-marketing');
 await clickPage('.service-introduction .button','home');
 if(!await ev(`document.querySelector('#help-with').value==='Growth Marketing'`))throw Error('Service prefill after transition');
 await ev(`document.querySelector('#name').value='Local QA';document.querySelector('#email').value='qa@example.com';document.querySelector('#issue').value='Transition test';document.querySelector('#enquiry-form').requestSubmit()`);
 if(!await ev(`document.querySelector('#form-status').textContent.includes('nothing has been sent')`))throw Error('Form after transition');
 const count=await ev('window.__pageLoads');await ev('history.back()');await wait('document.body.dataset.page==="growth-marketing" && window.__pageLoads>'+count);
 const back=await ev('window.__pageLoads');await ev('history.forward()');await wait('document.body.dataset.page==="home" && window.__pageLoads>'+back);
}
await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
await clickPage('#main-navigation a[href="/profile/"]','profile');
if(!await ev(`matchMedia('(prefers-reduced-motion:reduce)').matches`))throw Error('Reduced motion');
await call('Emulation.setEmulatedMedia',{features:[]});
await call('Emulation.setScriptExecutionDisabled',{value:true});
await navigate('http://127.0.0.1:4317/hospitality-presentations/');
if(!await ev(`document.querySelectorAll('.library-results article:not([hidden])').length===3 && document.querySelector('.library-tools').hidden`))throw Error('No-JS library fallback');
await call('Emulation.setScriptExecutionDisabled',{value:false});
await navigate('http://127.0.0.1:4317/');
const links=await ev(`[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href')).filter(x=>x.startsWith('/')&&!x.startsWith('//'))`);let bad=[];for(const url of [...new Set(links)]){const response=await fetch('http://127.0.0.1:4317'+url);if(!response.ok)bad.push({url,status:response.status});}if(bad.length)throw Error('Broken links '+JSON.stringify(bad));if(requests.some(x=>/formsubmit|googletagmanager/.test(x)))throw Error('Local preview made live request');if(errors.length)throw Error('Runtime errors '+errors);
const report={availabilityCalendar:true,addedDateLabels:true,subjectFilters:true,monthYearFilter:true,monthUrlRestore:true,monthChipRemoval:true,clientTransitions:true,repeatedNavigation:true,historyNavigation:true,noJsLibrary:true,reducedMotion:true,tagSearchReset:true,paginationFixture:15,paginationUrlRestore:true,results,interiorResults,internalLinksChecked:[...new Set(links)].length,brokenLinks:bad,errors,liveRequests:false};fs.writeFileSync(path.join(qa,'browser-report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
}finally{if(ws)ws.close();browser.kill();server.close();}})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
