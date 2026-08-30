# Session close 04:00-18:35Z -- `0.4.0_DS_ClientPlatform~C` (LANE ~C) -- ADVI_BDPARITY: P1-PROBE CLOSED 5/5, P2-CENSUS planned and graded, W2 FIRED and BLOCKED AT AUTH with the word unspent

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE

**Serial:** `0.4.0_DS_ClientPlatform~C` | **Window:** 04:00-18:35Z (prior log `dsC_bdparity_p1probe_pull_fired_0020-0400Z.md` covers 00:20-04:00Z) | **Project:** ADVI_BDPARITY, ONE project per Rule 27 | **Written for a successor who was not here**, per the 18:2xZ Andrew edict.

---

## READ THIS FIRST IF YOU ARE THE SUCCESSOR

**The census (W2) is authorized, built, and BLOCKED ON ONE THING: the Black Diamond session cookie
is expired.** Andrew spent the vendor word at 18:0xZ. W2 fired at 18:29:33Z and failed at
`/session/token` with **HTTP 401 BEFORE the account loop**.

```
ZERO data calls. ZERO objects landed. ZERO accounts pulled. THE WORD IS NOT SPENT ON DATA.
verified against S3, not the error: reporting_performance/2026-08-30/ = 5 objects (the P1 five, unchanged)
```
⛔ **DO NOT RE-APPROVE ANYTHING. DO NOT RE-ASK ANDREW.** The word survives intact. What is needed is a
**fresh `.bd.identity` cookie in Secrets Manager `blackdiamond/49f/session`** -- which requires a
**human BD login** (the module reuses the existing 49F session precisely so there is "no second login
box"). Routed to `0.7.0_AE_CloudOps` at msg 88977. The credential worked at 03:05Z (the P1 pull) and
04:35Z (the insurance fire); `describe-secret` LastChanged is 2026-08-27, so the session aged out
server-side between 04:35Z and 18:29Z.
⛔ **DO NOT RETRY THE 401.** It is not transient, and repeatedly hitting a vendor auth endpoint is its
own bad act.

**W2 IS READY TO RUN THE MOMENT THE COOKIE IS REFRESHED. Everything below is done and verified:**
- **Cohort: exactly 5,309 accounts**, built as `twr_daily` (7,370 at the 2026-08-28 vintage) INTERSECT
  `dim_account_xref` rows carrying a `bd_account_id`. Written to the scratchpad as `w2_cohort.json`;
  **rebuild it from those two tables rather than trusting a stale file.**
- **The account-id derivation, POSITIVE-CONTROLLED:** the xref stores the EXTERNAL id (`z08` +
  internal, uniform across all 6,201 rows); the puller needs the INTERNAL int. `external[3:]` matched
  the known internal id on **4 of 4** P1 accounts present in the xref. **0 ids failed to parse.**
- **Payload shape:** `{"q_start": "2026-07-01", "q_end": "2026-08-28", "pull_date": "<the run date>",
  "feeds": ["performance"], "accounts": [{bd_account_id, schwab_account, inception: null}, ...]}`.
  **`feeds: ["performance"]` is REQUIRED** -- without it the vehicle pulls all three feeds and triples
  the vendor spend on data P2 never reads.
- **CHUNKING IS MANDATORY: the Lambda timeout is 300 s, not 900.** At the measured 1.40 s/call that is
  ~212 calls/invocation theoretical, **~148 with a 30% margin -> ~72 invocations** for the two passes.
  **A chunk that overruns is KILLED mid-run, landing bronze with no manifest** -- that is the failure
  mode the margin exists for.
- **THE RUN IS INHERENTLY RESUMABLE.** List `blackdiamond/49f/bronze/reporting_performance/{pull_date}/`
  and pull only the accounts not already present. **Do not restart from zero.**

⚠ **AND THE THING A SUCCESSOR WOULD NOT GUESS: W2 WRITES TO FOUR OF THE FIVE KEYS THE PINNED P1
RECORD WAS COMPUTED FROM** (13477111, 18927251, 21089351, 22596361 -- same `pull_date`, same `q_end`;
an S3 key here is `{feed}_{account}_{q_end}` and carries NO pull identity). The bucket is VERSIONED so
nothing is destroyed, and **all 18 P1-era VersionIds were captured BEFORE W2 ran** and committed at
`3d9333bfb3` (`ADVI_BDPARITY_P1_bronze_object_versions_20260830.json`). **The P1 table now cites
VersionIds, not keys. Keep it that way.**

---

## What this window did

**P1-PROBE closed at 5 of 5** and **P2-CENSUS was planned, graded, and taken to the point of firing.**

| deliverable | commit | state |
|---|---|---|
| BP1-3 gap closure (per-cell day accounting) + BP1-4 design | `378a2d696f` | graded |
| BP1-5 proof instance (first issue) | `94169ae1ec` | superseded |
| BP1-6: ruled 1Y-open fix + CRO thresholds + Dlog | `2762f02f6a` | graded PASS |
| CTO's day-column ask | `aeb89b94de` | closed |
| BP1-5 re-issued over BP1-1..BP1-6 | `b462717dcc` | **VALID rc=0, 5/5 PASS** |
| Rule-24 record + alignment | `de93f43a1c`, `f54ebf7bf8` | closed |
| P2-1 census plan | `475e0605ea` -> re-cut `6a99820c40` | **graded PASS** |
| per-feed selector patch | `d9ac9dc597` -> `d981d2366a` | **applied by AE~Y @`49a851ea2e`** |
| H1-H4 post-g-7 measurement | `7dac32ff34` | **graded PASS** |
| P1 bronze VersionId pin | `3d9333bfb3` | committed |

**16 commits this window.** Overrides: three `STRUCTURAL-TWOPHASE` comp-system overrides taken and
**all three discharged in-session** (`a047965ac2`, `beb00571c3`, `ca7ce3b071`) -- an undischarged one
is a discipline event.

## The finding that matters

**One account's entire disagreement with BD was OUR OWN missing data.** `0010083855` read
**+41.0 / +44.2 / +46.2 bp LARGE**; after C02-g-7 backfilled the five never-produced trading days it
reads **+0.000007 bp -- EXACT on all three ruled periods.** Cohort-wide: **16 LARGE -> 11 LARGE /
2 TIGHT / 3 EXACT.** ⭐ **The eleven that did NOT move are now STRONGER evidence: the largest candidate
mechanism was removed and they held, so those are CALCULATION differences, not coverage.** That is
P3's material at the convention gate.

## Errors I made, all corrected on the record

1. **The cost table flattered the ask.** I priced both passes as batchable; pass 2 (SI at each
   account's own anchor) carries ONE range per call and does not batch. **4.1 h vs ~2.1 h, NOT vs
   5 minutes** -- and I had already told Andrew the wrong figure. Corrected at `6a99820c40`.
2. **A corroboration claim I had not earned.** I wrote that 5,309 "independently reproduces" CVO's
   figure. It does not: **5,309 first entered the record in MY OWN 17:38Z message the day before**,
   and the ruling cited it. **A claim that INHERITED a number cannot corroborate it** -- and I have a
   standing note about exactly that failure.
3. **H1's scope claim.** I predicted the backfill would add exactly five days "because it does NOT
   address 2026-08-18". **It did** -- 08-18 was re-emitted and now computes 6,382 returns, so the gain
   was six and the day-count gap went to **zero**. `1.0.0_SA_CTO` 86269 had composed exactly that case.
4. **A misattribution in my own docstring** -- I credited the issuer's wording to the gate.
5. **H2's unit conflation** -- "same shift" is true in Dlog and false in bp.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `returnMethod`, `83426`, `in_0833_universe`, `VACUOUS-NO-LINKED-DAYS` | PASS -- denominators printed every run; the `--query length()` page-count trap caught and replaced with client-side counting |
| `.tools/commit-gate.sh` | every `.py` edit | PASS -- also caught non-ASCII in the Lambda docstring |
| `.tools/safe-commit.sh -F` | 16 commits | PASS -- msg-verify MATCH each time; refused the DS lane on `infra/aws`, which correctly routed the selector to an AE lane |
| `.tools/proof-of-spec-check.py` | BP1-5 instance | PASS -- VALID rc=0 across THREE checker vintages (`3948c766a7`, `cec2a9b663`, `ecce0820d2`), re-run at each bump rather than assumed |
| `comp-system` | 3 regens | PASS -- all three overrides discharged |

**What worked:** the negative controls. The baseline run caught a count-standing-in-for-a-set arm; the
day columns caught three EXACT rows that were empty windows; the pre-flight caught W1's inexpressibility
and the key collision. **What failed:** nothing silently. **Gap found:** `HOLE_DATES` was a hardcoded
constant and went stale the instant the data it described was repaired -- now derived from the vintage.

## MCP traffic

~40 substantive dispatches handled. Significant: Andrew's word (17:1xZ card 2, 18:0xZ W1-skip/W2-run,
18:2xZ the reset edict); CVO grades on BP1-2/3/5/6, P2-1 and H1-H4; CTO's convention ruling (85237),
the selector diff read, and the day-column ask; COO's P2-CENSUS cut and the W1 sovereign escalation.

## Blockers

**ONE, evidence-cited, and it is not mine to clear:** the BD session cookie is expired (HTTP 401 on
`/session/token`, 18:29:33Z; zero data calls; S3 verified unchanged at 5 objects). Owner:
`0.7.0_AE_CloudOps` + a human BD login. **Not a blocker on the word, the plan, the cohort or the
vehicle -- all four are ready.**

## Next Steps

1. **[`0.7.0_AE_CloudOps`]** refresh `.bd.identity` in `blackdiamond/49f/session` (human BD login).
2. **[`0.4.0_DS_ClientPlatform~C` or successor]** on that refresh: fire W2 chunked (~148 accounts,
   `feeds:["performance"]`), resume by listing landed objects, report landed-vs-requested,
   `range_match` per account, and both prior snapshots untouched. **No new word needed.**
3. **[`3.0.0_SA_CVO`]** grades the census; **[`1.0.0_SA_CTO`]** holds P3 for the eleven real cells.
4. **[Andrew]** nothing outstanding -- his word is spent correctly and intact.
