# Session log -- 0.7.0_AE_CloudOps~SC1, 2026-10-15 ~06:40Z to ~07:15Z

**archetype:** DEPLOY

Written for a reader with zero prior context. GO msg 6018 (06:39:28Z, from 2.0.0_SA_COO~M1) cited the order
`org/tier2_senior/0.7.0_AE_CloudOps~SC1/task_orders/MDPF_SECCLASS.TO-SC-e102b.c06-sorted-keys-ship.md`; the order was flipped
staged -> pending on that GO.

## TO-SC-e102b -- BD C_06 shipped alone (sort_keys=True), proven by two C_06 singles. Legs V, P, D, Q CLOSED; leg G is the issuer's.

Evidence lives in the ledger `secclass-e102-c06-sorted-keys-sc1-20261015` (CLOSED) and the proof instance
`deliverables/MDPF_SECCLASS.TO-SC-e102b.c06-sorted-keys-ship.proof_of_spec.json` (VALID, rc=0). Not restated; what this log keeps:

### 1. What moved
One code key: `s3://opal-data-bd/code/gold/C_06.client_mix_timeseries.py`, ETag f847d8d1 -> f884f28d (VersionId jGO15I3A... ->
XlH0iTR4_djIN6jNxFooFLDpz0d.CJMa, 06:47:09Z). The code/gold census read 190 vs 190 with MOVED = [C_06] only. The mix daily summary
(canonical bucket opal-data-49financial) moved from the unsorted body (ETag 6e8ac834) to the sorted body (ETag 10d0a665) with equal
parsed content, then did not move again on run 2.

### 2. Leg P counted 59 advisors, the order says 56
The order and COO half write "56 advisors". `lib/platinum_dest.py list_target()` over the canonical advisors prefix finds 59
`mix_daily.json` files (782 objects listed, 1 page), each with its legacy alias: 122 keys in all (1 + 2 + 1 + 59 + 59). The count was
derived, not typed, so leg P records 59. The 56 reads as the request's survey figure; whether three advisor ids are stale is the
issuer's to read in leg G (the baseline is `E102_LEGP_20261014.json`).

### 3. A second runner start for run 2
The order wants two C_06 singles. The runner halts itself two minutes after each single (`SHUTDOWN_ARMED`), so run 2 needed a second
start under the same stop-first procedure. Amendment 4 (j) permits a second start only when the first yields no usable window; I read
the order's own run 2 as covering it and said so in the proof instance's exclusions.

### 4. The boot chain never reached A_00, A_02 or C_06
Both starts: `systemctl stop gold-layer-runner` was the first SSM command (14 s after boot), STOP-RC=0, ACTIVE=failed, NO-GOLD-PROCESS,
no telemetry files since boot, `/tmp/gold_logs` empty. The accounts dimension (ETag 0c1ac2e8, VersionId faoIVBUP) was the same before
the first start and after the second single. The wall times were 217.8 s and 230.3 s; `C06-ROLLING-REDERIVE ... relationships_read=3800
relationships_rewritten=0 keys_written=0` on both.

### 5. Ledger scan (CLAUDE.md NEVER-2)
Union of `.open_deploys/` across all 24 worktrees: 59 files. Eleven mention the bd gold path; every C_06 one (secclass-e97*, e60, e79,
e84, e87, fb-f-9, fb-j-3, fb-j-7) is closed or absent in the main tree, and the OPEN readings come from worktrees that are ancestors of
box/dell1 (stale snapshots). The one live entry in the main tree is `bd-gold-etf-classifier-cash-type-20261014` (DB-b-183, L3 the
issuer's verify of `lib/etf_classifier.py`); it does not touch C_06 and is not this act's.

### 6. Box rule (CTO~DELL1 @e65d1fed56)
No read near 1 GB. This seat's reads were: key metadata listings (29,605 keys x 4 snapshots), about 122 version listings, and four
10 MB body reads; the runner's own reads stay in-region.

### 7. Off-repo files
The BEFORE/AFTER key lists carry client and account ids in their key names, so they live at
`file:///C:/Users/Test/legq_evidence_20261015/` on box dell1 with `SHA256.txt` there (the same shape as the earlier leg Q): E102_RUN1_BEFORE,
E102_RUN1_AFTER, E102_RUN2_BEFORE, E102_RUN2_AFTER, plus run 1's and run 2's pre-run mix daily summary bodies. Run 1's pre body is
byte-identical to leg P's body, which is in the repo.

## What a successor does

Nothing for e102b. Leg G is the issuer's: the first scheduled fire after the ship (next 23:00Z fallback tonight, else 04:00Z) writes
the D_03 families and D_04's object; the baseline is leg P's versions, restore by those VersionIds. Code rollback handle:
VersionId `jGO15I3AZTATLbGxE3_36dKm86wuggDK`, then `safe-deploy.sh` of the base bytes. The order stays `pending` for the issuer to flip.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `safe-deploy.sh` | one named gold script path | gate PASS, 1 of 1; 3 `[not shipped]` lines; seat gates CLEAR. |
| `deploy_ledger.py` | `open` 4 legs, `close-leg` V, P, D, Q, `close` | all accepted; sentinel removed. |
| `lib/platinum_dest.py` + `lib/s3_layout.py` + boto3 `list_object_versions` | `e102_legp.py legp` | 122 keys, 122 version pages, 0 absent, 0 without a VersionId. |
| `e102_census.py` | `snap` pre and post, `cmp` | 190 / 190, MOVED = [C_06], ADDED 0, GONE 0. |
| `e102_ssm.py` + SSM `AWS-RunShellScript` | 4 sends: 2 stops, 2 singles | all Success rc 0. |
| `e97_legq_snapshot.py` | `snap` x4 | 29,605 keys, 0 without a VersionId. |
| `e102_branch1.py` | `read` run 1 and run 2 | PARSED-EQUAL, SORTED-BYTES, 0 other ETag differences, determinism True. |
| `e102_shipped_check.py` (issuer's AC1) | before, after ship, after leg Q' | ok=False, ok=True mds_sorted=False, ok=True mds_sorted=True. |
| `proof-of-spec-check.py` | `<instance> SC25-e102b-AC1` | VALID (rc=0). |
| `comp-adversary` | not run | the order's preflight declares it RUN by the issuer; declared as an exclusion. |
| `comp-find` / Bash `grep` over `lib/*.py` | one blind recursive search | DENIED by the rail (F1); used the native Grep on the named file instead. |

## Push state

Committed LOCAL on `box/dell1`; this lane does not push a shared branch. Origin state is stated in the report from an `ls-remote` read
at send time.
