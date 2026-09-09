# NFRA_REPORT -- one morning read you can trust, across three properties

*Registered 2026-09-09 under `D12` on Andrew-direct at the `1.0.0_SA_CTO~Z` terminal, VERBATIM:
**"NFRA_REPORT sits in D12"**. Proposed at L2 as `NFRA_INFRAREP` and renamed by him before
registration (**"let's brand this as NFRA_REPORT"**); that code was never registered and leaves no
citations behind.*

**Directive:** D12 Platform Operations · **Fabric:** site-z · **dep_stage:** PRD
**L1 owner:** `4.0.0_SA_CRO~Z` · **L2-L4 owner + author:** `1.0.0_SA_CTO~Z` · **L5-L6:** `2.0.0_SA_COO~ZZ` · **L8-L10:** `3.0.0_SA_CVO~Z` · **Integrator:** `0.0.0_AB_MSTR~Z`
**Brief (L1):** `docs/briefs/global-infrastructure-reporting-brief-20260909.md` @`37ff80867a`
**Endpoint (L2):** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_GLOBAL_INFRA_REPORTING_20260909.md`
**Version:** v0.2, 2026-09-09 ~19:0xZ -- **v0.2 ADDS THE SURFACE MANIFEST (section 8), WHICH v0.1 OMITTED.** Andrew asked whether the PRD carried one and 2.0.0_SA_COO~ZZ filed the same gap at msg 20590 as an L5 blocker-in-waiting. BOTH WERE RIGHT, and the census settles it: across 205 tracked *_PRD.md, seven carry a manifest, and of the SIX tree-home L4-spine PRDs FIVE do -- NFRA_CLDGRPH (28 rows), NFRA_OPSEC202609 (28), ETFS_GUARDRAIL (12), NFRA_COMPEFFICACY, NFRA_OUTSET -- with NFRA_REPORT the SOLE omission. That resolves msg 20590's fork in favour of reading (A): the manifest is an L4 DELIVERABLE, rule 27 makes L4 the CTO's alone, and the owned-paths gate independently refuses 2.0.0_SA_COO_ZZ on prd/**. Section 2 OWNS is ENUMERATED to twelve items in the same version, because a domain written as one prose sentence cannot have a MECE check RUN against it and rule 24(i) requires hunting the uncovered member -- that lane raised this too. Before it, **v0.1 = L4 MINT. The ENDPOINT below is RATIFIED IN FULL.** Ten bars
confirmed by Andrew's (b)/(c)/(d) on the L2 read; the remaining two -- `FWD-1`'s declarative re-cut
and `FWD-12` -- confirmed by his **"go with your recs on those two."** `FWD-12`'s bar was TIGHTENED
before landing (see its `CONFIRMED` line).
**archetype:** SCRIBE (spec)

```json
{
  "project": "NFRA_REPORT",
  "directive": "D12",
  "fabric": "site-z",
  "prd_version": "v0.1",
  "step": 4,
  "brief_ref": "docs/briefs/global-infrastructure-reporting-brief-20260909.md@37ff80867a",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10",
    "FWD-11",
    "FWD-12"
  ],
  "status": "RATIFIED"
}
```
*PRD_HEADER block (`org/standards/PRD_HEADER.schema.json`; limb 5 of `.tools/to-pipeline-gate.py`).
`status: RATIFIED` because EVERY outcome's `DONE WHEN` was confirmed by Andrew -- ten on the L2 read
and two on his "go with your recs". L5 may begin on this header.*

**Commissioning (Andrew-direct 2026-09-09, opening the review, VERBATIM):** *"which of course is
alarming, although I suspect merely a miscalibration... ultimately this should become a
/brief-create subject of having a proper infrastructure report, culminating in a daily morning
review. It has been miscalibrated for a long time and it's time that we fixed that."*

---

## ENDPOINT (step 2, /endpoint --forward)

*Phase 0 output. `FWD-n` ids are PERMANENT and never reused; a retired outcome leaves its number
vacant. `DONE WHEN` is the BAR, not the current state. ACCEPT lines are plain English and disputable,
by rule, and carry no technical language.*

```
  FWD-1  One morning read DECLARES whether anything needs Andrew today
         DONE WHEN  EXERCISED -- it has run on real trading mornings and its verdict
                    has been checked against the underlying rows and found right,
                    INCLUDING at least one morning where the verdict was "nothing"
         ACCEPT     On a trading morning the report states plainly whether anything
                    needs Andrew, and that statement can be checked against the rows
                    beneath it by anyone. A day when nothing needs him says so, and
                    does not look like a day when something does.

  FWD-2  Any reader can tell "nobody looked" apart from "we looked, and it is broken"
         DONE WHEN  APPLIED -- the distinction is in the report's own vocabulary and
                    a reader does not need to know how the report is built to see it
         ACCEPT     Someone who knows nothing about how this is put together can look
                    at any line and tell "we have no way of seeing this" from "we
                    looked, and here is how bad it is". Not being able to see
                    something never looks like seeing something wrong -- and
                    something wrong never looks like something catastrophic.

  FWD-3  A reader sees what changed since the last edition, on every row
         DONE WHEN  EXERCISED -- a reader has used it to tell a new problem from one
                    that has been standing for weeks
         ACCEPT     On each line a reader can see whether it is worse, better or
                    unchanged since the last one they read. Something that broke
                    overnight does not look the same as something that has been
                    wrong for a month, and a number that has not moved says so.

  FWD-4  A reader can tell which part of the business a problem belongs to, and who owns it
         DONE WHEN  EXERCISED -- a real failure has been read and attributed by a
                    person to one part and one owner
         ACCEPT     Every problem belongs to one of the three parts of the business
                    and names who would fix it. When one thing breaks it is mentioned
                    once, not once for every tool that happened to notice it.

  FWD-5  A person can tell whether an alert would reach a human, before an incident tests it
         DONE WHEN  EXERCISED -- at least one alert that would reach nobody has been
                    identified from the report, before any incident tested it
         ACCEPT     For any alarm we rely on, a person can tell whether a message
                    would actually arrive at a human being. One that would reach
                    nobody is shown as reaching nobody, and is never counted as
                    protection.

  FWD-6  A person can tell a broken thing from a deliberately retired one, without guessing
         DONE WHEN  EXERCISED -- one stale thing has been correctly called retired
                    and one correctly called broken, each on evidence rather than age
         ACCEPT     For anything that has stopped updating, a reader learns whether
                    anyone still relies on it. Being old raises the question and never
                    settles it, and "old" is never quietly treated as "dead".

  FWD-7  Someone can retire a dead thing and have the report stop raising it, on the record
         DONE WHEN  EXERCISED -- something has actually been retired and the next
                    edition stopped raising it
         ACCEPT     Someone can retire a dead thing, say why, put their name to it,
                    and stop seeing it every morning -- and anyone can later look up
                    what was retired, by whom, and for what reason.

  FWD-8  A person can see a cost movement that matters and ignore one that does not
         DONE WHEN  EXERCISED -- one real movement has been SURFACED, and ordinary
                    variation over the same window did NOT surface
         ACCEPT     A meaningful jump in what something costs shows up. Normal
                    week-to-week wobble does not. A reader can tell which is which
                    without doing the arithmetic themselves.

  FWD-9  Anyone can answer "what compute do we run, and what shuts itself down" from one place
         DONE WHEN  APPLIED -- one record covers both kinds of compute and states each
                    unit's duty cycle
         ACCEPT     Anyone can look in one place and see everything we run, whether
                    each thing turns itself off when idle, and which things are meant
                    to run all the time. Something nobody has recorded looks different
                    from something recorded as having none.

  FWD-10 A reader can trust that a number covers what it claims to cover
         DONE WHEN  APPLIED -- every count in the report carries what it counted out of
         ACCEPT     Every count says what it counted out of. Something barely watched
                    cannot produce a score that looks as healthy as something watched
                    thoroughly.

  FWD-11 A reader can tell what we publish that nothing is watching at all
         DONE WHEN  EXERCISED -- at least one thing we serve has been found that no
                    instrument covers
         ACCEPT     Someone can find the things we put in front of people that nobody
                    is checking at all. A part of the business with nothing watching
                    it looks different from one that is watched and healthy.

  FWD-12 When something looks wrong, the report shows what it is connected to and
         says what appears to be going on
         DONE WHEN  EXERCISED -- a real anomaly has produced a breakdown whose named
                    connections were CHECKED and found correct, and a written account
                    that asserts nothing the breakdown does not support
         ACCEPT     When something looks wrong, a reader sees what it is connected to
                    -- what feeds it, what reads it, what else would be affected --
                    and a few sentences on what appears to be happening. Nobody has
                    to go and assemble that picture themselves before they can judge
                    it.
```

**PROVENANCE:** `FWD-1`..`FWD-10` are the brief's `O1`..`O10`. **`FWD-11` was ADDED at L2** against
the brief's Part II *Owns* line -- monitored-vs-served reconciliation, *"the standing check that no
existing instrument performs"* -- which no numbered outcome covered and which would otherwise have
been owned and never graded. **`FWD-12` was ADDED on Andrew's word** 2026-09-09.

---

## 1. Purpose -- what DONE means

A named person opens one artifact on a trading morning and learns whether anything needs them, and
can believe it -- because every row says whether anyone looked, how bad it is if they did, what
changed since last time, whose it is, and what the number counted out of. When something is wrong,
the report shows what it touches and says what appears to be happening, without a generated sentence
ever standing in for a measured one.

## 2. Territory -- what this owns, and what it only relies on

**Owns (ENUMERATED for postulate (i) -- twelve items).** ⛔ **The enumeration is the point, not the
prose.** Rule 24(i) requires hunting the UNCOVERED member, and a domain written as one sentence
cannot be run against; `2.0.0_SA_COO~ZZ` raised exactly this at msg 20590 and was right.
**(1)** the report's STATE MODEL -- the two-axis vocabulary itself · **(2)** the report ARTIFACT's
row STRUCTURE, including the per-row delta · **(3)** its SCHEDULE and DELIVERY · **(4)** its
VERDICT -- the does-anything-need-Andrew determination · **(5)** the COMPUTE MANIFEST as a reporting
substrate (EC2 **and** ECS), its schema fix and its backfill · **(6)** the ALERT-DELIVERY read ·
**(7)** the DEPRECATION determination -- the consumer walk to the client-facing terminus ·
**(8)** SUPPRESSION / RETIREMENT as recorded state, with owner and reason · **(9)** the COST-ANOMALY
detector · **(10)** the COVERAGE / DENOMINATOR discipline carried on every count ·
**(11)** MONITORED-vs-SERVED reconciliation · **(12)** the ANOMALY BREAKDOWN and its written account.

**Relies on, does not own:**

| Surface | Owner |
|---|---|
| Detection of suspicious activity; the sentinel, address table, evidence store, WAF/IP sets | `NFRA_OPSEC202609` |
| Portal MFA enforcement | `D12_PLATFORM_OPS` |
| The IAM least-privilege posture it reports on | `NFRA_IAMROLES202609` |
| The gold/silver producers whose artifacts are reported on | the DS/AE pipeline lanes |
| Terraform module correctness | the owning infra lanes |
| The marketing site's DNS at GoDaddy | outside AWS entirely |

**Explicitly NOT re-opened:** the standing moratorium on new alerts/alarms/monitors -- **this project
REPAIRS existing egress and REPORTS; it does not mint alerting**. `NFRA_OPSEC202609`'s nineteen
outcomes are consumed here, never amended. Retiring served output still needs never-widen sign-off
(CTO+COO): this project **classifies**, it does not delete on its own authority.

## 3. Acceptance properties

1. Andrew reads it every morning and does not learn to skip it.
2. A row that says OK has been looked at.
3. One failure reads as one item.
4. A number can be trusted at the grain it is stated.
5. The report tells you what it cannot see.
6. A control that cannot fire is not counted as protection.

## 4. Out of scope

- Minting any new alert, alarm, monitor or notification. The standing moratorium holds entire.
- Amending `NFRA_OPSEC202609`'s outcomes, or re-running its four narrow least-privilege cells.
- Deleting or narrowing anything that serves live production without the estate's normal sign-off.
- Repairing the marketing site's edge. **`NFRA_OPSEC202609` C-19 establishes there is no AWS-only
  route**, and Andrew has ruled *"we do whatever we can without having to engage with GoDaddy."*

## 5. Constraints that BIND the decomposition

**`C-AI` -- WHERE AI ANALYSIS IS APPLIED, AND WHERE IT IS NOT.** Andrew-direct 2026-09-09: *"a clear
strategy for where AI analysis is applied, whether for summary generation and for nuanced description
of anomalous patterns."*
⛔ **LOAD-BEARING, NOT HOUSEKEEPING: a generated sentence beside a computed number will be read as a
measurement.** This project's premise is that instrument state and world state never share a colour
(`FWD-2`) and every count carries its denominator (`FWD-10`). An unlabelled model narrative
re-introduces that exact defect one layer up, in the most persuasive register available.
1. **DECLARED PER REGION** -- every part is COMPUTED, GENERATED or QUOTED, legible without knowing
   how the report is built.
2. **A GENERATED PART IS NEVER THE SOLE CARRIER OF A FACT.** `FWD-12`'s breakdown is COMPUTED; the
   analysis beside it is GENERATED and is a reading OF that evidence. **Strip every generated
   sentence and the report must still be true and still checkable.**
3. **A VERDICT IS COMPUTED, NEVER GENERATED.** A model may render `FWD-1`'s verdict in better
   English; it may not decide it.
   *Reuse the estate's existing a-value-carries-its-claim discipline rather than minting a second
   vocabulary -- the consuming half is the whole mechanism.*
> binds `FWD-1`, `FWD-12` · violated by: an unlabelled generated region; a fact that disappears when
> generated prose is stripped; a model deciding a verdict

**`C-FWD2-FIRST` -- `FWD-2` IS THE CRITICAL PATH.** Until the vocabulary exists, the report cannot
honestly render ANY `NFRA_OPSEC202609` surface: every gap becomes a false OK or a false alarm.
> binds `FWD-2` · violated by: rendering a security row before the vocabulary can express BLIND,
> DEGRADED, and DESIRED-not-APPLIED

**`C-WEBSITE-BLIND` -- the Website security row is settled PERMANENTLY, not pending.**
`NFRA_OPSEC202609` C-19: `opalinvest.com` and `www` resolve to the EC2 elastic IP, no CloudFront;
AWS WAF cannot attach to a bare EC2; every candidate edge needs a GoDaddy record change. **That row
renders BLIND with its reason attached FOREVER and does NOT wait on `TO-OP-S-13`.**
> binds `FWD-2`, `FWD-4` · violated by: rendering Website as a gap awaiting a fix

**`C-SENTINEL-STATE` -- a BLOCKED address is DESIRED, never APPLIED.** `TO-OP-S-14-21` is complete
and the sentinel runs watch-only; its reconciler `TO-OP-S-15-19` is staged. **A report rendering
that table without saying so reports INTENT AS FACT.**
> binds `FWD-2` · violated by: presenting the address table as applied state

**`C-TRADING-DAYS` -- delivery lands on TRADING DAYS ONLY, before Andrew's morning.** The current
report fires weekdays including market holidays; it sent on Labor Day.
> binds `FWD-1` · violated by: a calendar-day schedule

**`C-COST-15` -- Andrew's detector, verbatim:** *"whether there is a material divergence from
historical cost for a given compute box or cost segment... if something moves say 15% or more from
its trailing 30 day price."*
> binds `FWD-8`

**`C-DEPRECATED-TERMINUS` -- deprecated = ZERO consumers AT THE CLIENT-FACING TERMINUS**, established
by walking the chain to a served artifact and a rendered component -- never the first `scripts:`
field, never age.
> binds `FWD-6`, `FWD-7` · violated by: a one-hop consumer check

**`C-ALARM-ANCHORED` -- `FWD-5`'s check is anchored on the ALARM and reads CONFIRMED delivery**, never
"subscribed" and never the alarm's own configuration.
> binds `FWD-5` · violated by: grading delivery from an alarm's configuration

## 6. Rulings that BIND

- **2026-09-09, Andrew-direct:** the three properties are **Dashboard** (the entire serverless system
  feeding opalinvest.dev), **Website**, **Gateway** (the opal-gateway MCP server).
- **2026-09-09, Andrew-direct:** GREEN = every property CHECKED and OK; the two-axis state model;
  decommissioning is a FUNCTION of this work; the always-on set is named by group.
- **2026-09-09, Andrew-direct (clause a):** the morning read is **purely declarative**. *"I can elect
  to remediate issues or not at my discretion, separate from the greater flow."* **No outcome in
  this PRD requires Andrew, or anyone, to ACT.**
- **2026-09-09, Andrew-direct:** *"process the infra report brief first"* -- ordering against
  `NFRA_IAMROLES202609`, discharged at L2.
- **2026-09-09, CTO ruling at L4:** `FWD-8`'s bar lost its "acted on or consciously dismissed"
  clause on the clause-(a) principle, applied to an outcome Andrew did not enumerate and **flagged
  as reversible in one word**.

## 7. Sequencing input for `2.0.0_SA_COO~ZZ` (not a dispatch)

**`FWD-2` FIRST.** It is the critical path into the whole `NFRA_OPSEC202609` relationship and three
constraints hang off it.
**Then `FWD-9` / `FWD-10`** -- the compute manifest and the coverage discipline; both are APPLIED
bars and neither touches OPSEC.
**`FWD-11` and `FWD-12` want the dependency graph.** ⚠ **BUILD-LADDER RUNG 2 BEFORE ANY CELL:** the
connected-things half of `FWD-12` is very likely a QUERY, not a build -- the estate holds a
dependency graph with a call manifest and CLAUDE.md rule 20 says QUERY IT, NEVER REBUILD, and a
blast-radius surface exists.
⭐ **The shared blocked instrument is FIXED and no longer a dependency:** `comp-find --corpus aws`
was repaired at `9b99b49342` (TWO broken callers, both dropping a `--mode` argument `kuzu_cli.py` no
longer accepts) and exercised end-to-end -- 757 hits across 2157 AWS nodes. ⚠ **One residual: it
prints `VINTAGE: UNREAD`.** Rows come back and their age does not, which is a denominator without a
vintage. **Unowned, and it bears directly on `FWD-10`.**

**ZERO of the twelve outcomes are BLOCKED by `NFRA_OPSEC202609`.** That project is a CONTENT
dependency on three security rows, never a structural one on this report. OPSEC completion is a
QUALITY gate on those rows, not a LAUNCH gate on the project.
---

## 8. SURFACE MANIFEST (step 4 -> step 5) -- one row per ENGINE

**Contract** (as adopted @`ecaa7c7dcb`, ETFS_GUARDRAIL s.7, and used by `NFRA_OPSEC202609` s.8):
`claim` is about the SURFACE ADDRESS and takes the five-value basis vocabulary
`absent | unmeasured | held | inferred | measured` (`.tools/substrate-card-check.py` `BASIS_RANK`;
every legal transition is a rank increase, and `verify` is the act that moves `absent`/`unmeasured`);
`verb` is the contract enum `port | classify | wire | align | retire | verify`; `outcome` = `FWD-n`;
`accept` = the section 3 acceptance-property number; `depends_on` = row ids; `bound` = the constraint
the cell may not cross.

**Provenance, read before citing any cell.** Every `measured` evidence cell is the L1 BRIEF's
measurement at `@37ff80867a` (`4.0.0_SA_CRO~Z`, 2026-09-09) unless it names another seat. **Nothing
in this table was re-measured at L4**; the brief's `F<n>` ids are cited so `2.0.0_SA_COO~ZZ`'s L5
battery re-grounds each cell at its own vintage. `absent` rows are outcomes with nothing built.

**Domain (postulate i):** the section 2 **OWNS** cell, TWELVE enumerated items. **MECE is RUN below,
not asserted.**

| id | outcome | surface (engine) | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S1 | FWD-2, FWD-4 | The report's STATE MODEL -- the two-axis vocabulary (instrument axis CHECKED vs BLIND; world axis OK / DEGRADED / BREACH) and the property+owner attribution riding it | absent | brief F6 (the vocabulary already exists in two places, unratified as the report's law); Andrew-direct 2026-09-09 ratified the two-axis model and the three properties | report lane | wire | -- | 2, 3 | `C-FWD2-FIRST`; `C-WEBSITE-BLIND` -- it MUST express a PERMANENT blind, not only a not-yet; `C-SENTINEL-STATE` -- and a DESIRED-not-APPLIED row |
| S2 | FWD-3, FWD-1 | The report ARTIFACT's row structure and its PER-ROW DELTA against the previous edition | absent | brief F1: the rollup is a `max()` over eight rows and the subject line read the same value on every instance in the window -- a signal that never changes | report lane | wire | S1 | 1, 3 | a delta computed per ROW, never only on the total; `C-AI` -- the delta is COMPUTED |
| S3 | FWD-1 | The report's SCHEDULE and DELIVERY -- trading days only, before Andrew's morning | measured | brief F2: the detectors are weekday-aware and NOT trading-day-aware; **it sent on Labor Day 2026-09-07** | report lane | align | S2 | 1 | `C-TRADING-DAYS`; `lib/trading_calendar.py` is the ONE frontier (CLAUDE.md NEVER#4) -- never a calendar-day subtraction |
| S4 | FWD-1 | The VERDICT rule -- the does-anything-need-Andrew determination, derived from the rows | absent | brief F1 (the current signal cannot vary); FWD-1's own bar requires at least one correct NOTHING morning | report lane | wire | S1, S2 | 1 | `C-AI` part 3 -- **A VERDICT IS COMPUTED, NEVER GENERATED.** A model may render it, not decide it |
| S5 | FWD-9 | The COMPUTE MANIFEST as reporting substrate -- EC2 **and ECS**, each unit's duty cycle, autoshutdown state, the always-on set by group | measured | brief F8: 27 declared services, 18 of 27 rows carry a lifecycle word where a machine type belongs, two services share an id, **and the manifest is EC2-ONLY -- ECS absent entirely**; the manifest is itself 2014.2h old | infra lane | port | -- | 4 | `D3` -- per-box cost anomaly (S9) CANNOT be computed until this lands; segment grain is available now. Reuse `sync-ec2-manifest.sh`, do not re-buy it |
| S6 | FWD-5 | The ALERT-DELIVERY read -- alarm-anchored, resolving alarm -> topic -> CONFIRMED subscriber | measured | brief F4; and `1.0.0_SA_CTO~Z` 2026-09-09 live, row `NFRA_OPSEC202609-Z-S151`: **3 of 7 distinct alarm targets have ZERO confirmed subscribers** (`opal-login-abuse-alerts`, `astn-wsjft-alerts`, `etfs-reports-alerts`), positive-controlled by the 4 that do | report lane | wire | S1 | 6 | `C-ALARM-ANCHORED` -- CONFIRMED delivery, never "subscribed", never the alarm's own configuration. **A pending subscription delivers nothing** |
| S7 | FWD-6 | The DEPRECATION determination -- the consumer walk from a stale artifact to a client-facing terminus | absent | brief F7 (monitors outlive migrations and nothing detects it); Andrew-direct ruling 9 supplies the criterion and its grain | report lane | wire | S1 | 2 | `C-DEPRECATED-TERMINUS` -- zero consumers AT THE TERMINUS by walking the chain; **never the first `scripts:` field, never age** |
| S8 | FWD-7 | The RETIREMENT REGISTER -- suppression/deprecation as recorded state with owner, reason and date | absent | brief F10: 216 security findings are all configuration properties and **no suppression state exists, so the same items are re-reasoned daily** | report lane | wire | S7 | 2 | never-widen sign-off (CTO+COO) still governs RETIRING SERVED OUTPUT -- this project CLASSIFIES, it does not delete |
| S9 | FWD-8 | The COST-ANOMALY detector -- material divergence from a segment's or a box's own trailing history | measured | brief F9: cost has no standard so it cannot fail; **`(untagged)` is $154.21, 45% of spend and the largest single line** | report lane | wire | S5 | 4 | `C-COST-15` (Andrew's 15% / trailing-30-day detector, verbatim). **BOX grain is blocked on S5; SEGMENT grain is available now** |
| S10 | FWD-10 | The COVERAGE / DENOMINATOR carrier -- every count states what it counted out of | absent | brief F3: coverage, not staleness, is the freshness story (`mdpf 0/1`); brief F5: the drift section colours on INSTRUMENT freshness rather than on drift | report lane | wire | S1 | 4, 5 | a thinly-monitored surface must not produce a score that reads as healthy as a thoroughly-monitored one |
| S11 | FWD-11 | The MONITORED-vs-SERVED reconciler -- what we publish that no instrument covers | absent | brief Part II Owns, verbatim: *"the standing check that NO EXISTING INSTRUMENT PERFORMS"* | report lane | wire | S10 | 5 | the live-plane enumerator is `comp-find --corpus aws`, **REPAIRED 2026-09-09 and re-exercised at the merged head: 757 hits / 2157 nodes, VINTAGE now carried.** No longer a blocked dependency |
| S12 | FWD-12 | The ANOMALY BREAKDOWN -- connected resources/consumers/generators for an anomalous row -- plus its written account | absent | Andrew-direct 2026-09-09 (the outcome's SOURCE line) | report lane | wire | S1, S11 | 3, 5 | `C-AI` parts 1+2 -- the breakdown is COMPUTED, the account is GENERATED and **may never be the sole carrier of a fact**. **BUILD-LADDER RUNG 2 FIRST:** the graph and its call manifest exist; CLAUDE.md rule 20 says QUERY, NEVER REBUILD |

**MECE, BOTH DIRECTIONS, RUN RATHER THAN ASSERTED (at this edit):**
- **FORWARD -- every OWNS item has at least one row:** (1)->S1 · (2)->S2 · (3)->S3 · (4)->S4 ·
  (5)->S5 · (6)->S6 · (7)->S7 · (8)->S8 · (9)->S9 · (10)->S10 · (11)->S11 · (12)->S12.
  **12 of 12 covered, 0 uncovered.**
- **BACKWARD -- every row maps to an OWNS item and to at least one outcome:** 12 rows, 0 orphans.
- **OUTCOME COVERAGE:** `FWD-1` is served by S2/S3/S4, `FWD-2` and `FWD-4` by S1, every other outcome
  by exactly one row. **12 of 12 outcomes carried, 0 uncovered.**

⚠ **THE 12-AND-12 IS A MEASUREMENT AT THIS EDIT, NOT AN INVARIANT, AND IT IS DELIBERATELY NOT
DECLARED AS ONE.** `NFRA_OPSEC202609` asserted an `OP-s-<n>` IS `S<n>` bijection in a heading and it
went FALSE with nothing able to fail -- prose cannot fail. **A surface needing two acts across rounds
is normal, not an exception**, so a later cell mirroring S1 twice, or a row acquiring a second cell,
breaks nothing here. What L5 must preserve is COVERAGE IN BOTH DIRECTIONS, never the one-to-one.

**What this manifest does NOT assert:** that every row is buildable as written -- `S5`'s ECS half and
`S9`'s box grain are coupled and `D3` says so; that the `lane` column is a seat assignment (it is a
lane; `2.0.0_SA_COO~ZZ` seats workers at L6); or that `absent` means unexamined -- every `absent` row
names what was measured about the CURRENT state's failure to serve it.
