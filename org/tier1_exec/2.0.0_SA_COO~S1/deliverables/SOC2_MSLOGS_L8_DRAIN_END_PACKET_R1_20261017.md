# SOC2_MSLOGS round 1 -- drain-end packet (L8 input), issuer 2.0.0_SA_COO~S1, 2026-10-17

**Round:** 1, the FWD-1 thread (CTO scope msg 6869) over PRD v0.2 @5df576eada. **Decomposition:** `org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP.md` (L5 @087d4d5b24; issuance @09a7732aab).
**Release ledger:** `org/critical_paths/change_management/20261016T1804Z_soc2-mslogs-r1-raw-switch-20261016_deploy_completion.md`, CLOSED by 0.7.0_AE_CloudOps~SOC21 (10 legs, close commit 9ad6102a36).

## 1. The orders and their merges

| order | cell | worker / seat | merges on box/dell1 | criteria |
|---|---|---|---|---|
| TO-SM-s1 | SM-s-1 silver + timeline reader | ~3 | 56af05ace6 | AC1-AC2 PASS |
| TO-SM-x1 | SM-x-1 scrub | ~5 | 5660aeb021 | AC1 PASS |
| TO-SM-c1 | SM-c-1 collector to raw | ~1, then ~6 (AMENDMENT 2), then ~7 (AMENDMENT 3) | b2fef4b9b5, 6cef75fd39, 3b35dca82a | AC1-AC6 PASS |
| TO-SM-g1 | SM-g-1 registry home | ~4 | ddccf1e8f1 | AC1-AC2 PASS (AC1 later reads stale stamps after another seat's registry change; see 4.4) |
| TO-SM-a1 | SM-a-1 door | ~2 (+ write-once fix), then ~8 (AMENDMENT 2, detail) | 36f107cee9, c332e46ace | AC1-AC4 PASS |
| TO-SM-r1 | SM-r-1 release | 0.7.0_AE_CloudOps~SOC21 | (live account) | AC1-AC4 PASS, AC5 judgment (CVO) |

Drain checks on the merged tree (issuer, 2026-10-17 ~02:3xZ): c1 raw/switch/recollect/derive_time/derive_par/derive_client, a1 ops/bronze/detail/tf, s1 silver/timeline, g1 ledger, x1 scrub all OK; `thread_trace_r1.py` THREAD-R1-OK; 255 + 217 tests pass; ruff clean; terraform fmt -check rc 0, validate Success (scratch copy of the root).

## 2. The ONE REAL RUN (the issuer's own read of the live outcome, 2026-10-17 ~02:4xZ)

- `s1_check_r1.py applied` -> R1-APPLIED-OK; `subs` -> R1-SUBS-OK Audit.AzureActiveDirectory,Audit.Exchange,Audit.General,Audit.SharePoint; `switch <switch_at.txt = 2026-10-17T01:31:22Z>` -> R1-SWITCH-OK audit_records=9534 dates=8 silver_dates=9 (issuer re-ran all three; the seat ran plan -> R1-PLAN-OK exit 0).
- Live config read: door `globgrph-trino-access-lambda:member` version 5, 10240 MB, 600 s, code of c332e46ace (timeline detail).
- Silver (all accounts, raw-era): Eastern 2026-10-09 to 2026-10-16, 4 to 35 MB per day, rebuilt 01:32-01:38Z.
- **FWD-1 (AC5, judgment, the CVO's):** Andrew read his own account's week through the door from CloudShell (~02:1xZ, relayed by the laptop CTO msg 109788): it worked and was cut at 5,000 rows with six columns that could not say who acted. That read caused AMENDMENT 2 of the door (detail=true: every record whole). The enriched CloudShell block was delivered to him by Taildrop at 02:37Z (sha256 match confirmed by the laptop, MSTR msg 7171). His enriched read is the artifact the CVO grades.

## 3. What the live release found, and what was done (issuer defects first)

1. **Issuer defect -- a Terraform cell without `terraform validate`.** The door cell's access.tf referenced the collector function while collector.tf references the door alias: a dependency cycle; the text-only `a1 tf` check passed. Fixed in the release order (item 3a, the CloudOps seat); `a1 tf` now refuses the reference. Lesson for later rounds: a Terraform-touching cell carries `terraform validate` on a scratch copy of the root as a criterion.
2. **Collector derive starved and killed by the Lambda limit.** Cold-start fetch spent the whole budget; derive got 45 s; the fire was killed mid-derive (Status: timeout); derive ran oldest day first; the cursor was written after derive. Fixed: TO-SM-c1 AMENDMENT 2 (reserved derive share, start guard, newest first, cursor before derive).
3. **Door out of memory on busy raw days** (Runtime.OutOfMemory at 1024 MB). Raised to 6144 MB, then to 10240 MB on Andrew-direct ~00:55Z ("use the biggest lambad memory possible should be 10gb or so"; record `org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261017_0055Z_USE_THE_BIGGEST_LAMBDA_MEMORY_10GB.md`).
4. **The collector's default boto3 client re-invoked a slow derive five times** (60 s read timeout, 5 attempts): fires still ran past 900 s. Fixed: TO-SM-c1 AMENDMENT 3 (a derive client with a 200 s read timeout and max_attempts 1; owed days derived concurrently).
5. **Boundary ruling (09007b948b):** `switch_at.txt` is the start of the first invocation of the repaired code, not the apply time, because an old-code invocation that began before an apply can run on past it. The criterion was not changed.
6. **Issuer measurement error:** the first 7-day blob estimate (about 1,136) listed without paging; the real backlog was about 9,500 objects. The switch threshold (800 objects) was unaffected.
7. **Seat outage:** 0.7.0_AE_CloudOps~SOC21 ended between 20:50Z and 21:27Z with eight other seats (cause unmeasured, MSTR msg 7028); respawned 23:06Z.

## 4. Surprise rows (15 in `surprise-channel/investigations/INVESTIGATION_v1.md`) -- the issuer's proposed dispositions for the CVO

| row | class / hazard | proposed disposition | evidence |
|---|---|---|---|
| D1-W1-S2 | BLOCKING / ARMED | DISMISSED_WITH_REASON: `first_content.py` was deleted by SM-s-1 (56af05ace6); nothing reads `dropped_id_only` | merge 56af05ace6 |
| D1-W2-S1 | OBSERVATION / ARMED | DISMISSED_WITH_REASON: the columns exist in the merged silver builder (SM-s-1) | live silver read by the door since 01:3xZ |
| D1-W2-S2 | OBSERVATION / ARMED | GRADUATED: fixed (only a not-found head is absent; others fail closed), check arm added | e601e64560, d2074c2058 |
| D1-W2-S3 | OBSERVATION / ARMED | carried to round 2: the door's bronze prefixes as `lib/opal_naming` output (a WARN today) | handler.py hand-typed prefixes |
| D1-W2-S4 | BLOCKING / ARMED | GRADUATED: the order was re-opened on the worker's branch (f3da4710d8); the lane gate admitted the fix | b4f2f10bbb |
| D1-S1 (seat) | BLOCKING / INERT | GRADUATED: cycle fixed (item 3a, ade21bee08) | release plan 0 add / 15 change |
| D1-W1-S1, D1-W5-S1, D1-W7-S1 | OBSERVATION / INERT | carried to round 2: README / RUNBOOK / main.tf comments still name eight accounts, filter.py and an unsubscribed sign-in feed | text only |
| D1-W1-S3, D1-W5-S2 | OBSERVATION / INERT | DISMISSED_WITH_REASON: the empty channel file was refused at issuance (gate needs one row), so the first worker created it | issuance notes |
| D1-W1-S4, D1-W1-S5 | OBSERVATION / INERT | DISMISSED_WITH_REASON: both readings match the contract (last_end held at the oldest failure; empty means nothing listed) | TO-SM-c1 contract |
| D1-W4-S1, D1-W4-S2 | OBSERVATION / INERT | DISMISSED_WITH_REASON: a citation time (~15:5xZ vs ~16:1xZ) and sparse-worktree absence of records; the ledger row cites the record path | X18 row |

## 5. Enrichment candidates for the CTO's round-1 analysis (not cut; the CTO orders round 2)

1. The read client's Desktop option (CTO-carried: `org/missions/D12/SOC2/SOC2_MSLOGS/ledger/CTO_CARRIED_ROUND2_DESKTOP_PRINTOUT_20261016.md`) -- and the paging, detail-aware reader moved from the CloudShell block into `read_timeline.py`.
2. Silver's `client_ip` must also read Exchange's `ClientIPAddress` (blank on 4,307 of 5,000 rows of Andrew's first read); a re-derive of the 8 days follows.
3. A memory-bounded (streaming) derive in the door, so a busy day never needs 10 GB.
4. The collector's async retry policy (EventBridge invoke retried a timed-out fire twice on old code): `maximum_retry_attempts = 0` on the collector's async config.
5. The door's bronze prefixes from `lib/opal_naming` (row D1-W2-S3).
6. Text: README, RUNBOOK, main.tf comments (rows W1-S1, W5-S1, W7-S1).
7. Member-run helpers committed as stopgaps (`org/tier1_exec/2.0.0_SA_COO~S1/deliverables/derive_days.py`, `read_timeline_to_desktop.ps1`): retire or fold into the read client.
8. This machine's default AWS profile is the agent user; a member's CLI read on dell1 needs Andrew_Berman's own named profile (CloudShell avoids it).

Push state of this packet and the merges: LOCAL on box/dell1 at the time of writing; box-sync carries it.
