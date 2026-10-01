# DSGN_AMGTV1 ROUND 11 -- L8 COMPILE + L9 (n-1..n-6 AC4)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~09:4xZ
**Input:** `2.0.0_SA_COO~D`'s `round11/ROUND11_CLOSE_WALK.md` @`44844e4895`, msg 27060. The packet was read to EOF (6,347 B).
**Walk graded:** K, `tmp/ui-walk/20260930T085822Z/` (432 shots). This seat opened shots 163, 249, 294, 336 and 393 itself, and
read the served routes behind n-3, n-5 and n-6.
**L7 re-measured:** `AV-n-1`..`AV-n-6` read `complete` on their LAST `<status>` tag. There are 6 judgment criteria.

---

## 1. L9 VERDICTS

| criterion | verdict | grounds |
|---|---|---|
| n-1 AC4: a reader who stops early reads "unit not resolved", never an amount (TSM header) | **MET** | Shot 294: "Enterprise value unit not resolved -- raw figure 71,993,494.73 (TWD)". The qualifier leads and the digits are labelled raw, which closes v12's boundary 2.1. |
| n-2 AC4: a PM tells filing evidence from the team's pack and reads which evidence is absent (IMB Posture) | **MET** | Shot 249 heads "FILING EVIDENCE, EACH SIDE" and reads "IMB LN (subject): no filing evidence is carried for this name yet." The team's position keeps "Source: Imperial Brands Research Pack 2026 07 17_v1". Neither "pack" nor "on this object" remains, which closes v12's boundary 2.3. |
| n-3 AC4: the page no longer contradicts itself, and a PM reads how articles on an unsearched day were found (992 HK's opened days) | **PARTIAL** | Details below. |
| n-4 AC4: the no-dossier name is shot loaded and shows the served reason (6501 JP) | **MET** | Shot 336 shows 6501 JP's header and Thesis loaded, reading "The research team's thesis pillars: no research dossier for this name." That is distinct from 992 HK's "none are stated in the research team's pack" (163), where a dossier exists. This closes v12's o-2 unexercised arm. |
| n-5 AC4: an analyst returning can say what moved AND NAME THE EARLIER VERSION that shows it (BA Model) | **NOT MET** | Details below. |
| n-6 AC4: per input, where it came from, when it last ran, whether it worked, and that a lone re-run is unavailable (BA Model) | **MET** | Details below. |

**n-3 in detail:**
- **Met on BA 2026-09-08** (shot 393). The served state is DENIED with covered `[]`, and the page reads "NOT SEARCHED FOR THIS COMPANY
  DIRECTLY -- 5 ARTICLES FOUND IN OTHER SEARCHES". The page is truthful and consistent.
- **Not met on 992 HK 2026-08-13**, the day the order names (shot 163).
  - The served day is PARTIAL with `publishers_covered_codes` `[bbg]` and 2 articles, whose shown publishers are **wsj** and
    **sa**.
  - The page reads "Searched: a publisher this page has no name for yet -- 2 found".
  - It credits bbg's search with two articles that bbg's listing did not find, and it cannot name bbg.
  - A PM does not learn how those two articles were found. This is the found-only case of `C-HV-COVERED-VS-FOUND` (HARVST PRD
    v0.4, signed @`624bc0f4ca` today). There, wsj and sa should read as "found, listing not run".

**n-5 in detail:**
- What moved is readable: "212 figures added, 0 removed, 7 changed, 172 unchanged", with seven lines.
- The earlier version is **not nameable**. The page says "from the earlier version of September 10th, 2026", and the served
  `/versions` for BA lists **four** versions on that date (`20260910T224432Z`, `...225428Z`, `...231417Z`, `...232018Z`). The
  picker offers four identical "September 10th, 2026" options, and 25th, 24th and 19th are doubled too.
- An analyst cannot say which version shows the change, so the criterion's second arm fails.
- **Remedy (presentation only):** label each version with its time as well, for example "September 10th, 2026, 10:44 pm UTC". The
  stamp is already served.

**n-6 in detail:**
- Shot 393 reads "Market data: Bloomberg; last ran September 25th, 2026 and worked". The other five inputs read as not set up or
  not run, and "Re-running one input on its own is not available on this page yet."
- This seat tested the one way the line could be false. Versions of September 26, 29 and 30 exist with moved figures, so market
  data might have run after September 25.
  - The served `/ledger` reads the market-data `latest` stamp `20260925T042544Z`, outcome OK.
  - Every later `model_block` object this seat opened (`20260925T043907Z`, `...200034Z`, `20260929T024521Z`, `20260930T083927Z`)
    carries `raw_stamp_used` `20260925T042544Z`.
  - The later versions are re-derives from the same pull, so the line is true.

## 2. INPUTS FOR THE ROUND-11 ANALYSIS

1. **The literal FWD-13 string is on the page.** BA's What-moved reads "Market cap: 161867780096.00003 to 155544819936". DSGN FWD-13's
   ACCEPT (v0.4) is "No 161867780096.00003 anywhere". It also shows "Enterprise value: 193510.78009600003 to ...", "Beta:
   1.350954532623291 to ...", and Opal's rule line "-0.8280000000000001". FWD-13 enters at round 12, and this is its first
   target.
2. **The publisher name map cannot name bbg** ("a publisher this page has no name for yet"), and the What-moved list cannot name
   SHORT_INT_RATIO.
3. **The comparable line on IMB Posture reads "... (comparable): no filing evidence is carried for this name yet".** "For this
   name" on the comparable side reads as the subject.
4. The zero-citation footer ("0 of the 0 citations ...") and 6501's "No chatter_daily rows exist for this security_key yet" are
   carried as FWD-11 wording items.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S1` (ARMED: FWD-1 hop 6 on Valero) | **CARRIED** | unchanged since v12 |
| `Z-C-S13` (v12: o-2's no-dossier arm unexercised) | **GRADUATED** | n-4 exercises it: 6501 JP (0 dossier objects) is shot loaded, and its Thesis reads "no research dossier for this name" (336) |
| other rows | **CARRIED** as the packet's section "Channel" reads them | no worker rows this round (W40-W44: 0) |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 6 of 6. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** the packet reads every ARMED/BLOCKING latest disposition as terminal, and `Z-S1` is
   carried. **MET**
3. **Every judgment criterion graded:** 6 of 6 (n-1, n-2, n-4 and n-6 MET; n-3 PARTIAL; n-5 NOT MET). **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S14",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T09:40:00Z",
    "one_line": "L9 round 11 on walk K: n-1, n-2, n-4, n-6 AC4 MET; n-3 PARTIAL (BA 09-08 reads right; 992 HK 08-13, covered [bbg], credits 2 wsj/sa articles to an unnamed searched publisher); n-5 NOT MET (the 'earlier version of September 10th' names 4 served versions; picker labels repeat).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AV-n-1..n-6 read 'complete' on their LAST <status> tag.",
        "Walk K shots opened by this seat: 294 TSM header, 249 IMB Posture, 336 6501 JP Thesis, 163 992 HK 2026-08-13, 393 BA Model (versions, what moved, where each input came from).",
        "Lambda invoke /api/scoped/amgt/security/992_HK_Equity/timeline 2026-08-13: PARTIAL, publishers_covered_codes ['bbg'], articles_total 2; BA_US_Equity 2026-09-08: DENIED, covered [], articles_total 5.",
        "Lambda invoke /api/scoped/amgt/security/BA_US_Equity/versions: 14 versions, 4 stamped 20260910 (224432Z, 225428Z, 231417Z, 232018Z).",
        "Lambda invoke /api/scoped/amgt/security/BA_US_Equity/ledger: market_data latest 20260925T042544Z OK; S3 model_block 20260925T043907Z/200034Z, 20260929T024521Z, 20260930T083927Z raw_stamp_used 20260925T042544Z."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-C-S13"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "AV-n-3 AC4: on 992 HK's opened days the page no longer contradicts itself and a PM reads how articles were found; AV-n-5 AC4: an analyst can name the earlier version that shows what moved.",
    "world_is": "992 HK 08-13's partial-day line attributes two found-only articles (wsj, sa) to the one searched publisher, which it cannot name; BA's earlier version label 'September 10th, 2026' is shared by four served versions.",
    "notes": "FOR THE ROUND-11 ANALYSIS: add the time to version labels (stamp already served); render found-only publishers as 'found, listing not run' per C-HV-COVERED-VS-FOUND and name bbg; FWD-13's literal 161867780096.00003 is on BA's What-moved (round-12 target)."
  }
]
```
