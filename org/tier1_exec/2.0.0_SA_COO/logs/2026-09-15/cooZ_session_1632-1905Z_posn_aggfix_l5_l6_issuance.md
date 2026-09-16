# POSN_AGGFIX from respawn to a running round: one decomposition, one issuance, three workers -- 2.0.0_SA_COO~Z

**Date:** 2026-09-15
**Task Order:** POSN_AGGFIX round 1 (L5 decomposition, L6 issuance, L7 spawns)
**Status:** IN PROGRESS (L7 executing on three worker subagents)

---

## Objective

Seat `2.0.0_SA_COO~Z` after the account weekly limit (HTTP 429, resets Sep 19 17:00 ET) killed the prior session, then carry the new D4
project POSN_AGGFIX (Andrew-direct ~16:2xZ) through L5 and L6 the moment its PRD cleared L4-R, and start L7.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | PATH check: 104 of 104 comp-tools resolve bare and a forwarder ran |
| comp-find | `comp-find "positioning/positioning_data" --band DEF --limit 60` | PASS | 17 DEF hits across 61,858 files; 2 in code (the producer writer, the satellites reader) |
| comp-find | `comp-find "positioning_data\.json" --files` piped to tail | FAIL (rail) | refused as a piped census; re-run with the tool's own `--limit` |
| comp-schedule | `comp-schedule --drift` | PASS | 7 armed gates, 0 POSN; 6 open deploy-ledger entries, 0 POSN; 12 NEVER clauses |
| comp-iam | `comp-iam service auth-validator-edge` | PARTIAL | no record for the edge function; the service listing came back (declared blind in the orders) |
| comp-adversary | `comp-adversary compose <decomposition>` | PASS | 5 sources run, 4 declared-excluded; seven issuer gaps written into s.7 |
| missions-tree-index | `derive --write` then `check` | PASS | 18 of 18 valid, 0 violations after each stage flip |
| prd-signoff | `prd-signoff.py status POSN_AGGFIX` | PARTIAL | verdicts correct; the "OWED BY 4.0.0_SA_CRO~W" label is the known alphabetical quirk (delivery went to ~Z) |
| to-pipeline-gate | via safe-commit on the issuance | PASS | refused once, correctly: a preflight line read "DECLARED-BLIND", which is not in its grammar |
| surprise-row-gate | via safe-commit on the issuance | PASS | refused once, correctly: an empty channel file "mints on an item" |
| terraform | whole-root plans, `-lock=false` | PARTIAL | portal-auth 0 add / 1 change (WAF drift) / 0 destroy; yang-pipeline refused `Backend initialization required` in the shared tree |

**What worked:** the DEF band census answered the writer count in one call; the tree-index derive and check made both stage flips cheap to verify; both gate refusals named the exact defect.
**What failed:** a piped `comp-find` census and a `.tf` grep were refused by the rail; `comp-iam` has no record for Lambda@Edge functions.
**Gap found:** no tool resolves "which CloudFront behaviours and rewrites reach this S3 key" end to end; TO-C1-1's C1-AC1 builds that read by hand.

---

## Work Completed

### 1. Startup and the inbox
`/watcher` registered the lane (was NOT REGISTERED) and armed the inbox Monitor; session serial file written; delivery ledger READ 6 of 7 then 7 of 7. Read and acked: 23153 (POSN_ASTTAX CLOSED @e223c78ed5 by 1.0.0_SA_CTO~W, nothing owed), 23158 (respawn + POSN_AGGFIX), 23164 (Andrew: the ~W seats answer only AMGT_RESAPP), 23170, 23180, 23197 (the L5 release), 23200. My loop row (`/drive` NFRA_OPSEC202609) re-measured CLOSED: nothing armed.

### 2. The AUM contract conflict (before L5)
Measured on the served file: the five books' `aum` equal the July legacy rows 5 of 5 and the current rows 0 of 5, so PRD v0.1's byte-identity and its source re-point could not both hold. 4.0.0_SA_CRO~Z refused the brief half on the same defect (@7ffc16301a); I filed no duplicate row. v0.2 @cbd85e5cff answered it; both halves SIGNED at 18:02Z.

### 3. /open-calls for Andrew
One CARRIED call: remove the 13 POSN_ASTTAX round 2-4 worker worktrees (0 commits missing from SITEZ, 0 tracked changes, untracked `.scratch/` only); the 2026-09-14 ruling skips worktrees with untracked files, so it does not cover them. The three 2026-09-04 calls belong to the CLOSED NFRA_OPSEC202609.

### 4. L5 -- the decomposition @605c03f81f
`org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md`: 17 cells `AF1-s-1..AF1-s-17`, one per manifest row (subtraction 0 both ways; 8 of 8 outcomes carried); cell ids resolved 17 of 17 with the gate's own regex; ASCII 0. dep_stage PRD -> DECOMP.

### 5. L6 -- the issuance @ed1db8f1db
7 task orders, 17 of 17 cells owned (the gate's coverage limb agrees), 13 files, 0 outside the project, 0 left staged. The COO halves of both never-widen co-signs, `ledger/PORTAL_REFS.md`, and the channel opened with row `POSN_AGGFIX-Z-S1`. dep_stage DECOMP -> EXECUTING. Two refused attempts first, each fixed at the named line.

### 6. L7 -- worktrees and spawns
Worktrees from `ed1db8f1db` as sparse cones, each TREE-OK: `/c/tmp/wk-aggfix-1-1` (~1), `/c/tmp/wk-aggfix-1-2` (~2), `/c/tmp/wk-aggfix-1-3` (~3) with the portal worktree `/c/tmp/wk-aggfix-1-3/portal` on `wk-aggfix-1-3-portal` @edf85ce503 and a PowerShell junction to the main install (vite, playwright-core, typescript present). Spawned `0.9.0_WK_POSN_AGGFIX~1` on TO-A1-1, `~2` on TO-C1-1, `~3` on TO-B1-1. CTO halves requested from 1.0.0_SA_CTO~Z at 18:54Z.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| The Opal-only key is `json/positioning/opal_aggregate.json`, served at `/api/general/positioning/opal_aggregate.json` | `public-data-router` already rewrites `/api/general/*` and `/api/general/json/*` to `json/`; no new route or bucket grant is needed |
| `current_holdings.AGG.total_aum` = the members' sum; the five primary rows' sum and the file's `total.model_aum` ride in `reconciliation` | 4.0.0_SA_CRO~Z's msg 23200 note; it is the weights' own denominator and nothing on the page shows a total |
| The edge refusal lives in `auth-validator-edge` right after the JWT verify, admitting `firmId === 'opal-capital' || userType === 'Dev'` | the only viewer-request function with the claims; it mirrors the page's `isInternal() || isDev()` (AuthContext.tsx :736-737, :750-751), not the edge's `tier === 'internal'` bypass |
| Portal work is cut from `edf85ce503` (origin/PROD) | the tree Andrew checked live; origin/DEV adds one CI commit and no Positioning file |
| A partial weight read serves `status UNAVAILABLE` | never an aggregate that reads as current; carried as a judgment criterion (A2-AC12) for L9 |
| The channel opens on a real row, Z-S1 | the row gate refuses an empty channel; the PRD's fallback sentence describes only one of two measured arms |
| Spawn prompts point at the committed order file | the file at the worker's HEAD is the face verbatim; a retyped face could fork it |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md` | new, round 1 | Yes -- `605c03f81f` |
| `org/missions/D4/POSN/POSN_AGGFIX/project.json`, `org/projects/POSN_AGGFIX.json` | PRD -> DECOMP -> EXECUTING | Yes -- `605c03f81f`, `ed1db8f1db` |
| `org/missions/D4/POSN/POSN_AGGFIX/task-orders/` (7 orders) | new | Yes -- `ed1db8f1db` |
| `ledger/NEVER_WIDEN_ROUND1_PRODUCER_COO_HALF.md`, `ledger/NEVER_WIDEN_ROUND1_EDGE_GATE_COO_HALF.md` | new, SIGNED | Yes -- `ed1db8f1db` |
| `ledger/PORTAL_REFS.md`, `surprise-channel/investigations/INVESTIGATION_v1.md` | new; row Z-S1 | Yes -- `ed1db8f1db` |

---

## Blockers

None at this seat. The two deploy legs (TO-A3-1 A3-AC1, TO-C1-1 C1-AC6) refuse until `1.0.0_SA_CTO~Z` writes `ledger/NEVER_WIDEN_ROUND1_PRODUCER_CTO_HALF.md` and `ledger/NEVER_WIDEN_ROUND1_EDGE_GATE_CTO_HALF.md` (requested 18:54Z); that is a designed gate, not a stall.

---

## Current State

POSN_AGGFIX round 1 is EXECUTING from the issuance `ed1db8f1db` (decomposition `605c03f81f`, PRD v0.2 `cbd85e5cff`): worker ~1 is on TO-A1-1 in `/c/tmp/wk-aggfix-1-1`, worker ~2 on TO-C1-1 in `/c/tmp/wk-aggfix-1-2`, worker ~3 on TO-B1-1 in `/c/tmp/wk-aggfix-1-3` with its portal worktree at `edf85ce503`. Every commit is LOCAL under the site-Z push hold. The queues: ~1 then TO-A2-1 and TO-A3-1; ~3 then TO-B2-1, and TO-B3-1 only after TO-A3-1 and TO-C1-1 drain. If this session dies, check each worktree for edits and commits BEFORE respawning, and re-read each order at SITEZ.

---

## Next Steps

1. **Drain each worker's order on its final report** -- read the report AND the proof instance, `safe-merge.sh` the branch with the channel unioned by row id, read every row, remove nothing a later order needs, then continue the same worker on its next order.
2. **[1.0.0_SA_CTO~Z] Write the two CTO halves** -- the deploy legs wait on them.
3. **Drain slot ~3's portal branch onto `refs/drains/aggfix-1-portal`** at each of its drains; the gitlink never moves.
4. **Hand TO-B3-1 after TO-A3-1 and TO-C1-1 both drain**, then send the one drain-end message to 1.0.0_SA_CTO~Z (the CVO's watermark against the row count, and any armed row with an unseated owner).
5. **[Andrew] The carried call** -- the 13 POSN_ASTTAX round 2-4 worktrees.
