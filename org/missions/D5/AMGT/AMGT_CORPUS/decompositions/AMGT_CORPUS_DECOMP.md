# AMGT_CORPUS -- L5 decomposition v6.0 -- ROUND 6 (the enrichment round after the round-5 analysis)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-26 ~06:xxZ. **Source:** `1.0.0_SA_CTO~Z`'s round-5 analysis
`ledger/ROUND_ANALYSIS.round5.md` @`37217d8053` section 5 (eight items, "cells 1-8 independent except 2 and 3"), plus the
render-seam PRD addendum @`64d0a493ac` (FWD-10 and FWD-15 REALIZED on this project's halves, 12 of 19; FWD-11 owed as a new
outcome on AMGT_RESAPP's endpoint). Round 5's decomposition is kept as `AMGT_CORPUS_DECOMP.round5.md`. PRD v0.6: brief half
SIGNED; ratified-text half STALE since @`64d0a493ac` (insertions only), re-sign asked of `3.0.0_SA_CVO~Z` before issuance.

## 0. What this round IS, by subtraction from the analysis's eight items

| item | disposition |
|---|---|
| 1 FWD-17 (b), the IMB_LN_Equity candidate | ANSWERED at L5, read-only, and it moved the cell: IMB is NOT a violation (its objects differ on fund-form, typecast and Model-block inputs), but the table IS violating (b) through `read_dossier`'s newest pick -- row `Z-S41` (ARMED), disarmed by hold `Z-S42`. Cell `CRPS-h-1` |
| 2 AC4's workbook half | cell `CRPS-h-2` (evidence for the CVO; the grade stays L9's) |
| 3 the case-ratio distribution below 3.0 | inside `CRPS-h-2`: one census by name over every key with a Model block, both sides of both bounds |
| 4 FWD-9's census third state | cell `CRPS-h-3` |
| 5 FWD-14's fence triple | cell `CRPS-h-4` |
| 6 FWD-18 pillar terms + the feed filter | cell `CRPS-h-5` on the DATA half (pillar and KPI rows name their terms). The header feed and Chatter filter are the page's, the same seam `@64d0a493ac` measured for FWD-10/11/15: NOT cut here |
| 7 FWD-19 limb 2's discriminator | ANSWERED at L5, no cell (section 1a) |
| 8 FWD-2's one bronze-without-silver row | ANSWERED, row `Z-S43`: the Copa Holdings byte-identical pair, 356 objects / 355 report_ids / 355 silver |

**NOT cells:** FWD-10 and FWD-15 (REALIZED by the addendum), FWD-11 (a new AMGT_RESAPP outcome, the CTO's L2/L4 act), FWD-12
limb 3 (RESERVED at Andrew on the Upside/Downside method; a cell proposing a machine formula is refused at the cut). No cell
builds any render against this project's fence text.

## 1. The rectangle -- five cells `CRPS-h-<n>`, cut by WRITE SET (no two cells write one file)

| cell | serves | `<risk>` | class | write set (`<paths>`, plus the channel) | the build |
|---|---|---|---|---|---|
| `CRPS-h-1` | FWD-17 (b) (Z-S41) | SERVED (the drain's one-name `--write` exercise) | worker-light | `lib/research/corpus/dossier.py`, `lib/research/corpus/tests/test_dossier_newest.py` (new) | `read_dossier` returns the object WRITTEN LAST on the newest `as_of` date (S3 `LastModified`; gold never overwrites), key name only as a tie-break; the false docstring is corrected. `write_one` unchanged |
| `CRPS-h-2` | FWD-12 AC4 workbook half + the band's accept side | LOCAL | worker | `deliverables/0.9.0_WK_AMGT_CORPUS~2/case_evidence.py`, `CASE_EVIDENCE_ROUND6.json`, `CASE_EVIDENCE_ROUND6.md` | read-only scripted producer: (a) base/px_last per key over every key with a Model block, served or refused, binned, with the nearest names each side of 0.33 and 3.0; (b) for every key with a bronze workbook, every cell labelled Base/Bull/Bear/Upside/Downside/target price with its coordinate and the numbers beside it, next to the served Base case. SELECTS NOTHING |
| `CRPS-h-3` | FWD-9 | LOCAL | worker-light | `lib/research/corpus/readonly_proof.py`, `lib/research/corpus/tests/test_readonly_proof_tristate.py` (new) | every census row carries `state` library / unresolved / clear; totals print `library_write_calls` (library only) and `unresolved_write_calls` with each unresolved site listed; the exit predicate is UNCHANGED (both must be 0) |
| `CRPS-h-4` | FWD-14 | LOCAL | worker-light | `lib/research/corpus/backlog.py`, `lib/research/corpus/tests/test_backlog_fence14.py` (new) | the coverage totals gain ONE line in FWD-14's three names with a disclosed remainder: `fence14 resolved <a> ambiguous <b> empty-or-workbook-only <c> sum <a+b+c> outside-fence <d> folders_read <n>` |
| `CRPS-h-5` | FWD-18 data half | SERVED (the drain's continuation + dossier rewrite) | worker | `lib/research/corpus/continuation.py`, `lib/research/corpus/tests/test_continuation_terms.py` (new) | each pillar carries `terms` = its own heading plus every KPI-vocabulary term found in its text, word-bounded, first-appearance order; each KPI row carries `terms` = its name split on `/`; METHOD_VERSION `/2`; a read-only `--show-terms --security-key` prints them |

## 1a. Re-groundings at L5

- **h-1:** `dossier.read_dossier` takes `sorted(keys)[-1]` over `as_of=<date>.<inputs_sha16>.json`; its docstring says a later
  hash sorts after an earlier one on the same date, which a sha256 prefix does not do. Census
  `checks/round6/dossier_order_census.py` @`ac7fc54651`: 95 partitions, 373 objects, 37 rewrites on unchanged inputs (all
  09-26), 95 of 95 serving the last write NOW; 195 same-date pairs order by name like by write time on 100 and unlike on 95.
  `substrate._pick_stored` selects on inputs-equal-now and is not affected. No page reads the dossier table (portal 0 files).
- **h-2:** bronze holds 79 workbook extracts; 61 (53 names) carry a Base/Bull/Bear/target label in `sheet_data` (read at L5);
  each extract names its raw object in `bronze_key`. The served Model blocks: 43 served in band at 0.537-2.566, 20 refused
  (currency 14, band 4, EPS 1, no price 1), 26 absent (round-5 packet). NO vendor call: every read is this project's S3.
- **h-3:** `code_census` sets `reaches = LIBRARY in origins or (UNKNOWN in origins and not tmp-fixture-only)` and sums it as
  `library_write_calls`; the live census reads files_scanned 39, write_like_calls 43, library_write_calls 4 -- all four in
  `induction_run.py` (:462, :464, :688, :690), origin UNKNOWN via `deliverables_dir = deliverables_dir or DELIVERABLES_DIR`.
- **h-4:** `backlog --read-latest` prints `folders_read 95 = resolved 95 + unresolved 0 + ambiguous 0`; the coverage census
  measures `never_prose_reason` ('empty' / 'workbook-only' / None) per folder (`NEVER_PROSE_REASONS`, `backlog.py:142`); the
  FWD-19 fence line reads dossier-served 83 / resolved-but-no-prose 12 / unresolved-with-reason 0.
- **h-5:** a pillar is `{citation, pillar, text}` (`continuation.py:428`, `:586`); `kpi_set` is a dict of 25 names, each
  `{citations, count}`; 42 of 95 continuations carry both pillars and a KPI set.
- **Item 7, answered:** the 60 today-unresolved of 09-24 reached 0 through the scripted `induction_run`, each followed by a
  re-ingest -- 20 in the d-5 fire (`911d09d153`), 36 in the 40-name fire (`505fc14404`, UNRESOLVED 40 -> 4), 4 in the re-mint
  (`c79872b0ff`: GOOGL, LLY, PWR, UNH; its fifth, AMD, was outside the 60). AIA Group's registration (`2c35b9a062`) is the 95th
  folder and not one of the 60. So both named mechanisms moved it, 56 by induction and 4 by identity re-mint, and AIA none.

## 2. Rule 24 record, for what this file ADDS

h-3's `state` is three values over every write-like call, disjoint by precedence (library if LIBRARY is among the origins;
else unresolved if UNKNOWN is, outside the tmp-fixture exemption; else clear). h-4's fence line is a partition of the folder
list by precedence (empty-or-workbook-only first, from the measured `never_prose_reason`; then ambiguous; then resolved; the
remainder `outside-fence`), so `a+b+c+d == n` by construction and the fence holds exactly when `d == 0`. h-5's `terms` are a
subset of two named vocabularies (the pillar's own heading; the KPI names), never generated. h-2 selects nothing.

## 3. Placement and holds on others' surfaces

All five on this project's corpus package or its worker deliverables. h-2 reads the Bloomberg lane's served Model blocks and
this project's bronze, writing neither. Z-S42 holds every dossier `--write` at this seat until h-1 drains.

## 4. Dependency edges, keyed to OBSERVED completion

- The five cells are independent at build time; items 2 and 3 share one cell (h-2) per the analysis.
- h-1 -> the drain's exercise and the lift of Z-S42 -> h-5's served rewrite (a continuation rewrite changes every dossier's
  inputs, so it must run on the corrected newest pick).
- h-3, h-4 -> the drain's census runs; h-4's line is read on `--coverage` after h-5's rewrite.
- h-2 -> laid out for the CVO at L8 (AC4, judgment).

## 5. The round -- one issuance, fan-out as data

- **ONE issuance covers all 5 cells.** Slots `~1` h-1 (worker-light), `~2` h-2, `~3` h-3 (worker-light), `~4` h-4
  (worker-light), `~5` h-5. `fanout: 5 of 5 chains, cap 8, reason: five independent cells, no shared file.`
- **Drain duties owed by this seat, in order, every verify leg reading CONTENT (R-5):**
  1. At every merge: the package suites, `py_compile`, ruff, beside `safe-merge.sh`'s row gate.
  2. h-1 VALID: the census must read `read_dossier serves the last write 95 of 95`; then FWD-17 (b)'s exercised arm: with
     fresh inputs measured equal to the served object's immediately before, `dossier --write --security-key IMB_LN_Equity`
     TWICE, each printing `unchanged ... wrote 0`, and the census's rewrite count unchanged. Then Z-S42 lifts by row.
  3. h-5 VALID: a never-widen pair (COO half + `1.0.0_SA_CTO~Z` half) for the continuation rewrite and the dossier rewrite,
     expected outcome read from the producers' own rules; verify: every pillar on the served continuation carries `terms`,
     and every dossier carries the new continuation in `inputs`.
  4. h-3 and h-4 VALID: `readonly_proof --code-census` and `backlog --coverage` last; both fence lines read on the output.
  5. The COO's one real run of each outcome; h-2's evidence laid out for the CVO; the packet prints `graded this round /
     graded ever / endpoint denominator` (R-4).
- Surprise channel: `org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md` (seat rows to
  `Z-S43`; workers mint `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`).

## 6. `<preflight>` -- what this decomposition actually ran

```
prd-signoff.py status AMGT_CORPUS        v0.6 @64d0a493ac; brief SIGNED; ratified-text STALE (ENDPOINT hash moved by the
                                         insertions-only addendum) -> re-sign asked of 3.0.0_SA_CVO~Z at 06:12Z
task-order status census (last <status>)  see the issuance commit (read at the cut)
comp-schedule --drift                    1 drift candidate, on data/black_diamond (not these surfaces)
dossier_order_census.py                  partitions 95 objects 373 | rewrites 37 | serves the last write 95 of 95
checks as files                          org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/*, each run once at the base
```

## 7. comp-adversary declaration

This file specifies; it produces no artifact. The adversary lens applies at the drain's served acts (h-1's exercise, h-5's
rewrite), each under its control in section 5.

## 8. Rulings this decomposition makes, and what it REFUSES to assume

- h-1: "newest" is the last WRITE on the newest `as_of` date. Across dates the date still decides, as today.
- h-3: the exit predicate does not weaken; only the NAMES split. An unresolved site is listed for a reader, never cleared.
- h-4: the precedence is the issuer's and is printed; a folder outside the fence's three is counted, never folded in.
- h-5: no term is generated; the feed filter is the page's.
- REFUSED to assume: that the 37 extra dossier objects need removing (additive gold, never served over a newer one; no delete);
  that a workbook's labelled cell IS the team's Base case (h-2 lays out coordinates; the CVO judges).

## 9. Holds

| hold | on | owner | what lifts it |
|---|---|---|---|
| every dossier `--write` (Z-S42) | this seat | `2.0.0_SA_COO~X` | h-1 VALID and its exercise read |
| the continuation + dossier rewrite | this lane's drain | `2.0.0_SA_COO~X` + `1.0.0_SA_CTO~Z` (pair) | h-5 VALID; Z-S42 lifted |
| the team's Upside/Downside cases | Andrew | Andrew | the round-4 analysis s.9 card 1 |
| FWD-11's AMGT_RESAPP outcome | `1.0.0_SA_CTO~Z` | the CTO, L2/L4 | the addendum @`64d0a493ac` |

-- `2.0.0_SA_COO~X`
