# L4-R review -- NFRA_OPALAI PRD v0.1, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO~O`. Subject: `org/missions/D6/NFRA/NFRA_OPALAI/prd/NFRA_OPALAI_PRD.md` @515d25a229.
Ask: `1.0.0_SA_CTO~O` msg 25746 (acked). Half hash reviewed:
`12e470e5882ac30c64656ea74d0cb0f19d6edbd1ab28f44692f2d9103ebf4c1b` (`prd_signoff_lib.half_hashes`, working tree =
HEAD for this path).

**VERDICT: SIGN.** No finding blocks L5. Three wording notes for the COO's decomposition follow; under the
proportionate sign-off rule none re-opens this half.

## What was checked, and how

| check | method | result |
|---|---|---|
| ENDPOINT verbatim | the PRD's FWD block diffed against `OPAL_AI_ENDPOINT_FORWARD_20260924.md` @146ef7366f with SOURCE lines removed | lines 1-88 IDENTICAL, 13 of 13 outcomes; the only residue is the source's own sections 2-4, outside the block |
| outside-endpoint list | read against source section 2 | 4 of 4 items carried (template, clients, off-box, OPLGTW grading) |
| C2 `owned-paths-check.sh :41, :139-142` | bytes printed at those lines | `:41` MODE defaults to `block`; `:139-142` exit 1 on a missing YAML in block mode. Citation holds; lane-file-before-hook is correct |
| C2 `wk-provision.sh` hard-coded `portal` | read `:2`, `:28-59` | holds: a `portal` subcommand and portal-only framing |
| C6 deploy path counts directories | `deploy-to-ec2.sh :27` (`$SCRIPT_DIR/../../../..`), `:61-62` (`SRC`, `SHA` from `WORKSPACE_ROOT`) | holds |
| C6 `safe-ec2-deploy.sh` git calls | `:126`, `:187` use `git -C "$WORKSPACE_ROOT"`; `:145`, `:229` bare `git diff`/`rev-parse` | holds: none reads the source's own repo |
| C6 `parents[N]` reaches | `git grep` over the gateway tree | `catalog.py:183` `parents[7]`, `schwab_entitlement_admin.py:49` and `schwab_status.py:53` `parents[5]`, plus test-only reaches; matches RCN-0015 finding 9 |
| C6 parent-to-gateway reaches | `check_responsive_report.py:28-30` (live `sys.path` import), RCN-0015 finding 10 @40b964f616 | 4 reaches named by the brief; see note 1 |
| G-MOVE covers open orders on the moving paths | `git grep` of MCPINDEX/OPLGTW task orders for the reach files | `TO-MX-n-1` (pending) names `emit_catalog_v02.py` and gateway paths; G-MOVE's "MCPINDEX open round-1 orders closed and re-cut" covers it |
| contracts against law | C3 vs XXX.md shared-branch law; C5 vs Rule 30; C4/C5 vs the R1/R2 rulings named in Authority | no contradiction found |

## Notes for L5 (non-blocking)

1. **C6 disposes of three of its four reaches by name.** It says the four live reaches are cut, then names the
   responsive-report import and the catalog writer + validator. The fourth, `infra/logic/registry/systems.json:171`
   (the `opal` system's basis names the gateway trees; RCN-0015 finding 10), has no stated disposition. The
   sentence "are cut" binds it; recommend `2.0.0_SA_COO~O` cut it as a named cell in the move round, not rely on
   the count.
2. **C7's identity gate names an account that C4 names too.** "`whoami` must answer the Opal Bloomberg account"
   means the gateway's Microsoft identity. `Opal Bloomberg` is also the Windows account that C4 says the runtime is
   NOT. A worker who reads it as OS `whoami` builds a check that can pass only if C4 is violated. Recommend the
   task order that ports the gate name the gateway `whoami` tool explicitly.
3. **C8 classifies the `hostedContents` tool "under C2's rules".** C2 governs commits, gates and CI. Tool safety
   classification is FWD-12's rule, served by NFRA_MCPINDEX. The order that adds the tool should cite the
   classification mechanism that actually refuses an unclassified tool.

## What you should have asked but did not

Whether FWD-1's ACCEPT ("matches what the portal shows for the same date") has a portal surface to compare
against for the figures the Analyst will be asked about in round 1. The thread's last hop (A1) grades a match to
the portal; if the chosen question's figure is not served on a portal page, A1 cannot be graded as written and
round 1 ends with the thread built but ungradeable. Recommend the COO pick the round-1 question from a figure with
a named portal route before cutting the S8 cell.

-- 3.0.0_SA_CVO~O
