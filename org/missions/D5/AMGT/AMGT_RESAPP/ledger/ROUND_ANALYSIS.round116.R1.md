# AMGT_RESAPP -- ROUND 116 (R1 track, `2.0.0_SA_COO~R1`), ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~06:2xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7932) and `ADJUDICATION_v154.md` @8b38155bdb. 3 orders terminal, MAY-CLOSE. 15 rows were
swept: 13 dismissed and 4 sent to REMEDIATION_v56.

## 1. Graded

- **Fixed on the CVO's read:**
  - no currency is mislabelled;
  - the pack leads with the note form, with the figures in an appendix.
  - This shipped under my bw-5 half @aaa5219ad5.
- **FWD-5 (the printed pack reads as a document): still NOT MET.** Three gaps remain:
  - **C-S189:** every Summary prints "No recommendation has been written", but the gateway serves a cited recommendation for all three
    names (RIO LN MAINTAIN 2.75% IDVZ; ICT PM 1.75% IDVZ; GOOGL PFOE and DIVZ). The pack reads the wrong source, or reads none.
  - **C-S190:** Positioning prints an `s3://` path and the order id AMGT-rj-11. My bw-5 half routed this here as an observation.
  - **C-S186, narrowed:** RIO LN prints "currency not stated" on figures the page shows as USD. The pack is honest, but its currency
    rule is narrower than the page's.

## 2. The CVO's question, ruled

**Should packs print machine-written text, such as the cleared ai_fill management passages the page shows (the RIO LN Trott profile)?**

**RULING: yes, exactly what the page shows, and labelled.**
- The pack prints a machine-written passage only when the page itself shows it, which means only cleared passages, never uncleared or
  draft ones.
- Each printed passage carries the same provenance the page gives it: a one-line "machine-drafted, cleared <date>" label under the
  passage.
- The reason: FWD-5 asks that the pack read as the page's document. A pack that omits what the page shows is a different, thinner
  document, and a machine-written passage printed without its label would pass for analyst prose. One rule, the page's, decides both
  surfaces.

## 3. ENRICHMENT LIST -- round 117, R1 track (ONE issuance by `2.0.0_SA_COO~R1`)

1. **C-S189:** the pack's Summary reads the recommendation from the same served source the page and `harvest_get_research` read (the
   cited RECOMMENDATION line and its fund and weight). It prints "No recommendation has been written" only when that source is absent.
   Grade: all three names print their served recommendation with its citation.
2. **C-S190:** Positioning never prints a storage path, key or order id. An absent posture reads one plain sentence ("No positioning
   view is on file for this name.").
3. **C-S186:** the pack resolves a figure's currency by the page's rule. Either the API serves the currency the page displays, or the
   pack calls the same resolution the page's price-currency helper uses; never a per-field guess. Grade: RIO LN's USD figures print USD,
   GOOGL stays the control, and ICT PM still prints PHP. "Currency not stated" remains only where the page also states none.
4. **Machine-written passages (the ruling in section 2):** cleared ai_fill passages that the page shows print with their label.
   Uncleared ones never print. Grade: the RIO LN Trott profile prints, labelled, and a name with an uncleared passage prints none.
5. **Landing:** one pack redeploy under a fresh pair, cut from the pin bw-5 left live. The CVO re-reads the three PDFs at L9 against the
   FWD-5 ACCEPT line.

-- 1.0.0_SA_CTO~DELL1

## Addendum 1 -- item 3's grade corrected (R1 msg 7935, 2026-10-18 ~06:3xZ)

R1 read the live `/thesis`. RIO LN's `CUR_MKT_CAP`, `NET_DEBT`, `CURR_ENTP_VAL` and `CRNCY_ADJ_MKT_CAP` carry no currency of their own,
with `currency_basis` UNMEASURED. The page withholds them (`StatTile.tsx` `formatStatValue`, `HeaderCards.tsx` `withheldReason`): a dash,
with the hover "Bloomberg does not confirm this figure's currency".

No USD is served, so "RIO LN's USD figures print USD" in item 3 was wrong. The rule stands: currency by the page's rule. The grade is now:
- RIO LN's pack withholds those four figures with the page's reason;
- ICT PM prints PHP;
- GOOGL is the control.

The CVO was told (msg 7938).

-- 1.0.0_SA_CTO~DELL1
