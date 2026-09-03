# 2.0.0_SA_COO~Z -- session log 2026-09-03 18:50Z -> 21:45Z -- Andrew asked whether I had issued ALL the task orders or was doing them piecemeal; the answer was piecemeal and the numbers were worse than I would have guessed. Every cell now carries a face. A worker then stopped a 20-method production outage at the design read, and the certifier ran the BACKWARD arm of a rule I had only stated forward

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE

**Lane:** site-Z fabric, `2.0.0_SA_COO~Z`. Session 4ac75ff7; previous log `cooZ_session_1815-1850Z_four_bar_defects_ruled_and_a_control_that_failed.md` @4a2a6afcb8. Zero crons; `/watcher` Monitor `bs2clu5tl` streaming; `/drive` OFF.

## Window summary

**Andrew asked two questions and both were indictments.** "No one is working, are we done here or what" -- both lanes were parked and it was my fault. "Have you actually issued ALL task orders or are you doing them piecemeal?" -- piecemeal, and **9 faces covered 13 of 29 cells while 17 had never had one and SIX of those had no blocker at all.** Both are now fixed: **29 of 29 cells carry a task order, 22 faces on disk.** In the same window a worker's mandated pre-write read stopped an outage that would have made 20 API methods permanently unreachable, and the certifier found the same class already shipped in a face I had accepted.

## Commits by this seat (author `2.0.0_SA_COO~Z`), all LOCAL

| hash | what |
|---|---|
| ca5c6e7c82 / 4dd2664b7d | round-3 cut, 5 faces: the two web ACLs + IP sets, the login alarm, the throttle coverage, the key rotation, the gateway keys |
| f2f9168bae / 7ee7bef5a5 | the 8 staged faces with blockers named, completing coverage of all 29 cells |
| bc0d0ed2bd / 2f805081e9 | TO-OP-S-1: `S1-AC5` root exception, then `S1-AC3`'s denominator 39 -> 19 |
| 541fdfcc74 / 91e8572faf / 27558a62b9 / a8c4f2cf28 / b156402ca9 | disarm records Z-S68, Z-S53/56/57, the correction of my own Z-S70, Z-S75, Z-S80 |
| 2b28a42654 / cb4d734b0f | decomp v0.1.12 and v0.1.13: OP-s-4, OP-s-18, OP-s-29 to COMPLETE |

**Push state: LOCAL, MEASURED** -- `origin/SITEZ` reads `001709c96e`.

## THE ISSUANCE FAILURE, MEASURED

| | before | after |
|---|---|---|
| Cells with a task order | 13 of 29 | **29 of 29** |
| Cells with NO task order | 17 | 0 |
| ...of those, with NO blocker | 6 | -- |
| FWD outcomes fully served | 2 of 18 | **4 of 18** |

**Both lanes were PARKED, not stalled** -- CPU measured at ~0.2 s per 20 s, watcher-poll idle, zero unread. **One lane's finished work sat UNCOMMITTED in a checkout measured to lose it.** The other I had parked on a 20:00Z clock for a log object, on a comparable I had not checked for transferability: I matched a brand-new near-idle bucket against one receiving continuous traffic. **I proposed spawning three more lanes and Andrew stopped it -- the bottleneck was issuance, not capacity, and he was right.**

**Two standing rules adopted so it cannot recur:** a worker takes its next limb without waiting for my acknowledgement, and **a timed UNCOMPUTABLE whose underlying capability is separately PROVEN never blocks a completion flip.**

## THE OUTAGE STOPPED AT THE DESIGN READ

`0.7.0_AE_CloudOps~Z` halted limb 2 before writing anything. **`FWD-1` as specified would have made 20 of 39 methods permanently unreachable, four of them live POST writes.** The authorizer is keyed on `X-Opal-Origin-Verify`, which **CloudFront injects as a custom origin header** -- a method with no CloudFront route can never carry it.

**Measured on two planes by two seats.** The assignee, live: the disputed path through CloudFront returns the SPA shell as `text/html` while the raw address returns **1,417,396 bytes of JSON**, with a connectivity positive control. This seat, on the parsed behavior map: **of 28 declared behaviors exactly ONE targets that API origin, and nothing covers `/api/public/` at any depth.** The 19/20 split reconciles exactly with the corrected 21+18 method count.

> **The tool named the trap in its own words: a catch-all `/*` match is a DEFAULT, not a resolution, and must never be read as evidence the path is served.** The 200 through CloudFront was that default.

**RULED (A):** attach to the 19 reachable, print both denominators, file the 20 as a NAMED RESIDUAL **expressly barred from being written as "FWD-1 served"**. `S1-AC3` amended 39 -> 19 before any attachment.

**The endpoint half went to L4 and is the more important one:** nine paths including four writes are served only at the raw address on an API with **zero authorizers and no resource policy**. **The project's chosen mechanism cannot close the most exposed part of its own outcome.**

## THE BACKWARD ARM -- the certifier ran the half I did not

I promoted the edge-coverage rule **forward only**. `3.0.0_SA_CVO~Z` asked which COMPLETED faces it would have failed, and found one: **`TO-OP-S-2` gated `GET /metadata/yang` at 16:24:34Z and that route has no CloudFront behavior at any depth** -- the exact condition limb 2 halted to avoid, shipped five hours earlier under a face I accepted. Confirmed here: both metadata routes read `CUSTOM` on `naqxlm`, and `comp-routes trace` matches only the catch-all.

**`S2-AC1` stays PASS and is not reopened.** Its reading is exact: **ATTACHED and REACHABLE are two different properties and my criterion only ever measured the first.**

⛔ **THE PROPOSED DISARM CANNOT BE RUN: that API has `AccessLogSettings.DestinationArn: null` and `DetailedMetricsEnabled: false`.** No access-log plane, no per-route metrics, and the API-wide 4xx series is confounded by our own probes. **The caller question is unanswerable with the instruments that exist.**

**RULED: DETACH NOTHING.** Both routes are closed, which is this project's own direction; reverting to public on an unmeasured suspicion would undo the outcome to protect a caller nobody can find. **AND I REFUSED THE FIX I WOULD OTHERWISE HAVE ORDERED** -- enabling access logging is excluded by PRD :263 ("any monitor, alarm, log destination... NOT named in an outcome"), so it is a card, not a cut.

## Errors of mine this window

1. **Piecemeal issuance**, above -- the largest.
2. **Parked a lane on a clock** built from a comparable measured on a different population.
3. **Amplified a worker's finding without measuring it.** I called the build-manifest finding "the second that would have taken production down" and told the seat to bank it, **without opening `build-nodejs-lambda.sh`.** It retracted two hours later: the build **bundles**, and the `files` array is an OUTPUT written after the build. **A vivid finding from a seat with a good record is the one I stop auditing** -- earned credibility terminating inquiry by status. Banked.
4. **My own disarm record carried a false control** ("`opal-gateway` plans CLEAN"); its pre-apply plan churned and the apply converged it. Corrected at 27558a62b9.
5. **My ACL-2 hypothesis was refuted** -- I predicted no churn because it adds no managed group; its plan churned on two groups the face never touched. The experiment was still right to run.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| comp-routes | `behaviors`, `trace` | PASS | the behavior map is what independently confirmed the 19/20 split; its own doc named the catch-all trap |
| aws CLI (read-only) | wafv2 get-web-acl / list-ip-sets, apigatewayv2 get-routes / get-stages, cloudwatch get-metric-statistics, secretsmanager, elbv2, cloudfront | PASS | `get-stages` returning null log settings is what killed the proposed disarm |
| proof-of-spec-check.py | 2 instances with expected id lists | PASS | VALID rc=0 each, coverage checked |
| comp-read / comp-schedule | face and cell reads, the preflight gates | PASS | 21 gates over 5 carriers, cited in all 11 new faces |
| channel-commit-guard.py | 5 invocations | PASS | **refused twice, correctly**, on peer rows |
| safe-commit + gates | 14 commits | PASS | to-pipeline-gate rejected two faces for a preflight token and was right |

**What worked:** measuring before amplifying, on the ACL finding and the metadata routes. **What failed:** not doing it on the build-manifest finding. **Gap found:** the API has no access logging, so a whole class of question about it is unanswerable; excluded from this project by the PRD and surfaced as a card.

## Blockers

None at this seat. Both lanes hold queues; nothing waits on me.

## Current State (the handoff)

- **Complete and accepted this window:** `TO-OP-S-4-18` (the two ACLs and the IP sets -- the largest unlock, five cells came off the blocked list) and `TO-OP-S-29` (the log destination's source conditions).
- **Cells:** 29 total, **11 COMPLETE**, 2 in flight, the rest open or held. **FWD outcomes: 4 of 18 fully served.**
- **`0.7.0_AE_CloudOps~Z`:** `TO-OP-S-1` limbs 1, 2a and 3 complete; limb 2 executing shape (A) on 19 methods; then `TO-OP-S-7`, `TO-OP-S-10`, `TO-OP-S-12`.
- **`0.7.0_AE_CloudOps~S`:** `TO-OP-S-20` next and ahead of the queue -- it gates the sentinel's BLOCK arm; then `TO-OP-S-6`, `TO-OP-S-13`, `TO-OP-S-15-19`, `TO-OP-S-22`, `TO-OP-S-14-21`, `TO-OP-S-23`.
- **Records:** PRD v0.12; decomp **v0.1.13**; 82 channel rows, **every ARMED row this seat owns carries its disarm record**.
- **At Andrew:** the fixture call (the only sanctioned portal credential is MFA-enabled, so no unattended probe can complete a login; rec is a bounded permission to mint for the fixture identity), plus OP-x-3 and OP-x-4.
- **At L4:** FWD-1's shape (the mechanism cannot reach the unrouted paths); whether `/metadata/yang` should be public; and one route closed by an accident of routing rather than by decision.

## Next Steps

1. [`0.7.0_AE_CloudOps~Z`] limb 2 on 19 of 39 with both denominators printed; then its three queued faces.
2. [`0.7.0_AE_CloudOps~S`] `TO-OP-S-20`, then the queue in order.
3. [`2.0.0_SA_COO~Z`] validate each face as it lands; issue `TO-OP-S-14-21` only after `TO-OP-S-20` is terminal (C-4).
4. [`1.0.0_SA_CTO~Z`] the three L4 questions above.
5. Session close log at the project's L10 close; this log is the handoff until then.
