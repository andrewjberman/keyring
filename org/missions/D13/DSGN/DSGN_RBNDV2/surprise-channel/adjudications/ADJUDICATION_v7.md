# DSGN_RBNDV2: CVO L8/L9 at the round-6 close (2026-10-15)

<sweep_watermark>2026-10-15T17:25Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~RB` msg 109465 (record `deliverables/2.0.0_SA_COO~RB/ROUND6_CLOSE_RUN_20261015.md` @b8e6689ca4).

**Result: RB6Y1-AC3 and RB6Y2-AC3 MET. This cures the round-5 regression C-S18 (boxed Trending Topics rows). Nine INERT notes are dismissed.** This seat also
confirms the COO's typecheck correction: the round-4 and round-5 "rc=0" lines named an empty check, and the real one at the tip reads rc=0.

Instrument. This seat's own walk of `/market` on the feature-branch build at port 5174 (`tmp/ui-walk/20261015T172908Z`, gitignored). It was armed, signed in
and disarmed, with the post-disarm login REFUSED. Also `./node_modules/.bin/tsc -p tsconfig.app.json --noEmit` in `ajb_wk/rbndv2-int` @3509eae8, rc=0.

```json
[
 {
  "id": "DSGN_RBNDV2-C-S20",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T17:31Z",
  "one_line": "L9 round 6: RB6Y1-AC3 MET (the Trending Topics rows show no box again; the period chips keep their active underline); RB6Y2-AC3 MET (the Daily Cloud footer reads 'Source: Global News.' and the Trending Topics footer ends in proper-case source names). This cures C-S18.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "RB6Y1-AC3: the Trending Topics rows show no box (border colour transparent); the controls (period chips, dropdowns) keep their lines. RB6Y2-AC3: the Daily Cloud footer on Market Overview reads 'Source: Global News.' and the Trending Topics footer ends with proper-case source names.",
  "world_is": "The six topic rows render as plain lines under their headings with no box, as in the round-2 build, and the computed border is transparent by the COO's read. The Top/Bottom period chips render as in round 4, with the active WTD navy and underlined; no dropdown sits on these panels. The footers read 'October 15th, 2026, 7:18a ET | Source: Global News.', '... | Source: Bloomberg, CNBC, Financial Times, and more.', '... | Source: Bloomberg.' and '... | Source: CNN.'. The typecheck over the application and its tests (tsconfig.app.json) is rc=0 at 3509eae8, so the TS2769 merged in round 5 (W19-S3) is repaired.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "tmp/ui-walk/20261015T172908Z/shots/001--market-load.png (gitignored; this seat's walk, 2026-10-15 ~17:29Z)",
    "ajb_wk/rbndv2-int @3509eae8: ./node_modules/.bin/tsc -p tsconfig.app.json --noEmit -> rc=0",
    "org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ROUND6_CLOSE_RUN_20261015.md @b8e6689ca4"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard. 622 border-white/N uses in 119 files remain portal-wide; the other pages follow Andrew's page-by-page walk."
 },
 {
  "id": "DSGN_RBNDV2-C-S21",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T17:31Z",
  "one_line": "Round 6 worker notes dismissed INERT: W19-S1..S3, W20-S1..S4, W21-S1, W21-S2.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["DSGN_RBNDV2-W19-S1", "DSGN_RBNDV2-W19-S2", "DSGN_RBNDV2-W19-S3", "DSGN_RBNDV2-W20-S1", "DSGN_RBNDV2-W20-S2", "DSGN_RBNDV2-W20-S3", "DSGN_RBNDV2-W20-S4", "DSGN_RBNDV2-W21-S1", "DSGN_RBNDV2-W21-S2"],
  "spec_asserts": "Each order's text as written.",
  "world_is": "W19-S3 (TS2769 in the round-5 test) is repaired by RV-y-3; this seat's tsc read is rc=0. W19-S2: the portal's CONTRIBUTING-BOXES.md asks for a cand/<box>/<slug> branch cut from the last PROD release, while this project builds on feature/dsgn-rbndv2-light under C-BRANCH (Andrew's word, nothing pushed). That is for the CTO to reconcile before any merge forward. W20-S1: the Trending Topics footer passes the data's own source names through, so its casing rests on the data, not on a rule. The rest are sizing, base-commit and test-text notes.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md rows as listed",
    "ajb_wk/rbndv2-int @3509eae8 tsc rc=0"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Build notes. W19-S2 (the branch shape against the portal's contributing rule) is named in the slug for the CTO."
 }
]
```

-- 3.0.0_SA_CVO~L
