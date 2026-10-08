# TO MDPF_STRATID.TO-ST-t4 -- round 1 ST-t-4: READ-ONLY census of Eclipse (Inflection) sleeve names carrying an Opal ETF
<to_id>MDPF_STRATID.TO-ST-t4</to_id>
<project>MDPF_STRATID</project>
<issued_to>0.9.0_WK_MDPF_STRATID~3</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `ST-t-4` (`decompositions/MDPF_STRATID_DECOMP.md`, ROUND 1) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`ST-t-4`. An Opal ETF Strategy is a client SLEEVE (a whole model or sub-portfolio) whose NAME carries an Opal ETF's ticker as a whole
word, or its full fund name. It must be found in SmartX, Rebalancer and Eclipse alike. SmartX and Rebalancer have name rules today;
Eclipse (Inflection) has none, and nobody has looked for such sleeves there. You look, and write down what you found with the
denominator. You build nothing.

**What to look for.** Tickers, as whole words, case-insensitive: `DIVZ`, `IDVZ`, `PFDE`, `PFOE` (the Opal ETF list,
`s3://opal-data-etfs/config/etf_universe.json`, 4 tickers today -- read it and use what it holds). Full names: "Pathfinder Disciplined",
"Pathfinder Focused Opportunit" (measured prior art in `data/assets/scripts/silver/rebalancer_schemas.py:218-223`), any name containing
"Opal" plus a fund word, e.g. "Opal Dividend Income". Report every name containing "Opal" separately so a reader can judge.

**Where.** `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:82` `ECLIPSE_SILVER = "eclipse/inflection/silver"` (and :18: the
Inflection model path is Eclipse). Find the bucket and the silver table(s) that carry model / sleeve / portfolio names (read the code
that reads `ECLIPSE_SILVER`). Read the latest partition, and as many earlier ones as fit your time.

**Write** `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~3/ECLIPSE_SLEEVE_NAME_CENSUS.md`, which must contain
these lines at the start of a line:
- `SOURCE:` the exact s3 objects read (bucket/key, partition dates);
- `DENOMINATOR:` an integer, the count of DISTINCT names scanned;
- `RESULT:` `FOUND <n>` or `NONE-FOUND` (a zero stated with its denominator, never as absence);
then a table: name, match (ticker / full name / Opal-only), dollars and accounts on the latest date if the table carries them, and the
column the name came from. Close with what you could NOT read (a table you could not open is a stated blindness, not a zero).

### ACCEPTANCE

<criterion id="ST1-t4-AC1" cell_refs="ST-t-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/st_t4_census.py</invocation><expect>CENSUS-OK</expect></criterion>
`ST1-t4-AC1` -- the census document exists with its SOURCE, DENOMINATOR and RESULT lines.

<criterion id="ST1-t4-AC2" cell_refs="ST-t-4" judgment="true"/>
`ST1-t4-AC2` -- JUDGMENT (graded by `3.0.0_SA_CVO` at L9, not by you): the census read the table(s) that actually carry Eclipse sleeve
names, and its RESULT follows from its table.

<expected_criteria>ST1-t4-AC1 ST1-t4-AC2</expected_criteria>

Run the invocation from the worktree root. At the base (2026-10-08 ~20:5xZ): AC1 `CENSUS-BAD no file ...`. Record AC2 in the instance as
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; never PASS or FAIL it.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only AWS only** (S3 GetObject / List). No write anywhere in AWS. Edit no code.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_STRATID-W3-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below. Rows are APPEND-ONLY.

<paths>
org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~3/ECLIPSE_SLEEVE_NAME_CENSUS.md
org/missions/D8/MDPF/MDPF_STRATID/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP.md</decomp_doc> (round 1, the thread), cell `ST-t-4`.
<owned_cells>ST-t-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: ST1-t4-AC1, ST1-t4-AC2. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~3/MDPF_STRATID.TO-ST-t4.eclipse-sleeve-name-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> ST1-t4-AC1 ST1-t4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the document path, the RESULT and DENOMINATOR lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE read-only census.
comp-iam: DECLARED-NOT-APPLICABLE read-only S3 under the reading seat's own credentials; writes nothing in AWS.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: LOCAL -- a document; no served path.
direct_act: false -- carries a judgment criterion graded at L9.
</preflight>

Source: PRD v0.3 OPEN ITEM 1, C-SLEEVE, surface S04; decomposition round 1 ruling R4.
