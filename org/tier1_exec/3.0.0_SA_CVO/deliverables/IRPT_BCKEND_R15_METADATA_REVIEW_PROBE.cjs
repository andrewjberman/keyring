'use strict';
// CVO verification only: no worker edits, browser, cloud, credentials or session IO.
// The worker battery makes/removes its own isolated scratch checkout for each arm.
const cp = require('node:child_process');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const home = 'org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/';
const git = (...args) => cp.execFileSync('git', args);
const blob = ref => git('cat-file', 'blob', ref);
const proofPath = home + 'IRPT_BCKEND.TO-IB-rto-1.the-c-s174-metadata-recomputed-not-copied.proof_of_spec.json';
const proof = JSON.parse(blob('HEAD:' + proofPath));
assert.equal(proof.acceptance.length, 2);
assert.ok(proof.acceptance.every(row => !row.judgment));
for (const item of proof.artifacts_produced) {
  assert.equal(git('cat-file', '-t', item.commit_or_etag).toString().trim(), 'blob');
  assert.equal(git('rev-parse', 'HEAD:' + item.path_or_key).toString().trim(), item.commit_or_etag);
}
assert.equal(proof.artifacts_produced.length, 6);
const historical = blob('ded605028b2210b589735927868aacf92ceb852d');
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const lf = sha(historical);
const crlf = sha(Buffer.from(historical.toString().replace(/\r?\n/g, '\r\n')));
const diagnostic = JSON.parse(blob('HEAD:' + home + 'IB-rtk-1_repaired_r10_lifecycle_diagnostic.json'));
assert.equal(crlf, diagnostic.sourceSha256);
const rtk = JSON.parse(blob('HEAD:' + home + 'IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json'));
assert.ok(rtk.artifacts_produced[0].deploy_evidence.includes('PUBLISHED in a later pass'));
assert.ok(rtk.declared_exclusions.some(e => e.item.includes('any real host/SSM/S3 action')));
console.log('C174-RESIDUAL: publication recorded alongside an unqualified real-S3-action exclusion');
console.log(JSON.stringify({ proofBlob: git('rev-parse', 'HEAD:' + proofPath).toString().trim(),
  pins: '6/6 current blobs', lf, crlf, diagnosticHash: diagnostic.sourceSha256 }));
const program = `
import contextlib, io, json, os, subprocess
path = ${JSON.stringify(home + 'battery_ib_rtm_1.py')}
source = subprocess.check_output(['git', 'show', 'HEAD:' + path]).decode('utf-8')
space = {'__name__': 'cvo_verification', '__file__': os.path.abspath(path)}
exec(compile(source, path, 'exec'), space)
original_load = space['load']
lf = ${JSON.stringify(lf)}
crlf = ${JSON.stringify(crlf)}
cases = [('correct', None, None, 0),
         ('wrong-crlf', crlf, crlf.replace('03bfb20', '03fbb20'), 1),
         ('wrong-lf', lf, ('0' if lf[0] != '0' else '1') + lf[1:], 1)]
for name, before, after, expected in cases:
    def load(path, before=before, after=after):
        value = original_load(path)
        if path == space['IB_RTK_1_PROOF'] and before is not None:
            old = value['controls']['mutant']['observed']
            assert before in old
            value['controls']['mutant']['observed'] = old.replace(before, after)
        return value
    space['load'] = load
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        actual = space['arm_metadata']()
    text = output.getvalue()
    print(json.dumps({'case': name, 'rc': actual, 'expected': expected,
        'output': text}))
    assert actual == expected, name
    if expected:
        assert 'IBR115-C174-RECOMPUTED-NO-TRANSPOSITION-NO-MISATTRIBUTION' not in text
        assert 'FAIL: metadata arm' in text
    else:
        assert 'IBR115-C174-RECOMPUTED-NO-TRANSPOSITION-NO-MISATTRIBUTION' in text
print('R15-CVO-METADATA-CONTROLS-3-OF-3-PASS')
`;
process.stdout.write(cp.execFileSync('py', ['-3.12', '-B', '-c', program],
  { encoding: 'utf8', timeout: 180000, maxBuffer: 4 * 1024 * 1024 }));
