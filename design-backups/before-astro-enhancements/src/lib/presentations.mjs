import fs from 'node:fs';
import path from 'node:path';
const plain = value => value.replace(/<[^>]*>/g,'').replace(/&amp;/g,'&').replace(/&nbsp;/g,' ').replace(/&#39;/g,"'").replace(/&quot;/g,'"').replace(/\s+/g,' ').trim();
export function parsePresentations(html) {
 return [...html.matchAll(/<article\s+class="research-card"([^>]*)>([\s\S]*?)<\/article>/g)].map((m,index)=>{
  const body=m[2];
  const tagBlock=body.match(/<div class="research-tags">([\s\S]*?)<\/div>/)?.[1]||'';
  const tags=[...tagBlock.matchAll(/<span>([\s\S]*?)<\/span>/g)].map(t=>plain(t[1]));
  const href=body.match(/class="presentation-open" href="([^"]+)"/)?.[1] || body.match(/href="([^"]+)"/)?.[1];
  if(!href)throw new Error('Presentation requires a link');
  const link=new URL(href,'https://www.demandjourneys.com/hospitality-presentations/').pathname;
  const title=plain(body.match(/<h2[^>]*>([\s\S]*?)<\/h2>/)?.[1]||'Presentation');
  const meta=plain(body.match(/<span class="research-status">([\s\S]*?)<\/span>/)?.[1]||'Presentation');
  const published=m[1].match(/data-published="(\d{4}-\d{2}-\d{2})"/)?.[1];
  const slug=link.replace(/\/$/,'').split('/').pop();
  const thumbnail=`/presentation-previews/${slug}.jpg`;
  return {html:body.replace('View presentation','Open the deck'),tags,link,title,meta,published,index,thumbnail:fs.existsSync(path.resolve('public'+thumbnail))?thumbnail:null};
 }).sort((a,b)=>a.published&&b.published ? b.published.localeCompare(a.published)||a.index-b.index : a.published ? -1 : b.published ? 1 : a.index-b.index);
}
export function latestPresentations(limit=3){
 return parsePresentations(fs.readFileSync(path.resolve('_source/site/hospitality-presentations/index.html'),'utf8')).slice(0,limit);
}
