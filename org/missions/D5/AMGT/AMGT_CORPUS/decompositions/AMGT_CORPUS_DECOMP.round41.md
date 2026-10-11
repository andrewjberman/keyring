# AMGT_CORPUS -- L5 decomposition v41.0 -- ROUND 41 (passages end at a sentence end and start at a word; the feed matcher reads terms[1:]; Z-S90's batch repair; D1-S1)

**Issuer:** `2.0.0_SA_COO~C1` (dell1), 2026-10-09 ~16:5xZ.

**Source:** `1.0.0_SA_CTO~DELL1` round-40 analysis `ledger/ROUND_ANALYSIS.round40.md` @`05739a6e4e` s.2 (msg 2835), issued from the
pre-draft with AMENDMENTS 1 and 2. PRD v0.9, both L4-R halves on file; no ENDPOINT change this round. The rectangle is the
analysis's five items. Round 40's decomposition is kept as `AMGT_CORPUS_DECOMP.round40.md`. Bases: CLOUD/box/dell1 HEAD `522aa18dc2`
at the cut; portal origin/DEV `32835ce5`. Pre-draft: `deliverables/2.0.0_SA_COO~C1/ROUND41_DECOMP_PREDRAFT.md` @`6eaf6a9ed2`.

## 0. What this round IS

| # | item (analysis s.2) | cell | path | risk |
|---|---|---|---|---|
| 1 | a passage ENDS at a sentence end, or carries an explicit ellipsis (c1: CUT 0 or each remaining one marked) | `CRPS-aq-1` | worker `0.9.0_WK_AMGT_CORPUS~1` | LOCAL |
| 2 | a passage STARTS at a word, not at a scorecard label (c2: PREFIX 0; BABA US, ST SP) | `CRPS-aq-2` | worker `~1`, after aq-1 by continuation (same file) | LOCAL |
| 3 | 3a: the news feed's term filter reads each pillar's matched terms (`terms[1:]`), never the pillar title; a name with no real term says so in words (ap-4's repair) | `CRPS-aq-3` | worker `~2` | LOCAL (portal DEV candidate, CTO render review) |
| 4 | Z-S90's batch repair: the read-only code census learns its three origins; unresolved 0 with both positive controls flagged | `CRPS-aq-4` | worker `~3` (worker-light) | LOCAL |
| 5 | D1-S1: close `AMGT_CORPUS.TO-READ-R40-ap10b-lv.fire-log-and-budget-line-sitez` on its graded act | `CRPS-ap-10` (round 40's cell, carried here for this close only) | the issuer, in THIS issuance commit (an amendment, not a cell) | -- |
| 1s-2s | the SERVED half of items 1-2: the dossier re-write at the next method version, then the c1/c2 census on the served objects | `CRPS-aq-5` | the issuer's paired act (one never-widen pair to `1.0.0_SA_CTO~DELL1`), after aq-2 drains | SERVED |
| 3s | item 3 reaches the served page only through portal DEV -> PROD; the issuer's one real run reads it on a real name that has real terms AND a headline in the window, chosen by the read (analysis item 3) | -- | the issuer's close read | LOCAL (read) |

**Not CORPUS cells (analysis s.2):** c4, UNVGY's no-forecast reason, goes to AMGT_RESAPP's next round; 3b, growing the KPI
vocabulary, goes to `4.0.0_SA_CRO~DELL1` for round 42.

**Chains (M = 3 worker chains):** `aq-1 -> aq-2 -> aq-5` (one worker's queue: one file); `aq-3`; `aq-4`.
`fanout: 3 of 3 worker chains, cap 8`. Slots: `~1` aq-1 then aq-2 by continuation; `~2` aq-3; `~3` aq-4.

**Write sets (disjoint):**
- aq-1, aq-2: `lib/research/corpus/dossier.py`, `lib/research/corpus/tests/test_dossier_passage_edges_round41.py` (new), the five test files
  that pin the literal `amgt-corpus-dossier/7` (Grep census at the cut, 5 of 5: `test_dossier_method_bump.py`, `test_dossier_case_body.py`,
  `test_dossier_case_unit.py`, `test_dossier_case_positional.py`, `test_dossier_heading_only_round40.py`);
- aq-3: `portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx` and the ONE line in `portal/src/pages/SecurityAnalysis/tabs/NewsTab.tsx`
  (:32 at origin/DEV) where the pillars' terms are flattened before `HeaderBrief` sees them. NOT `continuation.py` (its RULED shape stands);
- aq-4: `lib/research/corpus/readonly_proof.py`, `lib/research/corpus/tests/test_readonly_proof_bound.py`.

## 1. The cells (every check dry-run at the base by the issuer before the cut)

**CRPS-aq-1.** `checks/round41/aq12_check.py aq1` re-composes the section fields of 24 flagged names + 5 controls OFFLINE from picks
frozen in `checks/round41/aq12_picks.json` (built from S3 at the cut). Base: `aq1 counts cut 25 of 95`; `aq1 build 0/1 control 1/1`.
**CRPS-aq-2.** `aq12_check.py aq2`. Base: `aq2 counts prefix 2` (BABA US, ST SP management); `aq2 build 0/1 control 1/1`.
**CRPS-aq-3.** `checks/round41/page_check41.cjs aq3`. Base (portal origin/DEV `32835ce5`): `aq3 build 0/3 control 1/1`
(`realPillarTerms` absent; no absent-words element; NewsTab flattens `p.terms`).
**CRPS-aq-4.** the bound test `test_code_census_arm_leaves_no_amgt_corpus_entry` and the census line. Base: `1 failed`;
`tristate library 0 unresolved 6 clear 80 write_like_calls 86`, both positive controls flagged 1.
**CRPS-aq-5 (SERVED).** After aq-2 merges: one never-widen pair; `python -m lib.research.corpus.dossier --write` at the bumped method;
then `checks/round40/r41_passage_census.py` (C1's instrument) on the SERVED objects reads `prefix 0` and `cut` only on values carrying
an explicit ellipsis. Not a worker cell.

## 2. Not in round 41 (analysis): anything that changes the 13:00Z fire's call, field list or address.
