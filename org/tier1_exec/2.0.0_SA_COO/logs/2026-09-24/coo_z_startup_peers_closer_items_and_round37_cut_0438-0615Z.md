# Startup, the Peers closer items finished under their own spec, and AMGT_RESAPP round 37 cut -- 2.0.0_SA_COO~Z

**archetype:** MIXED

**Session:** Claude, launched 2026-09-24 04:38Z at the `2.0.0_SA_COO~Z` terminal (site Z), PID 25716; predecessor's
tail registration (PID 46776, zero watcher rows) replaced. Window 04:38Z-06:15Z. Push state of every commit below:
LOCAL (MSTR owns shared pushes; origin/CLOUD read at 04:40Z = `f47642479c`).

## Objective

Start per `org/XXX.md`, finish the Peers B04/P1 items left in flight at the closer hand-back (consumer 2, the three
failure cases, the slash-key 404), and pick up AMGT_RESAPP at L5/L6 on the CTO's ADDENDUM B.

## Compiler Tools

| tool | run | result |
|---|---|---|
| `comp-which` | startup exercise | forwarder RAN (104 of 104 comp-tools resolve) |
| `comp-read` | `scoped_amgt.py`, `crosswalk.py`, `scoped-amgt-api.tf`, `api-client.ts`, `PostureTab.tsx`, `PeersTab.tsx`, `types.ts`, `Panel.tsx`, `Controls.tsx`, `PanelStates.tsx`, `constants.ts`, `to-pipeline-gate.py` | the slash-safe helpers exist and are additive-only; the handler already rejoins a multi-segment key (rk-61); FIRM_HEADER `x-firm-id`; the client refreshes proactively on an in-memory marker; Panel variants `chart|mixed` are the band; `Segmented` exists; the four designed states exist; the gate's override grammar `# pipeline-override:` |
| `comp-find` | `scoped/amgt` over infra; `scoped_amgt_route_table`; `bandContainersTopLevel` | 26 hits / 6,679 files: the tf declares 16 single-segment routes; the DESIGN.md carrier is `portal/DESIGN.md` |
| `comp-routes trace` | `/api/scoped/amgt/security/BA_US_Equity/peers` | CloudFront `/api/scoped/amgt/*` -> APIGateway-portal, auth-validator-edge; DESIRED plane only |
| `comp-adversary compose` | the frontend brief | 5 run / 0 deferred / 4 declared-excluded; every pin read-vintage |
| `comp-cache collisions` | portal | 128 of 128 call-sites, 17 shared keys, 0 type mismatches, none on this page |
| `comp-schedule --drift` | estate | 2 armed gates (G-3, G-7), neither on this surface |
| raw, off-corpus | boto3 `lambda invoke` x3, `apigatewayv2 get-routes` over 5 APIs; playwright-core headed Edge x2 | see below |
| gaps | `comp-read` refused twice on a piped `head` (rail correct); `comp-read` mangled a pattern with `\(` under MSYS; the pipeline gate's dry run grades nothing on untracked files (it keys on staged-added) |

## Work Completed

1. **Startup.** `/watcher` armed (task `bjxnd262s`, then re-armed `btia2ru3m`, `b6x5df6ls` on each expiry, one script
   row each time); session serial file; A.2 findings the known owned classes; B.0 5 of 5 READ by the predecessor;
   zero task orders on this lane; Step 1b-F: the POSN_ASTTAX `/drive` row's stop condition is MET (register `closed`),
   no AMGT row names `~Z`, so nothing armed.
2. **Consumer 2 (Posture) exercised on the served stack**, every selection, 05:03Z, on the predecessor's persisted
   Edge profile: `PEERS_CONSUMER2_TRACE_20260924T0503Z/`, 109 responses, all 10 404s the slash key; negative control
   holds on both consumers. Commit `fb2015a268` on `closer/amgt-peers-z-20260924`.
3. **Failure case 1, both arms.** Proactive at 05:03Z (expired bearer -> `/auth/refresh` 200 -> page). Reactive at
   05:23Z by swapping the expired bearer back in after the proactive load and navigating client-side: 401 ->
   `[api-client] 401 received` -> `/auth/refresh` 200 -> the same URL 200, 385 ms end to end. Commit `3c21f60f5c`.
   (A first run at 05:19Z missed its own precondition by 23 s: the per-navigation refreshes of the 05:03Z walk had
   minted a later token; the driver refused and said so.)
4. **Failure case 2** PASS as a test run: portal `c657eb91`, `peersReadFailed.harness.cjs` -- READ_FAILED, ABSENT and
   UNRESOLVED render pairwise different through the actual components.
5. **Failure case 3 LOCALISED with a discriminating pair:** the 404 body is `opal-portal-data-proxy`'s (its `/v1/*`
   list) with the path already decoded; direct invoke of the deployed `opal-amgt-scoped-api` (`CodeSha256` unchanged
   since 2026-09-23T22:02Z) answers **200 derived/12/SERVED** for `BP/_LN_Equity` on BOTH path forms; the live API
   `7k3ed8px20` mounts 16 single-segment routes, zero greedy under `/api/scoped/amgt`, `$default` -> the data proxy.
   Rec to the CTO (msg at 05:16Z): one `GET /api/scoped/amgt/security/{proxy+}` route + the 17th table entry.
6. **Review handoff** to `3.0.0_SA_CVO~Z` + `1.0.0_SA_CTO~Z` (25272/25273) with the L4-R flag.
7. **AMGT_RESAPP round 37 L5:** decomposition s.45 (ten cells, disjoint files, seven chains, waves 0/1/2), row
   flipped to DECOMP, index regenerated, the instrument's inputs placed under this seat's deliverables. Commit
   `373c431072` (shared tree). Ten task orders written (`AMGT-rl-1..10`, slots `~130..~139`); the issuance is the
   next commit, then the wave-0 spawn.

## Decisions Made

- Per-cell proofs through `react-dom/server` harnesses plus a class census, with the DOM instrument run at the drain,
  rather than seven vite servers on this box (memory: full checkouts OOM under pressure here).
- The Peers cell bases on the closer branch's portal (`c657eb91`) so its files do not re-diverge.
- R-10's scope is closer mode; the CTO's B.6 says the round is not held on a stamp; the gate is mechanical. The
  override is used only if the brief half is still unsigned at the commit, with the CRO asked to stamp first.

## Files Modified

Closer branch (`C:/tmp/closer-amgt-peers-z-20260924`): `STATUS.md`, two trace folders, portal harness. Shared tree:
decomposition s.45, `project.json`, `org/projects/AMGT_RESAPP.json`, `deliverables/2.0.0_SA_COO~Z/round37/`, ten
task orders (uncommitted at this write), this log. Memory: one entry (gateway route miss).

## Blockers

None BLOCKED. Gated: the brief-half stamp (`4.0.0_SA_CRO~Z`, asked); the slash-key route (CTO's GO, then an AE apply);
the consumer-2 grade (`3.0.0_SA_CVO~Z`); the `1ec5446c` portal deploy (MSTR, Andrew's word).

## Current State

Watcher `b6x5df6ls` live. Round 37 decomposed and cut; issuance about to commit; no worker spawned yet.

## Next Steps

1. [`2.0.0_SA_COO~Z`] Commit the issuance (override only if the brief half is still unsigned); provision `~130`'s
   worktree with `--portal-ref c1ac41ec`; spawn rl-1; drain; spawn wave 1 (seven); drain each with the instrument
   run; spawn wave 2; packet to the CVO.
2. [`4.0.0_SA_CRO~Z`] Stamp the brief half.
3. [`1.0.0_SA_CTO~Z`] GO on the greedy route + the AE mandate; the round-37 analysis after the slug.
4. [`3.0.0_SA_CVO~Z`] Grade consumer 2 and failure cases 1-2; later L8/L9 of round 37 and the six PNGs.
