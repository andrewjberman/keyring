'use strict';
// CVO review only: the issued SAME-MESSAGE / DIFFERENT-TYPE pair.
// Requires explicit source blob. Reads pinned worker harness; no edits to it or source.
// No browser, timer deadline, network, credentials, or real filesystem writes.
const cp = require('node:child_process');
const vm = require('node:vm');
const crypto = require('node:crypto');
const blob = process.argv[2];
if (!blob || !/^[0-9a-f]{7,40}$/.test(blob)) {
  console.error('Usage: node IRPT_BCKEND_R13_TYPED_PAIR_DIAGNOSTIC.cjs <source-git-blob>');
  process.exit(2);
}
const harnessRef = '7ece2be85c:org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/harness_ib_rtm_1.cjs';
const harnessBytes = cp.execFileSync('git', ['show', harnessRef]);
const text = harnessBytes.toString('utf8');
const start = text.indexOf('(async () => {');
if (start < 0) throw new Error('Missing pinned harness runner');
const sourceBytes = cp.execFileSync('git', ['cat-file', 'blob', blob]);
const tail = `(async () => {
  const inputs = [
    ['typed deadline-shaped error', 'TimeoutError', 'Timeout 60000ms exceeded'],
    ['SAME text, plain Error, no deadline fired', 'Error', 'Timeout 60000ms exceeded'],
    ['SAME text, TypeError, no deadline fired', 'TypeError', 'Timeout 60000ms exceeded'],
    ['plain Error, one punctuation change', 'Error', 'Timeout 60000ms exceeded.'],
    ['typed timeout, unrelated message', 'TimeoutError', 'opaque transport failure'],
    ['ordinary certificate error control', 'Error', 'net::ERR_CERT_AUTHORITY_INVALID'],
  ];
  const results = [];
  for (const [name,errorName,errorMessage] of inputs) {
    const r = await runClassify(name,{throwOnce:true,errorName,errorMessage});
    results.push({name,errorName,errorMessage,writes:r.writes,success:r.success,
      verificationCalls:r.verificationCalls,exitCode:r.exitCode,errors:r.errors});
  }
  return results;
})()`;
(async () => {
  const results = await vm.runInNewContext(text.slice(0,start)+'\n'+tail, {
    require, URL, Buffer, console, process:{argv:['node',__filename,blob]},
  });
  const accepts = r => r.success && r.writes===1 && r.verificationCalls===2;
  const refuses = r => !r.success && r.writes===0 && r.verificationCalls===1 && r.exitCode===1;
  const typeOnlyPairFails = accepts(results[0]) && accepts(results[1]) && accepts(results[2]) &&
    refuses(results[3]) && accepts(results[4]) && refuses(results[5]);
  console.log(JSON.stringify({blob,sourceSha256:crypto.createHash('sha256').update(sourceBytes).digest('hex'),
    harnessRef,harnessSha256:crypto.createHash('sha256').update(harnessBytes).digest('hex'),
    scope:'Immediate mocked rejection, no timer/deadline fired; tests the issued type predicate, not a live incident',
    typeOnlyPairFails,results},null,2));
  process.exitCode = typeOnlyPairFails ? 0 : 1; // zero = counterexample reproduced, NOT approval
})().catch(e => {console.error(e);process.exitCode=2;});
