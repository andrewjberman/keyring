# NFRA_MCPORTAL task order -- `MP-n-2` -- WORKSTREAM C17 ROUND 2: the gateway reads the integrate pointer (E1, reader)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-n-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-n-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~17</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; read when opened.
comp-iam: DECLARED-NOT-APPLICABLE -- the gateway already holds s3:GetObject on fabric/activity/v1/* (MP-x-3); the pointer sits under that prefix.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (absent pointer, rc 0, rc non-zero, fetch count at 10x history).
EGRESS CLASS, declared: none. Every store read in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-n-2` (workstream C17 round 2, decomposition sections C17R2.1 and C17R2.2)

Your worktree is `C:/tmp/mp-n2-17` (branch `wk-NFRA_MCPORTAL-n2-17`). Work and commit only there.

The control plane's Git state panel (FWD-16) shows, per box, whether integration was refused. Today
`app/admin_fabric_gitstate.py` `_refused(client, window)` (about `:172-190`) walks that box's 48 h window of history
records newest-first, fetching bodies until it meets an `integrate` pass. The served cold read is 9.7 s with 1,336 body
fetches (measured by the issuer today), close to the 10 s safety bar. A parallel cell makes the producer write ONE
pointer object per box on every integrate pass; this cell makes the reader use it.

**The object** (fixed; do not change its shape):
`s3://opal-313476888478-globgrph/fabric/activity/v1/gitstate/box=<B>/last_integrate.json`, ASCII JSON with exactly
`{"at": "<YYYY-MM-DDTHH:MM:SSZ>", "rc": <int>, "note": "<text, at most 200 chars>"}`.

Build, in the gateway app at `infra/aws/ec2/opal-gateway/`:
1. **`app/admin_fabric_gitstate.py`:** `_refused` reads ONE object per box, that pointer, through the module's existing
   client and read helper (`_read_json`, `_is_absent`). Remove the window scan from `_refused` entirely (it must fetch no
   history key). Change its signature as you need, and update its two call sites in `_compute` (about `:248`, `:263`).
   - absent (`NoSuchKey`/404) -> `integration_refused` is "not recorded";
   - `rc != 0` -> `{"at": <at>, "note": <note>}`;
   - `rc == 0` -> "not recorded";
   - any other read failure -> the module's existing 503 arm (unchanged).
   - Rewrite `_REFUSED_BASIS` (the basis string served beside the value) to say: decided by the box's newest integrate
     pass, read from its `last_integrate.json` pointer; a box with no pointer reads "not recorded" because no integrate
     pass has been recorded since the pointer began on 2026-10-13. Update the module docstring's C17 paragraph to match.
   - Change nothing else: the listing, `first_seen`, `_state`, the cache and the response shape stay as they are.
2. **`tests/test_admin_fabric_gitstate.py`:** keep its fixtures. Rewrite the three window-based refusal tests
   (`test_gitstate_integration_refused_is_superseded_by_a_later_success`,
   `test_gitstate_integration_refused_reports_a_standing_refusal`, `test_gitstate_integration_refused_carries_its_basis`)
   for the pointer, or replace them; every other test must still pass. Add these four, by these exact names:
   - `test_refused_fetch_count_equals_box_count_at_1x_and_10x` -- a planted stub store with every roster box, history
     at 1x and at 10x the window's record count, pointers present: the number of `get_object` calls `_refused` makes,
     summed over the boxes, equals the roster box count (4) at BOTH sizes.
   - `test_pointer_rc_nonzero_reads_at_and_note` -- a pointer with `rc` 1 gives `{at, note}` from the pointer.
   - `test_pointer_rc_zero_or_absent_reads_not_recorded` -- `rc` 0 gives "not recorded"; no pointer gives "not recorded".
   - `test_refused_reads_no_window_body` -- with a planted history containing a refusal inside the window and NO pointer,
     `_refused` fetches no history key and the box reads "not recorded".
   - `test_real_capture_gitstate` must still pass. The capture holds no pointer, so every box reads "not recorded" there.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `.tools/fabric-gitstate.py` (a parallel cell's), any
   other `app/` module, `admin_api.py`, Terraform, the manifest or `mcportal/`. No deploy and no AWS call.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_fabric_gitstate.py
infra/aws/ec2/opal-gateway/tests/test_admin_fabric_gitstate.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~17/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/admin_fabric.py`, `.tools/fabric-gitstate.py`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/fixtures/`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17r2/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W17-S<k>` (the next free k for W17). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`. Append a row as ONE whole fenced ```json block.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-n-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17r2/checks/n2.AC1.sh; echo "exit=$?"</invocation><expect>gitstate tests: 0 failed; named tests PASSED 4 of 4 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~17/NFRA_MCPORTAL.TO-MP-n-2.refusal-pointer-reader.proof_of_spec.json`.
Report once, with: the check output; the commit hash; the `_refused` diff; the get_object counts at 1x and 10x; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the C17 round-2 issuance (decomposition v8) from ROUND_ANALYSIS.c17-round1.md @53231d51ee E1
criteria (1) and (2); the producer side is MP-n-3, under 4.0.0_SA_CRO~Z's written consent @b5ce7b2966. Check dry-run at
the base: AC1 FAIL (10 passed, named 0 of 4). No gate. Lives through MP-n-4.

<status>pending</status>
<round>2</round>
<workstream>C17</workstream>
<slot>~17</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
