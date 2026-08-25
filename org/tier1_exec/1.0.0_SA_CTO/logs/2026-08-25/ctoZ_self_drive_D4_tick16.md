# /self-drive D4 -- ticks 15-16 log (2026-08-25 00:46Z - 01:09Z) -- state: ARMED

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier `org/XXX.md:408` · continues `ctoZ_self_drive_D4_tick14.md`.
**This window is the critical hour of the round.** Andrew escalated twice; one ruling of mine was refused and withdrawn, a second was withdrawn on my own audit, and a third was corrected by two seats.

## SCOPE + COMPLETION

```
D4 -> 2 project(s) [ETFS_INGEST, ETFS_POSITIONING]   device: sitez
  claim scan 324 JSONs · denominator 1 of 9 live directives · 0 ahead of origin/SITEZ
  COMPLETION TEST: NOT DONE -- 0 of 2.  REACHABLE 2 / UNREACHABLE 0.
  open calls at Andrew: ZERO
```

## ⭐ ANDREW'S QUESTION ANSWERED AT THE SOURCE: THERE IS NO PROVIDER DIVERGENCE

VERBATIM: *"establishing concretely what the 'as of' is for these securities... id rather just sync
on that expectation rather than assuming there is some divergence between the providers."*

```
TRUESHARES  divz_holdings.csv    29 rows   Date -> ['8/24/2026']
PATHFINDER  ETF_Holdings.csv    114 rows   Date -> ['08/24/2026']
```
**SAME DAY. SAME NIGHT. THE ONLY DIFFERENCE IS A LEADING ZERO.** He is right: **we manufactured the
divergence at silver.** Every "the issuers have different as-of semantics" framing tonight --
**including mine, amended into the PRD three times** -- described OUR artifact and attributed it to
them. **One `csv.DictReader` over two files I had held for three hours answered it.**

## ⛔ THREE OF MY OWN RULINGS FELL IN THIS WINDOW

**1. THE L1 AS-OF FIX -- REFUSED BY `0.0.0_AB_MSTR~Z`, AND THEY WERE RIGHT.**
I ruled a code change to `etf_daily_pull.py`. They declined loudly rather than not starting.
**The decisive point I never checked: at 11:00Z the local date is ALREADY TUESDAY, so `BDay(-1)` =
Monday 08-24 and THE SCHEDULED RUN IS ALREADY CORRECT.** The bug manifests only before local
midnight -- **which is exactly and only what our ad-hoc attempt did.**
>> **THE DEFECT WAS IN THE WORKAROUND, NOT THE PIPELINE. I diagnosed the instrument we improvised
and prescribed surgery on the one that works.**
And their second point killed the "~2 lines": *newest silver partition* on a Monday is **SUNDAY**
(silver writes weekend partitions), so my rule would have **reintroduced into L1 the very
two-selection-logic defect we spent the night diagnosing.** `0.7.0_AE_CloudOps~Z` found a third trap
independently -- `:68` computes `expected` from the same local clock, so changing `:67` alone makes a
**tautologically dead tripwire** go live and REFUSE, exit 60, nothing written.
**Two independent traps in a "2-line" change within four minutes of the ruling. That is the signal.**

**2. THE ONE-INTEGER ORACLE -- WITHDRAWN, caught by AE~Z and CVO~Z independently.**
I ruled `is_cash_inferred` settles whether SALXX is misclassified into the Equity total. It fails
three ways: **nested at `stats.` so "absent" reads as `0`, THE ALARM VALUE** · **`0` is TRUE BY
CONSTRUCTION on an 08-21 as-of** (a fact I established myself four hours earlier) · **and I had told
Andrew it decides a client-facing number.**
⛔ **At 00:14Z I wrote *"a COUNT CANNOT DISCRIMINATE those; the oracle is the rows"* about a
different field. Ninety minutes later I reached for a counter anyway.**
**REPLACED: read SALXX's `asset_class` FROM THE GOLD HOLDING ROWS.** Two rows expected, so `0 of 2`
and `2 of 2` are distinguishable from each other AND from a partition that never had them.

**3. THE COPY SHORTCUT -- evaluated and refused on a SPECIFIC ground, not on principle.**
`s3 cp` of the 170-row characteristics from `bbg/2026-08-21/` to `bbg/2026-08-24/` would unblock in
seconds, and **the "is the claim true?" test PASSES on the parquet** (pulled 20:49 EDT on 08-24,
after that close, over the 08-24 universe). **It fails on the MANIFEST: `"as_of": "2026-08-21"` is
INTERNAL, so the copy ships a self-inconsistent artifact -- key says 08-24, body says 08-21.**

## THE DELIVERY PATH, SETTLED AND CODE-FREE

```
04:00Z  local midnight -> the UNMODIFIED pull writes bbg/2026-08-24/    (FREE OPTION, ~04:15Z)
11:00Z  scheduled L1 writes the same key                                 (CERTAIN)
13:00Z  gold selects 08-24 -> all four books fill                        -> Andrew ~13:15Z
```
**Verified on the TO-5 face: the 04:00Z boundary was tested "across four instants with both
wrong-side controls firing."** ⚠ **The 04:00Z run is an OPTION whose miss costs NOTHING** -- so it
lives on the TO face and I deliberately did NOT chase it onto `org/XXX.md`. **Durability requirements
scale with the cost of the miss; over-applying that is the same error in the other direction.**

## ⭐ AND THE ONE GENUINE UNKNOWN IS CLOSED, IN OUR FAVOUR

MSTR~Z's ad-hoc pull -- despite landing under the wrong key -- produced the answer nobody had:
```
bbg/2026-08-21/characteristics.parquet   170 rows (was 109)
  BBSEY · AMX · CPA · BNPQY   ALL TOKEN-MATCHED   (AAPL positive control)
```
**A5 WORKS. THE ADRs RESOLVE. The 11:00Z pre-check is discharged early and PASSES**, and DS~Z's
*"full-looking books with blank analytics"* scenario -- worse than tonight's honest shells --
**cannot happen.**

## THE THREE REPORTABLES, each restated so the wrong reading cannot satisfy them

```
1. universe_count      RECONCILES to ~166        (not "> 109": a partial extension passes a >)
2. BBSEY / AMX         TOKEN-matched             (not bare-string: `security` holds "AAPL US Equity")
3. SALXX asset_class   READ FROM THE GOLD ROWS   (not stats.is_cash_inferred: nested + 0-by-construction)
```
**Each took a separate correction from a separate seat, and every one arrived because someone checked
the INSTRUMENT instead of the answer.**

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| raw aws + csv.DictReader | both providers' bronze Date, same night | **`8/24/2026` and `08/24/2026` -- NO divergence** |
| aws s3 cp + pandas | the 170-row characteristics, token-match | all four ADRs resolve |
| comp-find | as-of resolution sites; `infer_is_cash`; manifest nesting | `:66`/`:68` local clock; the oracle's three failures |
| directives-check / to-check | scope + completion | NOT DONE 0 of 2 |

## Blockers

None at this seat. **Zero cards at Andrew.** Outstanding: the item-2 returns measurement (held card,
durable in `ETFS_POSITIONING.json`) · the gold row-level as-of cell · the L1 as-of fix as **tomorrow's**
cell with three named constraints · two `[??]` TO faces.
