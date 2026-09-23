// Read-only CVO probes. Run from workspace root with node. No browser/network/write.
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
const source=fs.readFileSync('portal/scripts/ui-smoke.mjs','utf8');
const ground=source.slice(source.indexOf('const groundColor ='),source.indexOf('const contentResults ='));
assert(ground.startsWith('const groundColor =') && ground.includes('backgroundColor'));
const white={backgroundColor:'rgb(255, 255, 255)',backgroundImage:'none',parentElement:null};
const dark={backgroundColor:'rgba(0, 0, 0, 0)',backgroundImage:'linear-gradient(rgb(8, 19, 43), rgb(21, 37, 81))',parentElement:white};
const oklch={backgroundColor:'oklch(0.279 0.041 260.031)',backgroundImage:'none',parentElement:white};
for (const [label,element] of [['white',white],['dark-gradient',dark],['opaque-oklch',oklch],['absent',null]]) {
 const ctx=vm.createContext({document:{querySelector:()=>element},getComputedStyle:x=>x,page:{evaluate:fn=>fn('selector')}});
 const result=await vm.runInContext(ground+'groundColor("selector")',ctx);
 assert.equal(result,element===null?null:'rgb(255, 255, 255)');
 console.log('PRODUCTION-GROUND',label,JSON.stringify(result));
}
const styleRead=source.slice(source.indexOf('const firstComputedStyle ='),source.indexOf('// Ground ='));
const styleLoop=source.slice(source.indexOf('const styleResults ='),source.indexOf('const groundResults ='));
const logs=[];
const ctx=vm.createContext({document:{querySelector:()=>null},page:{evaluate:(fn,arg)=>fn(arg)},getComputedStyle:()=>{throw Error('absent element should not be styled');},expectStyleArgs:['[no-such-element]::background-color!=rgb(95, 59, 227)'],console:{log:x=>logs.push(x)}});
await vm.runInContext('(async()=>{'+styleRead+styleLoop+'})()',ctx);
assert(logs[0].includes('PASS null'));
console.log('PRODUCTION-STYLE-MISSING',logs[0]);
// Isolate the production matcher by its actual closing brace rather than copying its logic.
const matchDecl=/const matchFixture = url => \{[\s\S]*?\n\}/.exec(source)?.[0];
assert(matchDecl);
const hits={'/api/':new Set()};
const matched=vm.runInNewContext(matchDecl+'; matchFixture("http://localhost/api/scoped/investor-reporting/directory/resolve")',{fixtureKeys:['/api/'],fixtureHits:hits});
assert.equal(matched,'/api/');
assert.equal(hits['/api/'].size,1);
console.log('PRODUCTION-WIRE-MATCH broad non-contract key /api/ matched 1 of 1; hit counting is not contract-key validation');
const fixture=JSON.parse(fs.readFileSync('portal/src/pages/InvestorReporting/fixtures/smoke/default.json','utf8'));
console.log('DEFAULT-FIXTURE missing unprojected_grant',Object.values(fixture).filter(x=>!Object.hasOwn(x,'unprojected_grant')).length,'of',Object.keys(fixture).length);
const base='org/missions/D9/IRPT/IRPT_FNTEND';
const fence=String.fromCharCode(96).repeat(3);
const rows=p=>[...fs.readFileSync(p,'utf8').matchAll(new RegExp('^'+fence+'json\\s*\\r?\\n([\\s\\S]*?)^'+fence,'gm'))].flatMap(x=>JSON.parse(x[1]));
const inv=rows(base+'/surprise-channel/investigations/INVESTIGATION_v2.md');
console.log('ROW-PRESENCE',inv.filter(x=>/^IRPT_FNTEND-(S70|W(1[5-9]|2[0-3])-S[0-9]+)$/.test(x.id)).map(x=>x.id).join(','));
console.log('PORTAL-PIN',execFileSync('git',['-C','portal','rev-parse','HEAD'],{encoding:'utf8'}).trim());
const adjPath=base+'/surprise-channel/adjudications/ADJUDICATION_v3.md';
const priorText=execFileSync('git',['show','d20200b92c:'+adjPath],{encoding:'utf8'});
const parseText=t=>[...t.matchAll(new RegExp('^'+fence+'json\\s*\\r?\\n([\\s\\S]*?)^'+fence,'gm'))].flatMap(x=>JSON.parse(x[1]));
const prior=parseText(priorText), current=rows(adjPath);
assert.deepEqual(current.slice(0,prior.length),prior);
const added=current.slice(prior.length);
assert.equal(added.length,21);
assert.equal(new Set(current.map(x=>x.id)).size,current.length);
const targets=added.flatMap(x=>x.adjudicates??[]);
assert.equal(targets.length,14);
assert.equal(new Set(targets).size,14);
for(const id of targets) assert(inv.some(x=>x.id===id));
const grades=added.flatMap(x=>x.grades??[]);
assert.equal(grades.length,9);
assert.equal(grades.filter(x=>x.verdict==='FAIL').length,2);
const rem=rows(base+'/surprise-channel/remediations/REMEDIATION_v8.md');
assert.equal(rem.length,18);
assert.equal(rem.filter(x=>!x.closed).length,12);
const checks=[
 {schema:JSON.parse(fs.readFileSync('org/surprise_channel/schemas/investigation_item.schema.json','utf8')),rows:added},
 {schema:JSON.parse(fs.readFileSync('org/surprise_channel/schemas/remediation_row.schema.json','utf8')),rows:rem},
];
const result=execFileSync('python',['-c','import json,sys,jsonschema; batches=json.load(sys.stdin); [jsonschema.Draft7Validator(b["schema"]).validate(r) for b in batches for r in b["rows"]]; print("SCHEMA PASS")'],{input:JSON.stringify(checks),encoding:'utf8'});
console.log(result.trim());
console.log('CARRIER-CHECK preserved',prior.length,'old rows; added',added.length,'rows; 14 targets; 9 grades; 18 remedies (12 open)');
console.log('PROBES PASSED (instrument functions exercised with supplied computed-style records; not a browser render)');
