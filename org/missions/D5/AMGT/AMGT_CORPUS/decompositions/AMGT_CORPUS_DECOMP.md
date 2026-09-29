# AMGT_CORPUS -- L5 decomposition v9.0 -- ROUND 9 (the enrichment round after the round-8 analysis)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-29 ~01:3xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-8 analysis
`ledger/ROUND_ANALYSIS.round8.md` @`40ff643781` section 4, two cells (msg 26356, READ-acked), answering `3.0.0_SA_CVO~Z`'s
slug on `ADJUDICATION_v11`. Round 8's decomposition is kept as `AMGT_CORPUS_DECOMP.round8.md`. PRD v0.6 @`9e326e11c1`, ADMITTED.

## 0. What this round IS, by subtraction from the analysis's list

| item (analysis s.4) | disposition |
|---|---|
| 1 table-aware case rule + the held dossier rewrite under a pair | cell `CRPS-k-1` (one order, `~1`); the rewrite is this seat's drain act under a never-widen pair |
| 2 re-derive the model blocks under `case_rule.py`, gated on the combined scoped-API deploy's close | cell `CRPS-k-2`: an ISSUER ACT, not an order (s.8) |

**NOT cells** (the analysis): the six keys' adjusted-EPS pull (Andrew's card); worktree and `%TEMP%` removal (the operator's word).

## 1. The rectangle

| cell | slot | serves | `<risk>` | class | write set | the build / act |
|---|---|---|---|---|---|---|
| `CRPS-k-1` | `~1` | FWD-12 limb 3 data half, FWD-16 cases | SERVED (the drain's rewrite) | worker | `lib/research/corpus/dossier.py`, `lib/research/corpus/tests/test_dossier_case_table.py` (new), `lib/research/corpus/tests/test_dossier_case_body.py` | each case serves ITS columns of the scenario table, `{metric: {year: value}}`, with its unit and page citation; the census prints per-name ordering and unit |
| `CRPS-k-2` | issuer | the served Base-case guard of FWD-12 (`Z-S51`) | SERVED | issuer act | the stored `derived/model_block/<key>/<stamp>/model_block.json` objects (97 keys) | `model_block_pull derive` over the 97 keys under `case_rule.py`, in batches of 3 (the stage's cap), under a pair and a change entry |

## 1a. Re-groundings at L5

- **k-1 (measured @`895a999451`, packet s.3; the CVO's own run on ADBE and AZN at L9).** 34 names carry the three case labels
  as consecutive lines on page 0 of their class-A pdf pack, followed by 3k year headers (`2026E`..`2030E` x3, k = 5) and
  metric rows `EPS`, `Multiple`, `Price`, `Return`, each a label line and 3k value lines; values `[0,k)` Upside, `[k,2k)` Base,
  `[2k,3k)` Downside. ADBE Price 2026 `416 / 233 / 143`; AZN carries the pound sign (U+00A3) on its values. The dossier's
  `cases` field has NO downstream reader: `scoped_amgt._model_cases` computes cases from the model block through
  `case_rule.compute_cases`; `render_pack` renders that payload; `git -C portal grep dossier -- src` reads 0 files against a
  positive control of 159 (`useState`). So the value's shape can change.
- **k-2.** Under `case_rule.py` (@`b56fef3032`), `cases-report` over the 97 keys reads SERVED 69 vs the stored blocks' 49;
  21 ABSENT -> SERVED; CAT_US SERVED -> ABSENT; 48 of 48 served-in-both at a different ratio
  (`deliverables/2.0.0_SA_COO~X/evidence/r8_base_cases_report_all_20260928T234706Z.log`). The six keys `Z-W3-S6` carry no
  adjusted EPS at any landed stamp and stay ABSENT with the rule's reason (no GAAP fallback -- analysis s.2 ruling 3).
  **The gate:** change entry `amgt-combined-uu4-a2-scoped-amgt-timeline-and-adjusted-base-20260929` (`0.7.0_AE_CloudOps~A`,
  AMGT_RESAPP uu-4 + AMGT_HARVST a-2) is OPEN at the cut, 14 legs unproven. k-2 runs only after it CLOSES, so the stored
  blocks and the served adapter move to one rule in one window.

## 2. Rule 24 record, for what this file ADDS

k-1's case value is a closed shape: `{metric: {year: value}}` of strings exactly as written, `unit` a symbol read from the
row or null, the citation the table's page. The census partitions every case slot into `body` / `heading_only` / `absent`
(summing to 3N) and every name with a table into `ordering_held` / `ordering_violated`, others `ordering_na`; ordering is a
column, never a refusal (analysis s.2 ruling 1).

## 3. Placement and holds on others' surfaces

k-1 on this project's corpus package. k-2 writes this project's model blocks through the Bloomberg lane's puller, reading
landed raw only (no vendor call); it does not edit `case_rule.py` (AMGT_RESAPP's).

## 4. Dependency edges, keyed to OBSERVED completion

- k-1 -> drain -> never-widen pair for the dossier rewrite (expected outcome read from `write_one`'s rule: every name's stored
  object is `/1` and the code is `/2`, so every name writes -- 95 puts, objects 468 -> 563) -> change entry ->
  `dossier --write --workers 10` -> verify -> `Z-S53` lifts -> the CVO grades AC3 on the served table.
- k-2: the combined entry CLOSES -> never-widen pair (expected outcome read from `case_rule.compute_cases` over the landed raw
  via `cases-report`, both branches: 69 SERVED, 28 ABSENT, CAT_US SERVED -> ABSENT, the six ABSENT) -> change entry ->
  derive in batches of 3 -> verify on the SERVED blocks (a round-7 `actA_verify.py`-shaped read) -> `Z-S51` answered.
- k-1 and k-2 are independent.

## 5. The round -- one issuance, fan-out as data

- **ONE issuance.** `fanout: 1 of 2 chains, cap 8, reason: k-1 is the only build; k-2 is an issuer act with no code, gated
  on another project's change entry.`
- **Drain duties:** at the merge the corpus suite, `py_compile`, ruff; k-1 re-graded at its tip; the rewrite and the
  re-derive under their pairs, each with a change entry opened before the act and closed with proof; the one real run:
  `read_dossier` on ADBE (USD) and AZN (GBP) read by this seat, and the served blocks census after k-2.
- Surprise channel: `surprise-channel/investigations/INVESTIGATION_v1.md` (seat rows from `Z-S54`; workers
  `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`).

## 6. `<preflight>` -- what this decomposition actually ran

```
prd-signoff.py status AMGT_CORPUS        v0.6 @9e326e11c1 EXECUTING -> ADMITTED
task-order census (last <status>)         CRPS-j-1..j-4 complete -> 0 open on this project
consumer census of fields.cases           lib: scoped_amgt/render_pack read the MODEL block's cases, not the dossier's; portal 0 of 159
the k-2 gate entry                        OPEN, 14 legs, window 8 h (read at the cut)
checks as files, dry-run at the base      checks/round9/k1_AC1 FAIL (no tests ran); k1_AC2 FAIL (base line
                                          'case_census names 95 slots 285 body 34 heading_only 68 absent 183 sum 285' lacks
                                          heading_only 0 and the ordering/unit columns)
```

## 7. comp-adversary declaration

This file specifies; it produces no artifact. The adversary lens applies at the two served acts, each under its pair.

## 8. Rulings this decomposition makes, and what it REFUSES to assume

- **k-2 is not an order.** A worker holds no pair and the act needs no code; an order would be a wrapper around this seat's
  own act. It is recorded here as a cell so the rectangle covers the analysis's list, and it is drained by this seat.
- k-1 keeps the round-8 infrastructure (method-aware no-op, `--case-census`, `--write --workers N`, `read_dossier`'s method
  preference); only how a CASE is read from its block changes. A case heading that is NOT a table row label keeps round 8's
  body rule.
- Values are served exactly as written (strings); nothing is parsed into a number the team did not write, and nothing is
  computed.
- REFUSED to assume: that every table has k = 5 or exactly four metric rows (k-1 reads both); that the unit sits on every row
  (k-1 reports where it found it).

## 9. Holds

| hold | on | owner | what lifts it |
|---|---|---|---|
| every `dossier --write` (`Z-S53`) | this seat | `2.0.0_SA_COO~X` | k-1 VALID; the pair signed; the rewrite verified |
| every model-block `derive` (`Z-S51`) | this seat | `2.0.0_SA_COO~X` | the combined entry CLOSED; the k-2 pair signed |

-- `2.0.0_SA_COO~X`
