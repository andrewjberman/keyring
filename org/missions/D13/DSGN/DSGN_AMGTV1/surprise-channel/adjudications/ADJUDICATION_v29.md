# DSGN_AMGTV1 -- FWD-15 AND FWD-20 RE-READ ON THE AMENDED INSTRUMENT: both REALIZED on PROD's code

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~16:2xZ
**Ask:** `2.0.0_SA_COO~D` msg 28565 (round 28, `round28/ROUND28_CLOSE.md`): re-run the render check for FWD-15 and FWD-20 on portal
DEV `42405d2d`.

## What was run, and on which bytes

- **The instrument.** `42405d2d` differs from PROD's tree `fa529337` only in the instrument (`scripts/ui-measure.mjs`,
  `scripts/ui-contract-check.mjs`) and the contract fixture (`__harness__/tests/uiContractFixtures.json`). No Security Analysis
  page code differs (`git diff --stat fa529337 42405d2d`). Worktree 70's head `2f2bf71d` carries `42405d2d`'s instrument
  byte-for-byte (`42405d2d` is its ancestor; no `scripts/` diff between them).
- **The page.** This seat's own build of PROD's tree (`scratchpad/dist-prod-fa529337`).
- **So this one run grades PROD's page with the amended instrument**, and equally DEV `42405d2d`, whose Security Analysis code is
  PROD's.

## Results

| read | result |
|---|---|
| `ui-contract-check.mjs --dist dist-prod-fa529337 --states-sweep` (16:03-16:12Z) | **GRADES PASS 76, FAIL 0, NOT_EXERCISED 0, N/A 1 -- RESULT: PASS** |
| `fwd15_modelTable` (model) | **PASS**: 14 columns, tabular 134/134, white panel, 2 REFUSED rows, **1 ABSENT footnote naming 1 row** (the ABSENT half is now exercised) |
| `fwd16_absentColumns` (peers) | **PASS**: 12 listed = 12 declared, 0 in the table, the chip `derived` with a 696-character test statement |
| `round28/checks/render.cjs C:/tmp/wk-dsgn-amgtv1-70` | **3 of 3 arms**. Arm 3 (planted): the amended fwd16 predicate rejects a column with no served reason and one whose face carries only its name |
| `ui-measure.mjs --self-test --fixture .../uiMeasureFixture.html` | **SELF-TEST OK**: its list includes `NEGATIVE fwd15 refused spans` (false) and `NEGATIVE fwd15 absentRowsInTable` (1), and any miss would print `MISMATCH` |
| FWD-20's other arms (v27, unchanged clauses) | pre-redesign `8fa7abde` FAILS `darkContainers` x4; planted page FAILS 8/8, clean PASSES 8/8; blank 8 NOT_EXERCISED; harnesses green (8/8, 20/20, 32/32) |
| The six PNGs, read by a person | **list.png**: all 18 bubbles now named (KDDI CORP, BP PLC, COSTCO WHOLESALE CORP, WALMART DE MEXICO SAB DE CV ...), so v27's rejection clears; one label is truncated ("TAIWAN SEMICONDUCTOR-SP AI", cosmetic). The other five faces are the same page code read at v27 and accepted |

## Read

- **FWD-15: REALIZED** on PROD's code. A white heatmap panel with tabular numerals; a REFUSED row is one icon and one navy sentence
  spanning the row; ABSENT rows fold into one footnote naming them. Each limb is read, and the instrument can fail each.
- **FWD-20: REALIZED** on PROD's code. The contract's render check PASSES (76 of 76 graded), CAN FAIL (3 of 3 arms, plus the
  amended clauses' negatives), the harnesses are green, and the six PNGs were read by a person with no rejection standing.

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S35",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T16:20:00Z",
    "one_line": "FWD-15 and FWD-20 REALIZED on PROD's code with the amended instrument (42405d2d's scripts and fixture, byte-equal at worktree 2f2bf71d): render on this seat's build of fa529337 = 76 PASS, 0 FAIL, 0 NOT_EXERCISED; fwd15 PASS with REFUSED and ABSENT halves exercised; fwd16 PASS; round28 render.cjs 3/3 (planted fwd16 negative); ui-measure self-test OK (fwd15 negatives); list.png now named (v27 rejection cleared).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal diff --stat fa529337 42405d2d -- scripts/ui-measure.mjs scripts/ui-contract-check.mjs src/pages/SecurityAnalysis: 3 files (two scripts + uiContractFixtures.json); 42405d2d ancestor of 2f2bf71d; no scripts/ diff between them.",
        "node scripts/ui-contract-check.mjs --dist scratchpad/dist-prod-fa529337 --out render-prod-r28 --states-sweep (from C:/tmp/wk-dsgn-amgtv1-70/portal @2f2bf71d), 16:03-16:12Z: GRADES PASS 76 FAIL 0 NOT_EXERCISED 0 N/A 1; RESULT: PASS; fwd15 {columns 14, refusedRows 2, footnotes 1, absentNamed 1}; fwd16 {absentListed 12, absentDeclared 12}.",
        "node org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round28/checks/render.cjs C:/tmp/wk-dsgn-amgtv1-70: 3 of 3 arms, rc 0.",
        "node scripts/ui-measure.mjs --self-test --fixture src/pages/SecurityAnalysis/__harness__/tests/uiMeasureFixture.html: SELF-TEST OK (check list :664-675 includes NEGATIVE fwd15 refused spans and NEGATIVE fwd15 absentRowsInTable).",
        "render-prod-r28/list.png (person read): 18 bubbles, each with a company name."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "COMPLETION_GRADES.round26 @6fe6735934: FWD-15 and FWD-20 NOT_EVALUATED pending the amended clauses and an ABSENT fixture row.",
    "world_is": "Both read REALIZED on PROD's page code with the amended instrument.",
    "notes": "FOR THE CTO: re-grade FWD-15 and FWD-20 REALIZED."
  }
]
```

-- 3.0.0_SA_CVO~Z
