# MDPF_STRATID -- strategy identification into the Global aggregate: every Opal ETF Strategy and Opal SMA sleeve found at intake and counted once

```json
{
 "project": "MDPF_STRATID",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.6",
 "step": 4,
 "brief_ref": "docs/briefs/mdpf-strategy-identification-into-global-brief-20261008.md@68aa9dbe9e",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1` (L2-L4), 2026-10-08.
**Brief:** `docs/briefs/mdpf-strategy-identification-into-global-brief-20261008.md` @68aa9dbe9e (`4.0.0_SA_CRO~DELL1`).
**Andrew's words:** at the `1.0.0_SA_CTO~DELL1` terminal.
- ~18:3xZ, VERBATIM (record @4672605201, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_183xZ_COT_SMA_ADDITIVE_TO_GLOBAL_AND_STRATEGY_IDENTIFICATION_SYSTEM.md`):
  "Regarding the Cottonwood SMA dollars, that should be additive because those are outside of the Models. Beyond that, we need to
  figure out how to set up identification where when SMA Strategies (Tax or Muni for ALT thus far), and all the Opal ETFs for ETF
  Strategies, we need to make sure we have a system that gets those identified and sent over for counting in the global aggregate."
- ~20:1xZ, VERBATIM (record @8e4b5037b4, `.../ANDREW_DIRECT_20261008_201xZ_LIQUID_ALTS_TO_ALTERNATIVES_ETF_STRATEGY_SLEEVES_ENDPOINT_CONFIRMED.md`):
  "Opal has "ETF Strategies" in SMA form, whereby Opal manages the SMA itself. What these appear as, is when there is a whole sleeve
  in a clients portfolio named after an Opal ETF, e.g. the PFDE SMA with Cottonwood. What I'm looking for to accomplish here is
  creating a mechanism where as these sleeves appear in SmartX, Rebalancer, and Eclipse (so far) with Opal ETF names (either the
  ticker e.g. DIVZ or the full name Opal Dividend Income) that these get properly aggregated into the SMA Taxonomy category
  underneeath the ETF Strategies drill down." and "3. Confirm as written" (the endpoint below is RATIFIED).
**Placement:** dell1, by laptop `1.0.0_SA_CTO` msg 107101 as `MDPF_GLOBAL` owner: seated when a dell1 COO lane frees; any change to
Global's served output takes the laptop's never-widen pair. COO lane: UNSEATED.
**Sign-off:** `3.0.0_SA_CVO` (dell1) signs the ratified-text half. The brief half is accepted because the CRO wrote the brief.

## ENDPOINT (step 2, /endpoint --forward)

Ratified by Andrew ~20:1xZ ("Confirm as written"), FWD-5 amended in place by his restatement before ratification.

```
FWD-1  Andrew sees Cottonwood's PFDE strategy counted in the Global view
       DONE WHEN  EXERCISED -- Andrew (or someone for him) has opened the Global view after a scheduled run and read it
       ACCEPT     the PFDE figure under ETF Strategies in Global equals the PFDE figure in Cottonwood's own view, and Global's
                  total went up by that amount and nothing else
       SOURCE     brief Part I "Candidate thread (FWD-1)", O1

FWD-2  Every Cottonwood strategy outside its Models is added to Global
       DONE WHEN  EXERCISED -- one scheduled run read
       ACCEPT     each strategy Cottonwood's own view shows outside its Models has a matching amount in Global, in the same group
       SOURCE     brief O1; Andrew "additive because those are outside of the Models"

FWD-3  Muni shows as an ALT strategy, at Cottonwood and at Global
       DONE WHEN  EXERCISED -- a planted Muni SMA sleeve routed on the served bytes (the mechanism), and one
                  scheduled run read (the organic case, today "no Muni SMA dollars")
       ACCEPT     Muni dollars sit under ALT Strategies, not under custom models; the large single Muni Income account was checked
                  by a person and either confirmed as Opal Muni or kept out with the reason written down, before any of it counted
       SOURCE     brief O2, F7

FWD-4  A new Opal strategy reaches Global with no engineer involved
       DONE WHEN  EXERCISED -- shown on purpose, not waited for
       ACCEPT     a strategy the system has never seen is introduced, and on the next run it is either counted in the right group
                  or listed by name for a person to place; nobody edits a program to make either happen
       SOURCE     brief O3; Andrew "Tax or Muni for ALT thus far"

FWD-5  Every Opal ETF Strategy sleeve is counted under ETF Strategies, wherever it appears
       DONE WHEN  EXERCISED -- shown on purpose
       ACCEPT     a client sleeve named after an Opal ETF, by its ticker or its full fund name, is found in SmartX, Rebalancer and
                  Eclipse alike and shows in the SMA group under the ETF Strategies drill-down; adding a new Opal ETF to the one
                  list is the only step for its sleeves to be found the same way
       SOURCE     brief O4, F5; Andrew restatement ~20:1xZ

FWD-6  Nothing in Global is counted twice, and a person can see why
       DONE WHEN  EXERCISED -- shown on purpose
       ACCEPT     for any strategy amount in Global, a person can tell whether it is also inside a Model figure; an account set up
                  to sit in both is held out once and named as held out
       SOURCE     brief O5, F6

FWD-7  What the system could not identify is visible, never absorbed
       DONE WHEN  EXERCISED -- one scheduled run read
       ACCEPT     anything that looks like an Opal strategy but matched nothing is listed with its firm, its name and its dollars,
                  instead of disappearing into a catch-all or into Non-Model
       SOURCE     brief O6
```

`FWD-1` is the thread: one firm (Cottonwood), one strategy (PFDE), one served view, through every hop (sleeve identified at intake,
basis applied, dollars sent to Global, bucket shown).

## STARTING STATE (measured 2026-10-08, file:line)

- **Three intake surfaces, all present in the repo:**
  - SmartX (49financial): `data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py:62` hard-codes
    `OPAL_ETF_TICKERS = {"DIVZ", "IDVZ", "PFDE", "PFOE"}` and tags `is_opal_etf` per position (`:194`).
  - Rebalancer (Cottonwood): `data/assets/scripts/silver/rebalancer_schemas.py:218-223` `OPAL_SMA_NAME_RULES`, four regex rules
    (DIVZ, IDVZ, PFDE or "Pathfinder Disciplined", PFOE or "Pathfinder Focused Opportunit"), read by `opal_sma_member_of` (:226).
  - Eclipse (Inflection): `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:18` (inflection model = Eclipse) and `:82`
    `ECLIPSE_SILVER = "eclipse/inflection/silver"`. No sleeve-name rule for Opal ETF Strategies exists on this path today.
- **SMA taxonomy:** `data/mdpf/scripts/gold/mdpf_category_registry.py:343-369` `SMA_MEMBERS` (divz, pfoe, muni, tax, idvz, pfde; bucket
  "ETF Strategies" or "ALT Strategies"; one `source_basis` per member). `SMA_BASIS_VERIFIED = ("divz", "pfoe", "tax")` (:375).
- **Global's model set is fixed:** `GLOBAL_MODEL_KEYS` (`dim_mdpf_aggregate_aua_timeseries.py:158-159`).
- **Additive pattern with an overlap control exists:** `apply_taxsma_overlay` (`data/mdpf/scripts/gold/mdpf_gold_consolidator.py:1648`),
  test `data/mdpf/tests/taxsma/test_taxsma_cot_global_fold.py`.
- **Cottonwood SMA sleeves are held out of Global on purpose:** `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:354-357`. The
  basis that comment waits on is now ruled (ADDITIVE).
- **Opal ETF list:** `s3://opal-data-etfs/config/etf_universe.json` (4 tickers, read at runtime by the ETFS producers), plus seven
  hard-coded copies in MDPF/ETFS code (brief F5).
- **Muni:** no Muni rule in `OPAL_SMA_NAME_RULES`. `Opal_Muni_Sleeve` ($550,823.07) is a Custom model; `Opal_Muni_Income`
  ($64,119,753.85, 1 account) sits in Cottonwood's Custom catch-all (served 2026-10-07).

**v0.6 (1.0.0_SA_CTO~DELL1, 2026-10-09 ~18:5xZ), FWD-3's DONE WHEN only (UB-20261009T183753Z-5e37):** rule 27 L2 asks for "a mechanism driven deliberately, the organic case kept as the negative arm". The CRO census found zero Muni SMA dollars at any firm, so the mechanism is proved on a planted sleeve, in the existing seam harness, in memory, with no served write. The organic read stays on the scheduled run. **FWD-3's ACCEPT is UNCHANGED.** `Opal_Muni_Sleeve` ($550,823.07) is KEPT OUT with its reason written down: it is pending Andrew's call 203a, and its dollars already sit inside Cottonwood's Models. His answer moves that sleeve's membership, not this outcome. The ratified-text half re-signs.

## CONTRACTS

**C-BASIS -- basis is per strategy PER FIRM.** The registry's basis axis gains a firm dimension: `(member, firm) -> carve_out | additive`.
Cottonwood's SMA sleeves are ADDITIVE at Global (Andrew ~18:3xZ). 49financial's DIVZ and PFOE stay the VERIFIED carve-outs they are
today. Tax keeps its additive basis at every firm it has today. **Default (v0.3, CVO findings F1 + F3):** the default is set per FIRM, by where that firm's non-model dollars sit, and is declared
once per firm:
- a firm whose non-model dollars are OUTSIDE Global's population (Cottonwood today) defaults to ADDITIVE under C-OVERLAP, because its
  sleeves are outside the Models (Andrew ~18:3xZ);
- a firm whose non-model dollars are already INSIDE Global (49financial today; `mdpf_category_registry.py:343-345`) defaults to
  CARVE-OUT, so a new sleeve there is re-labelled into the ETF Strategies or ALT bucket and never added a second time;
- a firm with no declared population is not counted, and its sleeves are listed (C-UNIDENTIFIED).
A per-`(member, firm)` declaration overrides the firm default. This is what lets a new Opal ETF's sleeve, or an Eclipse sleeve, show in
the SMA group with no engineer (FWD-4, FWD-5) without a double count (FWD-6). An amount the overlap control withholds is listed as
withheld, never dropped silently.

**C-SLEEVE -- what an ETF Strategy is.** An Opal ETF Strategy is a client SLEEVE (a whole model or sub-portfolio in the source system)
whose NAME carries an Opal ETF's ticker as a whole word, or its full fund name. It is identified in all three intake surfaces: SmartX,
Rebalancer and Eclipse. It lands in the SMA taxonomy under the ETF Strategies bucket. Direct holdings of Opal ETF shares inside other
models are NOT strategies and are not counted by this project.

**C-ONE-LIST -- one runtime list of Opal ETFs.** The identifier reads the Opal ETF list (ticker + full fund name per fund) at run time
from ONE place. The prior art is `s3://opal-data-etfs/config/etf_universe.json`. The decomposition chooses whether that file gains a
`full_name` field or another existing home carries it. It does not mint a new address unless `lib/opal_naming.py address()` produces
it (Rule 30). The seven hard-coded copies that decide strategy identity are replaced by reads of that list. Adding a fund to the list
is the only step for its sleeves to be found (FWD-5).

**C-SMA-RULES -- SMA strategies as data.** Non-ETF SMA strategies (Tax, Muni under ALT Strategies; open-ended) are identified by name
rules held as DATA beside the ETF list, not as code. A new SMA strategy is a data row (FWD-4). One shared matcher serves all three
intake surfaces; whole-word matching; two rules matching one name raises (the `opal_sma_member_of` behaviour is kept).

**C-OVERLAP -- counted once.** Every additive `(member, firm)` carries an overlap control generalising `apply_taxsma_overlay`: a
strategy account that also carries a Model assignment on that date is withheld from the additive fold and named as withheld. The
served record states, per strategy amount, whether it is also inside a Model figure (FWD-6).

**C-UNIDENTIFIED -- nothing absorbed.** Each run lists every sleeve that looks like an Opal strategy (name contains "Opal", an Opal
ETF ticker, or a registered strategy token) but matched no rule or has no declared basis, with firm, name and dollars (FWD-7). It is
listed in a served or recorded file the reader can open, never only in a log.

**C-MUNI-VERIFY -- a person checks before Muni counts.** The Cottonwood `Opal_Muni_Income` account ($64.1M, one account) is verified
by a person as Opal Muni, or excluded with the reason recorded, before any Muni dollars count at Global (FWD-3). Until then it stays
where it is and appears on the C-UNIDENTIFIED list.

**C-GLOBAL-PAIR -- served Global moves only under the laptop's pair.** Any act that changes Global's served output
(`opal-data-assets/portal/gold/mdpf/global/`) carries a never-widen pair: the CTO half is signed by laptop `1.0.0_SA_CTO` (MDPF_GLOBAL owner, msg 107101), and the COO half by the
`2.0.0_SA_COO` lane seated on MDPF_STRATID (v0.2, CVO finding F2). `1.0.0_SA_CTO~DELL1` reads each pair before it goes to the laptop. Per-firm views (Cottonwood, 49financial, Inflection) do not move under this project except where a
named outcome requires it (FWD-3 Muni at Cottonwood).

**C-LAYERS -- where the work sits.** Identification happens where each sleeve is first named (silver or the feeder), through the
shared matcher. The fold into Global happens in the existing Global consolidation path. No new pipeline, no shadow output path, no
standing comparator (CLAUDE.md NEVER). The decomposition names the exact files.

## BOUNDARY

**Owns:** identification of Opal ETF Strategy sleeves and Opal SMA strategies across SmartX, Rebalancer and Eclipse; the per-firm basis;
the overlap control for additive strategies; the fold into Global; the unidentified list.
**Relies on, does not own:** `MDPF_GLOBAL` (laptop; the Global view and its taxonomy), `MDPF_TAXSMA` (Tax sources and fold; generalised
here, not rebuilt), `MDPF_SECCLASS` (security classification; a different axis), `ETFS_SETUP` (the Opal ETF universe file),
`MDPF_HEALGAP` (Cottonwood ingest; a sleeve never ingested cannot be identified), `WSE_COTMDL` (Cottonwood's per-firm view).
**Out of scope:** direct Opal ETF share holdings inside models; per-advisor views; frontend work; reclassifying an Opal Model as an SMA.

## OPEN ITEMS (for L5, not blocking admission)

1. **Eclipse sleeve naming.** The Eclipse path names Inflection's model portfolios (`dim_mdpf_aggregate_aua_timeseries.py:82`), but no
   Opal ETF Strategy sleeve has been measured there. Round 1's first cell reads Eclipse's silver for sleeve names carrying an Opal
   ETF ticker or full name and records the census, with the denominator printed. A zero is reported with its denominator, not as
   absence.
2. **Full fund names.** `etf_universe.json` carries tickers only. The full names (e.g. "Opal Dividend Income") must be added from an
   owned source and cited. "Pathfinder Disciplined" / "Pathfinder Focused Opportunit" in `OPAL_SMA_NAME_RULES` are the measured
   prior art for PFDE/PFOE.
3. **Writer census at the fold.** The decomposition counts every writer of Global's ETF Strategies and ALT Strategies figures
   before the first never-widen half (CLAUDE.md NEVER-1).

## SURFACE MANIFEST (step 4 -> step 5)

| id | outcome_ref | surface | claim | verb | bound |
|---|---|---|---|---|---|
| S01 | FWD-5, FWD-4 | one shared matcher (sleeve name -> strategy member) replacing `OPAL_SMA_NAME_RULES` and `OPAL_ETF_TICKERS` as the identity decision | measured (`rebalancer_schemas.py:218-223`; `wsb_49f_smartx_model_aua.py:62`) | build | C-SLEEVE; C-SMA-RULES; whole-word; two hits raise |
| S02 | FWD-5 | the one runtime list of Opal ETFs (ticker + full name) | measured (`etf_universe.json`, 4 tickers, no names) | amend | C-ONE-LIST; no new address without the builder |
| S03 | FWD-4 | SMA strategy name rules as data (Tax, Muni; open-ended) | held | build | C-SMA-RULES |
| S04 | FWD-5 | Eclipse (Inflection) sleeve names carrying an Opal ETF ticker or full name | held (no census yet; open item 1) | read | denominator printed |
| S05 | FWD-1, FWD-2 | the per-firm basis axis in the SMA registry | measured (`mdpf_category_registry.py:343-375`) | amend | C-BASIS; default per firm population (additive outside Global, carve-out inside) |
| S06 | FWD-1, FWD-2, FWD-6 | the additive fold of Cottonwood strategy dollars into Global with an overlap control | measured (`apply_taxsma_overlay`, `mdpf_gold_consolidator.py:1648`; hold-out `build_cottonwood_mdpf_slice.py:354-357`) | wire | C-OVERLAP; C-GLOBAL-PAIR |
| S07 | FWD-3 | the Muni sleeve and the $64.1M `Opal_Muni_Income` account | measured (served 2026-10-07) | read | C-MUNI-VERIFY before any dollar counts |
| S08 | FWD-7 | the per-run list of unidentified strategy candidates (firm, name, dollars) | held | build | C-UNIDENTIFIED |
| S09 | FWD-1 | the served Global and Cottonwood category views after a scheduled run | measured (served 2026-10-07 read) | read | the thread's acceptance read |

## BRIEF COVERAGE

| Brief heading | Carried | Consuming sections |
|---|---|---|
| PART I, thread and O1-O6 | the thread (PFDE at Cottonwood into Global); six outcomes plus FWD-7 split from O6 | ENDPOINT |
| PART II, boundary | owns identification, basis, fold, unidentified list; relies on GLOBAL, TAXSMA, SECCLASS, ETFS_SETUP, HEALGAP, WSE_COTMDL | BOUNDARY |
| PART III, bar | no hand-adding; reason on a row; a data change adds a strategy; per-firm views unchanged | FWD-4, FWD-7, C-SMA-RULES, C-GLOBAL-PAIR |
| PART IV, F1-F7 | fixed regex; per-member basis; fixed model keys; held-out sleeves; ETF list in eight places; Tax overlay; Muni | STARTING STATE; S01-S07 |
| PART V, must be true | per-firm basis; overlap key per additive strategy; one ETF list home; Muni verified; Cottonwood ingested | C-BASIS, C-OVERLAP, C-ONE-LIST, C-MUNI-VERIFY, BOUNDARY |
| PART VII, not claimed | the (a)/(b) reading | settled by Andrew ~20:1xZ (C-SLEEVE) |

## Provenance

GROUNDED ON: the brief @68aa9dbe9e; the ratified endpoint (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_STRATEGY_IDENTIFICATION_INTO_GLOBAL_20261008.md`);
Andrew's records @4672605201 and @8e4b5037b4; code reads at the file:line cited in STARTING STATE (2026-10-08). NOT READ: MDPF_GLOBAL's
and MDPF_TAXSMA's open task orders; the served Eclipse silver; the served Global files (figures are the 2026-10-07 read).

## PRIOR ART TO CARRY

`rebalancer_schemas.OPAL_SMA_NAME_RULES` + `opal_sma_member_of`; `mdpf_category_registry.SMA_MEMBERS` + `SMA_BASIS_VERIFIED`;
`mdpf_gold_consolidator.apply_taxsma_overlay` + `test_taxsma_cot_global_fold.py`; `s3://opal-data-etfs/config/etf_universe.json`;
`dim_mdpf_aggregate_aua_timeseries.GLOBAL_MODEL_KEYS`; `wsb_49f_smartx_model_aua.OPAL_ETF_TICKERS`.

## ADDENDUM v0.4 (1.0.0_SA_CTO~DELL1, 2026-10-09 ~04:4xZ) -- WORKSTREAM 2 opened (S01, S02, S03, S08); fold of UB-20261009T040755Z-d866

The ENDPOINT and CONTRACTS sections are not edited. Source: the CRO's approach (`python .tools/unblock.py show --id UB-20261009T040755Z-d866`).

- **Workstream 2 = S01 shared matcher, S02 one ETF list, S03 SMA rules as data, S08 unidentified list.** Its write surface is the
  matcher, the list and the rules data. It is disjoint from round 1's frozen surface (the S05/S06 fold and the deployed
  `mdpf-gold-lambda` at the pin-148f715f8c build). Rule 27: a workstream is a scope, not a round.
- **Issuer: `2.0.0_SA_COO~S1`, the same lane** (the REC). One project, one issuer. Workstream 2 is its own L5-L6 issuance, cut now,
  beside round 1.
- **GUARD 1, a criterion of EVERY workstream-2 order:** no deploy of `mdpf-gold-lambda`, and no write to the ETF universe config
  (`etf_universe.json` in the ETFS config prefix), before the 2026-10-09 13:30Z FWD-1 read is taken. Merged code does not reach that
  fire; only a deploy would.
- **GUARD 2, inputs:** S01-S03 orders read Track A's measured inputs: the CRO's S04 Eclipse census and S07 read
  (`org/tier1_exec/4.0.0_SA_CRO~DELL1/deliverables/MDPF_STRATID_S07_MUNI_VERIFY_20261009.md` @67e20ee89f). They are not cut against
  held rows.
- **S07 reads UNDETERMINED by data.** `Opal_Muni_Income` ($64,119,753.85, one account) is an Opal Rebalancer model of six third-party
  muni ETFs with SMA flags false. Under C-MUNI-VERIFY a person decides. Until then the S03 Muni rule is DATA with no member, and the
  account stays on the S08 unidentified list. No Muni dollars count. The person's check is listed as an act on this box's open calls.
- FWD-2 and FWD-6 share round 1's write surface and stay sequenced behind the round-1 analysis.

## ADDENDUM v0.5 (1.0.0_SA_CTO~DELL1, 2026-10-09 ~05:3xZ) -- note only: C-MUNI-VERIFY answered for `Opal_Muni_Income`

**Word:** Andrew-direct ~05:3xZ at the `2.0.0_SA_COO~S1` terminal, VERBATIM: "no that is a custom model, we should not be putting that in
ALT Strategies." Record `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/ANDREW_DIRECT_20261009_053xZ_OPAL_MUNI_INCOME_IS_A_CUSTOM_MODEL_NOT_ALT.md`
@07c19a9d0e. ENDPOINT and CONTRACTS are not edited.

- **FWD-3 stands as written.** Its ACCEPT already provides for this result: the large Muni Income account "was checked by a person and
  ... kept out with the reason written down". `Opal_Muni_Income` ($64.1M) stays a Custom model under Cottonwood Models, is excluded from
  ALT Strategies, and leaves the unidentified list as an identified Opal Model.
- **What FWD-3 still needs: the real Muni SMA's dollars.** `Opal_Muni_Sleeve` ($0.55M) was not named in his answer and stays open under
  C-MUNI-VERIFY. The next read is a CRO census of sleeves or accounts named Muni across SmartX, Rebalancer and Eclipse (a read, S07),
  with the denominator printed. If that census finds no Muni SMA dollars at any firm, FWD-3 cannot be EXERCISED. That is then a
  re-entry on this outcome, which this seat raises; FWD-3 is not quietly retired.
