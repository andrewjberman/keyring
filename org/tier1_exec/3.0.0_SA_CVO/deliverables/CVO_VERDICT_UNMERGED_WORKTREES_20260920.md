# CVO verdict -- the six unmerged worktrees, per commit

`3.0.0_SA_CVO`, 2026-09-20T19:46:58Z. Answering **0.0.0_AB_MSTR 98697**, Andrew-direct at that terminal ~19:0xZ, verbatim:
*"route the unmerged worktrees to CVO for a verdict"*. Packet:
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/CVO_REVIEW_PACKET_UNMERGED_WORKTREES_20260920.md` @`423d855bf7`.

Vintage of every measurement below: HEAD `e837e2eeb5`, origin/CLOUD `490b619ddf`, origin/SITEZ `047aee5478`.

## THE OPERATIVE ANSWER, BEFORE THE DETAIL

**NOT ONE OF THE SIX WORKTREES CLEARS FOR REMOVAL.** The verdict is per commit as asked, but the
removal decision is per WORKTREE, and a worktree is removable only if EVERY commit it carries is
SUPERSEDED. Every one of the six carries at least one commit that is not. The disk cannot be
recovered from this pool without losing work.

| verdict | commits |
|---|---|
| SUPERSEDED | 92 |
| UNIQUE | 29 |
| PARTIAL | 17 |
| RECUSED | 1 |
| **total** | **139** |

## THE INSTRUMENT, AND THE TWO TIMES IT WAS WRONG BEFORE IT WAS RIGHT

**FIRST PASS -- `git cherry` (patch-id). ABANDONED.** It returned `-` ZERO times across all six
branches. I did not report that as *nothing is superseded*: an all-zero result with no control is
the signature of a degenerate instrument, and cherry also answers the wrong question -- a squash or
an independent redo carries the substance while the patch-id differs. (It also lists only
non-merge commits, which is why it saw 100 of d13's 121.)

**SECOND PASS -- byte-identity at HEAD. ITS POSITIVE CONTROL FAILED, AND THAT IS WHY IT IS NOT THE
ANSWER.** `3dcb249826` is on origin/CLOUD and scored PARTIAL. Cause, measured: it touches two paths
and ONE of them had been edited once since, so the blob differs. That test asks *is this commit's
output still CURRENT*, not *did its substance LAND*. It was wrong in the SAFE direction -- it
over-reported UNIQUE, 87 against the true 30 -- and it would still have produced a useless verdict.

**THIRD PASS -- CONTAINMENT, which is what this record reports.** Of the substantive lines a commit
ADDED, how many appear in HEAD's copy of that same path? Containment survives later edits, squashes
and independent redos. >=95% present = SUPERSEDED, <=5% = UNIQUE, between = PARTIAL.
CONTROLS, both behaving: POSITIVE `3dcb249826` (on origin/CLOUD) -> 1484/1484 lines present, LANDED.
NEGATIVE `f2cac74c60` (known unlanded) -> 0/400, UNIQUE.

**AND IT IS WRONG-OBJECT FOR TWO FILE KINDS, WHICH I MEASURED SEPARATELY RATHER THAN LETTING THE
DEFAULT STAND:**

- **GITLINKS (11 commits).** A `portal` bump has no lines; its substance lives in ANOTHER REPOSITORY.
  Containment scored all 11 UNIQUE, which is meaningless. Measured on the right instrument -- the
  portal submodule -- **all 11 target commits exist AND are ancestors of BOTH origin/DEV and
  origin/PROD**. The portal-side work is fully landed; only the pointer value is local. All 11 are
  SUPERSEDED. That is 11 of the 41 apparent-UNIQUE corrected by asking a different repository.
- **BINARY RENDERS (2 commits).** A PNG produces no `+` lines at all. `d09508296c`'s image is
  byte-identical at HEAD (SUPERSEDED); `87185ad3f2`'s path is occupied at HEAD by a DIFFERENT
  capture, so that exact image exists nowhere else (UNIQUE, graded conservatively).

**RECUSAL.** One commit of the 139 is this seat's own -- `77a5acbf40`, the DSGN_REBRND round-1
L8/L9 record. I do not grade my own work; it is marked RECUSED and handed to `1.0.0_SA_CTO`.
98697 offered the whole d13 branch on that ground; the measured overlap is ONE commit of 121, so
recusing the commit rather than the branch costs nothing and keeps the other 120 graded.

## WHAT IS AT RISK, IN ORDER OF WHAT IT WOULD COST TO LOSE

1. **A COMPLETED CELL THAT NEVER LANDED** -- `wk-mdpf_taxsma-1-1`, 3 commits, all UNIQUE, 0 of 2624
   added lines present at HEAD. `infra/aws/ec2/opal-gateway/app/taxsma_workbook.py` (423 lines) does
   not exist at HEAD at all. `1.0.0_SA_CTO` reached the same conclusion from a different direction
   (the order reads `pending` on CLOUD and `complete` on the worktree, 98699); this is that finding
   corroborated on an instrument that never looks at a status tag. **This is a finding for
   MDPF_TAXSMA's issuer, not a disk question** -- and it means the estate's open-order census counts
   TX-g-1 as open while the work is done.
2. **AN ANDREW-DIRECT RECORD THAT EXISTS NOWHERE ELSE** -- `897c5f99b4` carries
   `laneD_ANDREW_DIRECT_20260911_134xZ_FETCH_LATO_HOLD_DEV.md`, 52 added lines, **0 at HEAD**.
3. **15 KRNY COMMITS, ALL UNIQUE, 0 LINES PRESENT ANYWHERE** -- four branches of `1.7.0_SA_KRN~Y`'s
   C3 work: design documents, fixtures and proof-of-spec JSON. Nothing of it is at HEAD.
4. **SESSION LOGS AND ROUND RECORDS** of `2.0.0_SA_COO~D`'s DSGN_REBRND work, several naming
   Andrew's own instructions (the indigo accent, the favicon).

## PER-COMMIT VERDICTS

### `wk-mdpf_taxsma-1-1` -- 3 commits: UNIQUE 3

REMOVABLE: **NO** -- 3 commit(s) are not SUPERSEDED.

| verdict | commit | author | date | subject | basis |
|---|---|---|---|---|---|
| UNIQUE | `f2cac74c60` | 0.9.0_WK_MDPF_TAXSMA~1 | 2026-09-15 | complete(MDPF_TAXSMA.TO-TX-g-1, 0.9.0_WK_MDPF_TAXSMA~1): proof of spec, result record, status fl | 0 of 400 added lines present at HEAD |
| UNIQUE | `8dce9aeb0b` | 0.9.0_WK_MDPF_TAXSMA~1 | 2026-09-15 | fix(MDPF_TAXSMA.TO-TX-g-1, 0.9.0_WK_MDPF_TAXSMA~1): three instrument defects the first probe run | 0 of 14 added lines present at HEAD |
| UNIQUE | `6abf60e5d5` | 0.9.0_WK_MDPF_TAXSMA~1 | 2026-09-15 | feat(MDPF_TAXSMA.TO-TX-g-1, 0.9.0_WK_MDPF_TAXSMA~1): GET /ms/taxsma-workbook capability, route,  | 24 of 2210 added lines present at HEAD |

### `feature/d13-visual-elevation` -- 121 commits: PARTIAL 17, RECUSED 1, SUPERSEDED 92, UNIQUE 11

REMOVABLE: **NO** -- 29 commit(s) are not SUPERSEDED.

| verdict | commit | author | date | subject | basis |
|---|---|---|---|---|---|
| UNIQUE | `c8cd12b2c0` | 2.0.0_SA_COO~D | 2026-09-11 | log(2.0.0_SA_COO~D): move the DSGN_REBRND session record into logs/2026-09-11/ and give it the s | 0 of 10 added lines present at HEAD |
| UNIQUE | `c5cc3ed72a` | 2.0.0_SA_COO~D | 2026-09-11 | log(2.0.0_SA_COO~D): REBOOT STATE for DSGN_REBRND -- written for a successor, per the managed wi | 0 of 86 added lines present at HEAD |
| UNIQUE | `87185ad3f2` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | render(DSGN_REBRND RB-s-4): re-capture /market from the committed tree | binary render; the path is occupied at HEAD by a DIFFERENT capture, so this exact image exists nowhere else -- graded conservatively, an equivalent-pu |
| UNIQUE | `bfd50d24d4` | 2.0.0_SA_COO~D | 2026-09-13 | log(2.0.0_SA_COO~D): DSGN_REBRND checkpoint -- resumed on Andrew's word, slots ~1 (RB-s-4) and ~ | 0 of 75 added lines present at HEAD |
| UNIQUE | `6d112cd5ee` | 2.0.0_SA_COO~D | 2026-09-14 | log(2.0.0_SA_COO~D): handoff update -- RB-s-14 landed complete on its worker branch (1df06e9112) | 0 of 5 added lines present at HEAD |
| UNIQUE | `b7df90d1b1` | 2.0.0_SA_COO~D | 2026-09-14 | log(2.0.0_SA_COO~D): reboot handoff -- Andrew's indigo-accent and favicon asks investigated and  | 0 of 167 added lines present at HEAD |
| UNIQUE | `a800f94050` | 2.0.0_SA_COO~D | 2026-09-14 | log(2.0.0_SA_COO~D): DSGN_REBRND -- RB-s-13 recovered from a network cut and drained (65 of 96 r | 0 of 88 added lines present at HEAD |
| UNIQUE | `962874be33` | 2.0.0_SA_COO~D | 2026-09-14 | log(2.0.0_SA_COO~D): DSGN_REBRND checkpoint 4a -- the CVO's watcher cannot see this project's ch | 0 of 22 added lines present at HEAD |
| UNIQUE | `09f23f9648` | 2.0.0_SA_COO~D | 2026-09-14 | log(2.0.0_SA_COO~D): DSGN_REBRND checkpoint 4 -- 11 of 15 complete, RB-s-10 reopened on AC2R, th | 0 of 32 added lines present at HEAD |
| UNIQUE | `c2c8712b53` | 2.0.0_SA_COO~D | 2026-09-14 | log(2.0.0_SA_COO~D): DSGN_REBRND checkpoint 3 -- RB-s-5 and RB-s-8 drained (9 of 15), the W2-S12 | 0 of 21 added lines present at HEAD |
| UNIQUE | `a92361d37e` | 2.0.0_SA_COO~D | 2026-09-14 | log(2.0.0_SA_COO~D): DSGN_REBRND checkpoint 2 -- RB-s-4 and RB-s-7 fully drained (7 of 15), two  | 0 of 17 added lines present at HEAD |
| PARTIAL | `07768ad8e4` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | deliverables(DSGN_REBRND.TO-RB-s-4): ordered-scales proof + result -- 3 PASS, 1 FAIL, 1 recorded | 72 of 241 added lines present at HEAD |
| PARTIAL | `f0bf49ade2` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | complete(DSGN_REBRND.TO-RB-s-3): canvas+surfaces proof + result, status -> complete | 303 of 320 added lines present at HEAD |
| PARTIAL | `897c5f99b4` | 2.0.0_SA_COO~D | 2026-09-11 | record(Andrew-direct 13:4xZ) + L6 amend(DSGN_REBRND.TO-RB-s-3): "Yes fetch lato" closes this lan | 28 of 80 added lines present at HEAD |
| PARTIAL | `37e88de91c` | 2.0.0_SA_COO~D | 2026-09-11 | L7 drain(DSGN_REBRND.TO-RB-s-2): typography merged from slot ~1 -- and the CSS-parse break RB-s- | 150 of 325 added lines present at HEAD |
| PARTIAL | `5fce0157ef` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | deliverables(DSGN_REBRND.TO-RB-s-2): typography proof-of-spec + result -- 4 PASS, 1 FAIL, 1 reco | 91 of 266 added lines present at HEAD |
| PARTIAL | `84dc6c9648` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-11 | fix(DSGN_REBRND.TO-RB-s-11): proof-of-spec instance pinned portal-repo artifacts to PENDING-THIS | 6 of 9 added lines present at HEAD |
| PARTIAL | `0f88ccde18` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-11 | worker(DSGN_REBRND.TO-RB-s-11): one-renderer -- deliverables + surprise rows; status stays pendi | 147 of 242 added lines present at HEAD |
| PARTIAL | `8c0b1af657` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | channel(DSGN_REBRND): open the project's surprise channel, rows W1-S1..S4 from TO-RB-s-1 | 74 of 85 added lines present at HEAD |
| PARTIAL | `296214fbd4` | 2.0.0_SA_COO~D | 2026-09-13 | drain(DSGN_REBRND.TO-RB-s-4): merge 0.9.0_WK_DSGN_REBRND~1 -- RB-s-4 complete under Amendments 1 | 264 of 301 added lines present at HEAD |
| PARTIAL | `4202b447a8` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-13 | proof(DSGN_REBRND.TO-RB-s-4): complete under Amendments 1 + 1a -- ladder back on canon, aum.ts o | 102 of 138 added lines present at HEAD |
| PARTIAL | `1cceadbf81` | 2.0.0_SA_COO~D | 2026-09-13 | refresh(wk-dsgn_rebrnd-1e): take feature/d13-visual-elevation into slot ~1's branch -- RB-s-4 Am | 638 of 740 added lines present at HEAD |
| PARTIAL | `edfc97ed99` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-14 | rows+carriers(DSGN_REBRND.TO-RB-s-5 Amendment 1, 0.9.0_WK_DSGN_REBRND~2): two channel rows and t | 42 of 45 added lines present at HEAD |
| PARTIAL | `bf25345dc9` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | deliverables(RB-s-10): proof, result, census and renders -- order stays OPEN on RB10-AC2 (row DS | 403 of 440 added lines present at HEAD |
| PARTIAL | `3623210d7c` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-8): merge 0.9.0_WK_DSGN_REBRND~2 -- RB-s-8 complete (instance VALID, 4 | 500 of 578 added lines present at HEAD |
| PARTIAL | `fa8d87fa08` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-8): AMENDMENT 1 -- REOPENED for one act, a row re-mint: this branch's  | 5 of 6 added lines present at HEAD |
| PARTIAL | `8cda2454ab` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-14 | RB-s-8 (DSGN_REBRND): the standing colour law rewritten in place onto portal/DESIGN.md -- Andrew | 274 of 352 added lines present at HEAD |
| PARTIAL | `c8ccbdb4f2` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-7): AMENDMENT 2 -- REOPENED for one act, the RB7-AC4 build by a fresh  | 15 of 16 added lines present at HEAD |
| SUPERSEDED | `9cd16f99f7` | 2.0.0_SA_COO~D | 2026-09-11 | amend(DSGN_REBRND.TO-RB-s-4): AMENDMENT 1 -- the duration ladder is CANON, the cell's premise wa | 339 of 346 added lines present at HEAD |
| SUPERSEDED | `f6aa9c7e19` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | channel(DSGN_REBRND): rows W1-S13, W1-S14 from TO-RB-s-4 | 40 of 40 added lines present at HEAD |
| SUPERSEDED | `1bedb59788` | 2.0.0_SA_COO~D | 2026-09-11 | design(DSGN_REBRND): THE INVERSION RULE -- a defined logic for light-on-dark -> dark-on-light, f | 101 of 101 added lines present at HEAD |
| SUPERSEDED | `11768022aa` | 2.0.0_SA_COO~D | 2026-09-11 | design(DSGN_REBRND): Andrew rules OPTION A -- panels go light -- and the semantic palette is mea | 37 of 37 added lines present at HEAD |
| SUPERSEDED | `401ad3b961` | 2.0.0_SA_COO~D | 2026-09-11 | design(DSGN_REBRND): recover the layer map from the flattening diff -- 7 tokens hid 24 effective | 156 of 156 added lines present at HEAD |
| SUPERSEDED | `4e732e2771` | 2.0.0_SA_COO~D | 2026-09-11 | L7 drain(DSGN_REBRND.TO-RB-s-3): canvas TERMINAL -- the canvas is #F4F6FA on both routes by the  | 385 of 385 added lines present at HEAD |
| SUPERSEDED | `cf5a65f497` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | fix(DSGN_REBRND.TO-RB-s-3): pin the two capture rows to the commits that carry them | 6 of 6 added lines present at HEAD |
| SUPERSEDED | `d09508296c` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | render(DSGN_REBRND RB-s-3): re-capture /market from the repaired tree | binary render; the PNG at HEAD is byte-identical to this commit's |
| SUPERSEDED | `94b2040205` | 2.0.0_SA_COO~D | 2026-09-11 | row(DSGN_REBRND-S1) + L6 amend(RB-s-9): the divergence-bar label is painted over by the centre o | 127 of 127 added lines present at HEAD |
| SUPERSEDED | `07a6dc7a5f` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | fix(DSGN_REBRND RB-s-3): RB3-AC5 regressed after the flip -- repaired and re-verified | 48 of 48 added lines present at HEAD |
| SUPERSEDED | `cf9aabf452` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | channel(DSGN_REBRND): rows W1-S9..S11 from TO-RB-s-3 -- the canvas ceiling, ink-from-a-backgroun | 57 of 57 added lines present at HEAD |
| SUPERSEDED | `76addd4f15` | 2.0.0_SA_COO~D | 2026-09-11 | integrate(DSGN_REBRND): bump the portal gitlink -- the typeface is now Lato, self-hosted, no net | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `a6ef12f982` | 2.0.0_SA_COO~D | 2026-09-11 | L7 drain(DSGN_REBRND.TO-RB-s-2): typography TERMINAL -- Lato 400 and 600 self-hosted from the on | 205 of 205 added lines present at HEAD |
| SUPERSEDED | `cf406a823c` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | complete(DSGN_REBRND.TO-RB-s-2): typography proof + result, status -> complete | 185 of 185 added lines present at HEAD |
| SUPERSEDED | `d4eefbe04e` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | channel(DSGN_REBRND): row W1-S8 -- the product's bold weight is a SemiBold, not a Bold | 20 of 20 added lines present at HEAD |
| SUPERSEDED | `95158c4d37` | 2.0.0_SA_COO~D | 2026-09-11 | L6 amend(DSGN_REBRND.TO-RB-s-2): the fonts were already on this box -- W1-S5 disarmed from BLOCK | 20 of 20 added lines present at HEAD |
| SUPERSEDED | `511f9c2721` | 2.0.0_SA_COO~D | 2026-09-11 | integrate(DSGN_REBRND): bump the portal gitlink to the feature branch tip -- three cells of port | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `7ebe04bfdb` | 2.0.0_SA_COO~D | 2026-09-11 | L7 drain(DSGN_REBRND.TO-RB-s-11): one rendering system merged from slot ~2 under the amended ord | 319 of 319 added lines present at HEAD |
| SUPERSEDED | `91212d2220` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | channel(DSGN_REBRND): rows W1-S5..S7 from TO-RB-s-2 -- font-binary gap, a broken AC4 check, an R | 59 of 59 added lines present at HEAD |
| SUPERSEDED | `46495a26a9` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-11 | complete(DSGN_REBRND.TO-RB-s-11): one renderer -- all five mechanical criteria PASS by output un | 85 of 85 added lines present at HEAD |
| SUPERSEDED | `f601f76862` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-11 | channel(DSGN_REBRND): row W2-S4 -- the amended TO reached this worktree but the merged channel d | 102 of 102 added lines present at HEAD |
| SUPERSEDED | `4de713e222` | 2.0.0_SA_COO~D | 2026-09-11 | L6 amend(DSGN_REBRND.TO-RB-s-11): a word cloud is not a chart renderer -- @visx/wordcloud carved | 17 of 17 added lines present at HEAD |
| SUPERSEDED | `4c21020c6b` | 2.0.0_SA_COO~D | 2026-09-11 | L7 drain(DSGN_REBRND.TO-RB-s-1): token spine merged from slot ~1 -- one writer (22 literals relo | 315 of 315 added lines present at HEAD |
| SUPERSEDED | `cc480cc723` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-11 | complete(DSGN_REBRND.TO-RB-s-1): token spine proof-of-spec + result, status -> complete | 242 of 242 added lines present at HEAD |
| SUPERSEDED | `1a6d26c833` | 2.0.0_SA_COO~D | 2026-09-11 | L6 amend(DSGN_REBRND.TO-RB-s-10): NO-PERMISSION renders nowhere in the product -- the cell is SC | 21 of 21 added lines present at HEAD |
| SUPERSEDED | `f850fd6f96` | 2.0.0_SA_COO~D | 2026-09-11 | L7 drain(DSGN_REBRND.TO-RB-s-12): affected-surface inventory merged from slot ~3 -- 99 rows over | 961 of 961 added lines present at HEAD |
| SUPERSEDED | `80dfead12e` | 0.9.0_WK_DSGN_REBRND~3 | 2026-09-11 | L7(DSGN_REBRND RB-s-12): affected-surface inventory minted -- 24 routes (router's own count) x e | 961 of 961 added lines present at HEAD |
| SUPERSEDED | `fb274b50c6` | 2.0.0_SA_COO~D | 2026-09-13 | amend(DSGN_REBRND.TO-RB-s-4): drop a literal status tag from the Amendment 2 note -- one tag per | 1 of 1 added lines present at HEAD |
| SUPERSEDED | `aaa8a79cf2` | 2.0.0_SA_COO~D | 2026-09-13 | row(DSGN_REBRND-S2): Option A's inversion work is covered by no cell -- round 1 closes with the  | 19 of 19 added lines present at HEAD |
| SUPERSEDED | `768bebce28` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-13 | complete(DSGN_REBRND.TO-RB-s-7): the contract -- proof VALID rc=0, 5 of 5 mechanical PASS by out | 441 of 452 added lines present at HEAD |
| SUPERSEDED | `d7d9ce14b4` | 2.0.0_SA_COO~D | 2026-09-13 | amend(DSGN_REBRND.TO-RB-s-4): AMENDMENT 2 -- REOPENED on row W1-S15: the scatter's ULT/LT benchm | 61 of 63 added lines present at HEAD |
| SUPERSEDED | `65a4bad6a2` | 2.0.0_SA_COO~D | 2026-09-13 | integrate(DSGN_REBRND): bump the portal gitlink to 547d12fd -- RB-s-4's canon ladder and one-hue | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `b835dbd931` | 2.0.0_SA_COO~D | 2026-09-13 | amend(DSGN_REBRND.TO-RB-s-9): proof_of_spec validates RB9-AC7 -- the row-S1 collision criterion  | 3 of 3 added lines present at HEAD |
| SUPERSEDED | `459af4b20a` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-13 | row(DSGN_REBRND W1-S15, W1-S16, W1-S17): RB-s-4 resume under Amendment 1 -- scatter pair vs the  | 58 of 58 added lines present at HEAD |
| SUPERSEDED | `f6f7bfa706` | 2.0.0_SA_COO~D | 2026-09-13 | amend(DSGN_REBRND.TO-RB-s-7 + RB-s-8): AMENDMENT 1 -- the contract carries the canon lock, Optio | 91 of 91 added lines present at HEAD |
| SUPERSEDED | `96e43eca94` | 2.0.0_SA_COO~D | 2026-09-13 | amend(DSGN_REBRND.TO-RB-s-4): AMENDMENT 1a -- the proof_of_spec id list matches expected_criteri | 5 of 5 added lines present at HEAD |
| SUPERSEDED | `ae8877f451` | 2.0.0_SA_COO~D | 2026-09-14 | issuer(DSGN_REBRND, 2.0.0_SA_COO~D): rb5-accent-check site 4 no longer requires the sidebar's wh | 4 of 4 added lines present at HEAD |
| SUPERSEDED | `e03e8d44fb` | 2.0.0_SA_COO~D | 2026-09-14 | sync(DSGN_REBRND, RULING G): the feature branch's PRD copy replaced with CLOUD's bytes at the si | 70 of 70 added lines present at HEAD |
| SUPERSEDED | `b90df6283e` | 3.0.0_SA_CVO | 2026-09-14 | steplog(DSGN_REBRND round 1, 3.0.0_SA_CVO): L8 compile, L9 grading, L9 carriers and the L10 slug | 50 of 50 added lines present at HEAD |
| SUPERSEDED | `14ca97a535` | 3.0.0_SA_CVO | 2026-09-14 | remediate(DSGN_REBRND round 1): the round-1 remediation slug -- 37 rows, all OPEN (33 graduated  | 663 of 663 added lines present at HEAD |
| SUPERSEDED | `baeeff2654` | 3.0.0_SA_CVO | 2026-09-14 | adjudicate(DSGN_REBRND round 1): C-S1..C-S14 carry all 67 rows -- 26 dismissed, 8 DECOMP_INVALID | 443 of 443 added lines present at HEAD |
| RECUSED | `77a5acbf40` | 3.0.0_SA_CVO | 2026-09-14 | l8-l9(DSGN_REBRND round 1): 67 new rows compiled, 22 judgment criteria graded -- 10 PASS, 9 FAIL | authored by 3.0.0_SA_CVO -- not graded by its own author; handed to 1.0.0_SA_CTO |
| SUPERSEDED | `a1d0a7451c` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-15): merge 0.9.0_WK_DSGN_REBRND~1 -- Andrew's side-by-side pack (3 rou | 397 of 397 added lines present at HEAD |
| SUPERSEDED | `1fb309e862` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | work(DSGN_REBRND.TO-RB-s-15): Andrew's side-by-side pack -- 3 routes BEFORE\|AFTER at 1440, no f | 378 of 378 added lines present at HEAD |
| SUPERSEDED | `8a43f2420b` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | row(DSGN_REBRND-W1-S38): the pre-round /market tab body is capture-timing-dependent -- 2 capture | 19 of 19 added lines present at HEAD |
| SUPERSEDED | `3327c5a890` | 2.0.0_SA_COO~D | 2026-09-14 | row(DSGN_REBRND-S4): prd-signoff.py hid every stamp refusal (a 6-line tail against safe-commit's | 18 of 18 added lines present at HEAD |
| SUPERSEDED | `c965bdf8b3` | 2.0.0_SA_COO~D | 2026-09-14 | integrate(DSGN_REBRND): bump the portal gitlink to 086371dd -- the RB-s-5 Amendment 1 drain (And | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `a72b78fa45` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-5 Amendment 1): merge 0.9.0_WK_DSGN_REBRND~2 -- order complete (issuer | 692 of 695 added lines present at HEAD |
| SUPERSEDED | `ed2aaccf85` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-14 | worker(DSGN_REBRND.TO-RB-s-5 Amendment 1, 0.9.0_WK_DSGN_REBRND~2): identity accents restored, pr | 650 of 650 added lines present at HEAD |
| SUPERSEDED | `3b45dfb5e3` | 2.0.0_SA_COO~D | 2026-09-14 | reopen(DSGN_REBRND.TO-RB-s-5): Amendment 1 -- Andrew's identity accents (title rule, header subt | 205 of 209 added lines present at HEAD |
| SUPERSEDED | `8d30b753f6` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-14): merge 0.9.0_WK_DSGN_REBRND~1 -- RB-s-14 complete (issuer re-grade | 2403 of 2403 added lines present at HEAD |
| SUPERSEDED | `1df06e9112` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | boundary-parity(DSGN_REBRND.TO-RB-s-14): the taste extractor run in place on /market, /positioni | 2332 of 2332 added lines present at HEAD |
| SUPERSEDED | `56997da6ea` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | row(DSGN_REBRND-W1-S34..S37): RB-s-14's boundary exercise -- no site render on record, AC1 count | 71 of 71 added lines present at HEAD |
| SUPERSEDED | `ff2bcda841` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-13): merge 0.9.0_WK_DSGN_REBRND~3 -- RB-s-13 complete (instance VALID; | 9745 of 9745 added lines present at HEAD |
| SUPERSEDED | `7333b9c5a1` | 0.9.0_WK_DSGN_REBRND~3 | 2026-09-14 | render-coverage(DSGN_REBRND.TO-RB-s-13): 96 of 96 render obligations and 58 of 58 keyboard walks | 9745 of 9745 added lines present at HEAD |
| SUPERSEDED | `0dacfd8dfb` | 2.0.0_SA_COO~D | 2026-09-14 | row(DSGN_REBRND-S3): the Global RSI bars still render lime on an ordered scale no cell owned, an | 20 of 20 added lines present at HEAD |
| SUPERSEDED | `4721f1f6ee` | 2.0.0_SA_COO~D | 2026-09-14 | integrate(DSGN_REBRND): bump the portal gitlink to a65b939a -- RB-s-10's four designed states re | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `77b203a426` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-10): merge 0.9.0_WK_DSGN_REBRND~1 -- RB-s-10 complete under Amendment  | 504 of 504 added lines present at HEAD |
| SUPERSEDED | `bccea536d0` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | complete(DSGN_REBRND.TO-RB-s-10): Amendment 1 executed -- RB10-AC2R reads MIGRATED; proof re-val | 77 of 77 added lines present at HEAD |
| SUPERSEDED | `7cf86f3a0f` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-13): AMENDMENT 1 -- RB13-AC2 retired for RB13-AC2R before spawn: the c | 63 of 63 added lines present at HEAD |
| SUPERSEDED | `e8be89b7fb` | 2.0.0_SA_COO~D | 2026-09-14 | refresh(wk-dsgn_rebrnd-1i): take feature/d13-visual-elevation into slot ~1's branch -- RB-s-10 A | 52 of 52 added lines present at HEAD |
| SUPERSEDED | `2d59c8e34c` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-10): AMENDMENT 1 -- on row W1-S32, RB10-AC2 is retired for RB10-AC2R:  | 52 of 52 added lines present at HEAD |
| SUPERSEDED | `c3b2416965` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | row(DSGN_REBRND-W1-S32, -W1-S33): RB10-AC2 is blocked by one hit outside the grant; each state p | 36 of 36 added lines present at HEAD |
| SUPERSEDED | `36d952f286` | 2.0.0_SA_COO~D | 2026-09-14 | integrate(DSGN_REBRND): bump the portal gitlink to e216de95 -- RB-s-9's C10 spacing and the dive | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `682df45328` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-9): merge 0.9.0_WK_DSGN_REBRND~1 -- RB-s-9 complete (instance VALID, 4 | 853 of 853 added lines present at HEAD |
| SUPERSEDED | `38f1c57663` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | complete(DSGN_REBRND.TO-RB-s-9): density -- proof-of-spec, result, captures and measurements; RB | 801 of 801 added lines present at HEAD |
| SUPERSEDED | `d30bc6bc32` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | row(DSGN_REBRND W1-S29..S31): RB-s-9 -- the contract names no page terminator; the lower third o | 52 of 52 added lines present at HEAD |
| SUPERSEDED | `92a8d363c7` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-15): AMENDMENT 1 -- the BEFORE renders are not on disk; pin the pre-ro | 16 of 16 added lines present at HEAD |
| SUPERSEDED | `ac6881d3f0` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-14): AMENDMENT 1 -- the extractor lives only in the main workspace; st | 11 of 11 added lines present at HEAD |
| SUPERSEDED | `faa2c48c37` | 2.0.0_SA_COO~D | 2026-09-14 | integrate(DSGN_REBRND): bump the portal gitlink to fb6f5023 -- RB-s-6's focus ring and the shell | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `d1e4734e06` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-9): fold in row W1-S24 -- a fifth stale "silver canvas" comment in Tic | 6 of 6 added lines present at HEAD |
| SUPERSEDED | `9e73442a44` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-6): merge 0.9.0_WK_DSGN_REBRND~1 -- RB-s-6 complete (instance VALID, 4 | 1142 of 1142 added lines present at HEAD |
| SUPERSEDED | `7a7364907b` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | proof(DSGN_REBRND.TO-RB-s-6): complete -- focus visible everywhere from DESIGN.md C11, the shell | 1023 of 1023 added lines present at HEAD |
| SUPERSEDED | `0fd33e1151` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | surprise(DSGN_REBRND RB-s-6): rows W1-S22..W1-S28 -- no ring token to use, the cited census row  | 119 of 119 added lines present at HEAD |
| SUPERSEDED | `afd6fd58b7` | 2.0.0_SA_COO~D | 2026-09-14 | integrate(DSGN_REBRND): bump the portal gitlink to 7bc22b6c -- RB-s-8's rewritten portal Color l | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `b6f276257c` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-14 | drain(DSGN_REBRND RB-s-8, AMENDMENT 1b): re-validated after the re-mint -- flip to complete | 1 of 1 added lines present at HEAD |
| SUPERSEDED | `76afb991e3` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-14 | remint(DSGN_REBRND RB-s-8, AMENDMENT 1b): DSGN_REBRND-W2-S12 -> DSGN_REBRND-W2-S16 on the unmerg | 5 of 5 added lines present at HEAD |
| SUPERSEDED | `7772585067` | 2.0.0_SA_COO~D | 2026-09-14 | integrate(DSGN_REBRND): bump the portal gitlink to 845833fb -- RB-s-5's one control vocabulary a | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `aa5115008e` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-6 + RB-s-5): fold row W1-S19 (the shell spends the accent on every rou | 11 of 11 added lines present at HEAD |
| SUPERSEDED | `56a41609c1` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-8): AMENDMENT 1b -- on row W2-S17, the issuer authorizes the audited s | 9 of 9 added lines present at HEAD |
| SUPERSEDED | `9ef338da44` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-5): merge 0.9.0_WK_DSGN_REBRND~1 -- RB-s-5 complete (instance VALID, 4 | 407 of 407 added lines present at HEAD |
| SUPERSEDED | `43c034f7b1` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-14 | surprise(DSGN_REBRND RB-s-8, AMENDMENT 1): BLOCKING row W2-S17 -- the ordered W2-S12 -> W2-S16 r | 19 of 19 added lines present at HEAD |
| SUPERSEDED | `ff2a6a9984` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | proof(DSGN_REBRND.TO-RB-s-5): accent controls complete -- 4 of 4 mechanical criteria PASS by out | 334 of 334 added lines present at HEAD |
| SUPERSEDED | `a635ac70f0` | 2.0.0_SA_COO~D | 2026-09-14 | amend(DSGN_REBRND.TO-RB-s-6): fold in row W2-S15 -- four source comments still state the superse | 9 of 9 added lines present at HEAD |
| SUPERSEDED | `b9287cae47` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | surprise(DSGN_REBRND RB-s-5): rows W1-S18..S21 -- AC4 vacuous, shell accent outside the grant, r | 73 of 73 added lines present at HEAD |
| SUPERSEDED | `15dccb63e3` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-14 | drain(DSGN_REBRND RB-s-8): the archetype rewrites COMPLETE -- 4 of 4 mechanical criteria PASS by | 189 of 193 added lines present at HEAD |
| SUPERSEDED | `ef46d4740e` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-7, Amendment 2): merge the fresh RB7-AC4 builder -- page, 1440 capture | 461 of 461 added lines present at HEAD |
| SUPERSEDED | `1794c79aef` | 0.9.0_WK_DSGN_REBRND~2 | 2026-09-14 | build(DSGN_REBRND.TO-RB-s-7 A2): RB7-AC4 page built by a fresh builder from portal/DESIGN.md@000 | 461 of 461 added lines present at HEAD |
| SUPERSEDED | `1a5ce1b0b7` | 2.0.0_SA_COO~D | 2026-09-14 | integrate(DSGN_REBRND): bump the portal gitlink to the RB-s-4 Amendment 2 drain -- the scatter's | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `4cad55331f` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-4, Amendment 2): merge 0.9.0_WK_DSGN_REBRND~1 -- RB-s-4 complete under | 81 of 81 added lines present at HEAD |
| SUPERSEDED | `5072b24fad` | 0.9.0_WK_DSGN_REBRND~1 | 2026-09-14 | proof(DSGN_REBRND.TO-RB-s-4): complete under Amendment 2 -- scatter ULT/LT back on canon; every  | 81 of 81 added lines present at HEAD |
| SUPERSEDED | `892434e6dc` | 2.0.0_SA_COO~D | 2026-09-14 | integrate(DSGN_REBRND): bump the portal gitlink to 63345fac -- the contract (portal/DESIGN.md, R | gitlink bump only; the portal commit it names exists in the portal submodule and is an ancestor of BOTH origin/DEV and origin/PROD, so the substance i |
| SUPERSEDED | `1e7d8c0a13` | 2.0.0_SA_COO~D | 2026-09-14 | drain(DSGN_REBRND.TO-RB-s-7): merge 0.9.0_WK_DSGN_REBRND~2 -- RB-s-7 complete (instance VALID, 5 | 441 of 452 added lines present at HEAD |

### `krny/c3-access-pair-fixture-20260910` -- 4 commits: UNIQUE 4

REMOVABLE: **NO** -- 4 commit(s) are not SUPERSEDED.

| verdict | commit | author | date | subject | basis |
|---|---|---|---|---|---|
| UNIQUE | `3cbcba4f80` | 1.7.0_SA_KRN~Y | 2026-09-10 | log(krn): record A5 byte-domain repair and successor evidence | 0 of 52 added lines present at HEAD |
| UNIQUE | `9cf5d1aa31` | 1.7.0_SA_KRN~Y | 2026-09-10 | docs(krn): hand back bounded access-pair certificate repair | 0 of 76 added lines present at HEAD |
| UNIQUE | `b6179bcc37` | 1.7.0_SA_KRN~Y | 2026-09-10 | log(krn): record access-pair fixture evidence and review handoff | 0 of 67 added lines present at HEAD |
| UNIQUE | `8fe8b102e0` | 1.7.0_SA_KRN~Y | 2026-09-10 | docs(krn): hand back reviewed access-pair successor implementation evidence | 0 of 289 added lines present at HEAD |

### `krny/c3-kernel-design-20260910` -- 4 commits: UNIQUE 4

REMOVABLE: **NO** -- 4 commit(s) are not SUPERSEDED.

| verdict | commit | author | date | subject | basis |
|---|---|---|---|---|---|
| UNIQUE | `f303236817` | 1.7.0_SA_KRN~Y | 2026-09-10 | design(krny): pin canonical LF witness bytes and matching execution evidence | 0 of 4 added lines present at HEAD |
| UNIQUE | `671df384be` | 1.7.0_SA_KRN~Y | 2026-09-10 | log(1.7.0_SA_KRN~Y): distinguish tested CRLF and canonical LF witness bytes | 0 of 5 added lines present at HEAD |
| UNIQUE | `bcaf704296` | 1.7.0_SA_KRN~Y | 2026-09-10 | design(krny): specify bounded C3 proofs and structural result basis | 0 of 479 added lines present at HEAD |
| UNIQUE | `f05cab8baf` | 1.7.0_SA_KRN~Y | 2026-09-10 | log(1.7.0_SA_KRN~Y): record C3 source census and bounded design work | 0 of 54 added lines present at HEAD |

### `krny/c3-offline-fixture-20260910` -- 2 commits: UNIQUE 2

REMOVABLE: **NO** -- 2 commit(s) are not SUPERSEDED.

| verdict | commit | author | date | subject | basis |
|---|---|---|---|---|---|
| UNIQUE | `32c3ef69b7` | 1.7.0_SA_KRN~Y | 2026-09-10 | log(1.7.0_SA_KRN~Y): record C3 offline fixture evidence handback | 0 of 59 added lines present at HEAD |
| UNIQUE | `3b7dbe4c1e` | 1.7.0_SA_KRN~Y | 2026-09-10 | docs(krn): hand back C3 offline fixture and CVO95381 correction | 0 of 661 added lines present at HEAD |

### `krny/c3-report-admission-20260910` -- 5 commits: UNIQUE 5

REMOVABLE: **NO** -- 5 commit(s) are not SUPERSEDED.

| verdict | commit | author | date | subject | basis |
|---|---|---|---|---|---|
| UNIQUE | `985453d506` | 1.7.0_SA_KRN~Y | 2026-09-10 | Log C3 D1/D2 repair, preserved failures and measured successor evidence | 0 of 69 added lines present at HEAD |
| UNIQUE | `ecb7f3a9d6` | 1.7.0_SA_KRN~Y | 2026-09-10 | Record committed C3 D1/D2 repair evidence for independent review | 0 of 87 added lines present at HEAD |
| UNIQUE | `c29fb79a1b` | 1.7.0_SA_KRN~Y | 2026-09-10 | Record committed C3 D1/D2 repair evidence for independent review | 0 of 78 added lines present at HEAD |
| UNIQUE | `c8a1817131` | 1.7.0_SA_KRN~Y | 2026-09-10 | Log bounded retained-report implementation and committed evidence | 0 of 65 added lines present at HEAD |
| UNIQUE | `87c0533527` | 1.7.0_SA_KRN~Y | 2026-09-10 | Record committed retained-report I1-I16 implementation evidence | 0 of 372 added lines present at HEAD |

## WHAT THIS RECORD DOES NOT DO

The verifier MARKS; it does not remove. Nothing here authorizes a deletion, and since no worktree is
wholly SUPERSEDED, nothing here would authorize one even if it did. A PARTIAL is not a verdict -- it
is a commit whose record partly landed, and each one needs a human read before anyone acts on it;
there are 17.

The obvious next act is NOT deletion: it is **landing the work**. Every UNIQUE commit here is a
record, a deliverable or a completed cell whose only copy is a directory on one laptop, on a volume
that reached zero bytes free earlier today. !! **AND NONE OF THESE SIX BRANCHES EXISTS ON `origin`**
-- `git ls-remote --heads origin` returns 5 heads in total and none of them is one of these, with a
fabricated branch name as the negative control. Pushing them costs nothing and removes the whole
hazard; that is 0.0.0_AB_MSTR's call and Andrew's, not this seat's.
