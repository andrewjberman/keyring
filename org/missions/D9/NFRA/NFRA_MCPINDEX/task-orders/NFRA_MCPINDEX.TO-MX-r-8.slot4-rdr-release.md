# NFRA_MCPINDEX task order -- `MX-r-8` -- the slot-4 gateway release: discover reads silver_datasets + Schwab rows (MX-d-6) and G-RDR (MX-g-3), live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-8</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-r-8</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~22</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no Terraform in this release; the internal reader role and the gateway's assume permission are live (NFRA_MCPMSP).
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-6 / MX-r-7 release pattern; G-A delta + never-widen halves (CTO + COO) before PHASE B.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM).
</preflight>

## 1. THE CELL -- `MX-r-8` (round 6; `ROUND_ANALYSIS.round5.md` @1edec80f63 section 4 and section 5 item 3; release-train ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` @cf5989190d)

**Start ONLY when all three hold; the issuer continues you with this order when they do:**
- MX-d-6 and MX-g-3 are complete and drained;
- this release is slot 4 of the opal-gateway train: MX-r-7 (landed `05e3eff563`), then NFRA_MCPMSP MS-d-2, then
  NFRA_OPLGTW OG-rl-1, then this;
- OG-rl-1 has landed, or the issuer names MS-d-2's ref as the base.

**The pattern is MX-r-7's.** Read its order whole and follow PHASE A and PHASE B:
`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-7.bd-release.md` (A1-A5). Its ANNOUNCE is the
template: `git show b92561fbec:org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/ANNOUNCE_MX-r-7.md`.
These are the differences:
1. **Base, by REF:** the LIVE ref at PHASE A, read from S3 `ec2/opal-gateway/opal-gateway-latest.tar.gz` metadata
   `git-ref` and the CLOUD `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.deployed_commit`.
   - Re-read it immediately before the ANNOUNCE and at PHASE B.
   - PHASE B runs `deploy-to-ec2.sh` with `DEPLOY_BASE_REF` set.
   - If the ref moved, STOP and report: the pins are void.
2. **Content:** the gateway-path commits of MX-d-6 and MX-g-3 only (identify them by content on CLOUD), applied onto
   the live ref.
   - Exclude by content every foreign payload, including MDPF_TAXSMA TX-g-1 and NFRA_OPALAI OA-e-10 (train C5).
   - Never merge another seat's release-branch manifest commit.
3. **No Terraform.** No `ENABLED_INTEGRATIONS` change.
4. **`.env` (train C1/C2):** hand-merge onto the LIVE printf line, never a CLOUD-sourced one.
   - This release adds NO key. `INTERNAL_READER_ROLE_ARN` arrives with MS-d-2; confirm it is in the live key set, and
     if it is absent, say so in the ANNOUNCE.
   - The ANNOUNCE prints the KEY set before and after (keys only, never values). Nothing is lost.
   - Both principal keys stay. `OG_MASTER_ADMIN_PRINCIPALS` / `OG_WRITE_CAPABLE_PRINCIPALS` are supplied off-repo by
     the issuer at PHASE B, unless OG-rl-1 moved them to a host-side read. Read the live script to know which.
5. **ac08 pin (train C3):** LIVE + OWN tool count. This release adds 0 tools, so the pin equals the live count.
6. **NEVER-2 ledger** `nfra-mcpindex-r6-rdr-release`. Name BOTH paths when committing: the entry under
   `org/critical_paths/change_management/` AND the sentinel `org/critical_paths/.open_deploys/nfra-mcpindex-r6-rdr-release.json`.
7. **Read-back:**
   - r8.AC2 (below);
   - `.env` keys before == after;
   - host == artifact;
   - `git-ref` on both S3 objects;
   - `e1z.AC1.sh` on the deployed tree reads `unrouted=0`.
   Roll back from the rollback tree on any failed leg. Never half-landed.

**Host safety (row Z-S73):** NEVER shell-source `/opt/opal-gateway/.env` (`set -a; . ./.env`). Its values are unquoted,
and bash echoes them in its errors. Parse it in Python, the way `deliverables/2.0.0_SA_COO~MI/round6/checks/r8_host.py`
does. The host interpreter is `/opt/opal-gateway/.venv/bin/python` (there is no `venv/`).

**Halt gate in a worktree (row Z-W21-S21):** if `safe-ec2-deploy.sh` resolves the issuer's serial, write your OWN serial
into your worktree's gitignored `org/mcp/sessions/<session>.serial`, as MX-r-7's deployer did. MX-x-4 is fixing this.

## 2. BOUNDS

1. No identity, grant, sign-in, role or policy change. No Terraform.
2. Never half-landed. Every void condition of both signed halves binds.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/**
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r6-rdr-release.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W22-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-8" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/r8.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-8" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/r8.AC2.sh; echo "exit=$?"</invocation><expect>status=Success; /health=200; BD ask next_tools includes blackdiamond_list_fees; ETF ask next_tools includes etfs_get_positioning -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/NFRA_MCPINDEX.TO-MX-r-8.slot4-rdr-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report the pins and stop. The issuer takes them to the never-widen halves and continues
you for PHASE B. After PHASE B, write the proof instance at the `<instance_path>` and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-6 item 3. BD ExternalId option A (Z-W21-S12) is NOT folded: it would add a
code path and a secret-read grant to a release whose job is routing. It stays an enrichment candidate. Battery dry-run at
base:
- r8.AC1 FAIL as expected (no entry; 22 of 22 sentinels);
- r8.AC2 FAIL as expected (live host: BD ask next_tools=[]; ETF control routed etfs_get_positioning; /health 200).

<status>complete</status>
<round>6</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
