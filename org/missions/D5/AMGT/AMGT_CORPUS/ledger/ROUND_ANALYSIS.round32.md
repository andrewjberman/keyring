# AMGT_CORPUS -- ROUND 32 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-02 ~16:4xZ

**Input:** CVO slug msg 28578, `surprise-channel/adjudications/ADJUDICATION_v38.md` @4197279 (precondition MET).

## 1. WHAT THE ROUND DELIVERED

- **CRPS-ah-3, served (pair @c216d1a52f + @b859ebff4c).** BA, GOOGL, HEI and PWR BEST_DIV_YLD moved DECIMAL -> PERCENT, with every
  value equal. GOOGL's 3 EQY_DVD_YLD_IND labels moved by name. CVO~Z read the four served blocks from S3. The plausibility check
  holds: GOOGL 0.25 is a 0.25% yield and BA 0.603 is a 0.60% yield, where DECIMAL would have claimed 25% and 60%.
- **Z-S74 is remedied by ah-1 (LOCAL):** `validate.py` and `render_print.py` read UNRESOLVED-ON-/ZERO-DOMINATED units as unmeasured.
- **Round 32 is CLOSED.** It carried no judgment criteria.

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **Z-S81 is the round-33 cell (served label only, with a pair).** The 77 remaining percent-family figures labelled DECIMAL by magnitude alone (RETURN_ON_INV_CAPITAL 20; EQY_DVD_YLD_IND 13; RETURN_ON_ASSET, RETURN_COM_EQY, RETURN_ON_TANGIBLE_ASSETS and OPER_MARGIN 10 each; SI_PERCENT_EQ...) are decided per mnemonic by a GROUND, never by magnitude. <br>- EQY_DVD_YLD_IND: the identity against EQY_DPS / PX_LAST (as ah-2 did for BEST_DIV_YLD). <br>- The returns and the margin: their statement inputs (numerator / denominator), or the series-median rule where a series exists. <br>- **Where no ground exists, the label becomes UNRESOLVED, not DECIMAL.** | The row's spec: a unit is decided by a ground, never by magnitude alone where magnitude cannot discriminate (a 0.2% return and a 0.002 fraction are the same number). |
| 2 | **The act shape copies ah-3.** <br>- A serializing dry run over EVERY key, through the producer's own `stage_derive`. <br>- The per-key map diff, with 0 value, sign or currency moves. <br>- A scoped `--securities ... --remeasure` naming only the affected names. <br>- Negative arms: a figure whose ground confirms DECIMAL stays DECIMAL, and is printed. <br>- The reach beyond the named mnemonics is printed and named in the COO half, as ah-3 named GOOGL. | ah-3 proved the shape on 4 names. A remeasure re-reads every mnemonic of a name, so its reach is measured, never assumed. |
| 3 | **Disarm owner:** `2.0.0_SA_COO~X` (the row's own field). The CTO half is owed here on the dry run. | -- |

## 3. ENRICHMENT LIST (round 33, ONE issuance)

1. Z-S81, per ruling 1 and ruling 2: a ground read per mnemonic, an UNRESOLVED class where none exists, and the serving with its pair.

## 4. CARRIED (each names its act and citation; no decision is listed for Andrew)

- **FWD-20's 49 rows (the V3 pull) and FWD-22's scheduled re-pull** stay on Andrew's word. Each is a Bloomberg pull under the
  budgeted sign-in (`integrations/bloomberg/READ_HERE.md`; round-31 section 3).
