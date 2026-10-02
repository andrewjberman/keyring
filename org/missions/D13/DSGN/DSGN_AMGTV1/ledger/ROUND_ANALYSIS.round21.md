# DSGN_AMGTV1 -- ROUND 21 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-02 ~06:4xZ

**Input:** CVO~Z slug msg 28249, `surprise-channel/remediations/REMEDIATION_v1.md` @2d6a452375 (19 REMEDIATED, 2 OPEN);
stamps in ADJUDICATION_v19 @a9f4fdc548 (open 0, ARMED 0). Round 21 close: `ROUND21_CLOSE.md` @0f6b932de1 (AV-y-1, 1 of 1
complete). PROD `b3a1d8a6` contains the round-21 freeze `3c37a01c`. **Round 21 is CLOSED.** **DSGN is not CLOSED-ready.**
CVO~Z's FWD read finds FWD-2, FWD-8 and FWD-11 NOT REALIZED, and all three are visible on PROD now.

**This analysis supersedes this seat's tick-1 hold ruling (msg 28223, "no round 22").** That ruling rested on the shipped face
being right. The slug shows three gaps on it.

## 1. WHERE EACH GAP IS WRITTEN (producer vs page)

| gap | FWD | written by | so the fix lands |
|---|---|---|---|
| 24 of 94 price bars named by ticker code (and the September bubbles BABA/COST/KPN/NOVN) | 2 | the served price ranking (AMGT_RESAPP) | served, no portal promote |
| "Lusha enrichment: SKIPPED -- no declared domain for VLO_US_Equity in domains.json" | 11 | `lib/research/management/enrich.py` (AMGT_RESAPP, TOs rk-49 and rk-110); `ExecManagementTab.tsx:317` prints it verbatim | served wording first; page guard second |
| Peers absent-column reasons print field codes (`ey_ntm`, `cash_mv`, ...) | 8, 11 | served registry reasons (codes from `factor_metadata_registry.json`) | served wording first; page guard second |
| Peers subject row prints "--" for Price, EV and P/E that the header carries | 8 | the page | portal, then promote |
| "ABSENT" in Posture reason 2 | 11 | to be located by the cut (served or page) | where it is written |
| VLO officer "Senior Vice", with roles carrying a trailing age | 7 | served M-1 parse (AMGT_RESAPP) | served |

**Rule: fix a served string at its producer, not with a page-side rewrite of it.** The page keeps one guard: it never prints a
code-shaped token, and it falls back to a plain generic reason. The producer fixes reach PROD with no portal promote. They do
move served output, so each one carries the never-widen sign-off pair (`1.0.0_SA_CTO~Z` + `2.0.0_SA_COO~Z`), and that sign-off
names its blast radius per key.

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **PRD v0.7 amends FWD-13's DONE WHEN.** The tooltip carries the plain label and the full-precision value, and the mnemonic is in `data-mnemonic`, never on the face. `3.0.0_SA_CVO~Z` re-signs the ratified-text half. | It contradicted FWD-11 and rulings 27914/27927 (slug section 3) |
| 2 | **RESAPP round 61 opens on this slug.** RESAPP round-60 ruling 1 held the issuance open for exactly this case ("unless the DSGN close walk surfaces a served-field defect"). The cells are section 3B. | the served-field defects above |
| 3 | **The walker's `raw-code` check is not evidence for FWD-11** until it sees snake_case inside prose. The check, and Z-S11's occluded-popover hit-test, are tool fixes to `.claude/skills/ui-walk/walk.mjs`, routed to `0.0.0_AB_MSTR~Z` as tool owner. Until then FWD-11 is graded by the round-22 text census (cell A1), not by walk.mjs. | slug section 3; remediation row Z-S11 |
| 4 | **Z-W56-S4 (errorEmpty's starred claims):** retire them in DSGN round 22 as cell A4, one instrument repair. | remediation row Z-W56-S4 |
| 5 | **Grades:** `ledger/COMPLETION_GRADES.round22.json` is written at the round-22 close, against v0.7 and the served artifact. FWD-1's live-product limb is read on the PROD URL after the promote. | spine :554-568 |

## 3. THE ENRICHMENT LIST -- ONE issuance each

**A. DSGN round 22, `2.0.0_SA_COO~D`** (page; lands on DEV; the promote is an act for Andrew, section 4):

| # | cell | criteria shape (at most three, mechanical) |
|---|---|---|
| A1 | No code-shaped token on the face (FWD-11): Exec, Posture and Peers render a plain reason whenever the served string carries a code, an id, `_US_Equity` or a file name | rendered-text census on BA, VLO and AMD reads 0 tokens matching `[a-z]+_[a-z0-9_]+`, `_Equity`, `\.json` or `ABSENT`; a planted served code string reads 1 before the fix (positive control) |
| A2 | Peers subject row (FWD-8): Price, EV and P/E are filled from the header's served values when the header carries them | BA's subject row shows USD 196.80 and 187B where it showed "--"; VLO likewise |
| A3 | Price bars and bubbles (FWD-2): the page shows the served company name whenever one is served | 0 bars whose label equals a `security_key` when the served row carries a name (read after RESAPP B1 deploys) |
| A4 | errorEmpty starred claims (Z-W56-S4) | the claims are retired, or re-pointed at the bubbles' starred empty state; the harness stays green |

Deadline: drained by **11:30Z (07:30 ET)**, so the promote candidate is ready for Andrew at ~13:00Z. A cell not drained by then
drops; PROD stays on `b3a1d8a6` and loses nothing.

**B. RESAPP round 61, `2.0.0_SA_COO~Z`** (served; each is a never-widen act with the CTO+COO pair):

| # | cell | criteria shape |
|---|---|---|
| B1 | A company name on every row of the price ranking and the chatter set (FWD-2). Use the same security reference that names the other 70 | served ranking: 0 of 94 rows lack a name, with a positive control on one of the 24 (e.g. `RMS FP`). It lands before the 07:13 ET generation if it can; otherwise the next one |
| B2 | Plain served reasons (FWD-8, 11): the Lusha skip reason and the registry's absent-column reasons in words, never a key, field code or file name | served Exec and Peers payloads for BA and VLO: 0 code-shaped tokens; a mutant restoring the old string fails |
| B3 | M-1 officer parse (FWD-7): the full title, and no trailing age in the role | VLO served officers: no title equals "Senior Vice"; 0 roles ending in a number |

## 4. ACTS ONLY ANDREW CAN DO (cited)

1. **The portal PROD promote of the round-22 candidate** (CVO verdict 27503; the PROD push is on his word at the terminal). Rollback is
   `b3a1d8a6`.

## 5. SEATS

`2.0.0_SA_COO~D` cuts A; `2.0.0_SA_COO~Z` cuts B; `3.0.0_SA_CVO~Z` signs v0.7 and runs L8/L9 at both drain-ends;
`0.0.0_AB_MSTR~Z` owns the walk.mjs tool fixes (ruling 3).
