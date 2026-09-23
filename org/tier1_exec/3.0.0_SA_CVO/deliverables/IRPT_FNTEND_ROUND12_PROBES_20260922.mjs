// Read-only CVO evidence. Run from workspace root: node <this file>.
// Supplied computed-style records exercise production functions; no browser claim.
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
const git=(...args)=>execFileSync('git',args,{encoding:'utf8'}).trim();
const base='org/missions/D9/IRPT/IRPT_FNTEND';
const fence=String.fromCharCode(96).repeat(3);
const rows=p=>[...fs.readFileSync(p,'utf8').matchAll(new RegExp('^'+fence+'json\\s*\\r?\\n([\\s\\S]*?)^'+fence,'gm'))].flatMap(x=>JSON.parse(x[1]));
const proofs=[];
for(let n=74;n<=79;n++) {
 const dir=`${base}/deliverables/0.9.0_WK_IRPT_FNTEND~${n-50}`;
 const path=dir+'/'+fs.readdirSync(dir).find(x=>x.includes(`TO-FE-s-${n}.`)&&x.endsWith('.proof_of_spec.json'));
 const proof=JSON.parse(fs.readFileSync(path,'utf8'));
 for(const a of proof.artifacts_produced??[]) {
  if(a.path_or_key.startsWith('portal/')&&/^[a-f0-9]{7,40}$/.test(a.commit_or_etag))
   for(const path of a.path_or_key.split(', ')) git('-C','portal','cat-file','-e',`${a.commit_or_etag}:${path.slice(7)}`);
 }
 proofs.push({n,path,pin:git('log','-1','--format=%H','--',path)});
}
if(process.argv.includes('--carrier-data')) {
 console.log(JSON.stringify({proofs,rem:rows(base+'/surprise-channel/remediations/REMEDIATION_v8.md'),inv:rows(base+'/surprise-channel/investigations/INVESTIGATION_v2.md').filter(x=>/^IRPT_FNTEND-W(24|25|27|28|29)-S/.test(x.id))}));
 process.exit(0);
}
const source=git('-C','portal','show','2d7b2f21043bc6964546f6a80869f313f9b2ebeb:scripts/ui-smoke.mjs');
const old=git('-C','portal','show','5c8a9ba9c264218e3edcd3649d4270f549e98172:scripts/ui-smoke.mjs');
const white={backgroundColor:'rgb(255, 255, 255)',backgroundImage:'none',parentElement:null};
const paints=[['white',white,'ok'],['gradient',{backgroundColor:'rgba(0, 0, 0, 0)',backgroundImage:'linear-gradient(black, navy)',parentElement:white},'unmeasurable'],['oklch',{backgroundColor:'oklch(0.279 0.041 260.031)',backgroundImage:'none',parentElement:white},'unmeasurable'],['absent',null,'absent']];
for(const [name,element,state] of paints) {
 const read=async text=>{
  const fragment=text.slice(text.indexOf('const groundColor ='),text.indexOf('const contentResults ='));
  const ctx=vm.createContext({document:{querySelector:()=>element},getComputedStyle:x=>x,page:{evaluate:fn=>fn('selector')}});
  return vm.runInContext(fragment+'groundColor("selector")',ctx);
 };
 const before=await read(old),after=await read(source);
 assert.equal(after.state,state);
 assert.equal(before,element===null?null:'rgb(255, 255, 255)');
 console.log('GROUND',name,JSON.stringify({before,after}));
}
for(const text of [old,source]) {
 const logs=[];
 const fragment=text.slice(text.indexOf('const firstComputedStyle ='),text.indexOf('// Ground ='));
 const loop=text.slice(text.indexOf('const styleResults ='),text.indexOf('const groundResults ='));
 const context={document:{querySelector:()=>null},page:{evaluate:(fn,arg)=>fn(arg)},expectStyleArgs:['[absent]::color!=rgb(95, 59, 227)'],console:{log:x=>logs.push(x)}};
 const flagged=await vm.runInNewContext('(async()=>{let anyUnmeasurable=false;'+fragment+loop+'return anyUnmeasurable})()',context);
 assert(logs[0].includes(text===old?'PASS null':'UNMEASURABLE'));
 assert.equal(flagged,text===source);
 console.log('ABSENT-INEQUALITY',text===old?'before':'after',logs[0],'nonzero flag',flagged);
}
assert(source.includes('if (anyUnmeasurable) process.exitCode = 1'));
const keyFragment=source.slice(source.indexOf('const routeKeyCandidates ='),source.indexOf('// --fail <url-substring>'));
const keyCheck=vm.runInNewContext(keyFragment+'checkKeyValidity', {readFileSync:p=>fs.readFileSync('portal/'+p,'utf8')});
const fixturePath='src/pages/InvestorReporting/fixtures/smoke/default.json';
const fixtures=JSON.parse(fs.readFileSync('portal/'+fixturePath,'utf8'));
assert.equal(keyCheck(['/api/'],fixturePath).valid,0);
const good=keyCheck(Object.keys(fixtures),fixturePath);
assert.deepEqual(JSON.parse(JSON.stringify(good)),{valid:5,total:12});
console.log('KEY-VALIDITY',JSON.stringify(good),'invalid /api/ = 0 of 1; static-prefix grammar, not runtime fulfilment');
console.log('DEFAULT-KEY-DETAIL',Object.keys(fixtures).map(k=>[k,keyCheck([k],fixturePath).valid]));
for(const name of ['default.json','fe-s-13-wire.json','fe-s-14-print-v1.json']) {
 const f=JSON.parse(fs.readFileSync('portal/src/pages/InvestorReporting/fixtures/smoke/'+name,'utf8'));
 console.log('UNPROJECTED-GRANT',name,'missing',Object.values(f).filter(x=>!Object.hasOwn(x,'unprojected_grant')).length,'of',Object.keys(f).length);
}
const luminance=rgb=>rgb.map(x=>x/255).map(x=>x<=0.04045?x/12.92:((x+0.055)/1.055)**2.4).reduce((n,x,i)=>n+x*[0.2126,0.7152,0.0722][i],0);
for(const rgb of [[107,114,128],[22,51,114]]) console.log('CONTRAST-ON-WHITE',rgb.join(','),(1.05/(luminance(rgb)+0.05)).toFixed(2));
console.log('PROOF-ARTIFACT-PINS: all declared portal path@commit objects resolve across six instances');
console.log('PORTAL-PIN',git('-C','portal','rev-parse','HEAD'));
if(process.argv.includes('--validate-carriers')) {
 const adj=rows(base+'/surprise-channel/adjudications/ADJUDICATION_v4.md');
 const rem=rows(base+'/surprise-channel/remediations/REMEDIATION_v9.md');
 const prior=rows(base+'/surprise-channel/remediations/REMEDIATION_v8.md');
 assert.equal(adj.length,14);assert.equal(rem.length,12);
 assert.equal(adj.flatMap(x=>x.adjudicates??[]).length,10);
 assert.equal(adj.flatMap(x=>x.grades??[]).length,6);
 assert.equal(rem.filter(x=>!x.closed).length,5);
 assert.equal(prior.filter(x=>!x.closed).length,4);
 const batches=[
  {schema:JSON.parse(fs.readFileSync('org/surprise_channel/schemas/investigation_item.schema.json','utf8')),rows:adj},
  {schema:JSON.parse(fs.readFileSync('org/surprise_channel/schemas/remediation_row.schema.json','utf8')),rows:[...rem,...prior]},
 ];
 console.log(execFileSync('python',['-c','import json,sys,jsonschema; b=json.load(sys.stdin); [jsonschema.Draft7Validator(x["schema"]).validate(r) for x in b for r in x["rows"]]; print("SCHEMA PASS: 14 new adjudications, 12 new plus 18 existing remediations")'],{input:JSON.stringify(batches),encoding:'utf8'}).trim());
}
console.log('PASS: bounded production-function and artifact probes; no browser rerender or live backend claim');
