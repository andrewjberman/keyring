# TO IRPT_DASHBD.TO-DB-b-66 -- E1: repair the two callers round 32's reader promotion broke (W40-S1, W42-S1) and re-run DB-b-65's near-zero fix WITHOUT its shim on the reader of record's own mean (row S36)

<to_id>IRPT_DASHBD.TO-DB-b-66</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~43</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-33 ADDENDUM 2 @47c849d75b (msg 2116, on ADJUDICATION_v18), enrichment item E1 | **Decomp cell:** `DB-b-66` (decomposition section 36) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-63, DB-b-65 (merged @96a0c9991a, @58fa2adf16).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-43`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~43/`.

**The cell (`DB-b-66`).** Round 32 (DB-b-60) made `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py` the one writer of the
daily-mean fee base and removed `mean_daily_value` from round 31's classifier (`deliverables/0.9.0_WK_IRPT_DASHBD~36/unexplained_classes.py`).
Two callers broke:
- `deliverables/0.9.0_WK_IRPT_DASHBD~39/large_flow_e3.py` calls `uc.mean_daily_value` (lines ~117 and ~279). Its own
  `test_large_flow_e3.py` fails 1 of 3 at HEAD.
- `deliverables/0.9.0_WK_IRPT_DASHBD~35/crossover_e1.py` calls `v2.daily_mean_value` (line ~49). It raises AttributeError and has no test.

Round 33's DB-b-65 (`deliverables/0.9.0_WK_IRPT_DASHBD~42/near_zero_e3.py`) ran with a SHIM, `uc.mean_daily_value = uc.daily_mean_value`
(lines ~189-193). Row W38-S1 measured those two means as different (positive-only vs all values), so its "79 fixed" is not counted until a
shim-free re-run (the CTO's ruling, row S36).

1. Repair both callers to import their fee-base function from the reader of record (`tieout_reader.py`, with the `positive_only` binding
   the round-31 classifier uses where they relied on it). Define no fee-base function in them. Make
   `deliverables/0.9.0_WK_IRPT_DASHBD~39/test_large_flow_e3.py` pass. Write
   `deliverables/0.9.0_WK_IRPT_DASHBD~35/test_crossover_e1.py` with a test whose name contains `caller` that exercises the repaired call
   path offline (a synthetic segment, no client data).
2. Remove the shim from `near_zero_e3.py`; it uses the reader's own mean. Re-run the 153 NEAR_ZERO_BALANCE rows (from
   `deliverables/0.9.0_WK_IRPT_DASHBD~36/UNEXPLAINED_CLASSES_E2.json`) shim-free. Write `NEAR_ZERO_SHIMFREE_E1.json` in your folder:
   `shim_applied` false, `rows` [{account, segment, sub_class, evidence, abs_diff_pp}], `counts`, `fixed_within` (rows of the fixed
   classes within 0.35 pp under the reader's mean, against round 33's 79), `tieout_within_total` (the whole 9,078 graded by the reader
   with the shim-free near-zero result, against 8,385), `reader_sha256`, and `files_read`. Write `NEAR_ZERO_SHIMFREE_E1.md` (COUNTS ONLY).
3. Re-run the ~35, ~36 and ~39 records and show which change; the change is expected only where the shim was wrong.

<criterion id="DB34-1-AC1" cell_refs="DB-b-66"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r34/p34_round34.py" . DB34-1-AC1</invocation><expect>DB34-1-AC1 PASS</expect></criterion>
`DB34-1-AC1` -- both callers' tests pass (a new 'caller' test for crossover_e1), no shim remains in the callers or near_zero_e3.py, and the reader is still the one fee-base writer. Base: FAIL.

<criterion id="DB34-1-AC2" cell_refs="DB-b-66"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r34/p34_round34.py" . DB34-1-AC2</invocation><expect>DB34-1-AC2 PASS</expect></criterion>
`DB34-1-AC2` -- the near-zero 153 re-run shim-free on the reader's own mean, with fixed_within and the tie-out total printed and the reader sha matching HEAD. Base: FAIL.

<expected_criteria>DB34-1-AC1,DB34-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~43/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/crossover_e1.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/test_crossover_e1.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/large_flow_e3.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/test_large_flow_e3.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~42/near_zero_e3.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-66.caller-repair.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 36 (round 34), cell `DB-b-66`.
<owned_cells>DB-b-66</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB34-1-AC1, DB34-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~43/IRPT_DASHBD.TO-DB-b-66.caller-repair.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB34-1-AC1,DB34-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the repaired calls, both test results, fixed_within against 79, the tie-out total against 8,385, which records changed, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: project-owned reconciliation code and records; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB34-1-AC1/AC2 base FAIL at base 5baf94294f (~39's test fails 1 of 3, no ~35 test, the shim is present -- the detector reads it at base); positive control on a planted record PASS.
lane: the <paths> block IS the grant.
</preflight>
