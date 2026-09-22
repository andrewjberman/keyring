'use strict';
// Review-only VM extensions of the committed R11 and R12 mock harnesses.
// No production source edits, real browser, network, credential or filesystem writes.
// A simulated failure is a counterexample to the predicate, NOT a live incident.
const fs = require('node:fs');
const vm = require('node:vm');
const cp = require('node:child_process');
const crypto = require('node:crypto');
const blob = process.argv[2] || '82abe68499ab1d5422f6f73979c3f5b72ed4c583';
const oldHarness = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs';
const atomicHarness = 'org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/harness_ib_rtl_1.cjs';
function once(text, needle, replacement) {
  if (text.split(needle).length !== 2) throw new Error('Harness extension anchor is not unique: ' + needle);
  return text.replace(needle, replacement);
}
function prefix(path) {
  const text = fs.readFileSync(path, 'utf8');
  const at = text.indexOf('(async () => {');
  if (at < 0) throw new Error('Missing harness runner');
  return text.slice(0, at);
}
async function execute(text, tail) {
  // The harness's own fs reads source bytes; the CAPTURE SOURCE only receives its mocked fs.
  const context = { require, URL, Buffer, console, process: { argv: ['node', __filename, blob] } };
  return vm.runInNewContext(text + '\n' + tail, context);
}
(async () => {
  let retry = prefix(oldHarness);
  retry = once(retry,
    "if (out.verificationCalls === 1 && cfg.firstFailure === 'generic') throw new Error('net::ERR_CERT_AUTHORITY_INVALID');",
    "if (out.verificationCalls === 1 && cfg.firstFailure === 'generic') throw new Error(cfg.errorText || 'net::ERR_CERT_AUTHORITY_INVALID');");
  retry = once(retry, "IRPT_CAPTURE_PORTAL_ORIGIN: origin, IRPT_CAPTURE_INSTANCE_ID:",
    "IRPT_CAPTURE_PORTAL_ORIGIN: origin, IRPT_CAPTURE_CHECK_ROUTE: cfg.checkRoute || '/investor-reporting/print', IRPT_CAPTURE_INSTANCE_ID:");
  const retries = await execute(retry, `(async () => {
    const a = await run('non-timeout certificate error, ordinary URL text', {firstFailure:'generic', errorText:'page.goto: net::ERR_CERT_AUTHORITY_INVALID at https://opalinvest.dev/investor-reporting/print'});
    const b = await run('same non-timeout certificate error, timeout substring in URL text', {firstFailure:'generic', checkRoute:'/investor-reporting/print?timeout=1', errorText:'page.goto: net::ERR_CERT_AUTHORITY_INVALID at https://opalinvest.dev/investor-reporting/print?timeout=1'});
    const c = await run('actual timeout positive control', {firstFailure:'timeout'});
    const d = await run('HTTP404 terminal control', {firstStatus:404});
    return [a,b,c,d];
  })()`);
  let atomic = prefix(atomicHarness);
  atomic = once(atomic,
    'unlinkSync(p) { out.unlinks++; disk.delete(p); out.deleted = true; },',
    "unlinkSync(p) { out.unlinks++; if (cfg.unlinkFails) { const e = new Error('EPERM: simulated unlink failure'); e.code = 'EPERM'; throw e; } disk.delete(p); out.deleted = true; },");
  const cleanups = await execute(atomic, `(async () => {
    return [await run('clean rename positive control', {hopOnRename:false}),
      await run('latched rename, deletion succeeds', {hopOnRename:true}),
      await run('same latched rename, deletion fails EPERM', {hopOnRename:true, unlinkFails:true})];
  })()`);
  const taxonomyCounterexample = retries[0].verificationCalls === 1 && retries[0].writes === 0 &&
    retries[1].verificationCalls === 2 && retries[1].writes === 1 && retries[1].success &&
    retries[2].verificationCalls === 2 && retries[2].success && retries[3].verificationCalls === 1 && retries[3].writes === 0;
  const cleanupCounterexample = cleanups[0].success && cleanups[0].diskFinal &&
    !cleanups[1].success && cleanups[1].deleted && !cleanups[1].diskFinal &&
    !cleanups[2].success && cleanups[2].exitCode === 1 && cleanups[2].diskFinal && !cleanups[2].deleted &&
    cleanups[2].errors.includes('was deleted');
  const slim = r => ({name:r.name, writes:r.writes, success:r.success, exitCode:r.exitCode,
    verificationCalls:r.verificationCalls, renames:r.renames, unlinks:r.unlinks,
    deleted:r.deleted, diskFinal:r.diskFinal, errors:r.errors});
  const result = {blob, sourceSha256:crypto.createHash('sha256').update(cp.execFileSync('git',['cat-file','blob',blob])).digest('hex'),
    scope:'mocked counterexamples; no real error occurrence or host execution claimed',
    taxonomyCounterexample, cleanupCounterexample, retries:retries.map(slim), cleanups:cleanups.map(slim)};
  console.log(JSON.stringify(result,null,2));
  process.exitCode = taxonomyCounterexample && cleanupCounterexample ? 0 : 1;
})().catch(e => {console.error(e); process.exitCode=2;});
