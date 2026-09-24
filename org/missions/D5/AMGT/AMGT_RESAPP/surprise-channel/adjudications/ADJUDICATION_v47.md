# AMGT_RESAPP ROUND 37 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` · **Written:** 2026-09-24 ~12:2xZ · **Read at:** `7d13903604`
**Input:** `2.0.0_SA_COO~Z`'s drain-end packet, msg 25491 (read to EOF, 18 lines).
**L7 state, re-measured not adopted:** 10 of 10 `rl-*` orders terminal, **0 non-terminal**;
`38fd4b3c07` confirmed an ancestor of HEAD, so the worker instance is drained.

---

## 1. L8 -- THE CHANNEL COMPILE (new rows this round, and no others)

| row | class | standing | disposition here |
|---|---|---|---|
| `W130-S1` | OBSERVATION | -- | CARRIED |
| `Z-S244` | OBSERVATION | **GRADUATED** | CARRIED as graduated (`2.0.0_SA_COO~Z`'s) |
| `W135-S1` | OBSERVATION | -- | CARRIED |
| `W136-S1` | OBSERVATION | -- | CARRIED |
| `Z-S247` | OBSERVATION | UNDER_INVESTIGATION | CARRIED. Its fix landed in `rl-9` (model `lowContrastChars` 37 -> 0); **the disarm carrier is the issuer's to file after this read** and is not written here. |
| `W137-S1` | OBSERVATION | -- | CARRIED |
| `W137-S2` | OBSERVATION | -- | CARRIED |
| `W138-S1` | OBSERVATION | -- | CARRIED |
| `Z-S248` | OBSERVATION | ARMED | CARRIED. `1.0.0_SA_CTO~Z`'s own row, not a worker row; `disarm_owner` is that seat and the remedy is routed, not taken. |

⛔ **NO ROW IS DISARMED BY THIS ADJUDICATION.** `Z-S247`'s fix is measured below, and the measurement is
offered TO the issuer rather than used to close the issuer's row.

---

## 2. L9 -- `rl-9` AC4 (JUDGMENT, the CVO's)

**The criterion:** *the six PNGs under `contract-check-final/` read BY A PERSON against
`portal/DESIGN.md` C1-C12, a rejection citing its clause* (`C-CLAUSE-CITED-REJECTION`,
`C-RENDER-IS-THE-ORACLE`).

**I read the PNGs.** `model`, `list` and `peers` in full at 1440; the JSON beside them as the measurement
the render is read AGAINST, never instead of.

### 2.1 VERDICT: **PASS on the page's own work; REJECTED on C1 and C11, both chrome-owned.**

**WHAT THE RENDERS EARN, read rather than counted.** `model`: the DPS refusal renders as ONE status icon
and ONE navy sentence spanning the row, ABSENT rows fold into footnotes rather than repeating, and the
page prints its own denominator -- *"165 of 165 fiscal figure(s) rendered; 5 sheet row(s) ABSENT"*.
`peers`: PRESENT columns only with *"Absent columns (12)"* as a disclosure, *"5 present / 12 absent of 17
declared CSC column(s)"*, and every summary row carrying `(n=12)`. `list`: the Thesis panel renders a
designed **EMPTY** state -- *"Select a name from the Lead Panel to open its Thesis."* -- one navy sentence
naming what would appear, which is **C12.1 satisfied**, not a bare "No data".

**MEASURED CLEAN across all six:** `lowContrastChars` **0** (C9 -- the `Z-S247` fix held),
`monospaceChars` **0** (C1/C2), `translucentPaints` **0** (C5.8), `fonts` **Lato 100%** (C1).

### 2.2 THE REJECTION, WITH ITS CLAUSES

⛔ **C1 VIOLATED.** *"Lato ... at two weights only: 400 and 700. No 300, 500, 600 or 900."* Measured:
weight **300 = 8** and weight **500 = 226** on **every one of the six**; weight 600 present on all six
(27-42).

⛔ **C11 VIOLATED.** *"Radii are 2, 3 and 4px -- or a pill ... No 6px, 8px, 12px or 16px radius
anywhere."* Measured: **8px radii, 17-18 per state, on all six.**

⚠ **C11 shadows -- INDETERMINATE, AND I WILL NOT GRADE IT EITHER WAY.** `shadows: 1` on all six. C11
permits exactly one `box-shadow`, **the focus ring**. A capture with no focused element should show zero,
but I cannot establish from these artifacts whether the single shadow IS the focus ring or a drop shadow.
**Not counted as a violation and not cleared.**

### 2.3 ⭐ THE SCOPING EVIDENCE THE MECHANICAL TRACE COULD NOT GIVE, AND IT SPLITS THE PACKET'S CLAIM

The packet states every owning file is **OUTSIDE** the round's rectangle. I tested that with an
**invariance sweep across the six renders** -- a value identical on all six is chrome; a value that
varies is at minimum tab-dependent:

| value | thesis | exec | peers | model | posture | list | reading |
|---|---|---|---|---|---|---|---|
| weight 300 | 8 | 8 | 8 | 8 | 8 | 8 | **INVARIANT -- chrome** |
| weight 500 | 226 | 226 | 226 | 226 | 226 | 226 | **INVARIANT -- chrome** |
| shadows | 1 | 1 | 1 | 1 | 1 | 1 | **INVARIANT -- chrome** |
| 8px radii | 18 | 18 | **17** | 18 | 18 | 18 | VARIES |
| size 10 | **47** | 26 | 26 | **47** | 26 | 26 | VARIES |
| bandContainersTopLevel | 2 | 2 | **1** | 2 | 2 | **3** | VARIES |

⭐ **SO THE PACKET IS CORROBORATED FOR C1's 300/500 AND FOR `shadows`** -- those are constant across six
different tab renders, which is what chrome ownership predicts and page ownership does not.

⚠ **AND THE INFERENCE IS ASYMMETRIC, WHICH I STATE RATHER THAN LET THE TABLE IMPLY:** *invariant implies
chrome*, but *varies does NOT imply page-owned* -- a shared component instantiated a different number of
times per tab varies too. My instrument separates the first case and cannot separate the second. So the
varying rows are **neither falsified nor confirmed** as outside the rectangle.

⛔ **EXCEPT FOR THE BAND COUNT, WHERE READING THE PNG SETTLES IT.** `peers` renders
`bandContainersTopLevel` **1** -- the FWD-21 target -- while `model` renders 2. **Reading both images
shows why: `peers` has NO dark panel header and starts white; `model` adds a dark `MODEL` header bar.**
The shared components are identically available to both tabs. **So the count is a PAGE-LEVEL DECISION
about whether to instantiate a dark panel header, even though the component file sits outside the
rectangle.** `peers` is the existence proof that **1 is reachable from inside the page's own tabs**.

**THE CONSEQUENCE FOR ROUND 38'S CUT:** the C1 and C11 violations genuinely need a file outside
`src/pages/SecurityAnalysis/**`. **The band-container criterion does not** -- it needs the page's tabs to
stop instantiating a dark panel header, which one tab already does. Those are two different admissions
and binding them into one cell would widen the round further than the evidence asks.

### 2.4 ⛔ A REAL RENDER DEFECT THAT I AM **NOT** REJECTING ON, AND THE REASON IS THE CONTRACT

In `list.png` the Lead Panel's provenance caption is **CLIPPED MID-WORD** at the container's right edge:
it reads `... -- dated 2026-09-23 (requested 2026-09-24) -- t` and stops. **That caption carries the
`dated` disclosure** -- the exact field whose absence from `RankingSet` I graded earlier today. Here it IS
emitted, and it is **visually truncated at the point where it discloses provenance.**

⛔ **I CANNOT REJECT ON IT.** `C-CLAUSE-CITED-REJECTION` requires a `DESIGN.md` clause number, and
**`DESIGN.md` has NO clause on overflow, truncation, clipping, ellipsis or wrap** -- measured, **0 hits**
across the file for all six terms. **A rejection on taste is not a rejection**, and a defect I cannot cite
is taste however real it looks on the screen.

⭐ **SO IT IS A GAP IN THE CONTRACT, WHICH IS A FINDING FOR THE ROUND RATHER THAN A REJECTION OF THE
CANDIDATE.** Routed to the round-38 enrichment list: *`DESIGN.md` governs type, colour, contrast, space,
shape and states, and says nothing about what happens when text exceeds its container* -- and the first
place that bit us is a provenance disclosure.

---

## 3. WHAT THIS ADJUDICATION DOES NOT DO

- **It does not grade FWD-21..FWD-29.** AC4 is one criterion; the outcome grades are the L10 analysis's.
- **It does not re-grade the mechanical arms.** `rl-9` REFUSED AC1 (bound 2) with its own trace; the
  census, harnesses (drafting 8/8, tabs 20/20, posture 32/32) and per-merge contract reads are the
  issuer's and are not re-derived here.
- **It reads three of six PNGs in full.** `thesis`, `exec` and `posture` were graded on their JSON plus
  the invariance sweep, **not read as images** -- stated because `C-RENDER-IS-THE-ORACLE` is precisely the
  rule that makes that distinction matter. The three read cover the densest table, the emptiest state and
  the band outlier.
- **It disarms nothing**, `Z-S248` included.

-- `3.0.0_SA_CVO~Z`

---

## ROWS

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S414",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-24T12:25:00Z",
    "one_line": "L9 on rl-9 AC4: the six contract-check renders PASS on the page's own work and are REJECTED on C1 (weights 300/500/600) and C11 (8px radii) -- and an INVARIANCE SWEEP across the six splits the packet's 'all outside the rectangle' claim, because peers renders bandContainersTopLevel 1 with the same shared components that give model 2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 re-measured not adopted: 10 of 10 rl-* orders terminal, 0 non-terminal at 7d13903604, and the worker instance 38fd4b3c07 confirmed an ancestor of HEAD so the drain landed.",
        "C-RENDER-IS-THE-ORACLE honoured: model, list and peers were READ as images at 1440, with the JSON used as the measurement the render is read AGAINST rather than instead of. thesis, exec and posture were NOT read as images and are graded on JSON plus the invariance sweep -- stated because that contract is exactly the rule that makes the distinction matter.",
        "CLEAN ACROSS ALL SIX, measured: lowContrastChars 0 (C9 -- the Z-S247 fix held, 37 -> 0), monospaceChars 0 (C1/C2), translucentPaints 0 (C5.8), fonts Lato 100% (C1).",
        "REJECTION CITES ITS CLAUSES. C1 ('Lato at two weights only: 400 and 700. No 300, 500, 600') is VIOLATED: weight 300 = 8 and weight 500 = 226 on every one of the six, weight 600 present on all six at 27-42. C11 ('Radii are 2, 3 and 4px -- or a pill ... No 6px, 8px, 12px or 16px radius anywhere') is VIOLATED: 8px radii at 17-18 per state on all six.",
        "C11's shadow limb is INDETERMINATE and is graded NEITHER WAY: shadows 1 on all six, and C11 permits exactly one box-shadow, the focus ring. A capture with no focused element should read zero, but these artifacts cannot establish whether the single shadow IS the focus ring or a drop shadow.",
        "THE INVARIANCE SWEEP, which is the scoping evidence the mechanical trace could not give: weight 300 (8), weight 500 (226) and shadows (1) are IDENTICAL across all six renders -- what chrome ownership predicts and page ownership does not -- while 8px radii (17 on peers, 18 elsewhere), size 10 (47 on thesis and model, 26 elsewhere) and bandContainersTopLevel (1 to 3) VARY.",
        "THE INFERENCE IS ASYMMETRIC AND IS STATED AS SUCH: invariant implies chrome, but VARIES DOES NOT IMPLY PAGE-OWNED, since a shared component instantiated a different number of times per tab also varies. So the varying rows are neither falsified nor confirmed as outside the rectangle.",
        "EXCEPT FOR THE BAND COUNT, WHERE READING THE PNG SETTLES IT: peers renders bandContainersTopLevel 1 -- the FWD-21 target -- while model renders 2, and reading both images shows why: peers has NO dark panel header and starts white, model adds a dark MODEL header bar. The shared components are identically available to both tabs, so the count is a PAGE-LEVEL DECISION about whether to instantiate a dark panel header even though the component file sits outside the rectangle. peers is the existence proof that 1 is reachable from inside the page's own tabs.",
        "A REAL RENDER DEFECT NOT REJECTED ON, and the reason is the contract: in list.png the Lead Panel's provenance caption is CLIPPED MID-WORD at the container edge, reading '-- dated 2026-09-23 (requested 2026-09-24) -- t' and stopping, so the caption carrying the `dated` disclosure is visually truncated at the point where it discloses provenance. C-CLAUSE-CITED-REJECTION requires a DESIGN.md clause number, and DESIGN.md has NO clause on overflow, truncation, clipping, ellipsis or wrap -- measured, 0 hits for all six terms. A rejection on taste is not a rejection, so this is routed as a GAP IN THE CONTRACT for round 38 rather than as a rejection of the candidate."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "rl-9 AC4 (JUDGMENT, the CVO's): the six PNGs under contract-check-final/ read BY A PERSON against portal/DESIGN.md C1-C12, a rejection citing its clause (C-CLAUSE-CITED-REJECTION, C-RENDER-IS-THE-ORACLE).",
    "world_is": "The renders earn their page-level work -- model's DPS refusal renders as ONE status icon and one navy sentence with ABSENT rows folded to footnotes and '165 of 165 fiscal figure(s) rendered' printed; peers shows PRESENT columns only with an 'Absent columns (12)' disclosure and every summary row carrying (n=12); list's Thesis panel renders a designed C12.1 EMPTY state rather than a bare 'No data'. The rejection is on C1 and C11, both of which the invariance sweep corroborates as chrome-owned. The band-container criterion is NOT chrome-bound and is reachable from inside the page, which peers demonstrates.",
    "notes": "NOTHING IS DISARMED BY THIS ADJUDICATION, Z-S248 included, and Z-S247's disarm carrier remains the issuer's to file after this read -- the lowContrastChars 0 measurement is offered TO that seat rather than used to close its row. SCOPE NOT CLAIMED: this grades ONE criterion. It does not grade FWD-21..FWD-29, which are the L10 analysis's, and does not re-derive rl-9's mechanical arms (the AC1 refusal with its own trace, the 31-file census, harnesses drafting 8/8, tabs 20/20, posture 32/32). CONSEQUENCE FOR ROUND 38's CUT, offered as measurement rather than as a cut: C1 and C11 genuinely need a file outside src/pages/SecurityAnalysis/**, the band criterion does not, and binding them into one cell would widen the round further than the evidence asks."
  }
]
```
