# DSGN_AMGTV1 ROUND 14 -- L8 COMPILE + L9 GRADES (AC4 of AV-k-1..k-7)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~05:2xZ
**Input:** `2.0.0_SA_COO~D`'s `round14/ROUND14_CLOSE_WALK.md` @`8a198b327b` (5,997 B, read to EOF), msg 27523.
**L7 re-measured:** AV-k-1..k-7 read `complete` on their LAST `<status>` tag. There are 7 judgment criteria, one AC4 per order.
**Read by this seat:** render run `C:/tmp/dsgn-r14-close-render/` (`exec-error.png`, `standalone-no-permission.png`,
`peers-empty.png`, `model-empty.png`, `posture-cites-open.png` + `.json`); walk N `tmp/ui-walk/20260930T235353Z` shots 016
(BA Thesis), 027 (BA Exec), 059 (BA Posture), 072 (6501 Exec), and `netlog.tsv`.

---

## 1. L9 GRADES

| order | AC4 clause | grade | what this seat read |
|---|---|---|---|
| k-1 | no machine token on BA's header, Exec, Posture, Thesis | **PARTIAL** | Round 13's tokens are gone: no "(IDVZ\|PFOE\|DIVZ)", no "class A", no ALL-CAPS section name. One remains: Posture reason 2 reads "Both names' fit scores are **ABSENT** rather than low" (059; `posture-cites-open.png`). That is served posture text, so the fix is the producer's (C-FRIDAY: a page-side rewrite of a served value is refused). |
| k-2 | what failed, what to do, no response body; this page's object named | **MET** | "Exec Management could not be loaded." / "Try again; if it keeps failing, the feed is down." No brace, quote or body. No-permission: "You do not have access to this security's research. Your firm administrator can grant it." |
| k-3 | a designed empty state a person reads as such | **MET** | "No peer set for this name yet." / "Comparable companies will appear here once a peer set is published." |
| k-4 | nothing asserted beyond the served record; nothing "still loading" at rest | **MET** | BA's Posture footer is settled ("20 of 20 were checked ... were read and are shown where cited"; the render's fixture variant "could not be read" is also settled). 6501's Exec states its served reason. The "M-1" interface code on that face is FWD-11's, carried as `Z-S9`; it is not this clause. |
| k-5 | nothing contradictory on the face | **PARTIAL** | `model-empty.png` reads "No model in the research pack for this name yet. **No figure, case or estimate is shown in its place.**" Three lines below, the same face shows a figure: "Opal's historical-multiple reference: forward EPS (FY1) is **-0.828**, not positive". The history block itself agrees with the empty sentence ("The latest pack holds no model for this name; these figures are from versions it held before."). |
| k-6 | the chart's labels still read; nothing styled off the contract | **MET** | Timeline axis ticks (4.3 / 2 / 0), legend swatches, the MACHINE chip and the thesis chart axes all render legibly on every PNG read. |
| k-7 | the cites a person counts on the PNG equal grades.json's | **MET** | Counted on `posture-cites-open.png`: reasons 1-6 carry 2+4+3+3+4+4 = **20** cites, **8** of them "Citation not resolved" (2+1+3+2). `posture-cites-open.json` reads visible 20 / unresolved 8 = fwd17 20 / 8. The footer's "12 of the 20 can be shown" equals 20 - 8. |

**Tally: 5 MET, 2 PARTIAL (k-1, k-5).**

## 2. FOUND ON THE FACES, OUTSIDE ANY CLAUSE

- **The research pack is said to be absent and present on the same name.** BA's Thesis reads "The research team's thesis
  pillars: no research pack for this security." (016). BA's Exec reads "no management section in the research pack or the
  earnings update" (027), and Model reads "No model in the research pack" (`model-empty.png`). Exec and Model presuppose a
  pack that Thesis says does not exist. One served reason, or its sentence mapping, is wrong. This is FWD-11, an input
  to the round-14 analysis.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S7` (l-3's remaining tokens on BA) | **GRADUATED** | the three token families are gone from BA's four faces (section 1, k-1); the residual "ABSENT" is a different source, recorded under k-1 |
| `Z-S8` (`/compare` 500 on "BA%20US") | **GRADUATED** | walk N `netlog.tsv`: every `/api/scoped/amgt/security/BA%20US/compare` call 200; 0 of 934 lines 5xx |
| `Z-S9` (6501 Exec "M-1" and producer words) | **CARRIED**, INERT | FWD-11, for the round-14 analysis |
| `Z-W51-S1` | **CARRIED**, INERT | as before |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 7 of 7. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** none open. **MET**
3. **Every judgment criterion graded:** 7 of 7 (5 MET, k-1 and k-5 PARTIAL). **MET**

## 5. FOR THE ROUND-14 ANALYSIS

The PRD moved to v0.6 (signed @0a41d21713) after this round was cut: the Friday round's FWD-21..24 supersede the list and
line views these orders polished. Of the PARTIALs, k-5's contradictory line and the pack-absent/present split sit on the
demo thread (Model and Thesis tabs). k-1's "ABSENT" sits in Posture's served text, a RESAPP/producer fix.

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S17",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T05:20:00Z",
    "one_line": "L9 round 14: k-2, k-3, k-4, k-6, k-7 AC4 MET (cites counted 20/8 = fwd17); k-1 PARTIAL (Posture reason 2 serves 'ABSENT'); k-5 PARTIAL ('No figure ... is shown' beside 'forward EPS (FY1) is -0.828'); BA Thesis says 'no research pack' while Exec and Model presuppose one; Z-S7 and Z-S8 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AV-k-1..k-7 read 'complete' on their LAST <status> tag.",
        "C:/tmp/dsgn-r14-close-render/model-empty.png: 'No model in the research pack for this name yet. No figure, case or estimate is shown in its place.' and 'Opal's historical-multiple reference: forward EPS (FY1) is -0.828, not positive'.",
        "posture-cites-open.png counted 2+4+3+3+4+4=20 cites, 8 'Citation not resolved'; posture-cites-open.json visibleCites 20 visibleUnresolved 8 fwd17 20/8; reason 2 'fit scores are ABSENT rather than low'.",
        "walk N shots 016 BA Thesis 'no research pack for this security'; 027 BA Exec 'no management section in the research pack or the earnings update'; 072 6501 Exec 'no M-1 management object has landed'.",
        "walk N netlog.tsv: /api/scoped/amgt/security/BA%20US/compare 200 on every call; 0 of 934 lines 5xx."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S7",
      "DSGN_AMGTV1-Z-S8"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close walk @8a198b327b presents AC4 of k-1..k-7 on walk N and the render run, 7 of 7 terminal, render PASS 74.",
    "world_is": "Five criteria met, two partial on the PNGs; one cross-face contradiction (research pack absent vs present) outside any clause.",
    "notes": "FOR THE ROUND-14 ANALYSIS: k-5's figure under 'no figure shown'; the pack absent/present split (Thesis vs Exec/Model); 'ABSENT' in Posture's served reason (producer fix); Z-S9's M-1 code."
  }
]
```
