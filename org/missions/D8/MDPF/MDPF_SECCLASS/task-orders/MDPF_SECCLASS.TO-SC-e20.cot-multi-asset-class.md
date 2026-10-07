# TO MDPF_SECCLASS.TO-SC-e20 -- round 7 SC-e-20: `multi_asset` joins the Cottonwood gold class lists, so no client mix drops a class the table produces

<to_id>MDPF_SECCLASS.TO-SC-e20</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~20</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-10-06</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~M-COTCLS</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-20` (`decompositions/MDPF_SECCLASS_DECOMP_R7.md`, AMENDMENT) |
**outcome_ref:** FWD-2 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-20`. FWD-2: an advisor sees a Cottonwood client's classes as the canonical table holds them. 1.0.0_SA_CTO ruled this round
(msg 105604, row `MDPF_SECCLASS-S29` in `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`).

**The defect, measured.** Four Cottonwood clients hold the security SGIIX (FIRST EAGLE GLOBAL I), which the canonical table classes
`multi_asset`. The Cottonwood gold scripts publish a client mix over a fixed class list that lacks `multi_asset`, so on the 2026-10-05
point those four mixes sum to 0.904, 0.957, 0.963 and 0.973 instead of 1 (the dollars missing equal the SGIIX holdings to within $1.5:
z09305621 $25,862.98; z09305679 $109,319.81; z09305578 $49,876.03; z09305703 $25,560.05).
C_06's own sum guard (`C_06.client_mix_timeseries.py:466-470`) checks the aggregate over every class in the data, so it passes while the
published mix drops one.

**Build (code, tests and a read-only check; NO deploy, NO gold run, NO table write):**
1. **The class lists.** Add `multi_asset` as its own class, never folded into another class and never into `unclassified`:
   - `data/cot/scripts/gold/C_06.client_mix_timeseries.py` `MIX_ASSET_CLASSES` (line 177);
   - `data/cot/scripts/gold/lib/mix_views.py` `MIX_ASSET_CLASSES` (line 24), so the period views publish it as itself;
   - `data/cot/scripts/gold/D_04.client_portal_summary.py` the firm mix snapshot loop (line 527), so the firm mix drops none;
   - `data/cot/scripts/gold/B_01b.classify_new_securities.py` `VALID_ASSET_CLASSES` (line 48): it admits the table's own class. Do not
     add it to that script's model prompt or answer vocabulary.
   - Keep the order `equity, fixed_income, alternatives, commodities, structured, cash, multi_asset, unclassified, other`. A published
     history that lacks the key reads as 0 (`entry.get(ac, 0.0)`, line 665); confirm that and print it in your report.
2. **The guard.** In `C_06.client_mix_timeseries.py` make the sum check run over the EMITTED mix (the `MIX_ASSET_CLASSES` shares), so a
   future class missing from the list makes the client SKIP LOUDLY instead of publishing a mix that does not sum. The verbose line says which class
   is missing. A client is never skipped for holding `multi_asset`.
3. **Tests** (`data/cot/scripts/gold/tests/`): update `test_other_admission.py` (the exact-list assertion) and
   `test_mix_publishes_every_class.py` (period views and D_04 read every class) for the new class, and add to
   `test_mix_publishes_every_class.py` three tests whose names contain `multi_asset` (the lane grant names these two test files only; do not create a new test file):
   - a client holding `multi_asset` publishes a mix summing to 1 within 0.001, with its own `multi_asset` share;
   - a position of a class outside the list makes the client skip loudly (the guard over the emitted mix);
   - the period views carry `multi_asset` as itself.
4. **The before/after read.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/cot_mix_multi_asset_check.py`:
   - it reads `s3://opal-data-cot/gold/canonical/holdings/2026-10-05.parquet`, the accounts dimension and the ghost-account list the way
     `C_06.process_partition` does, and runs `process_partition` (in-process, writing nothing) for the relationships z09305578, z09305621, z09305679
     and z09305703;
   - it prints, per client, the BEFORE shares (the live `gold/entities/clients/<id>.json` point for 2026-10-05, read only) and the AFTER shares
     from the edited code, and the sum of each;
   - its last line is `COT-MIX-CHECK clients=4 after_sums_to_1=<n> multi_asset_share_present=<n>`.
   Nothing it reads is written back.
5. **The census (read only).** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/COT_FIRM_CLASS_LIST_CENSUS_20261006.md`.
   - Name every class list or class-keyed branch that lacks `multi_asset` in: the Black Diamond gold (`data/black_diamond/scripts/gold`, 49 Financial's
     chain), the Inflection gold (`data/inf/scripts`), the 49F and Cottonwood runners (`data/assets/scripts/gold/runners_49f`, `runners_cot`), and the
     portal's Advisor Intelligence pages (`portal/src/pages/AdvisorIntelligence`: the readers named in
     `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/COT_REPOINT_READER_CENSUS_20261001.md` and any other that maps or drops a class).
   - One row per list: file and line, the list, whether `multi_asset` is absent, and whether the list feeds a served artifact (read what it writes).
   - Print the denominator (files scanned). Do not edit any of them: a gap becomes an amendment.

### ACCEPTANCE

<criterion id="SC7-e20-AC1" cell_refs="SC-e-20"><invocation>python -m pytest -q data/black_diamond/scripts/gold/tests -k multi_asset</invocation><expect>passed</expect></criterion>
`SC7-e20-AC1` -- the new `multi_asset` tests (named with `multi_asset` in the test name) pass: a `multi_asset` holder publishes a mix summing to 1, an out-of-list class skips loudly, the period views carry `multi_asset`. Also run `python -m pytest -q data/cot/scripts/gold/tests` and report it: every test in that folder must still pass.

<criterion id="SC7-e20-AC2" cell_refs="SC-e-20"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/bd_mix_multi_asset_check.py</invocation><expect>BD-MIX-CHECK ok=True</expect></criterion>
`SC7-e20-AC2` -- the edited code, run in process on the real 2026-10-05 positions of the four clients, publishes four mixes that each sum to 1 within 0.001.

<criterion id="SC7-e20-AC3" cell_refs="SC-e-20"><invocation>python -c "import subprocess,sys; r=subprocess.run([sys.executable,'-m','pytest','-q','data/black_diamond/scripts/gold/tests'],capture_output=True,text=True); t=r.stdout; print('FOLDER-OK' if r.returncode==0 and ' passed' in t and ' failed' not in t else 'FOLDER-BAD')"</invocation><expect>FOLDER-OK</expect></criterion>
`SC7-e20-AC3` -- (amended, AMENDMENT 1) the triage file carries one `VERDICT: DROPS-TODAY` or `VERDICT: HOLDS-NONE` line for each of the 22 served lists the census found lacking `multi_asset`.

<expected_criteria>SC7-e20-AC1,SC7-e20-AC2,SC7-e20-AC3</expected_criteria>

Dry-run at the base 2026-10-06: all three FAIL as expected (no `multi_asset` test selected, no check script, no census file).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No deploy, no gold run, no table write, no S3 write.** `safe-deploy`, the QA gold run and the before/after never-widen pair are the issuer's act.
- **No vendor or model call.** Do not touch `B_01b`'s prompt or its model call.
- **Rule 13:** these are DS-owned gold scripts; your commit is a candidate, and deployment is not yours.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W20-S<k>`), and do not weaken the test.

<paths>
data/cot/scripts/gold/C_06.client_mix_timeseries.py
data/cot/scripts/gold/lib/mix_views.py
data/cot/scripts/gold/D_04.client_portal_summary.py
data/cot/scripts/gold/B_01b.classify_new_securities.py
data/cot/scripts/gold/D_03.composition_artifacts.py
data/black_diamond/scripts/gold/D_03.composition_artifacts.py
data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py
data/black_diamond/scripts/gold/lib/mix_views.py
data/black_diamond/scripts/gold/tests/test_composition_canonical.py
data/black_diamond/scripts/gold/tests/test_mix_publishes_every_class.py
data/cot/scripts/gold/tests/test_other_admission.py
data/cot/scripts/gold/tests/test_mix_publishes_every_class.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/cot_mix_multi_asset_check.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/COT_FIRM_CLASS_LIST_CENSUS_20261006.md
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/COT_FIRM_CLASS_LIST_TRIAGE_20261006.md
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/bd_mix_multi_asset_check.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R7.md</decomp_doc> (round 7, AMENDMENT), cell `SC-e-20`.
<owned_cells>SC-e-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC7-e20-AC1, SC7-e20-AC2, SC7-e20-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~20/MDPF_SECCLASS.TO-SC-e20.cot-multi-asset-class.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC7-e20-AC1,SC7-e20-AC2,SC7-e20-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the four edits and the guard change as diffs, the tests added, the `COT-MIX-CHECK` output with each client's before and after shares,
the census counts (lists found, lacking `multi_asset`, feeding a served artifact), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell declares no schedule; the Cottonwood gold run's own schedule is unchanged.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the check reads S3 with the laptop profile.
comp-adversary: RUN -- the moratorium (no alert or monitor: the guard skips loudly in a verbose line, it adds no alarm); the vendor rule (B_01b's model call and prompt untouched); NEVER-widen (no served artifact changes in this cell; the deploy and run are the issuer's under a half); cross-firm (the census only reads other firms' code, writes nothing); BLIND: whether any other reader of the Cottonwood mix drops the class (the census names them).
lane: the <paths> block IS the grant; the CTO landed the exact-file lane grant @052024e409 (msg 105612: five files to MDPF_SECCLASS_FAST_M_BD_MIX; B_01b already ours via IRPT_COMPLETION_M).
workstream: `~M-COTCLS` is a second workstream of round 7 (disjoint write surface from the R7 rows and FWD-10 orders, which the ONE ISSUER PER ROUND limb keys by workstream and round; row IRPT_BCKEND-S179).
</preflight>

Source: CTO ruling msg 105604 (2026-10-06 14:51Z); row S29 @4dc751ec59; cause confirmed in msg to the CTO 14:55Z.

## AMENDMENT 1 (2.0.0_SA_COO~M, 2026-10-06 ~15:5xZ) -- the CTO's census ruling and the D_03 gap (msgs 105623, 105624)

The cell re-opens (`<status>` pending). The first pass drained @e0dd7aad05 (worker commit 88d22f3f84): AC1 3 passed, folder 25 passed, AC2
`COT-MIX-CHECK clients=4 after_sums_to_1=4`, the census 434 files, 36 rows, 28 lacking `multi_asset`, 22 feeding a served artifact.

1. **D_03** (`data/cot/scripts/gold/D_03.composition_artifacts.py`, granted exact file): `_ASSET_CLASS_LABELS` has no `multi_asset`, and the
   per-class loop at line 387 walks it, so a `multi_asset` holding is dropped from the served composition. Add `multi_asset` with the label
   `Multi-Asset` (the portal's own label). Never folded into another class. Add tests whose names contain `multi_asset`, in
   `test_other_admission.py` (granted): the label exists; a composition of positions that includes a `multi_asset` one carries it and its classes sum to the total.
   Re-run AC1 and the whole folder.
2. **Triage the 22 served lists by measured loss TODAY** (CTO ruling): write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/COT_FIRM_CLASS_LIST_TRIAGE_20261006.md`, one block per list (the 22 of the
   census's served rows lacking `multi_asset`):
   - the list (file:line) and the served artifact it writes (bucket and key, read from the code);
   - a READ of that served artifact now (read only): does a held `multi_asset` value exist for that firm (49 Financial, Inflection and Cottonwood
     hold `multi_asset` nodes per `R9_CHECKS/MULTI_ASSET_LEG_V_<firm>_20261005.json`), and does the artifact lose it: a mix or composition that no
     longer sums, or a total that differs from the custody total, by the held `multi_asset` dollars? State the dollars and both sides of the sum;
   - last line of the block: `VERDICT: DROPS-TODAY` (the artifact today loses a held `multi_asset` value) or `VERDICT: HOLDS-NONE` (it
     loses none today: the list is not exercised, the firm holds none in that surface, or the artifact passes the class through), with the evidence.
   - Where you cannot read the artifact, say so in the block and use `VERDICT: HOLDS-NONE` only if a read of the code and an artifact you CAN read
     shows nothing is lost; otherwise stop and file a surprise row. Never guess a verdict.
   - Do NOT edit any list outside the granted files. The triage reports; the issuer decides what joins the pair.
3. **Criteria.** AC1's invocation now selects `-k multi_asset` over the whole tests folder; AC3 now reads the triage file (`TRIAGE-VERDICTS 22`).
   AC2 is unchanged. The census file stays as the first pass's deliverable. Gate limb: none graded this modification (LIMB 6 fires on new orders only;
   the order declares no `<placeholders>`).

## AMENDMENT 2 (2.0.0_SA_COO~M, 2026-10-06 ~17:4xZ) -- the Black Diamond (49 Financial) lists join the cell (CTO msgs 105657, 105658; rows S30, S31)

The cell re-opens (`<status>` pending). Amendment 1 drained @344646cb6a (worker commit 88728a728e, rows S30 and S31 adopted by the issuer @5ec6cedd9c). Its
triage found a second served artifact that loses a held `multi_asset` value today, and an ARMED hazard, both in 49 Financial's Black Diamond gold:
- **T03** `data/black_diamond/scripts/gold/D_03.composition_artifacts.py:101-111`: the served `gold/views/firm_composition.json` (bucket `opal-data-bd`)
  has `total_market_value` $1,994,163,246.13 and a class sum of $1,988,724,709.05, a gap of $5,438,537.08 (the held `multi_asset`).
- **S31 (ARMED, disarm owner `2.0.0_SA_COO~M`)** `C_06.client_mix_timeseries.py:182` and `lib/mix_views.py:25`: their served run (2026-10-04) predates the table's
  `multi_asset` rows, so they lose nothing today; the next run drops the class for the 77 holders. C_06's guard (line 546) sums the aggregate over every class, as Cottonwood's did.

Do for Black Diamond exactly what the first pass did for Cottonwood (read your own diff of commit 88d22f3f84 and amendment 1's D_03 edit, and mirror them; nothing is folded):
1. `D_03` `_ASSET_CLASS_LABELS` gets `'multi_asset': 'Multi-Asset'` between `cash` and `unclassified`.
2. `C_06` `MIX_ASSET_CLASSES` gets `multi_asset` (order `equity, fixed_income, alternatives, commodities, structured, cash, multi_asset, unclassified, other`);
   its sum guard runs over the EMITTED mix and skips LOUDLY on a missing class, as in the Cottonwood C_06.
3. `lib/mix_views.py` `MIX_ASSET_CLASSES` gets `multi_asset` (the file computes `unclassified` separately; keep that).
4. Tests: in `data/black_diamond/scripts/gold/tests/test_composition_canonical.py` (granted) tests whose names contain `multi_asset` for D_03's label and a composition that
   carries the class and sums to the total; in the NEW file `data/black_diamond/scripts/gold/tests/test_mix_publishes_every_class.py` (the CTO adds its lane grant; if committing it is refused for lane,
   stop, commit the rest and say so in your report) tests whose names contain `multi_asset` for C_06 (a holder publishes a mix summing to 1;
   a class outside the list skips loudly) and for `mix_views` (the period views carry it). Run a negative control for the C_06 and D_03 tests (revert the file from `HEAD`, show the tests fail, restore).
5. The check: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/bd_mix_multi_asset_check.py` (read only, writes nothing, S3 read-only). It runs the EDITED C_06 `process_date` in process on the latest `gold/canonical/holdings`-equivalent
   partition for the BD holders that hold a `multi_asset` position (the 77), and the EDITED D_03 composition builder in process (factor out nothing; call the function the file already has, or the loop's own logic in a test harness if it has none), and prints:
   per holder the BEFORE (the live `opal-data-bd` client entity point) and AFTER shares and sums; for D_03 the live `total_market_value`, the live class sum, the AFTER class sum and the gap.
   Last line: `BD-MIX-CHECK ok=<True|False> holders=<n> after_sums_to_1=<n> composition_gap_after=<dollars>`; `ok=True` only if every holder's after-sum is within 0.001 of 1 AND the after composition class sum equals the total within $0.01.
   If a BD input needed is unreadable, stop and file a surprise row; never print `ok=True` on a partial read.
6. Criteria (amended, the issuer amends its own criteria; no limb graded the modification): AC1 selects `-k multi_asset` over BOTH the Black Diamond and Cottonwood gold tests folders;
   AC2 is the BD check above (the Cottonwood check passed at amendment 1, its output stays in the record); AC3 runs both whole folders and prints `FOLDERS-OK` only if every test passes.
7. Not in this amendment: any deploy, run or write (the issuer's act under the pair); `d08`; the Inflection `S30` row; any list the triage graded HOLDS-NONE.

## AMENDMENT 2, CORRECTION (2.0.0_SA_COO~M, 2026-10-06 ~19:5xZ) -- the two gold trees cannot share one pytest process; the registry; the rows

Worker ~20's report (amendment 2) found, and the issuer confirmed: (1) AC1 and AC3 as written ran the Black Diamond and Cottonwood tests folders in ONE pytest process. They cannot: two files
share the name `test_mix_publishes_every_class.py`, and both trees carry a `lib` package, so BD's shadows Cottonwood's. The criteria now name the Black Diamond folder only (AC1 `-k multi_asset`,
AC3 the whole folder, printing `FOLDER-OK`); the Cottonwood folder is a separate invocation, `python -m pytest -q data/cot/scripts/gold/tests` (27 passed at the drain). A compound criterion is refused, so
it stays out of the list and is reported. (2) The commit gate refused the BD `C_06` and `lib/mix_views.py` edits because `comp-constants.config.yaml` registers `MIX_ASSET_CLASSES` at both sites:
the issuer re-canonized it (canonical value, both site values, C_06's line 182 to 183) in the same commit @b71700fe64 as the worker's held edits. (3) The worker's rows W20-S6, S7 and S8 are adopted as seat rows
S32, S33 and S34 (a seat commit cannot carry a W id). AC2 is unchanged and read `BD-MIX-CHECK ok=True holders=47 after_sums_to_1=47 composition_gap_after=0.00` on the worker's tree with its held edits.
Gate limb: none graded this modification (no new order; no `<placeholders>`).

## CLOSE -- SUPERSEDED (2.0.0_SA_COO~M1, 2026-10-07, at the round-8 issuance)

`<status>` superseded, not complete: no proof instance was written for amendment 2. The cell's served change (the S29 class-list
fix for Cottonwood and Black Diamond gold) was rolled back and withdrawn: 8 S3 objects restored and read back, repo restored to
the pre-S29 bytes @a62580ef8f, ledger `secclass-s29-class-lists-m-20261006` CLOSED as ROLLED BACK (CLOUD 3bcb2d2f5a; rows
S35-S37). Andrew's rule B (six classes, no `multi_asset`) replaced the cell's premise: the 33 `multi_asset` rows were remapped
@0d9457b639, and round 8 (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) carries the remaining six-class work in SC-e-21 to
SC-e-23. Laptop 2.0.0_SA_COO~M's handoff `org/tier1_exec/2.0.0_SA_COO/handoffs/2026-10-07_0205Z.md` named this close. The worker
branch `wk-secclass-r7-20` is graded SUPERSEDED by 3.0.0_SA_CVO (6c72e70143). Gate limb: none graded this modification (no new
order; no `<placeholders>`).
