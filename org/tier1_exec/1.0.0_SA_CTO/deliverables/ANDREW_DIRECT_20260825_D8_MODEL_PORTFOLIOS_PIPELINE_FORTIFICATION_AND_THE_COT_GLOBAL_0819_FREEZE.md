# ANDREW-DIRECT 2026-08-25 ~14:20Z -- D8 RE-MINTED "MODEL PORTFOLIOS PIPELINE FORTIFICATION" + A LIVE SERVED FREEZE AT 2026-08-19

**Recorded by:** `1.0.0_SA_CTO`, CTO terminal, same turn as receipt.
**Class:** sovereign directive creation + a live client-facing outage, measured and confirmed.

## VERBATIM

> **"Another thing that we need to get to the bottom immediately, speaking of directives, is let's
> replace Directive 8 (now crossed out 'Philosophy' job) with 'Model Portfolios Pipeline
> Fortification'. Somewhere along the line, we fucked up cottonwood's model portfolios ingestion (on
> august 20 or so I'd guess) and as a result their model portfolios and Global are now stuck on
> august 19. That needs to get fixed immediately and since we're making a whole directive out of it,
> we should take this as an opportunity to actually make sure that entire pipeline is in pattern,
> because currently I think the Cottonwood code is somewhere different in some different format than
> the code and layout for 49 Financial and Inflection. We need a consistent methodology for this.
> I'm actually not against having the opal-data-mdpf where we keep the code because its very obvious
> where it is, or alternatively we do it all in opal-data-assets/portal/gold/mdpf which is where i
> think 49 and inflection are, but in retrospect I don't think that makes as much sense. The pattern
> that seems to be emerging which I do like is that 'ALL' data ingestion is handled in
> opal-data-assets, this covers both bronze and silver. Gold data (parquet query layer) will be in a
> specific bucket for its purpose, e.g. how we're going to do it for opal-data-49financial, or
> opal-data-mdpf, or opal-data-etfs. THen platinum data (serving) lives in the portal itself
> opal-data-portal-v2."**

And the correction he issued minutes later, which this record exists partly to carry:

> **"the code-shape you are referring to being incongruous is a category error, the scripts youre
> pulling from cot are for advi, they are not the cottonwood mdpf scripts"**

## THE OUTAGE -- MEASURED, CONFIRMED, HIS READ EXACT

**NEVER#1 discharged FIRST:** `expected_last_trading_day(2026-08-25) = 2026-08-25`; a partition at
`2026-08-19` is **FOUR TRADING DAYS** behind. Not a weekend.

```
partner        as_of_last    n_dates   served object LastModified (UTC, s3api)
49financial    2026-08-24      452     2026-08-25T13:50:49Z    CORRECT (T-1)
inflection     2026-08-24      452     2026-08-25T13:50:51Z    CORRECT (T-1)
cottonwood     2026-08-19      458     2026-08-25T13:50:50Z    <<< FROZEN
global         2026-08-19      458     2026-08-25T13:50:50Z    <<< FROZEN
```
Source: `s3://opal-data-portal-v2/platinum/mdpf/{partner}/aggregate-aua-timeseries.json`, field
`as_of_last`, read at 14:2xZ.

### ⛔ WHY NO INSTRUMENT CAUGHT IT -- THE STRUCTURAL FINDING

**THE OBJECTS ARE REWRITTEN EVERY DAY.** All four served keys were written within two seconds of
each other at 13:50:49-51Z today. **The publisher runs, emits, and succeeds. THE STALENESS IS
INSIDE THE PAYLOAD.**

> **Every freshness instrument that reads object mtime reports these HEALTHY -- and is CORRECT
> ABOUT THE FILE.** `comp-freshness`, an `s3 ls` age, a `head-object` LastModified: all green, all
> answering a question about the OBJECT and not about the DATA.

**This is `CONTROLS_OVER_CARE` s.11 at estate scale: a valid retrieval, a claim wider than the
read.** It is the reason a four-trading-day client-facing freeze ran silently while the fabric
spent the morning on a twr defect that had louder symptoms and less consequence.

### TWO PAYLOAD SIGNATURES, for whoever gets the TO -- LEADS, NOT DIAGNOSES

- **cottonwood's `dates` array is almost ENTIRELY `None`** -- hundreds of nulls, a single real value
  (`2026-08-19`) at the end. **That is not a stalled feed; something is emitting a full-length array
  of nulls.**
- **global's tail REPEATS `2026-07-22` roughly fifteen times** before `2026-08-18`, `2026-08-19` --
  a forward-fill / last-value-carried signature. `opal-data-cot` carries a `forwardfill_v2/` prefix.
- **global is a rollup INCLUDING cottonwood**, so one root cause plausibly explains both.
  **Do not treat them as two defects until someone proves they are.**

### INDEPENDENT CORROBORATION, from a different artifact, unprompted

`0.4.0_DS_ClientPlatform~I`, 14:14Z: *"served surface advanced to data_as_of 08-24 (total.aua
479,297,668.97) while D_05 is byte-identical at data_as_of 08-19 -- the AC4 vintage gap WIDENED
2d->5d."* **Same freeze, different artifact, found by a seat looking at something else.**
⛔ **They filed it as an OBSERVATION. It was correct to surface and it did not reach the level a
four-day served freeze warrants -- the signal existed before Andrew reported it.**

## ⛔ MY CATEGORY ERROR, AND WHY IT GOES IN THE RECORD

I told him the Cottonwood MDPF code was *"somewhere different in a different format,"* citing
`data/cot/scripts/gold/` (`A_00.accounts_dimension.py`, `B_00.canonical_holdings.py`) against
`data/mdpf/scripts/gold/` (`mdpf_*.py`, `build_mdpf_*.py`).

**`data/cot/` is Cottonwood's ADVI pipeline. Different PRODUCT. The naming divergence there is
expected and says nothing about MDPF.**

**THE COTTONWOOD MDPF CODE IS IN `data/mdpf/scripts/gold/` WITH EVERY OTHER PARTNER'S:**
```
mdpf_gold_consolidator.py:860          run_cottonwood_family()
mdpf_gold_consolidator.py:92-93        SCOPES = ("49financial","inflection","cottonwood","global")
build_mdpf_spine.py:56                 FIRMS = ("49financial","inflection","cottonwood","global")
dim_mdpf_aggregate_aua_timeseries.py:1915   load_cottonwood_slice()
```
> **He offered a hypothesis; I produced evidence that appeared to confirm it, from the wrong
> directory, and was one message from handing it back as a finding.** A claim that agrees with what
> the requester already suspects is the one that receives the least scrutiny -- **and the requester
> is the last person positioned to catch it, because it is their own hypothesis coming back.**
> **He caught it. I did not.**

**WHAT IS ACTUALLY THERE AND MAY MATTER -- a LEAD, unread:**
`dim_mdpf_account_distribution.py:328  COTTONWOOD_UNITS_KEY = "gold/mdpf_revamp/cottonwood/account_units.json"`
plus `_cottonwood_sidecar()` at :331 -- **a Cottonwood-only sidecar on an `mdpf_revamp/` prefix,
where the served config points at `portal/gold/mdpf/cottonwood/`.** A real special case. **I have
not read it and it is not a diagnosis.**

## THE TARGET ARCHITECTURE HE STATED

| tier | home | note |
|---|---|---|
| **bronze + silver** (ALL ingestion) | `opal-data-assets` | *"ALL data ingestion is handled in opal-data-assets"* |
| **gold** (parquet query layer) | a **purpose-specific bucket** -- `opal-data-49financial`, `opal-data-mdpf`, `opal-data-etfs` | |
| **platinum** (serving) | `opal-data-portal-v2` | *"lives in the portal itself"* |

⛔ **THIS DIVERGES FROM CLAUDE.md RULE 17b AS WRITTEN**, which places bronze+silver+gold all under
`opal-data-assets` and (per the 2026-08-11 amendment) puts product-gold at
`opal-data-assets/portal/gold/{product}/{scope}/`. **His pattern moves GOLD OUT into per-purpose
buckets.**

⛔ **DIRECTION RECORDED; RULE 17b IS *NOT* AMENDED BY THIS RECORD, AND NOTHING MOVES ON IT.** He
framed it as *"the pattern that seems to be emerging which I do like"* and reasoned aloud through
two alternatives before landing there -- **that is a stated architectural direction, and a law-file
amendment plus any migration is a separate act with its own PRD, its own Rule-24 pass, and his
explicit word.** Moving served output is NEVER#3 regardless. **The D8 PRD is where this gets pinned
precisely; this record only fixes what he said.**

## ROUTING

| item | owner | note |
|---|---|---|
| **the 08-19 freeze -- REPAIR** | `2.0.0_SA_COO` to seat | **SEPARATE TO, ahead of fortification.** His words are *"fixed immediately"* AND *"take this as an opportunity"* -- folding the repair into a directive-scale item makes the repair inherit the directive's timeline |
| **D8 re-mint** | `0.0.0_AB_MSTR` | D8 is CUT (`DIRECTIVES_RETIRED.yaml`, emit_log `2026-08-20T20:32:35Z`, frozen title *"Philosophy + benchmark modal live-edit"*). Re-mint with the new title; per his ~14:12Z ruling its projects are tagged to D8 at creation |
| **D8 PRD** | `1.0.0_SA_CTO` | purpose-level, Rule 27 stage 2; carries the target architecture above as a TARGET, not a migration order |
| **decomp** | `2.0.0_SA_COO` | Rule 27 stage 3, before any TO exists |

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `lib/trading_calendar` | `expected_last_trading_day` + `trading_days_behind` | **NEVER#1 discharged FIRST -- 4 trading days, not a weekend** |
| `aws s3api list-objects-v2` (UTC) | served frontier, 4 partners | **objects FRESH at 13:50:49-51Z -- the finding that explains the silence** |
| `aws s3 cp` + json shape scan | `as_of_last` per partner | **the freeze: cot + global at 08-19, 49f + inf at 08-24** |
| `comp-find -i 'cottonwood' data/mdpf/scripts` | the real code home | **257 hits / 57 files -- the category error, falsified** |
| `comp-find -i 'mdpf/cottonwood' data` | served-key producers | the `mdpf_revamp/` sidecar lead |

**What failed:** my code-shape claim (wrong product tree, and it flattered his hypothesis); a
generic JSON walker that returned 0 points for 3 of 4 partners and would have read as "no series"
had I not checked the shapes. **Gap found:** object-mtime freshness is structurally blind to a
payload freeze, and a served key rewritten daily with frozen contents passes every instrument we own.
