# TO NFRA_TRNSPT.TO-TR-w4 -- the scheduled mail pull reaches up to 120 days, listed in spans of at most 31

<to_id>NFRA_TRNSPT.TO-TR-w4</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by path floor (the Lambda handler); nothing is applied | **Decomp cell:** `TR-w-4` (`decompositions/NFRA_TRNSPT_DECOMP_R4.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-w-4` (CTO round-3 analysis @c2b5eb89a4, section 4, C1): "The scheduled function reaches past 31 days by spans.
`mail_handler.py` accepts a window of up to 120 days and lists it as spans of at most 31 days, as `pull.py --gateway` already does.
Default unchanged at 7."

**Measured at the cut:**
- `infra/aws/lambda/transcripts-pull/mail_handler.py` `lambda_handler` reads `WINDOW_DAYS` (default "7") and raises
  `ValueError("WINDOW_DAYS %d is outside 1..31")` outside 1..31, before any call. Its module docstring says "1..31".
- The span cutting ALREADY EXISTS in the client: `data/transcripts/scripts/outlook/gateway_mail.py` `HxMailClient.list_rows`
  (around line 148) cuts `[start, end)` with `_spans(start, end, LIST_WINDOW_DAYS)` (`LIST_WINDOW_DAYS = 31`, line ~172; `_spans` line
  ~180). The handler passes `now - timedelta(days=days)` .. `now` to `pull.GatewayMailSource`, which calls `client.list_rows` per
  sender. So the build is mostly the bound; the test must PROVE the spans through the handler.
- `data/transcripts/scripts/tests/test_mail_pull_handler.py:113` `test_a_window_outside_the_route_terms_is_refused_before_any_call`
  is parametrized `["0", "32"]` and matches `"outside 1..31"`. Its fakes (`ListingRoute`, `ListingS3`, `_client`, `_load_handler`,
  `ENV`, `NOW`, the `no_network` fixture) are the ones to reuse.
- Skipping a row already in bronze is `pull.sidecar_in_bronze(s3)` (the existing sidecar rule); `GatewayMailSource` counts it in
  `skipped_known`.

**Build:**
1. `mail_handler.py`: accept `WINDOW_DAYS` 1..120; outside raises `ValueError` before any call, message naming `1..120`. Default stays
   7. Update the docstring line. Do not change the client's 31-day cap or `_spans`.
2. New file `data/transcripts/scripts/tests/test_mail_window_spans.py`:
   - a test whose name contains `spans`: invoke `lambda_handler` with `WINDOW_DAYS=120` on a fake route that RECORDS each listing
     request's `[start, end)`; assert every span is at most 31 days, spans are contiguous, the first starts at `NOW - 120 days`, the
     last ends at `NOW` (every day covered once); and that a row whose sidecar is already in the fake bronze is skipped
     (`skipped_known` >= 1, nothing landed for it).
   - a test whose name contains `bounds`: `WINDOW_DAYS` "0" and "121" each raise `ValueError` matching `1..120` and the route records
     no call; "120" does not raise.
3. In `test_mail_pull_handler.py`, update only the bound test to the new terms (parametrize `["0", "121"]`, match `1..120`).

### ACCEPTANCE

<criterion id="TR4-w4-AC1" cell_refs="TR-w-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R4_CHECKS/r4_checks.py w4-spans</invocation><expect>R4-W4-SPANS-OK</expect></criterion>
`TR4-w4-AC1` -- a 120-day window is listed as contiguous spans of at most 31 days covering every day once; a known row is skipped.

<criterion id="TR4-w4-AC2" cell_refs="TR-w-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R4_CHECKS/r4_checks.py w4-bounds</invocation><expect>R4-W4-BOUNDS-OK</expect></criterion>
`TR4-w4-AC2` -- a window over 120 or under 1 raises before any call.

<criterion id="TR4-w4-AC3" cell_refs="TR-w-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_CHECKS/r2_bundle_import_check.py</invocation><expect>BUNDLE-IMPORT-OK</expect></criterion>
`TR4-w4-AC3` -- the deployed layout (CTO rule 103374): the Lambda bundle extract imports the handlers with no bare sibling module.

<expected_criteria>TR4-w4-AC1,TR4-w4-AC2,TR4-w4-AC3</expected_criteria>

Dry-run at the base (CLOUD b6a856bfb9): AC1 `R4-W4-SPANS-FAIL absent` and AC2 `R4-W4-BOUNDS-FAIL absent` -- FAIL as expected; AC3
`BUNDLE-IMPORT-OK files=48` -- PASS as expected (a control; it must still pass after your change).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **WORLD by path (the Lambda handler); NOTHING is applied.** Never `terraform apply` / `safe-apply`, never deploy, never invoke the Lambda, never call the gateway, never read the
  `opal-data-transcripts` bucket (this machine is refused its key, by ruling). `dist/` is a build product, never committed.
- Do not change `infra/aws/terraform/transcripts/mail_pull.tf`; the deployed `WINDOW_DAYS` stays "7".
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_TRNSPT-W1-S<k>`, next unused), and do not weaken a test to pass.

<paths>
infra/aws/lambda/transcripts-pull/mail_handler.py
data/transcripts/scripts/tests/test_mail_window_spans.py
data/transcripts/scripts/tests/test_mail_pull_handler.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R4.md</decomp_doc> (round 4), cell `TR-w-4`.
<owned_cells>TR-w-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR4-w4-AC1, TR4-w4-AC2, TR4-w4-AC3. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-w4.mail-window-spans.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR4-w4-AC1,TR4-w4-AC2,TR4-w4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the bound change, the spans the test recorded for 120 days (count and first/last), the three check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the 23:30Z rule and the deployed WINDOW_DAYS=7 are untouched by this cell.
comp-iam: DECLARED-NOT-APPLICABLE the cell writes no bucket and applies nothing; dell2's principal is refused kms:Decrypt on the transcripts key (measured 2026-10-07T14:2xZ), so no store read is in scope.
comp-adversary: RUN -- the bundle import control (AC3) is carried because the cell edits a module the Lambda bundle ships (CTO rule 103374).
lane: the <paths> block IS the grant; infra/aws/** is the AE lane at APPLY, which this order never reaches.
</preflight>

Source: CTO round-3 analysis @c2b5eb89a4 section 4 C1; decomposition round 4 cell TR-w-4.
