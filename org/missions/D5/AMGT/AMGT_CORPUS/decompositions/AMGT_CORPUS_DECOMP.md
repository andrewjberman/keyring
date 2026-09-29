# AMGT_CORPUS -- L5 decomposition v16.0 -- ROUND 16 (one cell: the daily trigger for induction_run)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-29 ~22:2xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-15 analysis
`ledger/ROUND_ANALYSIS.round15.md` @`c265fbb6ff` (msg 26742, READ-acked), s.2 ruling and s.4 ENRICHMENT LIST, one item.
Round 15's decomposition is kept as `AMGT_CORPUS_DECOMP.round15.md`. Base of the cut: CLOUD `8f7237f20f`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | schedule the existing `induction_run` (pinned commit, builder-named, first fire under a pair + NEVER-2 entry) | `CRPS-r-1` | `~1` |

**NOT cells** (the analysis): the six render outcomes (AMGT_RESAPP round 50); `Z-S59`; the two Disabled `OpalResearch-*`
tasks.

## 1. The rectangle

| cell | serves | `<risk>` | class | write set | the build |
|---|---|---|---|---|---|
| `CRPS-r-1` | FWD-4, FWD-19 | WORLD (the drain's registration and first fire) | worker | `lib/research/corpus/induction_scheduled.py` (new), `lib/research/corpus/schedule_induction.ps1` (new), `lib/research/corpus/tests/test_induction_schedule.py` (new) | the trigger only: an entry that computes today's UTC `as_of` and calls `induction_run.main`; a registration script whose `-Plan` names the builder's task name, a detached checkout of a pinned commit, and the action; an offline test of the scheduled path on planted folders |

## 1a. Re-groundings at L5

- **The producer exists and is complete.** `induction_run.py` makes ONE `add_security --batch` call per run, and NO call when
  the population is empty. It REFUSES ambiguous and folder-token-disagreeing rows. `--fire` is gated on `OPAL_INDUCTION_FIRE=1`
  plus today's `as_of`, and is refused under pytest. The cell does not edit it.
- **The name is builder output** (Rule 30), measured at the cut: `opal_naming.name('amgt', None, 'induction', 'daily')` ->
  `amgt-induction-daily`. No registry row is needed.
- **Pinned, never the shared tree.** Site-Z Scheduled Tasks run the tree they point at. The action's `WorkingDirectory` is a
  detached checkout of the merged commit, at a path derived from the repository root.
- **The producer's population rule has a limit (row `Z-S61`, filed with this issuance).** A folder whose ONLY identity evidence
  is its name, like Hitachi 6501 JP, is NO_EVIDENCE to `induction_run`, so the schedule would not have registered it. The
  analysis's contract ("every folder with no crosswalk row is registered") is therefore wider than the producer. The cell
  schedules the producer as ruled; whether to widen the rule is the CTO's call.
- **Drain (WORLD, the issuer's):**
  - `schedule_induction.ps1 -Register -Commit <merged sha>` under a never-widen pair and a NEVER-2 entry.
  - The first scheduled fire is the acceptance. Expected, by the producer's rule: population 0 of 96, so no call and no put.
  - Positive arm: AC1's planted folder on a scratch library.

## 5. The round -- one issuance, fan-out as data

- `fanout: 1 of 1 chains, cap 8, reason: one cell (the analysis's enrichment list has one item).`
- **Drain:** re-grade at the tip; merge; the pair; `-Register`; the first scheduled fire read from its log and the pool listing.
  Then the L8 packet goes to `3.0.0_SA_CVO~Z`.
- Surprise rows from `Z-S62`. Worker rows are `AMGT_CORPUS-Z-W1-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
