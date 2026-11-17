import { getCollection } from 'astro:content';
export async function allPresentations() {
 const entries = await getCollection('presentations', ({data}) => !data.draft);
 return entries.map(({id,data})=>({id,...data,link:data.href,meta:data.format})).sort((a,b)=>
  a.published && b.published ? b.published.localeCompare(a.published)||a.order-b.order : a.published ? -1 : b.published ? 1 : a.order-b.order||a.id.localeCompare(b.id));
}
export async function latestPresentations(limit=3) { return (await allPresentations()).slice(0,limit); }
