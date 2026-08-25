# CTO~Z 08:45-09:00Z -- display-name architecture RULED, pipeline posture CONFIRMED, and three instrument failures of my own

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Seat:** `1.0.0_SA_CTO~Z` (site Z) | **Window:** relaunch ~08:45Z -> ~09:00Z
**Assignment:** Andrew-direct 2026-08-25 ~07:3xZ via `0.0.0_AB_MSTR~Z` spawn brief -- the display-name
ARCHITECTURE (Rule 17b serving tier) + confirm pipelines scheduled/robust. Fence: *"this and only this."*

---

## 1. WHAT I WAS ASKED, AND WHAT I DELIVERED

| ask | deliverable | state |
|---|---|---|
| name the display-name architectural home (Rule 17b) | `ctoZ_ETFS_DISPLAY_NAME_ARCHITECTURE_20260825.md` | `@e6e3ffa7d8` landed LOCAL, rides integration |
| confirm pipelines scheduled/robust | `ctoZ_ETFS_PIPELINE_SCHEDULED_ROBUST_CONFIRMATION_20260825.md` | `@e6e3ffa7d8`, amended `@1dbddf6fdb`, corrected `@a5614b385e` |

**RULING 1 -- THE HOME.** `data/etfs/scripts/gold/etf_positioning_publisher.py` (STAGE 2, platinum
publisher), single existing `name` shaping site `:234`, keyed by constituent ticker, **defaulting to
the incoming vendor string**. Gold keeps the issuer string. No new table, config object, IAM grant,
or monitor. **Not a new architectural decision** -- Rule 17b names display naming as platinum-tier
work and this product already had the two-stage split; it was the first naming question put to it.

**THE MEASUREMENT THAT KILLED THE TRANSFORM REMEDY.** On the live served bytes the two instruments
in the class fail by DIFFERENT mechanisms: `SALXX` = all-caps issuer style; `FXFXX` =
**already correctly title-cased, carrying a FABRICATED maturity date** (`01/01/2040`) on a fund that
has none. Title-casing gets SALXX wrong three ways and is a NO-OP on FXFXX. **You cannot transform
your way out of a fabricated substring.** One map, N mechanisms.

**RULING 2 -- POSTURE.** SCHEDULED: **yes**, and the defect CLAUDE.md names is absent BY
CONSTRUCTION (one invocation runs both stages; the handler docstring cites that rule as its reason).
`OPAL_ETFS_PUBLISH_GRANT=1` **applied**, re-verified POST-apply -- without it the scheduled fire runs
green and publishes nothing forever. ROBUST: **one exposure, not in AWS** -- leg 1 is a LOCAL WINDOWS
TASK on this workstation; box asleep -> no `bbg/{date}/` -> leg 3's guard SKIPS -> serves stale on a
green run, invisible from every AWS instrument. **Posture reported, NO monitor proposed** (07-28
moratorium).

**FOUR MORE RULINGS ROUTED TO ME AND MADE:** `da2fedda` PERFRP passenger **RIDES** · `PerfrpTable.tsx:29`
**STAYS** (self-reversed, below) · Andrew's condition (ii) vs his ~23:44Z word are **DIFFERENT AXES**,
no supersession · rung 2 is produced by **INVOKING THE DEPLOYED LAMBDA**, never a local run.

---

## 2. THREE INSTRUMENT FAILURES OF MY OWN, ALL CAUGHT BY A CONTROL OR A PEER

1. **`.get('KeyCount', 0)` read 0 for EVERY S3 prefix**, including a live one holding 7 objects --
   the CLI strips `KeyCount` when it auto-paginates. **The prefix I cared about was genuinely empty,
   so the answer was RIGHT for a reason that was BROKEN.** Only a positive control on a
   known-populated prefix exposed it. Banked to memory with the `len(Contents)` remedy.
2. **`'cron(0 11'` substring -> "ZERO rules at hour 11"** in a committed deliverable and a 7-seat
   broadcast. **TEN fire in hour 11.** A test for *"fires at exactly 11:00"* reported as *"fires in
   hour 11."* Falsified by `0.4.0_DS_ClientPlatform~Z` **before it reached Andrew**. On re-derivation
   I found **one more than they did** -- `access-anomaly-scanner-schedule` is `cron(0 * * * ? *)`, and
   **a wildcard hour field is invisible to a literal-hour matcher**, so even the narrow claim was
   false. Corrected `@a5614b385e` + same-turn broadcast.
3. **"every artifact to date is AD-HOC" -- true and TOO COARSE.** `2.0.0_SA_COO~Z` correlated object
   versions against invocations and showed the served artifact **was not produced by the Lambda at
   all**. I read CloudWatch LOG STREAMS (answers *"did the schedule fire"*); they read provenance.
   **A true statement at the wrong grain still terminates inquiry.** Amended `@1dbddf6fdb`.

**AND I REVERSED MY OWN RULING AFTER ~12 MINUTES.** I ordered `PerfrpTable.tsx:29` deleted to restore
DEV's dead typecheck. `2.0.0_SA_COO~Z`'s counter beat it (a third PERFRP change to a cut whose PERFRP
content is under sovereign question), and **my premise died anyway once both local typechecks became
mandatory**. I had argued from a gap without checking whether the gap was already covered --
`0.2.0_DT_PortfolioAnalytics~Z`'s own message named the covering control and I read past it.
`0.4.0_DE_ClientPlatform~Z` had already refused to execute the order, correctly.

---

## 3. WHAT I CAUGHT FOR OTHERS

- **COO~Z's path correction to DE~Z was a WRONG-PLANE error.** `portfolios[code].holdings[]` is right
  about the ARTIFACT and wrong about the COMPONENT'S PROPS: the adapter downgrades it to
  `{ticker, weight}` (`etfAdapter.ts:128-131`), and `sub_asset_class` exists only in `toCurrentHolding`
  (`:81`). It would not have thrown -- **187 rows, right length, `sub_asset_class === undefined` on
  every one**, rendering an empty panel that reads as a failed fix. COO re-verified at source and
  retracted.
- **Stopped a rollback of a healthy promote.** MSTR~Z ran a ~10-min deadline on the 100x scale hazard.
  I recomputed the percentages from the artifact against DE's rendered DOM: **16 of 16 cells exact**;
  a fraction-scale page would read `0.0684`, it reads `6.84`. Sound risk argument, premise already
  falsified.
- **Narrowed MSTR~Z's render hold from three questions to one.** Their *"14 messages, ZERO render
  evidence"* was false -- DE had delivered a render at 08:22:59Z answering (1) and (2) with numbers.
  **But the hold survived on (3) for a reason nobody had stated: DE rendered 8m07s BEFORE the name fix
  published.** Their page could not have shown the new string. **A clock, not an omission.**
- **The IDVZ 2.69% panel gap**, root-caused: ICT/MER/2602335D carry ZERO Bloomberg characteristics
  (positive control ISNPY has all three), so the classifier is correct on absent input. **The
  ETFS_INGEST PRD's own predicted failure arriving.** Filed, not fixed.
- **Corrected DT~Z's `3.18` to `2.69`** before it reached Andrew -- the other `0.49` is the ISSUER's
  book not summing to 100, and fusing them over-states our defect and invites forcing a book to 100.
- **Pre-empted a false alarm at 13:00Z:** corrected COO's check (d). **`data_as_of` STAYING at
  `2026-08-24` is the PASS**, because silver 08-25 lands at 22:00Z. As worded it would have reported
  a defect on a healthy first fire. Same class as `99.51 is the pass mark for IDVZ, not 100`.

---

## 4. VALIDATION I PERFORMED (RAVC step 4 -- evidence, not reports)

| claim | my instrument | result |
|---|---|---|
| 2a deploy landed | `get-function-configuration`, baseline = a sha **I** recorded pre-deploy | `631ELit...` -> `p/mc7hvS...` @08:19:03Z; **grant still `1` post-apply** |
| rung 2 (Defect B on the serve) | full-record diff of all 187 rows vs my own pre-change copy | **4 rows, ONE field (`name`), 183 identical, key set identical, `data_as_of` unmoved** |
| the push | `ls-remote` (the remote, not a local ref) + content at the ref | `origin/PROD` = `a7a7ff16`; `current_holdings` **0 -> 3**, file lines 1267/1301 so neither `git show` failed silently |
| passenger set | `origin/PROD..origin/DEV` | 5 commits / 5 files / 157 ins -- **exactly what I ruled**; `PerfrpTable.tsx` diff **EMPTY**, my reversal held on the wire |

---

## 5. Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find -i` | `'etf.classification'`, `'SALXX'`, `'FXFXX'` | PASS | 847 / 26,447 files; 219 / 26,447; 132 / 26,447. **`-i` per Rule 21** -- a case-sensitive census would have dropped the emphatic lines. Band filtering (`--band DEF/SURFACED/CONFIG`) separated source hits from 182 doc hits in one call. |
| `comp-find` (bands) | `--band HEAD/DEF/SURFACED/CONFIG` | PASS | The band split is what made a 219-hit census readable; without it the doc noise buries the one `_CASH_TICKERS = {"SALXX"}` definition. |

**What worked:** `comp-find -i` with band filtering answered the whole "is SALXX already in an
existing map" question in two calls, with printed denominators, and its SYSTEMS-CONTEXT footer
pointed me at the two `_shared/` Lambda files that turned out to be the crux.
**What failed:** nothing in the comp layer. **Every failure this session was in raw tooling I reached
for where no comp-tool fits** (`s3api` counts, `aws events` cron parsing, `git show`/`grep -c`
chaining) -- which is itself the argument for the rail.
**Gap found:** **no comp-tool answers "did this schedule ever fire, and what made these bytes."**
`comp-freshness` reads artifact age, `comp-aws` reads config; neither answers provenance. I marked
the Lambda-invocation-history read `# rail-checked:` accordingly. **A `comp-provenance`-shaped gap is
a real coverage hole** (CLAUDE.md: a comp-tool coverage gap is a DEFECT, not an inconvenience) --
surfaced here, not proposed as a build under the fence.

---

## 6. Blockers

**None at this seat.** Nothing is waiting on me. Every remaining item has a named owner:
rung 3 + the deploy ledger (`0.2.0_DT_PortfolioAnalytics~Z`), the 11:00Z universe check and the
13:00Z first-ever scheduled fire (`0.7.0_AE_CloudOps~Z`, owner ratified this window; **TO to be cut
by `2.0.0_SA_COO~Z` as the PRIMARY carrier** -- `to-check.py --all` is what a successor actually runs
at startup, a deliverable section is queried by nobody).

**At Andrew (not mine to close):** the DIVZ/IDVZ `Polen` vs `Opal` fund-name divergence -- two serving
surfaces, two client-facing names, one fund. `0.0.0_AB_MSTR~Z` escalated it directly. **Nobody
touches it without his word.**

---

## 7. Current State (for a reader with ZERO prior context)

- **Both defects are LIVE and verified.** Defect B (names) shipped by **Lambda apply 08:19:03Z** and
  needed no bundle; Defect A (sub-categories panel) shipped by **portal promote, `origin/PROD` =
  `a7a7ff16`**. **Two defects, two vehicles** -- a held promote never blocked Defect B.
- **Served artifact:** `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`, 126,809 B,
  `generated_at 2026-08-25T08:31:05Z`, `data_as_of 2026-08-24`, 187 rows / 4 books / 13
  `sub_asset_class` values. `SALXX -> "State Street U.S. Government MMKT"` (x2),
  `FXFXX -> "First American Treasury Obligations Fund"` (x2).
- **Producer:** `etf-positioning-producer`, CodeSha `p/mc7hvS...`, 2 package members (NOT 4 --
  `build_package.py` would shadow the trading-calendar layer; **ruled: do not use it**),
  `cron(0 13 * * ? *)` ENABLED, **never yet fired on schedule**.
- **My deliverables:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_ETFS_DISPLAY_NAME_ARCHITECTURE_20260825.md`
  and `..._PIPELINE_SCHEDULED_ROBUST_CONFIRMATION_20260825.md`. **Landed LOCAL @e6e3ffa7d8 /
  @1dbddf6fdb / @a5614b385e -- rides integration, NOT pushed** (LD-0367).
- **Loop state: ZERO crons armed.** I did **NOT** re-arm `/self-drive D4` -- Andrew's later, narrower
  07:3xZ word binds under `latest + most-restrictive`. **I did NOT strike the XXX.md CTO row** (a lane
  does not strike a sovereign-authored clause; the COO~Z precedent); I declined to arm under it and
  surfaced the conflict to `0.0.0_AB_MSTR~Z`.

---

## 8. Next Steps

- **[0.2.0_DT_PortfolioAnalytics~Z]** rung 3 -- re-render LIVE production after CI propagates; their
  ~08:35Z render was pre-push and they have not claimed it. **Close the deploy ledger** -- NEVER#6 is
  discharged by the closed ledger, not by a green CI.
- **[0.7.0_AE_CloudOps~Z]** the 11:00Z universe read (**if it covers ICT/MER, IDVZ goes 96.82 ->
  99.51, NOT 100**) and the 13:00Z first-ever scheduled fire, against the six corrected pass criteria.
- **[2.0.0_SA_COO~Z]** cut the 13:00Z TO as the primary durable carrier; scope Z-S48 forward.
- **[3.0.0_SA_CVO~Z]** decide whether the eight-instrument-failure pattern becomes a record. **Eight
  failures / five seats / ~90 minutes, sharing ONE property: not one of them ERRORED** -- every one
  returned a well-formed, plausible, confident value. **Zero reached Andrew, zero reached production.
  The controls held; carefulness did not do it.**
- **[Andrew]** the `Polen`/`Opal` fund-name divergence; FXFXX's target string is **DERIVED by DS~Z,
  not his ruling**, and awaits his confirm.

-- `1.0.0_SA_CTO~Z`
