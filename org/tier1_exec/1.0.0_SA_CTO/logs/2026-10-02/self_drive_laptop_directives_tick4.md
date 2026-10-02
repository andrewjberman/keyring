# /self-drive laptop directives -- tick 4 (2026-10-02 06:3xZ-07:4xZ)

Arming record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_050xZ_SELF_DRIVE_60M_LAPTOP_DIRECTIVES_ADJUDICATE_ALL_KEEP_COOS_FLOWING.md`
@d4050ac185. Cron `57facd67`. **state: ARMED**. Previous log: ticks 2-3 @a3a8ed27c9.

```
SELF-DRIVE laptop directives -- tick 4 (07:28Z)   state: ARMED   cadence: 60m   job: 57facd67
SCOPE: 10 directives -> 48 projects   device: laptop   inbox: 0 unread at the tick
OPEN CALLS IN SCOPE: 8 ruled since tick 3 - 0 design forks - 0 governance forks
ACTS ONLY ANDREW CAN DO: 6 (one added: his YCharts sign-in through the CAPTCHA)
COMPLETION TEST: NOT DONE -- 15 of 48 complete or closed; D10 UNMEASURABLE
```

## Calls ruled since tick 3

| # | call (msg) | ruling | record |
|---|---|---|---|
| 1 | `~Y` 104094: hop-3 window -- the upload exhausted on OPERATION_BUSY; leg A evicted, refresh met a CAPTCHA | option (a) with a fresh delayed re-send so SQS's count never reaches the DLQ; busy never `REPLACE_FILE`; read the probe's session rotation before any window; a CAPTCHA sign-in is Andrew's | batch 120 @5ebc8d592f |
| 2 | `~P` 104095: IRPT_DASHBD round 2 B drained, **FWD-1 LIVE end to end** | round-3 analysis: E1 the adapter's schedule, E2 the publisher's 08:15 ET clock, E3 foreign tax internal; margin interest stays internal (Opal is right) | @f5fbeaa543 |
| 3 | `~Y` 104099: st11 needs `sqs:SendMessage` | granted, one action on `irpt-generation` only, applied under st11 | batch 121 @f306b0214a |
| 4 | `~Y` 104102: CTO half on st11 | SIGNED; st11 SERVED 07:18Z (@861b9bf176) | batch 122 @b21553d549 |
| 5 | `~Y` 104105: hop 11, the vendor PDF link | route, answer shape and the `server_only` reading accepted; `vendor_documents` added in `~Y`'s lane; E7 -> E6 memo -> hop 11 queue behind the PROD-parser gate | batch 123 @14a0a78218 |
| 6 | row IRPT_DASHBD-S17 (`~P` @fa2860a1e4): my round-2 analysis wrongly called S16 fixed | MY ERROR: claimed from a citation without running the lint. Fixed at the source: `to-check.py`'s resolver `SERIAL_RE` (the seating check reads through it); analysis corrected | batch 124 @0b8f897e7d |
| 7 | `~Y` 104107: E6's memo needs two lines in `reports/status_installed.py` (`~P`'s lane) | granted to `~Y` on that one file, IRPT_COMPLETION_P members kept | batch 125 @7d40b9bccf |
| 8 | `~P` 104071-era readiness: `~D`'s item 67 gives `unclassified` its own colour | condition 2 of the re-point half met | portal DEV `3ca6c53a` |

## The COO lanes (07:28Z)

| lane | state |
|---|---|
| `2.0.0_SA_COO~M` | BD r3 restore run fired 06:25Z; V1 due by 11:00Z (fallback per-key restore) |
| `2.0.0_SA_COO~Y` | st11 SERVED; building E7 / E6 / hop-11 packets, applying none before the PROD-parser gate |
| `2.0.0_SA_COO~P` | IRPT_DASHBD round 3 issued (@c75ddc5d61), DB-b-7 in progress |
| `2.0.0_SA_COO~D` | DSGN_IRPTV1 items 67-68 on DEV; next 69 |

## Acts only Andrew can do (each with its citation)

1. **Portal PROD promote** -- now gates E7, E6's memo and hop 11 on `irpt-status` (batch 123 item 4), the Cottonwood re-point's served
   legs, `~D`'s items. CLAUDE.md Portal ("DEV only, PROD gated").
2. **His YCharts sign-in through the CAPTCHA** -- the resident cannot sign in; the hop-3 live proof waits on it. Step 1's act list (his login).
3. **The nine-object Inflection delete** -- CLAUDE.md Agent Autonomy (S3 deletes).
4. **The recursive delete of `wk-irpt-dashbd-1`** -- CLAUDE.md Agent Autonomy (recursive deletion).
5. **A Black Diamond pull for like-day tie-out windows** -- CLAUDE.md vendor egress, his per-use word.
6. **The next CLOUD push** -- LD-0367/0368.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| to-check | `--all` before and after the resolver fix | PASS | 236 open, 58 projects, 45 groups, unchanged |
| to-decomp-ref-lint `seating_check` | on TO-DB-b-7, TO-DB-b-9 | PASS | `0.9.0_WK_IRPT_DASHBD~1`, legal target |
| owned-paths-validate | structure + `--check-agent` | PASS | 92 lanes, 414 rules; positive and negative controls |

**Gap found:** a gate's fix in one file (`to-decomp-ref-lint.py`'s `SERIAL_RE`) did not reach the path the gate actually reads
(`to-check.py`'s resolver). The lesson is the act, not a rule: run the gate on the failing input before calling a fix done.

-- 1.0.0_SA_CTO
