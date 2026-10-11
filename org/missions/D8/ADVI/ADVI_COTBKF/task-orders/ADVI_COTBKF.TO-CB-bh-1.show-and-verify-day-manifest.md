# TO ADVI_COTBKF.TO-CB-bh-1.show-and-verify-day-manifest -- round 60 CB-bh-1: show the day manifest before the mint; read its method fields back after

<to_id>ADVI_COTBKF.TO-CB-bh-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~87</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bh-1` (`decompositions/ADVI_COTBKF_DECOMP.round60.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow in ANY tracked file.** Counts, sha256,
addresses and reason codes only. Every value in a test is SYNTHETIC. When you print a day manifest, print it WITHOUT any field that
is keyed by or lists account ids (for example `first_data_date`): print that field's count instead.

**Why (the signed CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R59_ARD_COTTONWOOD_MINT_CTO_HALF.md`, conditions 2 and 3 --
read section 4 of it first).** The mint writes 3,325 day manifests through the producer's `emit_day`. Each must state method row 3
and not the custodian method. That has only ever been exercised on faked S3. The applier must SEE one before the mint, and the
read-back must check all of them after.

**Your item, all in `data/assets/scripts/silver/commonwealth_account_return_daily.py`. Do NOT touch `apply_days` or `build`.**

1. **A no-write show mode.** Add `--show-day-manifest --manifest <tracked manifest> [--days-dir <dir>] [--date <YYYY-MM-DD>]`
   (default date: the manifest's last day).
   - It makes NO S3 call and creates no S3 client.
   - It re-hashes that day's local file against the manifest, loads the frame exactly as `apply_days` does, builds `first_data_date`
     exactly as `apply_days` does, and calls the PRODUCER's own `build_manifest(frame, firm, day, uri, thresholds=None,
     first_data_date=..., src=<the _commonwealth_delivery entry>)` with the `uri` the producer's `emit_day` would compute. Factor the
     shared steps into one helper that `apply_days` could call; do not copy a second version of them and do not change `apply_days`.
   - It prints the manifest as JSON (account-keyed fields replaced by their counts), then ONE last line:
     `ARD-COTTONWOOD-DAY-MANIFEST date=<D> method_version=<v> valuation_source=<s> fee_treatment=<f> price_basis=<p> custodian_text=<absent|PRESENT>`.
   - `custodian_text` is `PRESENT` when the producer's custodian method sentence, or the string `custodian_reported`, appears anywhere
     in the manifest's JSON text. Take the sentence from the producer (its `method_text` for `custodian_reported`); do not type it.
   - It exits 0 only when `method_version` is 3, the three other fields read `positions_x_as_traded_close`, `net_of_fees` and
     `as_traded`, and `custodian_text` is `absent`. Print which field failed otherwise.
2. **The read-back reads every day manifest.** In `verify_served`, for each day also get `<address>/manifest.json` and check the same
   five things with the SAME function the show mode uses. The last line keeps its start and its `sidecar=` and `method_row=` parts
   and gains `manifests=<k>/<n>` (k = days whose served manifest passes). A missing or failing manifest is counted, never raised
   past; print the first three failing days with the field that failed.
3. **Tests alone first.** Add `data/assets/scripts/silver/tests/test_commonwealth_ard_day_manifest.py`, committed ALONE first; report
   its red line. On synthetic frames and a faked S3 it asserts: the show mode creates no S3 client and exits 0 on a row-3 entry; it
   exits non-zero and prints `custodian_text=PRESENT` when `src` is an entry whose method is the custodian one; it exits non-zero
   when one of the three fields differs; `verify_served` prints `manifests=<n>/<n>` after a faked mint and `manifests=<n-1>/<n>`
   after one faked served manifest is changed to the custodian method.
4. **Run** the three acceptance invocations.

**Inputs.** The real day files are in the BASE checkout, read-only: `C:/dev/ajb_workspace/.scratch/advi_cotbkf/ard_cottonwood_r47`. Read the producer
`data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (`build_manifest` line 1842, `method_text` line 1826, `emit_day`
line 1863) to call it correctly; do NOT edit it.

### ACCEPTANCE

<criterion id="CB60bh1-AC1" cell_refs="CB-bh-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_commonwealth_ard_day_manifest.py -q</invocation><expect>passed</expect></criterion>
`CB60bh1-AC1` -- the show mode and the wider read-back behave as step 3 lists; 0 failed, 0 skipped.

<criterion id="CB60bh1-AC2" cell_refs="CB-bh-1"><invocation>python data/assets/scripts/silver/commonwealth_account_return_daily.py --show-day-manifest --manifest org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json --days-dir C:/dev/ajb_workspace/.scratch/advi_cotbkf/ard_cottonwood_r47 --date 2026-06-22</invocation><expect>ARD-COTTONWOOD-DAY-MANIFEST date=2026-06-22 method_version=3 valuation_source=positions_x_as_traded_close fee_treatment=net_of_fees price_basis=as_traded custodian_text=absent</expect></criterion>
`CB60bh1-AC2` -- on the REAL last day, the manifest the producer will write states row 3 and carries no custodian text. If the line
differs, do not change anything to make it match: that is the refusal clause, and it is the finding the CTO's condition exists for.

<criterion id="CB60bh1-AC3" cell_refs="CB-bh-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB60bh1-AC3` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before this order.

<expected_criteria>CB60bh1-AC1,CB60bh1-AC2,CB60bh1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** `apply_days`, `build`, the stamp and bond-check modes; anything under `data/assets/scripts/gold/`, `lib/` or
  `infra/`; any other test; any manifest; anything under `C:/dev/ajb_workspace/` (read only); `surprise-channel/` except your own
  NEW row.
- **Do NOT run `--apply` or `--verify-served`.** No AWS or S3 call of any kind. No push.
- **No gate override** of any kind and no `--force`. If a gate refuses a commit and the fix is not an ordinary code correction inside
  your grant, stop and report its exact refusal line.
- **Do not open or print** anything under `C:/dev/_cotbkf_private_evidence_20261009/`. Never print an account id.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise row
  (id `ADVI_COTBKF-D2-W87-S<k>`, `"fabric": "dell2"`, carrying no account id, its `surfaced_at` read from the clock). Do not weaken
  a test.

**AMENDMENT 1 (issuer, 2026-10-11 ~06:0xZ) -- row ADVI_COTBKF-D2-W87-S1 ruled: the grant widens to the two older tests that pin the read-back line.**
- The gap was the issuer's: step 2 changes the last line of `verify_served`, and two existing tests assert that line with `==`. Both
  files are added to the `<paths>` block below.
- `test_commonwealth_ard_mint_claims.py`: update the three assertions on the `ARD-COTTONWOOD-VERIFY` line to the new line, with the
  `manifests=<k>/<n>` value the faked bucket really gives. Nothing else in the file changes.
- `test_commonwealth_ard_apply.py`: the happy-path test mints through the producer and then verifies. Make its faked entry a row-3
  entry (as the real `_commonwealth_delivery` entry is), so the served day manifests state row 3 and the line reads `manifests=3/3`;
  then update the assertion. Do NOT assert `manifests=0/3` on a happy path, and do not loosen `==` to a prefix match.
- If the happy path cannot read `manifests=3/3` without changing product code, stop and report: that would be a finding about the
  mint, not a test detail.
- `CB60bh1-AC3` is unchanged: 0 failed, 0 errors, 12 skipped.

<paths>
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/test_commonwealth_ard_day_manifest.py
data/assets/scripts/silver/tests/conftest.py
data/assets/scripts/silver/tests/test_commonwealth_ard_mint_claims.py
data/assets/scripts/silver/tests/test_commonwealth_ard_apply.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round60.md</decomp_doc> (round 60), cell `CB-bh-1`.
<owned_cells>CB-bh-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB60bh1-AC1, CB60bh1-AC2, CB60bh1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~87/ADVI_COTBKF.TO-CB-bh-1.show-and-verify-day-manifest.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB60bh1-AC1,CB60bh1-AC2,CB60bh1-AC3` BEFORE the flip. All three are
mechanical.
</proof_of_spec>

**REPORT (counts only):**
- the red pytest line of the test-alone commit; the three acceptance lines, with the full `ARD-COTTONWOOD-DAY-MANIFEST` line;
- the top-level keys of the real day manifest you showed, and the method sentence it carries, verbatim (it is not client data);
- `git diff --stat` of `apply_days` and `build`: 0 lines changed in either, or say what moved and why;
- commits, with the test-alone commit first; every gate refusal, verbatim; anything you could not run or verify.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run adapter and a new test; nothing scheduled runs it (row ADVI_COTBKF-D2-S84).
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the show mode creates no S3 client and the read-back is exercised on faked S3.
comp-adversary: RUN -- the test alone first, red at the base; the show mode has two refusing arms (custodian entry, one field differing) and asserts that no S3 client is created; the read-back has an arm with one served manifest changed; the real-data criterion forbids adjusting the code to match; BLIND: the served manifest gains a `landed` field the local build does not have, and the real bucket's bytes are read only at the mint.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` CTO half @1013274c3f (msg 4211), conditions 2 and 3; the COO half @41395d1eb5; row ADVI_COTBKF-D2-W66-S1.
