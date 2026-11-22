import { existsSync, readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

const dist=resolve('dist');
const routes=[
  '/',
  '/profile/',
  '/services/',
  '/services/engagements/',
  '/services/growth-marketing/',
  '/services/platforms-analytics/',
  '/hospitality/',
  '/selected-work/',
  '/selected-work/decks/booking-transformation/',
  '/selected-work/decks/customer-data-platform/',
  '/selected-work/decks/distribution-governance/',
  '/interactive-tools/',
  '/interactive-tools/page-scanner/',
  '/ai-search/',
  '/hospitality-presentations/',
  '/privacy/'
];
const errors=[];
const pages=[];
for(const route of routes){
  const relative=route==='/'?'index.html':join(route.slice(1),'index.html');
  const path=join(dist,relative);
  if(!existsSync(path)){errors.push('Missing page: '+route);continue;}
  const html=readFileSync(path,'utf8');
  if(!/<h1\b/i.test(html)) errors.push('Missing main heading: '+route);
  if(!/<meta\s+name="description"/i.test(html)) errors.push('Missing description: '+route);
  if(!/<link\s+rel="canonical"/i.test(html)) errors.push('Missing canonical: '+route);
  pages.push({route,html});
}
const front=pages.find(p=>p.route==='/')?.html||'';
for(const route of ['/services/engagements/','/selected-work/','/interactive-tools/','/hospitality/']){
  if(!front.includes('href="'+route+'"'))errors.push('Homepage missing discovery link: '+route);
}
const selected=pages.find(p=>p.route==='/selected-work/')?.html||'';
for(const slug of ['booking-transformation','customer-data-platform','distribution-governance']){
  const route='/selected-work/decks/'+slug+'/';
  if(!selected.includes('src="'+route+'"'))errors.push('Selected Work embedding missing: '+slug);
  const deck=pages.find(p=>p.route===route)?.html||'';
  if(!deck.includes('class="reveal"'))errors.push('Reveal.js deck missing: '+slug);
  if(!deck.includes('Placeholder edition'))errors.push('Placeholder label missing: '+slug);
}
const tools=pages.find(p=>p.route==='/interactive-tools/')?.html||'';
for(const id of ['channel-mix','booking-funnel','media-efficiency','roi-scenario','ai-readiness','platform-fit']){
  if(!tools.includes('id="'+id+'"'))errors.push('Interactive tool missing: '+id);
}
if(!tools.includes('href="/interactive-tools/page-scanner/"'))errors.push('Page Scanner missing from Interactive Tools directory');
const scanner=pages.find(p=>p.route==='/interactive-tools/page-scanner/')?.html||'';
for(const id of ['page-audit','content-analysis','schema-analysis','serp-analysis'])if(!scanner.includes('id="'+id+'"'))errors.push('Page Scanner analyzer missing: '+id);
if(!scanner.includes('aria-label="Interactive tool topics"'))errors.push('Page Scanner left navigation missing');
if(!existsSync(join(dist,'interactive-tools','page-scanner.js')))errors.push('Page Scanner JavaScript missing');
if(!tools.includes('aria-label="Interactive tool topics"'))errors.push('Interactive tools topic navigation missing');
const map=readFileSync(join(dist,'sitemap.xml'),'utf8');
for(const route of routes.filter(x=>x!=='/privacy/')){
  if(!map.includes('https://www.demandjourneys.com'+route))errors.push('Sitemap missing '+route);
}
// Prevent a future presentation template from silently reverting to the superseded logo.
for(const name of ['wordmark-forest-456.webp','wordmark-white-456.webp']){
  if(!existsSync(join(dist,'identity',name)))errors.push('Production wordmark missing: '+name);
}
for(const file of ['hospitality-presentations/personal-portfolio/portfolio.css','hospitality-presentations/geo-work/geo.css','reveal/css/demand-journeys.css','brand/presentation-logo.css']){
  const target=join(dist,file);
  if(!existsSync(target)||!readFileSync(target,'utf8').includes('/identity/wordmark-')){
    errors.push('Presentation logo styling missing: '+file);
  }
}
const selectedDeck=pages.find(p=>p.route==='/selected-work/decks/booking-transformation/')?.html||'';
if(!selectedDeck.includes('/identity/wordmark-forest-456.webp'))errors.push('Selected Work decks missing production wordmark');
const atlas=join(dist,'hospitality-presentations/tri-market-blueprint/index.html');
if(existsSync(atlas)&&!readFileSync(atlas,'utf8').includes('/identity/wordmark-white-456.webp')){
  errors.push('Tri-market blueprint missing production wordmark');
}
for(const kind of ['hotels','airlines','cruises','tours']){
  const file=join(dist,'demo',kind,'presentation.html');
  if(!existsSync(file)||!readFileSync(file,'utf8').includes('/brand/presentation-logo.css')){
    errors.push('Demo deck missing production wordmark stylesheet: '+kind);
  }
}
console.log(JSON.stringify({checkedRoutes:routes.length,errors},null,2));
if(errors.length)process.exitCode=1;
