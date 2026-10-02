# DSGN_AMGTV1 ROUNDS 17-21 -- L8 COMPILE + L9 STAMPS (every open and ARMED row, re-measured at PROD b3a1d8a6)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~05:5xZ
**Input:** `1.0.0_SA_CTO~Z` msg 28229 (queue item 2). The close records `round17..21/ROUND{17..21}_CLOSE.md` (round 21 @`0f6b932de1`);
rows `Z-S12` (@`d11d8ee1fe`) and `Z-S13` (@`092047f79f`).
**Denominator (the consumer's instrument):** `comp-surprise --project DSGN_AMGTV1 --json` at ~05:5xZ: 41 items, 18 open, 7 ARMED
(Z-S10 is in both), so **24 items** owe a stamp. 0 duplicate ids, 0 malformed.
**L7 re-measured (LAST `<status>` tag):** AV-h-1, h-2, i-1, i-2, j-1, x-1, y-1 all read `complete`. Rounds 17-21 carry **0 judgment
criteria**: every criterion is a node check. So there is no per-criterion L9 grade to owe for rounds 17-21. The L9 owed is the
dispositions below, plus the FWD read the CTO asked for (a separate record).
**Portal plane:** PROD `b3a1d8a6` contains DEV `24646bca` and the freeze `3c37a01c` (both `merge-base --is-ancestor`, true). The portal
working tree is at `24646bca`, clean.

---

## 1. THE SEVEN ARMED ROWS -- each disarm re-measured by this seat

| row | the disarm claim (Z-S12 / Z-S13) | this seat's read | stamp |
|---|---|---|---|
| `Z-S5` | 0 files carry byte 0x08 | `git show b3a1d8a6:` over all **77** files under `src/pages/SecurityAnalysis`: **0** with 0x08 | DISMISSED_WITH_REASON |
| `Z-W4-S1` | exportCompare keys on data, not wording | `exportCompare.harness.cjs` @b3a1d8a6 keys on `data-model-case-formula` / `data-model-line-refusal` at :297, :307, :342, :348 | DISMISSED_WITH_REASON |
| `Z-W28-S1` | walk.mjs accepts the documented flags | `.claude/skills/ui-walk/walk.mjs:40` parses `--thread`; 11 lines carry `lead-lists.json` / `timeline-day` / `timeline-event` | DISMISSED_WITH_REASON |
| `Z-W2-S1` | one channel file, one header | comp-surprise: `duplicate_ids {}`, `malformed []`, 41 items in one file | DISMISSED_WITH_REASON |
| `Z-W3-S1`, `Z-W3-S2` | tabs.harness green 20 of 20 | `node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs` at 24646bca, run by this seat: `CHECKS-OK 20 of 20`, `thesis_sentences_and_one_chart true`, rc 0 | DISMISSED_WITH_REASON |
| `Z-S10` | no 500 on a cookie-bearing refresh | both netlogs (`tmp/ui-walk/20261001T151253Z`, `...164049Z`), 943 lines each: **0** 5xx; POST `/auth/refresh` 401 x2 before login (the row's own control), then **8 of 8** 200 | DISMISSED_WITH_REASON, **scope stated**: the 5174 dev build against the shared backend, never a PROD read |

The disarm records themselves, `Z-S12` and `Z-S13`, are stamped with them.

## 2. THE OPEN OBSERVATIONS (INERT)

| row | stamp | grounds |
|---|---|---|
| `Z-S9` (interface code "M-1" on the Exec face) | DISMISSED_WITH_REASON | fixed in PROD: `reasonWords.ts:25` drops a letter-dash-digit code; 0 such codes in the round-21 walk's findings |
| `Z-S2` (clients-tab 500 on a selection) | DISMISSED_WITH_REASON | off-project (an Advisor Intelligence route); the round-21 walk reads it **9 of 9 200** |
| `Z-W65-S1` | DISMISSED_WITH_REASON | resolved in portal f049ec3c, as the row records |
| `Z-W5-S1`, `Z-W8-S1`, `Z-W11-S1` | DISMISSED_WITH_REASON | harness anchors moved to data attributes; the bound harnesses stay green (tabs 20 of 20 above) |
| `Z-W45-S1`, `Z-W45-S2`, `Z-W51-S1`, `Z-W56-S1`, `Z-W56-S2`, `Z-W56-S3`, `Z-W61-S1` | DISMISSED_WITH_REASON | a worker's reading of a cell's wording, recorded and since superseded by later cells (bubbles round 15, chatter rounds 18-19); no page defect |
| `Z-W56-S4` (errorEmpty's starred-case claims pass by ABSENCE) | **GRADUATED** | a verification-instrument residual. Three checks expected `false` read green because no StarredList renders, so they grade nothing. This is batch-cell material for the CTO, never a page defect |
| `Z-S11` (walk.mjs reads every pointer-events-none tooltip as occluded) | **GRADUATED** | an instrument false positive (walk.mjs:102-111). Occlusion was graded with hoverprobe.mjs's corrected hit-test (round 21: BA 13 of 13, AMD 10 of 10). walk.mjs is the ui-walk skill's, not DSGN's |

## 3. AFTER THIS ROW

Open: 0. ARMED: 0. The two GRADUATED residuals are INERT and do not hold the slug (spine L10 gate).

## 4. WHAT YOU SHOULD HAVE ASKED BUT DID NOT

The round-21 walk's `timeline:no-event-element` on AMD and TSM is labelled `FWD-6` by walk.mjs, but in the PRD the timeline is
**FWD-5** and FWD-6 is the Thesis cards. The walker's rule labels are an older numbering. Any FWD grade that reads walk findings by
their label grades the wrong outcome. The FWD read must map each finding to the PRD's text, never to the walker's tag.

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S21",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T05:58:00Z",
    "one_line": "L9 stamp: the seven ARMED rows are disarmed in the world, each re-measured by this seat at PROD b3a1d8a6 / DEV 24646bca: S5 0 of 77 files with 0x08; W4-S1 data-keyed at :297-348; W28-S1 walk.mjs:40 --thread; W2-S1 0 duplicates; W3-S1/S2 tabs CHECKS-OK 20 of 20 rc 0; S10 0 5xx and 8 of 8 post-login refresh 200 in both walks (dev build, not PROD).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal merge-base --is-ancestor 24646bca b3a1d8a6 -> true; 3c37a01c b3a1d8a6 -> true.",
        "git show b3a1d8a6:<f> over 77 files under src/pages/SecurityAnalysis: 0 contain 0x08.",
        "exportCompare.harness.cjs @b3a1d8a6 lines 297, 307, 342, 348 carry data-model-case-formula / data-model-line-refusal.",
        ".claude/skills/ui-walk/walk.mjs:40 `else if (a === '--thread')`; 11 lines match lead-lists.json|timeline-day|timeline-event.",
        "comp-surprise --project DSGN_AMGTV1 --json: duplicate_ids {}, malformed [], investigation_items 41.",
        "node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs at portal 24646bca: CHECKS-OK 20 of 20, rc 0.",
        "tmp/ui-walk/20261001T151253Z/netlog.tsv and 20261001T164049Z/netlog.tsv: 943 lines each, 0 rows with a 5xx status; POST /auth/refresh 401 at 80-81 (pre-login), then 200 at 259, 260, 427, 428, 633, 634, 828, 830."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S5",
      "DSGN_AMGTV1-Z-W4-S1",
      "DSGN_AMGTV1-Z-W28-S1",
      "DSGN_AMGTV1-Z-W2-S1",
      "DSGN_AMGTV1-Z-W3-S1",
      "DSGN_AMGTV1-Z-W3-S2",
      "DSGN_AMGTV1-Z-S10",
      "DSGN_AMGTV1-Z-S12",
      "DSGN_AMGTV1-Z-S13"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each hazard's cause is absent at the PROD-contained build, re-measured by this seat (grounding); Z-S10 on the dev build only.",
    "spec_asserts": "Z-S12 and Z-S13 record the disarms and leave the formal disposition to L9.",
    "world_is": "Every cause is absent at the PROD-contained build; the disarms hold on this seat's own reads. Z-S10's evidence covers the dev build only.",
    "notes": "Dismissed because the hazard is gone, not because it never stood."
  },
  {
    "id": "DSGN_AMGTV1-Z-C-S22",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T05:58:00Z",
    "one_line": "L9 stamp: thirteen INERT observations close -- S9 fixed in PROD (reasonWords.ts:25 drops letter-dash-digit codes); S2 off-project and 9 of 9 200 in the round-21 walk; W65-S1 resolved in f049ec3c; W5-S1, W8-S1, W11-S1 anchors on data attributes with the bound harnesses green; W45-S1, W45-S2, W51-S1, W56-S1, W56-S2, W56-S3, W61-S1 are cell-wording readings superseded by later cells.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/SecurityAnalysis/reasonWords.ts:25 (portal 24646bca, in PROD b3a1d8a6): an interface code (letters, dash, digits -- \"M-1\") is dropped.",
        "tmp/ui-walk/20261001T164049Z/netlog.tsv: GET /api/scoped/advisor-intelligence/clients-tab 9 of 9 status 200.",
        "tmp/ui-walk/20261001T164049Z/findings.json: no letter-dash-digit code on a face (the 2 hits are the walker's 'FWD-6' rule label).",
        "tabs.harness.cjs CHECKS-OK 20 of 20 (this seat's run, row Z-C-S21)."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S9",
      "DSGN_AMGTV1-Z-S2",
      "DSGN_AMGTV1-Z-W65-S1",
      "DSGN_AMGTV1-Z-W5-S1",
      "DSGN_AMGTV1-Z-W8-S1",
      "DSGN_AMGTV1-Z-W11-S1",
      "DSGN_AMGTV1-Z-W45-S1",
      "DSGN_AMGTV1-Z-W45-S2",
      "DSGN_AMGTV1-Z-W51-S1",
      "DSGN_AMGTV1-Z-W56-S1",
      "DSGN_AMGTV1-Z-W56-S2",
      "DSGN_AMGTV1-Z-W56-S3",
      "DSGN_AMGTV1-Z-W61-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved in PROD (S9, W65-S1), off-project and now answering 200 (S2), or a worker's cell-wording reading superseded by later cells with the bound harnesses green (the rest); no page defect stands.",
    "spec_asserts": "Each row records an observation made while building or walking; none names a page defect still standing.",
    "world_is": "Each is resolved or superseded as the grounds state.",
    "notes": "No page change owed."
  },
  {
    "id": "DSGN_AMGTV1-Z-C-S23",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T05:58:00Z",
    "one_line": "Two verification-instrument residuals graduate to the CTO (INERT, not slug-holding): errorEmpty's three starred-case checks pass by ABSENCE since StarredList left the chatter face (W56-S4); walk.mjs's occluded-popover check reads every pointer-events-none tooltip as covered (S11). Also: walk.mjs labels the timeline finding FWD-6 while the PRD's timeline is FWD-5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-W56-S4 world_is: unresolved_row_navigates, a_click_sent_a_ticker, error_claims_no_daily_row each expected false and green because no row renders.",
        "Z-S11: walk.mjs:102-111 document.elementFromPoint skips pointer-events-none; round21 hoverprobe BA 13 of 13, AMD 10 of 10 with the corrected hit-test.",
        "tmp/ui-walk/20261001T164049Z/findings.json:744, :869 rule 'FWD-6: bursts of coverage appear as marked events'; DSGN_AMGTV1_PRD.md:85 FWD-5 is the timeline, :93 FWD-6 is the Thesis cards."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W56-S4",
      "DSGN_AMGTV1-Z-S11"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "A green check grades the behaviour it names.",
    "world_is": "Three errorEmpty checks and walk.mjs's occlusion check grade nothing on the faces they name; walk.mjs's FWD labels are an older numbering.",
    "notes": "FOR THE CTO: one instrument batch cell (or the ui-walk skill owner for walk.mjs); none holds the close."
  }
]
```

-- 3.0.0_SA_CVO~Z
