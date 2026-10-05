# TO MDPF_SECCLASS.TO-SC-e16 -- round 7 SC-e-16: the BLOOMBERG-namespace reader census -- every reader of etf-classifications exercised on a BBG row

<to_id>MDPF_SECCLASS.TO-SC-e16</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~13</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-16` (`decompositions/MDPF_SECCLASS_DECOMP_R7.md`) |
**outcome_ref:** FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-16`. FWD-9 puts every Rival Funds stock into DynamoDB `etf-classifications`. Of 822 securities, 516 are non-US with no
ISIN or CUSIP. 1.0.0_SA_CTO RULINGS batch 257 Q1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`)
keys them in a third namespace:
- `ticker` = `BBG:<ticker>:<exch>`, with no whitespace (for example `BBG:REL:LN` from `REL LN Equity`);
- `identifier_namespace` = `BLOOMBERG`;
- `security_bloomberg` = the Bloomberg id verbatim (`REL LN Equity`), in its own attribute.

The census comes FIRST. Before any such row is written, prove that every reader of the table tolerates one. **No reader may
crash, refuse the row, mis-key it as a US ticker, or fail a strict contract.** The named risk is the Holdings contract
`docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` (`additionalProperties:false`).

The reader set is round 6's model-row census
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_MODEL_READER_CENSUS_20260930.json` (34 readers). Its check
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_model_reader_census.py` is the pattern to follow.

**Build (LOCAL build + record: no table write):**
1. **Find every reader.** Re-run the search with the comp tools, printing each denominator: `comp-find 'etf-classifications'`,
   `comp-find 'etf_classifications_dynamodb'`, `comp-find 'identifier_namespace'`. Start from the R6 census's 34 readers and
   add any new ones.
2. **Exercise each reader.** Run its REAL read or classification function, stubbing only the table, on a synthetic row:
   `{"ticker": "BBG:REL:LN", "identifier_namespace": "BLOOMBERG", "security_bloomberg": "REL LN Equity",
   "asset_class": "equity", "sub_asset_class": "Developed", "instrument_kind": "single_security", "classified_by":
   "scheduled", "listing_country": "GB", "low_confidence": false}`.
   Then run it a second time with `sub_asset_class` absent and `low_confidence: true`.
   - Record one verdict per reader: `TOLERATES`, `CRASHES`, `REFUSES`, `MISKEYS` (treats the key as a bare US ticker, or
     matches it to a holding by `ticker` text) or `FAILS-CONTRACT`, with the evidence line.
   - A reader you cannot exercise (a portal TypeScript mapping) is `READ-ONLY`, with the exact line that decides it.
   - Where a reader serves through a strict contract (Holdings), validate the served node against that contract.
3. **The check.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_bbg_reader_census.py` runs the
   exercises.
   - It writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_BBG_READER_CENSUS_20261005.json`, shaped
     `{"readers": [{"path", "function", "verdict", "evidence"}], "denominator", "search": [...]}`.
   - It prints `BBG-READER-CENSUS readers=<n> tolerates=<n> read_only=<n> crashes=<n> refuses=<n> miskeys=<n> fails_contract=<n>`.
   - It also prints `BBG-READER-TOLERATED` when crashes, refuses, miskeys and fails_contract are all 0.

### ACCEPTANCE

<criterion id="SC7-e16-AC1" cell_refs="SC-e-16"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_bbg_reader_census.py</invocation><expect>BBG-READER-CENSUS readers=</expect></criterion>
`SC7-e16-AC1` -- the census of every reader of the table on a BLOOMBERG row exists, one verdict each.

<expected_criteria>SC7-e16-AC1</expected_criteria>

Dry-run at the base 2026-10-05: AC1 has no such check yet, so it FAILS as expected.

**If a reader does not tolerate the row:** that is the finding this cell exists to surface. The census is the deliverable; the
tolerance bar gates the ROWS ACT (round 6 precedent, TO-SC-e15 amendment 1). Do not change the reader (it is outside your
grant). File a surprise row naming the reader, and report.

**Import note (1.0.0_SA_CTO DECISION 103371):** no import in a runner-deployed script changes, so the deployed-layout criterion
does not apply.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **LOCAL.** No table write. Live reads of the table are allowed.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W13-S<k>`), and do not weaken the check.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_bbg_reader_census.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_BBG_READER_CENSUS_20261005.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R7.md</decomp_doc> (round 7), cell `SC-e-16`.
<owned_cells>SC-e-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC7-e16-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~13/MDPF_SECCLASS.TO-SC-e16.bbg-namespace-reader-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC7-e16-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the search denominators, the census line, one line per reader with its verdict, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE -- no new call; readers run with the table stubbed.
comp-adversary: RUN -- 1 ruling read (batch 257 Q1), 1 census read (R6: 34 readers), 1 contract read (MDPF_SECCLASS_CONTRACT 0.3.0 identifier_namespace values TICKER/CUSIP: BLOOMBERG needs contract 0.4.0 before the ACT, asked of 1.0.0_SA_CTO at issuance); BLIND: readers added since round 6 (step 1 measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.3 addendum @ffb329af49; RULINGS batch 257 @a272c26a75; intake @320b02aa6b.
