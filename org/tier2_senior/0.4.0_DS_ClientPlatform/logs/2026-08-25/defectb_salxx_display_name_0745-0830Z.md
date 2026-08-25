# 0.4.0_DS_ClientPlatform~Z -- ANDREW-DIRECT DEFECT B: SALXX display name (0745-0830Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Window

Relaunch 07:45Z on Andrew's 07:3xZ direct instruction ("fix this and only this, verify visually,
confirm pipelines scheduled/robust, commit, push / prod-deploy, all necessary logging").
Two defects across the fabric; **DEFECT B (the SALXX display name) is this seat's**, assigned by
`0.0.0_AB_MSTR~Z`. Defect A (sub-categories panel) is `0.4.0_DE_ClientPlatform~Z`'s and is not
touched here.

## Current State

**DEFECT B's CODE IS DONE, COMMITTED, PUSHED AND DEPLOYED. Rung 2 (the served artifact) is NOT
discharged: the live key still carries the raw strings because nothing has invoked the new code
yet.**

- **Commit `2e9737af49`** -- `data/etfs/scripts/gold/etf_positioning_publisher.py`, +68/-1.
  **ON `origin/SITEZ`** (ls-remote `refs/heads/SITEZ` = `e4b241a80f`; `git branch -r --contains
  2e9737af49` -> `origin/SITEZ`). Pushed by `0.0.0_AB_MSTR~Z` per LD-0367, not by this seat.
- **DEPLOYED**: `etf-positioning-producer` CodeSha256 `631ELit6nuAD0+...` -> `p/mc7hvScGyYxxMK9...`
  at 2026-08-25T08:19:03Z. Applied by `0.7.0_AE_CloudOps~Z`; **verified independently at this seat
  on the deployed artifact, not on the deployer's report** (see Verification).
- **NOT PUBLISHED**: `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json` still
  LastModified 2026-08-25T04:53:51Z, 126,863 B, SALXX still
  `STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS`. "Deployed" is true and misleading alone.
  **2b (ad-hoc INVOKE of the deployed Lambda) is `0.7.0_AE_CloudOps~Z`'s and is the only remaining
  step before Andrew can see the fix.** This seat deliberately did NOT invoke: two concurrent runs
  would race a client-facing key and the loser's bytes are indistinguishable afterwards.

### What was built

A serving-tier, ticker-keyed `DISPLAY_NAME_OVERRIDES` + `_display_name(ticker, raw)` in
`etf_positioning_publisher.py`, applied at the holdings serve step. Two entries: `SALXX` ->
`State Street U.S. Government MMKT` (Andrew's verbatim string, a ruling), `FXFXX` ->
`First American Treasury Obligations Fund` (**DERIVED BY THIS SEAT, NOT HIS WORD** -- the raw
carries a meaningless maturity date on a money-market fund; approved by `2.0.0_SA_COO~Z` as
derived-awaiting-confirm and labelled as such in the code, the commit message and every message).

**Home = the platinum publisher, per Rule 17b (display naming is serving-tier).** Confirmed by
`0.0.0_AB_MSTR~Z` (8599) and `1.0.0_SA_CTO~Z` as Rule 17b APPLIED rather than a new ruling.

### Why a curated map and not a transform (four prior remedies were falsified)

```
raw     STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS
target  State Street U.S. Government MMKT
```

Title-casing yields `State Street Inst U.S. Government Mmkt Admn Class` -- wrong three ways at once.
No string function maps raw to target; the edit is EDITORIAL. **The generic alternative was tested
against real data and rejected on evidence**: a trailing-date strip works on 1 of 169 names today
and would silently corrupt a bond name the day one lands, because maturity IS a bond's identity.

**The property the four dead remedies lacked:** a ticker ABSENT from the map returns the INCOMING
NAME unchanged. `seed-etf-classifications.py:62` is `.get(ticker, ticker)` -- it falls back to THE
KEY, so a miss writes the literal `"SALXX"` and presents as success. Same idiom, opposite blast
radius.

## Verification

**The acceptance oracle (Z-S48, amended by its disarm owner `2.0.0_SA_COO~Z` from 4 names to 2).**
Built the artifact TWICE from the SAME gold partition in the same minute, fix ON and fix OFF, so
upstream movement cannot confound the diff:

```
CONTROL A  fix-OFF build == the SERVED artifact field-for-field (generated_at excluded)
           -> nothing upstream moved; the delta is mine alone
ORACLE     ROWS CHANGED 4 of 187 | FIELDS TOUCHED ['name'] | book-level diffs 0 of 4
             DIVZ SALXX + IDVZ SALXX -> State Street U.S. Government MMKT
             PFDE FXFXX + PFOE FXFXX -> First American Treasury Obligations Fund
           2 distinct names of 169 tickers; 183 of 187 ROWS byte-identical.
           BOTH GRAINS STATED -- COO~Z's oracle is in tickers, my measurement in rows, and a
           later reader diffing "2" against "4" would file a false discrepancy.
MUTANT     re-point the fallback at the KEY -> damages 8 of 8 unlisted controls.
           A control that COULD have failed and did not.
NEGATIVE   BP PLC / GSK PLC / MPLX LP unchanged (acronym companies, Z-S48's open product fork).
           JPM / MRVL / VZ unchanged -- outside Andrew's instruction.
```

**Deployed-artifact verification (Rule 22a CODE layer), done at this seat:**

```
downloaded the DEPLOYED package; recomputed sha256(b64) == reported CodeSha256 p/mc7hvS...
   -> the artifact inspected IS the artifact deployed, not a same-named one
MEMBERS 2 (etf_positioning_gold.py, etf_positioning_publisher.py)
   both raw-sha256 IDENTICAL to their repo files
   no trading_calendar.py -> nothing shadows opal-trading-calendar-layer:1
CONTENT 4/4 probes PRESENT incl. the CALL SITE; negative control zzz_no_such_token_9999 ABSENT
=> CTO~Z's stated arithmetic acceptance test for the deploy PASSES.
```

## Corrections issued against my own work

1. **"the two name maps share ZERO keys" was measured over ONE key space and argued as if it were
   the only one.** There are two: holding tickers (169, intersection 0) and BOOK CODES (4,
   intersection 4 -- **and 3 of 4 ALREADY DIVERGE**). Corrected before either exec ruled on it.
2. **"deploy-first inverts D5 from a reverter into a no-op" is FALSE.** `generated_at` is inside
   the hashed body, so **D5 can never fire** -- exercised both ways (two builds, same gold, 1s
   apart: shas differ; with `generated_at` removed: equal). The ORDERING conclusion is unchanged
   and stronger (13:00Z writes unconditionally). `1.0.0_SA_CTO~Z` ratified the correction and
   bounded it to ONE file: the source pattern it was adopted from keeps its wall-clock in the
   MANIFEST, so the defect was introduced in translation, not inherited. **The error ran in the
   direction of describing the system as SAFER than it is, inside a hazard warning.**
   `2.0.0_SA_COO~Z` had amplified the original form to six seats and self-corrected in parallel.

## Findings FILED, not fixed (scope fence: two defects, not a third)

| Finding | Evidence | Routed to |
|---|---|---|
| Book-name divergence, 3 of 4 | served `Polen Dividend Income ETF` vs shared map `Opal Dividend Income ETF`, which calls ITSELF served canon. Client-facing branding. | `2.0.0_SA_COO~Z`; escalated to Andrew by `0.0.0_AB_MSTR~Z` |
| D5 is inert while its docstring asserts it is active | `generated_at` inside the hashed body; two senior seats cited it as a live guard in a decision | `2.0.0_SA_COO~Z` |
| 3 stale PRE-FIX copies of the publisher | `.runtmp_to5/{pkg,dep/pkg,mf/pkg}/etf_positioning_publisher.py`, all 22022 B vs the real 26133 B. Untracked, not gitignored. A build from them ships old code and looks normal. INERT tonight (AE~Z's zip verified correct). | `2.0.0_SA_COO~Z`, `0.7.0_AE_CloudOps~Z` |
| `build_package.py` lists 4 members; the live package is 2 | a packaged `trading_calendar.py` would shadow the layer | ratified as a DEPLOY RULING by `1.0.0_SA_CTO~Z`; the 4-vs-2 disagreement itself filed |
| "EventBridge has ZERO rules at hour 11" is FALSE | 9 rules fire in hour 11 (8 with hour field exactly `11`, +1 at `11,21`). The zero is a `cron(0 11 ` PREFIX count. **The true and stronger finding: ZERO rules match bbg/bloomberg/terminal at ANY hour** (137 rules materialised client-side; positive control `etf` = 8). | `0.7.0_AE_CloudOps~Z` (owns the deliverable), CTO~Z, COO~Z, MSTR~Z |
| `comp-pipescript` has no `etfs` pipeline | `--pipeline` choices are bd/inf/cot/mdpf/advi only; a comp-tool coverage gap is a defect per CLAUDE.md | noted, unrouted |

## Pipelines scheduled/robust -- this seat's leg only

```
etf-positioning-producer-daily   cron(0 13 * * ? *)  ENABLED   <- a REAL ScheduleExpression
etfs-netassets-daily             cron(0 22 * * ? *)  ENABLED   <- writes silver/holdings
resolve_as_of() on the deployed path, CALLED (not assumed): as_of 2026-08-24,
   frontier 2026-08-25, trading_days_behind = 1  -> HEALTHY T-1, NEVER#1 resolved
silver/holdings newest 2026-08-24 written 22:00:17Z
   (aws s3 ls renders 18:00:17 LOCAL with no marker; pinned with head-object -- 4h offset)
```

So today's silver 2026-08-25 lands ~22:00Z, AFTER the 13:00Z gold fire; on today's inputs 13:00Z
should resolve the same as_of that rung 2's evidence is about. **Stated as a PREDICTION, not a
measurement** -- the 13:00Z input state does not exist yet. The name fix is as-of independent, so a
byte difference at 13:00Z is not a regression.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-find | -i NAME_OVERRIDE, -i ETFS_GOLD_BUCKET, -i opal-data-etfs, --name etf-positioning | PASS | Found the estate's existing ETF_NAME_OVERRIDES (BUILD LADDER rung 2) and the producer TF. -i used per Rule 21's case-sensitivity law. |
| comp-find | --name pattern under infra | WARN | Measured zero over 7844 files; the tool NAMED the remedy (-i) itself and the -i content form found it. Guarded-zero behaviour worked as documented. |
| comp-estate | --resource etf-positioning-producer | FAIL | "no chain references" -- the ETF positioning thread is not in the coverage resolver. |
| comp-aws | comp-aws etf-positioning-producer | FAIL | Not a valid form; comp-aws takes derive/score/snapshot/..., not a resource name. |
| comp-pipescript | io ... --pipeline etfs | FAIL | **GAP: no etfs pipeline exists.** Answered the consumer question with comp-find instead. |

**What worked:** comp-find's band classification separated the real ETF_NAME_OVERRIDES definition
from doc/test noise in one call, which located the estate's existing mechanism and made the
"different universe" argument possible.
**What failed:** comp-estate --resource and comp-aws both dead-ended on this producer.
**Gap found:** comp-pipescript has no etfs pipeline, so "who consumes this gold?" -- exactly the
completeness question a gold-script edit should ask -- has no comp-tool. Answered with comp-find
plus a live s3 ls: only the two producer files reference the ETF gold bucket, so the publisher is
its sole consumer and the fix is complete.

## MCP traffic

~28 messages read and ACKed (7 at load + the rest in-window). Significant: MSTR~Z 8577 (relaunch
brief + fence), MSTR~Z 8599 (publisher home CONFIRMED), COO~Z 8609 (Z-S48 scope RATIFIED + oracle
amended 4->2), COO~Z 8669 (rung 2 ordering ADOPTED from my inversion), COO~Z 8707 (the served
artifact was never produced by the Lambda), CTO~Z 8713 (D5 correction ratified + bounded to one
file; build_package.py deploy ruling). Sent 8 dispatches, 25/25 DELIVERED.

## Blockers

**None on this seat.** Rung 2c is SEQUENCED behind `0.7.0_AE_CloudOps~Z`'s 2b invoke, which is a
named owner performing an assigned act -- not a blocker, and not a gate I manufactured. The
verifier is written and staged; it runs in seconds on the republish.

## Next Steps

1. **[0.7.0_AE_CloudOps~Z]** 2b: invoke the DEPLOYED Lambda ad-hoc (not a local run) so the served
   artifact is produced by the production code path for the first time in this product's life.
2. **[0.4.0_DS_ClientPlatform~Z -- me]** 2c on republish: report (i) the two target rows, (ii) that
   the DEPLOYED Lambda produced the bytes (version + invocation correlation), (iii) the Z-S48
   oracle re-run ON THE SERVE.
3. **[0.2.0_DT_PortfolioAnalytics~Z]** Rung 3, the production render Andrew actually opens. They
   hold a BEFORE capture showing both defects on the live page.
4. **[Andrew]** the FXFXX target string, as a DERIVED string awaiting his confirm.
5. **[Andrew]** the Polen-vs-Opal book-name branding divergence, escalated by MSTR~Z.

---

## ADDENDUM 08:3xZ -- RUNG 2 IS NOW DISCHARGED

Appended rather than rewritten: the body above was true when committed (`a03a8fc710`) and this
record should show the sequence, not a tidied end state. **What changed: `0.7.0_AE_CloudOps~Z`
invoked the deployed Lambda at 08:30:31Z, and it published at 08:31:06Z.**

```
SERVED  platinum/etfs/positioning_data.json  08:31:06Z  126,809 B  data_as_of 2026-08-24
   DIVZ SALXX / IDVZ SALXX -> State Street U.S. Government MMKT
   PFDE FXFXX / PFOE FXFXX -> First American Treasury Obligations Fund
ORACLE RE-RUN ON THE SERVE (vs the 04:53:51Z pre-fix document, not vs a local build)
   ROWS CHANGED 4 of 187 | FIELDS TOUCHED ['name'] | book-level diffs 0 of 4
   183 of 187 rows byte-identical | VERDICT exactly-4-and-only-name TRUE
```

**PRODUCER ATTRIBUTION PROVEN ON CONTENT, NOT ON A CLOCK** -- the discriminating step, because
timestamp proximity degrades exactly when two writes land close together:

```
Lambda log:  [publisher] built 126809 B, sha256 98650407cd829225...
I hashed the served object myself: sha256 = 98650407cd829225...   IDENTICAL, size IDENTICAL
run_class=adhoc  -> correctly marked a QA run, not production
as-of resolution IN THE LAMBDA: expected_frontier=2026-08-25, as_of=2026-08-24,
   trading_days_behind=1  -> independently reproduces my pre-run prediction
```

This also closes `2.0.0_SA_COO~Z`'s 8707 finding for the first time in the product's life: the
served artifact is now one its own producer made.

**NOT discharged: RUNG 3** (the rendered page), `0.2.0_DT_PortfolioAnalytics~Z`'s. Noted to them
that Defect B needs NO promote -- it is a DATA change on an already-served key -- so the two
defects reach the page through different mechanisms and should not be reported as one gate.

**Observation for `0.7.0_AE_CloudOps~Z`'s posture leg, filed not chased:** the run took 36,847 ms
of a 120,000 ms timeout and 264 MB of 512 MB. Rule-5 sizing holds, but the measured wall time is
~2.5x the TO contract's stated 15.0 s worst case (Init 2,297 ms is only part of it). Headroom is
smaller than the contract implies.
