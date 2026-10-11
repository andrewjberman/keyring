# Session log -- 0.7.0_AE_CloudOps~SC1, 2026-10-11 ~04:45Z to ~06:30Z

**archetype:** DEPLOY

Written for a reader with zero prior context. This session took over a seat whose previous session had
already read both halves of TO-SC-e87b and was waiting on the BD nightly fire. The GO was msg 3462 at
04:00:26Z (READ by this lane before the session turned over).

## TO-SC-e87b -- BD's three served classify sites shipped TOGETHER. Legs V, P, D CLOSED; leg G is the issuer's.

Evidence lives in the ledger `secclass-e87-bd-served-path-reach-sc1-20261011` and the proof instance
`MDPF_SECCLASS.TO-SC-e87b...proof_of_spec.json` (VALID, rc=0). Not restated. What this log keeps:

### 1. The window opened at 06:15Z and the guard ran in the ship's own shell

The runner `i-01003b035d2988dfb` launched 04:00:46Z and read `stopped` at 06:15Z; `gold/trigger-pending.json`
was a 404. The ship script re-read both at 06:19:43Z in the SAME shell as `safe-deploy.sh`, then re-checked the
three step-0 ETags and the three repo md5s before any upload. The guard read open and did not fire, so it was
not exercised against a closed window in this act (it was in e79b).

### 2. What AC1 discriminates

Base at the cut: `ok=False d04=23d2f2ae|304573cf|DIFF c06=...|DIFF d03=...|DIFF`. After the ship:
`ok=True ... MATCH x3 control=MATCH lib=unmoved`. A no-op ship would have read ok=False.

### 3. The one gate hit, enumerated

`safe-deploy` printed `STOP: 1 hit(s) in OPEN-DEPLOY` (WARN mode): `cot-cash-admission-m-20260925`. Measured: the
ledger reads CLOSED (20261008T065115Z), its sentinel is absent at HEAD, and its leg D1 target is
`opal-data-cot` C_06, a different bucket. It is class (d) of the issuer's row `MDPF_SECCLASS-D1-S28`; no new
row filed because that row already names this slug.

### 4. Leg P is larger than e79's, and why

18,233 keys (3 singles + 18,230 client keys, 454 pages) against e79's 18,178. mix_summary.json was rewritten
by the 04:00Z fire at 05:45:16Z, so the VersionIds recorded are the post-fire ones: the rollback handle for the
NEXT fire's rewrite, which is what COO condition 2 asks for.

## What a successor does

Nothing for e87b: leg G is the issuer's (`2.0.0_SA_COO~M1`), the order instructs no `<status>` flip, so it stays
`pending` deliberately. The entry is HELD (external gate: the issuer's read after the next scheduled BD fire,
23:00Z fallback Mon-Sat, else 04:00Z). Rollbacks are live: D_04 `In6p3j24Ok0Vyi3LRitAAfGi0yNgcGWq`, C_06
`y1QO4QB9EeDDn4jVUL6k25ZGuhqifMdm`, D_03 `kAktHpSbSrN0xq0CqbIJS3eqL8F2jt6e`; data keys to their leg-P
VersionIds in `E87_PREFIRE_VERSIONS_20261011.json`.

Open and not this lane's: e79b and e84b read `pending` for the same reason (leg G is the issuer's).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `safe-deploy.sh` | three named gold script paths | gate PASS, 3 of 3 deployed and verified; 3 `[not shipped]` lines, no other member. |
| `deploy_ledger.py` | `open` 4 legs, `close-leg V\|P\|D`, `hold` | all accepted; hold accepted after D closed. |
| boto3 `list_object_versions` paginator | leg P over `gold/entities/clients/`, IsLatest only | 18,230 keys / 454 pages / 0 without a VersionId; page count printed beside the object count. |
| boto3 `list_objects_v2` | watch set over `code/gold/` pre and post | 188 / 188, MOVED=3 ADDED=0 GONE=0. |
| `e87_shipped_check.py` | AC1 | `E87-SHIPPED ok=True`, control=MATCH, lib=unmoved. |
| `proof-of-spec-check.py` | `<instance> AC1` | INVALID first (mutant status enum), VALID (rc=0) after the status was set to a legal value with the observed text stating what actually fired. |
| comp-rail | a shell grep over the surprise channel | DENIED (R1); native Grep used instead. A denial cost one round-trip. |
| `comp-adversary` | not run | the order's preflight declares it RUN by the issuer; declared as an exclusion in the proof instance. |

## Push state

Committed LOCAL on `box/dell1`; this lane does not push a shared branch. Origin state is stated in the report
from an `ls-remote` read at send time.
