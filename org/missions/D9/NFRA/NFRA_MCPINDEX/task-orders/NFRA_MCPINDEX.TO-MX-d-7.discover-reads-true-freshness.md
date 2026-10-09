# NFRA_MCPINDEX task order -- `MX-d-7` -- discover states a dataset's TRUE as-of, read from the served artifact, and routes a model-performance ask to the benchmarks tool (the FWD-11 thread)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-d-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~28</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- discover's S3 access widens from HEAD to GetObject on the SAME objects it already HEADs, under the gateway role's existing json/* and platinum/* read grant; no role or policy file changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-d-4/d-6 discover pattern; the battery dry-run is the control (d7.AC2 reads 0 of 3 at base).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (GetObject of the served object discover already HEADs).
</preflight>

## 1. THE CELL -- `MX-d-7` (round 8; PRD v0.7 @b06af7c0d2 FWD-11, FWD-13, contract 4; decomposition section ROUND 8)

**The defect, measured at the base (2026-10-09 ~04:3xZ):**
- `opal_discover` states every dataset's `latest_value` from the catalog row's PROSE, with claim `held`.
  - Source: `_latest_value()` at `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py:166-174`,
    regex `live (\d{4}-\d{2}-\d{2})` over `vintage_semantics`.
  - That value was recorded at certification and is never re-read.
- For the model benchmarks it states 2026-08-10, while the served object carries 2026-10-07. The same holds for
  `platinum/mdpf/global/aum-metrics.json` and `platinum/mdpf/global/aggregate-aua-timeseries.json`.
  `d7.AC2` reads exactly this at the base: 0 of 3 equal.
- The structured field is already there. 37 of 37 artifact rows in `app/refs/DATA_CATALOG.yaml` carry `vintage_field`.
  The three named rows read:
  - `data_as_of`;
  - `_provenance.source_vintages['global/aum-metrics']`, a nested path;
  - `as_of_last`.
- `_answer_row()` (:364-390) already passes `vintage_field` out as `freshness.field`; it just never reads it.

**PRD v0.7 contract 4, verbatim:** "An entry's `latest_value` is read from the served artifact at answer time, with
claim `measured`. A held certification value is never shown as the as-of."

**The act (reader only; you write NO catalog file):**
1. **Read the as-of from the served object.** For a SERVABLE artifact row with a single-object key (after the existing
   family/scope substitution, the same key `_served_written_at` HEADs), discover reads that object once and resolves
   the row's `vintage_field` path into it. A path may be dotted, with `['...']` segments.
   - `latest_value` becomes `{value: <that date>, claim: "measured", source: ...}`.
   - The read is injectable, beside `head=` (for example `get=`), so tests need no network.
   - It uses the SAME client path as the HEAD: `internal_role.s3_client()` when set, else the default client with
     discover's own timeouts. Never add a second client policy.
2. **Never fall back to the held value.** When the read fails, the object is not a single key, or the path does not
   resolve, `latest_value` is `{value: None, claim: "absent", error_class: ...}`. The held prose date is never shown as
   the as-of.
   - You may keep the prose date in a separate, clearly named field (for example `held_at_certification`) so the
     drift stays visible. It must never sit in `latest_value`.
3. **Bound the read.** The served objects can be large (`aggregate-aua-timeseries.json` is a full series).
   - Measure the three objects' sizes and state them in your report.
   - Choose a bound (a byte cap, a timeout, or both), so discover never blocks an answer on a huge body. A body over
     the bound is `absent` with a named error_class, never a partial guess.
4. **The thread route (FWD-11).** Alyssa asks, in her own words, how a model did against its benchmark for a period.
   The ask "how did the Short Term model do against its benchmark year to date" must reach the model-benchmarks row
   FIRST, with `next_tool` = `mdpf_get_model_benchmarks`.
   - Measure where it lands at your base first, and fix through discover's ranking only.
   - The catalog is MX-c-6's this round, not yours. If it cannot be fixed without a catalog change, that is a BLOCKING
     row. Do not edit the catalog.
5. Add the three named tests to `tests/test_opal_discover.py` (see d7.AC1). Every existing test in that file still
   passes.

## 2. BOUNDS

1. You change `app/integrations/opal_discover/integration.py` and its test file only. You write NO catalog source:
   not `app/refs/DATA_CATALOG.yaml`, not `workflows/atom_decomposition/**`. Those belong to MX-c-6, running in
   parallel.
2. No change to `catalog_gate`, `query_v0`, any other tool, role, grant or route.
3. Nothing under `data/cot/`. No push. No deploy (MX-r-9 releases this). REFUSE a criterion you cannot meet as written,
   and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~28/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W28-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%Y-%m-%dT%H:%MZ`), never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-d-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/d7.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-d-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/d7.AC2.sh; echo "exit=$?"</invocation><expect>stated as-of equals served as-of (claim measured) for 3 of 3 datasets -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-d-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/d7.AC3.sh; echo "exit=$?"</invocation><expect>ROUTING: n of 27 with n >= 24 (floor 24 of 27) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~28/NFRA_MCPINDEX.TO-MX-d-7.discover-reads-true-freshness.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message, naming:
- the read bound you chose and the three objects' measured sizes;
- where the model-performance ask landed at your base, and why;
- any row you filed.
Do not edit this task order beyond your status flip. After this order, the issuer continues you with MX-d-8.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-8 chain head of [MX-d-7 -> MX-d-8 -> MX-r-9], worker ~28. It is the thread,
so it goes first. Battery dry-run at base ac135370d2 (`round8/checks/`):
- d7.AC1 FAIL as expected: named tests passed 0 of 3, failed/error 0.
- d7.AC2 FAIL as expected: 0 of 3. Each dataset states 2026-08-10 `held` against 2026-10-07 served.
- d7.AC3 PASS as expected: the regression control, ROUTING 24 of 27.

<status>issued</status>
<round>8</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
