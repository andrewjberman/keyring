# TO MDPF_SECCLASS.TO-SC-e32 -- round 8 SC-e-32: FWD-17 / FWD-15 -- the old list's reclassification set, its dry-run writer and its half request

<to_id>MDPF_SECCLASS.TO-SC-e32</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~26</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-32` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-17, FWD-15 | **depends_on:** MDPF_SECCLASS.TO-SC-e26 (the old-list census and the key-form proposal),
MDPF_SECCLASS.TO-SC-e27 (the contract's declared key form), MDPF_SECCLASS.TO-SC-e31 (the AI path). Slot `~26`, third in its
queue; the issuer hands it to the slot only when all three have drained.

---

## WORKER FACE

### THE CELL

`SC-e-32`. "The old list's reclassification set: every old row not in the shared list, through the direct-match plan and then
`SC-e-31`'s path, held securities first; the row set, a dry-run writer and the half request. The write is the issuer's act"
(R8).

FWD-17 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12): "Every security the old Black Diamond list
holds has its entry in the shared list, placed again under the shared list's six classes." ACCEPT: "every security in the old
list, held today or not, has an entry in the shared list. Each was placed again under the shared list's own six classes and its
own wording, not carried across as the old list had it." FWD-15: the held securities with no entry, per firm, reach zero.

**The contract notes that bind this cell (PRD addenda v0.10 and v0.11, inlined):**
- "Six means the six asset classes": `cash`, `fixed_income`, `equity`, `structured`, `alternatives`, `commodities`
  (Andrew-direct 2026-10-07 ~00:4xZ, record
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md`:
  "there should be no multi-asset class"). The old list's four classes and its folds are not carried.
- "The whole old list, in this order: securities held today first (FWD-13 and FWD-15 depend on them), then the rest. ... Each
  remaining row goes through the direct-match plan, then the AI classifier (FWD-11), with the value bound and the index of
  AI-made rows as already set. A row nothing can place is listed UNRESOLVED by name."
- "Key forms. The old list keys some rows `NAME::<slug>`. The key form for a security with no ticker and no CUSIP is declared
  before any such row is written." Read the key form from `org/standards/MDPF_SECCLASS_CONTRACT.json` as `SC-e-27` left it. A
  row no declared key form fits is `UNPLACED-KEY` in the set, never given an invented key.
- Andrew's word covers the outside-model use at the full old-list volume (addendum v0.11; record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_0003Z_AI_CLASSIFIER_RUNS_ON_THE_FULL_OLD_TABLE.md`, "RUn on
  the full old table"). It is exercised at the ISSUER's write act, not by you.
- The shared list's precedence: a write is a conditional put on an absent key; a present key is never touched.

**Measured by the issuer 2026-10-07 (read-only scans):** DynamoDB `bd-securities` (key `ticker`) holds **10,965** rows (R8
held 10,873 from the research seat; the measured figure governs): 7,133 keyed `NAME::<slug>`, 3,825 ticker-shaped, 7 other,
0 `CUSIP:`. Its classes: equity 6,135, fixed_income 3,161, alternatives 1,654, cash 15. **2,381** of its keys are already keys
of `etf-classifications` (R8 held 2,378). `etf-classifications` holds 3,507 rows, 0 `multi_asset`, 0 `cash`.

**Inputs:**
- `SC-e-26`'s `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_CENSUS_<date>.json` (its held-today
  partition decides `held`) and `KEY_FORM_PROPOSAL_<date>.md`.
- The contract's key form after `SC-e-27`.
- The direct-match plan: `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` (`classify_asset_class`,
  `TableVocabulary`, `write`). Its rule (i) uses an old-list value only as an INPUT, and only when both the class and the
  sub-class are already members of the shared list's own vocabulary; a fold is never a match.
- The AI path: `infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py` as `SC-e-31` left it.
- The clean name: `infra/aws/lambda/v2_portal/_shared/security_name.py` `clean_name()` (`SC-e-30`).

**Build (NO table write, NO model call):**
1. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reclassify_set.py`: builds
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_20261007.tsv`, tab-separated, header
   `old_key	shared_key	held	route	asset_class	sub_asset_class	clean_name`, one line per `bd-securities` key:
   - `shared_key`: the key the row would carry in the shared list (a ticker as itself; any other form only as the contract
     declares it); blank when no declared form fits;
   - `route`: `PRESENT` (shared_key already in the shared list), `DIRECT` (the direct-match plan places it: class one of the six,
     sub-class blank or a live-table member for that class), `AI` (the plan leaves it UNRESOLVED; class and sub-class BLANK
     here, decided by the AI path at the write act), `UNPLACED-KEY` (no declared key form);
   - non-`PRESENT` rows ordered held first; `clean_name = clean_name(old row name)`.
2. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reclassify_write.py`: the writer. Default is
   a dry run. `--write` requires `--half <path>` (refuses unless both halves read SIGNED in that file) and `--snapshot <path>`.
   DIRECT rows: conditional put via `write()`. AI rows: through `SC-e-31`'s runner with its model enabled, in held-first
   order. The dry run prints `RECLASSIFY-DRY-RUN direct=<n> to_ai=<n> unplaced_key=<n> present=<n> puts=0 model_calls=0`
   and asserts both zeros (wrap the table and `send` with counters). Rollback per key: a conditional delete of a key this run
   put (`updated_by` equals the run's value), from the snapshot.
3. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_OLD_LIST_RECLASSIFY_20261007.md`:
   the half request, COO and CTO halves UNSIGNED, naming the blast radius (the one table, keys by route with counts, the
   AI-route count at the model volume Andrew's word covers), the rollback per key, and the dry-run line.

### ACCEPTANCE

<criterion id="SC8-e32-AC1" cell_refs="SC-e-32"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sc_e32_reclassify_set_check.py</invocation><expect>RECLASSIFY-SET ok=True</expect></criterion>
`SC8-e32-AC1` -- the set covers every old-list key exactly once, routes are consistent with the live table, nothing is minted, held first.

<criterion id="SC8-e32-AC2" cell_refs="SC-e-32"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reclassify_write.py</invocation><expect>puts=0 model_calls=0</expect></criterion>
`SC8-e32-AC2` -- the writer dry-runs over the set with no put and no model call.

<expected_criteria>SC8-e32-AC1,SC8-e32-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`RECLASSIFY-SET ok=False missing=OLD_LIST_RECLASSIFY_SET_20261007.tsv`);
positive control PASS (a synthetic set of PRESENT/UNPLACED-KEY over the live keys read `ok=True old_rows=10965 present=2381
unplaced_key=8584`, then deleted). AC2 FAIL as expected (no writer).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No table write, no model call, no secret read, no `--write` run.** Reads of `bd-securities` and `etf-classifications` are
  read-only scans. The write and the AI run are the issuer's act under the signed half.
- Do not edit the contract, the AI runner, `etf_classification_scheduled.py` or `security_name.py`; a gap in any becomes a
  surprise row.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W26-S<k>`), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reclassify_set.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reclassify_write.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_20261007.tsv
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_OLD_LIST_RECLASSIFY_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-32`.
<owned_cells>SC-e-32</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e32-AC1, SC8-e32-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~26/MDPF_SECCLASS.TO-SC-e32.old-list-reclassify-set.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e32-AC1,SC8-e32-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the counts per route and held, the key form used, the UNPLACED-KEY count and why, the dry-run line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ): 8 gates name the lane, all open deploy-ledger entries; none names the old-list reclassification. The write is an issuer act with its own pair and ledger entry.
comp-iam: RUN (R8 battery, DESIRED plane): 0 gap lines on etf-classifications or bd-securities. No role is declared by this cell.
comp-adversary: RUN -- R8 compose. Cell reads by the issuer 2026-10-07: bd-securities 10,965 rows (7,133 NAME::, 3,825 ticker, 7 other, 0 CUSIP:), 2,381 in both, classes equity/fixed_income/alternatives/cash; etf-classifications 0 cash rows. BLIND: the held partition (SC-e-26 measures it) and the key form (SC-e-27 declares it).
Andrew word (C-VENDOR, volume): org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_0003Z_AI_CLASSIFIER_RUNS_ON_THE_FULL_OLD_TABLE.md.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.12 FWD-15, FWD-17, addenda v0.10 and v0.11 @87ad6d2e4c; R8 @495efa3c32.
