# 49F twin flip — PRODUCT-READINESS FINDING and the determination it changed (CTO, 2026-08-21 ~17:1xZ)
**archetype:** VALIDATE

**In one sentence:** every portal-reachable 49F twin key carries a user-visible product regression
against the legacy serve — history truncation, dimension collapse, or advisor-population loss —
all DECLARED at the pin layer as in-band, NONE decided at the product plane until `0.4.0_DE`'s
P4R-4 named-deltas check measured them (65234, 65284, 65323) an hour before PROD. **The
single-green-Friday product promote of the 49F twins does not happen today. This is a readiness
finding about the SOURCE, not a fire miss and not a port defect.**

## What DE measured (live twin vs live legacy, recursive array-length diff — a top-level shape diff read "identical" on three of these)

| key | legacy | twin | class |
|---|---|---|---|
| `cumulative_chart` | 2020-01-02..2026-08-19 (2,421 d, 352 pts); geo 9 states + Other | 2024-07-08..2026-08-20 (773 d, 111 pts); geo `['Other']` | history truncation + dimension collapse |
| `timeseries_overview` | quarterly 27 / monthly 80 / annual 7 | 9 / 26 / 3 | history truncation |
| `partner_analytics_quarterly`, `_annual` | AUA-by-Office 9 offices; AUA-by-State unassigned 0.069% | Office 100% `'other'`; State 100% unassigned | dimension collapse ×2 |
| `leaderboard` | 163 entries every window | 146; **20 named advisors absent** | population loss — mechanism UNKNOWN (identity coverage? defect?) |
| `mix_summary` | mix_periods 5 quarters | 1 | history truncation |

## Mechanism (CVO 65279/65312 — measured, not inferred)

- The 2024-07-08 floor is **the entire Schwab silver tree's floor** (`dim_balance`, `fact_acc`,
  `dim_position`, `fact_trn`, `fact_sec`, `dim_transaction` all earliest 2024-07-08); the
  canonical series (529 partitions) inherits it. **No recompute/backfill can extend it — the
  source rows do not exist in this plane.** Legacy's 6.6 years are Black-Diamond-side history.
- No geographic dimension among the 11 canonical dims; office/state are plausibly the same class
  (CVO to confirm). The leaderboard −20 is a different mechanism and is the one item that could
  be a DEFECT rather than an extent — it needs its own measurement cell.

## The determination as it now stands

CTO never-widen half **WITHDRAWN on all six portal-reachable keys** (my GIVEN on four was
conditional on exactly the figures that then failed). COO's half was already withheld on the two
history keys; the four-key GIVEN carried the same condition. Held keys (4) + d14 unchanged.
**No consumer-visible key clears the two-halves control today.** DEV registry → all six `'held'`
(DE); promote stood down, worktree torn down, origin/PROD untouched at `8a96c916` (DT/MSTR).

**What STANDS, built today and reusable per key:** the route act (remedy A, exercised, tenant
assertion), the registry-as-data flip, the certs, the pins, the oracle table, the capture
discipline. What changed is the answer to *"is the canonical source ready to serve this
product?"* — measured at the product plane for the first time.

## Carded to Andrew — ONE product-readiness question, six keys

Canonical = Schwab-authority from 2024-07-08, no geo/office/state dims, leaderboard population
short 20 pending mechanism. Legacy = 6.6 years, nine states/offices, 163 advisors. **REC: keep
49F Advisor Intelligence LEGACY-SERVED; commission the gap closures as NAMED programs** (vendor
history feasibility — does the vendor supply pre-2024-07 at grain, does it reconcile; BD-side
attribute dims in canonical; identity coverage for the leaderboard); **re-flip PER KEY as each
closes.** The word "backfill" does not appear in any option until obtainability is measured.

## ⛔ CORRECTIONS within 20 minutes of writing (two measurements that change the REMEDY, not the hold)

1. **HISTORY EXISTS IN THE ESTATE — the "vendor procurement" framing above is RETRACTED** (CVO
   65337, own retraction): `opal-data-bd/gold/canonical/` carries 2,423 dated entries
   2020-01-02..2026-08-21 (performance, nna, holdings, account_gains) — the legacy chart's span.
   The Schwab plane's tree-wide 2024-07-08 floor stands, so the remedy is a **CROSS-PLANE PORT**
   (BD gold → Schwab-authority canonical) with one named feasibility test CVO is running now on my
   word: **do the two vendors' books RECONCILE** (account universe, valuation basis, NNA
   definition) across the 2024-07-08 seam? If not, a splice manufactures a discontinuity in a
   client-facing trend chart — worse than the truncation. Nobody ports until that read lands.
2. **GEOGRAPHY IS NOT SOURCE-LIMITED — "no geography available" was FALSE** (COO 65343, measured
   at Andrew's direct prompt): `schwab/08335338/silver/fact_acc` carries `ac_st` at **100%
   population (7,331/7,331, 48 states)** plus city/zip/country, and the top states ARE the legacy
   chart's set. "No canonical geo DIM" (CVO) is true; the remedy is **an UNBUILT canonical
   dimension over data we already hold** — a scoped dim build (DS lane; dim + two emit sites +
   reader vocabulary + pin refresh), not a program. Sizing is mine; it is small.
3. Still UNMEASURED and stated as such: **OFFICE** (the `views.ofc` collapse — is office a Schwab
   field at grain or BD-side? measure before classing) and the **LEADERBOARD −20 named advisors**
   (identity coverage vs defect — the one item that could be a BUG).

**The hold on all six keys stands regardless — a twin serving `['Other']` today is a product
regression today whatever the remedy costs. What changed is the card: history = port-ability test;
geo = scoped build; office/leaderboard = measure first.**

## ⛔ THE COMPLETE PASS (DE 65377, recursive array/key diff over ALL TEN certified keys) + the reconciliation read (CVO 65382)

**NINE OF TEN certified keys carry material regressions; exactly one (`clients-tab-slim`) is
clean.** Beyond the six portal-reachable keys above: `timeseries_chart` / `_full` adv.data 2,422 →
774; **`ownership_map` SEVERE** — 198 arrays shrunk, 48 keys dropped, per-advisor accounts ~halved
(kyle_sims 844 → 352), certified + published with no portal reader (any non-portal consumer gets a
half-populated book). Geo donut is 48 → 1 segments, not merely "collapsed". **Ruled: hold three
more (ownership_map, timeseries_chart, timeseries_chart_full); clients-tab-slim stays 'flip'.
Final DEV census FLIP 1 / HELD 13 / STRUCTURAL 1 (DE @6d0403a5 + the three-row follow-up). THE
CUTOVER IS STAGED, NOT LANDED.** This is the canonical plane's extent showing through every key
that carries history, geography, office, or population — not per-key bad luck.

**Reconciliation read (CVO, 2026-08-18, both planes, own reads):** BD `gold/canonical/performance`
relationship-grain 3,092 rows, `sum(aua_current)` $1,809,106,006.08 (claiming 6,478 accounts) vs
Schwab `canonical_valuation` account-grain 7,315 rows, `sum(net_mv_plus_cash)` $1,802,835,074.50 —
**delta −$6,270,931.58 (−0.347%), account universes differ by 837, measures differ.** Consistent
with one firm's two books; NOT a tie. The history half is therefore a **scoped reconciliation
program with a measured starting delta** (explain the basis difference, reconcile grain + universe,
THEN splice) — never "a port," never "a backfill." CVO's quotable BD span: 2,422 partitions
2020-01-02..2026-08-19 (holdings 2,423 from 2020-01-01). **Owner needed (bd lane):** every BD gold
history object carries LastModified 2026-08-21T00:51Z — the whole plane was written this morning
and is not long-settled; that goes on the reconciliation program's first page.

**Exposure question CLOSED — nothing was exposed at any point.** Andrew-direct at the COO terminal
~17:24Z, VERBATIM: *"DEV is fine dont worry about it thats purely local on my device"* (COO 65395,
recorded + broadcast). Corroborated independently by DT (65401) and AE (65407), full 3-workflow
denominator with a positive control: `ci.yml` (DEV) has ZERO aws/s3/cloudfront refs (its one
"upload" is a GitHub Actions artifact); `deploy.yml` is the ONLY deployer and triggers on PROD alone
(4 publish refs); `promote-to-prod.yml` is manual dispatch. **The DEV branch deploys nowhere;
origin/PROD is untouched at 8a96c916; the deployed client bundle predates the flip and requests
legacy URLs.** AE's route measurement (the router WILL serve twin bytes to a valid token) is true on
the route plane and has no consumer — two planes, and the exposed one has no reader.

## ⛔ SOVEREIGN RULING 19:18Z — THE FLIP IS HELD ON TWO CONDITIONS, and the second one nobody had

**Andrew-direct 2026-08-21 ~19:18Z (relayed COO 65457, recorded + broadcast), VERBATIM:** *"the position on
flipping this should be held until source gaps and schedule are addressed, that needs to be documented,
including relevant publisher resources, paths, and etc for the switch covering what is the current
route and what is the contemplated route."* **The hold IS the decision, with two named release
conditions — BOTH required, NEITHER sufficient alone.** It binds the FLIP only: the canonical chain
runs daily, the BD-migration programs proceed, nothing else is held. The REC above ("keep legacy-served;
run the programs; re-flip per key") is SUBSUMED by his ruling — the release now needs the schedule leg too.

**The documentation he ordered lives at COO's seat and stays there as the MAINTAINED home:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/ADVI_49F_SERVE_ROUTE_CURRENT_AND_CONTEMPLATED.md` @ad8bb50e56
(current route: `opal-data-bd/platinum/firm/*`, D-series emitters `runners_49f/d01..d14`, 04:00Z serve of
record; contemplated route: canonical → `d_publisher_port` → `portal-v2/platinum/advi/49financial`, CF
path-class override, tenant assertion, `adviKeyRepoint` registry; the two hold conditions; BD-exclusive
dims; what stands; five UNMEASURED items). The owned-paths gate refused it under `docs/architecture/`
(ANY_CTO lane) and COO correctly did not override; I am NOT copying it into my lane — a second home for a
document carrying five open measurements is the two-homes defect. This finding points at it.

**THE SCHEDULE LEG — grounded at my seat, then CLASSIFIED at source (Rule 22a: a detector that cannot tell
a hold from neglect manufactures the wrong reflex):**
- APPLIED: `aws scheduler get-schedule advi-49f-publisher` → **State DISABLED**, `cron(15 13 * * ? *)`,
  target `advi-49f-gold-dispatch`; `list-schedules --name-prefix advi-49f` → 2 (publisher DISABLED,
  **`advi-49f-gold-floor` ENABLED**); `events list-rules --name-prefix advi-49f` → 0. *My first probe was
  `events describe-rule` → ResourceNotFound — the wrong-SERVICE zero; CVO and DE hit the identical trap in
  the same minute, DE with a positive control that fired inside the wrong plane. Three seats, one trap.*
  The split explains the measured pattern exactly: canonical fresh (floor enabled), twins frozen at
  15:03–15:04Z (publisher disabled; today's twin publish was manual).
- DESIRED + CLASSIFICATION: **`infra/aws/terraform/opal-assets/advi_49f_publisher.tf` (AE @1abc54fa4c,
  2026-08-19, OPAL_ADVIPOINTERS P4-PUBIAM-49F / P4I-3) declares `state = "DISABLED"` DELIBERATELY** —
  header verbatim: *"STATE = DISABLED, DELIBERATELY — THIS IS THE CONTRACTED DESIGN, NOT A HALF-LANDING.
  The publisher schedule activates only when DS~B's emitters are deploy-ready."* Activation = ONE TF
  change, three steps named in the header: (1) mint `aws_ssm_document.advi_49f_publisher_dispatch` with
  DS~B's contracted body; (2) append its name to the dispatcher's `ALLOWED_DOCUMENTS` env; (3) flip state
  to ENABLED — and *"even a stray manual enable fails CLOSED + LOUD"* (allowlist refuses; document absent).
  **So: DELIBERATELY-HELD, not stale-by-neglect; the reflex "re-enable it" is wrong twice (not the remedy,
  and it fails closed).** What lapsed is the ACTIVATION ACT — its condition (emitters deploy-ready) was met
  today and no seat fired it because every seat was on the cutover. A correct hold outlived its condition.
- Consequence: the second release condition is a **named existing act (P4I-3 activation), AE-class, with a
  named contract input (DS~B's entrypoint + args)** — not a new build, not an open question. Routed 19:23Z
  (COO re-grounds P4I-3 at pickup; AE confirms authorability; AE queued — no live session at 19:23Z; MSTR
  holds seating).

**clients-tab-slim → HELD (CTO word to DE 19:23Z).** The one clean key passes the source-gap condition and
fails the schedule one (same publisher, same freeze); my stays-flipped ruling predated his word and yields
to it. DE flips; the census DE reads after the act is the record (expected FLIP 0 / HELD 14 / STRUCTURAL 1).

**Still UNMEASURED, owner named, no clock:** the 04:00Z legacy producer of `bd/platinum/firm/*` is neither
an EventBridge rule nor a Scheduler entry (COO enumerated both) — AE read-only census (on-host cron /
systemd timers on the bd EC2 plane; event chain off `bd-49f-session-*`). **Nothing is decommissioned
until it is named; nothing is being decommissioned now.**

## Why the afternoon's controls were right and still missed this

Pins measure values against DECLARED bands; certs cover route + value planes; the consumer-plane
capture proved the portal REQUESTS the twin; the never-widen halves were given on KEY SCOPE. Every
one was true and none was about the product plane. "Declared means the pipeline knew, not that
anyone decided a client should see it" (CVO, written into the cert itself). DE's P4R-4
never-blended discipline is the control that catches this class, and it fired one hour out.
