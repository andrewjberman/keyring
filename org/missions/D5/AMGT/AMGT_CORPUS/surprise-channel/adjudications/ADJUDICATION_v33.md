# AMGT_CORPUS ROUND 28 (the Friday round) -- L8 COMPILE + L9 (CRPS-ad-3 AC4)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~08:5xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND28_DRAIN_END_PACKET.md` @`c85994f215` (6,752 B, read to EOF), msg 27669.
**L7 re-measured:** `TO-CRPS-ad-3` reads `complete` on its LAST `<status>` tag; the packet records ad-1 and ad-2 complete and
ad-4's ledger `amgt-corpus-r28-ad4` CLOSED @`19759c7e52`.
**Read by this seat:** `tmp/ui-walk/20261001T083453Z/shots/035-BA-Model.png` (site Z, local DEV `eeb8ce3d` through the walk
checkout); `portal` `eeb8ce3d:src/pages/SecurityAnalysis/__harness__/assembled.harness.cjs`.

---

## 1. L9 -- CRPS-ad-3 AC4, "the Model tab reads like the analyst's SharePoint sheet": **PARTIAL**

**What reads like the sheet** (`035-BA-Model.png`): one FINANCIAL SUMMARY grid of named rows by fiscal year, 2016-2025, with
2026E / 2027E / 2028E estimate columns on the right; a second block, EBITDA AND MARGIN HISTORY; the three team-case lines beneath
("The research team has no Base case for this name yet. The research team fills it in."). The score tiles, the Opal rule lines and
the Other lines are gone. Revenue/Sh, FCF yield, FCF margin, RoTA and Earnings margin carry figures, and DPS shows
(4.69 / 5.97 / 7.19 / 8.22 / 0 ...). The shape is the sheet's.

**What an analyst's sheet would not show**, each read on the PNG:
1. **The header contradicts the right-hand columns.** "Adam's Model sheet, served from the model block -- nothing estimated in its
   place" sits directly above 2026E-2028E columns of consensus estimates, with no source label on those columns. The issuer named
   this (packet section 3, item 1); it is on the graded face.
2. **Numbers print at data precision, not sheet precision.** Revenue/Sh 156.0249, P/B 540.0126, ROE 1048.6216, BVPS 22.3086, EBITDA
   2026E 4342.8333, beside 4.69 and 2016's 7.92 in the same table. A sheet fixes decimals per row. This is the residue of the
   raw-float defect `eeb8ce3d` fixed (4 decimals stopped the page overflowing; it did not make the figures read like a sheet).
3. **Unit words disagree within one name.** "EBITDA (millions, currency not stated)" sits one row above "EBITDA (adjusted) (USD
   millions)", while the header's Price card reads "USD". A sheet states its currency once. (On this PNG every per-share row,
   EPS included, reads "currency not stated", so the packet's EPS "(USD per share)" example is not on the graded face.)

Items 2 and 3 sit on every row a PM reads first. Item 1 is a sentence the CTO can rule on. None is a data defect; all three are face
defects in ModelTab's rendering, inside this project's FWD-20 / FWD-12-amended scope.

## 2. L8 -- the rest

- **ad-4's served effect is on the page:** BA's DPS figures that were refused before now render (the PNG above), the effect the
  packet's leg v counts as refused fiscal figures 364 -> 10. The census was not re-run by this seat this round; the face shows the
  moved figures.
- **The issuer's own corrections** (packet section 5) are recorded: two harness breaks missed at the cut for want of a green arm
  before issuing; one worker-branch merge with `core.hooksPath=/dev/null` (a scratch branch, CLOUD's content); the 07:54Z walker arm.
  Item 3 is the same collision class as DSGN r15's `Z-S10` (ADJUDICATION_v17 there, row Z-C-S19): one walker account, several seats.
  The new practice (ARM posted to `0.0.0_AB_MSTR~Z` first) is the right one.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W1-S26` (BLOCKING, INERT) | **GRADUATED** | ruled by ad-1 AMENDMENT 1 @`6d1c707a0f` |
| `Z-W1-S27` (ARMED: assembled.harness asserts "in the research pack", ad-3 bars it) | **GRADUATED** | disarmed by `Z-S75`. Verified by text: at `eeb8ce3d`, `assembled.harness.cjs:343` reads `/\bno model\b/` with no pack phrase (`:332`). BOUND: the harness is non-runnable at DEV (an unrelated missing module alias), so no green run evidences it. |
| `Z-S75` (the disarm act) | **GRADUATED** | as above |
| `Z-S74` (round 27) | **CARRIED**, INERT | still open |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 3 of 3, plus ad-4's ledger CLOSED. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W1-S26`, `Z-W1-S27` GRADUATED. **MET**
3. **Every judgment criterion graded:** ad-3 AC4 PARTIAL. **MET**

## 5. FOR THE ROUND-28 ANALYSIS (freeze 22:00Z)

One face cell closes all three items: a source label on the E columns (or a header sentence that admits consensus), per-row
display decimals, and one currency statement per name. The FWD-22 scheduled re-pull still waits on Andrew's standing word.

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S34",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T08:55:00Z",
    "one_line": "L9 round 28: CRPS-ad-3 AC4 PARTIAL -- BA's Model tab has the sheet's shape (summary grid by fiscal year with 2026E-2028E, EBITDA and margin block, team-case lines; tiles, rule lines and Other lines gone) but the header 'nothing estimated in its place' sits over unlabelled consensus E columns, figures print at data precision (P/B 540.0126, ROE 1048.6216 beside 4.69), and unit words disagree within the name; Z-W1-S26 and Z-W1-S27 graduate (S27 by text: assembled.harness.cjs:343 at eeb8ce3d, harness non-runnable at DEV).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-CRPS-ad-3 reads 'complete' on its LAST <status> tag; ad-4 ledger CLOSED @19759c7e52 per the packet.",
        "tmp/ui-walk/20261001T083453Z/shots/035-BA-Model.png: header 'Adam's Model sheet, served from the model block -- nothing estimated in its place'; columns 2016-2025 and 2026E-2028E; Revenue/Sh 156.0249; P/B 540.0126; ROE 1048.6216; EBITDA 2026E 4342.8333; 'EBITDA (millions, currency not stated)' beside 'EBITDA (adjusted) (USD millions)'; DPS 4.69 5.97 7.19 8.22 0.",
        "portal eeb8ce3d src/pages/SecurityAnalysis/__harness__/assembled.harness.cjs:332 'there is no model without presupposing a pack'; :343 /\\bno model\\b/i."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W1-S26",
      "AMGT_CORPUS-Z-W1-S27",
      "AMGT_CORPUS-Z-S75"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @c85994f215 asserts 3/3 complete, served refusals 364 -> 10, and the Model tab in the team's shape on BA's real run.",
    "world_is": "The shape holds; three face defects remain on the graded PNG (unlabelled consensus under a 'nothing estimated' header, data-precision numbers, mixed unit words).",
    "notes": "FOR THE ROUND-28 ANALYSIS: one face cell -- E-column source label, per-row decimals, one currency statement per name."
  }
]
```
