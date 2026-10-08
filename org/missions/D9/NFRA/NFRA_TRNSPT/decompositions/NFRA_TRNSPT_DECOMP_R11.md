# NFRA_TRNSPT decomposition -- ROUND 11 (2026-10-08, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on 1.0.0_SA_CTO~DELL2's round-10 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_10_20261008.md`
@8ce4b5098e (msg 1620) and ruling msg 1608 (row D2-S5: a securities ALLOWLIST from the served security master, not a new detector).

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-a-11` | E1: the versioned securities allowlist + the research fold honoring it + the planted-token gate | FWD-5 | dell2 worker | LOCAL | worker | -- |
| `TR-b-11` | E2: re-fold and re-write the 29 Research objects (laptop write, as round 9), read back on the stored bytes | FWD-5 | ISSUER (served; the laptop writes) | SERVED | -- | TR-a-11 drained |

**Chains.** A = TR-a-11 -> TR-b-11. Fan-out 1 of 1 worker chain, cap 8.

**Issuer rulings.**
1. **The served security master is DynamoDB `etf-classifications`** (us-east-1, hash key `ticker`, column `name`): the canonical per-security
   table of Andrew-direct 2026-09-29 (`org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260929_175xZ_ONE_CANONICAL_SECURITY_TABLE_FOR_ALL_HOLDINGS.md`),
   firm-neutral. The issuer snapshotted it at the cut (a worker holds no AWS call):
   `data/transcripts/scripts/teams/securities_source_20261008.json` -- 11,172 table rows read, 5,207 kept (`asset_class == equity` with a
   name), fields `ticker` and `name` only. MSFT "Microsoft Corp", AAPL "Apple Inc", AVGO "Broadcom Inc", NVDA "NVIDIA Corp", XOM
   "ExxonMobil Holdings Corp" are present.
2. **The mail wipe is not changed.** The research fold widens `wipe.Assets.allow` (the per-token allowlist the wipe checks first,
   `outlook/wipe.py:147-159`, rule 4 at :9) with the securities tokens. The mail pull's wipe is untouched.
3. **The fifth company is Exxon** (the fifth of round 10's probes; the CVO named none in the channel). Its source name is "ExxonMobil",
   while the transcripts say "Exxon"; whether it recovers is reported, not forced.
4. **Known limit, stated:** an issuer name that is also a surname (e.g. Ford, Dell) survives the wipe wherever it appears; the gate tests
   a planted person name that is NOT an issuer.
5. **E2's write overwrites the project's own 29 objects** (versioning keeps the priors); a literal key list the actor controls
   (never-widen non-application). dell2's key grant is Decrypt-only, so the laptop writes, as in round 9.

## Rule 24 record

Domain: analysis s.3 E1 (1)-(2), E2 (1)-(3). E1 = TR-a-11 (AC1 list, AC2 gate). E2 = TR-b-11 (issuer read-back: five-company re-probe with
Microsoft > 0 the arm; re-wipe + an independent PII sweep at 0; held-out vs 4,555). Remainder: none.

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R11_CHECKS/r11_checks.py` at base box/dell2 1c4acb766b:
a11-list FAIL (absent), a11-gate FAIL (absent).
