# TO MDPF_STRATID.TO-ST-t1 -- round 1 ST-t-1: the Cottonwood slice measures, per Opal SMA sleeve, the dollars also inside a Model
<to_id>MDPF_STRATID.TO-ST-t1</to_id>
<project>MDPF_STRATID</project>
<issued_to>0.9.0_WK_MDPF_STRATID~1</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `ST-t-1` (`decompositions/MDPF_STRATID_DECOMP.md`, ROUND 1) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`ST-t-1`. FWD-1 needs Cottonwood's PFDE sleeve added to the Global total exactly once. A sleeve account that ALSO carries an Opal
Model assignment on the same date may already be inside a Model figure, so its dollars must be known before anything is added. Your
job is to measure that, per Opal SMA member and date, where the sleeve is first named: the Cottonwood slice.

**The estate, read at the base.**
- `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`: `build_slice(dates, gold_by_date, ...)` (:602). At :615-630 it pulls Opal SMA
  sleeves out FIRST, by name, with `rs.opal_sma_member_of(model_name)` (`data/assets/scripts/silver/rebalancer_schemas.py:226`), from
  model-level rows (`dollar_value`, `account_count` per model per date) -- no account ids reach it. Each SMA member lands in `by_model`
  as `{"display_name", "cohort_class": "sma", "model_value": [...], "account_count": [...]}` aligned to `dates`. The slice reads
  `s3://opal-data-assets/blackdiamond/cottonwood/...` (bucket constant `ASSETS_BUCKET` :130; silver reads at :528, :582).
- Account -> model assignments exist in Rebalancer silver: `rebalancer_schemas.ASSIGNMENT_COLUMNS` (:164, starts `account_id`). Find
  the silver table/prefix that carries them under `blackdiamond/cottonwood/silver/` (read the silver writer beside `rebalancer_schemas.py`
  in `data/assets/scripts/silver/`).
- Opal Model vs sleeve: a model name is an Opal Model when the slice keeps it as a model (`model_key_of`, `CANONICAL_KEY`/`CUSTOM_KEY`);
  it is a sleeve when `opal_sma_member_of` returns a member. Prior art for the same overlap question on Tax: the TaxSMA BASE_OVERLAP
  control (`data/mdpf/tests/taxsma/test_taxsma_cot_global_fold.py`, and the `taxsma_reconcile` module it imports) -- read it and reuse
  its notion of "model-assigned population" where it fits.
- Served today (2026-10-07): `pfde` 412,892.63, 4 accounts; `divz` 1,369,406.08.

**Build:**
1. `measure_sma_overlap(s3, value_date: str) -> dict` in `build_cottonwood_mdpf_slice.py`: reads that date's Rebalancer assignment rows
   (read-only) and returns, per Opal SMA member present that date, `{"sleeve_accounts": int, "overlap_accounts": int, "overlap_dollars":
   float}` -- `overlap_accounts` = sleeve accounts that also carry an Opal Model assignment that date; `overlap_dollars` = those accounts'
   dollars IN THE SLEEVE. No assignment rows for the date -> return `None` (not measured), never `{}` read as zero.
2. `build_slice` writes `overlap_model_value` on every `cohort_class: "sma"` by_model entry: a list aligned to `dates`, the member's
   `overlap_dollars` per date, `None` where unmeasured. Give `build_slice` the per-date measurements as an optional argument (default
   None -> every slot None) so existing callers and tests keep working; wire the real reader where the slice is run for upload.
3. NO served figure moves: `model_value`, `account_count`, `model_aua`, `non_model_aua` and the category tree stay byte-identical for the
   same inputs. The new key is the only change to the artifact.
4. Tests in NEW `data/assets/scripts/gold/tests/test_cottonwood_sma_overlap.py` (stub S3 / DataFrames, no network), these exact names:
   `test_overlap_zero_when_no_sleeve_account_has_a_model`, `test_overlap_counts_dollars_of_sleeve_accounts_with_a_model`,
   `test_overlap_none_when_assignments_absent_for_date`, `test_overlap_field_aligned_to_dates`. Copy the import preamble of
   `test_cottonwood_custom_and_sma.py` (sys.path for gold, silver and mdpf gold).

### ACCEPTANCE

<criterion id="ST1-t1-AC1" cell_refs="ST-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/st_t1_tests.py</invocation><expect>T1-OK</expect></criterion>
`ST1-t1-AC1` -- the four named tests pass.

<criterion id="ST1-t1-AC2" cell_refs="ST-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/st_t1_regress.py</invocation><expect>T1-REGRESS-OK</expect></criterion>
`ST1-t1-AC2` -- the existing `test_cottonwood_custom_and_sma.py` still passes (no served figure moved).

<criterion id="ST1-t1-AC3" cell_refs="ST-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/st_t1_live.py</invocation><expect>LIVE-OK</expect></criterion>
`ST1-t1-AC3` -- the seam probe: `measure_sma_overlap` on the real silver for the served slice's last date returns a well-formed `pfde`
row (read-only S3).

<expected_criteria>ST1-t1-AC1 ST1-t1-AC2 ST1-t1-AC3</expected_criteria>

Run each invocation from the worktree root. At the base (2026-10-08 ~20:5xZ): AC1 `T1-BAD no file ...`; AC2 `T1-REGRESS-OK` (regression
guard); AC3 `LIVE-BAD no measure_sma_overlap ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only AWS only** (S3 GetObject / List on `opal-data-assets`). No S3 write, no `--upload` run, no Lambda invoke, no deploy. Every
  deploy is the issuer's, at the drain.
- Do not edit `rebalancer_schemas.py`, the matcher, the registry, or anything under `data/mdpf/`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_STRATID-W1-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken a check. Rows are APPEND-ONLY. If the assignment rows cannot tell an Opal Model from a sleeve, that is a
  BLOCKING row, not a guess.

<paths>
data/assets/scripts/gold/build_cottonwood_mdpf_slice.py
data/assets/scripts/gold/tests/test_cottonwood_sma_overlap.py
org/missions/D8/MDPF/MDPF_STRATID/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP.md</decomp_doc> (round 1, the thread), cell `ST-t-1`.
<owned_cells>ST-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: ST1-t1-AC1, ST1-t1-AC2, ST1-t1-AC3. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~1/MDPF_STRATID.TO-ST-t1.sleeve-overlap-at-intake.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> ST1-t1-AC1 ST1-t1-AC2 ST1-t1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the PFDE row AC3 printed, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule change.
comp-iam: RUN at L5 (decomposition ROUND 1 battery): one new read under s3://opal-data-assets/blackdiamond/cottonwood/silver/, the prefix family the slice already reads; runtime role (EC2 MDPF daily runner) unmapped by comp-iam, DESIRED plane only; APPLIED read at the drain.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: SERVED -- a served data path (the Cottonwood slice artifact gains a field); the deploy is the issuer's at the drain.
direct_act: false -- the class is SERVED.
</preflight>

Source: PRD v0.3 ENDPOINT FWD-1, C-OVERLAP; decomposition round 1 hop 1b, ruling R3.
