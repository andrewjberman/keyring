# TO ADVI_COTBKF.TO-CB-t-2.sweeps-v2-core -- round 20 CB-t-2: sweeps-v2, the custodian's core position under rule (b), re-graded

<to_id>ADVI_COTBKF.TO-CB-t-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~41</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-t-2` (`decompositions/ADVI_COTBKF_DECOMP.round20.md`) |
**outcome_ref:** FWD-3 | **depends_on:** `CB-t-1`

---

## WORKER FACE

### THE CELL

FWD-3 and the chain as in CB-t-1 (same worker, continued). After CB-t-1, `commonwealth_sweep_regrade.py` persists month grades
(`month_grades_before.parquet`, `month_grades_after.parquet`) and takes `--before-list` / `--after-list`; `commonwealth_mover_classes.py`
classes the 163 round-19 MATCH -> DIFF months (`deliverables/0.9.0_WK_ADVI_COTBKF~41/mover_classes.parquet`).

**Your item (the CTO's round-19 analysis, E2, and its ruling on row D2-S30).** The ruling: "A security goes on the declared sweep
list when it is EITHER (a) a bank deposit sweep by its stated source; OR (b) the custodian's designated core cash position for the
account. The list entry for (b) names the custodian's designation (the custodian's own documentation or account data naming it the
core position) and a list-level behavior census: accounts holding it, the share of its rows paired same-day with another CUSIP, and
its dividend cadence. Membership is still decided per CUSIP on the list, never per row. A security not on the list is never cash."
"316067107 (Fidelity Government Cash Reserves) goes on the list, sweeps-v2, under (b) ... If no designation can be cited, the entry
does not land and the cell says so." "The other 22 money-market funds stay off ... E2 lists any that do, and adds none."
1. `commonwealth_sweeps.py`: `SWEEP_LIST_VERSION` sweeps-v2-<date>, keep v1 reachable (the runner's `v1`); each entry carries its rule
   (`a` / `b`). Add 316067107 under (b) ONLY with a designation source line you can cite from data already in the repo or already
   readable by the chain (a vendor field, a statement line, a custodian document in the repo); if none can be cited, leave it off,
   and say so in the report and a row. Print the behavior census for 316067107 (accounts, rows, first date, share same-day paired,
   dividend months) and the same census for every other `CANDIDATES_REJECTED` entry with reason MMF, as a list only;
2. re-grade with `--before-list v1 --after-list v2`, `--out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41/v2`:
   whole grade before and after, and the 163 months of `mover_classes.parquet` with their v2 result, counted per class. The CONTROL is
   now months of accounts with no listed sweep or core position on or before the month. Keep the runner's LAST line format.

Tests in `data/assets/scripts/silver/tests/test_commonwealth_sweeps.py` (stubs): a same-day `sl` of a (b) core entry paying an `lo`
moves the value once; an MMF not on the list with core-like behavior is NOT cash; an entry under (b) without a designation source is
refused by the list's own check.

### ACCEPTANCE

<criterion id="CB20t2-AC1" cell_refs="CB-t-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_sweeps.py</invocation><expect>passed</expect></criterion>
`CB20t2-AC1` -- the (b) core entry moves a funded withdrawal once; the list governs over behavior; no (b) entry without a source.

<criterion id="CB20t2-AC2" cell_refs="CB-t-2"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v2 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41/v2</invocation><expect>control_same=True</expect></criterion>
`CB20t2-AC2` -- v1 -> v2 re-graded, the 163 shown with their result, months of accounts with no listed position unmoved.

<criterion id="CB20t2-AC3" cell_refs="CB-t-2" judgment="true"/>
`CB20t2-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the (b) entry's source line is the custodian's own designation of a core position (or its absence is stated and the entry is off), and no MMF listed by census alone was added.

<expected_criteria>CB20t2-AC1,CB20t2-AC2,CB20t2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return or month that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W41-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_zero_amount_flows.py
data/assets/scripts/silver/tests/test_commonwealth_mover_classes.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round20.md</decomp_doc> (round 20), cell `CB-t-2`.
<owned_cells>CB-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB20t2-AC1, CB20t2-AC2, CB20t2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41/ADVI_COTBKF.TO-CB-t-2.sweeps-v2-core.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB20t2-AC1,CB20t2-AC2,CB20t2-AC3` BEFORE the flip. Mechanical: CB20t2-AC1,
CB20t2-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SWEEP-REGRADE line, the v2 list with each entry's rule and source, the MMF census list, the 163 per class after v2, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the (b) entry lands only with a cited designation; census informs, never decides; BLIND: a designation held only in documents outside the repo (the laptop's restricted statements), which makes the entry refuse rather than land.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-19 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_19_20261008.md` @c015b6de3d (msg 1355), section 1 and E2; row D2-S30.
