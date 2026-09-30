# DSGN_AMGTV1 ROUND 10 -- L8 COMPILE + L9 (o-1..o-4 AC3)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~07:2xZ
**Input:** `2.0.0_SA_COO~D`'s `round10/ROUND10_CLOSE_WALK.md` @`34427cf77c`, msg 27000. The packet was read to EOF (6,042 B).
**Walk graded:** J, `tmp/ui-walk/20260930T063347Z/` (242 shots, site Z). This seat opened these shots itself: 084, 117, 118, 147,
152, 169, 192, 204 and 020.
**L7 re-measured:** `AV-o-1`..`AV-o-4` read `complete` on their LAST `<status>` tag. There are 4 judgment criteria.

---

## 1. L9 VERDICTS

| criterion | verdict | grounds |
|---|---|---|
| o-1 AC3 (FWD-11): every date reads like the reference pages | **MET** | Every date on the shots opened is in the house form: "September 29th, 2026", "January 1st, 2026", "SEPTEMBER 1ST, 2026 TO SEPTEMBER 30TH, 2026", "Updated September 30th, 2026", "February 12th, 2026, 11:28a ET" (117), "August 13th, 2026 to August 14th, 2026" (117), "the 20-F filed February 26th, 2026" (084), "Snapshot: drafted by a machine on September 16th, 2026" (169). |
| o-2 AC3 (CORPUS FWD-10/11/15/16/18) | **NOT MET** | Details below. |
| o-3 AC3 (CORPUS FWD-12): AZN's Model tab | **MET** | Shot 192: "THE RESEARCH TEAM'S BASE / UPSIDE / DOWNSIDE CASE", each with "SOURCE: THE RESEARCH TEAM'S PACK, ASTRAZENECA RESEARCH PACK 2026 06 17_V1". Beneath them are three lines, each opening "Opal's", and the historical-multiple line reads once, correctly (the 0x08 repair). There is no "not in the pack" line beside any team case. |
| o-4 AC3 (RESAPP FWD-30): a planted header beside a measured one | **MET** | TSM (204): "Enterprise value TWD 71,993,494.73 (unit not resolved)". There is no K/M/B/T, the digits are raw, and the qualifier is inside the same card. The measured control AZN (192/194) reads "USD 281B". An unresolved figure is not dressed as a scaled amount. |

**o-2 AC3 in detail:**
- **The team's arms: met.**
  - IMB's Thesis (147) shows six pillars, each with "Source: Imperial Brands Research Pack 2026 07 17_v1".
  - IMB's Exec Management (152) heads "THE RESEARCH TEAM ON MANAGEMENT", with its source.
  - IMB's Posture (169) reads "Fund of record: IDVZ; last stated position: Potential ADD in IDVZ (currently ~2.5%). Source: Imperial
    Brands Research Pack 2026 07 17_v1".
  - Each reads as the team's and traces to its report. TSM (204) and SAP (084) show the same.
- **The arm "a name with no dossier says so" was NOT EXERCISED.**
  - The order names 6501's Thesis tab as the witness. On S3 `opal-data-harvest` `amgt/harvest/gold/research_dossier/`, 287 objects
    were read:
    - **6501 JP has 0 dossier objects;**
    - every other walked name (VLO, INTU, SAP, 992, IMB, AZN, TSM) has 3.
  - 6501 never opened on walk I (only `/peers` was requested). Walk J replaced it with TSM, which has a dossier.
  - So neither walk shows the page for a name that has no dossier. "None are stated in the research team's pack" on VLO (020) and
    992 HK (118) is the different state: a dossier exists and carries no pillars. That is correct, but it is not this arm.
  - ABSENT is not EXERCISED-AGAINST, so the arm is unmet, not met by default.
- **Cheapest remedy:** one signed-in walk that opens a dossier-less name's Thesis tab. 6501 JP needs its search pick fixed, or any
  other name with 0 objects will do.

## 2. BOUNDARIES THE ANALYSIS SHOULD DECIDE (not corrections to the grades)

1. **o-4: the currency prefix reads as a literal amount.**
   - "TWD 71,993,494.73" with grouping and cents reads as about TWD 72 million to a reader who skips the parenthetical.
   - At USD 451 per ADR the enterprise value is of order TWD 72 **trillion**, so the served number is very likely in millions.
   - The figure is not scaled, so AC3 holds. But the literal reading is off by 10^6.
   - Options for the CTO:
     - put the qualifier before the digits ("unit not resolved: 71,993,494.73 TWD"); or
     - drop the cents on an unresolved figure.
2. **o-1:** source titles quote dates as written in the document name ("Research Pack 2026 07 17_v1", "research pack 4_30_2026").
   This seat reads a quoted title as a name, not a page date. If the CTO reads FWD-11 as covering titles, o-1 moves to PARTIAL.
3. **IMB's Posture tab contradicts itself (169).**
   - "EVIDENCE COVERAGE ... IMB LN (subject): no pack for IMB_LN_Equity is carried in packs on this object" sits two lines below the
     position cited to "Imperial Brands Research Pack".
   - The two "packs" are different objects, but a PM cannot tell. This is the packet's FWD-11 item 1, and it is also a
     traceability fault on o-2's own face.
4. **992 HK's timeline (117) says "NOT SEARCHED ON THIS DAY" above two articles on that day.**
   - The articles are "named 9 times" (sa) and "named 7 times" (wsj) on February 12th.
   - Every bar is red (not searched) on a chart that lists coverage events.
   - A day with served articles was searched. The coverage state and the article list disagree, which is a HARVST/timeline
     honesty item.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S5` (ARMED: three 0x08 bytes break "Opal's" and "from Bloomberg") | **GRADUATED** | `Z-S6` repair @CLOUD 4813813e75 / DEV 2bb60cc3. Walk J shot 192 reads "Opal's historical-multiple reference" once and "Company description from Bloomberg" in words, and the header on 147/204 reads the same. AC4 `bytes.cjs` is on the order. |
| `Z-S6` | **GRADUATED** with `Z-S5` | |
| `Z-S1` (ARMED: FWD-1 hop 6 on Valero, team cases ABSENT) | **CARRIED** | VLO (020) reads "THE RESEARCH TEAM'S BASE CASE IS NOT IN THIS PACK", which is the state the row names |
| `Z-S2`..`Z-S4` | **CARRIED**, INERT | |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 4 of 4. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S5` GRADUATED; `Z-S1` CARRIED. **MET**
3. **Every judgment criterion graded:** 4 of 4 (o-1 MET, o-2 NOT MET, o-3 MET, o-4 MET). **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S13",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T07:20:00Z",
    "one_line": "L9 round 10 on walk J: o-1, o-3, o-4 AC3 MET; o-2 AC3 NOT MET -- the team's pillars/management/position read as the team's with sources, but 'a name with no dossier says so' was never exercised: 6501 JP (0 dossier objects of 287) never opened and TSM (3 objects) replaced it; Z-S5 graduates on shot 192.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AV-o-1..o-4 read 'complete' on their LAST <status> tag.",
        "Walk J shots opened by this seat: 192 AZN Model (team base/upside/downside with source; three 'Opal's' rule lines; historical-multiple label once), 204 TSM Thesis ('Enterprise value TWD 71,993,494.73 (unit not resolved)'), 147/152/169 IMB Thesis/Exec Management/Posture (sources 'Imperial Brands Research Pack 2026 07 17_v1'), 084 SAP, 020 VLO, 118/117 992 HK.",
        "S3 opal-data-harvest amgt/harvest/gold/research_dossier/: 287 objects; security_key 6501 = 0 objects; VLO, INTU, SAP, 992, IMB, AZN, TSM = 3 each.",
        "Packet: walk I requested only /security/6501%20JP/peers; walk J substituted TSM US for 6501."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S5",
      "DSGN_AMGTV1-Z-S6"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "AV-o-2 AC3 asks that a name with no dossier says so, witnessed on 6501's Thesis tab, alongside the team's pillars, management view and position reading as the team's.",
    "world_is": "The team's arms read right on IMB, TSM and SAP. No walked page shows a name without a dossier: the only such walked name, 6501 JP, was never opened, so that arm is unexercised and graded unmet.",
    "notes": "FOR THE ROUND-10 ANALYSIS: re-walk a dossier-less name (6501 JP or any 0-object key); o-4 literal-reading boundary (TWD 71,993,494.73 reads as ~72 million, true order ~72 trillion); IMB Posture 'no pack for IMB_LN_Equity' beside a cited IMB pack; 992 HK 'NOT SEARCHED ON THIS DAY' above two served articles."
  }
]
```
