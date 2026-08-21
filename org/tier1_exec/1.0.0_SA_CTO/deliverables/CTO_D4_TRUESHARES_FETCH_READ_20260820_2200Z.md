# D4 / D4c -- the 22:00Z TrueShares fetch read

**Author:** 1.0.0_SA_CTO · **Date:** 2026-08-20 ~22:20Z · **Status:** MEASURED, one FINDING open
**Why this exists:** Andrew deferred the D4 serving question and the Phase-B scope word to
tomorrow morning "against tonight's fetch read" (~1425Z, REC agreed). This is that read:
what landed, its shape, its coverage -- and one defect the read surfaced.

---

## 1. THE HEADLINE

**The fetch fired on schedule and the data is genuinely live. But the TrueShares HOLDINGS arm --
the thing that was armed last night -- produced NOTHING, and it cannot have: the flag it is
gated on is never read and the function it would call is never called. `TS_HOLDINGS_ENABLED=1`
IS A NO-OP ON THE DEPLOYED BYTES.**

This is not a run failure. The run was clean. The capability was never wired.

---

## 2. WHAT LANDED (applied, measured at my seat)

Fire at **22:00:15-22:00:16Z**, exactly on the rule's `cron(0 22 * * ? *)`.

| Artifact | Bucket | Size | Written (UTC) |
|---|---|---|---|
| `silver/holdings/2026-08-20.parquet` | opal-data-etfs | 16,912 B | 22:00:15Z |
| `silver/netassets/2026-08-20.parquet` | opal-data-etfs | 10,072 B | 22:00:15Z |
| `silver/netassets_daily.parquet` | opal-data-etfs | 15,286 B | 22:00:15Z |
| `etf_history.csv` | opal-data-etfs | 53,336 B | 22:00:16Z |
| `snapshots/snapshot_2026-08-20.json` | opal-data-etfs | 2,876 B | 22:00:16Z |
| `trueshares/DIVZ/bronze/netassets/20260820/divz.html` | opal-data-assets | 467,033 B | 22:00:10Z |
| `trueshares/IDVZ/bronze/netassets/20260820/idvz.html` | opal-data-assets | 257,335 B | 22:00:10Z |
| `trueshares/{DIVZ,IDVZ}/silver/fact_netassets_page/date=2026-08-20/data.parquet` | opal-data-assets | 13,427 B ea | 22:00:16Z |
| + per-fund `meta/conversions/` + `meta/pulls/` manifests | opal-data-assets | | 22:00:16Z |

Bronze lands in **`opal-data-assets` under the monolith grammar** (`BRONZE_BUCKET=opal-data-assets`,
`BRONZE_GRAMMAR=monolith`, both applied), not in `opal-data-etfs`. **Naming this because a
`bronze/` census against `opal-data-etfs` returns a clean, confident, well-formed ZERO** (741
objects, top level = `config/ daily/ platinum/ silver/ snapshots/`) -- the wrong-prefix hazard,
not an absence. Raw ingest is healthy; it is simply in the other bucket by design.

**The data is genuinely fresh, not a re-stamped copy.** Day-over-day on the 114 holdings rows:
**111 changed `shares`, 108 changed `price`**. A live producer, verified by content movement
rather than by an mtime.

## 3. COVERAGE -- the discriminator

| Fund | Source | NAV / net assets | HOLDINGS |
|---|---|---|---|
| PFDE (Pathfinder Disciplined US Equity) | filepoint | YES | **YES -- 90 rows** |
| PFOE (Pathfinder Focused Opportunities) | filepoint | YES | **YES -- 24 rows** |
| DIVZ (Polen Dividend Income) | trueshares | YES | **NO -- 0 rows** |
| IDVZ (Polen International Dividend Income) | trueshares | YES | **NO -- 0 rows** |

- netassets: **4 of 4 funds** -- complete.
- holdings: **2 of 4 funds**. `source='trueshares'` rows in the holdings parquet: **0 of 114**
  today, **0 of 114** yesterday.
- Under `trueshares/` in opal-data-assets (368 objects, full pagination walk): the only bronze
  feed is `netassets/`. **Keys mentioning "holding" anywhere under that tree, all time: 0.**

## 4. THE MECHANISM -- SOURCE-CONFIRMED on the DEPLOYED ARTIFACT

Deployed package pulled and read, not inferred from the repo.
`CodeSha256 = tHeVS53pKxV4hX9UXciJsigvO8t5v10T3CmN2VwQURI=`, LastModified `2026-08-20T01:18:32Z`,
2 members (`lambda_function.py`, `landing_guard.py`).
`sha256(deployed lambda_function.py) = f306aa237e3ea3536ed9ff5316da0ce09ebc0b9d548792a3f2d9f02677594298`
= **byte-identical** to `infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py`
at HEAD. No drift; the repo IS the runtime here, so the source read below is a deployed-bytes read.

Token counts across **every member of the deployed package**, each with a positive control run in
the same call so the instrument is shown to discriminate:

| Token | Occurrences | Verdict |
|---|---|---|
| `TS_HOLDINGS_ENABLED` | **1** -- only `:381` its own assignment | read into a module-level bool, **never branched on** |
| `fetch_trueshares_holdings` | **1** -- only `:420` its own `def` | **never called** |
| `fetch_filepoint` (POSITIVE CONTROL) | 3 -- def `:557` + call `:715` + docstring | wired |
| `fetch_trueshares` (POSITIVE CONTROL) | 2 -- def `:467` + call `:727` | wired |

The only route into the holdings parquet is `rec["_holdings"]`, set at **`:626`, inside
`fetch_filepoint`** (def `:557`). `resolve_fund` (`:705`) branches `filepoint` -> `fetch_filepoint`
(holdings + NAV) / else -> `fetch_trueshares` (**NAV only**). There is no third branch and no
flag test anywhere in the file.

**Therefore the TrueShares holdings capability is written and unreachable. Flipping the env var
to "1" changes nothing, and would change nothing on any future run.**

## 5. WHY EVERY CHECK PASSED -- this is Rule 22a's named class, and it is worth the record

The deploy ledger `org/critical_paths/change_management/20260820T0113Z_trueshares-holdings-enable_deploy_completion.md`
L5 states the verify as: *"DEPLOYED BYTES read the flag AND the applied env carries it -- both
planes"*, with the bar *"deployed package `TS_HOLDINGS_ENABLED` > 0 AND `get-function-configuration`
env shows =1."*

**Both limbs were TRUE. I re-ran both and both still pass.** The package does contain the token
(count 1 > 0); the applied env does carry `"TS_HOLDINGS_ENABLED": "1"`. The deploy was closed
honestly against the bar it wrote.

**The bar measured PRESENCE and was read as WIRING.** `> 0` cannot separate *"the code reads this
flag and acts on it"* from *"the string appears once, in its own assignment, and nothing consumes
it."* The count that would have discriminated is not the token's -- it is the **call count of the
function the flag is supposed to enable**, where the def-only case reads 1 and the wired case
reads >= 2. Both positive controls in the same file show >= 2.

**It is the exact inverse of the 2026-08-12 instance already in CLAUDE.md Rule 22a** (there: env
vars applied and verified 6/6 on a package containing ZERO references to them). Same defect, opposite
polarity: **there the reference was missing, here the reference is present and inert -- and the
present-but-inert form is the more dangerous one, because it makes a presence check pass.**

**The discriminating test, which costs one query and is the acceptance bar this arm should have
carried:** *does `silver/holdings/{date}.parquet` contain rows with `source='trueshares'`?*
Today: 0 of 114. That test fails on the defect and passes only on the capability. A behavioral
bar, not a config read -- Rule 22a's "EXERCISE the path."

**Live specimen for NFRA_EPISTEMY.C3-IDENTITY:** 0.8.0's `reach` axis would have caught this by
construction. The closure terminates **PRESENCE_ONLY** (chain reached the deployed digest and
stopped), and their constructor **refuses `BEHAVIOR` without a KNOWN EXECUTION hop** -- so the
schema could not have rendered this arm as working. Routed to them tonight as a same-day specimen.

## 6. SECOND OBSERVATION -- not a defect, a naming one

`staleness_days` reads **0** for all four funds, while `data_as_of` is **2026-08-19** for
DIVZ/IDVZ and **2026-08-20** for PFDE/PFOE.

**This is NOT a staleness finding and must not be reported as one.** Today is Thursday 2026-08-20,
a trading day; an issuer-reported NAV drawn at 22:00Z carrying the prior day's as-of is ordinary
issuer behavior, and NEVER#1's T-1 default covers it directly.

The observation is that **`staleness_days` does not measure days.** Source-confirmed at `:726-728`
and `:697`: it is set to `0` by the tier-1 live-draw branch and to a carry distance by `_carry` --
so it is the **source-ladder tier distance**, and a name saying "days" invites a reader to compare
it against `data_as_of` and conclude the two disagree. Naming a field by the number it happened to
hold rather than by what it measures -- the same class I named across four surfaces today. One-line
observation for the D4 owner; no action tonight.

## 7. WHAT THIS DOES AND DOES NOT AUTHORIZE

- **The fix is ordinary lane work and needs no new approval.** Andrew's standing TrueShares egress
  approval (0057Z) already covers the pull; the missing piece is a call site, not a permission.
  **I am not manufacturing a gate on it** -- wiring belongs to the D4c owner (0.4.0_DS Phase A
  design / 0.7.0_AE arm), lands through the normal commit -> plan -> apply -> ledger cycle, and
  should carry the section-5 behavioral bar as its acceptance instead of a token count.
- **It does not touch tomorrow's D4 serving question.** That call is Andrew's and is unchanged;
  this read simply means the holdings half of the TrueShares picture does not exist yet, which is
  material to how he scopes Phase B.
- **Nothing is armed, changed, or deployed by this read.** Read-only throughout: S3 gets,
  `get-function`/`get-function-configuration`, one package download to scratchpad.

## 8. GROUNDING

`grounding:` **desired** -- EventBridge `etfs-netassets-daily` `cron(0 22 * * ? *)` ENABLED;
TF `netassets-lambda.tf:186`. **applied** -- `get-function-configuration` env (5 vars, verbatim
in section 2/4); `get-function` CodeSha256 + downloaded package bytes; S3 `head-object` UTC on the
landed keys. **exercised** -- the artifacts' own CONTENT read (114 rows, 111 shares-moved), the
4-fund vs 2-fund coverage join, and the 0-of-114 `source='trueshares'` measurement, each with its
denominator printed.

---

## 9. THE SERVING SURFACE -- measured, and it REFRAMES tomorrow's call

Andrew's deferred D4 question is a SERVING question, so I read what is actually served rather
than reasoning from the silver tier.

**`opal-data-etfs/platinum/etf_ownership_dashboard.json`** (6,404 B, written today 16:00:03Z) is
the live served surface. It answers **"which partner firms own how much of the four Opal ETFs"** --
`grand_total_ownership_value` $655,865,245.20 over a universe of exactly `["DIVZ","IDVZ","PFDE","PFOE"]`,
three partners each.

**IT HAS ZERO DEPENDENCY ON THE HOLDINGS FEED.** Token counts over the entire served document:
`holding` **0** · `shares` **0** · `cusip` **0** · `security_name` **0** · `nav` **0** ·
`net_assets` **0**. It is built from the partner ownership files (`daily/{partner}/{date}.json`),
not from the issuer holdings draw.

**So the section-4 defect degrades NOTHING that is currently served.** The two things sit on
different axes: the dashboard is *who owns the ETFs*; the holdings feed is *what the ETFs hold*.
**That makes Phase B a "should we build the look-through" decision, not a "we are broken, repair
it" one** -- and those are different questions with different answers. Stating it because the
section-4 finding, read alone, invites the second framing.

**Second, and it cuts the other way:** the served dashboard covers **all four** ETFs including
DIVZ/IDVZ. So the ownership axis is complete while the holdings axis is 2 of 4. **A reader of the
dashboard has no signal that the look-through would be half-empty** -- which is precisely the sort
of thing to settle before serving a look-through, not after.

**Cadence note, EXPLICITLY NOT A STALENESS FINDING.** Per-partner: 49financial `as_of=2026-08-19`
(1 day), inflection `as_of=2026-08-20` (0), cottonwood `as_of=2026-08-17` (3). Counting in TRADING
days from Thursday 2026-08-20: 08-19, 08-18, 08-17 -- so cottonwood is three trading days back,
**not** a weekend artifact, and the honest thing is to say so rather than reach for NEVER#1 as a
dismissal. **But the producer is not frozen and I checked rather than assumed:** `daily/cottonwood/2026-08-17.json`
was WRITTEN TODAY at 10:30:30Z, and `daily/49financial/2026-08-19.json` today at 10:45:11Z. **Our
pipeline ran today and emitted the newest data the source carries** -- an upstream cadence fact,
not a producer defect. The dashboard's own `freshness` cell reads `current` for all three, so its
author treated a 3-day cottonwood lag as within declared cadence. **Open question for the D4 owner,
not a finding from me: is cottonwood's 3-trading-day lag its DECLARED cadence?** If it is, nothing
to do; if nobody has declared one, then `freshness: "current"` is a verdict with no bar behind it.
*(Relevant beside today's Cottonwood work: that feed lands with a lag, and it is the ownership feed,
not the supervised-AUM plane investigated separately today.)*

**`monthly_context: {"available": false}`** -- last monthly report is `platinum/reports/2026-07/`
written 2026-08-01, consistent with a month-end cadence not yet due for August. Flagged as an
observation only; I did not establish whether `available:false` means "not due" or "lookup failed",
and those are different, so I am not claiming either.

---

**Time plane pinned before any timestamp was quoted.** `aws s3 ls` rendered `2026-08-20 18:00:15`
for the same object `s3api head-object` renders `Thu, 20 Aug 2026 22:00:15 GMT` -- the 4h EDT
offset, proven on one object with both tools. **My own pre-fetch baseline recorded the historical
18:00 stamps as "prior-cadence residue, not a second producer"; that note was this exact error**,
and had it survived I would have reported a phantom cadence change on a producer that has been
firing at 22:00Z all along. Caught before it reached a report, by the control the law prescribes.
