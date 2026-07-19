# audit-archive-invoker -- FINDINGS (append-only)

Durable, human-readable record of every finding the audit-archive-invoker emits: non-append edits
(clause 2), stale baselines (clause 1), invoker death (clause 4), coverage gaps, and snapshot
failures. It states the EDIT, never an opinion on authority (clause 3) -- a human rules on whether an
edit was authorized. Owner: 0.7.0_AE_CloudOps. Gate: 1.0.0_SA_CTO.

This file is itself append-only, mirroring the logs it guards.

Format per entry:

    ## <UTC timestamp> -- <CLAUSE> -- <VERDICT>
    - log: <path>          (when log-scoped)
    - detail: <what was detected>
    - action: <what the invoker did>

<!-- entries append below this line -->

## 2026-07-19T191123Z -- LIVENESS -- STALE-BASELINE
<!-- sig: LIVENESS|STALE-BASELINE||baseline #-#-#T#Z is #.#h old (>#.#h) AND uncaptured tail exists -->
- detail: baseline 2026-07-16T175907Z is 73.2h old (>24.0h) AND uncaptured tail exists
- action: minting fresh snapshot below
