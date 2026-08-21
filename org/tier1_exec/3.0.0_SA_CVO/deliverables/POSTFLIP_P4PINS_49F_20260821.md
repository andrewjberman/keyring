# POST-FLIP FILE -- ADVI/49F 4c repoint, 10-key group (PARITY_BAR section 8, five legs)

**Author:** 3.0.0_SA_CVO · 2026-08-21 ~16:45Z · **archetype:** VALIDATE
**Phase:** POST-FLIP (its own act, per `P4PINS_49F_PIN_FILE_SHAPE_20260818.md` section 4 -- never
an edit of the PRE-FLIP pins). **Consumes:** pins @28bb34a56d · certs @5c004cacf6 (+@ec0933f6d5,
@bb7f20c7a0) · emission manifest `933dfc1bf6b1` · route act (AE, CTO-accepted 65005) · flip
@9580e18b (DE). **Scope: exactly the 10 certified keys.** Held 4 + d14 are untouched and their
PRE-FLIP pins stay live under stale-pin law.

## VERDICT — CURRENT STATE (amended twice; read this, not the superseded line below)

**ALL FIVE PARITY_BAR §8 LEGS ARE CLOSED FOR THE SIX PORTAL-REACHABLE KEYS**, every figure from my
own reads: values ✅ · write-side ✅ · **read-side ✅ (consumer plane exercised, 6/6 twin requests
200, both failure paths exercised, zero-control re-run at my seat)** · mirror ✅ · ETag-identity ✅.
**THREE DENOMINATORS, each true of its own plane and none substitutable: CERTIFIED 10 ·
PORTAL-REACHABLE 6 · EXERCISED 6 of 6.** Rows 12/13 are UNRUN-BY-CONSTRUCTION (no live 49F
consumer, mechanism verified at source at this seat); rows 8/11 have no portal reader at all.
**LD-0441's non-discharge obligation is DISCHARGED** — closed on the raw markers, not on PROD.

> **SUPERSEDED, preserved as authored (the state at first landing, ~16:45Z):** *"FOUR OF FIVE LEGS
> MEASURED CLEAN AT THIS SEAT. THE READ-SIDE LEG IS SPLIT: its DESIRED half is measured; its
> EXERCISED half is UNRUN with a named dependency and owner. This file does not grade the flip
> complete, and section 8's own words are why: 'a grade that verifies (1)+(2) and ASSUMES (3)
> certifies a pipeline that may be serving a frozen vintage.' I will not close by assumption the one
> leg that discriminates a landed repoint from a stranded one."*
> **Kept because the refusal was the right call and the record should show it was made BEFORE the
> capture existed, not after it succeeded** — and banner-at-the-top because a superseded verdict
> sitting where the reader arrives first is the half-live-block class I corrected in two other
> people's documents this same afternoon.

## LEG 1 -- VALUES (own reads)

10/10 twin objects byte-identical to the certified anchors (ETag + size, head-object per exact
key): mix_summary `a779b1c5` 11,129 B · leaderboard `6225228b` 2,167,593 · ownership_map
`68b0f05e` 566,205 · timeseries_overview `d89fe8a1` 84,991 · cumulative_chart `0ea66403`
1,050,145 · clients-tab-slim `8e85ac59` 636 · timeseries_chart `ab37740d` 7,260,521 ·
timeseries_chart_full `ab37740d` 7,260,521 · partner_analytics_quarterly `8382e401` 1,513,413 ·
partner_analytics_annual `80427d7d` 1,086,444. **Nothing re-emitted between cert and flip.**

## LEG 2 -- WRITE-SIDE LOCATION (live primitive, not a config read)

Same head-object pass: all 10 present at `s3://opal-data-portal-v2/platinum/advi/49financial/`,
LM 15:03:17-15:04:19Z, unchanged since emission. **NEVER-WIDEN CONTROL, same listing call:** twin
root carries exactly 10 data keys + 2 manifest objects; **held/structural keys present = 0** of 5.
Present-set and absent-set from ONE call, so the instrument demonstrably discriminates.

## LEG 3 -- READ-SIDE LOCATION: **SPLIT** (this is the honest state)

**DESIRED half -- MEASURED at this seat from the LANDED portal source (`git show HEAD:` reads, not
a report):** `ADVI_ROUTE_LIVE = true` (:109) · `adviTwinUrl` (:121-123) constructs
`/api/scoped/advisor-intelligence/platinum/advi/{firm}/{leaf}` -- the route-act path class ·
**exactly 10 registry entries carry `state: 'flip'`** (lines 153-160, 165, 166; line 143 is the
TYPE DECLARATION and is not an entry -- a `grep -c` reading 11 was my own imprecise instrument,
settled by reading the lines) · **5 entries carry `held`/`structural` and structurally cannot
prefer the twin**, so flipping the constant cannot widen the determination.
**THE d12 PER-CONSUMER BINDING, verified at source (the leg DE's cross-check made mandatory):**
`advisor-intelligence.ts:305-310` binds key `timeseries_chart_full` (legacy base
`artifacts/timeseries_chart.json`, the gold-plane consumer) and `:441-443` binds key
`timeseries_chart` (legacy base `platinum/firm/timeseries_chart.json`, the windowed consumer) --
matching the ratified per-consumer mapping. **This binding is load-bearing precisely because the
two twins are byte-identical today (leg 5), so a cross-serve is invisible to values and to shape;
the URL is the only discriminator until the 1,091-day truncation re-arms.**

### ⚡ EXERCISED HALF -- AMENDED 2026-08-21 ~17:00Z: THE CAPTURE RAN, AND IT CORRECTED THIS FILE'S DENOMINATOR

**CONSUMER PLANE ESTABLISHED for 6 of 6 REACHABLE keys** (DE's netlog, real bearer, 180 requests
in a 9s post-load window): `mix_summary` · `leaderboard` · `timeseries_overview` ·
`cumulative_chart` · `partner_analytics_quarterly` · `partner_analytics_annual` -- all **200 at
the twin URL**. That is the portal REQUESTING the twin, which AE's route fetch structurally could
not establish. **HELD-KEY INVERTED ORACLES in the same capture: `dashboard`, `fee_efficiency`,
`header_metrics` still served from `platinum/firm/` (200), ZERO twin requests for any held key --
over-flipping is measured absent, not assumed.**

⛔ **ROWS 12/13 ARE UNRUN-BY-CONSTRUCTION, NOT PENDING ANYONE'S EFFORT — and I verified the
mechanism at source myself rather than accept the report** (`git show HEAD:` reads at this seat):
- **Row 12 `timeseries_chart` (WINDOWED):** its only caller is `PartnerAnalytics.tsx:273`,
  `enabled: usesStackedBars`, and `:171` derives that from `tenantLayout.features.barChart.stacked`.
  **Measured across all four tenant layouts: `49financial` = `false`; only `inflection` = `true`.**
  The 49F tenant NEVER requests it — and the one tenant whose gate is open has NO TWINS (the twins
  are `platinum/advi/49financial/` only).
- **Row 13 `timeseries_chart_full` (FULL-DOMAIN):** `getCumulativeChart` is a **DEAD EXPORT** — one
  definition (`advisor-intelligence.ts:304`) and exactly three references, **all of them comments**
  recording that `getTimeseriesOverview` replaced it. Zero importers.

**THE DENOMINATOR THIS CORRECTS, stated plainly because it is mine to correct:** the portal-visible
flip population for the 49financial tenant is **SIX**, not eight (DE's P4R-1 finding 2C was right
as far as it went and two short) and not ten (rows 8/11 have no portal reader at all). **Certified
set 10 · portal-reachable 6 · exercised 6/6.** Three different denominators, each true of its own
plane, and none of them substitutable for another. **Nothing here says unpublish: rows 12/13 remain
correctly published and certified — the portal simply is not their consumer today.**

⚠ **MY OWN MANDATORY-L1 REQUIREMENT ON ROWS 12/13 IS THEREFORE UNSATISFIABLE, AND I AM RECORDING
WHY RATHER THAN QUIETLY DROPPING IT.** I made it mandatory because the d12 pair is byte-identical,
so the URL is the only cross-serve discriminator. That reasoning stands. What I had not measured is
that **neither key has a live 49F consumer to cross-serve** — so there is no cross-serve to catch
at this tenant today. **THE HAZARD IS DORMANT, NOT RETIRED: it re-arms the moment a consumer
appears** (a tenant flipping `barChart.stacked` to true, or `getCumulativeChart` gaining an
importer) **and it would then be invisible until the 1,091-day truncation re-arms the content
plane.** Under the channel's axis that is `INERT` today with a named re-arm condition — not
`ARMED`, because the bindings at source are CORRECT (`:305-310` and `:441-443` verified above) and
the harm needs a future consumer wired wrong, not a present trap.

### ⚡ SECOND AMENDMENT ~17:05Z -- LEG 3 IS CLOSED. I READ THE RAW ARTIFACTS MYSELF.

Capture landed at `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/p4r3_flip_capture_20260821/`
(@cd89ff7e80, 15 git-tracked files, deliberately un-digested by DE). **Every figure below is my own
read of those files, not DE's summary of them:**

- **L1 CONSUMER PLANE — 6 distinct twin keys requested by the portal, EVERY twin request 200**
  (`awk` over the netlog for any non-200 on a twin path returns EMPTY): `mix_summary` ·
  `leaderboard` · `timeseries_overview` · `cumulative_chart` · `partner_analytics_quarterly` ·
  `partner_analytics_annual`. **This is the plane AE's route fetch structurally could not
  establish** — the portal ISSUING the request, not merely the URL answering one.
- **NEVER-WIDEN AT THE CONSUMER PLANE (stronger than the listing-layer control):** all five
  held/structural keys measured **0 twin requests each**, while `header_metrics`, `dashboard` and
  `fee_efficiency` appear served from `platinum/firm/`. Over-flipping is now measured absent at the
  plane where it would actually manifest.
- **L2 (shape mutants) 6/6 LOUD:** every key emits `CONSOLE[error] [P4-REPOINT-49F] SHAPE MISMATCH
  on {key}: twin ... returned 200 with an unrecognized shape. Serving legacy and reporting -- this
  is a cutover defect, not a transport fallback.`
- **L4 (forced 503) 6/6 QUIET:** every key emits `CONSOLE[warning] [P4-REPOINT-49F] {key}: twin
  unavailable, serving legacy`, page still renders. **The designed asymmetry is visible in the raw
  severities themselves — `error` vs `warning` — not merely in the wording.**
- **ZERO-CONTROL, re-run at my seat:** `SHAPE MISMATCH` count in the L1 capture (no mutant, no
  forced failure) = **0**. The marker grep can return zero, so its non-zeros mean something.
- **ONE ARTIFACT OF MY OWN INSTRUMENT, recorded:** my first pass also grepped for the diagnostic
  ENUM string `fallback-shape-mismatch` and got 0 across all six, which briefly looked like a
  missing signal. Reading the raw text settled it: the console prints the human-readable marker;
  the enum lives in the in-memory `adviReadDiagnostics()` record and is never emitted to console.
  **My pattern was looking for a string that surface does not produce — a wrong-question zero, not
  an absence.**

**LEG 3 VERDICT: CLOSED for the 6 reachable keys** (DESIRED + EXERCISED both measured). Rows 12/13
remain UNRUN-BY-CONSTRUCTION per the mechanism above; rows 8/11 have no portal reader at all.
**LD-0441's non-discharge obligation is DISCHARGED by this read** — it closed on the raw markers,
not on PROD being green.

**FIVE-LEG STATE: values ✅ · write-side ✅ · read-side ✅ (6 reachable) · mirror ✅ · ETag-identity ✅.**

**ORIGINAL PRE-CAPTURE TEXT, preserved:** *"UNRUN. Dependency named, owner named:* a real bearer
token through the auth path. DE holds no token (minting is AE's lane, 65048); AE runs the capture or supplies the bearer.
**Required artifacts: the netlog per plane (DEV, then PROD), L1 MANDATORY on rows 12/13, and the
console markers from the 8 L2 mutant fixtures + the L4 `--fail` runs -- emitted, read by me, not
summarized.** *DE's refusal to produce a token-less capture is correct and worth recording: it
would have shown the tolerant read falling back to legacy and NOTHING about the flip -- an
artifact that looks like evidence.*

**WHAT AE's ROUTE EXERCISE DOES AND DOES NOT COVER (two planes, stated so they are not merged):**
AE proved 10/10 twins return 200 byte-identical through the auth path -- that is the ROUTE plane
(does a request for the twin URL resolve). It does NOT establish the CONSUMER plane (does the
portal REQUEST that URL). Only the netlog does. Both are needed; neither substitutes.

## LEG 4 -- THE MIRROR LEG (the counterpart; the only leg that separates landed from stranded)

**16/16 legacy keys re-headed against their PRE-FLIP pinned LM+size: 16/16 UNMOVED.** Baseline
captured minutes before the flip and re-verified after. *Presence at the new root can never
discriminate a landed repoint from a stranded one; only the counterpart can -- and a silently
failed repoint ADVANCES the old root.* It did not move.

## LEG 5 -- ETag IDENTITY / the d12 blind spot, stated as a standing condition

`timeseries_chart.json` and `timeseries_chart_full.json` are byte-identical today (`ab37740d`,
7,260,521 B both) -- **correct by design, not a defect**: the `PLATINUM_NNA_TRUNC_DAYS = 1091`
window is vacuous while the canonical domain is 774 days. **CONSEQUENCE CARRIED FORWARD: while
this holds, L1 (the URL) is the ONLY discriminator of a d12 cross-serve. The content plane regains
discrimination when the domain crosses 1,091 days** -- at which point a future pass may treat
value/shape legs as sufficient for these two rows, and not before.

## ⛔ PRODUCT-PLANE CONSEQUENCE -- NAMED HERE BECAUSE THIS IS WHERE A PROMOTE READER LOOKS (added 17:15Z at CTO's ask, on DE's P4R-4 finding)

**THE FLIP CARRIES THREE SEPARABLE COMPONENTS AND THEY MUST NEVER BE BLENDED INTO ONE "certified"
LINE:** (1) ROUTE-MOVE — DELTA=0 by construction, which my certs establish; (2) CONTENT-REFRESH —
`data_as_of` 08-19 → 08-20, one trading day, benign; (3) **DOMAIN TRUNCATION + DIMENSION COLLAPSE,
which is neither** and is USER-VISIBLE:

| | legacy serve | advi twin |
|---|---|---|
| `cumulative_chart.date_range` | 2020-01-02 → 2026-08-19, **2,421 days** | 2024-07-08 → 2026-08-20, **773 days** |
| `cumulative_chart` geo | 9 states + Other | **`['Other']` alone** |
| `timeseries_overview` periods | quarterly 27 / monthly 80 / annual 7 | 9 / 26 / 3 |

**A 49F advisor opening Advisor Intelligence after this flip would see trend charts beginning
2024-07 instead of 2020-01, and a geographic breakdown reduced to one bucket.**

**MECHANISM, MEASURED AT THIS SEAT — and it is NOT a port defect:** the canonical series runs
**529 partitions from exactly 2024-07-08**, and the **ENTIRE Schwab silver tree floors at the same
date** (`dim_balance`, `fact_acc`, `dim_position`, `fact_trn`, `fact_sec`, `dim_transaction` — all
2024-07-08). The twin shows everything its source has. Likewise geo — the canonical dimensions tree
carries eleven dims and **none is geographic**, so the producer's "no canonical dim" declaration is
literally true at the artifact layer.

> ⛔ **BOTH OF THE ABOVE ARE PLANE-LIMITED TRUTHS WHOSE IMPLICATIONS I OVERREACHED, CORRECTED
> WITHIN THE HOUR BY TWO OTHER SEATS. THE MEASUREMENTS STAND; THE INFERENCES DID NOT.**
> **HISTORY:** I wrote that reaching 2020 needs data "not in this plane at all," which invited
> *the data does not exist*. **It does** — I then measured `opal-data-bd/gold/canonical/`:
> `performance`/`nna`/`account_gains` **2,422 filename-dated partitions 2020-01-02..2026-08-19**,
> `holdings` 2,423 from 2020-01-01. *(Corrected: my first pass read 2,423 ending 2026-08-21 — the
> regex swept the LastModified COLUMN as well as the filename, mixing write-dates into data-dates.
> Substance unchanged, figures were not.)* So extending history is a **CROSS-PLANE PORT**, not a
> vendor re-ingest — **and I then RAN the reconciliation (CTO's word): same date 2026-08-18, BD
> `sum(aua_current)` $1,809,106,006.08 across 3,092 RELATIONSHIP rows vs Schwab
> `sum(net_mv_plus_cash)` $1,802,835,074.50 across 7,315 ACCOUNT rows — DELTA −$6,270,931.58
> (−0.347%), account-count delta 837. CLOSE, NOT EQUAL, AND AT DIFFERENT GRAINS: consistent with
> two books of one firm, so a port is feasible-looking; not a tie, so a splice without a basis
> reconciliation would put a visible step at 2024-07-08 in a client-facing chart.*
> **GEO:** I wrote that a geo breakdown needs a dimension that does not exist — true of the
> canonical layer, and it implied geography was *unavailable*. **It is not.** COO measured
> (Andrew-prompted) `schwab/08335338/silver/fact_acc`: **`ac_st` 100% populated, 7,331/7,331 rows,
> 48 states — and the top values ARE the legacy chart's own state set.** The geography Schwab
> supplies is right there; the canonical layer simply never built a dim over it.
> **THE PATTERN IN MY OWN WORK, named because it happened TWICE IN TEN MINUTES:** each time I
> measured a plane correctly, flagged the adjacent plane as unmeasured — and then let the
> unmeasured half carry weight in the framing anyway. **Flagging an unmeasured premise is not the
> same as refusing to lean on it.** The session's own thesis, landing on its verifier: a sweep that
> closes a blind spot while hiding its own is the same defect one level up.
> **WHAT NEITHER OF US HAS MEASURED, and it is now the decisive one:** whether BD-plane history
> RECONCILES with the Schwab-sourced canonical plane (same account universe, same valuation basis).
> The planes overlap 2024-07-08..2026-08-20, so **it is testable** — and splicing two vendors' books
> without that test would manufacture a discontinuity in a client-facing trend chart, which is worse
> than the truncation. *Also observed, unexplained: every BD gold history object carries
> LastModified 2026-08-21T00:51Z — the full 2,423-file span was materialised hours ago. Worth an
> owner's read before anyone treats that plane as long-settled.*

**DISPOSITION:** CTO withdrew the never-widen half on `cumulative_chart` + `timeseries_overview`;
those two join the HELD class. **My certs are unchanged and were never product clearance** — see
the cert's own plane-limitation section (@ab585bb00e). The remaining four flip keys stay cleared
pending DE's per-key P4R-4 figures.

## CROSS-DAY COMPONENT -- the flip's own movement, isolated by the pins

The legacy serve carried content-date **2026-08-19**; the twins carry **2026-08-20**. That
one-day movement is **the flip's own**, not a divergence: the PRE-FLIP pins measured both sides at
a SHARED content-date (08-19) precisely so this component could be separated from the
divergence component. Per the issuer's ruling (COO 64729), each phase file is internally
same-content-date and the cross-day difference is stated here rather than folded into a delta.

## 08-19 PROVENANCE -- final (a)-form

The twins' series include the 2026-08-19 canonical partition, **re-produced by a RECORDED
PRODUCTION-HOST BACKFILL ACT** -- SSM CommandId `6b96ab4b-eeb1-4f1a-a0cb-23c156bf368c`, ledger
20260821T1520Z, self-uploaded log `_logs/chain_backfill_0819_20260821T151733Z.log`. Named actor,
done date. The earlier "superseded at backfill" wording was withdrawn as an unbacked promise. The
byte-plane re-emission is DISCLOSED as encoder-environment (14/14 JSON manifests byte-identical
over the same frames = the discriminating control; accrual_materiality full-column value-identity
via S3-versioning recovery = the second), and pins/certs stand on the VALUE plane per COO 64815 --
independently confirmed at this seat at full field grain (fleet rebuilt from the production bytes:
pin-side 14/14 payloads and twin-side 7/7 keys diff ZERO).

## WHAT THIS MEANS FOR THE DT PROMOTE -- stated, not decided

The promote decision is the promote owner's. **What I can say:** values, write-side, mirror, and
the never-widen control are all measured clean, and the consumer-plane DESIRED state is verified
at source. **What I cannot say:** that the portal has been OBSERVED requesting the twin URLs --
that is the unrun EXERCISED half, and it is the leg that would catch a stranded repoint. Promoting
before it runs is a decision someone makes knowing that; it must not happen by accident, which is
why it is stated here in the file that the DT trigger reads.

-- 3.0.0_SA_CVO
