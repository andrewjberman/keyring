# DSGN_AMGTV1 ROUND 8 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~03:1xZ
**Input:** `2.0.0_SA_COO~D`'s `round8/ROUND8_CLOSE_WALK.md` @`8fad06d`, msg 26866. The packet was read to EOF (6,226 B).
**Walk G:** `tmp/ui-walk/20260930T023916Z/` (157 shots, `timeline-days.json`). This seat read PNGs `005`, `115` and `146`.
**L7 re-measured, not adopted:** `AV-q-1`..`AV-q-3` all read `complete` on their LAST `<status>` tag. Three judgments.

---

## 1. L9 -- THREE JUDGMENTS

| criterion | verdict | what the page and the served route show |
|---|---|---|
| **q-1 AC4** (the opened day's shot shows its articles strongest first, not a skeleton; `timeline-days.json` records every opened day's state; HARVST FWD-5/6) | **MET** | **On pixels for the first time:** `115` shows "2026-08-13'S ARTICLES, STRONGEST FIRST", then "NOT SEARCHED ON THIS DAY", then two rows (wsj "Lenovo Posts Record Revenue ...", sa "Lenovo Group jumps on strong Q1 revenue ..."). No skeleton. `timeline-days.json` records all 6 opened days with state and wait: 3 empty at ~1.6-1.9 s, 2 with rows at 5.3 s and 5.6 s, 0 failed, 0 at the ceiling. **"Strongest first" verified on the served order**, since the pixels could not show it. The route sorts by `_dissection_sort_key` = (tier, `mention_count` DESC, earliest time) (`lib/research/harvest/timeline_api.py:132-139`). This seat's reads of `/timeline/day`: **08-13** wsj A mention_count **8**, then sa A **5**; **02-12** sa A **9**, then wsj A **7**. Both days are strongest first. The "opposite time directions" the packet noted is the mention count at work, not disorder. ⚠ **The page does not show `mention_count`**, so a PM sees two identical "A, headline yes, lead yes" rows and cannot tell why one leads. |
| **q-2 AC3** (every footer reads as a date and a source in the reference pages' one form, FWD-11) | **MET, with residuals** | `005` lead line: "Dated September 28th, 2026 \| Source: ranked from Bloomberg prices (32 names); requested for September 30th, 2026". That is the long date form and a source. There is no time because none is served (ruling 4). The header card window (`121`, per the packet) reads "September 28th, 2026, 10:45p ET \| Source: Bloomberg". `146` Positioning reads "September 28th, 2026, 5:00p ET \| Source: Bloomberg." **Residuals:** only the lead line starts with "Dated". The line below it ("this list is older than the date requested, shown as such rather than silently") reads as a system message. The Positioning model window's own footer has no source; that is the reference page's gap, not this page's. |
| **q-3 AC4** (the lead list's classification columns read like the Positioning breakdown; the unserved finer field is not mistaken for the column of sector names, FWD-2) | **PARTIAL** | **Headers: MET.** `005` reads "Asset Class" / "Sub Asset", as `146` does. **The finer field: MET.** "Not served for this list yet: Industry group (finer than Sub Asset), places moved since the last run." **Values: NOT like Positioning.** `146`'s Sub Asset holds Opal's buckets ("Ultra Short Duration", "Short Duration", "High Yield"; equities "Large"). The lead list's Sub Asset holds **sector names** ("Energy", "Information Technology", "Utilities", "Consumer Staples"). Asset Class reads "equity" in lower case against Positioning's "Equity". **The label now matches while the grain does not**: a PM comparing the two pages reads "Energy" and "Large" as values of the same field. One cell is truncated ("Communication Servic..."). |

## 2. L8 -- THE CHANNEL COMPILE

`_latest_dispositions('.', 'DSGN_AMGTV1')` returns **21 items: 15 GRADUATED, 1 DISMISSED_WITH_REASON, 5 UNDER_INVESTIGATION**
(10 files). No new rows came from round 8.

| row | disposition | grounds |
|---|---|---|
| `Z-W4-S1` (ARMED since round 2: does the export follow the page) | **GRADUATED** | Half (a), keyed on data, was served at round 3. Half (b), one served definition, was served by AMGT_RESAPP ww-4. The value arm is AMGT_RESAPP round 50. **This seat's own plants in AMGT_RESAPP ADJUDICATION_v60 are caught on both sides** ("FIGURES(values) differ" for a wrong page text value and for a wrong export value), and the issuer's post-deploy sweep reads 96 of 96 equal on values. The export follows the page on facts and values, with `Z-W176-S1`'s 6 unscaled names as a counted exception in AMGT_RESAPP. |
| `Z-W8-S1`, `Z-W5-S1`, `Z-S2`, `Z-W11-S1` | **CARRIED**, INERT | unchanged |

## 3. FOR THE ROUND-8 ANALYSIS

1. **FWD-2's grain:** serve Opal's sub-asset value for equities (Positioning's "Large"-style bucket), or head the served field
   by its own grain ("Sector"). The label alone now misleads. This is an AMGT_RESAPP producer question.
2. **FWD-5:** show the strength that orders the day (mention count, or a visible rank), so "strongest first" can be read on the
   page, not only in the route.
3. **FWD-11:** the raw ISO article times with "(instant)", the lone "Dated" prefix, and the system-sounding second line.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 3 of 3. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W4-S1` GRADUATED; no ARMED row remains open in this channel. **MET**
3. **Every judgment criterion graded:** 3 of 3. q-1 and q-2 are MET; q-3 is PARTIAL. **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S11",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T03:10:00Z",
    "one_line": "L9 round 8 on walk G: q-1 MET -- the day's articles are on pixels and strongest first is verified on the served order (08-13 wsj 8 > sa 5 mentions; 02-12 sa 9 > wsj 7), though the page never shows the count; q-2 MET with residuals; q-3 PARTIAL -- headers match Positioning but the lead list's 'Sub Asset' holds sector names where Positioning holds size/duration buckets; Z-W4-S1 graduates on AMGT_RESAPP v60's value plants.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AV-q-1..AV-q-3 read 'complete' on their LAST <status> tag.",
        "Shot 115: '2026-08-13'S ARTICLES, STRONGEST FIRST', 'NOT SEARCHED ON THIS DAY', rows wsj 'Lenovo Posts Record Revenue ...' then sa 'Lenovo Group jumps on strong Q1 revenue, AI growth'.",
        "lib/research/harvest/timeline_api.py:132-139 _dissection_sort_key = (tier, -mention_count, published_utc); deployed /timeline/day 992_HK 2026-08-13: wsj A mention_count 8, sa A 5; 2026-02-12: sa A 9, wsj A 7.",
        "Shot 005: headers 'Asset Class' / 'Sub Asset', values 'equity' / 'Energy', 'Information Technology', 'Utilities', 'Consumer Staples'; footer 'Dated September 28th, 2026 | Source: ranked from Bloomberg prices (32 names); requested for September 30th, 2026'. Shot 146: Positioning 'ASSET CLASS' / 'SUB ASSET' values 'Fixed Income' / 'Ultra Short Duration' ... 'Equity' / 'Large'; footers 'September 28th, 2026, 5:00p ET | Source: Bloomberg.'",
        "L8: _latest_dispositions('.', 'DSGN_AMGTV1') 21 items (15 GRADUATED, 1 DISMISSED_WITH_REASON, 5 UNDER_INVESTIGATION), 10 files."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W4-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close walk @8fad06d asserts 3 orders terminal, walk G VALID, and per-criterion observations, noting the two days order their rows in opposite time directions with equal visible marks.",
    "world_is": "True as read. The ordering is strongest first by the served rule (mention count breaks the tie); the page hides the count. The lead list's Sub Asset column is sector-grain under Positioning's bucket-grain heading.",
    "notes": "FOR THE ROUND-8 ANALYSIS: FWD-2 grain (serve the bucket or relabel as Sector); FWD-5 show the ordering strength; FWD-11 raw ISO article times, the lone 'Dated' prefix, the system-sounding line."
  }
]
```
