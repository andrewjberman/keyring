# IRPT_BCKEND round 68, workstream ~Y -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~Y2` (issuer, dell2) **for** `3.0.0_SA_CVO`, 2026-10-08 ~21:4xZ. Risk WORLD (the L6 gate floor; the pair names
SERVED). Decomposition: `decompositions/IRPT_BCKEND_DECOMP_R68_Y.md`. Issuance: @4e455af9e6. The cell is release 3: the E6 build
proven on the TEMPLATE lane, with no new grant. It ran on CTO GO msg 1643, on Andrew-direct "You have egress to ycharts, do not delay".

## Terminality

**1 of 1** order is drained. It stays `pending` until AC2 is graded on the laptop's cleanup result (9 keys relayed ~21:4xZ).
Drained @84916b911a (8 paths, 0 dropped, 0 foreign; index check 0 of 8 differ). The worktree and branch are removed.

## What ran (BRANCH A: LIVE)

| step | result |
|---|---|
| pre-checks | census = 4 members; live `ZspX0qD2...`; opal-partner grant present; withdrawn CSV grant absent |
| ledger | `irpt-ycg-release3-20261008` opened before any write; CLOSED, L1-L4 |
| upload + apply | built `Un0wVZqj...` = signed; S3 version `NqbpRnnx...`; targeted 0/1/0, plan committed first @16f4e4ac90; **live 21:26:18Z** |
| after-reads 0-2 | PASS (grant read-back; live = built, re-plan 0; import census 62 modules `failed: {}`) |
| after-read 3 | test filer put (no login identity; `allowedFirmIds` = [49financial]); deleted; NOT FOUND |
| **after-read 4 (real on-behalf admit, template lane)** | advisor `adv-04b85b8aefda` at 49financial: RESOLVING, then NORMALIZED on the first re-POST of the same token (`input_id` `portfolio_7112270b...`); upload `UP-a5f12db5...`; body sha256 `fdb23578...` |
| after-reads 5-7 | 5: unlisted-firm advisor `adv-27637b75127c` refused NOT_AUTHORIZED. 6: unlisted firm (inflection) refused FIRM_BINDING. 7: ordinary own-firm upload refused NOT_AUTHORIZED, as row D2-W158-S2 predicted. None returned an upload id. |
| vendor egress | only the resident's own `securities_info` resolution for the one admit (authorized); the worker made no vendor call |

| criterion | worker | issuer re-run at 84916b911a |
|---|---|---|
| Y68-1-AC1 | PASS (8 of 8 reads) | PASS; live `Un0wVZqj...` re-read |
| Y68-1-AC2 | FAIL, PENDING-ISSUER (test row NOT FOUND; 9 admit keys, 0 laptop results) | pending the laptop |
| Y68-1-AC3 | PASS (branch A) | PASS |

**Served state:** `irpt-ycharts-generate` = `Un0wVZqj...` (release 3). TCKT_VNEXT X-1 is live. `2.0.0_SA_COO~V2` has been told TV-r-1 may
run in Alyssa's sign-in (her entitlement was written @d6bace6f09).

## Rows for your L9

| row | what it says | my read |
|---|---|---|
| D2-W159-S1 (OBSERVATION, INERT) | `record-terraform-deploy.sh` stages `infra/aws/terraform/investor-reporting/CHANGELOG.json`, which is outside the order's paths; the source-map half was committed and the CHANGELOG entry was not. | The recorder stamps HEAD on EVERY function of the pipeline, so running it for a one-function release would mark functions with code they do not run. The CHANGELOG has not recorded `irpt-ycharts-generate` since 2026-09-23 (releases 1-3 are all missing). The deploy ledgers are this function's authoritative release record. Recommend a recorder scoped to one function, routed to the CI owner, rather than a hand entry here. |
