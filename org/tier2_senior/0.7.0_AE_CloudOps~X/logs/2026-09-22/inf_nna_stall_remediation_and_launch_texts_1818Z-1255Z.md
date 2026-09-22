# INF gold chain unstalled: NNA guard reads GROSS, 351/1206 excused for 2026-09-04 only, launch texts only on real failure -- 0.7.0_AE_CloudOps~X

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, IMPLEMENT
**Date:** 2026-09-21 18:18Z -> 2026-09-22 12:55Z
**Task Order:** ad-hoc, Andrew-direct in session. Source brief: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/INF_GOLD_CHAIN_NNA_GUARD_STALL_BRIEF_20260921.md`
**Status:** COMPLETE -- accepted on the scheduled 2026-09-22 run
**Workspace CLOUD commits:** `158dbeb7bf` `6c9cd5140d` `458cfbd688` `79cc430cba` `3c80e6e438` `a437fbf699` `75e31a784b` `20142bab18` `cc518ade9e` `4125630e8a` -- all ON ORIGIN (ls-remote read 2026-09-21 20:10Z, origin CLOUD later @d228ce5cb2); tag `inf-pipeline-v1.7.101` on origin.

---

## Objective

The Inflection (INF) full gold chain had hard-failed 16 of 16 days (09-06..09-21) at step 33,
`INF_C_01.canonical_nna`. The NNA coverage guard refused to rewrite the 2026-09-04 partition without
accounts 351 and 1206, so every Inflection file the portal serves was frozen at the 09-05 run. Andrew's
directions, verbatim:
1. "We need to patch the error type that caused the confusion with the NNA."
2. `/open-calls` answered "recs approved for call 1 and 2. FOr 3, need more clarification on what your
   scope/denominator is here. call 4, yes." (record @458cfbd688).
3. Option (b) "(B) is good" (at 0.0.0_AB_MSTR's terminal, record @aaef3179f8, relayed by 1.0.0_SA_CTO
   msg 99186).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript io | `io INF_C_01` | PASS | Named the input set: silver/transactions/ + gap_manifest. That pointed the root-cause read at the daily full-history silver snapshots. |
| comp-pipescript deployed | `deployed --firm inf` | FAIL | Hit its 90 s budget, 0 of 1 s3_head_object, `STATE: NOT-DECIDABLE`. Its truncated first page carried no `lib/` rows. The guard's deployed bytes were compared by direct `s3 cp` + LF-normalised equality instead (26,438 = 26,438). |
| comp-pipescript deployed (inside safe-deploy) | safe-deploy VERIFY | PASS | `VERIFY OK comp-pipescript deployed data/inf/scripts/gold/lib/nna_coverage_guard.py`, twice. |
| comp-routes trace | `trace --json` over 5 ADVI routes | PARTIAL | 2 RESOLVED (`artifacts/timeseries_chart.json` -> gold/artifacts; `advisors/x/mix-views` -> gold/entities, which holds 0 keys in opal-data-inf: the documented fixed-bucket limit, not filed); 1 UNRESOLVED_NO_RULE; 2 returned no parseable JSON. |
| comp-iam | not run | SKIPPED | The new grant is one `lambda:InvokeFunction` on one function ARN, and comp-iam models (action) not (action, resource). The live primitive was used with ONE ARN per call plus a negative control: allowed on the retry function, implicitDeny on another. |

**What worked:** `comp-pipescript io` named the right input in one call. safe-deploy's built-in VERIFY.
**What failed:**
- `comp-pipescript deployed --firm inf` timed out NOT-DECIDABLE.
- safe-deploy SILENTLY DROPPED an explicitly passed `.json`: 2 args, "1 path(s) to deploy ... all 1 file(s) deployed and verified".
**Gap found:**
- No comp-tool answers "what serves this COMPUTED portal route for firm X". The four `partners/books/*`, `mix-views` and `clients-tab` routes stayed unmeasured.
- safe-deploy has no argument-denominator line, so a dropped file reads as success.

---

## Deployment Sequence

### A. NNA guard headline: GROSS, not a netted sum (Andrew-direct ~18:2xZ)

| Step | Action | Result |
|------|--------|--------|
| 1 | Diagnose | `assert_partition_coverage_continuity` headlined `sum(unexcused.values())`, a SIGNED sum. 351 (+120,000) and 1206 (-120,000) netted to "$0.00 of SERVED NNA", confirmed at `chain_full_20260921_113302.log:36700`. |
| 2 | Patch + 4 tests (worktree) | GROSS + signed net + "(partition, account) row(s)" + "THE NET UNDERSTATES IT"; register ALARM same. `158dbeb7bf` |
| 3 | Control | The 4 new tests against the unpatched guard: all 4 FAIL, the first on "'carrying $0.00' unexpectedly found". |
| 4 | Merge | `6c9cd5140d`, first-parent diff = 2 intended paths |
| 5 | Deploy | `safe-deploy` -> `VERIFY OK` (Andrew call 1) |
| 6 | Verify by import from bucket (outside repo) | The incident case prints "$240,000.00 GROSS (signed net $0.00)", and a faithful rewrite passes. |

### B. Root cause of 351/1206 (Andrew call 2) -- fact only

| Step | Action | Result |
|------|--------|--------|
| 1 | Row trace, silver 09-04/-05/-06/-21 | txn 5835499 (351) and 5833840 (1206) persist in every snapshot; ONLY the type changed: Merge In/Out (39/42, NNA) -> Internal Account Journal In/Out (172/171, Internal), editedDate 2026-09-05 20:28. |
| 2 | Real classifier (INF_C_01 `_normalize_silver_schema` + `classify_nna`, `INF_AOR_FOLD_ACTIVE=1`, AoR re-key stubbed as a stated substitution) | The 09-05 snapshot gives 16 rows = served gold. The 09-06 and 09-21 snapshots give 14 rows, with only 351/1206 absent. |
| 3 | Whole-history census | 1,473,605 ids: exactly 2 changed type between 09-05 and 09-21, and both are this pair. |
| 4 | Write-up + route to decider | `79cc430cba` (`deliverables/INF_NNA_351_1206_ROOT_CAUSE_20260921.md`); msg 99175 to 1.0.0_SA_CTO + 0.0.0_AB_MSTR |

### C. EC2 launch texts only on real failure (Andrew call 4), inf-pipeline-v1.7.101

| Step | Action | Result |
|------|--------|--------|
| 1 | Baseline | The deployed `lambda_function.py` of both functions == repo, downloaded and diffed. |
| 2 | Commit source (worktree) | Monitor: hands off to the retry Lambda by async invoke, with SNS publish as the fallback. Retry: start -> wait -> check, stop once running, text on EXHAUSTED or on its own error. TF: `RETRY_FUNCTION_NAME` + `lambda:InvokeFunction`. `3c80e6e438` |
| 3 | Local exercise (stub clients) | Patched 11 of 11 arms PASS. The unpatched control 5 of 11: the 6 failures are exactly the changed behaviours. |
| 4 | Merge | `a437fbf699` |
| 5 | build-and-upload.sh | monitor `RdBNvM6I/9sgEQGenRFaOzJh2fzj6eV+K9AF/s+Eitk=`, retry `ANaVsVVRSA+Cu3GTxowx4AF9gTMexjTJqtT9kNbMhdM=`; write VERIFIED |
| 6 | terraform plan (targeted, .tools/terraform.exe 1.9.8 = state writer) | 0 to add, 3 to change, 0 to destroy |
| 7 | safe-apply of the saved plan | `Apply complete! Resources: 0 added, 3 changed, 0 destroyed.` |
| 8 | 0-diff plan | `No changes. Your infrastructure matches the configuration.` |
| 9 | Deploy ledger | `inf-launch-texts-20260921` CLOSED, 3 of 3 legs |
| 10 | record-terraform-deploy | REFUSED by the naming gate: 61 pre-existing inf-* names in the regenerated CHANGELOG entry. Source map committed alone, CHANGELOG restored. Row `LGIC_ENFORCE-S151` @`4125630e8a`. |
| 11 | Commit + tag | `75e31a784b`, tag `inf-pipeline-v1.7.101` |

### D. Date-scoped excusal (Andrew option (b))

| Step | Action | Result |
|------|--------|--------|
| 1 | Guard | Optional `partitions` list; the match moves from account id to the (partition, account) pair. Without it an entry stays ACCOUNT-WIDE; a malformed scope RAISES. |
| 2 | Manifest | 351 and 1206 get `"partitions": ["2026-09-04"]`, with the vendor reclassification quoted. |
| 3 | Tests + control | 46 of 46 pass. The 4 new tests on the previous guard: 3 FAIL, and 1 PASS (the back-compat arm, correct on both). |
| 4 | Real-data arm | Served gold 09-04 vs the classifier on the 09-21 silver: "OK ... (2 excused by review)" with the manifest, RAISES $240,000.00 GROSS without it. |
| 5 | Commit + merge | `20142bab18`, `cc518ade9e` (lane POD4 override, audited) |
| 6 | Deploy | Guard via safe-deploy `VERIFY OK`. Manifest via direct `s3 cp` of the committed bytes, because safe-deploy dropped the `.json`: read-back sha256 == committed (`6fdf008c749170cb`), 0 CR bytes. |
| 7 | Verify from bucket | The deployed guard + manifest excuse (351, 09-04) and (1206, 09-04). 351 dropped from 09-15 still RAISES. |

## Verification (the scheduled run, 2026-09-22)

```
run_id chain_full_20260922_113345   started 2026-09-22T11:33:45Z
status complete | step 65 of 65 | done 65 | not-ok [] | errors []
INF_C_01 ok (202 s) at ~12:40Z
gold/meta/pipeline-complete.json: Tue, 22 Sep 2026 12:51:20 GMT   (previous 2026-09-05)
gold/meta/pipeline-failed.json:   Mon, 21 Sep 2026 12:35:38 GMT   (no new failure)

chain_full_20260922_113301.log:
  NNA COVERAGE: account 351 ($120,000.00, ['2026-09-04']) is EXCUSED [partitions ['2026-09-04']] -- Vendor RECLASSIFICATION ...
  NNA COVERAGE: account 1206 ($-120,000.00, ['2026-09-04']) is EXCUSED [partitions ['2026-09-04']] -- Vendor RECLASSIFICATION ...
  OK: NNA partition coverage -- 1,437 partition(s) being written, no account dropped from any of them (2 excused by review).

platinum/firm/header_metrics.json: generated_at 2026-09-22T12:47:53Z | data_as_of 2026-09-21
  (lib/trading_calendar prev_trading_day(2026-09-22) = 2026-09-21)
platinum/firm top-level files: 32 | written today after 12:00Z: 29
inf-portal-publisher first event 12:51:21Z; inf-portal-advisor-publisher "COMPLETE: 5 published, 0 errors" 12:52:01Z
alarm inf-gold-chain-failed: OK (last state change = the 09-21 recovery; no ALARM today)

Launch texts, live (call 4):
  11:15:22Z inf-bronze-runner stopped; reason='Server.InternalError' -> Handed launch failure to inf-ec2-retry-launch (no text)
  11:15:55Z Instance i-083ad9ae297f88e9f recovered on attempt 1/3 (state=running) -- no further attempts
  11:32:40Z inf-gold-layer-runner stopped; reason='Server.InternalError' -> Handed ... (no text)
  11:33:13Z Instance i-0ed5afded2ebd4ed4 recovered on attempt 1/3 (state=running) -- no further attempts
  SNS NumberOfMessagesPublished, inf-otp-alert, last 3h: 0 datapoints   (control, 09-21 11:00-13:00Z: 2)
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Read "the error type" as the netted $0.00 headline | It was the confusing element, confirmed verbatim at the live log. The patch is message-only, so every verdict is unchanged. |
| REC option (b), date-scoped, over (a), account-wide (Andrew ruled (b)) | 351 is a LIVE ~$929k account. An account-wide excusal would strip the guard from every partition forever, for one reclassified date. |
| A malformed `partitions` scope RAISES | A scope that silently widens to account-wide is the exact over-grant (b) exists to prevent. |
| Monitor -> retry by direct invoke, with the SNS subscription kept | A failed hand-off falls back to the old path (text + retry), so the change can degrade only to old behaviour, never to silence. |
| Retry texts on its own error (RETRY-LAMBDA-ERROR) | Once it is the only launch-failure texter, its own failure must text. |
| CHANGELOG.json not committed | The tool's regenerated entry recorded other seats' deploys under this version, and the gate refused it. Filed as S151 rather than overridden. |
| The ad-hoc QA run was not fired | It would move served output. It was asked of Andrew, and the scheduled run arrived first as the acceptance. |
| Route-model gap not filed | It is the documented `comp-routes` fixed-bucket limit, not a new defect. |

---

## Files Modified

See commit messages: `158dbeb7bf`, `458cfbd688`, `79cc430cba`, `3c80e6e438`, `75e31a784b`, `20142bab18`, `4125630e8a`. Rows needing context:

| File | Change | Committed |
|------|--------|-----------|
| `data/inf/scripts/gold/lib/nna_coverage_guard.py` | GROSS headline (`_stake`, `_understated`, `_offset_note`); date-scoped excusal (`_is_excused`, `partitions` validation) | Yes -- `158dbeb7bf`, `20142bab18` |
| `data/inf/scripts/gold/lib/nna_coverage_excusals.json` | +351, +1206 with `partitions: ["2026-09-04"]` | Yes -- `20142bab18`; deployed by direct cp |
| `infra/aws/lambda/inf-pipeline/inf-ec2-{launch-monitor,retry-launch}/lambda_function.py` + 2 `.tf` | hand-off / stop-once-running / error text | Yes -- `3c80e6e438` |
| `infra/aws/terraform/inf-pipeline/CHANGELOG.json` | NOT modified: the regenerated entry was refused and restored to HEAD; the generated copy is in this seat's scratchpad | No -- row S151 |

---

## Blockers

None. The acceptance criteria were all met on the scheduled run.

---

## Current State

- **The chain.** INF's full gold chain on `inf-gold-layer-runner` (i-0ed5afded2ebd4ed4) completed 65 of 65 on 2026-09-22. `s3://opal-data-inf/gold/meta/pipeline-complete.json` is dated 12:51:20Z and the served `platinum/firm/header_metrics.json` has `data_as_of 2026-09-21`, so the 16-day freeze is over.
- **The guard.** `data/inf/scripts/gold/lib/nna_coverage_guard.py` headlines GROSS with the signed net beside it. It supports `partitions`-scoped excusals, matched on the (partition, account) pair. Accounts 351 and 1206 are excused for 2026-09-04 ONLY, and both stay guarded on every other date. Repo @`cc518ade9e` == `s3://opal-data-inf/code/gold/lib/{nna_coverage_guard.py,nna_coverage_excusals.json}`.
- **The launch texts.** `inf-ec2-launch-monitor` now hands launch failures to `inf-ec2-retry-launch` with no text. The retry stops once the instance is running and texts only on exhaustion or its own error. Proven live on two real bounces this morning, with 0 SNS publishes (inf-pipeline-v1.7.101).
- **Standing, not new.** The guard's non-raising AT-RISK register now reads "17 account(s) holding $632,611.72 GROSS (signed net $441,576.22)". This is the July exposure, and it closes only when attribution stops being re-derived from the current-state vendor roster.

---

## Next Steps

1. **[Andrew] Call 3 (which Inflection ADVI value moves daily).** Now moot, since served data refreshes again. Measured denominator on the record: platinum/ 8,682 keys, of which 2,310 are `_meta` writes and the rest are frozen at 09-05. Four computed routes remain unmeasured. Trace only if wanted.
2. **[0.7.0_AE_CloudOps] safe-deploy silently drops an explicitly passed non-.py file.** 2 args gave "all 1 file(s) deployed". It is this lane's own tool (ADHC_DSFLOW.005). The fix is to print an argument denominator and refuse or SKIP-log the unmapped args. Awaiting Andrew's word.
3. **[1.0.0_SA_CTO] Row LGIC_ENFORCE-S151.** record-terraform-deploy's CHANGELOG step is refused by the naming gate on pre-existing names, so every inf-pipeline deploy's CHANGELOG stays unrecorded. The remedy belongs to the gate owner and the tool owner.
4. **[0.4.0_DS_ClientPlatform] FYI.** This seat edited POD4 files (guard, manifest, tests) under audited `GIT_COMMIT_AUTHOR_OVERRIDE=POD4` on Andrew's word. The excusal schema now has `partitions`, so any future excusal for a LIVE account should use it.
5. **[2.0.0_SA_COO~X] Stale TO.** `NFRA_SUBSTRATECARDING.TO-CARD-R-W4-COX`, issued 2026-08-30 to this lane, is still `pending` and was not touched this session (ad-hoc Andrew work took precedence).
