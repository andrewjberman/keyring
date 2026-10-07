# TO MDPF_SECCLASS.TO-SC-e33 -- round 8 SC-e-33: the missing list on demand -- for each of the three firms, the held securities with no entry in the shared list and their total

<to_id>MDPF_SECCLASS.TO-SC-e33</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~23</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** placement DELL1 (the project row's `fabric` still reads laptop) | **Decomp cell:** `SC-e-33`
(`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) | **outcome_ref:** FWD-15 | **depends_on:** none (no data edge). Slot `~23`
queue: second, after `MDPF_SECCLASS.TO-SC-e24`.

---

## WORKER FACE

### THE CELL

`SC-e-33`. "The missing list on demand: for each of the three firms, the held securities with no entry in the shared list and
their total" (R8).

FWD-15 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12): "A person filling the shared list can pull,
for each firm, the held securities that have no entry, and sees the count reach zero." ACCEPT: "on demand, for each firm, a
person gets the list of held securities with no entry and its total. It reads zero for all three firms." **This cell builds
the on-demand pull.** Reaching zero is what the later writes do (`SC-e-32`, the old list's reclassification), not this cell.
A non-zero total today is the expected result, never a failure.

**Definitions (bind the script):**
- **The three firms:** `49financial`, `cottonwood`, `inflection`. Their buckets come from `firm_bucket_map()` in
  `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:180` (generated from the identity registry):
  `49financial -> opal-data-bd`, `cottonwood -> opal-data-cot`, `inflection -> opal-data-inf`. Read each firm only from its
  own bucket.
- **Held:** a security in that firm's latest SERVED Holdings build, i.e. the `HoldingsSnapshot` the Holdings producer
  `holdings_snapshot.py` publishes. Find the served address from the producer's own code and builder output
  (`lib/opal_naming.py`). Never type one by hand. Name the object you read in the file's `source`.
- **No entry:** the producer's own lookup finds nothing. Read `holdings_snapshot.py`'s classification lookup and apply the same
  keys in the same order. A security is missing when neither its symbol key nor `CUSIP:<cusip>` exists in
  `etf-classifications`, read with consistent gets. Exclude cash and non-security lines the producer itself excludes, and say
  which.
- **The shared list:** DynamoDB `etf-classifications`, us-east-1, read only.

**Build:**
1. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/missing_list.py`, the on-demand pull, read-only
   apart from its three output files. Running it with no argument writes, for each firm,
   `.../MDPF_SECCLASS_M/MISSING_LIST_<firm>_<yyyymmdd>.json` (today's UTC date) with
   `{"firm", "as_of", "source", "held_count", "missing": [{"key", "name", "cusip" (when known), "amount" (when served)}], "total"}`.
   - `total == len(missing)`.
   - It prints one line per firm, then `MISSING-LIST-PULL firms=3 total=<sum>`.
   - It finishes within 120 s.
2. Run it once and commit the three files it wrote.

### ACCEPTANCE

<criterion id="SC8-e33-AC1" cell_refs="SC-e-33"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/missing_list.py</invocation><expect>MISSING-LIST-PULL firms=3</expect></criterion>
`SC8-e33-AC1` -- the pull runs on demand for all three firms and writes their lists.

<criterion id="SC8-e33-AC2" cell_refs="SC-e-33"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/missing_list_check.py</invocation><expect>MISSING-LIST ok=True</expect></criterion>
`SC8-e33-AC2` -- each firm's list is in shape (held count printed, total equals the entries), and every listed key, plus `CUSIP:<cusip>` where an entry names its cusip, is truly absent from the table. A positive control row (AAETX) reads present.

<expected_criteria>SC8-e33-AC1,SC8-e33-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (no script); AC2 FAIL as expected
(`MISSING-LIST ok=False firms=0 of 3 listed=0 false_entries=0 control=present problems=3`). The AC2 check is the issuer's
judge: you READ it and never edit it.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **Read-only against AWS:** S3 GetObject/List on the three firms' served Holdings objects; DynamoDB GetItem/BatchGetItem on
  `etf-classifications`. No put, update, upload or deploy.
- **One firm per bucket.** Never read one firm's data from another firm's bucket or prefix (CLAUDE.md cross-firm rule).
- **No vendor or model call.**
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W23-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/missing_list.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/MISSING_LIST_49financial_*.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/MISSING_LIST_cottonwood_*.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/MISSING_LIST_inflection_*.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-33`.
<owned_cells>SC-e-33</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e33-AC1, SC8-e33-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~23/MDPF_SECCLASS.TO-SC-e33.missing-list-on-demand.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e33-AC1,SC8-e33-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** per firm, the served object read, the held count, the missing total and its served amount; the lookup rule you
mirrored (file and line); both outputs; commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery 2026-10-07 ~07:3xZ: no gate names FWD-15; the pull is on demand by design (no schedule, no monitor: CLAUDE.md moratorium).
comp-iam: RUN -- R8 battery: the pull runs under the issuer's session with read access to the three buckets and the table; no new grant.
comp-adversary: RUN -- R8 battery on the decomposition. Cell-specific reads by the issuer: firm_bucket_map at holdings_snapshot.py:180-187; the R8 "187 CUSIP: rows" and brief counts are held, not inlined as bars. BLIND: the served HoldingsSnapshot address (the worker resolves it from the producer and builder output); whether a firm's latest build predates the 2026-10-07 remap.
lane: the <paths> block IS the grant (three globs for the dated output files).
</preflight>

Source: DECOMP_R8 @495efa3c32 (origin 1640a0e86e); PRD v0.12 @87ad6d2e4c.

## AMENDMENT 1 (2.0.0_SA_COO~M1, 2026-10-07 ~09:1xZ) -- ruling on BLOCKING row W23-S4: the held set comes from a local producer build

Worker ~23 stopped under the refusal clause: the three firm buckets (`opal-data-49financial|cottonwood|inflection`) deny
`cloudops-dell1-agent-user` by resource policy (`DenyForeignFirmPrincipals`, `infra/aws/terraform/shared-infra/s3-49financial.tf:93-147`),
so the served Holdings manifests cannot be read from this box. The same wall met TO-SC-e26 (row W25-S1).

RULING (the issuer's): build the held set exactly as TO-SC-e26 did -- the Holdings producer
`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` run per firm WITHOUT `--upload` (nothing published), as-of
2026-10-05, reusing `old_list_census.py`'s `build_firm()` method or its built parquet if present under the worker's `.scratch/`.
Each `MISSING_LIST_<firm>_<date>.json` sets `"source"` to `"local producer build as-of <date> @<git HEAD>, inferred (not the served
bytes)"`. Assume no other role, read no firm bucket another way, upload nothing. Exclude the producer's cash line as the face says.
Criteria and `<paths>` unchanged (the check accepts any `source` string). The served-bytes read needs a principal the firm buckets
admit; the issuer carries that to 1.0.0_SA_CTO~DELL1 at the drain end. Gate limb: none graded this modification.

