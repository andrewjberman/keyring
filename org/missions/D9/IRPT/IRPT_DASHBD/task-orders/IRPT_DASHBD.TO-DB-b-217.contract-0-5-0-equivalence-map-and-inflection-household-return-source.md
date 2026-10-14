# TO IRPT_DASHBD.TO-DB-b-217 -- the CONTRACT 0.5.0: an equivalence map (members that name the same quantity for the same entity compare as one figure) and the household return sourced from Orion's client grain for Inflection only; every earlier live criterion still passes (14 of them)

<to_id>IRPT_DASHBD.TO-DB-b-217</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~175</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>110</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-110 ANALYSIS section 1 (rows "Why the whole-document rule missed count 2" and "household returns from Orion's client grain") and section 2 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_110_20261014.md`) | **Rows:** IRPT_DASHBD-D2-W175-S<k> | **Decomp cell:** `DB-b-217` (decomposition section 112) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-175` (branch `wk-IRPT_DASHBD-175`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/`. Commit with `.tools/safe-commit.sh` and your author line; never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`; an account's last four characters and any household or client id are never written in the repo, a row or your report: counts, hashes and words only.

**Why.** The CVO graded the first Inflection render FAIL (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_109_L9_GRADE_20261014.md`). One count: the gain/loss "Ending Value" printed "Not available yet" for accounts whose ending values print on the overview, and the whole-document rule read 0 conflicts, because the two cells are DIFFERENT contract members (`glr.ending_value` and `avs.<window>.ending_value`) with the SAME meaning and the rule compares member ids. The CTO's ruling: the contract gains an EQUIVALENCE MAP, and the checkers compare through it. The CTO also ruled (round 110 row 3): the household return for Inflection comes from Orion's `fact_performance` at the CLIENT grain, with its source claimed; account returns stay NO_SOURCE_YET. This order edits the contract only; the sample (`DB-b-222`) and the render (`DB-b-223`) follow in your queue.

**The cell (`DB-b-217`).**
1. **Read first.** The contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (0.4.3) with its `change_rule`, `read_rule` and `open_changes`; the last bump's commit (`git show fc69a8f606`) to see exactly what a bump touches (the version, the `lineage` entry carrying the OLD bytes' sha256 and a reason, the changed text; nothing else); the issuer's check `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_inflection.py` (function `check_contract` is your criterion: read it fully); the round-108 read of Orion's tables `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~172/COVERAGE_READS_R108.json` and `READ_COVERAGE_RUN_R108.json` (the performance table's shape; it is keyed by client, has no account key, and is cumulative: read the NEWEST dated partition only); the adapter `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py` (its GET-only reader is the only way you read S3).
2. **Run the earlier criteria first.** Run each of these 14 invocations from the repo root and record PASS or FAIL: `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/<dir>/<file>" . <ID>` for DB104-1-AC1, DB104-4-AC1 and DB104-5-AC1 (`r104/p104_round104.py`; DB104-2-AC1 and DB104-3-AC1 pin the contract at 0.4.1, read FAIL since the 0.4.2 bump and are superseded: leave them out), DB105-1..3-AC1 (`r105/p105_round105.py`), DB106-1..2-AC1 (`r106/p106_round106.py`), DB107-1-AC1 (`r107/p107_round107.py`), DB108-1..2-AC1 (`r108/p108_round108.py`), DB109-1..3-AC1 (`r109/p109_round109.py`). All 14 read PASS at your base; if any does not, file a BLOCKING row naming it and stop.
3. **Read Orion's performance table's shape** with the reader: the newest partition's column names, the period each window column covers, its unit (a fraction or percent points), and how many clients it holds. Counts and column names only. For each contract window (`qtd`, `ytd`, `last_12_months`, `since_inception`) decide: an Orion column whose period is evident from its name and which carries the same period as the contract's window rule (`document.windows`) is SOURCED; a window with no such column, or whose period is not evident, is ABSENT for Inflection with a reason in words. At least one window must be sourced; if none can be, file a BLOCKING row with the column list and stop.
4. **Edit the contract to 0.5.0** (one edit, nothing else): (a) `contract_version` 0.5.0 and a `lineage` entry carrying the 0.4.3 bytes' sha256 (`git show HEAD:<contract> | sha256sum`) and the reason; (b) a top-level `equivalences` list of classes `{id, meaning, entity, members}` (`entity` is `household` or `account`; a class's members share one unit): class `ENDING_VALUE_HOUSEHOLD` (entity household) holds `pvs.qtd.ending_value`, `pvs.ytd.ending_value`, `pvs.last_12_months.ending_value`, `pvs.since_inception.ending_value`, `hold.ending_value`, `act.ending_value.household`; class `ENDING_VALUE_ACCOUNT` (entity account) holds `avs.qtd.ending_value`, `avs.ytd.ending_value`, `avs.last_12_months.ending_value`, `avs.since_inception.ending_value`, `glr.ending_value`, `act.ending_value.account`; no member is in two classes; (c) a rule sentence in `change_rule` or `read_rule`: members of one class, for one entity, are all printed or all absent and agree where printed, and a figure printed under one member never reads unavailable under another; (d) for each of `pvs.qtd.return_cumulative`, `pvs.ytd.return_cumulative`, `pvs.last_12_months.return_cumulative`, `pvs.since_inception.return_cumulative`: keep `source` exactly `"ABSENT"` (every other firm stays absent) and add EITHER `firm_sources: {"inflection": {input, grain, table, field, fold, claim}}` OR `firm_absent: {"inflection": "<reason in words>"}` (exactly one per window, nothing for any other firm). A `firm_sources.inflection` object: `input` "orion_fact_performance"; `grain` "client"; `table` the silver prefix `s3://opal-data-assets/orion/inflection/silver/fact_performance` with the words "newest dated partition only"; `field` the Orion column name; `fold` how the sample reads it (the client row of the household's client id; the unit and the conversion to PERCENT POINTS, stated); `claim` the words "reported by the platform at client grain; not computed by Opal; includes dividends (round-108 read)"; (e) update the household-return entry of `open_changes` to say Inflection is sourced at 0.5.0 and every other firm stays ABSENT.
5. **Re-run the 14 earlier criteria** after the edit. Each must read PASS. A criterion that turns FAIL because of the contract change is a BLOCKING row naming it and the clause; never edit an issuer check file (outside your grant).
6. **Record** `CONTRACT_R110.json` in your folder: `contract_version`, `contract_sha256` (of the contract bytes you commit), `equivalence_classes` (the count), `household_windows_sourced` and `household_windows_absent` (lists of window keys), `orion_columns` (the column names of the newest partition, names only), `older_criteria` (an object: each of the 14 ids, value `"PASS"` after your edit), `reads` ({`s3_reads` integer, `s3_writes` 0, `vendor_calls` 0, `secret_reads` 0}).

<criterion id="DB110-1-AC1" cell_refs="DB-b-217"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_inflection.py" . DB110-1-AC1</invocation><expect>DB110-1-AC1 PASS</expect></criterion>
`DB110-1-AC1` -- the contract reads 0.5.0 or later; the `equivalences` list holds classes with exactly the keys id, meaning, entity, members, no member in two classes, one unit per class, the household class and the account class holding the six ending-value members each; each of the four household return members keeps source ABSENT and carries for Inflection exactly one of `firm_sources` (the six keys, grain client, the Orion fact_performance prefix) or `firm_absent` (a reason), at least one window sourced, no other firm named; the equivalence rule is quiet on a consistent synthetic set and reports a planted pair; `CONTRACT_R110.json` matches the contract bytes and lists all 14 earlier criteria PASS; the checker re-runs DB105-1-AC1 and DB109-1-AC1 itself and both pass. Base: FAIL (the contract reads 0.4.3).

<expected_criteria>DB110-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every issuer check file, every adapter and test, every sibling contract and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the two granted Inflection prefixes ONLY through the adapter's GET-only reader. Writes: the repo files of the grant. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Client data.** Column names and counts only: no client id, no account id, no figure from the silver in the repo, a row or your report.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If an earlier criterion's convention, not your edit, is what fails, file a BLOCKING row naming the clause and stop. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W175-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-217.contract-0-5-0-equivalence-map-and-inflection-household-return-source.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 112 (round 110), cell `DB-b-217`.
<owned_cells>DB-b-217</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB110-1-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/IRPT_DASHBD.TO-DB-b-217.contract-0-5-0-equivalence-map-and-inflection-household-return-source.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB110-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the 14 earlier criteria before and after (counts); the Orion performance table's column names, which windows you sourced and which you left absent and why (words); the equivalence classes as written; any BLOCKING row. Counts, hashes and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one contract file edit in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call beyond the adapter's granted GET and LIST reads.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB110-1-AC1 FAILS at base (the contract reads 0.4.3) and its control arm (a planted equivalence pair) is exercised by the checker's self-test.
lane: the <paths> block IS the grant.
</preflight>
