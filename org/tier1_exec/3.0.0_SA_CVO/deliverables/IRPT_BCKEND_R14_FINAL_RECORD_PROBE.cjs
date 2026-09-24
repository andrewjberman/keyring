'use strict';
// Read-only R14 final-record reconciliation; no browser, cloud or session-file IO.
const assert = require('node:assert/strict');
const cp = require('node:child_process');
const crypto = require('node:crypto');
const root = 'org/missions/D9/IRPT/IRPT_BCKEND/';
const home = root + 'deliverables/0.9.0_WK_IRPT_BCKEND~13/';
const finalPath = home + 'IRPT_BCKEND.TO-IB-rtn-1.the-capture-tool-timeout-by-type-or-deadline-state-only.proof_of_spec.json';
const git = (...args) => cp.execFileSync('git', args);
const object = ref => git('cat-file', 'blob', ref);
const read = path => object('HEAD:' + path);
const json = path => JSON.parse(read(path));
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const proof = json(finalPath);
const prior = JSON.parse(object('32bfd035de:' + finalPath));
assert.deepEqual(proof.acceptance, prior.acceptance);
for (const artifact of proof.artifacts_produced) {
  const ref = artifact.commit_or_etag;
  assert.equal(git('cat-file', '-t', ref).toString().trim(), 'blob');
  assert.equal(git('rev-parse', 'HEAD:' + artifact.path_or_key).toString().trim(), ref);
}
assert.equal(proof.artifacts_produced.length, 11);
assert.equal(sha(read('infra/aws/ec2/investor-reporting-export/capture-session.cjs')),
  'ea437510ee96fdf7fd106ff36dff3dead1aaf8ada94458a62556bae210cdc25a');
const oldProof = json(home + 'IRPT_BCKEND.TO-IB-rtm-1.the-capture-tool-typed-error-classification-and-truthful-cleanup-report.proof_of_spec.json');
const oldResult = oldProof.artifacts_produced.find(a => a.path_or_key.endsWith('.result.md'));
assert.equal(oldResult.commit_or_etag, 'af259448fd8f1eb4d118fa4e7e9b95a7eb1c04ce');
assert.equal(git('rev-parse', 'HEAD:' + oldResult.path_or_key).toString().trim(), oldResult.commit_or_etag);
const historical = object('ded605028b2210b589735927868aacf92ceb852d');
const lfHash = sha(historical);
const crlfHash = sha(Buffer.from(historical.toString().replace(/\r?\n/g, '\r\n')));
const diagnostic = json(home + 'IB-rtk-1_repaired_r10_lifecycle_diagnostic.json');
const rtk = json(home + 'IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json');
const battery = read(home + 'battery_ib_rtm_1.py').toString();
const expectedCRLF = battery.match(/CRLF_VALUE = "([a-f0-9]{64})"/)[1];
assert.equal(diagnostic.sourceSha256, crlfHash);
assert.notEqual(expectedCRLF, crlfHash);
assert.ok(rtk.controls.mutant.observed.includes(expectedCRLF));
assert.ok(!rtk.controls.mutant.observed.includes(crlfHash));
assert.ok(rtk.controls.mutant.observed.includes('sourceSha256 ' + lfHash));
console.log(JSON.stringify({
  finalProofBlob: git('rev-parse', 'HEAD:' + finalPath).toString().trim(),
  artifactPins: '11/11 resolve as blobs and equal current path blobs',
  acceptanceUnchangedFromC195: true,
  C194FinalResultPin: oldResult.commit_or_etag,
  C174: { lfHash, crlfHash, diagnosticHash: diagnostic.sourceSha256, expectedCRLF,
    verdict: 'STILL OPEN: shared wrong full-hash oracle and misattributed diagnostic hash' }
}, null, 2));
console.log('R14-FINAL-RECORD-RECONCILED; C174-RESIDUAL-CONFIRMED');
