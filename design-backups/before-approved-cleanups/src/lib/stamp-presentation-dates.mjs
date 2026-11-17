import fs from 'node:fs';
import path from 'node:path';
const directory=path.resolve('src/content/presentations');
export function stampPresentationDate(file, now=new Date()) {
 const resolved=path.resolve(file);
 if(!resolved.startsWith(directory+path.sep)||!resolved.endsWith('.json')||!fs.existsSync(resolved))return;
 const entry=JSON.parse(fs.readFileSync(resolved,'utf8'));
 if(entry.published)return;
 entry.published=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Singapore',year:'numeric',month:'2-digit',day:'2-digit'}).format(now);
 fs.writeFileSync(resolved,JSON.stringify(entry,null,2)+'\n');
}
export function stampMissingPresentationDates(){
 function visit(dir){for(const entry of fs.readdirSync(dir,{withFileTypes:true})){const file=path.join(dir,entry.name);if(entry.isDirectory())visit(file);else stampPresentationDate(file);}}
 visit(directory);
}
