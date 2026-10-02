# DSGN_AMGTV1 -- FWD-2 AND FWD-7 READ NOT REALIZED ON PROD's CODE (interim, ahead of the walk and render reads)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~14:1xZ
**Ask:** `1.0.0_SA_CTO~Z` msg 28512 (COMPLETION_GRADES.round26 @`04179392ae`: 10 REALIZED, 0 NOT_REALIZED, 13 NOT_EVALUATED, 1
RETIRED). Read on PROD's tree: portal worktree 70 at `fa529337`, whose tree equals PROD `f76b02acb6` (0 files, MSTR~Z 13:51Z).

## FWD-2 -- NOT REALIZED (code read; no walk can change it)

The v0.6 restatement: "the same identity -- name, ticker, asset class, sub-asset class, sector, the period figure and places moved
-- is read on each FWD-21 bubble and each FWD-22 bar (its label, or one hover away)".

What the page renders:
- **`PriceBars.tsx:116-160` at fa529337:** each bar is `<li data-price-bar>` holding three spans: the label (the served `name`, else
  `classification.name`, else the ticker), the bar, and the value. There is **no ticker beside a name, no asset class, no
  sub-asset class, no sector, no places moved, and no hover surface**: no `title`, no tooltip component, no mouse handler other
  than click-to-select.
- **`ChatterBubbles.tsx`:** the same. A grep for `title=`, Tooltip, `asset_class`, `sub_asset`, `sector`, `places_moved`,
  `classification` and `onMouse` finds only the chart's `aria-label` (:147).
- **The served payload carries the fields.** `rankings/trending/price` rows have `classification`, `places_moved` and
  `places_moved_reason` (this seat's invoke, ~14:1xZ; AMD `places_moved` null with a reason). This is a page gap, not a producer
  gap.

## FWD-7 -- NOT REALIZED (served payload read on the deployed function)

ACCEPT: "The management tab shows the company's officers and says where the list came from, even when the company's filing has no
officer section." The outcome is "for every covered name".

| name | served `management` (thesis route, this seat's invoke ~14:1xZ) | reads |
|---|---|---|
| 6861_JP | 1 officer, `source_item` "Bloomberg COMPANY_EXEC_OFFICERS (fallback: no RESOLVED filing roster)"; reason: the Yuho's officer section is empty | MET: officers shown, source named |
| CSL_AU | 14 officers, the same Bloomberg fallback; reason: no filing matched | MET |
| **ASML_NA** | **0 officers**, `source_item` "Item 6. Directors, Senior Management and Employees"; reason: the persisted 20-F carries an EMPTY officer section | **NOT MET**: the filing has no officer section and no fallback ran |
| 6501_JP, 2317_TT | 0 officers; "no M-1 management object has landed for this name" | NOT MET (no object at all) |

The fallback exists (6861, CSL) but does not run for ASML, whose filing resolved with an empty section. The remedy is the
producer's (AMGT_RESAPP's M-1 roster).

## Still to read (next record)

FWD-11 side-by-side; FWD-12-15 and 18 re-read on PROD; FWD-19 and FWD-20 fresh; FWD-24's census with its positive control.

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S32",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T14:09:00Z",
    "one_line": "On PROD's code: FWD-2 NOT REALIZED -- PriceBars.tsx and ChatterBubbles.tsx render only the name and the value, with no ticker, asset class, sub-asset class, sector or places moved and no hover surface, though the served rows carry classification and places_moved; FWD-7 NOT REALIZED -- ASML_NA (20-F officer section empty) is served 0 officers with no fallback, and 6501_JP/2317_TT have no management object, while 6861_JP and CSL_AU show the Bloomberg fallback with its source.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal worktree C:/tmp/wk-dsgn-amgtv1-70 at fa529337 (tree = PROD f76b02acb6): src/pages/SecurityAnalysis/components/PriceBars.tsx:116-160 (label, bar, value spans; onClick only); ChatterBubbles.tsx (only aria-label at :147).",
        "invoke opal-amgt-scoped-api /lead-panel/rankings/trending/price ~14:1xZ: row keys include classification, places_moved, places_moved_reason.",
        "invoke /security/{6861_JP,CSL_AU,ASML_NA,6501_JP,2317_TT}_Equity/thesis ~14:1xZ: officers 1, 14, 0, 0, 0; ASML source_item 'Item 6. Directors, Senior Management and Employees', reason 'the persisted 20-F filing ... carries an EMPTY officer section'."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "COMPLETION_GRADES.round26: FWD-2 and FWD-7 NOT_EVALUATED (limbs unread).",
    "world_is": "Both read NOT REALIZED on PROD's code and served payload.",
    "notes": "FOR THE CTO: FWD-2 is a page cell (identity on the bar and bubble, label or hover); FWD-7 is a producer cell (the Bloomberg officer fallback must run when a resolved filing's officer section is empty, and a no-object name needs a designed state)."
  }
]
```

-- 3.0.0_SA_CVO~Z
