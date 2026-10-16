# NEVER-WIDEN -- COO half -- ADVI_FIRMBKTS Door 6, order FB-p-2: the feeder's second look (13:08Z) and the catch-up

**Signer:** `2.0.0_SA_COO~B1` (dell1) | **State: DRAFT for the CTO's read** (2026-10-16 ~19:2xZ; becomes GIVEN when this seat stamps it after his read). **Counterpart:** `1.0.0_SA_CTO~DELL1` (owed; not in force until his half is signed against this file's bytes). **Order named:** `ADVI_FIRMBKTS.TO-FB-p-2.door6-retirement` (WORLD, staged). **Applier:** the one dell1 ADVI CloudOps lane (rule 34), named by `0.0.0_AB_MSTR~DELL1`. **Ruling it executes:** CTO msgs 6978, 6980, 6983 and `ledger/CTO_DECISION_DOOR6_RETIREMENT_ORDER_20261016.md`. **Timing (CTO 6983):** neither act lands before D1 reports its read of the 2026-10-17 13:30Z fire (about 14:30Z); the schedule's first live day is Monday 2026-10-19.

Reads behind this half: `ledger/DOOR6_STEP2_READS_20261016.md` (sections 1 to 5). All reads below are live, read-only, 2026-10-16 ~19:0xZ to 19:2xZ.

## 1. What is stale, since when (read)

| object | newest write read | note |
|---|---|---|
| `opal-data-mdpf` `mdpf/feeds/model_aua_positions/inflection`, `model_composition/inflection`, `non_model_aua/inflection` | partition `2026-10-12`, written 12:52:59Z | 105 objects in each of the first two families, 506 in the third; nothing newer |
| `mdpf/feeds/etf_net_assets` | partition `2026-10-12`, 12:52:58Z | 267 objects |
| `mdpf/feeds/non_model_aua/49financial` | partition `2026-10-12`, 12:54:12Z | 100 objects |
| `mdpf/feeds/model_aua_positions/49financial`, `model_composition/49financial`, `partner_held_etf/49financial` | partition `2026-10-16`, written 03:30Z to 03:31Z | CURRENT. Written by a process this seat did not read (not the 12:52Z dispatch on the days it did not run) |
| `opal-data-assets` `gold/mdpf_revamp/_aggregate_aua/` (the served aggregate) | `2026-10-12.json`, 17:32:45Z | 493 objects; no partition for 2026-10-13, 10-14, 10-15, 10-16; a skip is logged for 10-06, 10-07, 10-08 and 10-10 as well |

Denominators: the feeds listing returned 1,635 objects (162 pagination-marker lines excluded); the aggregate listing 493 objects. The cause, read in `mdpf-gold-lambda`'s log: on 10-13, 10-14, 10-15 and 10-16 at 13:31Z `non_model=0.00 partners=1 reconciliation=ERROR`, then `A7 reconciliation ERROR -- partition write SKIPPED (drop-rather-than-fabricate); prior emit stays authoritative` (8 such lines since 10-05: 10-06, 10-07, 10-08, 10-10, 10-13, 10-14, 10-15, 10-16). So the served figure has not advanced since 10-12 and the guard has refused to publish a wrong one.

**Not read:** what the portal shows for the gap (`opal-assets-mdpf-portal-publisher`, scheduled 13:50Z, reads the aggregate); whether any other path writes the Inflection or 49 Financial non-model feeds.

## 2. Does the 13:30Z fire consume the feeder? Yes (read)

`mdpf-scheduled-floor` (`cron(30 13 * * ? *)`) invokes `mdpf-gold-lambda`, which runs `mdpf_aggregate_aua.py` with `FEEDER_PREFIX = "mdpf/feeds"` and `FEEDER_BUCKET = "opal-data-mdpf"` (lines 65 and 66) and writes `s3://opal-data-assets/gold/mdpf_revamp/_aggregate_aua/<date>.json`. The 10-12 run (feeds present from the 12:52Z dispatch) wrote it at 13:31:38Z with `non_model=299,469,660.46` and passed; the 10-13 to 10-16 runs (feeds absent for the date) refused. The log also shows a second 10-12 run at 17:32Z that rewrote the same key (someone re-ran the floor by hand; who is not read).

## 3. The two acts and their blast radius

**Act A (Terraform, root `infra/aws/terraform/mdpf-pipeline`, file `feeder-trigger.tf`):** ONE added resource, an `aws_scheduler_schedule` on the default group with `schedule_expression = "cron(8 13 * * ? *)"`, UTC, flexible window OFF, the SAME target block as `mdpf_feeder_backstop` (`module.mdpf_feeder_trigger.function_arn`, role `mdpf_feeder_scheduler`, DLQ `mdpf_trigger_dlq`), no static input. Its name comes from the naming builder or the gate refuses it (CLAUDE.md rule 30); the applier adds the registry row if refused. Expected plan: `add=1 change=0 destroy=0`; the applier STOPS on any other count. It touches no data. Its first live day is Monday 2026-10-19; it also fires on Saturdays and Sundays, as the 12:52Z backstop does (the backstop dispatched on Sunday 10-11).

**Act B (the catch-up).** Two branches, and only the first is covered by this half:

- **B1, the current date only (covered).** After D1's read of the 10-17 fire, invoke `mdpf-feeder-trigger` once with the default date (today UTC) and read the SSM command to `Success`; then re-run the floor lambda for that same date. Writes: new feeds partitions dated that day in the five stale families, and one new key `gold/mdpf_revamp/_aggregate_aua/<that date>.json`. Equal bytes: the dispatch reads the LATEST Inflection gold partition and the LATEST Schwab rps partition for the date (see 4), so for the date on which that vintage is current it writes what the organic fire would have written, if the inputs are unchanged between the two. That equality was NOT tested (a test is a dispatch).
- **B2, per-date catch-up for 2026-10-13 to 10-16 (NOT covered; needs the CTO's fork).** Re-dispatching `--date 2026-10-13` today does not rebuild 10-13. Read: the trigger passes only `--date` (`mdpf-daily-dispatch.sh:346`, `run_step WS-C ... --date "$RUN_DATE" --upload`); `build_mdpf_wsc_inflection_feeder.py` calls `latest_inf_eclipse_dates(args.eclipse_date)` (line 544; the function is at line 161) with `--eclipse-date` (line 500) defaulting to the latest gold partition with a sentinel; `build_mdpf_wse_49f_non_model_aua.py` takes `rps_date = args.rps_date or _latest_rps_partition()` (line 807). The dispatch script has no `--eclipse-date` or `--rps-date` passthrough (searched: 0 hits). So a dated re-dispatch writes the LATEST vintage under the OLD date's name: the T-1-wearing-T-0 defect that the trigger's own docstring names, and the floor, finding non-zero non_model for that date, would then PASS A7 and publish a figure dated 10-13 holding 10-17's inputs. That is worse than the gap the guard is holding. **Recommendation: do not run B2 by re-dispatch.** The honest options: (i) leave 10-13 to 10-16 as a documented gap (the guard's own outcome, "prior emit stays authoritative"); (ii) add `eclipse_date` and `rps_date` event passthrough to the trigger and the dispatch (a code change and deploy, its own order); (iii) run the two feeder scripts by hand on the runner with explicit vintages (hand-picked steps, which `mdpf-feeder-trigger`'s comment calls the swallow-fix class). The gold partitions for 10-13 to 10-15 exist (their `_meta/gold_complete.json` objects were read present on all three days); whether the rps partitions do was not read.

## 4. Both branches of each act's outcome (read from the producers' own rules)

- **A, applied:** a second invocation at 13:08Z. If the Inflection gate `gold/eclipse/<date>/_meta/gold_complete.json` is present, the trigger starts the runner and dispatches (the chain took 1m51s to 1m56s in 7 histories, so it ends about 13:10Z, 20 minutes before the 13:30Z floor); if absent, it returns NOT-YET and nothing is written. On a day the 12:52Z backstop already dispatched (3 of the last 10), the 13:08Z fire dispatches again: the code has no already-done check (`lambda_function.py` lines 155 to 209) and its comment calls the re-run an idempotent overwrite. Same-date same-input overwrite with equal bytes is the code's claim, not read as bytes. What differs when the input moved between 12:52Z and 13:08Z: the second write carries the newer input; that is the intended result.
- **B1:** if the floor re-run finds non_model non-zero and reconciliation clean, it writes one new aggregate partition; if A7 still errors, it writes nothing and the figure stays at 10-12. Either way no existing key is overwritten (all five feed families and the aggregate key for that date are new).
- **The 49 Financial feeds written at 03:3xZ:** a dispatch with the 49F branch enabled runs WS-B and WS-D.2, which write `model_aua_positions/49financial` and `partner_held_etf/49financial`. If the 03:3xZ writer is the same code, the dispatch overwrites same-date keys with bytes this seat has not compared. The applier reads the writer of those two families (one `comp-find` on the key prefix, denominator printed) BEFORE B1 and STOPS if a same-date key exists and the writers differ.

## 5. Rollback per key

- **Act A:** remove the added resource and `safe-apply` (expected `destroy=1`), or `scheduler update-schedule` to `DISABLED` and reconcile. Nothing else to undo; no data written.
- **B1 new keys (the five feeds partitions for the date and the aggregate partition):** all are NEW keys in versioned buckets (`opal-data-mdpf`: Enabled; `opal-data-assets`: Enabled). Rollback is a delete marker on each, which is an S3 delete and waits on Andrew's word.
- **Any same-date key B1 overwrites (section 4, the 49F families):** copy the prior VersionId back as current (`s3api copy-object --copy-source <bucket>/<key>?versionId=<prior>`); the applier records every prior VersionId before the dispatch and prints the list.
- **The served aggregate for 2026-10-12 and earlier:** untouched by A and B1.

## 6. Conditions

- The CTO half is signed against this file's sha256 (printed in my message), the section-1 reads and the section-3 plan count. An unmeasured change to any of them voids this half.
- The close is two reads by the COO and the CVO, never the applier's word: (a) for A, the schedule's first fire on 2026-10-19 12:52Z/13:08Z reads in the trigger's log as one dispatch or NOT-YET-then-dispatch, and `mdpf feeder chain` appears in the runner's SSM list; (b) for B1, the new aggregate partition exists or the A7 refusal is logged, and the five feeds partitions carry the date.
- Neither act lands before D1's read of the 2026-10-17 13:30Z fire (CTO 6983: one change per fire).
- Ledger entry opened at the start and closed at completion (NEVER-2). Nothing about a client account, advisor or dollar value is written to a record, a message or a commit beyond the aggregate totals already in the floor's log.
- The accelerator rule and the marker write are NOT part of this half; they stay in FB-p-2 steps 2 and 3 under the CTO's decision text.
