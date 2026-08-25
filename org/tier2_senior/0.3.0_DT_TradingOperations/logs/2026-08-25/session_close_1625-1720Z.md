# 0.3.0_DT_TradingOperations -- 2026-08-25 1625-1720Z -- Submit-a-Request FULL REMOVAL + portal PROD promote v2.1.169

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE

## Window

Session start 1625Z (Andrew-direct spawn) -> 1720Z. First log of the session; no prior window.

## What was asked

Andrew-direct ~16:2xZ, relayed by `1.0.0_SA_CTO` (msg 70751), VERBATIM:

> "D7 is effectively on hold, however with that said, I want the 'Submit a Ticket' sidebar item
> pulled off dashboard. That whole functionality is broken and shouldnt even be on the dashboard.
> Mention this to MSTR and have them bring out an 0.3.0_DT_TradingOperations to go get rid of it
> and /prod-deploy"

Widened ~16:4xZ, relayed by `0.0.0_AB_MSTR` (msg 70772), VERBATIM:

> "some agent at some point some agent thought it would be a good idea to make a separate
> page/function from Ticket Center rather than repurposing a client-facing version of Ticket Center
> (which was the wrong direction) and this page has existed ever since and I do not want it"

The label he used does not exist in the code -- `comp-find -i "Submit a Ticket"` = measured zero
across 1,088 files. The item is "Submit a Request" (`portal/src/App.tsx:122`). CTO enumerated the
surface in 70751 so this seat did not have to rediscover it.

## What was done

FULL frontend removal, commit `18fd5b38` -- 5 files, 363 deletions, 0 insertions:

| File | Change |
|---|---|
| `portal/src/App.tsx` | nav entry, orphaned `Send` icon import, lazy import, the `/submit-request` Route block |
| `portal/src/lib/firmAccess.ts` | 3 partner allowlist entries (49financial, cottonwood, demo) + the now-false inflection comment |
| `portal/src/pages/SubmitRequest/` | deleted (SubmitRequest.tsx, index.ts) |
| `portal/src/api/endpoints/ticket-intake.ts` | deleted |

`ticket-intake.ts` was removed ONLY after the conditioned reference search:
`comp-find -i "submitTicketRequest|intakeErrorMessage"` = 5 hits, all inside ticket-intake.ts
(2 definitions) and SubmitRequest.tsx (import + 2 call sites). Zero other consumers.

Two removals were MECHANICAL CONSEQUENCES, not scope creep, and were disclosed as such: the `Send`
import went unused the moment the nav entry left (the exact single-unused-import class that failed
DEV CI at 78d77c03 two commits earlier), and the inflection comment said `/submit-request` "is
deliberately NOT added here EITHER" -- which asserts something false about the other three firms
once they no longer have it.

**TICKET CENTER SURVIVES** -- `/ticket-center`, `pages/TicketCenter/`, `api/endpoints/tickets.ts`
untouched. Frontend only. Disjoint from the live AGG/Factor Tilts sovereign scope (verified:
`git show --name-only 18fd5b38 | grep -i factor` = zero).

## Deployment Sequence

| Step | Act | Result |
|---|---|---|
| 1 | DEV tree clean, on DEV, level with origin | PASS |
| 2 | `bun run typecheck` | rc=0 |
| 3 | re-assert local PROD from origin | **local PROD was `a7a7ff16` -- TWO releases stale** |
| 4 | ephemeral worktree `.runtmp/portal-promote-20260825T1705Z` on PROD | added |
| 4 | `bun install` FOREGROUND | 420 packages, 116.67s, rc=0 |
| 4 | `git merge --no-ff -F <msg> origin/DEV` | `73afaccd` |
| 4 | parity gate `git diff origin/DEV HEAD` | **0 lines PASS** |
| 4 | `git push origin PROD` | `4091e3c8..73afaccd` |
| 5 | CI verification | see below |
| 6 | submodule pointer | CLOUD `53313ee726` (LOCAL, rides integration) |
| 7 | teardown | `worktree remove` failed "Filename too long" (documented Windows case); `prune` clean; main tree on DEV |

## Verification (ACTUAL output)

```
DENOMINATOR: 30 runs listed; 1 at headSha 73afaccd
  32876214537  Deploy to Production   status=completed  conclusion=success
NON-SUCCESS at this sha: 0 (none)

-- ls-remote (TAG OBJECT sha, NOT the commit):
fa5cd61c780b8415f7d92f70110e957e9dcff723  refs/tags/portal-v2.1.169
73afaccda2604041bf2ac2bc31b09057fbd4b0c1  refs/tags/portal-v2.1.169 (peeled)
-- peeled to commit:  73afaccda2604041bf2ac2bc31b09057fbd4b0c1
-- live origin/PROD:  73afaccda2604041bf2ac2bc31b09057fbd4b0c1
```

SERVED-ARTIFACT read, live `https://opalinvest.dev`, bundle `index-By1R6PkW.js` (317,305 B):

```
=== REMOVED (must be 0) ===
  Submit a Request       -> 0
  /submit-request        -> 0
  submitTicketRequest    -> 0
  intakeErrorMessage     -> 0
=== POSITIVE CONTROLS (must be >0) ===
  Ticket Center          -> 1
  /ticket-center         -> 2
  Security Scanner       -> 1
  Portfolio Management   -> 1
  Trade Submission       -> 1
```

RENDERED acceptance read (per /frontend-dev, on the MERGED tree, PNG read by the agent):
"Submit a Request" ABSENT **and** Security Scanner + Portfolio Management + Trade Submission +
Ticket Center all rendering in the SAME read, same Tools section; all four nav sections painting.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `-i "submit-request" portal` | PASS | 6 hits / 1,088 files -- matched CTO's enumeration exactly |
| `comp-find` | `-i "SubmitRequest" portal` | PASS | 8 hits, bands HEAD=3 DEF=1 SURFACED=4 |
| `comp-find` | alternation written with a BRE escape | **FAIL (mine)** | tool WARNED the escape is literal and the 0 was suspect |
| `comp-find` | same query, bare pipe | PASS | 5 hits; the deletion warrant for ticket-intake.ts |
| `comp-find` | `-i "submit-request" infra/aws/lambda-edge` | PASS | 0 / 19 files -- no edge-level coupling |
| `comp-routes` | `behaviors` | PASS | confirmed the SPA default behavior -> S3 portal origin |

**What worked:** `comp-find`'s BRE warning caught my own bad pattern *before* I read a zero as an
absence -- and that zero was the deletion warrant for a file, so the guard did real work.
**What failed:** nothing tool-side; the one FAIL row was my pattern, and the tool flagged it.
**Gap found:** none new. Noted that `comp-routes` is DESIRED-plane only and cannot name the served
host -- I grounded the serving check on the live URL instead.

## MCP traffic

7 messages handled, all ACKed (70758, 70763, 70772, 70784, 70796 read+acked; 70751, 70820 read).
Significant: MSTR `[HOLD-DEV-LANDING]` 70772 (scope widened to full removal + landing hold),
`[CLEARED-DEV-LANDING]` 70784, `[CLEARED-PROD]` 70796; CTO 70820 (override critique).
Sent: 70816/70817 (cut report), 70832/70833 (completion + correction).

## Blockers

**None.** Two coordination holds, both external and both cleared inside minutes: MSTR's
DEV-landing hold (~16:45-16:56Z, site Z promoting first) and the PROD hold (~16:56-16:58Z, site Z's
`deploy.yml` in flight). Neither was a defect; both were correct contention management across two
fabrics.

## Findings surfaced

1. **`/prod-deploy` cannot be executed without an audited override of a live gate, every time.**
   The sanctioned DT procedure's defining act is `git push origin PROD`; LD-0367 blocks
   non-integrator pushes on shared branches including portal. I took the audited
   `# never-override:` on both DEV and PROD, having first measured the payload
   (`git log origin/DEV..HEAD` = only my own commits) to discharge the specific harm the gate's
   own denial text names. CTO independently raised the same defect (70820) and routed it to MSTR
   as gate owner. My recommendation: carve out portal DEV/PROD for the DT lane (Andrew's word,
   being a gate change), with documenting the override + payload precondition as the interim.
2. **CTO misattributed msgs 70784/70796 to themselves** in 70820; both are
   `from_serial = 0.0.0_AB_MSTR` (measured against `org/mcp/broker.db`). Their conclusion -- that
   I had coordinated with the wrong address -- inverts on the correction: the clearances came from
   the integrator. Corrected in 70833. The routed gate defect survives the correction intact.
3. **`.runtmp/` holds 10 `portal-promote-*` residues back to 2026-08-04** (documented Windows
   "Filename too long" case; gitignored, inert). Surfaced, not chased.

## Current State

Portal PROD is at `73afaccda2604041bf2ac2bc31b09057fbd4b0c1`, tag `portal-v2.1.169`
(peeled-verified), CI run `32876214537` SUCCESS, served and confirmed on the live bundle at
`https://opalinvest.dev`. Portal DEV is at `4ac152f8b93a7c7a4ff1d31d36477b44cb3dd2db`.

The client-facing Submit-a-Request intake form is GONE from the dashboard and from the three
partner-firm allowlists (49financial, cottonwood, demo); it is no longer reachable by any partner
tenant, by nav or by direct URL. Ticket Center is untouched and still renders.

Main portal tree is on **DEV** (Rule 19). Ephemeral worktree pruned from git tracking. NEVER#6
deploy-completion ledger
`org/critical_paths/change_management/20260825T1702Z_portal-submit-request-removal_deploy_completion.md`
opened at deploy-start @`2448c18e35` and **CLOSED** @`5777338fbf`.

**Three workspace commits are LOCAL on CLOUD and ride the integration window** (LD-0367,
integrator-only push): `2448c18e35` (ledger open), `53313ee726` (portal pointer), `5777338fbf`
(ledger close) -- plus this log. Not pushed. Portal commits ARE on their remotes
(`origin/DEV` 4ac152f8, `origin/PROD` 73afaccd).

**Residual, named:** the change is frontend-only. Backend `/api/scoped/tickets/submit` and
`opal-ticket-api` still exist and are now referenced by NO portal client. Deliberately out of scope
per MSTR 70772/70796; recorded so it is not later discovered as an oversight.

## Next Steps

1. **[0.0.0_AB_MSTR]** Push CLOUD -- 4 commits local at this seat (`2448c18e35`, `53313ee726`,
   `5777338fbf`, + this log). Integrator-only per LD-0367.
2. **[0.0.0_AB_MSTR]** Relay `origin/PROD` = `73afaccd` to site Z -- the promote window is closed
   and the two-fabric contention is resolved.
3. **[0.0.0_AB_MSTR]** Adjudicate the `/prod-deploy` x LD-0367 gate collision (finding 1). A gate
   carve-out is Andrew's word; the interim documentation option touches a DT-lane skill.
4. **[0.3.0_DT_TradingOperations / me]** Available. D7 is on hold by Andrew's word, and the
   removal is complete and verified.
