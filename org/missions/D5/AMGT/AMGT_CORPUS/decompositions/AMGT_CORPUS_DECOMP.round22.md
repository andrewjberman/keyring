# AMGT_CORPUS -- L5 decomposition v22.0 -- ROUND 22 (three cells; each served act under a pair)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-30 ~04:5xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-21 analysis
`ledger/ROUND_ANALYSIS.round21.md` @`0bf907bee8` (msg 26915, READ-acked), s.4 ENRICHMENT LIST (three items) and s.2 rulings 1-4.
Round 21's decomposition is kept as `AMGT_CORPUS_DECOMP.round21.md`. Base of the cut: CLOUD `2a4c7f5451`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot / executor |
|---|---|---|---|
| 1 | `pack_shape` served: the `METHOD_VERSION` bump + the dossier rewrite | `CRPS-x-1` | `~1` builds the bump (LOCAL); the rewrite is the issuer's WORLD act under a pair |
| 2 | the unit apply: 8 per-security units with evidence and read count; 5 model blocks re-derived | `CRPS-x-2` | `~2` builds the apply writer (LOCAL); the `field_map.json` commit and the re-derive are the issuer's WORLD act under a pair |
| 3 | re-sign `r-1` | `CRPS-x-3` | the issuer's WORLD act; COO half SIGNED @`0d437b429d` (`NEVER_WIDEN_ROUND21_INDUCTION_SCHEDULE_RESIGN.md`), CTO half owed |

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-x-1` | WORLD at the drain (the order itself is LOCAL code) | `lib/research/corpus/dossier.py` (the `METHOD_VERSION` line only), `.../tests/test_dossier_method_bump.py` (new), `.../tests/test_dossier_case_positional.py`, `.../tests/test_dossier_case_body.py`, `.../tests/test_dossier_case_unit.py` (their `/4` literals) | `amgt-corpus-dossier/5`, so `write_one` writes |
| `CRPS-x-2` | WORLD at the drain (the order itself is LOCAL code) | `integrations/bloomberg/research/build_unit_map.py`, `.../tests/test_build_unit_map_apply.py` (new) | `apply_discriminated(facts, field_map_path, s3=None)`: writes only RESOLVED facts, each with `unit_evidence` {`method`, `reads`, `detail`}; never an UNRESOLVED fact, never any other entry |

Write sets are disjoint. x-2 runs its apply only on a temp copy; the committed `field_map.json` is written by the issuer's pair
act alone.

## 1a. Re-groundings at L5 (measured)

- **x-1's rewrite, expected diff read from the writer** (`checks/round21/w1_expected_moves.py` over the dossier's 95 resolved
  names, HEAD `5b55a4ee1d`; `evidence/r21_w1_expected_moves.txt`):
  - `names 95 built 95 errors 0 pack_shape_only 95 other_moves 0`, and `pack_shape pdf 48 docx 25 mixed 4 none 18`;
  - every dossier gains `pack_shape`, and no other field moves (ruling 2's bar).
  - The analysis says "96 folders"; the dossier's own universe is 95. 6501 is the 96th census key, with no report.
- **x-1, the served read path.**
  - The deployed scoped API reads dossiers through its OWN packaged `read_dossier`, which prefers objects naming ITS
    `METHOD_VERSION` (`/4`, `dossier.py:1310`).
  - So a `/5` rewrite adds objects that the deployed reader does not pick until AMGT_RESAPP redeploys with `/5`. That is its
    r52 pass-through item.
  - The rewrite moves no served page by itself; the pair names that.
- **x-2, the read count, measured** (`discriminate_facts` at HEAD `2a4c7f5451`): **all 8 RESOLVED facts rest on 1 read.**
  - SALES_REV_TURN, CURR_ENTP_VAL and BEST_SALES use value / CUR_MKT_CAP; NET_DEBT uses |value| / CUR_MKT_CAP.
  - The per-share x shares read exists only for SALES_REV_TURN and is skipped on 6501 and 8316 (row `Z-W2-S16`(b)).
  - Ruling 3's "the other six state 2 reads" does not match the measurement. The entries state the MEASURED count, which is 1
    for all 8 today; this is the ruling's intent ("the unit with its strength of evidence") carried with the measured number.
- **x-3:** its dependency is met. AMGT_RESAPP `zz-1` drained @`fde642f9f6` (msg 26911), and the COO half is signed against
  `33c1d096a3`.

## 5. The round -- one issuance, fan-out as data

- `fanout: 2 of 3 chains, cap 8, reason: x-1/x-2 independent builds (disjoint write sets); x-3 is the issuer's WORLD act on its
  own pair, no order.`
- **Drain, per chain:**
  - Re-grade, then merge.
  - Then the issuer's WORLD act under its pair, each with a NEVER-2 entry opened at start and closed with content proof.
  - x-1: the 95-name rewrite. x-2: the apply to `field_map.json`, its commit, then the re-derive of the 5 blocks (6501, 8316,
    9433, 8035, 8766). One executor (this seat) may run both acts under one entry (ruling 3).
- The L8 packet goes to `3.0.0_SA_CVO~Z` after the acts, or states which pair is still owed.
- Surprise rows from `Z-S68`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
