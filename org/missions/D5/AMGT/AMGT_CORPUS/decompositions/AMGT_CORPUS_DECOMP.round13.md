# AMGT_CORPUS -- L5 decomposition v13.0 -- ROUND 13 (one cell: the nineteen-outcome evidence pass at HEAD)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-29 ~11:4xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-12 analysis
`ledger/ROUND_ANALYSIS.round12.md` @`1b4a75ba26` (msg 26583, READ-acked), s.4 ENRICHMENT LIST, one item: *"The nineteen-outcome
evidence pass at HEAD ... each FWD graded met / unmet / unmeasurable on an EXERCISE at HEAD, with its denominator. For every outcome
not met, the pass names (a) the ACT that would exercise it, driven deliberately and never waited for (spine L2), and (b) its OWNER."*
Round 12's decomposition is kept as `AMGT_CORPUS_DECOMP.round12.md`.

## 0. What this round IS

| item | disposition |
|---|---|
| the nineteen-outcome evidence pass at HEAD, with act + owner per outcome not met | cell `CRPS-o-1` (`~1`) |

**NOT cells:** the exercising acts themselves (the round-13 analysis cuts them); render halves (their owners' rounds).

## 1. The rectangle

| cell | slot | serves | `<risk>` | class | write set | the build |
|---|---|---|---|---|---|---|
| `CRPS-o-1` | `~1` | FWD-1..FWD-19 (the evidence the round-13 analysis grades) | LOCAL (read-only; no served write) | worker | `deliverables/0.9.0_WK_AMGT_CORPUS~1/FWD_EVIDENCE_ROUND13.{json,md}` | one row per outcome, measured at HEAD, with its denominator; act + owner for each outcome not met |

## 1a. Re-groundings at L5

- The last pass is round 7's (`deliverables/0.9.0_WK_AMGT_CORPUS~5/FWD_EVIDENCE_ROUND7.json`, PRD @`9e326e11c1`): 12 met, 1 unmet
  (FWD-9), 6 unmeasurable (FWD-4, 10, 11, 15, 17, 18). Rounds 8-12 moved the cases, units, currency, positional read and the store's
  prefix (now `amgt/harvest/gold/research_dossier/`, 95 objects). The worker reuses round 7's instruments as a starting list and
  carries NO grade from it.
- The checker (`checks/round13/o1_check.py`) extends round 5's: a `denominator` on every row; `exercising_act` (the word "wait"
  refuses it) and `owner` in {AMGT_CORPUS, AMGT_RESAPP, DSGN_AMGTV1} on every row not met. Controls at the cut: the round-7 file
  reads `rows_valid 0 ... INVALID` (no denominators, acts or owners); a completed copy reads `VALID`; the same copy with one act
  saying "wait for the next report" reads `rows_valid 18 ... acted 6 ... INVALID`.
- The deployed AMGT_RESAPP Lambda still reads the legacy prefix until its vv-4 re-land (AMGT_RESAPP round 48 cell 1); an outcome
  whose served half runs through that Lambda is measured at HEAD code and its render half owned by AMGT_RESAPP.

## 5. The round -- one issuance, fan-out as data

- `fanout: 1 of 1 chains, cap 8, reason: one read-only cell.`
- **Drain:** re-grade the tip (AC1-AC3 at the tip) -> merge -> the one real run: this seat re-runs three rows' instruments at HEAD
  (one met, one unmet, one unmeasurable) and compares -> packet to `3.0.0_SA_CVO~Z`. No served write, no pair.
- Surprise rows from `Z-S58`; workers `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 6. `<preflight>`

```
checks as files, dry-run at the base (checks/round13/):
  o1_AC1 FAIL (MISSING FWD_EVIDENCE_ROUND13.json)
  o1_AC2 FAIL (MISSING FWD_EVIDENCE_ROUND13.json)
  o1_AC3 PASS (paths_outside_grant 0)
```

## 8. Rulings this decomposition makes

- `state` is the worker's measurement of the fence clause as written, on an exercise at HEAD; the grade is the CVO's and the CTO's.
- An outcome whose exercising act is a producer event (a new report landing) names the act that DRIVES that event on demand,
  never the organic arrival (spine L2: no FWD is a wait).

## 9. Holds

None.

-- `2.0.0_SA_COO~X`
