# DATA_PLATFORM D1 — DS field-modeling consult (input to 0.6.0's Schwab field spec)

**Role:** DS field-modeling consult to DATA_PLATFORM.D1 (lead 0.6.0_AE_PartnerETL; verify 3.0.0_SA_CVO).
**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-24 · **For:** 0.6.0 to fold into the D1 spec.
**Grounded against (not memory — Rule 22):** the `/49-schwab-conv` canonical process + `build_schwab_bd_account_xref.py` + `comp-grep "schwab/silver" data/black_diamond/scripts/gold` (the live gold consumers) + live `aws s3 ls` of `opal-data-bd/schwab/silver/`, `opal-data-schwab/silver/`, and `opal-data-schwab/01_raw/`. DATA_DICTIONARY.md read for field-grain.

> Answers 0.6.0's 3 asks + the converter-canonicality bonus. Two findings correct common assumptions — called out inline.

---

## Ask 1 — Silver-path reality (the RPS-empty + bucket split)

**The split is RESOLVED in practice — unified to `opal-data-bd` (2026-05-12 "SCHWAB-BUCKDR"); the `opal-data-schwab` silver is the dead vestige.**

- **LIVE canonical schwab silver = `s3://opal-data-bd/schwab/silver/{acc,rps,trn_nna,uln,ult,rld}/date=YYYYMMDD/data.parquet`.** Confirmed live: `rps/` has `date=20260617/`, `date=20260618/`. This is what `/49-schwab-conv` writes and what every B_0x/A_03 gold script reads.
- **`s3://opal-data-schwab/silver/` is the OLD/dead location** — live `ls` shows `PRE ACC/ TRN/ ULN/ scripts/` and **NO `RPS/` at all.** So the PRD's "canonical silver/RPS EMPTY" = the OLD `opal-data-schwab` canonical (RPS absent/dead), NOT the live path. `gold_freshness_config.yaml:54` records the incident verbatim: a freshness check ran "against `opal-data-schwab/silver/RPS/` while B_00 read stale canonical" — which is exactly why the 2026-05-12 unify moved everything to `opal-data-bd/schwab/silver/`.
- **Recommendation for D1:** document `opal-data-schwab/silver/*` as a **retire-candidate vestige** (raw + bronze/rps stay in `opal-data-schwab`; all silver is `opal-data-bd/schwab`). The "bucket-lineage split" is a doc-drift artifact, not a live data gap.

**Gold consumers per schwab silver table (comp-grep-grounded):**

| Silver table (`opal-data-bd/schwab/silver/`) | Gold consumer(s) | Role |
|---|---|---|
| `rps/` | A_03.positions_cube (`quantity_settled` = ground truth), B_00.canonical_holdings (custodial snapshots), B_01.holdings_lots | the positions/AUA snapshot |
| `uln/` | B_02.canonical_lots | unrealized lots |
| `ult/` | (gold_freshness_config + lib/s3_layout) | unrealized-lot-tax (a 6th table — see Ask 2) |
| `rld/` | B_02.canonical_lots | **realized lots — PRIMARY realized-tax source** (B_02 silently falls back to BD's own realized if RLD missing — no error) |
| `trn_nna/` | lib/schwab_flows.py ("Layer B AE canonical") | NNA flows enrichment — **note: consumed as `trn_nna`, NOT `trn/`** (see bonus) |
| `acc/` | build_schwab_bd_account_xref.py | the BD↔Schwab join (Ask 3) |

---

## Ask 2 — Capture-vs-available (live 01_raw enumeration)

**The gap is BIGGER than the dictionary's 5 types — 17 raw extensions delivered, 6 captured, 11 uncaptured.**

Live `s3://opal-data-schwab/01_raw/` carries **17 SI2 extensions:** `ACC, RPS, TRN, ULN, ULT, RLD, RLU, RLW, RLY, RTU, RTY, SEC, TCF, TCFX, TNN, UPN, UPT`.

| Cohort | Extensions | Notes |
|---|---|---|
| **CAPTURED to silver (6)** | ACC, RPS, TRN(→`trn_nna`), ULN, ULT, RLD | the `/49-schwab-conv` 6-step rolls these (ACC/RPS/TRN/ULN/RLD per the skill; **ULT is also a live silver table** per gold_freshness_config + lib/s3_layout — correct the "5 tables" framing to 6) |
| **UNCAPTURED (11)** | SEC, TCF, TCFX, TNN, UPN, UPT, RLU, RLW, RLY, RTU, RTY | the full-feed richness we do NOT ingest |
| of which, HIGH-VALUE uncaptured | **SEC** (securities-master: CUSIP/ISIN/SEDOL, ratings, FI/option detail) | SEC is the security dimension that would let us join positions→security-master ourselves instead of relying on BD |

> **CORRECTION (0.6.0 raw-header ground-truth, 2026-06-24):** TCF/TCFX are **trade confirmations** (raw H1 feed-ids `CONFIRM`/`CONFRMX`: trade/settle/action/qty/price + full commission+fee breakdown), **NOT tax/cash-flow** — the Nov-2025 DATA_DICTIONARY.md mislabeled TCF and this consult initially inherited that label. Grounding-vs-raw-header beats grounding-vs-doc. SEC=securities-master stands. (Tax-lot/distribution detail lives in ULN/ULT/RLD + the BD tax templates, not TCF.)

**DATA_DICTIONARY.md v1.0 is incomplete on BOTH axes** (a D1 doc-gap to close): it documents `ACC/RPS/TRN/SEC/TCF` — i.e. it documents SEC+TCF (which we DON'T capture) but **omits ULN/ULT/RLD (which we DO capture)** and the other 6 uncaptured extensions (RLU/RLW/RLY/RTU/RTY/TNN/UPN/UPT/TCFX). D1's field-spec should document all 17 at field-grain, tagged captured/uncaptured.

---

## Ask 3 — Join model (grounded from build_schwab_bd_account_xref.py + the silver tables)

**BD ↔ Schwab account join (the cross-firm bridge):**
- **Key:** Schwab `ACC.account_id` (10-char zero-padded) → normalize `acct10 = lstrip('0')` **==** BD `original_account_number` (also `lstrip('0')`). Outer join, one row per account in either side.
- **Status enum:** `bd+schwab` (direct match) / `bd_only` / `schwab_bd_fuzzy` / `schwab_only`.
- **Fallback:** for Schwab-only accounts, fuzzy taxpayer-last-name match (`schwab taxpayer_last_name` vs BD `client_name` token) → `fuzzy_last_name`, else `schwab_only_unassigned`.
- **Sources:** Schwab `silver/acc/` (latest) + BD `silver/transactions/` (90-day lookback, for architect/relationship attribution). Output → `opal-data-bd/schwab/silver/account_xref/date=…/data.parquet`.

**Within-Schwab grain + joins (from DATA_DICTIONARY referential integrity + the silver tables):**
- **account** (`ACC.account_id`) → **position** (`RPS`, grain = account × CUSIP × business_date; `RPS.account_number` FK→ACC).
- **position → security** by **CUSIP** (`RPS.CUSIP` → `SEC.CUSIP`) — **but SEC is UNCAPTURED**, so today the security-master enrichment is a GAP (we carry RPS's inline `ticker`/`security_description` only; no ratings/ISIN/FI-detail). A self-owned platform that captures SEC closes this.
- **account + CUSIP → tax lot** (`RLD` realized / `ULN`+`ULT` unrealized; grain = account × CUSIP × lot, with open-date/unit-cost/quantity).

---

## Bonus — canonical vs legacy converters (the one item needing a joint 5-min trace)

- **RPS: `convert_schwab_rps_to_parquet.py` is CANONICAL** → `schwab/silver/rps/` (what the skill runs + every gold rps-reader points at `schwab/silver/rps/`). `convert_schwab_rps_to_silver.py` = legacy (no live gold consumer of a distinct path found).
- **TRN: needs a joint confirm — do NOT assume.** Gold consumes **`trn_nna`** (`lib/schwab_flows.py`, "Layer B AE canonical") = the output of `convert_schwab_trn_to_nna_silver.py` (the `_nna` one). But the `/49-schwab-conv` recurring step runs `convert_schwab_trn_to_parquet.py` → `silver/trn/`. So either `trn/` is an **intermediate** that `_to_nna_silver` reads to produce the consumed `trn_nna`, or they're parallel and `trn/` is vestigial. **I haven't read both converters' I/O — flagging rather than asserting (Rule 22).** A 5-min read of the two `convert_schwab_trn_*` headers resolves it; recommend we do it together so the D1 spec states the TRN lineage correctly (this is exactly the canonical-vs-legacy ambiguity you flagged).

---

## Suggested D1 spec structure (DS view; your call as lead)

1. The 17-extension feed catalog at field-grain (per DATA_DICTIONARY + the uncaptured-extension headers), tagged captured/uncaptured.
2. The 6 live silver tables (`opal-data-bd/schwab/silver/*`) — grain, fields kept-vs-dropped, the gold consumer of each.
3. The capture-vs-available gap (the 11 uncaptured; SEC/TCF as the high-value targets).
4. The join model (BD↔Schwab acct10 + the within-Schwab account/position/security/lot grain; the SEC-uncaptured security-master gap).
5. Ingest-automation scoping (your lane: manual SI2-desktop-pull → programmatic/multi-firm; the `opal-data-schwab` SSE-deny + AE-owned constraint).
6. The `opal-data-schwab/silver` vestige retire-note.

I'll fill #1-4 (field-modeling) against your draft skeleton, and verify the TRN-lineage item with you. Ping when your draft section lands.
