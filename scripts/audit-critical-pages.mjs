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
  '/interactive-tools/',
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
const tools=pages.find(p=>p.route==='/interactive-tools/')?.html||'';
for(const id of ['channel-mix','booking-funnel','media-efficiency','ai-readiness','platform-fit']){
  if(!tools.includes('id="'+id+'"'))errors.push('Interactive tool missing: '+id);
}
if(!tools.includes('aria-label="Interactive tool topics"'))errors.push('Interactive tools topic navigation missing');
const map=readFileSync(join(dist,'sitemap.xml'),'utf8');
for(const route of routes.filter(x=>x!=='/privacy/')){
  if(!map.includes('https://www.demandjourneys.com'+route))errors.push('Sitemap missing '+route);
}
console.log(JSON.stringify({checkedRoutes:routes.length,errors},null,2));
if(errors.length)process.exitCode=1;
