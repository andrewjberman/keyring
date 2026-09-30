# DSGN_AMGTV1 ROUND 9 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~04:2xZ
**Input:** `2.0.0_SA_COO~D`'s `round9/ROUND9_CLOSE_WALK.md` @`e196b68`, msg 26904. The packet was read to EOF (5,503 B).
**Walk H:** `tmp/ui-walk/20260930T040420Z/` (157 shots). This seat read PNGs `005` and `115`.
**L7 re-measured, not adopted:** `AV-p-1`..`AV-p-4` all read `complete` on their LAST `<status>` tag. There are three judgments; p-4 is
Andrew-direct DIRECT-ACT, with no L9.

---

## 1. L9 -- THREE JUDGMENTS

| criterion | verdict | what the page shows |
|---|---|---|
| **p-1 AC3** (each classification column's heading names what its values are; "Sector" is not read as Positioning's "Sub Asset"; no value cut short, FWD-2) | **MET** | `005`: the columns are headed "Asset Class" / "Sector", over "Equity" (now capitalised as on Positioning) and "Energy", "Information Technology", "Utilities", "Consumer Staples". "Communication Services" wraps onto two lines, whole. The note reads "Not served for this list yet: Industry group (finer than Sector), places moved since the last run." The grain mismatch this seat named in v10 is resolved by heading the column by its own grain. BP/ LN's "--" is the unserved-name ask, carried at AMGT_RESAPP. |
| **p-2 AC3** (a PM sees on each row why the rows run in their order; each row's time reads like every other time on the page, HARVST FWD-5, FWD-11) | **MET, one residual** | `115`: "A wsj named 8 times August 13th, 2026, 12:55a ET" above "A sa named 5 times August 13th, 2026, 10:19a ET". The tier and the count are the served sort key (v10: tier, then `mention_count` DESC), and both are now on the face, so the order explains itself. The times are converted correctly: 04:55Z = 12:55a EDT and 14:19Z = 10:19a EDT. There is no ISO and no "(instant)". **Residual:** the same panel still prints ISO elsewhere. The heading reads "2026-08-13'S ARTICLES", the tooltip reads "2026-08-13: not searched ...", and the event links read "2026-02-12, 2 articles". So "reads like every other time on the page" is true of the rows against the footers, not of the panel as a whole. That is the packet's section "Seen on the walk" item 1. |
| **p-3 AC3** (the lead footer reads like every other footer; the line about an older list reads as plain words, FWD-11) | **MET** | `005`: "September 28th, 2026 \| Source: ranked from Bloomberg prices (32 names); requested for September 30th, 2026". The lone "Dated" prefix is gone. The line below reads "This list is from September 28th, 2026, the newest available." That is plain, and it replaces the system-sounding line v10 named. There is no time because none is served (ruling 4). |

**p-4 (DIRECT-ACT, not graded):** in the signed-in shots, the Security Analysis icon, highlighted on this route, sits in the lower
(Tools) group (`005`, `115`). That agrees with the packet.

## 2. L8 -- THE CHANNEL COMPILE

`_latest_dispositions('.', 'DSGN_AMGTV1')` returns **21 items: 16 GRADUATED, 1 DISMISSED_WITH_REASON, 4 UNDER_INVESTIGATION**
(11 files). All 4 open rows are INERT notes (`Z-W8-S1`, `Z-W5-S1`, `Z-S2`, `Z-W11-S1`). **No BLOCKING or ARMED row is open in this
channel.** Round 9 added no row.

## 3. FOR THE ROUND-9 ANALYSIS

1. **FWD-11's remaining ISO dates** (packet item 1) are now the page's main date-form gap. They appear on the day heading, the
   tooltip, the event links, the axis, "identity as of", "Posture (as of ...)", the movement windows and "Updated". Round 5's v-6
   made ISO the page's own form. Rounds 7-9 moved footers and rows to the reference pages' long form. **The CTO should rule the one
   house form for the whole page.** Today it is split, and each round fixes one surface.
2. The queued items: the six outcomes' page render with whose-case labels past Base (AMGT_CORPUS v23 section 2), and never print
   K/M/B/T on an UNRESOLVED unit.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 4 of 4. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** none is open. **MET**
3. **Every judgment criterion graded:** 3 of 3 MET (p-2 with one residual). **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S12",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T04:20:00Z",
    "one_line": "L9 round 9 on walk H: p-1, p-2, p-3 all MET -- 'Asset Class'/'Sector' headed by grain with nothing truncated; each day row shows 'named N times' so the order explains itself, with times in the long form correctly converted (04:55Z = 12:55a ET); the lead footer and its note in plain words; residual: the panel still prints ISO dates (heading, tooltip, event links, axis).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AV-p-1..AV-p-4 read 'complete' on their LAST <status> tag.",
        "Shot 005: headers 'Asset Class' / 'Sector'; 'Equity'; 'Communication Services' on two lines; note 'Not served for this list yet: Industry group (finer than Sector), places moved since the last run.'; footer 'September 28th, 2026 | Source: ranked from Bloomberg prices (32 names); requested for September 30th, 2026'; 'This list is from September 28th, 2026, the newest available.'",
        "Shot 115: 'A wsj named 8 times August 13th, 2026, 12:55a ET'; 'A sa named 5 times August 13th, 2026, 10:19a ET'; heading '2026-08-13'S ARTICLES, STRONGEST FIRST'; events '... -- 2026-02-12, 2 articles'.",
        "L8: _latest_dispositions('.', 'DSGN_AMGTV1') 21 items (16 GRADUATED, 1 DISMISSED_WITH_REASON, 4 UNDER_INVESTIGATION, all INERT), 11 files."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The close walk @e196b68 asserts 4 orders terminal, walk H VALID, and per-criterion observations for p-1..p-3.",
    "world_is": "True as read. Every round-8 residual this seat named is fixed; the page's remaining FWD-11 gap is a split date form across surfaces.",
    "notes": "FOR THE ROUND-9 ANALYSIS: rule one house date form for the whole page (ISO vs the reference pages' long form); the six outcomes' page render with whose-case labels past Base."
  }
]
```
