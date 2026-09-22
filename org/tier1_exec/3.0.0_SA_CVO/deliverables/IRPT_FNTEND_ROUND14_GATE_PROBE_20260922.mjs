// Run with Bun from workspace. Lift the exact F49-AC8 hunk comparator, vary input text only.
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {resolve} from 'node:path';
const portal=resolve('portal'),out=resolve('.runtime/codex-seats/3.0.0_SA_CVO~F/r14-gate');mkdirSync(out,{recursive:true});
const git=(...args)=>execFileSync('git',args,{cwd:portal,encoding:'utf8'});
const code=readFileSync(resolve(portal,'src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts'),'utf8');
const start=code.indexOf('const SANCTIONED_ADDITIONS:'),end=code.indexOf('    const carried = unrelated.filter',start);
if(start<0||end<0)throw Error('Comparator extraction failed');
const js=new Bun.Transpiler({loader:'ts'}).transformSync(code.slice(start,end)+'\nreturn identical;');
const comparator=new Function('headLines','gateHunks','RENDERING','ROUTE',js);
const hunks=[];
for(const l of git('show','--format=','c29a8b86','--','src/App.tsx').split('\n')){
 if(l.startsWith('@@'))hunks.push({plus:[],minus:[]});
 else if(hunks.length&&l.startsWith('+')&&!l.startsWith('+++'))hunks.at(-1).plus.push(l.slice(1));
 else if(hunks.length&&l.startsWith('-')&&!l.startsWith('---'))hunks.at(-1).minus.push(l.slice(1));
}
const gateHunks=hunks.filter(h=>h.plus.some(p=>p.includes('/investor-reporting'))),app=git('show','HEAD:src/App.tsx');
const modify=(change)=>app.split('\n').map(l=>l.includes('path="/investor-reporting/print"')?change(l):l);
const cases={current:app.split('\n'),removeInternal:modify(l=>l.replace(' requireInternal','')),removeAdmin:modify(l=>l.replace(' requireAdmin','')),internalFalse:modify(l=>l.replace(' requireInternal',' requireInternal={false}')),adminFalse:modify(l=>l.replace(' requireAdmin',' requireAdmin={false}'))};
const results=[];
for(const [name,lines] of Object.entries(cases)){
 console.log('CASE',name);results.push({name,comparatorMatches:comparator(lines,gateHunks,'c29a8b86','/investor-reporting'),hunks:gateHunks.length});
}
writeFileSync(resolve(out,'result.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results,null,2));
