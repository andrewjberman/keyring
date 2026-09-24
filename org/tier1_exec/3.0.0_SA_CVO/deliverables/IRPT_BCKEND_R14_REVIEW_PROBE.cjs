'use strict';
// CVO bounded review: immutable git blobs, unmodified historical diagnostics, no live host.
const cp=require('node:child_process');
const assert=require('node:assert/strict');
const crypto=require('node:crypto');
const before='058ba2f8f86328d73f2aca140b8a6c81fe0ad3ae';
const after='17aff45ed837a3a6e62fb2ce0410075b62a499dd';
const dir='org/tier1_exec/3.0.0_SA_CVO/deliverables/';
function run(file,blob){
 const p=cp.spawnSync('node',[file,blob],{encoding:'utf8',timeout:60000});
 if(p.error)throw p.error;
 assert(p.status===0||p.status===1, p.stderr);
 return {rc:p.status,data:JSON.parse(p.stdout)};
}
const sources={};
for(const b of [before,after]){
 const bytes=cp.execFileSync('git',['cat-file','blob',b]);
 sources[b]=crypto.createHash('sha256').update(bytes).digest('hex');
}
assert.equal(sources[after],'ea437510ee96fdf7fd106ff36dff3dead1aaf8ada94458a62556bae210cdc25a');
const pairs={};
for(const [round,file] of Object.entries({
 R13:'IRPT_BCKEND_R13_TYPED_PAIR_DIAGNOSTIC.cjs',
 R12:'IRPT_BCKEND_R12_CAPTURE_FAILURE_DIAGNOSTIC.cjs',
 R11:'IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs',
 R10:'IRPT_BCKEND_R10_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs',
 R9:'IRPT_BCKEND_R9_CAPTURE_REDIRECT_DIAGNOSTIC.cjs',
 R8:'IRPT_BCKEND_R8_CAPTURE_DIAGNOSTIC.cjs'})){
 pairs[round]={before:run(dir+file,before),after:run(dir+file,after)};
}
const r13=pairs.R13;
assert.equal(r13.before.data.typeOnlyPairFails,true);
assert.equal(r13.after.data.typeOnlyPairFails,false);
assert.equal(r13.after.data.results.length,6);
for(const [i,r] of r13.after.data.results.entries()){
 const accept=i===0||i===4;
 assert.equal(r.success,accept);assert.equal(r.writes,accept?1:0);
 assert.equal(r.verificationCalls,accept?2:1);
 if(!accept)assert.equal(r.exitCode,1);
}
const changes={};
for(const round of ['R12','R11','R10','R9','R8']){
 const a=pairs[round].before.data,b=pairs[round].after.data;
 const key=round==='R12'?'retries':'results';
 assert.equal(a[key].length,b[key].length);
 assert.deepEqual(a[key].map(x=>x.name),b[key].map(x=>x.name));
 const delta=[];
 for(let i=0;i<a[key].length;i++)if(JSON.stringify(a[key][i])!==JSON.stringify(b[key][i]))delta.push({name:a[key][i].name,before:a[key][i],after:b[key][i]});
 changes[round]={total:a[key].length,changed:delta};
 if(round==='R12'||round==='R11'){
  assert.equal(delta.length,1);
  assert.equal(delta[0].name,round==='R12'?'actual timeout positive control':'same-origin timeout then clean');
  assert.equal(delta[0].before.success,true);assert.equal(delta[0].after.success,false);assert.equal(delta[0].after.writes,0);
 }else assert.equal(delta.length,0);
 if(round==='R12')assert.deepEqual(a.cleanups,b.cleanups);
}
const fixture='org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/fixture_ib_rtn_1_typed_timeout_v1.cjs';
const timed={before:run(fixture,before),after:run(fixture,after)};
assert.equal(timed.after.data.pairOk,true);
assert.equal(timed.after.data.good.realTimerFired,true);
assert.equal(timed.after.data.bad.realTimerFired,true);
console.log(JSON.stringify({sources,scope:'fresh before/after stub runs; no publish or live host/capture',R13:pairs.R13,changes,timed},null,2));
console.log('R14-CVO-PROBE-PASS');
