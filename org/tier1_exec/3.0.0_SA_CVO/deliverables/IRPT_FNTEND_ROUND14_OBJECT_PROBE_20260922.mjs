// Run with Bun from workspace root. Generator source is unchanged except import relocation
// and interception of filesystem writes; no generated output is written into the portal.
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {pathToFileURL} from 'node:url';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
const root=process.cwd(), portal=resolve(root,'portal');
const out=resolve(root,'.runtime/codex-seats/3.0.0_SA_CVO~F/r14-object');mkdirSync(out,{recursive:true});
const file=resolve(portal,'src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts');
const source=readFileSync(file,'utf8');
let src=source.replace("import { mkdirSync, readFileSync, writeFileSync } from 'node:fs'", "import { readFileSync } from 'node:fs'; const mkdirSync=()=>{}; const writeFileSync=(p,s)=>globalThis.__cvoGenerated.set(p,s);");
if(src===source)throw new Error('write interceptor did not bind');
src=src.replace(/from '(\.\.?\/[^']+)'/g,(_,p)=>`from '${resolve(dirname(file),p).replaceAll('\\','/')}'`).replaceAll('import.meta.url',JSON.stringify(pathToFileURL(file).href));
globalThis.__cvoGenerated=new Map();
const runFile=resolve(out,'generator.instrumented.ts');writeFileSync(runFile,src);
await import(pathToFileURL(runFile).href);
const git=(args)=>execFileSync('git',args,{cwd:portal,encoding:'utf8',maxBuffer:20*1024*1024}).trim();
const result={portal:git(['rev-parse','HEAD']),sourceSHA256:createHash('sha256').update(source).digest('hex'),capturedWrites:globalThis.__cvoGenerated.size,fixtures:[]};
for(const name of ['fe-s-13-wire.json','fe-s-14-print-v1.json','default.json']){
 const path='src/pages/InvestorReporting/fixtures/smoke/'+name;
 const generated=JSON.parse(globalThis.__cvoGenerated.get(resolve(portal,path)));
 const current=JSON.parse(git(['show','HEAD:'+path]));
 const before=JSON.parse(git(['show','467354c9:'+path]));
 const count=v=>({present:Object.values(v).filter(x=>x.unprojected_grant!=null).length,total:Object.keys(v).length});
 result.fixtures.push({path,current:count(current),before:count(before),generatedEqualsCommitted:JSON.stringify(generated)===JSON.stringify(current),baselineDataEqual:JSON.stringify(before)===JSON.stringify(current)});
}
writeFileSync(resolve(out,'result.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));
