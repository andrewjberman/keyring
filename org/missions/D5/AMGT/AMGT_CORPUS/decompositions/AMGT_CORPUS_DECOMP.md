# AMGT_CORPUS -- L5 decomposition v10.0 -- ROUND 10 (the enrichment round after the round-9 analysis)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-29 ~03:5xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-9 analysis
`ledger/ROUND_ANALYSIS.round9.md` @`abfad1355c` section 4, four cells (msg 26429, READ-acked), answering `3.0.0_SA_CVO~Z`'s
slug on `ADJUDICATION_v12`. Round 9's decomposition is kept as `AMGT_CORPUS_DECOMP.round9.md`. PRD v0.6 @`9e326e11c1`, ADMITTED.

## 0. What this round IS, by subtraction from the analysis's list

| item (analysis s.4) | disposition |
|---|---|
| 1 case unit carries its claim (ruling 1), rewrite under a pair | cell `CRPS-l-1` (`~1`, second in its queue) |
| 2 team-vs-rule Base census (ruling 2), read-only | cell `CRPS-l-2` (`~2`) |
| 3 the 6 unreadable tables (ruling 3) | cell `CRPS-l-3` (`~1`, first in its queue) |
| 4 `cases-report` refuses an unresolvable key (`Z-S55`) | cell `CRPS-l-4` (`~3`) |

## 1. The rectangle

| cell | slot | serves | `<risk>` | class | write set | the build |
|---|---|---|---|---|---|---|
| `CRPS-l-3` | `~1` (first) | FWD-12 limb 3 data half (six names) | SERVED (the shared rewrite) | worker | `lib/research/corpus/dossier.py`, `tests/test_dossier_case_layouts.py` (new), `tests/test_dossier_case_table.py` | each of the six tables is read, or served ABSENT with a reason naming its own layout defect |
| `CRPS-l-1` | `~1` (second) | FWD-12 (the unit's claim) | SERVED (the shared rewrite) | worker | `lib/research/corpus/dossier.py`, `tests/test_dossier_case_unit.py` (new) | `unit_as_written` + `currency` / `currency_basis`; census columns |
| `CRPS-l-2` | `~2` | FWD-12 guard (the rule's pairing, `Z-S51`) | LOCAL | worker | `lib/research/corpus/base_census.py` (new), `tests/test_base_census.py` (new) | read-only team-Base / rule-Base census over every name carrying both |
| `CRPS-l-4` | `~3` | `Z-S55` | LOCAL | worker-light | `integrations/bloomberg/research/model_block_pull.py`, `integrations/bloomberg/research/tests/test_cases_report_refuses_unresolved.py` (new) | `cases-report` refuses a key that resolves to no landed stamp |

l-3 and l-1 share `dossier.py`: ONE chain, one worker, l-3 first (its layouts decide which names have a unit to claim).

## 1a. Re-groundings at L5

- **l-3.** `checks/round10/l3_six.py` at the base: `l3 names 6 body_names 0 absent_specific 0 absent_generic 6 sum 6`; every
  one of the six reads `... row 'EPS' carries 14 values, expected 3 x 5` (round 9's worker: one Base EPS value missing).
- **l-1.** Round 9's census: `unit_carried 10` (AZN U+00A3 on a GBp listing; ML U+20AC; `$` on BP, CPA, ORA, SAP, SHOP, SPOT,
  TTE, UNVGY). The CVO measured `$` on three EUR listings and one CAD listing (ADJUDICATION_v12). The listing currency is on
  the name's stored model block (`currencies`), which `build()` already reads (`_model_block_read`).
- **l-2.** A stored block's `cases.base` carries `status`, `ratio_to_px_last`, `px_last.value`, `inputs.consensus_eps`,
  `inputs.trailing_median_pe`, `band`, `band_basis`; `value` only when SERVED. ADBE's newest block (`20260929T024507Z`) is
  ABSENT (outside the band) with `ratio_to_px_last 3.319...` on `px_last 238.93` -- the rule's figure exists though the band
  refused it. The team's Base is the served dossier's `cases.base.value.Price` by year.
- **l-4.** At the base: `cases-report --securities AMD_US_Equity` prints `base ABSENT ... no consensus EPS on the landed block`,
  `cases_report served 0 refused 1`, rc 0; `"AMD US Equity"` prints `base SERVED ratio 0.659...`.

## 2. Rule 24 record, for what this file ADDS

`currency` is `null` unless the symbol maps to exactly one ISO code AND that code is the listing's; `currency_basis` names
why when null. The six-table checker partitions the six into `body_names` / `absent_specific` / `absent_generic`, summing to 6.
The Base census partitions names into `both` / `team_only` / `rule_only` / `neither`, summing to the resolved names.

## 3. Placement and holds on others' surfaces

l-4 on the Bloomberg lane's puller (read-only stage, `<paths>` grant for this order only); it does not touch `derive` or
`case_rule.py`. l-1/l-3/l-2 on this project's corpus package.

## 4. Dependency edges

- Chain A: l-3 -> l-1 -> drain -> ONE never-widen pair for the dossier rewrite covering both -> change entry -> `dossier
  --write --workers 10` -> verify -> the CVO grades.
- l-2 and l-4 independent. l-2 reads the served dossier and blocks as they stand; it is re-run by this seat after chain A's
  rewrite as the one real run.

## 5. The round -- one issuance, fan-out as data

- `fanout: 3 of 3 chains, cap 8, reason: l-3 and l-1 share dossier.py and run as one queue on ~1 (l-3 first); l-2 (~2) and
  l-4 (~3) are independent.`
- Drain duties: at each merge the touched suites, `py_compile`, ruff; each worker re-graded at its tip; chain A's rewrite
  under its pair; the one real run: `read_dossier` on AZN (U+00A3 on GBp), ML (U+20AC on EUR) and one `$` name; `base_census`
  after the rewrite; `l3_six.py`.
- Surprise channel rows from `Z-S56`; workers `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 6. `<preflight>` -- what this decomposition actually ran

```
prd-signoff.py status AMGT_CORPUS        v0.6 @9e326e11c1 EXECUTING -> ADMITTED
task-order census (last <status>)         CRPS-k-1 complete -> 0 open on this project
checks as files, dry-run at the base      checks/round10/: l3_AC1 l1_AC1 l2_AC1 l4_AC1 FAIL (no tests ran); l3_AC2 FAIL
                                          (absent_generic 6); l1_AC2 FAIL (no currency columns); l2_AC2 FAIL (No module
                                          named lib.research.corpus.base_census); l4_AC2 FAIL (planted underscore key rc 0);
                                          l4_AC3 PASS (AMD US Equity base SERVED)
```

## 7. comp-adversary declaration

This file specifies; it produces no artifact. The adversary lens applies at chain A's served rewrite, under its pair.

## 8. Rulings this decomposition makes, and what it REFUSES to assume

- l-1 converts nothing and infers nothing from the listing; the listing is used only to REFUSE a currency the symbol does not
  uniquely name (analysis s.2 ruling 1).
- Chain A bumps the dossier's `METHOD_VERSION` to `/3` (in l-1): it changes what a case serves but moves no `inputs`, and
  `write_one` writes nothing when the stored method and inputs are both unchanged -- without the bump the rewrite is a no-op
  (round 8's lesson on this table). Rollback is the revert to `/2` through `read_dossier`'s method preference.
- l-2 grades nothing; it prints a distribution with its denominator and names every name it could not pair, with the reason.
- l-4 refuses at the CLI; it changes no rule and no derive.
- REFUSED to assume: that the six tables share one defect (l-3 reads each); that the team's Base year equals the rule's (l-2
  states the year it paired on, per name).

## 9. Holds

| hold | on | owner | what lifts it |
|---|---|---|---|
| every `dossier --write` | this seat | `2.0.0_SA_COO~X` | chain A VALID; the pair signed |

-- `2.0.0_SA_COO~X`
