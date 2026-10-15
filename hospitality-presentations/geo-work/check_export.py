import urllib.request,json,time,base64
from pathlib import Path
p=Path(__file__).resolve().parent;base='http://127.0.0.1:9517'
def req(path,data=None):
 r=urllib.request.Request(base+path,data=json.dumps(data).encode() if data is not None else None,headers={'Content-Type':'application/json'})
 return json.load(urllib.request.urlopen(r,timeout=90))['value']
s=req('/session',{'capabilities':{'alwaysMatch':{'browserName':'chrome','goog:chromeOptions':{'binary':'/opt/helium-browser-bin/chrome','args':['--headless=new','--no-sandbox','--disable-dev-shm-usage','--window-size=1500,1000']}}}})['sessionId'];root='/session/'+s
req(root+'/url',{'url':p.joinpath('index.html').as_uri()});time.sleep(.8)
def js(x):return req(root+'/execute/sync',{'script':x,'args':[]})
assert js('return Reveal.getTotalSlides()')==28
js("Reveal.configure({transition:'none'})")
issues=[]
for i in range(28):
 js(f'Reveal.slide({i})');time.sleep(.06)
 result=js("let s=Reveal.getCurrentSlide(),body=s.querySelector('.body'),f=s.querySelector('.source');return {slide:Reveal.getIndices().h+1,overflow:body.getBoundingClientRect().bottom>f.getBoundingClientRect().top-8,title:s.querySelector('h2').innerText,bottom:body.getBoundingClientRect().bottom,footer:f.getBoundingClientRect().top};")
 if result['overflow']:issues.append(result)
 p.joinpath(f'check-{i+1:02}.png').write_bytes(base64.b64decode(req(root+'/screenshot')))
print('OVERFLOW',json.dumps(issues),flush=True)
assert js("return document.getElementById('leads-out').textContent")=='50'
assert js("document.getElementById('cost').value=20000;calculate();return document.getElementById('leads-out').textContent")=='100'
js("document.getElementById('cost').value=10000;calculate();document.querySelector('[data-priority=answers]').click()")
assert 'Resolve the factual gap' in js("return document.getElementById('priority-detail').textContent")
js("priority('access')")
# Check navigation and layout at a small viewport.
req(root+'/window/rect',{'width':390,'height':844});js('Reveal.slide(0);Reveal.layout()');time.sleep(.3)
p.joinpath('mobile.png').write_bytes(base64.b64decode(req(root+'/screenshot')))
print('MOBILE',js("return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,buttons:[...document.querySelectorAll('header a,header button')].map(e=>({text:e.textContent,right:e.getBoundingClientRect().right}))}"),flush=True)
req(root+'/window/rect',{'width':1500,'height':1000})
req(root+'/url',{'url':p.joinpath('index.html').as_uri()+'?print-pdf'});time.sleep(1)
js("document.querySelectorAll('header,.bottom').forEach(e=>e.remove());document.querySelectorAll('a[href^=\"#/\"]').forEach(e=>e.removeAttribute('href'));document.querySelector('.cover .button').textContent='Anonymised diagnostic case studies';document.querySelectorAll('.lead').forEach(e=>{if(e.textContent.includes('Use the selector'))e.textContent='Example starting point: an access problem. The first sprint depends on the diagnosed constraint.';if(e.textContent.includes('Explore what must'))e.textContent='Illustrative example using the default assumptions below. Interactive controls are available in the HTML deck.'});")
assert js("return document.querySelectorAll('.pdf-page').length")==28
pdf=req(root+'/goog/cdp/execute',{'cmd':'Page.printToPDF','params':{'printBackground':True,'preferCSSPageSize':True,'displayHeaderFooter':False,'marginTop':0,'marginBottom':0,'marginLeft':0,'marginRight':0}})
p.joinpath('Demand-Journeys-GEO-AEO-SEO.pdf').write_bytes(base64.b64decode(pdf['data']))
print('Exported PDF; interactions passed.',flush=True)
p.joinpath('validation.json').write_text(json.dumps({'overflow':issues,'slides':28,'interactions':'passed'},indent=2))
