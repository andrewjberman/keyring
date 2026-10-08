# L1 BRIEF -- Strategy identification into the Global aggregate: every Opal SMA and Opal ETF found at intake and counted once

- **Author:** `4.0.0_SA_CRO~DELL1` (L1), 2026-10-08 ~18:5xZ. **Mode:** NEW. The scope is new; the territory it
  lands in (the Global aggregate) belongs to `MDPF_GLOBAL`, whose placement is the CTO's call (Part II).
- **Order:** Andrew-direct 2026-10-08 ~18:3xZ at the `1.0.0_SA_CTO~DELL1` terminal, recorded @4672605201 in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_183xZ_COT_SMA_ADDITIVE_TO_GLOBAL_AND_STRATEGY_IDENTIFICATION_SYSTEM.md`.
  Asked of this seat by `1.0.0_SA_CTO~DELL1` msg 1045. Verbatim:

  > "Regarding the Cottonwood SMA dollars, that should be additive because those are outside of the Models. Beyond
  > that, we need to figure out how to set up identification where when SMA Strategies (Tax or Muni for ALT thus far),
  > and all the Opal ETFs for ETF Strategies, we need to make sure we have a system that gets those identified and sent
  > over for counting in the global aggregate."

- **Consumer:** `1.0.0_SA_CTO~DELL1`, `/endpoint --forward` at L2. The L2 DONE WHEN goes to Andrew to confirm.
- **Words used here.** "Global" = the Global Aggregate view in Model Portfolios (served from
  `opal-data-assets/portal/gold/mdpf/global/`). "A strategy" = an Opal SMA (Tax, Muni, PFDE, PFOE, DIVZ, IDVZ or any
  later one) or an Opal ETF. "Identified" = a holding is tagged with the strategy it belongs to. "Counted" = its dollars
  appear in Global under the right bucket, once.

---

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1):** Andrew opens the Global Aggregate view for the default window and sees Cottonwood's
PFDE SMA dollars under ETF Strategies, the same dollars Cottonwood's own view shows, and Global's total is higher by
exactly that amount. One firm (Cottonwood), one strategy (PFDE), one served view. It exercises every hop the system
needs: a sleeve identified at intake, a basis applied, the dollars sent to Global, and the bucket shown.

### O1 -- Andrew sees Cottonwood's SMA dollars in Global, added on top of its Model dollars
The basis question that the Cottonwood slice left open is ruled ADDITIVE ("outside of the Models"). Andrew reads a
Global figure that includes Cottonwood's SMA sleeves and can trace each one to the same sleeve in Cottonwood's view.

### O2 -- Andrew sees Muni under ALT Strategies, at Cottonwood and at Global
A Muni sleeve or account that exists today is shown as Muni SMA under ALT Strategies, not inside Custom.

### O3 -- A new Opal SMA reaches Global without anyone editing code
Andrew's list is "thus far". When a new Opal SMA appears at a custodian or in a rebalancer, it is tagged and counted
in Global by the next scheduled run, or it is shown as an unidentified strategy candidate that a person can name. It
is never silently left in Custom or Non-Model.

### O4 -- A new Opal ETF reaches ETF Strategies without anyone editing code
"All the Opal ETFs". When Opal launches an ETF, its holdings at every firm are counted under ETF Strategies from the
first run after one list is updated, not after seven files are edited.

### O5 -- Andrew can see that nothing is counted twice
For any strategy dollar in Global, a reader can answer "is this also inside a Model figure?" from the served view or
its record. The Tax fold's overlap control (a Cottonwood Tax account that carries a Model assignment is withheld) is
the pattern every additive strategy follows.

### O6 -- A person can see what the system could not identify
Every holding or sleeve that looks like an Opal strategy but matched no rule is listed by name and dollars, with the
firm, so a gap is a visible row and not a figure absorbed into Custom or Non-Model.

---

## PART II -- WHERE THE BOUNDARY SITS

**Owns:** the identification of Opal SMA strategies and Opal ETFs across firms; the per-strategy basis (additive or
carve-out) as applied to Global; the sending of identified dollars into Global's fold; the unidentified list (O6).

**Relies on, does not own:**
- `MDPF_GLOBAL` (owner `1.0.0_SA_CTO`, laptop): the Global view, its segment taxonomy and its fold. This work feeds
  it. Whether this becomes a workstream of `MDPF_GLOBAL` (its WS-1 "ETF and SMA segment roster" is `not_started`) or a
  new project is the CTO's call at L3.
- `MDPF_TAXSMA`: the Tax SMA sources and fold (`data/mdpf/scripts/gold/taxsma_sources.py`,
  `mdpf_gold_consolidator.apply_taxsma_overlay`). Tax already reaches Global. This work does not rebuild it; it
  generalises its pattern.
- `MDPF_SECCLASS`: the one security-classification table (DynamoDB `etf-classifications`). What a SECURITY is lives
  there. Whether a holding is part of an Opal STRATEGY is a different axis, but L2 should state whether the Opal ETF
  list (O4) lives in that table.
- `ETFS_SETUP` (lane `0.4.0_DS_ClientPlatform`): `s3://opal-data-etfs/config/etf_universe.json`, the runtime list of
  Opal ETFs for the ETF ownership producers.
- `MDPF_HEALGAP`: the Cottonwood rebalancer ingest's re-run behaviour. A sleeve never ingested cannot be identified.
- `WSE_COTMDL` / the Cottonwood slice (`data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`): Cottonwood's
  per-firm view. Its per-firm numbers do not move under this work. Only Global changes.

**Out of scope:** per-advisor views; frontend work (Global is backend-served); reclassifying an Opal Model as an SMA.

---

## PART III -- THE QUALITATIVE BAR

1. Andrew reads a Global strategy figure he would otherwise have built by adding Cottonwood's SMA tiles to Global by
   hand.
2. When a strategy is missing from Global, the reason is on a served or recorded row (unidentified, withheld for
   overlap, or no dollars), never in an absence.
3. Adding a strategy is a data change a non-engineer can make, or none at all. It is never a commit that has to
   touch several files together.
4. No Global figure moves except by the dollars of identified strategies. Per-firm views are unchanged.

---

## PART IV -- THE SUBSTRATE: is this in a canonical pattern?

Findings, each measured at this seat 2026-10-08 ~18:4xZ unless marked as the CTO record's.

- **F1 -- The SMA identification is a fixed regex tuple with four rules.** `OPAL_SMA_NAME_RULES`
  (`data/assets/scripts/silver/rebalancer_schemas.py:218-223`): DIVZ, IDVZ, PFDE (or "Pathfinder Disciplined"), PFOE
  (or "Pathfinder Focused Opportunit"). There is no Muni rule and no Tax rule. Its design is right for the purpose
  (one shared rule, whole-word matching, raises when two rules match one name). Its weakness is that a new strategy
  requires a code edit.
- **F2 -- The registry already declares Muni and Tax, each with a basis.** `SMA_MEMBERS`
  (`data/mdpf/scripts/gold/mdpf_category_registry.py:343-368`): six members. `muni` is "ALT Strategies", basis
  `carve_out`, marked UNVERIFIED ("Verify before its first dollar"). `tax` is the one `additive` member. `divz`/`pfoe`
  are verified carve-outs; `idvz`/`pfde` are declared carve-out, unverified. **The basis is one value per member, not
  per member per firm.** Andrew's ruling makes Cottonwood's SMA dollars additive at Global while 49financial's
  divz/pfoe are verified carve-outs of that firm's model population. A single per-member value cannot hold both
  (Rule 24 iv, state coherence). L2 must place this.
- **F3 -- Global's model set is a fixed tuple, and a missing key has already cost real dollars.** `GLOBAL_MODEL_KEYS`
  (`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:158-159`). The comment at `:133-157` records the
  2026-08-26 fire (Fixed Income absent from Global, composition gate refused at -$8,442,396.92) and the "three files,
  one commit" rule that followed. That rule is a discipline, not a mechanism. O3 and O4 retire it for strategies.
- **F4 -- Cottonwood's SMA sleeves are held out of Global on purpose.**
  `build_cottonwood_mdpf_slice.py:348-357`: "Global gains Cottonwood's SMA sleeves only under a ruled basis for that
  mix." That basis is now ruled (O1).
- **F5 -- The Opal ETF list exists in eight places.** One runtime config
  (`s3://opal-data-etfs/config/etf_universe.json`, `tickers` = DIVZ, IDVZ, PFDE, PFOE, LastModified 2026-06-23,
  description: "append its ticker ... no redeploy") and seven hard-coded copies with the same four tickers:
  `mdpf_aggregate_aua.py:83`, `build_mdpf_wsd2_etf_netassets_feeder.py:61`, `build_mdpf_wsc_inflection_feeder.py:80`,
  `feeders/wsd_partner_held_etf.py:78`, `feeders/wsc_inflection_held_etf.py:103`, `feeders/wsb_49f_smartx_model_aua.py:62`,
  and `data/etfs/scripts/gold/avgcap_bd_rps_recon.py:42`. **Prior art for O4: the config already exists and is
  read at runtime by the ETFS producers. The MDPF side does not read it.**
- **F6 -- The additive pattern with an overlap control exists and is tested.** `apply_taxsma_overlay`
  (`mdpf_gold_consolidator.py:1648`): Cottonwood's Tax is added to Global, and a date whose Cottonwood Tax account
  carries a Model assignment is withheld. Test: `data/mdpf/tests/taxsma/test_taxsma_cot_global_fold.py`. The overlap
  key source is `taxsma_sources.blackdiamond_model_assigned_keys`. O1 and O5 extend this pattern; they do not need a
  new one.
- **F7 (CTO record) -- Muni is not reached today.** Opal_Muni_Sleeve ($550,823.07) is a Custom model, and
  Opal_Muni_Income ($64,119,753.85, 1 account, `auto_classified`) sits in the Custom catch-all. The record marks the
  second figure "to verify". It is large enough that a misclassification would move Global materially either way.

**Canonical-pattern verdict:** identification by name at intake (F1) and additive with an overlap control (F6) are
both the estate's established shapes. What is NOT canonical is that both lists (SMA rules, Opal ETFs) are code. For
the ETF list, the estate's own answer, a runtime config, already exists (F5).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- A per-firm (or per-population) basis for each SMA member, or a ruling that the basis axis stays per-member with
  Cottonwood handled as its own member population (F2).
- An overlap key for every additive strategy at every firm. Today only Tax has one (F6).
- One home for the Opal ETF list that the MDPF producers read (F5). Whether that is `etf_universe.json` or the
  `MDPF_SECCLASS` table is a choice, not a precondition.
- The Opal_Muni_Income account verified as Opal Muni before its dollars move (F7).
- Cottonwood sleeves ingested on schedule (`MDPF_HEALGAP`).
- Any new by_model key reaching Global without the three-file edit (F3), or the edit made by the system.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Status ages; nothing here is an outcome.

- Served 2026-10-07 (CTO record): PFDE shows at Cottonwood under ETF Strategies ($412,892.63) and is absent at Global.
  Cottonwood's DIVZ is absent from Global. Muni SMA is absent at both levels.
- Measured 2026-10-08 ~18:4xZ (this seat): `etf_universe.json` carries 4 tickers, LastModified 2026-06-23T15:54:47Z.
  `OPAL_SMA_NAME_RULES` carries 4 rules. `SMA_MEMBERS` carries 6 members, 3 with a verified basis.
- Tax SMA reaches Global for 49financial and Cottonwood through the Tax fold (code read; served values not
  re-measured here).

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **Not measured:** the served Global and Cottonwood artifacts. Every served dollar figure is the CTO record's
  2026-10-07 read, not re-read.
- **Not verified:** Opal_Muni_Income's $64.1M. Whether it is an Opal Muni SMA, a mislabel or a different product is
  open.
- **Open reading of the words, for L2 and Andrew:** "all the Opal ETFs for ETF Strategies" can mean (a) Opal ETFs
  held in SMA sleeves only, or (b) every direct holding of an Opal ETF at every firm. Under (b), Opal ETFs held inside
  Opal Models are already in Model dollars and must not be counted again (O5). This brief does not choose between
  them.
- **Not checked:** whether firms other than 49financial, Inflection and Cottonwood hold Opal SMAs or Opal ETFs. "Across
  firms" is taken at its widest. The Global population's firm set is `MDPF_GLOBAL`'s.
- **Not read:** `MDPF_GLOBAL`'s and `MDPF_SECCLASS`'s open task orders. Overlap with WS-1 is named, not measured.
- **Not specified:** the identification mechanism. A runtime list, a classification-table column or rules at intake
  are all admissible. That is PRD territory.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/mdpf-strategy-identification-into-global-brief-20261008.md
  PROJECT           NONE-YET (CTO's call: MDPF_GLOBAL workstream -- WS-1 -- or a new code)
  EXISTING PRD      docs/architecture/MDPF_GLOBAL_PRD.md (the territory's PRD; not this scope's)
  SIBLING PROJECTS  MDPF_GLOBAL, MDPF_TAXSMA, MDPF_SECCLASS, ETFS_SETUP, MDPF_HEALGAP, WSE_COTMDL
  PRIOR ART         rebalancer_schemas.OPAL_SMA_NAME_RULES; mdpf_category_registry.SMA_MEMBERS + SMA basis axis;
                    mdpf_gold_consolidator.apply_taxsma_overlay + test_taxsma_cot_global_fold.py;
                    s3://opal-data-etfs/config/etf_universe.json; dim_mdpf_aggregate_aua_timeseries.GLOBAL_MODEL_KEYS
  ORDER             org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_183xZ_COT_SMA_ADDITIVE_TO_GLOBAL_AND_STRATEGY_IDENTIFICATION_SYSTEM.md @4672605201
  MEASURED AT       code + etf_universe.json: 2026-10-08 ~18:4xZ (this seat); served figures: 2026-10-07 (CTO record)
```
