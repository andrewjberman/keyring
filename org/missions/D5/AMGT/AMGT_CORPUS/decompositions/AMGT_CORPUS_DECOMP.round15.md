# AMGT_CORPUS -- L5 decomposition v15.0 -- ROUND 15 (two cells: one resolved at L5 by evidence, one issuer served act)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-29 ~21:5xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-14 analysis
`ledger/ROUND_ANALYSIS.round14.md` @`c2e8fc74f6`, s.4 ENRICHMENT LIST (two items) and s.2 rulings 3-4.
Round 14's decomposition is kept as `AMGT_CORPUS_DECOMP.round14.md`. Base of the cut: CLOUD `3cccb8db91`.

## 0. What this round IS

| # | item (analysis s.4) | cell | class |
|---|---|---|---|
| 1 | a dossier reads by its own name when the ticker holds `/` (`Z-W4-S5`) | `CRPS-q-1` | RESOLVED AT L5 by the issuer's measurement; no order |
| 2 | crosswalk rows for library folders newer than the crosswalk (`Z-S58`, RESAPP `Z-S303`) | `CRPS-q-2` | issuer SERVED act under a never-widen pair; no build, no order |

**NOT cells** (the analysis): the six render outcomes (AMGT_RESAPP round 50); `Z-S59` (the tool's owner); the temp cleanup
(operator).

## 1. The rectangle

| cell | serves | `<risk>` | write set | the act |
|---|---|---|---|---|
| `CRPS-q-1` | the served read of 2 covered names (`BP/ LN`, `NG/ LN`) | LOCAL | none | measurement only (1a) |
| `CRPS-q-2` | FWD-4's organic arm; identity for every folder newer than the crosswalk | SERVED | `crosswalk/v1/<today>.json` (pool), one bronze identity object, `lib/research/identity/registrations.json` (+1 row) | `add_security --folder "Hitachi 6501 JP" --bloomberg "6501 JP" --write-pool`, under the pair |

## 1a. Re-groundings at L5

- **q-1 -- the gap the row named is in the SWEEP, not the read path.** Measured 21:42:14Z at HEAD
  (`deliverables/2.0.0_SA_COO~X/evidence/r15_q1_slash_read.txt`):
  - `read_dossier("BP/_LN_Equity")` and `read_dossier("NG/_LN_Equity")` return their served objects under
    `security_key=BP-SLASH-_LN_Equity` / `NG-SLASH-_LN_Equity`, the writer's own encoding (`crosswalk.slash_safe_key`).
  - All 95 dossier partitions decoded through `crosswalk.security_key_from_slash_safe` read: `read_ok 95 fail 0 slash_keys 2`.
  - Negative control: the partition form passed as a key raises `SlashSafeKeyError`, which is correct, because it is not a key.
    `Z-W4-S5`'s sweep (`.scratch/p4/sweep.py`) took the partition name as the key and never decoded it.
  - `continuation._resolved_security_keys()` carries both names in the `/` form (95 of 95).
  - **Ruled:** no build is owed. A dedicated round-trip test would be a cell cut for coverage alone. The route-level `/` test
    already exists (`lib/research/api/tests/test_slash_safe_security_route.py`), as does the key-form test
    (`lib/research/identity/tests/test_slash_safe_key.py`).
- **q-2 -- nothing to build; the gap is an input never registered.**
  - `add_security --folder "Hitachi 6501 JP"` alone reads the id from a `*ONE PAGER*.xlsx`. The folder has none, so the
    dry-run at 21:43:19Z returned UNRESOLVED with 0 calls.
  - With `--bloomberg "6501 JP"`, taken from the folder's `<Name> <ROOT> <CC>` name, the dry-run at 21:44:16Z made one
    scripted call and returned `MEASURED 6501_JP_Equity 'HITACHI LTD' ... AGREES`.
  - The write lands the served crosswalk key, so it is the issuer's act under a never-widen pair
    (`deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND15_HITACHI_CROSSWALK.md`). The identity choice is named in the pair for the
    CTO half to grade.
  - Vendor authority: Andrew R-21 `b390c36444`, through the script.
  - Verify: `checks/round15/q2_census.py`. At base it reads `folders 96 resolved 95 unresolved 1 ambiguous 0 hitachi
    UNRESOLVED` and `added 0 removed 0 changed 0` against `crosswalk/v1/2026-09-25.json`.

## 5. The round -- one issuance, fan-out as data

- `fanout: 0 of 2 chains, cap 8, reason: q-1 resolved at L5 by measurement (no build owed); q-2 is the issuer's served act
  under a pair (a registration run, no code).`
- **Close:** q-2's change entry closes on the pair's after-state reads. The one real run is `q2_census.py` against the pool,
  plus `induction_request.run()` for FWD-4's organic arm. Then the L8 packet goes to `3.0.0_SA_CVO~Z`.
- Surprise rows continue from `Z-S61`.
