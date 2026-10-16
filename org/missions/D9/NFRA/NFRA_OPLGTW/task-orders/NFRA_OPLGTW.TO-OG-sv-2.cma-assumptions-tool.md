# NFRA_OPLGTW task order -- `OG-sv-2` -- one more typed read in the json-served family: the capital-markets assumptions (CTO ruling @131991960e)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sv-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sv-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~113</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests plus one read-only probe; no deploy, no schedule. The release is the later applier order OG-ap-23.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The object is `opal-data-portal-v2/json/capital-markets/assumptions.json`, under `json/*`, which the gateway role already reads (`infra/aws/terraform/opal-gateway/queryv0-iam.tf` line 34).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling @131991960e (file `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_MCPINDEX_R18_RESEARCH_32_OUT_OF_LINE_20261016_Z.md`) that this row owes a tool.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-sv-2` (decomposition addendum R3-T.77, workstream JSON-SERVED-2, FWD-22)

Add ONE tool to the module `app/portal_json_served.py` that your own first order (OG-sv-1) built and the issuer has merged to your branch base: `portal_get_cma_assumptions`, for the catalog row `opal_data_portal_v2_served_cma_assumptions` (bucket `opal-data-portal-v2`, catalog `prefix` `json/capital-markets/assumptions.json`, grain: one row per asset class, 27 rows, an ANNUAL edition: its freshness is the edition year, current when it is the 2026 edition; there is no trading-day lag to state, say `edition` instead). Follow EXACTLY the pattern of the five tools already in that module (read them first): catalog row read at call time (no bucket, prefix or key literal typed), `admit_scope` before any S3 call, Opal principals only, the envelope (`as_of` from the object's own date or edition field, `source_keys`, `denominator`, `absent_reason`, plus `edition`), 50 KB projection, `served_prefixes()` extended to include this row's prefix. The 27 rows are returned whole when they fit the cap.

1. **Measure.** Read the object from the real bucket (box credentials, no content printed) and write `W/SV2_ROW.json` = `{"row": {"entity": "opal_data_portal_v2_served_cma_assumptions", "class": "BUILT", "tool": "portal_get_cma_assumptions", "edition": "<the edition year read from the object>", "rows": <the row count>}}`. If the object is NOT the 2026 edition, write class `RULED_OUT` with the measured edition in a `reason` field, build nothing, and file a BLOCKING surprise row.
2. **Build** the tool and extend `served_prefixes()`.
3. **Probe** (`W/probe_sv2.py`, you write and run it; the issuer re-runs it as AC2): call the tool as an Opal stand-in principal against the real bucket (`INTERNAL_READER_ROLE_ARN` unset), assert the envelope is complete and the body non-empty; call it again as a non-Opal principal and assert the refusal with zero reads; print ONE line: `probe sv2: portal_get_cma_assumptions answered True as_of <YYYY> non_opal_refused True reads_on_refusal 0`. Print no object content.

### Tests, named, in `tests/test_og_sv2.py` (a recording fake S3, a synthetic catalog fixture of the same shape; an Opal stand-in principal)

- `test_ogsv2_ac01`: the tool reads ONLY its synthetic row's `bucket` + `prefix` and returns the envelope with `edition`.
- `test_ogsv2_ac02`: a missing row, a retired row and two rows of the entity each answer `absent_reason` with ZERO reads.
- `test_ogsv2_ac03`: a non-Opal and an absent principal are refused with ZERO reads; an object over the cap answers `harvest_over_cap`.
- `test_ogsv2_ac04`: the tool name does not end in `_group` or `_role`; `served_prefixes()` returns the OG-sv-1 BUILT prefixes plus this one, all computed from the rows.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no catalog edit.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer registers the tool and re-pins at the merge. Name the registration you expect.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name, an email, an account number or an amount, or any object's content (counts and booleans only); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/portal_json_served.py
infra/aws/ec2/opal-gateway/tests/test_og_sv2.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/SV2_ROW.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/probe_sv2.py
infra/aws/ec2/opal-gateway/tests/test_og_sv1.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/`. You WRITE only the first four and the investigation file (append rows); the rest you read. Rows: id `NFRA_OPLGTW-Z-W113-S<k>` (continue after your last), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sv-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/sv2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sv-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/sv2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)row: entity ok True; class BUILT; tool defined 1 of 1; edition read from the object True.*cma tool probed 1 of 1.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sv-2.cma-assumptions-tool.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, AC lines, the edition and row count, the registration you expect).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream JSON-SERVED-2 (decomposition addendum R3-T.77). Origin: MCPINDEX msg 34695 and the CTO ruling @131991960e moving `served_cma_assumptions` into the (a) set; ledger of the answer: my msg to ~MI2 (cma_assumptions IN).
- Same slot ~113 as OG-sv-1: it continues the same worker on a branch the issuer has synced to trunk after the sv-1 merge (the module must be on the base).
- Pre-cut: sv2.AC1 and sv2.AC2 base FAIL as expected.

<status>pending</status>
<round>37</round>
<workstream>JSON-SERVED-2</workstream>
<slot>~113</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
