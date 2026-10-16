# NFRA_MCPINDEX task order -- `MX-c-25` -- the gold book catalog entry drops its stale `open_items` line

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-25</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-25</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~48</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- a catalog source entry text; no role, policy or grant change, no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- one removed line, graded by a git diff against the base (c25.AC1).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-25` (round 19, enrichment E2; CVO row Z-C-S63)

Work in your own worktree (cut from `box/sitez`). Every path is relative to its root. **First**, run once: `git sparse-checkout add workflows infra/aws/ec2/opal-gateway/app/refs` (the only sparse change you may make; the validator reads the catalog under app/refs).

**Why.** The file `workflows/atom_decomposition/catalog_entries/opal_data_etfs_gold_book.yaml` ends its `open_items` list (lines 69 to 73) with this item, wrapped over two lines:

```
- 'gateway role: GetObject on gold/book simulates implicitDeny (read-grant widening
  needed)'
```

It is stale. The OG-ap-20 grant names `gold/book/*` (and `gold/holding/*`) in the same statements (`infra/aws/terraform/opal-gateway/etfs_read_iam.tf`, the MX-c-22 ruling), `etfs_get_positioning` reads gold/book, and a live gateway answer read gold/book at 2026-10-16 10:36Z. The catalog row says a read-grant widening is needed when it is not.

**What to do.** Delete exactly that one `open_items` item (both source lines of it) from the entry file. Add nothing, change nothing else: not the first `open_items` item (the Bloomberg L1 landing line), not any other field, not any other entry file. The file stays valid YAML and valid for `workflows/atom_decomposition/validate_catalog_v02.py`.

### Steps

0. The sparse command above.
1. Make the one deletion. Run the two criteria in section 4.

## 2. BOUNDS

1. You change only the file in `<paths>`. No other entry, no emitter, no `DATA_CATALOG.yaml`. No deploy. No push.
2. The checks are `deliverables/2.0.0_SA_COO~MI/round19/checks/c25.AC1.sh` and `c25.AC2.sh` (python `c25_check.py`). Read them for exactly what is graded. Do not edit them.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
4. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/catalog_entries/opal_data_etfs_gold_book.yaml
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~48/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W48-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 1)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-25" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/checks/c25.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR catalog entry files differing from 0afc0f3a19: 1; open_items at base 2 (stale 1); now 1; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-25" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/checks/c25.AC2.sh; echo "exit=$?"</invocation><expect>validator rc 0; gold book OK lines 1; FAIL lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~48/NFRA_MCPINDEX.TO-MX-c-25.gold-book-entry-drops-its-stale-open-item.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The expect fields are prose; the checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, replacing digits with `[0-9]+`, and disclose that in a row. Pin each artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file was committed before the instance.)
2. Do NOT flip the order's status; the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in two commits: (i) the entry file; (ii) the proof instance.
4. Report once, with: the removed lines verbatim; the AC1 DENOMINATOR lines and CHECK lines verbatim; the two commit shas.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 19, worker ~48, an independent chain, DIRECT-ACT (one line, LOCAL). Source: CVO row Z-C-S63 and ADJUDICATION_v13 @c5ba2988f4 (the gold book row's stale `open_items`), endorsed by the CTO (msg 35012). Base dry-runs: `c25.AC1` FAIL (the stale item stands), `c25.AC2` PASS (the entry validates at base, a bound control).

**A1 (2.0.0_SA_COO~MI, ~14:2xZ):** the sparse command above gains `infra/aws/ec2/opal-gateway/app/refs`: `validate_catalog_v02.py` reads `app/refs/DATA_CATALOG.yaml` and raised FileNotFoundError in the sparse cone (worker ~48, row Z-W48-S1). The issuer added the folder to the worktrees of ~48 and ~49. Gate limb that graded this amendment: none (a modification; no criterion changed).

<status>issued</status>
<round>19</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

**ISSUER RULING (2.0.0_SA_COO~MI, 2026-10-16 ~15:0xZ); MX-c-25 COMPLETE.** Worker ~48 removed the one stale `open_items` item (two source lines) from the gold book entry: `0761bf4c0e`. Its first run read AC2 FAIL because the validator reads `app/refs/DATA_CATALOG.yaml` outside the sparse cone (row Z-W48-S1, the order's defect, ruled in amendment A1 and re-run PASS at `58d8f95972`). Drained by `safe-merge.sh` at `7309ccc274` (4 files, none foreign). Issuer re-run on the merged tree: c25.AC1 PASS (1 entry file differs from `0afc0f3a19`, open_items 2 to 1, no line added) and c25.AC2 PASS (validator rc 0, gold book OK, 0 FAIL); proof-of-spec VALID (checked inside the worker tree, whose checker scope matches the instance). Gate limb that graded this ruling: the flip-needs-a-VALID-instance limb of to-pipeline-gate.

<status>complete</status>
