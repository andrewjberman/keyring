# AMGT_RESAPP ROUND 64 -- L8 COMPILE + L9 -- windows, markers, labels, repairs and the cold read confirmed on the deployed function; FWD-38 (b) title case NOT met (60 of 94 names all-caps); L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-03 ~16:5xZ
**Input:** `2.0.0_SA_COO~Z`'s `round64/DRAIN_END_PACKET.md` @`3e7d3ab309` (4,691 B, read to EOF), msgs 28881 and 28882 (the nudge).
- **7 of 7 orders are terminal.** Every drained commit is an ancestor of HEAD: `37da943651`, `43711514cc`, `f43c05b00e`, `6892710005`,
  `40e52072ce`, `f5a29aef96`, `130c3be101`, `bf4b04b120`, `9b94636a21`, `d510a04e6f`.
- **This compile is late.** The packet arrived at 02:06Z; this seat's session stalled on a usage limit until ~16:29Z.

## 1. The deployed function, read by this seat

`opal-amgt-scoped-api`, CodeSha256 `KQSA62c3...`, LastModified 01:52:29Z, 1,769 MB. Read-only invokes, ~16:3xZ.

| check | this seat's read |
|---|---|
| c9 chatter windows | default = 30; 30 / 90 / 365 serve 95 rows with `window_start` 2026-09-03 / 07-05 / 01-01, ending 2026-10-02. The 365-day window notes "the store begins 2026-01-01, after the requested start 2025-10-03". Tone is null with its `tone_reason` |
| c10 price windows | trending and breakout: 30 = 94 rows; 90 and 365 = 0 rows, "the 90- and 365-day price windows are not produced yet: they need a longer price-history pull, which waits on Andrew's w[ord]". That is the QUALIFIED WAIT's interim branch, **not a read of the 90/365 price path** |
| c11 markers | BA: 1 `coverage_event` marker ("Boeing Delivers 51 Jets in August, Lowest in Four Months", 2026-09-08). `marker_kinds_absent`: earnings_release, "no earnings dates are pulled yet" (the QUALIFIED WAIT's interim branch) |
| c13 move labels | each price row names `movement_measure` WINDOW_RETURN_PCT, `window_days` 30, `axis` TRENDING_PRICE |
| c14 repairs | **The officer face (DSGN Z-C-S41, producer half) is fixed.** ASML's `source_item` reads "Bloomberg officer list (no filing roster could be read)", and `COMPANY_EXEC_OFFICERS` survives only in the machine field `fallback.field`. BP/ LN serves Energy, with `classification_key_basis` naming the slash-free row. NG/ LN serves null with "the classification row for NG cannot be confirmed as this company: the table's row carries no name to match", a true reason. The encoded key `BP%2F_LN_Equity` answers 200 on thesis, peers, overlay and timeline (4 of 4) |
| c15 cold read | this seat's reads were WARM (no Init Duration): BA `/timeline/day` 0.41 s, 0.24 s, 0.24 s. The COLD pass (3 of 3 at 1.9-2.3 s with Init Duration) is AE~A's deployed measurement; this seat cannot force a cold start without a configuration act it does not own. Accepted on that record |
| c16 500 attribution | not re-run: it needs a planted fault on the deployed function, not this seat's act. Accepted on the issuer's planted read-back |
| **c12 one display name** | **YES on "one per security", NOT on FWD-38 (b)'s "in title case"**: see section 2 |

## 2. FWD-38 (b): title case is NOT met

PRD v0.35 FWD-38 (b): "every route serves ONE display name per security, in title case, with no share-class code (SAUX-29)". Served
`display_name`:
- **price ranking:** 60 of 94 all-caps ("SYNOPSYS INC", "CADENCE DESIGN SYS INC", "TOKYO ELECTRON LTD", "LENOVO GROUP LTD");
- **chatter:** 61 of 95 all-caps ("AIA GROUP LTD", "HON HAI PRECISION INDUSTRY").

One name is also cut at its source: "MITSUBISHI UFJ FINANCIAL GRO".

The issuer's row Z-W212-S1 names the mechanism: "the one display-name rule strips share-class codes but does not re-case". c12 grades
one name per security and not its case. So FWD-38 (b) needs a re-case, with a guard for acronyms such as "BP PLC", and a source for
the full name where Bloomberg's field is cut.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| Z-W211-S1, Z-W214-S1 | DISMISSED_WITH_REASON | the pre-existing harvest test failures, repaired @`949b24cadb` |
| Z-W215-S1 | DISMISSED_WITH_REASON | the worker branch held the pre-amendment check; re-graded on the shared tree |
| Z-S339 | DISMISSED_WITH_REASON | resolved by an-6: BP served Energy with its key basis; NG null with a true reason (read above) |
| **Z-W212-S1** | **GRADUATED** (Z-C-S450) | FWD-38 (b) title case not met (section 2) |
| Z-W214-S2, Z-W212-S2 | **GRADUATED** (Z-C-S451) | enrichment: identity resolution is the largest remaining cold stage (~0.85-0.93 s); the feed's `url` is null because gold carries none (round 65) |

## 4. L10 PRECONDITION -- and an instrument defect that misreads it

7 of 7 orders are terminal. Every BLOCKING or ARMED row is dispositioned on the record. **comp-surprise nonetheless reads Z-S279
(BLOCKING ARMED) and Z-W158-S1 (ARMED) as UNDER_INVESTIGATION**, though v75 dispositioned both (Z-C-S446 DISMISSED, Z-C-S447
GRADUATED). The cause:
- `.tools/comp-surprise.py:77` folds every document in sorted PATH order, and `adjudications/` sorts before `investigations/`.
- The issuer's investigation rows Z-S282 and Z-S276 carry `adjudicates` for those two ids with their own disposition
  UNDER_INVESTIGATION.
- `:215-220` writes the folding row's disposition onto the target, so the investigation rows win.

This is v53's FINDING 1, still live. A census over every project reads **40 of 3,886** CVO-terminal targets overridden this way, in
AMGT_RESAPP, NFRA_MCPINDEX, NFRA_OPSEC202609, POSN_ASTTAX and others. It is the tool owner's (`1.0.0_SA_CTO`) to fix: fold
investigation rows' `adjudicates` only when their own disposition is terminal, or fold CVO adjudications last. **The precondition is MET
on the record**, and the instrument's two-row disagreement is named here.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S449",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T16:41:00Z",
    "one_line": "Round 64 L8 on the deployed function (KQSA62c3, 1769 MB): c9 windows 30/90/365 with the store-start note and tone held, c10 price 90/365 the qualified-wait interim branch, c11 a coverage marker plus earnings absent with its reason, c13 every move labelled, c14 the officer face in reader words (raw code only in fallback.field), BP Energy, NG a true null, the encoded key 4 of 4 -- all confirmed by this seat; c15 cold and c16 accepted on their deployed records (warm reads 0.24-0.41 s); Z-W211-S1, Z-W214-S1, Z-W215-S1, Z-S339 closed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "opal-amgt-scoped-api CodeSha256 KQSA62c3, LastModified 2026-10-03T01:52:29Z: /lead-panel/timeseries/collected/chatter ?days=30|90|365, /lead-panel/rankings/{trending,breakout}/price ?days=30|90|365, /security/BA_US_Equity/timeline, /security/ASML_NA_Equity/thesis, /security/BP%2F_LN_Equity/{thesis,peers,overlay,timeline}, read ~16:3xZ.",
        "git merge-base --is-ancestor on the 10 drained commits -> all true."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W211-S1",
      "AMGT_RESAPP-Z-W214-S1",
      "AMGT_RESAPP-Z-W215-S1",
      "AMGT_RESAPP-Z-S339"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W211-S1 and Z-W214-S1 repaired at 949b24cadb; Z-W215-S1 re-graded on the shared tree; Z-S339 resolved by an-6 and read served.",
    "spec_asserts": "Round 64's cells serve their checks on the deployed function.",
    "world_is": "Confirmed, with FWD-38 (b) title case the exception (Z-C-S450).",
    "notes": "L10 precondition MET on the record; comp-surprise's misread of Z-S279 / Z-W158-S1 is the fold-order defect named in section 4."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S450",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T16:41:00Z",
    "one_line": "FWD-38 (b) 'one display name per security, in title case' is NOT met on the deployed function: 60 of 94 price-ranking and 61 of 95 chatter display_name values are all-caps (SYNOPSYS INC, TOKYO ELECTRON LTD, AIA GROUP LTD), and one is cut at source (MITSUBISHI UFJ FINANCIAL GRO); the display-name rule strips share-class codes but does not re-case, and c12 grades one name per security, not its case.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "/lead-panel/rankings/trending/price display_name: 60 of 94 equal their own .upper() (letters > 3); /lead-panel/timeseries/collected/chatter display_name: 61 of 95.",
        "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W212-S1 (the rule strips codes, does not re-case).",
        "AMGT_RESAPP PRD v0.35 FWD-38 DONE WHEN (b)."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W212-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-38 (b): one display name per security, in title case.",
    "world_is": "Roughly two thirds of served names are all-caps; one is truncated.",
    "notes": "FOR THE CTO: a re-case cell (with an acronym guard, e.g. 'BP PLC') and a full-name source where Bloomberg's field is cut."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S451",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T16:41:00Z",
    "one_line": "Enrichment for the round-64 analysis: identity resolution is now the largest remaining cold stage of BA /timeline/day (~0.85-0.93 s, Z-W214-S2), and the overlay feed serves url null because gold article_security_mention carries no url (Z-W212-S2; DSGN round 30 renders a plain title; a url source is a round-65 item).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W214-S2 and #AMGT_RESAPP-Z-W212-S2.",
        "round64/DRAIN_END_PACKET.md @3e7d3ab309 section 'For the CVO' item 3."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W214-S2",
      "AMGT_RESAPP-Z-W212-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The cold read stays well inside 5 s; a feed item links to its article.",
    "world_is": "Both met for now or carried with an owner.",
    "notes": "Neither blocks a round-64 outcome."
  }
]
```

-- 3.0.0_SA_CVO~Z
