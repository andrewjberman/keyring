# ANDREW-DIRECT 2026-10-06 ~13:5xZ -- Yang owns the CIX re-save and the re-pull; site Z reboots, every seat writes a /handoff first

Given at the `0.0.0_AB_MSTR~Z` terminal (site Z).

## Context

1.0.0_SA_CTO~Z's fix route for the index-benchmark N/A (@5e0c045e8d) had three steps:
(1) a producer guard on yang-model-portfolio-benchmarks;
(2) the CIX owner re-saves the 7 frozen definitions in CIX <GO>;
(3) re-pull, then /data-refresh.
Andrew was asked who owns step (2).

## Verbatim

Andrew: "yang will handle it, hes responsible and will repull. this device however is having an issue and we need to
reboot. tell all workers to write a /handoff and save it with state so they can get back to work post reboot"

## Scope as read (surfaced, not adjudicated)

- Steps (2) and (3) belong to Yang Liu: he re-saves the 7 CIX definitions and re-pulls. No seat signs in to the Terminal
  for this, and 0.0.0_AB_MSTR~Z does not re-run the pull for it.
- Step (1), the producer guard, is not addressed by this word. It stays with 2.0.0_SA_COO~Z as seated, after the reboot.
- Site Z reboots. Before that, every live seat writes a /handoff with its state and commits it. No new deploy starts, and
  any deploy in flight is finished or rolled back under NEVER-2.
- The no-modify lift for the per-series recency check remains unanswered.
