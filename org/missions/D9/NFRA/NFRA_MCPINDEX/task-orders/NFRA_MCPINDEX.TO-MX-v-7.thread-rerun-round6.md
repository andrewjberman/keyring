# NFRA_MCPINDEX task order -- `MX-v-7` -- the thread re-run after the slot-4 release: the BD figure against its source by VersionId, then the r7.J1 re-grade and r6.J1

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-v-7</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-v-7</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~22</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot read.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only: SSM on the gateway host, and an S3 GetObject by VersionId on the BD fees source.
comp-adversary: DECLARED-NOT-APPLICABLE -- J1 is the CVO's; this cell produces its material.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `MX-v-7` (round 6; `ROUND_ANALYSIS.round5.md` @1edec80f63 section 5 item 4)

**Start after MX-r-8 has SERVED and drained. The issuer continues you with this order.**

**The act (reads only):**
1. **On the host** (SSM `AWS-RunShellScript` on `i-07dccb1615503ac99`, under `/opt/opal-gateway/.venv/bin/python`,
   with `.env` parsed in Python, NEVER shell-sourced; row Z-S73):
   - call `blackdiamond_list_fees` in-process through the tool's own entry point, as MX-r-7's read-back did, for the
     latest available date;
   - take ONE figure from the answer (one fee amount on one row, named by its row key) and the answer's `as_of`;
   - record the answer's denominators (rows_matched, rows_returned, partitions read).
2. **From the source:** read the same row's field from the silver fees object for that date BY VersionId
   (`s3api get-object --version-id`, bucket `opal-data-bd`, prefix `silver/fees/`), and the object's own as-of field.
   Record the VersionId.
3. **On the host, in-process:** `opal_discover` for "what fees did Black Diamond charge", "Schwab positions" and "ETF
   positioning". Record the `next_tool` names. List the tools the host registers.
4. Write `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/THREAD_RERUN_round6.json` with
   these keys, each a plain value:
   - key `blackdiamond_list_fees`: `served_figure`, `source_figure`, `served_as_of`, `source_as_of`,
     `source_version_id`, `denominator`, `row_key`;
   - key `discover`: the three asks and their next tools;
   - key `tools`: the registered tool list.
   No account identifier, no ExternalId, and no secret goes in it. Name a row by a hashed key if the natural key is an
   account id.
5. J1 and J2 below are judgment criteria. The CVO grades them at L9; you record no verdict on them.

## 2. BOUNDS

1. Reads only. No write to any AWS resource, no deploy, no grant.
2. Never print a `.env` value; never shell-source the host `.env`.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W22-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,J1,J2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-v-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/v7.AC1.sh; echo "exit=$?"</invocation><expect>fields missing=[]; figure X == X; as_of D == D; VersionId printed; denominator printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-v-7" judgment="true"><!-- r7.J1 RE-GRADE at L9 by 3.0.0_SA_CVO~O (FWD-4, PRD:132-136): through a principal session whose tool list postdates MX-r-8's release, discover names blackdiamond_list_fees for the BD fees ask, and that tool's figure and as-of equal the source object read by VersionId (this cell's THREAD_RERUN_round6.json); denominator printed. --></criterion>
  <criterion id="J2" cell_refs="MX-v-7" judgment="true"><!-- r6.J1 at L9 by 3.0.0_SA_CVO~O (FWD-1/FWD-3; rulings B1/B2, A5): Alyssa's cold run, by an already-admitted non-author principal holding a Schwab grant, in a fresh session with only the MCP connected: one position question and one transaction question. The round's ONE essential wait: a person is the instrument, on Andrew's word. Scheduled only after MX-r-8 serves. --></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/NFRA_MCPINDEX.TO-MX-v-7.thread-rerun-round6.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>` (J1 and J2 under UNVERIFIABLE-BY-INSTRUMENT, `status_reason` naming
3.0.0_SA_CVO~O). Report once, in your final message.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-6 item 4. The issuer adds its own principal-session asks at the drain
(round 5's material: `deliverables/2.0.0_SA_COO~MI/round5/R7_J1_PRINCIPAL_SESSION_20261001.md`) and books Alyssa's run
through 0.0.0_AB_MSTR~Z for Andrew. Battery dry-run at base: v7.AC1 FAIL as expected (record absent).

<status>complete</status>
<round>6</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
