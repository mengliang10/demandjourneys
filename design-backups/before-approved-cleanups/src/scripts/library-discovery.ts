import {matchesPresentation,validMonth} from '../lib/library-filters.mjs';
const initialized=new WeakSet<Element>();
let lifecycle:AbortController;
export function initializeLibrary(){
 const root=document.querySelector<HTMLElement>('.presentation-library');
 if(!root){lifecycle?.abort();return;}
 if(initialized.has(root))return;
 lifecycle?.abort();initialized.add(root);lifecycle=new AbortController();
 const find=<T extends Element>(s:string)=>root.querySelector<T>(s)!;
 const input=find<HTMLInputElement>('#presentation-search');
 const month=find<HTMLInputElement>('#publication-month');
 const dropdown=find<HTMLDetailsElement>('.subject-dropdown');
 const subjectSearch=find<HTMLInputElement>('#subject-search');
 const topicButtons=[...root.querySelectorAll<HTMLButtonElement>('[data-tag]')];
 const subjectChecks=[...root.querySelectorAll<HTMLInputElement>('[data-subject]')];
 const tags=new Set<string>(),subjects=new Set<string>();
 const params=new URLSearchParams(location.search);
 input.value=params.get('q')||'';
 for(const tag of params.getAll('tag'))if(topicButtons.some(b=>b.dataset.tag===tag))tags.add(tag);
 for(const id of params.getAll('subject'))if(subjectChecks.some(b=>b.dataset.subject===id))subjects.add(id);
 month.value=validMonth(params.get('month'))?params.get('month')!:'';
 let page=Math.max(1,parseInt(params.get('page')||'1')||1);
 const previous=find<HTMLButtonElement>('#library-prev'),next=find<HTMLButtonElement>('#library-next');
 const cards=[...root.querySelectorAll<HTMLElement>('.research-card')];
 const records=cards.map(card=>({card,tags:JSON.parse(card.dataset.tags||'[]') as string[],subjects:JSON.parse(card.dataset.subjects||'[]') as string[],published:card.dataset.published||'',text:(card.dataset.search||card.textContent!).toLocaleLowerCase()}));
 const monthPicker=find<HTMLDetailsElement>('.month-dropdown');
 const yearSelect=find<HTMLSelectElement>('#calendar-year');
 const years=[...new Set(records.filter(r=>r.published).map(r=>r.published.slice(0,4)))].sort().reverse();
 const initialYear=month.value.slice(0,4)||years[0]||String(new Date().getFullYear());
 if(!years.includes(initialYear))years.push(initialYear);
 years.sort().reverse().forEach(year=>{const option=document.createElement('option');option.value=year;option.textContent=year;yearSelect.append(option);});
 yearSelect.value=initialYear;
 const names=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
 names.forEach((name,index)=>{const button=document.createElement('button');button.type='button';button.dataset.monthNumber=String(index+1).padStart(2,'0');button.textContent=name;button.addEventListener('click',()=>{month.value=yearSelect.value+'-'+button.dataset.monthNumber;month.dispatchEvent(new Event('change'));monthPicker.open=false;monthPicker.querySelector('summary')!.focus();});find('.calendar-months').append(button);});
 function renderCalendar(){
  const counts=new Map<string,number>();
  for(const record of records.filter(r=>matchesPresentation(r,{query:input.value,tags,subjects,month:''}))){if(record.published){const key=record.published.slice(0,7);counts.set(key,(counts.get(key)||0)+1);}}
  let available=0;
  root!.querySelectorAll<HTMLButtonElement>('[data-month-number]').forEach(button=>{const value=yearSelect.value+'-'+button.dataset.monthNumber,count=counts.get(value)||0;button.disabled=!count;button.setAttribute('aria-pressed',String(month.value===value));button.setAttribute('aria-label',`${button.textContent} ${yearSelect.value}: ${count} presentations`);if(count)available++;});
  find<HTMLElement>('.calendar-empty').hidden=available>0;
  find<HTMLElement>('#month-label').textContent=month.value?new Intl.DateTimeFormat('en-SG',{month:'short',year:'numeric',timeZone:'UTC'}).format(new Date(month.value+'-01')):'All months';
 }
 yearSelect.addEventListener('change',renderCalendar);
 monthPicker.addEventListener('toggle',()=>{if(monthPicker.open){dropdown.open=false;if(month.value)yearSelect.value=month.value.slice(0,4);renderCalendar();}});
 dropdown.addEventListener('toggle',()=>{if(dropdown.open)monthPicker.open=false;});
 find('.all-months').addEventListener('click',()=>{month.value='';monthPicker.open=false;month.dispatchEvent(new Event('change'));monthPicker.querySelector('summary')!.focus();});
 const pageSize=12;
 const selectedArea=find<HTMLElement>('.active-library-filters');
 function render(updateUrl=true){
  renderCalendar();
  const filters={query:input.value,tags,subjects,month:validMonth(month.value)?month.value:''};
  const matches=records.filter(record=>matchesPresentation(record,filters));
  const pages=Math.max(1,Math.ceil(matches.length/pageSize));page=Math.min(page,pages);
  const visible=new Set(matches.slice((page-1)*pageSize,page*pageSize));
  records.forEach(record=>record.card.hidden=!visible.has(record));
  topicButtons.forEach(b=>b.setAttribute('aria-pressed',String(tags.has(b.dataset.tag!))));
  subjectChecks.forEach(b=>b.checked=subjects.has(b.dataset.subject!));
  find<HTMLElement>('#subject-selection-count').textContent=tags.size+subjects.size?`(${tags.size+subjects.size})`:'';
  find<HTMLElement>('#library-status').textContent=`${matches.length} of ${cards.length} presentations`;
  find<HTMLElement>('.library-empty').hidden=matches.length!==0;
  find<HTMLElement>('.library-pagination').hidden=pages<=1;
  find<HTMLElement>('#library-page').textContent=`Page ${page} of ${pages}`;
  previous.disabled=page===1;next.disabled=page===pages;
  selectedArea.replaceChildren();
  const chip=(text:string,remove:()=>void)=>{const b=document.createElement('button');b.type='button';b.textContent=text+' ×';b.setAttribute('aria-label','Remove '+text+' filter');b.addEventListener('click',()=>{remove();page=1;render();});selectedArea.append(b);};
  subjects.forEach(id=>chip(subjectChecks.find(b=>b.dataset.subject===id)!.parentElement!.textContent!.trim(),()=>subjects.delete(id)));
  tags.forEach(tag=>chip(tag,()=>tags.delete(tag)));
  if(month.value)chip(new Intl.DateTimeFormat('en-SG',{month:'short',year:'numeric',timeZone:'UTC'}).format(new Date(month.value+'-01')),()=>{month.value='';});
  if(updateUrl){const url=new URL(location.href);for(const key of ['q','tag','subject','date','on','from','to','month','page'])url.searchParams.delete(key);if(input.value.trim())url.searchParams.set('q',input.value.trim());tags.forEach(tag=>url.searchParams.append('tag',tag));subjects.forEach(id=>url.searchParams.append('subject',id));if(validMonth(month.value))url.searchParams.set('month',month.value);if(page>1)url.searchParams.set('page',String(page));history.replaceState(null,'',url);}

 }
 const changed=()=>{page=1;render();};
 input.addEventListener('input',changed);
 month.addEventListener('change',changed);
 topicButtons.forEach(b=>b.addEventListener('click',()=>{const tag=b.dataset.tag!;tags.has(tag)?tags.delete(tag):tags.add(tag);changed();}));
 subjectChecks.forEach(b=>b.addEventListener('change',()=>{const id=b.dataset.subject!;b.checked?subjects.add(id):subjects.delete(id);changed();}));
 find('#clear-library').addEventListener('click',()=>{input.value='';month.value='';tags.clear();subjects.clear();subjectSearch.value='';filterSubjects();changed();input.focus();});
 function filterSubjects(){const q=subjectSearch.value.trim().toLocaleLowerCase();let count=0;root!.querySelectorAll<HTMLElement>('[data-subject-group]').forEach(group=>{const name=group.querySelector('legend')!.textContent!.toLocaleLowerCase();let found=false;group.querySelectorAll<HTMLButtonElement>('[data-tag]').forEach(button=>{button.hidden=!(name.includes(q)||button.dataset.tag!.toLocaleLowerCase().includes(q));if(!button.hidden)found=true;});group.hidden=!found;if(found)count++;});find<HTMLElement>('.subject-search-empty').hidden=count>0;}
 subjectSearch.addEventListener('input',filterSubjects);
 const close=()=>{dropdown.open=false;dropdown.querySelector('summary')!.focus();};
 find('.close-subjects').addEventListener('click',close);
 document.addEventListener('keydown',e=>{if(e.key==='Escape'){if(dropdown.open)close();if(monthPicker.open){monthPicker.open=false;monthPicker.querySelector('summary')!.focus();}}},{signal:lifecycle.signal});
 document.addEventListener('click',e=>{if(!dropdown.contains(e.target as Node))dropdown.open=false;if(!monthPicker.contains(e.target as Node))monthPicker.open=false;},{signal:lifecycle.signal});
 for(const [button,delta] of [[previous,-1],[next,1]] as const)button.addEventListener('click',()=>{page+=delta;render();find('.library-tools').scrollIntoView({block:'start'});});
 find<HTMLElement>('.library-tools').hidden=false;render(false);
}
