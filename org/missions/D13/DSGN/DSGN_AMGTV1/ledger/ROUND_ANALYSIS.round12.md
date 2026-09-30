# DSGN_AMGTV1 -- ROUND 12 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~13:1xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27148, *"L10 slug DSGN_AMGTV1 round 12 @f77f228ec4 -- lead: live no-dossier
regression"*), which cites `surprise-channel/adjudications/ADJUDICATION_v14.md` (read to EOF, 10,456 B). Issuer: `round12/DRAIN_END_READ.md`
@`123befacf8` and `ROUND12_CLOSE_WALK.md` (walk L).

**Round 12 is CLOSED:** 5 of 5 terminal; `Z-W47-S1` GRADUATED; 5 of 5 judgment criteria graded (m-1, m-2, m-4 and m-5 MET; m-3
PARTIAL). **The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED (the CVO's L9 on walk L and the six render PNGs)

- **m-1 (FWD-20):** the instrument landed and the person-read ran. The style clauses hold on all six PNGs:
  - one dark band;
  - white hairline panels;
  - one purple action;
  - two weights;
  - tabular figures;
  - the designed error and loading states.
  **3 C14 rejections stand** (ruling 3).
- **m-2 (RESAPP FWD-6 page half): MET.** Versions carry their UTC time, and September 10th reads as four distinct labels.
- **m-4 (FWD-11, HARVST FWD-5): MET.** Searched publishers are named, found articles are never credited to a search, and a
  never-collected timeline reads as not quiet.
- **m-5 (FWD-11): MET.** The empty evidence and the empty footer are plain sentences.
- **m-3 (FWD-13): PARTIAL.** The header and What-moved are met. The Model tab's fiscal cells have no unit, no tooltip and no mnemonic.

## 2. RULINGS

1. **THE LIVE NO-DOSSIER REGRESSION (v14 s.0) IS DSGN's TO FIX: the page reads the served per-field reason. RESAPP's shape is NOT
   rolled back.**
   - AMGT_RESAPP ab-2 (ratified, CVO-graded at round 52) serves a no-dossier name as the full `dossier_fields` block, each field ABSENT
     with its reason. A top-level `{status, reason}` now appears only on a failed read.
   - `ThesisTab.tsx:112-125` (DEV `ba62e945`, read by this seat) keys the no-dossier sentence on `dossier.status`, so with the new
     shape it falls through to "none are stated in the research team's pack". **That asserts a pack that does not exist, on every
     no-dossier name.**
   - `C-PRESENTATION-ONLY` says the page renders what the payload carries: the payload carries `thesis_pillars_absent.reason`, so the
     page reads it.
   - **Round-13 cell 1:** the reader handles all three served shapes, each planted in its AC:
     - `thesis_pillars` present;
     - `thesis_pillars_absent` with its reason (6501);
     - a top-level READ_FAILED.
     "none are stated in the research team's pack" is reachable ONLY when a dossier exists and states none.
   - **And the CVO's contract point is adopted in the same cell as its AC, not as a gate:** the ui-contract fixture for `/thesis` is
     refreshed from the LIVE served shape, and the reader test runs against it. The next shape move then fails the test, not the page.
   - **This regression is on site-Z DEV only** (not origin, not PROD). It is why this seat's open-calls card 1 (the portal DEV push) is
     re-carded: push AFTER cell 1 lands.
2. **FWD-13 binds the Model tab's fiscal cells** (m-3): each fiscal figure carries its unit and tabular numerals, and a tooltip with its
   mnemonic and full-precision value, exactly as the header does. This also serves FWD-15's table.
3. **m-1's three C14 rejections are cut, each to one plain sentence or folded, never a count block at rest:**
   - the header's "Description: ABSENT -- no description header scalar ..." becomes one plain sentence ("No company description is on
     file yet"), or nothing where the page has a description slot already;
   - Posture's "FILING EVIDENCE, EACH SIDE" count block folds behind the verdict card's evidence affordance;
   - Exec's "CEO public profile ...: unreadable object -- status=ABSENT query=set absence_class=None." becomes one plain sentence.
   - With them go FWD-11's raw tokens: "PASSAGE P0278", "derived before C-MODEL-WINDOW-AND-ROWS (5)", and the ISO "as of
     2026-09-24T0310Z", which reads as a long-form date.
4. **The `list` title strip is the instrument's error, not the page's** (the CVO: not a C3 rejection). `darkContainers` counts a strip
   INSIDE a band as that band. The AC plants a second, separate dark band, which must still FAIL.
5. **FWD-19's no-permission state needs its lever:** the `--states-sweep` path renders `PanelNoPermission`, so the `fourStates` clause
   can pass. FWD-20 stays NOT REALIZED until the three rejections are cleared and `fourStates` passes.

## 3. FWD GRADES

- **REALIZED, standing:** FWD-4, FWD-9, FWD-10.
- **MET on local DEV, NOT REALIZED until the portal promotion (Andrew's):** FWD-12 (one band, on the five Security states and the list).
- **NOT REALIZED:**
  - FWD-11 (the C14 blocks and raw tokens);
  - FWD-13 (Model cells);
  - FWD-20 (3 rejections, `fourStates`);
  - FWD-14..19 (now gradable by the landed instrument, and graded at round 13 once the fixtures are refreshed);
  - FWD-1, 2, 3, 5, 6, 7, 8 as round 11.
- **3 of 20 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 13 in ONE issuance

| # | cell | FWD | risk | note |
|---|---|---|---|---|
| 1 | **The no-dossier reader** (ruling 1) + the `/thesis` fixture refreshed from the live shape | 11, CORPUS six | LOCAL | The AC plants the three shapes. 6501 reads "no research dossier for this name" again on the walk. **It leads the round.** |
| 2 | **Model fiscal cells: unit, tabular numerals, tooltip** (ruling 2) | 13, 15 | LOCAL | The AC hovers a BA fiscal cell and reads its mnemonic and full value. The DOM carries 0 floats with more than 6 fractional digits. |
| 3 | **The three C14 blocks + the FWD-11 raw tokens** (ruling 3) | 11, 20 | LOCAL | The AC greps the rendered DOM of the six states for each quoted string: 0 hits. |
| 4 | **The instrument:** an in-band strip counts as the band; the fixture refresh for FWD-14..19 | 20 | LOCAL | The AC: the list reads `darkContainers` 1, and a planted separate band FAILs. |
| 5 | **`PanelNoPermission` via `--states-sweep`** (ruling 5) | 19, 20 | LOCAL | The AC: `fourStates` PASSES, captured at least once. |
| 6 | **The FWD-14..19 grading pass** on the refreshed instrument | 14-19 | LOCAL read | It follows 4. It prints each clause's value per state, and a NOT_EXERCISED clause is never a PASS. |

**Fan-out:** 1, 2, 3, 4 and 5 are independent; 6 follows 4. **NOT cells:** `publishers_found_codes` on the page (it waits on
AMGT_RESAPP round-53's slash-key window build).

## 5. ACTS ONLY ANDREW CAN DO (cited)

- The portal DEV push, after cell 1 lands, and the promotion [CLAUDE.md Portal].
- Remove the worktrees `/c/tmp/wk-dsgn-amgtv1-18..48` and the scratch roots [recursive deletion].

## Compiler Tools

- The CVO's v14: walk L shots 163, 249, 334 and 394, the six PNGs, and its `dossier_fields` read.
- This seat read `ThesisTab.tsx:105-128` at portal DEV `ba62e945` (`git -C portal show`) and confirmed the reader keys on
  `dossier.status`.
