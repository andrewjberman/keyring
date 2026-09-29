# NFRA_MCPINDEX task order -- `MX-x-3` -- validate_catalog_v02.py gets an offline mode with zero AWS calls, and the live run's non-OK row is identified (row Z-W13-S2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-x-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~18</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a tool change.
comp-iam: DECLARED-NOT-APPLICABLE -- the live run is read-only on opal-data-portal-v2 with existing credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- a tool mode added (offline) and one read-only live run; the live run changes nothing.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (the live validation's S3 HEAD and list reads).
</preflight>

## 1. THE CELL -- `MX-x-3` (round 4; `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round3.md` @f354170b42)

**Why.** `workflows/atom_decomposition/validate_catalog_v02.py` makes live S3 reads by design (stage C). A cell
under a "No AWS" bound therefore cannot run it (row Z-W13-S2). Its live run reported 1 of 36 rows as
`family_mismatch_or_error`, and nobody identified which. Its report writer also crashes when `catalog_v02/` does not
exist.

**The act:**
1. Add `--offline`: run ONLY the local schema pass (`validate_silver_entries`) and exit with its verdict. Make ZERO
   `aws()` calls and write no report. Print that it is offline.
2. The report writer creates `catalog_v02/` if absent. The report is not committed, and remains gitignored if it is
   already ignored.
3. Run the LIVE validation once (read-only). Write `MISMATCH_ROW_MX-x-3.md` in your deliverables:
   - the live run's `SUMMARY:` line, verbatim;
   - one line per non-OK row: `ROW: <entity> | STATE: <state> | CAUSE: <cause, measured>`.
4. Run AC1 and AC2, and commit.

## 2. BOUNDS

1. No S3 write. The report file is not committed.
2. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/validate_catalog_v02.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~18/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W18-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-x-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/x3.AC1.sh; echo "exit=$?"</invocation><expect>offline rc=0 aws calls=0; schema pass printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-x-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/x3.AC2.sh; echo "exit=$?"</invocation><expect>ROW lines>=1; SUMMARY line present=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~18/NFRA_MCPINDEX.TO-MX-x-3.validator-offline.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-3 analysis s.5 item 7. The carried round-2 tooling items are closed: Z-S22 and Z-W7-S2 (MX-x-1), Z-W3-S4 (MX-x-2) and Z-W3-S12 (the issuer's battery). Z-W5-S1 and Z-S24 are routed to their owners, as ruled in round 2.

<status>pending</status>
<round>4</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
