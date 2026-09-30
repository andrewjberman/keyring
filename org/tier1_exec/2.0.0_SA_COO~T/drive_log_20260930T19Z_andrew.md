# /canonical-drive -- 2.0.0_SA_COO~T -- 2026-09-30, hours 13Z-19Z (laptop, host andrew)

Post-crash relaunch (reboot 07:52Z). One tick run by hand; no cron (no LIVE_ARMS row names ~T). Lease FULL.

| time | project | limb | round | TOs t/T | cells | thread | act fired |
|---|---|---|---|---|---|---|---|
| 13:2xZ | NFRA_TRNSPT | L5 -> L6 | 1 | 0/12 | 12/12 cut | none | DRIVE FORWARD: decomposition + one issuance @81e350ba0a, fan-out 4 of 4, cap 8 |
| 14:4xZ | NFRA_TRNSPT | L7 | 1 | 0/12 | 12 | none | spawned ~1..~4; index drift fixed @17ad3ea043 |
| 16:0xZ | NFRA_TRNSPT | L7 | 1 | 6/12 | 12 | y | chain B drained @b9b933859f (FWD-1 trace real) |
| 17:0xZ | NFRA_TRNSPT | L7 | 1 | 10/12 | 12 | y | chain C drained @fed423d013 |
| 18:0xZ | NFRA_TRNSPT | L7 | 1 | 11/12 | 12 | y | chain A drained @26bc60a8cf |
| 19:0xZ | NFRA_TRNSPT | L7 -> L8 | 1 | 12/12 | 12 | y | chain D drained @8e22dc9ddb + 0225e80b2f; issuer real runs; drain-end packet |

Residue at relaunch: none of this seat's (no worktrees, no index.lock, no open deploys). MDPF_TAXSMA parked on Andrew's word;
15 non-terminal orders recorded in the issuance commit, not driven.

Decisions ruled inside the decomposition this window (each in its commit): registry domains as data, not a hand-kept table
(W4-S3); the PyPI `names` library as the name list under Andrew's call-2 word (W4-S1); the TR-a-1 check recut @0aa2b56c11; the
S1 closure as a new row (append-only channel).

Instrument lessons, stated once: (1) an issuance that flips a tree row must regenerate the generated project index in the same
commit, or every worker's org commit refuses; (2) a shared-tree drain of an append-only channel always conflicts -- reconcile
CLOUD into the worker branch inside its own worktree first, or conclude the union in the same call, so MERGE_HEAD never lingers;
(3) merging CLOUD INTO a branch re-grades rows another seat edited in place on CLOUD, the reverse direction does not; (4) a fixture
built from the issuer's description of a tool is not the tool: the first real input found S9.

Worktrees wk_nfra_trnspt_1..4 retired with their branches. Kept: portal branch `wk-NFRA_TRNSPT-3-portal` @d8bad891 (an unlanded
stamp-line restamp of `firmDisplayNames.generated.ts`), left for the portal lane; not deleted because it is not merged.
