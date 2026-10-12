# TO MDPF_SECCLASS.TO-SC-e98 -- round 23 SC-e-98: READ: who holds the rebuilt 2026-10-09 Unclassified, by security, and why no classifier places it

<to_id>MDPF_SECCLASS.TO-SC-e98</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~87</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-98` (`decompositions/MDPF_SECCLASS_DECOMP_R23.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-22 analysis section 3 item 2, msg 4333

---

## WORKER FACE

### THE CELL

`SC-e-98`, row MDPF_SECCLASS-D1-W80-S4 (the unlisted dollars). The CTO ruled that the dollars **no classifier places stay Unclassified, listed
by security with the reason, and no class is invented for them**. The list is the input to the NEXT classifier cell; this cell only reads. At
2026-10-09 the served firm Unclassified is $1,846,399.46 and a rebuild from the current canonical partition and the current classifier reads
$883,483.05 (SC-e-95's record `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESIDUAL_READ_C06_FREEZE_20261012.json`, section
`unlisted_unclassified` and the `dates` entry for 2026-10-09). Of that, $210,486.42 across 22 blank-ticker positions sits outside every
relationship's stored top-10 list.

**Read-only, in memory, no S3 or table write.**

1. **Rebuild 2026-10-09 from the CURRENT canonical partition** through the module's own path (`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`
   `load_static_tables` once, then `process_date`; import it, do not copy it). The class-sum Unclassified you obtain is `total_unclassified_usd`
   and must agree with SC-e-95's rebuilt $883,483.05 to the cent or you say why in a surprise row (partition versions may have moved since).
2. **By security.** For every position that resolves `unclassified`, aggregate by security (ticker, or the name where the ticker is blank): `usd`
   (market value summed), `positions` (count), and the reason the classifier did not place it, from the classifier's OWN branch for that input
   (`lib/etf_classifier.py` and `classify_series` in C_06; for example no ticker and no `NAME::` row, a ticker with no classification row, a name
   row that resolves to no class). Declare the closed set of `reason_codes` you used, each with a one-sentence `meaning`; a security's
   `reason_code` is one of them and its `reason` is the specific sentence.
3. **`listed_in_stored`.** True where that security's holding appears in any relationship's stored top-10 concentration list for 2026-10-09
   (read the stored `gold/entities/clients/{rid}.json` entries; bounded concurrency; aggregate only, never print a relationship id), false where it
   appears in none. `unplaced_subset` is the sum over the `false` securities (the CTO's $210,486.42; if it reads differently say so).
4. **The record**, `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNLISTED_UNCLASSIFIED_20261009_BY_SECURITY_20261012.json`, with the keys listed
   in `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_CHECKS/r23_checks.py` (header, `unlisted`), at most 400 securities (aggregate
   the tail into one `OTHER` security per reason code, with its positions, if there are more), `tolerance_usd` at most 250 (the code rounds each
   relationship's mix to six places, row D1-W85-S6, so class dollars and position dollars differ by up to $128.58).

### ACCEPTANCE

<criterion id="SC23-e98-AC1" cell_refs="SC-e-98"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_CHECKS/r23_checks.py unlisted org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNLISTED_UNCLASSIFIED_20261009_BY_SECURITY_20261012.json</invocation><expect>UNLISTED ok=True</expect></criterion>
`SC23-e98-AC1` -- the record exists, the securities sum to the rebuilt Unclassified within the tolerance, every security carries a declared reason code and a
reason, the unplaced subset equals the sum of the unlisted securities, no relationship, account or client key appears, and a copy with one field
broken fails the same check first.

<expected_criteria>SC23-e98-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-12 ~11:3xZ): `UNLISTED ok=False error=absent`; a synthetic valid record reads `ok=True control=ok`; one
whose securities do not sum to the total, one with an undeclared reason code and one carrying a `relationship_id` key each read `ok=False`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, list_object_versions, DynamoDB get_item, ec2 describe): no write to any bucket or table, no deploy, no
  invoke. Never push.
- A command that needs more than `timeout 120` runs in the background (`run_in_background`) and is read when it ends; the static-table load is the
  slow part: do it once per process.
- **Client data stays out.** Security-level and aggregate figures only: no relationship id, account id or client name in the record, the report or a
  surprise row. A security name is a market name (an issuer and a maturity), never an account's.
- **Refusal clause.** If a figure cannot be read as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W87-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not estimate a figure and do not fill a field you did not read.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNLISTED_UNCLASSIFIED_20261009_BY_SECURITY_20261012.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R23.md</decomp_doc> (round 23), cell `SC-e-98`.
<owned_cells>SC-e-98</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC23-e98-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~87/MDPF_SECCLASS.TO-SC-e98.unclassified-by-security-read.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC23-e98-AC1`.
</proof_of_spec>

**REPORT:** the rebuilt total against SC-e-95's, the reason codes with their dollars and positions, the unplaced subset, the top ten securities by
dollars, whether any reason code is one a classifier change could clear (say which, in a sentence, without recommending), commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE a read the seat's role already makes (the same reads as SC-e-95).
comp-adversary: RUN -- a list that sums to something other than the rebuilt total (the checker refuses it within the tolerance); a reason typed from the security's look instead of the classifier's branch (the code set is declared and every security names one); a stored-list flag read on a stale date (the date is fixed and the partition version is named in the claim); a relationship key leaking into a security row (the checker refuses it). BLIND: a position the classifier places differently on a later partition version; the claim names the version read.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-22 analysis section 3 item 2 (msg 4333); row D1-W80-S4; SC-e-95's record; DECOMP_R23.
