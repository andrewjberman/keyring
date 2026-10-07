# TO MDPF_HEALGAP.TO-HG-t1 -- round 1 HG-t-1: the Rebalancer runner skips a complete day by listing its stamp, and can be made to fail like a lapsed login

<to_id>MDPF_HEALGAP.TO-HG-t1</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~1</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-1` (`decompositions/MDPF_HEALGAP_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-1`. FWD-1: on a day the 06:00Z Cottonwood Rebalancer pull fails because the vendor login lapsed, the day's three bronze feeds still land
the same day with nobody acting. A sibling cell adds a SECOND invocation of this runner each day, after the login chain succeeds (~11:32Z). This
cell makes that second invocation safe (a complete day must skip without touching the vendor or the session) and makes the morning failure
inducible on purpose without touching the real login.

**The code, read at the base.** `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py`:
- `_already_landed(date)` (lines 211-218) calls `_s3.get_object` on `_stamp_key(date)` = `blackdiamond/cottonwood/meta/<date>-complete.json`
  and returns False on ANY exception. The Lambda's role holds `s3:ListBucket` on the bucket for prefix `blackdiamond/cottonwood/*` and does
  NOT hold `s3:GetObject`, so in AWS this always raises AccessDenied and the guard never skips.
- `ingest(now_iso, date, force=False)` (line 400) checks the guard first, then `Puller(load_bd_session())` reads the session secret and mints the
  bearer. A lapsed login fails in `mint_rebalancer_bearer` as `RuntimeError("BD GET /auth/token -> HTTP 401: ...")` (from `_request`, line 141).
- `lambda_handler(event, context)` (line 466) reads `mode`, `date`, `force` from the event and calls `ingest`.
- `_land` already verifies by listing (`list_objects_v2(Prefix=key)`, exact key, `Size > 0`); copy that shape.
- The existing offline suite `test_lambda_function.py` in the same folder (run as `python test_lambda_function.py` from that folder) uses a
  `FakeS3` with `put_object`, `get_object`, `list_objects_v2` and `get_paginator`, and imports `lambda_function` bare.

**Build:**
1. `_already_landed(date)`: decide by `_s3.list_objects_v2(Bucket=BD_S3_BUCKET, Prefix=_stamp_key(date))` -- True only when a listed object's
   `Key` equals the stamp key exactly and its `Size > 0`. Keep "fail-open to PULL on any doubt": any exception returns False. No `get_object`.
2. The induced lapse: `ingest` takes `induce=None`; `lambda_handler` passes `event.get("induce")`. AFTER the guard check (a complete day still
   skips) and BEFORE `load_bd_session()`, when `induce == "auth-lapse"` raise
   `RuntimeError("BD GET /auth/token -> HTTP 401: INDUCED auth-lapse (MDPF_HEALGAP FWD-1 exercise; no secret read, no vendor call)")`, so
   `_is_auth_error` reads it as an auth failure. Any other non-empty `induce` value raises `ValueError` naming it. The CLI `main()` is unchanged.
3. NEW file `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/test_healgap_guard.py`, pytest-collectable, offline. Its fake S3 raises on EVERY
   `get_object` (as the real role does) and serves `list_objects_v2` from an in-memory dict; patch `lambda_function._s3` with it, and replace
   `lambda_function.load_bd_session` with a stub that records the call and raises a test-local exception. Tests, exact names:
   - `test_guard_skips_on_listed_stamp_with_getobject_denied`: the stamp for 2026-10-07 is stored (non-empty); `ingest(now, "2026-10-07")`
     returns `{"verdict": "SKIP-IDEMPOTENT", ...}` and the session stub was NOT called.
   - `test_guard_pulls_when_stamp_absent_control`: the same fake with no stamp; `ingest(now, "2026-10-07")` raises the stub's exception (the
     session read was reached). This is the difference control: the only change is the stamp's presence.
   - `test_induced_auth_lapse_raises_before_session_read`: no stamp; `lambda_handler({"mode": "pull", "date": "2026-10-07", "induce":
     "auth-lapse"}, None)` raises `RuntimeError` whose text contains `HTTP 401`, and the session stub was NOT called.
   - `test_induced_auth_lapse_skipped_on_complete_day`: the stamp is stored; the same event returns `SKIP-IDEMPOTENT`.
4. Keep `python test_lambda_function.py` passing from the runner folder.

### ACCEPTANCE

<criterion id="HG1-t1-AC1" cell_refs="HG-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_t1_guard_tests.py</invocation><expect>GUARD-TESTS-OK</expect></criterion>
`HG1-t1-AC1` -- with `GetObject` denied, a listed stamp makes the runner skip before the session read, and an absent stamp reaches it.

<criterion id="HG1-t1-AC2" cell_refs="HG-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_t1_induce_tests.py</invocation><expect>INDUCE-TESTS-OK</expect></criterion>
`HG1-t1-AC2` -- the induced lapse fails as an HTTP 401 before the session read on an incomplete day, and a complete day still skips.

<expected_criteria>HG1-t1-AC1 HG1-t1-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base (2026-10-07): `GUARD-TESTS-BAD ... rc=4` and `INDUCE-TESTS-BAD ... rc=4`
(no test file).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Offline only.** No AWS call, no Lambda invoke, no build-and-upload, no `terraform`, no Black Diamond call. The deploy is the issuer's.
- Do not touch `_reconcile_counts`, the landing gates, the model-detail scope or `landing_guard.py`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) in the investigation file below, and do not weaken a test.

<paths>
infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py
infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/test_healgap_guard.py
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 1, the thread), cell `HG-t-1`.
<owned_cells>HG-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG1-t1-AC1, HG1-t1-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~1/MDPF_HEALGAP.TO-HG-t1.guard-by-listing-and-induced-lapse.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG1-t1-AC1 HG1-t1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the diff of `lambda_function.py`, the test file, both checks' output, `python test_lambda_function.py` output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule.
comp-iam: RUN at L5 (comp-iam service cot-rebalancer-runner, 2026-10-07): s3:ListBucket GRANTED, s3:GetObject UNGRANTED; the repair moves the guard onto the granted call, so no IAM write.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: WORLD -- the L6 floor for an infrastructure path (the runner's Lambda source). The worker writes code and offline tests only; the deploy is the issuer's act at the drain under a change-management entry, with the CTO's exercised read.
direct_act: false -- the class is WORLD, so the direct-act path does not apply.
</preflight>

Source: PRD v0.1 @78db344481 section 2 (THREAD hops 1 and 3), C-IDEMPOTENT; decomposition round 1.
