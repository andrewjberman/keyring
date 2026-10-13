# NFRA_MCPORTAL task order -- `MP-n-3` -- WORKSTREAM C17 ROUND 2: the producer writes the integrate pointer (E1, writer)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-n-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-n-3</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~18</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the producer already runs from every box-sync pass; no new cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the producer's existing put_object path and prefix; no new grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (non-integrate modes, a raising put).
EGRESS CLASS, declared: none in this cell. Every S3 call in a test is a fake client; the live writes begin when box-sync runs the merged file.
</preflight>

## 1. THE CELL -- `MP-n-3` (workstream C17 round 2, decomposition sections C17R2.1 and C17R2.2)

Your worktree is `C:/tmp/mp-n3-18` (branch `wk-NFRA_MCPORTAL-n3-18`). Work and commit only there.

`.tools/fabric-gitstate.py` (129 lines) runs at the end of every box-sync pass (`.tools/box-sync.sh:72-73`, in the
background, with `--mode "$MODE" --rc "$1"`). It puts one stamped record and `latest.json` per pass under
`s3://opal-313476888478-globgrph/fabric/activity/v1/gitstate/box=<B>/`. The gateway (a parallel cell) will read, per box,
ONE pointer naming the newest integrate pass, instead of walking the window.

**The object** (fixed; do not change its shape):
`<PREFIX>/box=<B>/last_integrate.json`, ASCII JSON with exactly `{"at": "<the record's own 'at'>", "rc": <int, the --rc>,
"note": "<the record's pass note, cut to 200 chars>"}`.

**The writer's owner, `4.0.0_SA_CRO~Z`, consented in writing on five conditions. Build to all of 1-4, verbatim:**
1. **Integrate passes only.** The pointer is written only when `--mode integrate`. A `box`, `manual` or dry pass never
   writes or deletes it.
2. **Same path, no new address.** The key is built in `put()` from the existing `PREFIX` constant and the same `box=<B>`
   segment: `<PREFIX>/box=<B>/last_integrate.json`, the same bucket, the same client. No second bucket, prefix or
   hand-typed key.
3. **The rc is the pass's rc.** `rc` in the pointer is the `--rc` box-sync passed in, never this script's own exit code.
   `at` is the same `now` as the stamped record from that pass, so a reader can join the pointer to its full record.
4. **A failed put fails nothing else.** If the pointer put raises, the LAST line says so (`pointer=no:<ExceptionName>`
   beside `put=`), the two existing keys are still attempted, and box-sync's exit is unchanged (the call is already
   backgrounded). Body ASCII (`ensure_ascii=True`, as today); `note` is the same note the stamped record already carries,
   cut to 200 characters.
(5, not this round: if the CRO's GitOps home lands later, the pointer folds into it.)

On a non-integrate pass the LAST line carries `pointer=n/a`; on an integrate pass `pointer=yes` or `pointer=no:<Exc>`.
Update the module docstring (the RECORD paragraph and the LAST-line spec) to name the pointer and the five conditions'
source (the consent record path below).

Add `.tools/tests/test_fabric_gitstate_pointer.py` (new), offline, with a fake S3 client injected where `put()` builds
its client (patch `boto3.client`), and the git reads stubbed. These four tests, by these exact names:
- `test_pointer_written_on_integrate_only` -- `--mode integrate` puts `last_integrate.json`; `box`, `manual` and
  `--dry-run` put no pointer key.
- `test_pointer_key_uses_prefix_and_box` -- the key equals `PREFIX + "/box=<B>/last_integrate.json"`, the bucket equals
  `BUCKET`, and the same client object made the three puts.
- `test_pointer_rc_and_at_join_the_pass_record` -- with `--rc 3` the pointer's `rc` is 3 (and the script's exit is
  still its own verdict); its `at` equals the stamped record's `at`; a 300-char note is cut to 200; the body is ASCII and
  its keys are exactly `{at, rc, note}`.
- `test_failed_pointer_put_reported_and_others_attempted` -- the fake raises on the pointer key only: both existing
  keys were attempted, the LAST printed line contains `pointer=no:<that exception's class name>` and `put=yes`, and the
  return code equals what it is with no pointer failure.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Change nothing else in the producer (the record, its fields, the two
   existing keys, the CLI). Do not edit `.tools/box-sync.sh` or anything under `infra/`. No AWS call: never run the script
   without `--dry-run` outside a test.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
.tools/fabric-gitstate.py
.tools/tests/test_fabric_gitstate_pointer.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~18/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `.tools/box-sync.sh`, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CONSENT_NFRA_MCPORTAL_C17_E1_LAST_INTEGRATE_POINTER_20261013.md`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17r2/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W18-S<k>` (the next free k for W18). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`. Append a row as ONE whole fenced ```json block.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-n-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17r2/checks/n3.AC1.sh; echo "exit=$?"</invocation><expect>pointer tests: 0 failed; named tests PASSED 4 of 4 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~18/NFRA_MCPORTAL.TO-MP-n-3.integrate-pointer-writer.proof_of_spec.json`.
Report once, with: the check output; the commit hash; the producer diff; the `--dry-run --mode integrate` LAST line; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the C17 round-2 issuance (decomposition v8) from ROUND_ANALYSIS.c17-round1.md E1, under
4.0.0_SA_CRO~Z's written consent (msg 33630, record @b5ce7b2966). Check dry-run at the base: AC1 FAIL (test file absent).
Risk WORLD because the merged file runs on every box at its next box-sync pass. The issuer's close run is the first
integrate pass's pointer read back from S3. No gate.

<status>pending</status>
<round>2</round>
<workstream>C17</workstream>
<slot>~18</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
