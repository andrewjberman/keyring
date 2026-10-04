# AMGT_RESAPP ROUND 65 -- L8 + L9 JUDGMENT READ of the served display names: FWD-38 (b) PASS; the five all-caps names are acceptable as served; four cosmetic residues named; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-03 ~20:1xZ
**Input:** `2.0.0_SA_COO~Z`'s `round65/DRAIN_END_PACKET.md` @`26bea252e9` (3,897 B, read to EOF), msg 28983. **2 of 2 orders are
terminal** (ao-1, ao-2). The ask is CTO ruling 1: the L9 JUDGMENT read of the served names.

## 1. What was read

- **The list.** `round65/served_names_lPTMo20T.json`: 94 breakout/price names and 95 chatter names, each with its
  `display_name_source`.
- **The live function, by this seat.** `opal-amgt-scoped-api` CodeSha256 `lPTMo20T...`, LastModified 19:47:12Z, 1,769 MB:
  - live names equal the recorded list on both routes (**0 differences**, 94/94 and 95/95);
  - one security carries one name across the two routes (**0 disagreements**).

## 2. The judgment read (as a reader would)

The 95 distinct names read as company names:
- "Advanced Micro Devices Inc", "Taiwan Semiconductor Manufacturing Co Ltd", "Mitsubishi UFJ Financial Group", "Grupo Aeroportuario
  del Centro Norte SAB de CV", "The Home Depot Inc".
- Acronyms are kept where a reader expects them: "ASML Holding NV", "ICICI Bank Ltd", "KDDI Corp", "IDEXX Laboratories Inc",
  "MSCI Inc".
- No name is all-caps outside the declared acronyms. The five cut names are served whole.

**The open question (packet item 1): "BP PLC", "GSK PLC", "RWE AG", "SAP SE", "SSE PLC" -- ACCEPTABLE AS SERVED.** The list's own
convention is upper-case legal forms throughout:
- "AstraZeneca PLC", "HSBC Holdings PLC", "Unilever PLC", "National Grid PLC";
- "Novartis AG", "UBS Group AG";
- "TotalEnergies SE".

The five read the same way, so a reader meets one convention. "plc" would match some companies' own styling, but changing these five
alone would make the list inconsistent. If lower-case "plc" is wanted, it is a list-wide rule, not an exception for five names.

**Cosmetic residues** (not FWD-38 (b) misses, which grades case and share-class codes):
1. "Cadence Design Sys Inc" and "Canadian Natl Railway Co": Bloomberg abbreviations ("Sys", "Natl") a reader must expand.
2. "Michelin (CGDE)": an opaque parenthetical code.
3. "Telefonica Brasil S.A." against "SA" on six names ("Air Liquide SA", "Nestle SA", "Iberdrola SA" ...): one punctuation outlier.
4. **A served string still carries the pre-sweep hold wording.** The chatter route's `tone_reason` is still the string that COO~H's
   `c20fd8cc98` (Andrew-direct ~18:xxZ) replaces. That commit landed after this deploy's pin, so the new string ships at the next
   `opal-amgt-scoped-api` deploy (packet item 3).

**Grade: FWD-38 (b) PASS** on the deployed function.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| Z-W216-S1 | DISMISSED_WITH_REASON | the worker's test-pin edits and share-type tail rule are inside the cell, and the served read above passes |
| Z-S342 | DISMISSED_WITH_REASON | c17 on deployed reads the acronym list at the build commit. This seat's live read (0 differences against the record) closes the gap |
| Z-S341 | **GRADUATED** (Z-C-S453) | the seating lint counts a WITHDRAWN order as open; the lint owner is the CTO |
| Z-S343 | **GRADUATED** (Z-C-S453) | two root-level harvest test files break 10 management tests when collected together. It is pre-existing and an enrichment item |

## 4. L10 PRECONDITION

2 of 2 orders are terminal; the round's rows are OBSERVATION/INERT and dispositioned; the one judgment criterion is graded here.
**MET.**

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S452",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T20:09:00Z",
    "one_line": "Round 65 L9 judgment: FWD-38 (b) PASS on the deployed function (lPTMo20T): the 95 served display names read as company names, live equals the recorded list (0 differences on 94 + 95) with one name per security across routes; 'BP PLC', 'GSK PLC', 'RWE AG', 'SAP SE', 'SSE PLC' are acceptable as served because the list's own convention upper-cases PLC/AG/SE throughout (AstraZeneca PLC, Novartis AG, TotalEnergies SE); cosmetic residues: 'Sys'/'Natl' abbreviations, 'Michelin (CGDE)', one 'S.A.' against six 'SA', and the chatter tone_reason still carrying the pre-sweep hold wording until the next deploy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "round65/served_names_lPTMo20T.json (94 + 95 names) read in full by this seat.",
        "opal-amgt-scoped-api CodeSha256 lPTMo20T (19:47:12Z): live display_name vs the record -- 0 differences on /lead-panel/rankings/breakout/price and /lead-panel/timeseries/collected/chatter; chatter tone_reason still the pre-sweep string that c20fd8cc98 replaces."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W216-S1",
      "AMGT_RESAPP-Z-S342"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W216-S1's edits are inside the cell and the served read passes; Z-S342's build-commit grading is closed by this seat's live comparison (0 differences).",
    "spec_asserts": "FWD-38 (b): one display name per security, in title case, with no share-class code.",
    "world_is": "Met; the declared acronym names follow the list's own legal-form convention.",
    "notes": "FOR THE CTO: grade FWD-38 (b) REALIZED; the four residues are cosmetic, and the tone_reason string rides the next deploy."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S453",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T20:09:00Z",
    "one_line": "Graduated: the seating lint counts a WITHDRAWN order as open (Z-S341, the lint owner is the CTO), and two root-level harvest test files break 10 management tests when collected together (Z-S343, pre-existing).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S341 and #AMGT_RESAPP-Z-S343.",
        "round65/DRAIN_END_PACKET.md @26bea252e9 section 'Rows'."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S341",
      "AMGT_RESAPP-Z-S343"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "A lint counts only open orders; a test suite is order-independent.",
    "world_is": "One lint miscount; one collection-order interference.",
    "notes": "Neither moves a served figure."
  }
]
```

-- 3.0.0_SA_CVO~Z
