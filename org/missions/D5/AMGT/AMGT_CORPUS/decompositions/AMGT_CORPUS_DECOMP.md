# AMGT_CORPUS -- L5 decomposition v5.0 -- ROUND 5 (the enrichment round after the round-4 analysis)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-25 ~17:xxZ. **Source:** `1.0.0_SA_CTO~Z`'s round-4 analysis
`ledger/ROUND_ANALYSIS.round4.md` @`2f9b10b7d3` + amendment A1 @`047b6211e1`: section 8 (eight enrichment items, item 1 amended
by A1 to the base/px_last band), rules R-1..R-5. Round 4's decomposition is kept as `AMGT_CORPUS_DECOMP.round4.md`. PRD v0.6
@`031c3a3a3e`, both halves SIGNED current.

## 0. What this round IS, by subtraction from the analysis's eight items

| item | disposition |
|---|---|
| 1 FWD-12 limb 3 -- the base/px_last band refusing, the forward-EPS domain check, the GBp reconciliation | cell `CRPS-g-1` |
| 2 Z-S36 -- the dossier Model rows, reasons derived from the data (R-3) | cell `CRPS-g-2` |
| 3 R-2 -- the FWD-19 census emits the fence's three names | cell `CRPS-g-3` |
| 4 the 19-outcome re-grade pass, its own cell and budget | cell `CRPS-g-4` (EVIDENCE only; grading stays L9/L10) |
| 5 cite `C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER` from AMGT_RESAPP's PRD | NOT CUT -- a PRD edit is L4, `1.0.0_SA_CTO~Z`'s lane; routed |
| 6 the trailing-P/E window, declared | inside `CRPS-g-1` (the block names its window rule) |
| 7 R-1 on every judgment criterion | applied: `CRPS-g-1` AC4's sample is a floor with every venue named |
| 8 R-4 on every round analysis | the analysis's own format; this seat's drain packet prints the same three integers |

The team's OWN Upside/Base/Downside cases cited to their workbooks (limb 3's second half) are not cut: the Upside/Downside
methodology is a card at Andrew (analysis s.9 card 1), and no seat chooses a spread.

## 1. The rectangle -- four cells `CRPS-g-<n>`, cut by WRITE SET (no two cells write one file)

| cell | serves | `<risk>` | class | write set (`<paths>`) | the build |
|---|---|---|---|---|---|
| `CRPS-g-1` | FWD-12 limb 3 | SERVED (the drain's re-derive moves the served Model block) | worker | `integrations/bloomberg/research/model_block_pull.py`, `integrations/bloomberg/research/tests/test_model_cases_guard.py` (new) | `_compute_cases` REFUSES (status ABSENT, derived reason) when forward EPS <= 0, when px_last is absent, or when base/px_last falls outside [0.33, 3.0]; expresses the Base case in px_last's quote unit (a minor-unit quote such as GBp scales by its factor) and carries both currencies; names its P/E window rule; a read-only `cases-report` mode prints the decision per key |
| `CRPS-g-2` | FWD-12 dossier half (Z-S36) | SERVED (the drain's dossier write) | worker | `lib/research/corpus/dossier.py`, `lib/research/corpus/tests/test_dossier_model_rows.py` (new) | `model_rows` read the newest derived Model block for the key by the served reader's own rule, fill each row's figure from it, name the block in `inputs`, and derive every absent reason from the data; the constant `FIGURE_ABSENT_REASON` is gone; a read-only `--model-rows-probe` prints the counts |
| `CRPS-g-3` | FWD-19 census (R-2) | LOCAL | worker-light | `lib/research/corpus/backlog.py`, `lib/research/corpus/tests/test_backlog_fence_names.py` (new) | the coverage census prints ONE fence line in the fence's own three names, with its own classes mapped onto them; a read-only `--coverage-dry-run` computes and prints without writing |
| `CRPS-g-4` | FWD-1..FWD-19 (analysis s.7) | LOCAL | worker | `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/FWD_EVIDENCE_ROUND5.json`, `.../FWD_EVIDENCE_ROUND5.md` | one evidence row per outcome: the fence's DONE-WHEN quoted verbatim from the PRD, the instrument run at HEAD against served state, its output, and a state (`met` / `unmet` / `unmeasurable` with reason). No grade: grading is L9's and L10's |

## 1a. Re-groundings at L5

- **g-1:** `_compute_cases` (`model_block_pull.py:1073-1135` @HEAD) multiplies FY1 `BEST_EPS` by the median of every closed
  fiscal year's `PE_RATIO` and carries `PX_LAST` "as context only". All eight names the analysis flags (BA, ULVR, HSBA, RKT,
  BP/, NFLX, NOW, ROG_SW) are among this project's 89 keys, so the drain's re-derive reaches every one. Band [0.33, 3.0] is the
  ISSUER'S choice, stated so the CTO can correct it: the 24 plausible served cases sit at 0.54-2.00 (A1), and the band refuses
  all seven flagged signatures (0.014-0.046, -0.09, 3.04, 4.45) with margin on the plausible side.
- **g-2:** `dossier._model_rows` (`dossier.py:407-440`) writes `FIGURE_ABSENT_REASON` (`:117`) on every row and reads no block;
  94 dossiers, 9,471 rows, 0 values (Z-S36).
- **g-3:** the round-4 census prints `dossier_served 82 served_as_empty_shell 12 resolved_no_prose 0 unresolved_with_reason 0`;
  the fence (PRD `:399-408`) names three classes and `served_as_empty_shell` IS its `resolved-but-no-prose` (analysis s.4).
- **g-4:** the PRD's `endpoint_outcomes` lists FWD-1..FWD-19; 2 of 19 have ever carried a grade (analysis s.7).

## 2. Rule 24 record, for what this file ADDS

g-1's refusal reasons are one derived string per cause (four causes, disjoint by the order they are tested: EPS domain, price
absent, unit, band); g-3's fence line maps four own classes onto three fence names (`served_as_empty_shell` and
`resolved_no_prose` both onto `resolved-but-no-prose`), a subtraction the line prints; g-4's `state` enum is three values over
the 19 outcomes, `unmeasurable` always carrying its reason. No record, key or identity moves in any cell.

## 3. Placement and holds on others' surfaces

g-1 on the Bloomberg lane's puller, granted by `<paths>` for this order only (as e-2 and f-2 were). g-2 and g-3 on this
project's corpus package. g-4 writes only its worker's deliverables. Item 5 is routed to `1.0.0_SA_CTO~Z` in the issuance message.

## 4. Dependency edges, keyed to OBSERVED completion

- The four cells are independent at build time.
- g-1 -> the drain's re-derive (a derive-pair ADDENDUM, since the rule changes what is served: the expected outcome read from
  `cases-report` over the 89 before the run).
- g-2 -> the drain's `dossier --write`, AFTER the re-derive, so the rows read the guarded blocks.
- g-3 -> the drain's `backlog --coverage` last.
- g-4 -> laid out for the CVO at L8.

## 5. The round -- one issuance, fan-out as data

- **ONE issuance covers all 4 cells.** Four worker slots: `~1` g-1, `~2` g-2, `~3` g-3 (worker-light), `~4` g-4.
  `fanout: 4 of 4 chains, cap 8, reason: four independent cells, no shared file.`
- **Drain duties owed by this seat, in order, every verify leg reading CONTENT and every served figure checked against its
  same-object comparator (R-5):**
  1. At every merge: the package suites, `py_compile`, ruff, beside `safe-merge.sh`'s row gate.
  2. g-1 VALID: `cases-report` over the 89 (read-only) -> the expected outcome for the addendum (COO half + CTO half); then the
     re-derive of the 89 under a change-management entry; verify on the served reader: every SERVED base inside [0.33, 3.0]
     of its own `px_last`, every refusal carrying a derived reason, printed as `served / refused / by cause` over 89.
  3. g-2 VALID and item 2 done: `dossier --write`; verify: model_rows with a value > 0 on every key whose block has figures;
     no row carries a constant reason; the dossier names its block in `inputs`.
  4. g-3 VALID: `backlog --coverage`; verify the fence line sums to the live folder count.
  5. The COO's one real run of each outcome, and f-style evidence for g-1 AC4 laid out for the CVO; the packet prints
     `graded this round / graded ever / endpoint denominator` (R-4).
- Surprise channel: `org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md` (seat rows to
  `Z-S37`; workers mint `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`).

## 6. `<preflight>` -- what this decomposition actually ran

```
prd-signoff.py status AMGT_CORPUS        v0.6 @031c3a3a3e; both halves SIGNED current; ADMITTED
task-order status census (last <status>)  25 of 25 terminal on this project -> 0 open
comp-schedule --drift                    2 armed (G-3 CTO, G-7 POD4), 0 on these surfaces
named-name coverage                      8 of 8 flagged names are in the 89 keys (FWD12_PULL_KEYS_20260924.json)
checks as files                          org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/*, each run once at the base
```

## 7. comp-adversary declaration

This file specifies; it produces no artifact. The adversary lens applies at the drain's two served acts (the re-derive, the
dossier write), each under its control in section 5.

## 8. Rulings this decomposition makes, and what it REFUSES to assume

- The band [0.33, 3.0] is the issuer's; the refusal serves ABSENT with its cause, never a clipped or adjusted number.
- A minor-unit quote (GBp and its kin) is reconciled by the currency fields the block already carries (round-3 `currencies`
  block), never by a venue list typed into code.
- REFUSED to assume: that the flagged seven are the only implausible values (the band runs over all 89 at the drain, R-5); that
  a split explains NFLX/NOW (A1 calls it PROBABLE; the band refuses them either way and the reason names the ratio).

## 9. Holds

| hold | on | owner | what lifts it |
|---|---|---|---|
| the re-derive | this lane's drain | `2.0.0_SA_COO~X` + `1.0.0_SA_CTO~Z` (addendum) | g-1 VALID; the addendum signed |
| the dossier write | this lane's drain | `2.0.0_SA_COO~X` | g-2 VALID; the re-derive done |
| the team's Upside/Downside cases | Andrew | Andrew | card 1 of the round-4 analysis s.9 |

-- `2.0.0_SA_COO~X`
