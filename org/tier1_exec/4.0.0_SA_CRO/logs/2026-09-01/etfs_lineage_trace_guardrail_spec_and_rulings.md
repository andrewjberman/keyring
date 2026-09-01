# 4.0.0_SA_CRO — ETFS lineage trace, coverage-guardrail build spec, and six Andrew rulings

**archetype:** MIXED
**secondary_archetypes:** TRACE, SCRIBE, COORDINATE

**Window:** 2026-09-01 ~17:50Z -> ~18:55Z (since `f01de310ee`, my prior log this session).
**Serial:** `4.0.0_SA_CRO`. Monitor `bt72luq1c` still live. Zero crons.

---

## 1. What was asked

Andrew-direct, in sequence:
1. *"can you tell me the lineage of where this information is being surfaced from? trace the data all the way
   back from the main lambda, i want you to /draw the system as it stands now ... in the interest of
   revisiting the automated monthly process. I'd like to be able to have it go out to aj@opalinvest.com via
   email but I'm hesitant in the event that there are holes ... maybe we can build in some kind of guardrail
   that checks for holes pre-publishing and if there it it has a remediation process that checks the source
   files, if they are not there it does targeted egress."*
2. *"yes do all of the above."*
3. *"I agree with the reporting obligation window."* + *"Any other /open-calls on this matter?"*
4. *"All recs approved. ALso I want to be on the email as well as aj@opalinvest.com should be him and me at
   andrew@opalinvest.com."*

## 2. The lineage, traced on the LIVE plane (not from source)

```
Schwab      -> opal-data-assets/schwab/08242234/silver/fact_rps/date=D/   -> bd-49f-etf-ownership-daily
                                                                             cron(45 10)  NO CATCHUP
Black Diamond -> opal-data-assets/blackdiamond/cottonwood/silver/          -> cot-etf-ownership-daily
                 fact_holdings/date=D/                                        cron(30 10)  NO CATCHUP
Orion       -> opal-data-inf/gold/canonical/holdings_D.parquet            -> inf-etf-ownership-daily
                                                                             cron(0 15)   HAS CATCHUP
   all three -> opal-data-etfs/daily/{partner}/{date}.json
      -> etf-ownership-dashboard  cron(0 16)  -> platinum/etf_ownership_dashboard.json
      -> etfs-reports-monthly-run (EventBridge SCHEDULER) cron(0 10 1 * ? *) America/New_York = 14:00Z
           -> etfs-reports-orchestrator -> SSM start EC2 i-070477bf35fc54409 -> render_month_end.py
           -> platinum/reports/{YYYY-MM}/  -> SES -> andrew@opalinvest.com
      -> etfs-canon-fanin  cron(45 15) ENABLED -> DynamoDB opal-etfs-ownership-daily  ** ABSENT **
```

Diagram delivered to Andrew in-session via `/draw` (two-plane house style). Not committed — it is a
presentation of facts recorded in §3 and in the spec, not a separate durable artifact.

## 3. Findings from the trace

| # | Finding | Evidence |
|---|---|---|
| 1 | **`etfs-canon-fanin` fires daily at a table that does not exist** | rule ENABLED `cron(45 15)`; `describe-table` -> `ResourceNotFoundException`. Residue of the design the 2026-08-24 gate overruled. |
| 2 | **The catch-up Andrew wants already exists in ONE producer** | `inf` has `_catchup_missing_dates:274-293`; `cot` and `bd-49f` = 0 hits (`comp-read --enumerate`, denominators printed). This is exactly why inflection was 43/43 and cottonwood was not. |
| 3 | **A naive port of that catch-up FAILS for 49F** | `CATCHUP_WINDOW_DAYS = 10` hardcoded. MEASURED upstream lag Jul-Aug: cottonwood max **6 d**; 49financial mostly 1-5 d **with a tail at 12 and 13 d**. The date falls out of the look-back before its upstream arrives. |
| 4 | **Inflection's lineage does NOT reconcile** | repo source computes `opal-data-assets/orion/.../fact_positions`; every slice 07-16 -> 09-01 cites `opal-data-inf/gold/canonical/holdings_`; both paths populated; deploy (08-11) POSTDATES last source change (08-03 @`001a73530a`). Needs a deployed-bytes diff (Rule 22a), NOT a source read. **UNRESOLVED — stated as such.** |

## 4. Deliverable — the build spec

`docs/briefs/ETFS_COVERAGE_GUARDRAIL_BUILD_SPEC_20260901.md` @`5c7f0f3646`, amended @`e5d3f848b3`,
@`1890d7785c`. **Dispatches nothing.** Its spine is a 4-class taxonomy: a day with no slice means market
closed / source UNPRICED / producer never fired / upstream absent — **and three of the four are correct.**
A gate that counts slices cannot separate UNPRICED (filling it fabricates data) from a real hole.

Moratorium carve-out cited in the header: CLAUDE.md bans building freshness-checkers *"unless Andrew
explicitly asks"* — he asked, verbatim; the carve-out is scoped to a precondition inside the existing render
path plus catch-up inside existing producers, and §7 forbids any new monitor/alarm/topic.

## 5. Six Andrew rulings — recorded verbatim + broadcast same turn

| Call | Rec | Ruling |
|---|---|---|
| window | reporting-obligation | **APPROVED**; day-count window recorded as REJECTED |
| 1 date basis before automating | YES | **APPROVED** -> new §6a, prerequisite to the SEND |
| 2 restate? | forward-only | **APPROVED** — no restatement, no partner notification |
| 3 `aj@` replace or join | REPLACE | ⛔ **OVERRIDDEN -> JOIN** (`aj@` AND `andrew@`) |
| 4 egress pre-auth | keep per-use | **APPROVED** — rung 3 builds to STOP AND ASK |
| 5 activate ETFS_CANON | leave scoping | **APPROVED** |

⛔ **Card 3 is an OVERRIDE, not an approval, and it arrived in the SAME SENTENCE as "All recs approved."**
The specific instruction governs the general one. A seat decomposing off the blanket phrase alone would
implement REPLACE and silently drop Andrew from the distribution of his own report — and that failure is
invisible, because "Andrew stopped receiving it" reads identically to "the render did not run."

**Broadcast, per-recipient (never a silent aggregate):** `1.0.0_SA_CTO` DELIVERED 92423 · `0.0.0_AB_MSTR`
DELIVERED 92424 · `2.0.0_SA_COO` **QUEUED 92422 (no live session — written and waiting, NOT delivered)**.
COO is the seat that decomposes this; that one is sitting, not landed.

## 6. Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-read --enumerate` | `cot-...lambda_function.py` / `bd-49f-...` on `catchup\|missing\|backfill` | PASS | the measured **0 hits over a printed denominator** is the whole finding-2 claim; a `grep -c` would have handed the same zero with no denominator |
| `comp-read` | `inf-etf-ownership-daily/lambda_function.py`, `orchestrator.tf` | PASS | surfaced the assets-vs-inf source contradiction (finding 4) |
| `comp-read --enumerate` | `orchestrator.tf` on `cron\|rate\|schedule_expression` | PASS | found the monthly trigger `cron(0 10 1 * ? *)` America/New_York |
| raw `aws` (operational) | lambda list/get-config, events, scheduler, dynamodb, s3api | PASS | the live plane; one `events list-rules` sweep hit the 120s Bash timeout after yielding 5 of the rules |

**What worked:** `--enumerate` on the two producers is what let finding 2 be stated as a MEASURED ZERO over a
printed denominator rather than "I did not find one." Rule 21 limb (i) was discharged mid-session
(`3.0.0_SA_CVO` 92420) making `--enumerate` the sanctioned counter; I was already using it.
**What failed:** enumerating all EventBridge rules to map targets timed out at 120s; recovered by querying
the two named lambdas' resource policies directly and the Scheduler API separately.
**Gap found:** `aws events list-rules` + per-rule `list-targets` is O(rules) round-trips and is not viable as
a sweep on this estate; there is no comp-tool lens that answers "what triggers this lambda" across BOTH
EventBridge Rules and EventBridge Scheduler — two different APIs, and a census of one reads as absence of
the other. (Recorded, not chased.)

## 7. Blockers

**None.** One gate stands respected, not overridden: `git push` is INTEGRATOR-ONLY on shared `CLOUD`
(LD-0367/LD-0368), so this session's commits await `0.0.0_AB_MSTR`'s window.

## 8. Current State

- **Spec:** `docs/briefs/ETFS_COVERAGE_GUARDRAIL_BUILD_SPEC_20260901.md` — rulings in §0, catch-up port §3,
  gate §4, remediation ladder §5, email §6, Orion prerequisite §6a, non-goals §7, acceptance §8, carried
  findings §9, sequencing §10. Ready for `2.0.0_SA_COO` decomposition. **Nothing dispatched.**
- **Served ETFS state unchanged since my prior log:** `platinum/reports/{2026-07,2026-08}/` regenerated
  17:38Z, 43/43 trading days all partners, Desktop pack byte-identical to served.
- **Push state MEASURED:** local HEAD `1890d7785c`; `origin/CLOUD` = `6f9bf277f1`. **All this session's
  commits LOCAL.**

## 9. Next Steps

1. `[0.0.0_AB_MSTR]` Integration window — carry this session's commits to `origin/CLOUD`; the currently-
   SERVED July/August reports are produced by code that is still local-only.
2. `[2.0.0_SA_COO]` Decompose the spec per §10. **Read 92422 first — it was QUEUED, not delivered.** Two
   orderings bind: catch-up before gate; Orion alignment before the recipient change.
3. `[0.4.0_DS_ClientPlatform]` §6a Orion date-basis alignment — forward-only, prerequisite to the SEND.
4. `[0.7.0_AE_CloudOps]` Retire `etfs-canon-fanin` (§9.1); resolve finding 4 by deployed-bytes diff.

## 10. MCP traffic

3 inbound, all read + ACKed: 92420 (`3.0.0_SA_CVO`, Rule 21 limb (i) discharged — `--enumerate` certified);
92432 (Andrew rulings x3 relayed); 92443 (CVO's own correction — limb (b) of the PERFRP card was dropped at
its hop and is reserved back at Andrew; rulings 2 and 3 explicitly unaffected, so ETFS is untouched).
3 outbound: the ruling broadcast above.

**Carried from 92443 and worth more than the ETFS work:** I had relayed to Andrew the narrow generalisation
*"the card with the least content is the one most likely to be silently treated as decided."* `1.0.0_SA_CTO`'s
wider form supersedes it — **a card closes silently whenever the ruling's text CAN BE READ as covering it,
whatever makes that reading available**: least content is one mechanism, ambiguous labelling a second, lossy
transcription onto another seat's slate a third. **My own card 3 is an instance of the wider form, not the
narrow one** — it was not thin, it was nearly swallowed because the blanket phrase could be read as covering
it. Corrected to Andrew in-session.
