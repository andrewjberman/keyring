# ETFS rebate-basis: emergency-rollback defect -> July lineage audit -> three-producer repoint (1330-2300Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, VALIDATE, COORDINATE

Started as "a colleague ran emergency rollback and it didn't work." Ended at a three-producer
architectural repoint onto the monolith. The thread stayed on one artifact class the whole way: the
**ETFS_AVGCAP partner-rebate basis** — the numbers that decide what a partner is paid.

## What landed

| commit | what |
|---|---|
| `27209335f3` | merge exemption on mstr-ledger + branch-isolation (CTO review of MSTR's emergency edit, exercised 4/4) |
| `f3aba0895b` | OWNED/HELD: the pre-commit installer is WRITE-ONCE |
| `b5c3618ba6` | MEMORY.md pre-cleanup snapshot into the repo (memory dir is NOT git) |
| `890924ce5b` · `d9e827e267` | `docs/doctrine/VERIFICATION_LAW.md` — 13 laws relocated out of the memory cap, +law 14 |
| `7c489c7b3c` | deploy ledger: roll-forward to the 2026-07-27 vintage + the CDN invalidation the Lambda cannot do |
| `f1ba015d21` | spec: DATAREFRESH_ROLLBACK_INVALIDATION_FIX |
| `5c6031ec7a` · `23681477f8` · `da9a83cd31` | spec: INF_ETF_OWNERSHIP_SCHEDULED_FLOOR + Andrew reversal + AC3 repair |
| `4f34addd74` | spec: ETFS_PRODUCERS_REPOINT_TO_OPAL_DATA_ASSETS (all three partners) |

## The chain of findings, in the order they actually came

**1. The rollback restored S3 and never touched the CDN.** `lambda_function.py:1251` hardcoded
`/api/public/*` — a prefix renamed to `/api/general/*` on 2026-02-25. Positive control:
api/public = **0** matching behaviors, api/general = **6**. CloudFront *accepts* a no-match
invalidation and returns `Completed`, so the code printed `OK:` for a no-op. **Every rollback since
February was broken at the CDN step.** Reproduced live three times, including once by my own
roll-forward.

**2. Roll-forward to the 7/27 vintage, verified on two oracles.** Acceptance fixed in the ledger
BEFORE execution so it could not be fitted after: etag `a8cb00d8…`/19221, 4/4 match, negative control
held (the 7/22 object was 19212 and is gone). Published-state proof needed a REAL authenticated
session — `ui-smoke.mjs --origin` stubs `/auth/refresh`, so against a real origin every call 401s and
the tab reads "No benchmark data available" **for any vintage**. That first smoke was DISCARDED AS AN
INVALID MEASUREMENT, not scored as a failure.

**3. July carry-forward audit, per partner, against the NYSE calendar** (22 trading days; 07-03
closed for Independence Day observed):

| partner | written / classifiable | producer schedule |
|---|---|---|
| 49financial | **21/21 = 100%** | `bd-49f-etf-ownership-scheduled-floor` cron(45 10) |
| cottonwood | 19/21 = 90.5% | `cot-etf-ownership-daily-schedule` cron(30 10) |
| inflection | 13/21 → **14/22 true** | **NONE** |

**The gap count tracked the presence of a scheduled floor exactly.** Inflection was the only one of
three without one — CLAUDE.md's "a pipeline whose only trigger is another pipeline's success has no
schedule" made flesh.

**4. And a schedule alone would NOT have closed it.** `_latest_holdings_key()` returns
`sorted(keys)[-1]` — the MAX partition only. `holdings_2026-07-13.parquet` did not exist until
**2026-07-17T18:08:39Z**; the upstream backfilled 07-13/14/15 on the 17th and the producer processed
only the newest. **My first spec would have shipped, passed its own acceptance test, and left the gap
open.** Paired with a trailing-window catch-up; AC4 widened so a floor that fires perfectly and never
fills a gap must FAIL.

**5. The date-value slip — found only because Andrew said "remember it is T-1."** Content-hashing all
31 upstream partitions: **24 distinct books across 31 dates.** The upstream rewrites the `date` column
to match the filename, so `holdings_2026-07-18` (Sat) and `holdings_2026-07-20` (Mon) are
byte-identical ex-date. **The producer's promised guarantee — "source_as_of = the TRUE data vintage,
NOT the run date" — is defeated silently: a vintage field that cannot disagree with the filename is
not a vintage field.** My backfill of 07-20 returned `source_as_of: 2026-07-20` for a book proven to
be 07-18's.

**THREE DETECTORS, EACH CATCHING WHAT THE LAST MISSED — the progression is the finding:**
body-hash → 07-20, 07-27 · total-MV → **07-06** (different body, identical total to the cent) ·
per-ticker freeze → **07-15, 07-16** (3 of 4 tickers frozen, invisible to a whole-vector check).

**6. Layer-by-layer localisation — and it changed the fix.** bronze DISTINCT · inf-silver DISTINCT ·
**inf-GOLD IDENTICAL** · monolith DISTINCT. **The defect is confined to inf gold, so no vendor egress
was required at all.** Andrew had authorised Orion; the measurement made it unnecessary. Re-fetching
data we already hold correctly is exactly how a live rebate chain gets deepened.

## Errors of mine, and who caught them

1. **I told Andrew the inflection slips bore on the served-benchmark vintage decision. Category
   error** — served benchmarks are `data.pkl → Yang`; the slips are `opal-data-inf → ETFS`. Different
   bucket, producer, lineage. Caught by me, but only after offering it as a decision input.
2. **My Andrew-directed §2 reversal did not propagate to AC3 forty lines below it.** `~E` hit the
   contradiction before writing Terraform and SURFACED it rather than resolving it silently.
   **The retraction-did-not-propagate class, inside one document, by the agent who had just written
   the correction.**
3. **I credited `0.7.0_AE_CloudOps` with an observation they had already made themselves.** They
   declined the credit and showed the data was in their own pre-fire listing. Generosity that
   misplaces a fact is an error with better manners.

## The incident inside the incident

`~C` proved the rollback fix by running a REAL rollback — onto `exec-1b6a2a98c1c3`, reasoning "onto
itself, zero business-content risk." **That premise was checkable and false:** served state was the
7/27 vintage under an explicit Andrew goal. The test **displaced a sovereign-directed served state**
and invalidated the CDN so it went live. Andrew ruled restore; `~C` repaired it — reading state FIRST
this time — and all five discriminating values landed exactly. **A fix for a broken rollback proved
itself by performing an unintended real one.** Second finding from it: both mutations recorded
`restoredBy: dev@test.com`; `~C` then found a way to stamp a real actor identity, and was precise
that this is an evidence-gathering workaround, not a closure of the finding.

## What the seats did that made this work

Three separate agents stopped and said something where proceeding was easier and defensible:
`~E` on the AC3 contradiction AND on refusing to delete a correct S3 object to manufacture a test gap
(CLAUDE.md reserves that for human confirmation) · `~C` on the AC2 credential gap · `0.7.0_AE` on two
instrument traps during the Aug-1 fire, either of which would have produced a **false RED-ALERT on a
pipeline that had already paid three partners correctly**. The one thing that went wrong went wrong
because a premise was not checked before acting on production.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-which "yang pipeline execution records..."` | **NO CURATED RULE** | honest miss — it said so rather than routing a guess. Did not pick a fuzzy candidate |
| `comp-estate data-refresh` / `etf-reports` | named the chains + all 9 producers | first contact; gave the per-firm producer split that made the gap/schedule correlation visible |
| `comp-estate yang` | **not a known vertical** | correct refusal, redirected to `data-refresh` |
| `comp-routes behaviors` / `trace` | api/public=0 vs api/general=6 | THE control that proved the invalidation defect. Trace resolved the benchmark route to its exact S3 key |
| `comp-grep` | located `:1251`, the producers, the TF files | on-rails; used where a raw grep would have been gated |
| `comp-aws <fn>` | **rejected the arg** | not a lookup tool — it takes subcommands. Fell back to `lambda get-function-configuration` with a `# rail-checked:` marker |
| `lib/trading_calendar.py` | 22 trading days, July 2026 | resolved the calendar FIRST per NEVER#1. MEMORY's recorded "20 trading days" is WRONG for July 2026 |

## Next

- `~E`: three-producer repoint @`4f34addd74`. Oracles: 49F must sum to 528,132,730.04 to the cent;
  cottonwood 07-20 must CHANGE to 50,292,778.58 — **a repoint reproducing the old number has FAILED.**
- `~C`: closed. Open finding carried: any direct invoker can self-assert an arbitrary identity string.
- **INF-gold relabelling → INF-gold-canon cluster (MSTR), stays S3, gated on Andrew's ETFS-canon P0.**
  Also unrecorded elsewhere: `gold/canonical/holdings_*` is REWRITTEN DAILY (13-16 versions/partition),
  so **a rebate basis computed from it is not reproducible after the fact.**
- Cottonwood's two gaps: 07-20 fixed by the repoint, **07-31 genuinely absent upstream — not fixable
  by it, and must not be fabricated.**
