// Run from workspace. Evaluate actual production function bytes against real and synthetic tables.
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {resolve} from 'node:path';
const root=process.cwd(),portal=resolve(root,'portal'),out=resolve(root,'.runtime/codex-seats/3.0.0_SA_CVO~F/r14-classifier');mkdirSync(out,{recursive:true});
const src=readFileSync(resolve(portal,'scripts/ui-smoke.mjs'),'utf8');
const from=src.indexOf('const routeKeyCandidates = routeKeys => {'),to=src.indexOf('// --fail <url-substring>',from);
if(from<0||to<0)throw Error('Extraction boundary missing');
const make=read=>new Function('readFileSync',src.slice(from,to)+'\nreturn checkKeyValidity;')(read);
const read=(p)=>readFileSync(resolve(portal,p),'utf8'),fn=make(read);
const reference='src/pages/InvestorReporting/fixtures/smoke/default.json';
const keys=['/api/scoped/investor-reporting/holdings/A-0001','/api/scoped/investor-reporting/holdings/A-0001/not-a-declared-operation','/api/scoped/investor-reporting/status/REQ-1','/api/scoped/investor-reporting/holdings/'];
const results={controls:keys.map(key=>({key,...fn([key],reference)})),staticSuffix:make(()=>"export const WIRE_CONSUMED_ROUTE_KEYS = ['GET /api/scoped/investor-reporting/status'];")(['/api/scoped/investor-reporting/status/extra-junk'],reference),fixtures:[]};
for(const file of [reference,'src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json','src/pages/InvestorReporting/__tests__/fe-s-84/fixtures/reporting-qualified.json','src/pages/InvestorReporting/fixtures/smoke/fe-s-13-wire.json','src/pages/InvestorReporting/fixtures/smoke/fe-s-14-print-v1.json']){
 const entries=Object.keys(JSON.parse(read(file)));
 results.fixtures.push({file,...fn(entries,file),invalid:entries.filter(k=>fn([k],file).valid===0)});
}
const before=execFileSync('git',['show','467354c9:scripts/ui-smoke.mjs'],{cwd:portal,encoding:'utf8'});
const bStart=before.indexOf('const routeKeyCandidates = routeKeys => {'),bEnd=before.indexOf('// --fail <url-substring>',bStart);
const beforeFn=new Function('readFileSync',before.slice(bStart,bEnd)+'\nreturn checkKeyValidity;')(read);
results.before=results.fixtures.map(x=>({file:x.file,...beforeFn(Object.keys(JSON.parse(read(x.file))),x.file)}));
writeFileSync(resolve(out,'result.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results,null,2));
