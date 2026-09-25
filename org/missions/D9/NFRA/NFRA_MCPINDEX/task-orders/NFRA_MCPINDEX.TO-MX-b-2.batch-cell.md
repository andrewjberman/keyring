# NFRA_MCPINDEX task order -- `MX-b-2` -- ROUND 2, E6: the batch cell (the emitter's docstring; the validator's report untracked)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-b-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two small edits; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface.
comp-adversary: DECLARED-NOT-APPLICABLE -- a batch cell.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-b-2` (round 2, decomposition section R2.1)

Two small repairs the round-1 adjudication carried to this round:
1. **The emitter's docstring (row C-S15).** `workflows/atom_decomposition/emit_catalog_v02.py` is the one writer of the
   live catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`. Its opening docstring lines (`:2-3`) still name
   the staged file `catalog_v02/DATA_CATALOG.v0.2.staged.yaml` as its output; only `:5` corrects that. Make the opening
   lines (1-4) name `refs/DATA_CATALOG.yaml` as what it writes, and drop the staged file from them. Change no code.
2. **The validator's report (row W1-S3; the issuer's pick).** `workflows/atom_decomposition/validate_catalog_v02.py`
   rewrites `workflows/atom_decomposition/catalog_v02/validation_report.json` on every run, and that file is tracked, so
   every run dirties the tree. Make it a run artifact: add it to the repository's `.gitignore` (the nearest existing one
   that already governs `workflows/`; say which), and remove it from the index with `git rm --cached` (the file on disk
   stays). Then run the validator once, and show `git status` stays clean for it.

## 2. BOUNDS

1. No other file changes. The emitter's behaviour and the catalog are untouched.
2. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/catalog_v02/validation_report.json
.gitignore
workflows/.gitignore
workflows/atom_decomposition/.gitignore
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_MCPINDEX-Z-W5-S<k>`, fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-b-2"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/bx.AC1.sh; echo "exit=$?"</invocation><expect>emitter lines 1-4: names refs/DATA_CATALOG.yaml>=1; mentions the staged file=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-b-2"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/bx.AC2.sh; echo "exit=$?"</invocation><expect>tracked at HEAD=no; ignored=yes; status lines for the report after a run=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/NFRA_MCPINDEX.TO-MX-b-2.batch-cell.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once:
- which `.gitignore` you used;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E6 (C-S15, W1-S3). Chain C, independent; cut from CLOUD.

<status>complete</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
