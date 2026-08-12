# INF_RUNNER_REFACTOR.P1 — Group A + parquet writer-format built, QA-run, proof-instanced (0926–1005Z)

**archetype:** IMPLEMENT
**Serial:** 0.4.0_DS_ClientPlatform~A (Andrew-instantiated ~0924Z for INF P1, parallel with base's 49F P1)
**TO:** INF_RUNNER_REFACTOR.P1.scripts-groups-a-d-parquet (COO dispatch 092643Z; TO file confirmed on disk)
**Commits:** id mint @e1c11a8b37 (pre-registered before evidence) · Group A build @7564cf53ab

## What was built (data/inf/scripts/gold/runners_inf/)

Seven Group A artifacts + the harness, field-SOURCED from INF silver per @6e180df78e (no 49F code
ported): runner_common (parquet {table}/date={D} writer + atom-3 manifests + atom-9 provenance +
paginated readers; output root INJECTED per run — F-1 undecided, no default), a00 dim_account
(DERIVED rep-scope predicate from the representatives dim: 19 reps, 869/869 universe, zero
allowlist constants), a01 dim_relationship (F-5 census 869 mapped + 0 self-family == 869),
a02 dim_boundary (VERSIONED; collection detection ABSENT-with-shape on the measured structural
fact — 0 of 20,504 Management Fee rows carry the payee side; 2 Fee-Credit reversal accounts
declared noise and kept in book), a03 dim_security (1,658-ticker live spine; stale enrichment
vintages declared), a04 dim_calendar (trading_calendar JOIN × 2,450 observed partitions; 6 true
gaps named — all 2019-09 ramp week; 722 STATEMENT-DAY artifacts declared, never promoted),
a05 ref_txn_classification (full 1.43M-row census, 46 codes, ratified taxonomy v2 verbatim +
gips_class projection; 743 rows / 0.052% rows / 0.050% $ UNRESOLVED-LOUD across 5 named codes),
a06 dim_identity_crosswalk (near-identity, both denominators, off-spine ids carried as findings).

QA = ad-hoc run-and-read against live silver 2026-08-11 into the session scratchpad (nothing
standing). Controls: a02 determinism STABLE (boundary_version identical across two same-input
runs), a02 mutant FIRED (dropped account flips version), a05 census key re-derived identical on a
second full-series run, writer no-root REFUSE fired.

## Findings (surfaced same-window to COO, no action taken)

1. Five txn codes absent from the ratified taxonomy land UNRESOLVED-LOUD (Stock Split 553 /
   Remark 174, $1.79M abs / Reverse Stock Split 9 / Reversal 6, $273K / Expired- 1). Taxonomy
   amendment is a ruling-class act (the yaml is CTO-ratified) — surfaced, not guessed.
2. Off-spine account ids per surface (16 txn / 79 positions_mv / 73 perf / 73 billing) = the
   closed-account class: current-day accounts_v2 cannot frame deep history. W-D point-in-time
   scope; declared, carried into B/C backfill design as a limitation.
3. The a02 detection amendment: the custody ledger structurally lacks the fee payee side, so the
   INF spec's ELSE branch (ABSENT-with-shape) is the TRUE verdict — the naive net>0 predicate
   would have ejected a live managed client account (4320 "Thompson") from the book on a $0.17
   fee credit.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-to | comp-to INF_RUNNER_REFACTOR.P1.scripts-groups-a-d-parquet | session TO context set |
| comp-find | comp-find "unified_account_dim" data/inf | located bronze pull scripts + denominator 47 hits/207 files; activity dim confirmed as silver landing |
| comp-which (A.3 exercise) | comp-which "how do I grep the repo" | forwarder RAN (PATH probe: 96 of 97 resolve bare) |
| comp-validate | comp-validate a00_dim_account | no script matching — new family unregistered in gold_validate_config; DECLARED exclusion, config authoring routed to wave close (NO_CONFIG = UNVALIDATED, not signaled safe) |
| comp-pipescript | comp-pipescript io a00_dim_account --pipeline inf | Script not found — registry does not know runners_inf yet; registration is P2/P3 wiring scope, declared |

py_compile ran stage-by-stage per script (Andrew @4dbf4a0d7c), logged per stage in the build
transcript; ruff clean at commit (commit-gate exercised: caught 4 findings across 3 files, fixed).

## Next

Group B id mint from its battery, then b00–b03 build. Group C after. D = HOLD FOR RULING; my
C-completion report fires the ruling (Andrew ~0928Z via COO 093155Z).
