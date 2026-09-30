# TO MDPF_SECCLASS.TO-SC-e15 -- round 6 SC-e-15: the MODEL_ROWS reader census -- every reader of etf-classifications exercised on a model row

<to_id>MDPF_SECCLASS.TO-SC-e15</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~12</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-15` (`decompositions/MDPF_SECCLASS_DECOMP_R6.md`) |
**outcome_ref:** FWD-4, FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-15`. Round 4 classified 357 securities with the Kimi K3 model. 260 have a class, 130 of them with confidence below
0.80. The planned write puts them into `etf-classifications` as NEW rows (conditional on absence) with
`classified_by = "model"`, a number `classification_confidence` and a boolean `low_confidence`. Census and half:
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R4_MODEL_CLASSIFY_CENSUS_20260930.json` and
`NEVER_WIDEN_HALF_REQUEST_SECCLASS_MODEL_ROWS_20260930.md` (same directory). The contract is
`org/standards/MDPF_SECCLASS_CONTRACT.json` (0.3.0).

Andrew's word governs the flag (recorded @6a861c4e18): "We don't need a human review for that, what would be better is a
flag if Kimi has lower confidence." So flagged rows will be WRITTEN and SERVED. 1.0.0_SA_CTO's ruling (rounds 4-5
analysis @533bcae124, ruling 2): before the half is signed, prove that every reader of `etf-classifications` tolerates a
model row. **No reader may crash, refuse the row, or fail a strict contract on the new enum value or the new
attributes.** The named risk is the Holdings contract
`docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` (`additionalProperties:false`; row IRPT_BCKEND-W93-S1).

**Build (LOCAL build + record: no table write):**
1. **Find every reader.** Start from the reader census of round 3 (`R2_CUSIP_CENSUS_20260930.json` key `readers`, 18
   readers) and the PRD's surface manifest (`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` section 7).
   Re-run the search yourself with the comp tools (`comp-find 'etf-classifications'`, `comp-find 'classified_by'`,
   `comp-find 'etf_classifications_dynamodb'`), printing each denominator. The census must include at least: the IRPT
   Holdings producer `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, the BD library
   `data/black_diamond/scripts/gold/lib/etf_classifier.py`, the one client and its two Lambda copies, the portal's
   asset-class mapping, and IRPT_DASHBD's C-CLASSES consumer (find it under `org/missions/D9/IRPT/IRPT_DASHBD/`).
2. **Exercise each reader.** For each reader, run its REAL classification or read function (import it; stub only the
   table) on a synthetic model row built from a real R4 result, for example
   `{"ticker": ..., "asset_class": ..., "sub_asset_class": ..., "classified_by": "model",
   "classification_confidence": 0.62, "low_confidence": true}`. Record one verdict per reader: `TOLERATES`, `CRASHES`,
   `REFUSES` or `FAILS-CONTRACT`, with the evidence line. A reader you cannot exercise (a portal TypeScript mapping, say)
   is read and marked `READ-ONLY` with the exact line that decides it; never mark it TOLERATES without that line.
   Where a reader serves through a strict contract (Holdings), validate the served node against that contract.
3. **The check.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_model_reader_census.py` runs the
   exercises, writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_MODEL_READER_CENSUS_20260930.json`
   (`{"readers": [{"path", "function", "verdict", "evidence"}], "denominator", "search": [{"pattern", "hits",
   "files"}]}`) and prints `MODEL-READER-CENSUS readers=<n> tolerates=<n> read_only=<n> crashes=<n> refuses=<n>
   fails_contract=<n>`. When crashes, refuses and fails_contract are all 0, it also prints `MODEL-READER-TOLERATED`.
4. **The half's census section.** Append `## Reader census (SC-e-15)` to the MODEL_ROWS half: the check's lines
   verbatim, one line per reader with its verdict, and the sentence that the MODEL_ROWS act is REFUSED unless a fresh
   census immediately before it prints `MODEL-READER-TOLERATED`. Edit no other section.

### ACCEPTANCE

<criterion id="SC6-e15-AC1" cell_refs="SC-e-15"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_model_reader_census.py</invocation><expect>MODEL-READER-CENSUS readers=</expect></criterion>
`SC6-e15-AC1` -- every reader of the table tolerates a model row (none crashes, refuses it or fails a strict contract).

<criterion id="SC6-e15-AC2" cell_refs="SC-e-15"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_MODEL_ROWS_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC6-e15-AC2` -- the MODEL_ROWS half still reads HALF-READY with its reader census section.

<expected_criteria>SC6-e15-AC1,SC6-e15-AC2</expected_criteria>

Dry-run at the base 2026-09-30 19:3xZ: AC1 no such check (FAIL as expected); AC2 HALF-READY already (the half exists from
SC-e-10; the criterion binds the file after step 4, and the section's presence is read by the issuer at the drain).

**If a reader does not tolerate the row:** that is the finding this cell exists to surface. Do not change the reader
(outside your grant) and do not weaken the check. Write the verdict into the census and the half, file a surprise row,
and report AC1 as failed with the reader named.

**Import note (1.0.0_SA_CTO DECISION 103371):** this cell changes no import in a runner-deployed script, so the
deployed-layout import criterion does not apply.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write. Readers are exercised with the table stubbed; live reads of the table are
  allowed.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W12-S<k>`), and do not weaken the test to pass.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_model_reader_census.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_MODEL_READER_CENSUS_20260930.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_MODEL_ROWS_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R6.md</decomp_doc> (round 6), cell `SC-e-15`.
<owned_cells>SC-e-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC6-e15-AC1, SC6-e15-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~12/MDPF_SECCLASS.TO-SC-e15.model-rows-reader-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC6-e15-AC1,SC6-e15-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the search denominators, the census line, one line per reader with its verdict, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE -- no new call; readers run with the table stubbed.
comp-adversary: RUN -- 1 ruling read (rounds 4-5 analysis ruling 2), 1 census read (R4_MODEL_CLASSIFY_CENSUS: 260 classified, 130 flagged of 357), 1 contract read (Holdings additionalProperties:false, W93-S1); BLIND: the reader set beyond round 3's 18 is unmeasured (step 1 measures it).
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO rounds 4-5 analysis @533bcae124 section 4 item 4 and ruling 2; Andrew-direct @6a861c4e18.

## AMENDMENT 1 (2.0.0_SA_COO~M, 2026-09-30 ~23:0xZ) -- the cell delivers the census; tolerance gates the act

Ruling on the worker report (AC1 FAIL: `MODEL-READER-CENSUS readers=34 tolerates=22 read_only=8 crashes=3 refuses=0
fails_contract=1`; rows W12-S1 BLOCKING/ARMED, W12-S2 BLOCKING/INERT). The census is complete (34 readers, 0 uncensused of
60 tracked code files) and did exactly the job the CTO's rounds 4-5 ruling 2 set: find the readers that do not tolerate a
model row BEFORE the MODEL_ROWS half is signed. What this cell delivers is the census and the half's census section. The
"every reader tolerates" bar is the MODEL_ROWS ACT's precondition, and the half already states it: the act is REFUSED
unless a fresh census immediately before it prints `MODEL-READER-TOLERATED`. So AC1's expectation moves from
`MODEL-READER-TOLERATED` to the census line `MODEL-READER-CENSUS readers=`. The tolerance bar is RELOCATED to the act, not
lowered: the MODEL_ROWS half stays UNSIGNED and the act cannot run while the census reads crashes=3 fails_contract=1.

- W12-S1 (`seed-etf-classifications.py` `merge_item` keeps `classification_confidence` / `low_confidence` on a seed-corrected
  model row) and W12-S2 (`ETFClassifier.classify_holdings` KeyError on alternatives / commodities / structured, pre-existing,
  zero callers) route to round 7 as repairs through the round-6 L10 packet. Whether a zero-caller method counts as a reader
  is left to 1.0.0_SA_CTO with that packet; the W12-S1 contract break needs a fix either way.
- Re-validate the proof against the amended AC1 (VALID rc=0), flip `<status>` to complete, commit.

Gate limb: none graded this modification (a modification of an existing order; LIMB 6 fires on new orders only; no
placeholders declared).
