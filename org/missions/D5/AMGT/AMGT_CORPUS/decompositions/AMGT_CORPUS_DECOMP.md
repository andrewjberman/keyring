# AMGT_CORPUS -- L5 decomposition v11.0 -- ROUND 11 (the enrichment round after the round-10 analysis)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-29 ~07:3xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-10 analysis
`ledger/ROUND_ANALYSIS.round10.md` @`8b54c2b4fd` section 4, two cells (msg 26489, READ-acked), answering `3.0.0_SA_CVO~Z`'s
slug on `ADJUDICATION_v13`. Round 10's decomposition is kept as `AMGT_CORPUS_DECOMP.round10.md`. PRD v0.6 @`9e326e11c1`, ADMITTED.

## 0. What this round IS

| item (analysis s.4) | disposition |
|---|---|
| 1 a currency where the pack's symbol and the listing agree on exactly one (ruling 2) | cell `CRPS-m-1` (`~1`, first) |
| 2 a positional read of the six blank Base cells (ruling 3) | cell `CRPS-m-2` (`~1`, second) |

**NOT cells** (the analysis): the Base anchor (ruled @`1621a80b0c`); `Z-W2-S12` (closed by ruling 4); worktree removal (Andrew).

## 1. The rectangle -- one chain (both cells write `lib/research/corpus/dossier.py`), one pair, one served rewrite

| cell | slot | serves | `<risk>` | class | write set | the build |
|---|---|---|---|---|---|---|
| `CRPS-m-1` | `~1` (first) | FWD-12 (the unit's claim) | SERVED (the shared rewrite) | worker | `dossier.py`, `tests/test_dossier_case_currency_intersection.py` (new), `tests/test_dossier_case_unit.py` | `_case_currency`: a currency when the symbol's ISO set INTERSECTED with the listing is exactly one code |
| `CRPS-m-2` | `~1` (second) | FWD-12 limb 3 (six names) | SERVED (the shared rewrite) | worker | `dossier.py`, `tests/test_dossier_case_positional.py` (new), `tests/test_dossier_case_layouts.py` | a short table row is placed by the pdf page's x-coordinates when, and only when, the position puts the blank in exactly one column; `--case-positional-census`; `METHOD_VERSION` /4 |

## 1a. Re-groundings at L5

- **m-1.** `_case_currency` (dossier.py, @`bc50ea89cf`) returns a currency only when the symbol alone maps to ONE ISO code AND
  it equals the listing; `$` maps to (USD, CAD, AUD), so it never sets. The ruling's criterion is the INTERSECTION of the
  symbol's set with the listing. Measured symbol-bearing names (l-1's report): AZN U+00A3/GBp, BP/ `$`/GBp, CPA `$`/USD,
  ML U+20AC/EUR, ORA `$`/EUR, SAP `$`/EUR, SHOP `$`/CAD, SPOT `$`/USD, TTE `$`/EUR, UNVGY `$`/USD. **Under the ruled rule:**
  CPA, SPOT, UNVGY -> USD; ML stays EUR; **SHOP_CN -> CAD** (`$`'s set contains CAD, the listing is CAD); every other stays
  null. **The analysis expects "CPA, SPOT, UNVGY -> USD, and no other name moves" -- its own rule also moves SHOP.** This
  file does not choose: m-1 builds the rule as ruled, the census prints every set name, and the never-widen pair (which
  names each moving name, CTO-signed) decides SHOP before anything is served.
- **m-2.** The six (8035_JP, BZLFY_US, HEI_US, SNPS_US, TSM_US, V_US) serve ABSENT: "row 'EPS' has 14 of 15 cells; the empty
  cell's position is not recoverable from line order (no x-coordinates)". The stored extraction lines carry no
  x-coordinates; the bronze pdf is reachable by the picked row's `bronze_key` (read-only). Importing `dossier` must still load
  no PDF library (round 10 amendment 1): any fitz/pymupdf use is inside the function that needs it.
- **The rewrite writes only with a method bump:** m-1 and m-2 change what a case serves but move no dossier `inputs`;
  `write_one` writes nothing when the stored method AND inputs are unchanged. m-2 bumps to `amgt-corpus-dossier/4`.

## 2. Rule 24 record

m-1 changes one predicate: `currency` = the single element of (symbol's ISO set) intersect {listing}, else null with the existing
basis values (plus `symbol's currency differs from the listing` when the intersection is empty). m-2's positional census
partitions the six into `placed` / `ambiguous` / `no_positions`, summing to 6; a name is `placed` only if every value of every
short row falls in exactly one column band and exactly one column per row is empty.

## 3. Placement

Both cells on this project's corpus package; m-2 reads bronze pdf bytes from S3 (read-only). No other project's file.

## 4. Dependency edges

Chain: m-1 -> m-2 -> drain -> ONE never-widen pair naming (a) each name whose currency moves (CPA, SPOT, UNVGY, SHOP as
measured) and (b) each of the six names' two branches (placed / stays ABSENT) -> change entry -> `dossier --write --workers
10` -> verify -> the CVO grades.

## 5. The round -- one issuance, fan-out as data

- `fanout: 1 of 1 chains, cap 8, reason: both cells write dossier.py; one queue on ~1 (m-1 first), one pair, one rewrite.`
- Drain duties: the corpus suite, `py_compile`, ruff; the worker re-graded at its tip; the pair; the rewrite; the one real run:
  `read_dossier` on CPA (USD), SHOP (as the pair rules) and one placed name if any.
- Surprise channel rows from `Z-S57`; workers `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 6. `<preflight>` -- what this decomposition actually ran

```
prd-signoff.py status AMGT_CORPUS        v0.6 @9e326e11c1 EXECUTING -> ADMITTED
task-order census (last <status>)         CRPS-l-1..l-4 complete -> 0 open on this project
checks as files, dry-run at the base      checks/round11/: m1_AC1 m2_AC1 FAIL (no tests ran); m1_AC2 FAIL
                                          ('m1 names 95 currency_set 1 ML_FP_Equity=EUR'); m2_AC2 FAIL (argparse refuses
                                          --case-positional-census); m2_AC3 PASS (l3 absent_generic 0 sum 6);
                                          m2_AC4 PASS (dossier import loads no PDF library)
```

## 7. Rulings this decomposition makes, and what it REFUSES to assume

- m-1 implements the ruling's criterion literally (intersection); it does not special-case SHOP either way -- the pair does.
- m-2 serves a value only where position alone places it; arithmetic (Price = EPS x Multiple) is never a placement rule.
- m-2 bumps `METHOD_VERSION` to /4 (round 8's lesson: no bump, no write).
- REFUSED to assume: that the positions will place all six (m-2 reports each branch).

## 8. Holds

| hold | on | owner | what lifts it |
|---|---|---|---|
| every `dossier --write` | this seat | `2.0.0_SA_COO~X` | the chain VALID; the pair signed, SHOP ruled in it |

-- `2.0.0_SA_COO~X`
