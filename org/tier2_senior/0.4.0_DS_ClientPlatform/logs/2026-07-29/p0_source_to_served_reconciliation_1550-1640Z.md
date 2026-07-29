# Session log — 0.4.0_DS_ClientPlatform (base) — 2026-07-29 1550Z-1640Z

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

**Window:** since my previous log `bdcd9b580a` (covered 1450-1550Z). This window = the NEW P0
from Andrew (source-to-served reconciliation), the 15:52:29Z slice write, an attribution
retraction, and the accrual-bridge history question.

## The P0 (Andrew via CTO 155702Z) — source-to-served reconciliation

**The indictment, accepted:** our oracle was derived by two agents from the SAME dim partitions
the producer reads -- internal consistency, not correctness. **The sharpest version lands on my
own work:** I spent the afternoon making the falsifier set more rigorous (found F1-F6's unstated
write premise, got the F4 qualifier adopted). **Every improvement made a CONSISTENCY test more
precise; none made it a CORRECTNESS test.** That is VERIFICATION LAW (6) -- a rigorous instrument
on the wrong axis survives review -- and I applied it to other agents' instruments today, not to
the oracle I was grading against.

Scoped to ONE firm end-to-end per CTO: **cottonwood** (known defect = ground truth to check the
METHOD against; genuinely different lineage; unavoidable vintage question).

### RECONCILED EXACTLY, INDEPENDENTLY — the AUM leg
Path: raw custodial parquet, pandas, no gold logic / no dim / no mdpf_revamp.
  `s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/date=2026-07-24/data.parquet`
  389,605 B retrieved == 389,605 reported; 16,825 rows; _source_as_of 2026-07-24.
  **DERIVED sum(Market Value) = 463,015,162.92 == SERVED partner_custody_total. DELTA 0.00.**
Decomposes exactly against the oracle: model_aua 125,132,212.03 + non_model 337,882,950.89
= 463,015,162.92. **First independently-established number of the day.**

### A DELTA WITH A NAMED CAUSE — and the artifact names it itself
account-distribution total_aum 125,894,245.45 vs oracle model_aua 125,132,212.03 = **762,033.42**.
Cause declared IN-BAND: `meta.sleeves_dropped = {leaf_hits 3, dollars 762033.42, names ["Sleeve -
Core Money Market","Sleeve - Equity","Sleeve - Tax-Free Bond"]}`. 125,894,245.45 - 762,033.42 =
125,132,212.03 exactly. **NOT a defect** -- a declared definitional difference, quantified to the
cent. Flagged only because a reader comparing the two artifacts without opening `meta` sees $762k.

### UNRECONCILED (declared, not laundered) — the COUNT leg + all of 49financial
- cottonwood count: PREDICATE `strategy_name contains "Opal"` over fact_model_assignment/
  date=2026-07-28 (915 rows) -> **296** vs served 292 / active 294. **My predicate is the problem:**
  45 distinct strategies incl. a whole `Core | Satellite NN` family the substring misses, plus a
  canonical crosswalk (PRD v1.23 @a41c582ba) I did not apply. Within-4 off a substring guess is a
  COINCIDENTAL NEAR-MISS, not a reproduction.
- 49financial: 5 candidate AUM measures against served 1,404,555,608.22 -- equity
  1,384,985,689.79 / equity+cash 1,399,674,845.48 (**closest, -0.35%, -$4,880,762.74**) /
  +accruals 1,399,846,935.11 / long_equity 1,414,881,393.16 / roster.value 1,496,635,440.64.
  Counts: 9,627 distinct allocation_id; 7,178 with equity+cash>0; roster 'open' 7,177 vs served
  active 7,090. **The 0.35% near-miss is the dangerous shape and I refused it in BOTH directions**
  -- close enough to read as rounding, far enough to be a real $4.88M gap; an unattributable delta
  is an unvalidated predicate, not a finding.

### >> HEADLINE: THE CHAIN READS COTTONWOOD'S SOURCE ~3 HOURS BEFORE IT LANDS <<
  producer generated_at            2026-07-29T00:33:22.950505Z
  fact_holdings date=07-27 LANDED  2026-07-29T03:30:38Z   (2h57m LATER)
**So the producer was CORRECT** -- 07-24 genuinely was the latest available at read time.
STRUCTURAL across a 38-object census (landings all ~23:30 LOCAL = ~03:30Z; one off-cadence
exception, date=07-22 at 07-23 10:17:06). **Nothing is broken; the ORDER is wrong, every day.**
**THIS INVERTED MY OWN 154056Z CALL** ("cottonwood did not advance -> fix-shape 2, stated basis
rule"). The SOURCE has advanced to 07-27; a run after the landing yields cottonwood@07-27 = the
same vintage as inflection@07-27 which global ALREADY includes. **Cheap fix = run ordering; the
expensive design question may not need answering.**

### >> THE MECHANISM (the finding CTO asked for "in those words") <<
**A FIRM RECONCILES INDEPENDENTLY IFF ITS ARTIFACT DECLARES ITS OWN BASIS IN-BAND.**
  cottonwood  full meta (value_date, assignment_date, sleeves_dropped, income residual,
              canonical_merge, count_axis_note) + basis + source -> RECONCILED TO THE CENT
  49financial NO meta; basis+source only                          -> UNRECONCILED
  inflection  NO meta; basis+source only                          -> same shape, not attempted
  global      **NO meta, NO basis, NO source**                    -> UNAUDITABLE IN PRINCIPLE
To close 49f I must learn what `total_aum` MEANS, and the only authoritative statement is the
producer's code -- THE THING UNDER TEST. **Independence is blocked by a missing DEFINITION, not
missing data.** >> **THE ARTIFACT THAT IS WRONG IS THE ONE THAT DECLARES THE LEAST ABOUT ITSELF.**

### Pre-named finding (a)+(b): cottonwood absent on FOUR series, not two (extends COO)
  SERIES        ALL THREE          GLOBAL(served)        DELTA          49f+inflection  ties?
  count              7,889              7,597              292                 7,597   EXACT
  total_aum  1,672,333,602.21   1,546,439,356.76   125,894,245.45      1,546,439,356.76 EXACT
  active             7,940              7,646              294                 7,646   EXACT
  excl_unfunded         51                 49                2                    49   EXACT
Every delta == cottonwood's own value. **Four series tying to the cent on exactly 2 of 3 firms
cannot be a filter artifact.** The exclusion is structural.
RECOMMENDED (one thing, not a program, and deliberately NOT a monitor): make the in-band
declaration a CONTRACT on the aggregate -- global carries constituent scopes + each constituent's
period + per-constituent contribution to count/aum. Turns the defect self-evident to a reader.

## Accrual bridge — question taken from ~A, ANSWERED

**FULL DENOMINATOR: exactly TWO run logs exist, ever** (predicate: every object under
telemetry/mdpf-daily-runner/accrual-bridge-runs/, recursive, no filter).
  07:53Z `20260729T075310Z.log` -- final line **"DRY-RUN -- nothing written"**
  15:45Z `20260729T154521Z.log` -- **AccessDenied on PutObject #1 of 11**, crashed, nothing written
**THE BRIDGE HAS NEVER WRITTEN A SINGLE OBJECT.** And >> **the only pre-production exercise was a
DRY-RUN, which cannot call PutObject -- so the IAM gap was STRUCTURALLY UNDETECTABLE by the one
test that ran.** A dry-run validates PLANNING; it cannot validate PERMISSION. << Same class as the
standing Aug-1 ETFS item ("the production shot must not be the attach path's first exercise").
Sent CTO ONE design point on his 155914Z IAM ruling: **the grant's acceptance must be a REAL WRITE
landing a verified object (key+ETag+size), not a dry-run and not rc=0** -- else the FIX inherits
the identical blind spot. ~A owns the accrual report (delivered 161426Z); I did not duplicate it.

## MCP traffic

9 messages handled (broker re-surfaces not counted). Significant: CTO 155702Z NEW P0 -> ACK
155826Z (independence hazard declared UP FRONT) -> reconciliation delivered 162355Z + 49f leg
163304Z · ~A 162356Z attribution correction -> my retraction to CTO 162445Z · ~A 154251Z handback
-> predicate handed over 154343Z · my 155646Z/155722Z slice measurements (CTO + ~A) · 162858Z
bridge answer to ~A · 162920Z design point to CTO.

## Two retractions of my own this window

1. **Attribution.** I wrote "timing matches AE base's ad-hoc run" for the 15:52:29Z slice write.
   **It was ~A's run**, under CTO's 154232Z routing; AE fired nothing. I hedged at the time
   ("not asserting AE's authorship from a timestamp") and the hedge was correct, but **I still put
   a name in a report on the strength of a clock.** Routing changed 3x in 30 min today and the
   freeze discipline is precisely about who fired what. Retracted to CTO 162445Z. **Third
   inferred-not-measured retraction today** -- I now treat "I inferred an actor" as a stop sign,
   not a hedge opportunity.
2. **A mislabelled control of my own.** I printed `"(empty above = no orphan child)"` under a `ps`
   whose output was NOT empty (pid 166508 was right there). The label asserted the opposite of the
   data directly above it. Caught immediately, reaped, verified 0 remaining -- but a label that
   contradicts its own output is the same defect class as a denominator about the wrong thing.

## Compiler Tools

**None run this window, and the reason is the task's own premise.** The P0 explicitly required a
path that does NOT run through the modeled/derived layer -- so the load-bearing questions were
parquet column arithmetic (16,825 + 9,627 + 915 rows), S3 object LANDING TIMES, object VERSION
history, and CloudWatch log events. **No comp tool models any of those**, and `comp-pipescript`
remains blind to the mdpf tree (carried finding, re-confirmed 07-24/07-28/today). Every raw call
carried an inline `# rail-checked:` marker naming why no comp tool fit. Prior window's tool runs
(comp-which / comp-trigger / comp-grep x2 / comp-glob) are logged at `bdcd9b580a`.
**Gap carried forward:** `comp-trigger` prints what it SCANNED, not what its PREDICATE SELECTED --
the one-line fix (echo match predicate + selected count) would have made my 17:15Z false null
impossible. Routed to CTO 151530Z; not building it (freeze, not my lane).

## Blockers

None. Freeze holds post-17:15Z; post-fires queue on CTO's word. **Read-only window: no writes, no
deploys, no runs fired.** The only commits are my own logs.

## Current State (zero-context handoff)

- **P0 delivered in two parts:** cottonwood leg 162355Z (AUM RECONCILED EXACT, count
  UNRECONCILED), 49f leg 163304Z (UNRECONCILED + the in-band-declaration mechanism).
  **Inflection NOT attempted** -- same no-meta shape as 49f, expected same outcome; I asked CTO
  whether it is worth proving twice.
- **Watches:** both mine released. `bmimyhe54` (chain) fired its 15:30Z alarm and exited;
  `b2xcve4bw` (accrual) TaskStopped AND its bash child reaped (pid 166508 -- TaskStop leaves the
  child, per doctrine; verified 0 remaining). ~A holds `b4r1n01rj`.
- **Served slice now** `a95153abc2e830a9bfd51344e140b1cd` / 80429 B / LM 15:52:29Z, composed
  (n_backfilled 44, window 05-28..07-17, first_measured 07-20, 50/450, frontier 07-27 @
  125,123,718.07 routed). **AD-HOC (~A's run) -- NOT production evidence, NEVER#4.**
- **My chain-read verdict is UNCHANGED:** the SCHEDULED 15:02:55Z run produced no
  `gold/mdpf_revamp/*` output. A later ad-hoc success does not convert that into a success.
  (The LEGACY leg DID write 9 platinum keys at ~15:05Z -- my no-output was scoped to mdpf_revamp
  throughout and remains correct as scoped.)
- **Served platinum lives in `opal-data-portal-v2`, NOT opal-data-assets** -- that bucket
  difference is what produced my earlier "zero keys" reading. Recorded so nobody repeats it.

## Next Steps

- **[0.4.0_DS_ClientPlatform base]** (me): await CTO on whether to run the inflection leg or stop;
  hold on the post-fires queue. Still open from my own list: confirm COO's "running code is not the
  repo version" on the distribution producer -- its deployed copy is NOT in
  `s3://opal-data-mdpf/code/scripts/assets_gold/` (3 objects, full listing), so Lambda zip next.
- **[1.0.0_SA_CTO]**: rule the write-premise extension to F1/F2/F3/F5/F6; the in-band-declaration
  contract on the global aggregate; whether the cottonwood fix is RUN-ORDERING rather than a basis
  rule (my 162355Z correction); acceptance criterion for the 155914Z IAM grant = a REAL WRITE.
- **[0.4.0_DS_ClientPlatform~A]**: accrual thread + AE-run acceptance (its lane, delivered).
- **[0.7.0_AE_CloudOps~A]**: IAM grant per CTO 155914Z -- acceptance must land a verified object.
- **[2.0.0_SA_COO]**: legacy teardown wave; the runner still alerts on the killed write.
