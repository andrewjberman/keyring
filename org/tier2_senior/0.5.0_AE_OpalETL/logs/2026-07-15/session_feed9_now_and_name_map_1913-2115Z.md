# 0.5.0_AE_OpalETL -- feed-9 Andrew-NOW arc + the model name map (2026-07-15 19:13-21:15Z)

**archetype:** MIXED (DIAGNOSE + IMPLEMENT + SCRIBE)

Continues session_reset_resume_fire_and_wave_1813-1900Z.md. This window was driven by FIVE
Andrew-direct messages (four in my terminal, one fuller parallel at CTO's), each recorded
verbatim + broadcast same-turn. Fire watch v2 stayed armed throughout; nothing touched the
22:00Z clock.

## 1. Feed-9 enumeration fix (Andrew-NOW ~19:13Z; record 48e278c01)

Investigation COMPLETE same hour (findings @ 90bc234b8, amended through 092e6308e):
- MECHANISM (source): roster-driven enumeration off users/access modelAccess, owned-filter.
- LIVE GRANT (probe 1): opal7 modelAccess = EXACTLY 11 fullAccess + 0 view; the 3 missing
  models ABSENT from the entitlement entirely (not view-filtered).
- CAPABILITY FORK (probe 2, control-first): owned model passes all 3 endpoints (perf
  recordCount 492 == wave pin); absent model 401s on performance + aum, same token/session.
  VERDICT: VENDOR-GRANT LIMIT -> named boundary to Andrew per CTO pin 2.
- HAZARD (probe 2b): enterprises/allocations?modelid=<unentitled> returns HTTP OK + the
  UNFILTERED universe (9,545 recs / 8 models / 0 target; control 71/1/71) -- vendor
  silently drops unknown filters.
- ANDREW RULED (B) verbatim: "The three missing models do not matter for our needs."
  Boundary accepted; augmentation + two-class guard MOOT; the 3 other-brand ids =
  expected-per-ruling in future R3 matrices (class stays loud for NEW ids).

## 2. Filter-integrity refuse-gate (CTO GO 195116Z; landed e5855aad0)

parse_allocation_ids(raw, expect_model_id=...) -- every record must PROVE model.id ==
requested; refuses on mismatch or missing nest; legacy form backward-compatible. Staged
OFF-TREE first (shared-worktree discipline), 4 new suite checks incl. the unfiltered-universe
mutant; applied via exact-match hunks; test_pull 42 OK on the real tree. CTO CLOSED-ACCEPTED.

## 3. Stale-test catch (own commit, 90ee0f188)

Full-module suite run surfaced test_smartx_client.py asserting the DEAD 17/min vendor ceiling
(killed by rulings 9d42d2d77 + c7cad5762) -- discriminated pre-existing via the pre-edit
snapshot failing identically; fixed by exercising the RULED reality (per_min=0 short-circuit
check added) rather than deleting the assertion. Module suite now 6/6 green. CTO: "textbook"
(his word); the resurrection risk (re-imposing a killed constraint to green a test) is the
banked lesson.

## 4. OPAL_STNDRD census answers (0.7.0~Z asks) + MSTR LCLRPO ack

- OWNER CLAIM on the record: etfs-netassets-daily IS the standing pathfinder/filepoint bronze
  feeder, mine (C4/OpalETL).
- smartx-model-monthly-pull: B1/B3-era PORTAL benchmarks feeder (grain-vs-cadence naming,
  both true); DISABLED decision-record unknown from my seat; NOT superseded by C5 (different
  consumer); portal-consumer check flagged before any dead-weight call; disposition rides my
  LCLRPO answer (owed MSTR in days; ~Z CC'd on the linkage).

## 5. THE NAME MAP (needs-roster rulings; delivered 092e6308e; CTO CLOSED-ACCEPTED 211047Z)

Andrew's needs roster reconciled by his ruled magnitude method (aum latest-day closing_equity
+ roster pairs; total $1,426,386,759 ties ~$1.428B ground truth -- the map's own integrity
check): five term models matched; LTC = Opal Conservative Growth ANDREW-CONFIRMED;
**main SMA = Opal Dividend Income ($18,586,236, sole [12-25M] candidate)**; Tax SMA =
Pathfinder Focused Opportunities CANDIDATE-ONLY ($4,659,490 sole match, no 'Tax' in name,
his 'maybe' honored); 50/50s STRUCK Eclipse-only BY RULING (never again a smartx gap);
Opal Equity Growth honest-UNMATCHED. NEGATIVE FINDING (durable): no SmartX model carries
'SMA' in its name -- every title hit is the SMARTX custodian tag; colloquial-name matching
structurally fails on this vendor. Standing table: SMARTX_INGESTION_ARCHITECTURE.md sec 8.
Dead ends measured en route (all on the record): valuation atom = model-type only by
construction; sleeves = 49F funding book ($8.7M); trading_type uniformly modelTraded;
models_summary endpoint 500s live and never landed bronze.

## AWAITING ANDREW (two confirm-words, his queue via both terminals)

1. Pathfinder Focused Opportunities == the Tax SMA? (or Tax SMA = not-in-SmartX)
2. 'Opal Equity Growth' -- where it lives, or confirm not-a-SmartX-model.

## Compiler Tools

| tool | use | result |
|---|---|---|
| comp-grep (prior window) | ligament definition | logged prior log |
| (this window) | -- | no comp-tool covers the SmartX vendor surface or monolith smartx/ trees -- the standing coverage gap, third consecutive log. Raw calls were operational probes (documented in findings) + one rail-checked live lambda read for the census answer. |

## MCP traffic (this window)

In: CTO x6 (re-time ack + pins, gate GO, gate accepted, ruling relay, map accepted), CloudOps~Z
x2 (census asks), MSTR x1 (LCLRPO flag), DS x2 (RAVC-close, feed-9 ack). Out: 14 (rulings
broadcasts x2 waves to COO/CTO/MSTR/DS, census answers, gate evidence, map delivery x3).
All loops closed; two confirm-words ride Andrew's queue.

## Next Steps

1. [21:56Z-] watcher v2 fires -> SCHEDULED-CORE-LANDED -> harness on refreshed bytes ->
   unpiped parity (day-3) -> verdicts to COO+CTO. V2-1 rides a GREEN 07-15 row.
2. [Andrew] the two confirm-words above; map rows update on his word.
3. [days] MSTR LCLRPO data/smartx disposition (incl. smartx-model-monthly-pull portal-consumer
   check); ~Z CC'd.
4. Standing: msn code-strike rides CTO's artifact-swap gate after tonight; cutover order
   untouched.
