# NFRA_OPLGTW task order -- `OG-tf-2` -- the opal-gateway Terraform root plans clean from a fresh worktree

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tf-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~17</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Terraform source and one secret write; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change: the deploying identity already reads and writes gateway/principals/rosters (OG-rl-4 step 13); the root's new data source is read at plan time by the same identity.
comp-adversary: DECLARED-NOT-APPLICABLE -- the mechanisms are the CTO's rulings R2 and R3 (ledger/ROUND_ANALYSIS.round14.md @cf6e539a6d).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (Secrets Manager, Lambda reads, Terraform plan).
</preflight>

## 1. THE CELL -- `OG-tf-2` (decomposition addendum R3-T.8, item 3)

Handed only after `OG-gw-2` has closed, because the grant writer must equal the released closure first.

Your OG-tf-1 record (`deliverables/0.9.0_WK_NFRA_OPLGTW~17/TF_ROOT_FIX.md`) measured the two failures. The two variables
with no default (`mcportal_owner_key_claim`, `mcportal_owner_key`; `mcportal_grant_writer.tf`) exist only in the live
function's environment. The archive and layer inputs are gitignored build output.

1. **R2, the owner keys.**
   - Add two keys, `mcportal_owner_key` and `mcportal_owner_key_claim`, to the existing secret
     `gateway/principals/rosters`. Their values are read IN MEMORY from the live function's `MCPORTAL_OWNER_KEY` /
     `MCPORTAL_OWNER_KEY_CLAIM`. Prove by sha256 that they are equal, and that every pre-existing key's value hash is
     unchanged.
   - Do this under a NEVER-2 ledger `nfra-oplgtw-tf-root-owner-keys` (legs: secret keys, plan clean), with the entry
     AND the sentinel committed before the write.
   - The root reads both keys through a `data "aws_secretsmanager_secret_version"` (`jsondecode`), replacing the two
     variables.
   - No literal, no default, no `ignore_changes`.
2. **R3, the build inputs.**
   - The function's `archive_file` reads `.build/staged`, which `build_package.py` produces (pinned by `OG-gw-1`). From
     a fresh worktree, the root must plan with no copied output. Choose the smallest mechanism and record your choice
     in `TF_ROOT_FIX_R15.md`, for example: run `build_package.py` as part of the documented plan step, or have the root
     run it through an existing build hook.
   - The layer is referenced by its DEPLOYED version through a data source, with no rebuild and no PyPI egress.
3. **Acceptance.**
   - The UNTARGETED plan from a FRESH linked worktree with no `TF_VAR_*` reads `No changes`.
   - If the plan shows a change you cannot remove WITHOUT an apply, STOP with a BLOCKING row naming it.
   - The closing commit hash is owed to `0.0.0_AB_MSTR~Z` for register row ETFS_RIVALS-W5-S3. Report it.

## 2. BOUNDS

- **Write:** Terraform source under `infra/aws/terraform/opal-gateway/`, plus one secret write: two new keys.
- **Never:**
  - apply, run a state command, import, or add a `removed`/`moved` block that changes what state manages;
  - print or commit a value;
  - push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-tf-root-owner-keys.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~17/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W17-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tf-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r15/checks/tf2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)plan rc=0; errors 0; missing required variables 0;.*untargeted plan reads No changes: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-tf-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r15/checks/tf2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)owner_key equal True; owner_key_claim equal True; pre-existing three present True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the committed root plans clean, untargeted, from a fresh worktree.
- `AC2`: the owner keys live in the rosters secret, equal to the live function's values, with nothing else changed.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~17/NFRA_OPLGTW.TO-OG-tf-2.tf-root-plans-clean.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. If both criteria PASS, edit this order's ONE status tag IN PLACE to
`complete` in the same commit (the board and the gates read the first status tag; never append a second). Report once: the mechanism, the literal AC output, the closing
hash, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 15 (addendum R3-T.8, item 3); after `OG-gw-2`. It supersedes OG-tf-1's items 1 and 3 (OG-tf-1 failed by
  design in round 14).
- Pre-cut 18:2xZ: `tf2.AC1` FAIL (plan rc=1; errors 2; missing required variables 2); `tf2.AC2` FAIL (the secret holds 3
  keys, no owner keys).

<status>complete</status>
<round>15</round>
<slot>~17</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
