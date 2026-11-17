import fs from 'node:fs';
import path from 'node:path';
const root=path.resolve('dist');
function visit(dir){for(const item of fs.readdirSync(dir,{withFileTypes:true})){if(!item.isDirectory())continue;const full=path.join(dir,item.name);if(item.name.endsWith('.html')){const children=fs.readdirSync(full);if(children.length!==1||children[0]!=='index.html')throw Error('Unexpected output structure: '+full);const temp=full+'.route-tmp';fs.renameSync(full,temp);fs.renameSync(path.join(temp,'index.html'),full);fs.rmdirSync(temp);}else visit(full);}}
visit(root);
console.log('Preserved legacy .html file URLs.');
