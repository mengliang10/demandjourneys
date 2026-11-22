/* URL-scanner frontend: the Cloudflare Worker fetches public HTML, then this browser
   parses it as inert text. No third-party scripts are executed or source displayed. */
(function(){
  function init(){
    const root=document.querySelector('.scanner-shell');
    if(!root||root.dataset.scannerReady==='yes')return;
    root.dataset.scannerReady='yes';
    const el=id=>root.querySelector('#'+id);
    const value=id=>el(id)?.value||'';
    const write=(id,message)=>{el(id).textContent=message;};
    let last=null;
    const add=(parent,tag,text,cls)=>{const e=document.createElement(tag);if(cls)e.className=cls;e.textContent=String(text);parent.appendChild(e);return e;};
    const rows=(parent,items)=>{const ul=add(parent,'ul','', 'scanner-list');for(const item of items)add(ul,'li',item);};
    const words=s=>s.trim().split(/\s+/).filter(Boolean);
    const note=(ok,name,details,level='review')=>({status:ok?'pass':level,name,details});
    function extract(raw,url){
      if(raw.length>5e6)throw Error('HTML exceeds the 5 MB browser analysis limit.');
      const doc=new DOMParser().parseFromString(raw,'text/html');
      const meta=name=>doc.querySelector('meta[name="'+name+'"]')?.getAttribute('content')||'';
      const og=key=>doc.querySelector('meta[property="'+key+'"]')?.getAttribute('content')||'';
      const title=doc.querySelector('title')?.textContent?.trim()||'';
      const description=meta('description').trim();
      const h1=[...doc.querySelectorAll('h1')].map(e=>e.textContent.trim());
      const headers={h1:h1.length,h2:doc.querySelectorAll('h2').length,h3:doc.querySelectorAll('h3').length};
      const images=[...doc.querySelectorAll('img')];
      const altMissing=images.filter(e=>!e.hasAttribute('alt')).length;
      const altEmpty=images.filter(e=>e.hasAttribute('alt')&&!e.getAttribute('alt')?.trim()).length;
      const anchors=[...doc.querySelectorAll('a[href]')];
      let base=null;
      try{if(url)base=new URL(url);}catch{}
      let internal=0,external=0,other=0,placeholders=0;
      for(const a of anchors){
        const rawHref=a.getAttribute('href')?.trim()||'';
        if(!rawHref||rawHref==='#'){placeholders++;continue;}
        if(/^(mailto:|tel:|javascript:|data:)/i.test(rawHref)){other++;continue;}
        try{
          if(!base){if(/^https?:\/\//i.test(rawHref))external++;else internal++;}
          else{const link=new URL(rawHref,base);if(link.protocol!=='http:'&&link.protocol!=='https:')other++;else if(link.origin===base.origin)internal++;else external++;}
        }catch{other++;}
      }
      const schemas=[];const jsonErrors=[];
      for(const [index,s] of [...doc.querySelectorAll('script[type="application/ld+json"]')].entries()){
        try{const parsed=JSON.parse(s.textContent||'');schemas.push(parsed);}catch(e){jsonErrors.push('Block '+(index+1)+': '+e.message);}
      }
      const types=[];
      function visit(node){
        if(!node||typeof node!=='object')return;
        if(Array.isArray(node)){node.forEach(visit);return;}
        const type=node['@type'];if(type)types.push(...(Array.isArray(type)?type:[type]).filter(x=>typeof x==='string'));
        if(node['@graph'])visit(node['@graph']);
      }
      schemas.forEach(visit);
      const clean=doc.body.cloneNode(true);
      clean.querySelectorAll('script,style,template,svg,noscript').forEach(n=>n.remove());
      const text=clean.textContent.replace(/\s+/g,' ').trim();
      const headings=[...doc.querySelectorAll('h1,h2,h3')].slice(0,30).map(n=>({level:n.tagName,text:n.textContent.trim().slice(0,160)}));
      const canonical=doc.querySelector('link[rel~="canonical"]')?.getAttribute('href')||'';
      const checks=[
        note(Boolean(title),'Title tag',title?title.length+' characters':'Missing title','important'),
        note(Boolean(description),'Meta description',description?description.length+' characters':'Missing meta description'),
        note(h1.length===1,'Heading hierarchy',h1.length+' H1 elements; '+headers.h2+' H2; '+headers.h3+' H3','review'),
        note(Boolean(canonical),'Canonical link',canonical||'Absent'),
        note(Boolean(og('og:title')),'Open Graph title',og('og:title')||'Absent'),
        note(Boolean(meta('viewport')),'Responsive viewport',meta('viewport')||'Absent'),
        note(Boolean(doc.documentElement.getAttribute('lang')),'Document language',doc.documentElement.getAttribute('lang')||'Absent'),
        note(altMissing===0,'Image alt attributes',altMissing+' missing attributes; '+altEmpty+' empty values (which may be intentional for decorative images)'),
        note(placeholders===0,'Placeholder links',placeholders+' empty or hash-only links'),
        note(jsonErrors.length===0,'JSON-LD parse errors',jsonErrors.length?jsonErrors.join('; '):'No JSON parsing errors'),
        note(schemas.length>0,'Structured data availability',schemas.length+' JSON-LD block(s)'),
        note(!/noindex/i.test(meta('robots')),'Robots meta directive',meta('robots')||'No page-level robots meta directive found')
      ];
      return {source:'Cloudflare Worker fetched source',url:url||null,analyzedAt:new Date().toISOString(),
        title,description,canonical,ogTitle:og('og:title'),headers,headings,h1,images:{total:images.length,missingAlt:altMissing,emptyAlt:altEmpty,lazy:images.filter(i=>i.getAttribute('loading')==='lazy').length},
        links:{total:anchors.length,internal,external,other,placeholders},scripts:doc.querySelectorAll('script').length,
        schemaTypes:[...new Set(types)],schemaBlocks:schemas.length,jsonErrors,documentLanguage:doc.documentElement.getAttribute('lang')||'',
        wordCount:words(text).length,text,checks};
    }
    function render(report){
      const summary=el('scan-summary'),checks=el('scan-checks'),details=el('scan-details');
      summary.replaceChildren();checks.replaceChildren();details.replaceChildren();
      const summaryItems=[['Title',report.title||'Missing'],['Words in parsed body',report.wordCount],['Headings',report.headers.h1+' H1 / '+report.headers.h2+' H2 / '+report.headers.h3+' H3'],['Links',report.links.total],['Images',report.images.total],['JSON-LD blocks',report.schemaBlocks]];
      for(const [key,v] of summaryItems){const tile=add(summary,'div','','scanner-stat');add(tile,'small',key);add(tile,'strong',v);}
      add(checks,'h3','Source checks');
      for(const check of report.checks){const row=add(checks,'div','','scanner-check '+check.status);add(row,'strong',(check.status==='pass'?'PASS':check.status==='important'?'IMPORTANT':'REVIEW')+' · '+check.name);add(row,'p',check.details);}
      add(details,'h3','Technical observations');
      rows(details,['Title: '+(report.title||'Not present'),'Meta description: '+(report.description||'Not present'),'Canonical: '+(report.canonical||'Not present'),
        'Internal/external links: '+report.links.internal+' / '+report.links.external,
        'Images missing alt attribute: '+report.images.missingAlt,
        'Script tags in source: '+report.scripts,
        'JSON-LD types: '+(report.schemaTypes.join(', ')||'None'),
        'Document language: '+(report.documentLanguage||'Not present')]);
      if(report.headings.length){add(details,'h3','First 30 headings');rows(details,report.headings.map(h=>h.level+' · '+h.text));}
      el('scan-report').hidden=false;el('scan-download').disabled=false;
      if(!value('content-text'))el('content-text').value=report.text.slice(0,100000);
      if(!value('serp-title'))el('serp-title').value=report.title;
      if(!value('serp-desc'))el('serp-desc').value=report.description;
      if(!value('serp-url'))el('serp-url').value=report.url||'';
      write('scan-status','Source analysis complete. This does not verify live HTTP headers, crawler access or PageSpeed scores.');
    }
    async function scan(){
      let url;
      try {
        url = new URL(value('scan-url').trim());
        if (!['https:', 'http:'].includes(url.protocol)) throw Error('Invalid URL scheme');
      } catch {
        write('scan-status','Enter a valid website URL beginning with https://.');
        return;
      }
      const endpoint = root.dataset.scannerApi?.trim() || '';
      if (!endpoint) {
        write('scan-status','The URL scanner backend has not been activated yet. The site administrator must deploy and configure the Cloudflare Worker.');
        return;
      }
      const button = el('scan-run');
      button.disabled = true;
      el('scan-report').hidden = true;
      el('scan-download').disabled = true;
      last = null;
      write('scan-status','Fetching public HTML via scanner gateway for '+url.hostname+'…');
      try {
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: { 'content-type': 'application/json' },
          body: JSON.stringify({ url: url.href }),
          credentials: 'omit',
          signal: AbortSignal.timeout(18000)
        });
        let data;
        try { data = await response.json(); } catch { throw Error('The scanner gateway returned an invalid response.'); }
        if (!response.ok) throw Error(data.error || 'Gateway HTTP '+response.status);
        if (typeof data.html !== 'string' || !data.url) throw Error('No HTML was returned.');
        last = extract(data.html, data.url);
        render(last);
      } catch (e) {
        const offline = /Failed to fetch|NetworkError|Load failed/i.test(e.message);
        write('scan-status',offline
          ? 'The scanner gateway cannot be reached. Check its deployment and configuration.'
          : 'Unable to scan: '+e.message);
      } finally { button.disabled = false; }
    }
    el('scan-run').addEventListener('click',scan);
    el('scan-url').addEventListener('keydown',event=>{if(event.key==='Enter'){event.preventDefault();void scan();}});
    el('scan-clear').addEventListener('click',()=>{
      el('scan-url').value='';
      el('scan-report').hidden=true;
      el('scan-download').disabled=true;
      last=null;
      write('scan-status','Cleared.');
    });
    el('scan-download').addEventListener('click',()=>{
      if(!last)return;
      const {text,...report}=last;
      const blob=new Blob([JSON.stringify({...report,textExcerpt:text.slice(0,1500)},null,2)],{type:'application/json'});
      const link=document.createElement('a');link.href=URL.createObjectURL(blob);link.download='demand-journeys-page-audit.json';link.click();URL.revokeObjectURL(link.href);
    });
    const stop=new Set('the a an and or but in on at to of for as is are was were be been by with this that from it its you your our into than they their these those which how what when where over under can will would could should also more most'.split(' '));
    el('content-run').addEventListener('click',()=>{
      const target=el('content-report');target.replaceChildren();
      const text=value('content-text');if(!text.trim()){add(target,'p','Enter content to analyse.');return;}
      const tokens=text.toLowerCase().match(/[\p{L}\p{N}]+/gu)||[];
      const counts=new Map();for(const t of tokens){if(t.length<3||stop.has(t))continue;counts.set(t,(counts.get(t)||0)+1);}
      const top=[...counts.entries()].sort((a,b)=>b[1]-a[1]).slice(0,15);
      const sentences=text.split(/[.!?。！？]+/).filter(s=>s.trim().length>4);
      const summary=add(target,'div','','scanner-summary');
      for(const [label,val] of [['Total words (approx.)',tokens.length],['Unique significant terms',counts.size],['Sentences',sentences.length],['Average terms / sentence',sentences.length?(tokens.length/sentences.length).toFixed(1):'—']]){const tile=add(summary,'div','','scanner-stat');add(tile,'small',label);add(tile,'strong',val);}
      const phrase=value('content-phrase').trim().toLowerCase();
      if(phrase){const occurrences=text.toLowerCase().split(phrase).length-1;add(target,'p','Target phrase: '+occurrences+' occurrence(s). This is descriptive, not an ideal density or ranking signal.');}
      // Flesch Reading Ease is designed for English prose. It is not a search ranking factor.
      const latin=words(text.match(/[A-Za-z][A-Za-z'’-]*/g)?.join(' ')||'');
      const englishSentences=text.split(/[.!?]+/).filter(v=>v.trim().length>10);
      if(latin.length>=30&&englishSentences.length>=2){
        function syllables(token){
          let w=token.toLowerCase().replace(/[^a-z]/g,'');
          if(w.length<=3)return 1;
          w=w.replace(/(?:[^laeiouy]es|ed|[^laeiouy]e)$/,'').replace(/^y/,'');
          return Math.max(1,(w.match(/[aeiouy]{1,2}/g)||[]).length);
        }
        const syllablesTotal=latin.reduce((n,w)=>n+syllables(w),0);
        const ease=206.835-1.015*(latin.length/englishSentences.length)-84.6*(syllablesTotal/latin.length);
        const grade=Math.max(0,0.39*(latin.length/englishSentences.length)+11.8*(syllablesTotal/latin.length)-15.59);
        add(target,'h3','English readability approximation');
        add(target,'p','Flesch Reading Ease: '+Math.round(ease)+' (higher is easier) · Estimated US grade: '+grade.toFixed(1)+'. Estimates may be unreliable on technical terms, product names and non-English content.');
      }
      add(target,'h3','Frequent terms');
      rows(target,top.length?top.map(([term,n])=>term+' · '+n+' occurrences'):['No significant terms identified.']);
      add(target,'p','Word-count thresholds, keyword density and freshness mentions are not reliable Google ranking guarantees.','scanner-caveat');
    });
    el('schema-run').addEventListener('click',()=>{
      const target=el('schema-report');target.replaceChildren();
      try{
        const raw=value('schema-text');if(!raw.trim())throw Error('Paste a JSON-LD object first.');
        let parsed=JSON.parse(raw);
        const nodes=Array.isArray(parsed)?parsed:[parsed];const all=[];const problems=[];
        function inspect(node){
          if(!node||typeof node!=='object'||Array.isArray(node)){problems.push('Expected a JSON-LD object.');return;}
          if(!node['@context'])problems.push('No @context on this node (may be inherited in a @graph).');
          if(!node['@type'])problems.push('Missing @type.');
          const type=node['@type'];all.push(Array.isArray(type)?type.join(', '):type||'Unknown');
          for(const field of ({Organization:['name'],Person:['name'],Article:['headline','author'],Product:['name'],LocalBusiness:['name'],BreadcrumbList:['itemListElement'],FAQPage:['mainEntity']})[type]||[]){
            if(node[field]===undefined||node[field]===null||node[field]==='')problems.push((type||'Node')+' missing common field: '+field);
          }
          if(Array.isArray(node['@graph']))node['@graph'].forEach(inspect);
        }
        nodes.forEach(inspect);
        add(target,'h3','JSON syntax: valid');
        add(target,'p','Detected types: '+all.join(', '));
        if(problems.length){add(target,'h3','Heuristic checks');rows(target,problems);}else add(target,'p','No issues in the supported checks. Full Schema.org / rich result eligibility is not verified.');
      }catch(e){add(target,'p','Validation error: '+e.message);}
    });
    el('serp-run').addEventListener('click',()=>{
      const target=el('serp-report');target.replaceChildren();
      const title=value('serp-title'),description=value('serp-desc'),url=value('serp-url');
      const preview=add(target,'div','','scanner-serp');
      add(preview,'small',url||'example.com');
      add(preview,'h3',title.length>65?title.slice(0,64)+'…':title||'Page title');
      add(preview,'p',description.length>165?description.slice(0,164)+'…':description||'Meta description missing.');
      add(target,'p','Title: '+title.length+' characters · Description: '+description.length+' characters. Real search display is pixel-dependent and may be rewritten.','scanner-caveat');
    });
    const menuButton=root.querySelector('.tools-menu-toggle'),menu=el('tools-menu');
    menuButton?.addEventListener('click',()=>menuButton.setAttribute('aria-expanded',String(menuButton.getAttribute('aria-expanded')!=='true')));
    menu?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>menuButton.setAttribute('aria-expanded','false')));
  }
  document.addEventListener('astro:page-load',init);init();
})();
