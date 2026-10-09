# TO IRPT_DASHBD.TO-DB-b-99 -- E1: the tie-out classifier's thresholds tested for sensitivity (peak cut 0.5% / 1% / 2%, dollar-tie neighbours), pre-registered before the run, and every reason carrying its claim (inferred | confirmed) and robustness

<to_id>IRPT_DASHBD.TO-DB-b-99</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~74</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>49</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 15 (msg 3492, @74243ee7c8) and ADDENDUM 13.2 (msg 3501), enrichment item E1 | **Decomp cell:** `DB-b-99` (decomposition section 51) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-98 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-74`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~74/`.

**The cell (`DB-b-99`).** DB-b-98 (`C:/dev/wk-irpt-dashbd-74/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~73/classify_unexplained.py`, record `UNEXPLAINED_CLASSIFIED.json`)
reasoned 793 of the 990 OUTSIDE segments of the 49F vs Black Diamond tie-out, using thresholds the worker chose: NEAR_ZERO_BASE at 1% of peak, and a
dollar tie at $1 / 0.1%. The CTO ruled (ADDENDUM 15 items 1-3) that FWD-8 is NOT REALIZED until those choices are tested and every reason carries its
claim.

1. **Pre-register first.** Write `THRESHOLDS.json` in your folder: peak cuts 0.005, 0.01, 0.02 and at least three dollar-tie settings (the current
   one and its neighbours). COMMIT it on its own BEFORE any run. That commit is `rule_commit`.
2. **Run** the classifier at every setting, over the same inputs DB-b-98 read (S3 GETs only). For each setting record `by_reason` over the 990.
   Print the 156 NEAR_ZERO_BASE segments at 1% as `cut_segments`, with their verdict at each setting.
3. **Robustness.** A reason whose count moves by more than half across the band is `robust: false`. Its segments are re-graded UNEXPLAINED in
   `final`.
4. **Claim.** Every reason carries `claim`:
   - `confirmed` only where Black Diamond's own record shows it;
   - `inferred` otherwise.

   Record which reasons are MECHANICAL two-sided reads (flow timing or an income date read from both sides' transaction dates). Those are the only
   inferred reasons that can realize FWD-8.
5. **Output.** Record `SENSITIVITY.json` {settings: {peak_cut, dollar_tie}, per_setting: {<name>: by_reason}, cut_segments, final: {by_reason,
   reasons: {<reason>: {claim, robust, mechanical}}}, preregistration: {thresholds_file, rule_commit, output_commit}}.
   - Commit it in a LATER commit than the thresholds.
   - `output_commit` is the commit that adds SENSITIVITY.json. Fill it in the next commit, or record it as the parent of the commit that records it.

**No vendor call, no AWS write.** Copy no client identifier beyond the account keys the tie-out already carries.

<criterion id="DB49-1-AC1" cell_refs="DB-b-99"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r49/p49_round49.py" . DB49-1-AC1</invocation><expect>DB49-1-AC1 PASS</expect></criterion>
`DB49-1-AC1` -- every setting's counts sum to 990, the 156 cut segments are printed, and the final classification carries claim and robustness with non-robust reasons re-graded. Base: FAIL.

<criterion id="DB49-1-AC2" cell_refs="DB-b-99"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r49/p49_round49.py" . DB49-1-AC2</invocation><expect>DB49-1-AC2 PASS</expect></criterion>
`DB49-1-AC2` -- the thresholds were committed before the output that graded them. Base: FAIL.

<expected_criteria>DB49-1-AC1,DB49-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** S3 GETs of the objects DB-b-98 read; you write only in your folder.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~74/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~74/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-99.classifier-sensitivity.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 51 (round 49), cell `DB-b-99`.
<owned_cells>DB-b-99</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB49-1-AC1, DB49-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~74/IRPT_DASHBD.TO-DB-b-99.classifier-sensitivity.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB49-1-AC1,DB49-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the per-setting counts, the non-robust reasons, the claims, the two commits, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an offline analysis over existing inputs; nothing served moves in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 GETs of already-read objects only; no write, no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB49-1-AC1 and DB49-1-AC2 FAIL at base (no record). CTO ADDENDUM 15 items 1-3.
lane: the <paths> block IS the grant.
</preflight>
