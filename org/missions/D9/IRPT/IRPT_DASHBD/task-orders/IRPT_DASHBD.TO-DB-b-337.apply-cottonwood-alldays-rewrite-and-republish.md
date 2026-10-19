# TO IRPT_DASHBD.TO-DB-b-337 -- APPLY the signed all-days Cottonwood rewrite pair (packet sha256 `1439a74f`): every landed gold day from 2026-07-10 rewritten with the corrected reader through the function's own rewrite event (a one-day scaling dry run first, events of landed trading days) and the series republished ONCE: gates and live reads, ledger, scaling run, dry runs, rewrites, the pre-write read, the dry build, ONE canary, the full republish, the after-read (CTO GO msg 11048) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-337</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>ALLDAYS</workstream>

**STAGED. NO ACT before the issuer's GO amendment below this line is committed and its GO message reaches you.** The GO comes only after (1) the corrected reader's first scheduled fire (Tuesday 2026-10-20 12:15Z) has been read clean by `~F2` and by the issuer, (2) the COO half reads SIGNED at the packet's sha256, (3) the CTO half reads SIGNED at it, and (4) the Inflection pair (`TO-DB-f-2702`) has finished. If the 12:15Z fire does not read clean, nothing moves and the issuer reports to the CTO.

<go_amendment>NONE YET.</go_amendment>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's GO (msg 11048, pause DONE @09748b7ca7) and the pair: COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_COTTONWOOD_ALLDAYS_REWRITE_AND_REPUBLISH_COO_HALF.md`, CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_ALLDAYS_REWRITE_AND_REPUBLISH_CTO_HALF.md`, both bound to the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_COTTONWOOD_ALLDAYS_REWRITE_AND_REPUBLISH.md` (sha256 `1439a74f417e3de33fa5a7e4f909c8fd4a8dc44a6cc5b800e7815d47605e338e`) | **Decomp cell:** `DB-b-337` (decomposition section 198).

**Risk class WORLD, served output:** every landed gold day from the claim floor is rewritten (a new version each; the previous version kept) and the Cottonwood series are republished (new versions at the same keys). No code, role, schedule or other gold day changes. The days with no landed gold day (2026-08-19, 2026-09-24, 2026-09-25) are NOT touched. **The client-facing change:** the daily returns AND the daily flow entries of the Cottonwood series change on every day that had an external flow (the flows stop being summed across overlapping transaction partitions); four days gain rows; the four days after the re-landed days become measured.

**The days.** The landed gold days from 2026-07-10 as you read them at step 2 (66 at the 2026-10-17 census, plus any landed since: 2026-10-16 landed 2026-10-19T12:16Z and later days by the scheduled fire). The issuer's committed read of what each day should hold: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/RD_COT_ALLDAYS_DRY_20261017.json` (rows per day, old and new; the five days whose rows differ are 2026-07-22, 07-27, 07-29, 08-03 and 10-15).

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying the packet, both halves, the checker and the read tools); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No account id, name or response body appears in any file, commit message, row, log line or message you send: an account is named only by the first 12 hex of the sha256 of its id. Counts, statuses and words only.

**Read first (all in your worktree):** the packet (whole) and both halves; `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (`lambda_handler`, `_rewrite`, `_run`, `settle_days`); `infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py` (the republish events); the read tools `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/cot_publish_offline_diff.py`, `.../reads/cot_alldays_state_read.py` and `.../reads/cot_alldays_dry_read.py`; the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p201_cot_alldays_apply.py` (the record's exact keys: read it first and build the record to it). **Lessons applied here:** every invoke uses `--cli-read-timeout 0 --invocation-type RequestResponse --log-type Tail`; a lost client response is judged from the Lambda log, never retried blind; **no act between 11:30Z and 14:15Z on a weekday; never alongside another IB2 act (the Inflection pair finishes first)**; the sequence is the packet's and a STOP line stops the pair.

**Do, in this order. Record every value named in `COT_ALLDAYS_APPLY_RECORD.json` as you go; a per-day value is an object keyed by the ISO date over `days`.**

0. **Gates, read only.** (a) The packet's sha256 equals the one above; both halves read SIGNED at it (`gates.packet_sha256`, `gates.coo_half_signed`, `gates.cto_half_signed`). (b) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (print the denominator) has an OPEN LEG on `irpt-cot-account-return-daily-lambda`, `irpt-cot-reporting-publish-lambda`, the gold prefix `irpt/cottonwood/gold/account_return_daily/` or the published prefix `irpt/cottonwood/platinum/reporting/` (`gates.one_change_at_a_time`: `worktrees_read`, `open_markers_naming_this_surface` = 0); `~F2`'s ledger `irpt-dashbd-cottonwood-transaction-wiring-20261017` reads CLOSED (`gates.transaction_pair_ledger_closed` true). (c) The live state equals the packet's section 2: the gold function's CodeSha256 `pa5JdBfOL2GUA6b/UU5sp9upDcj0JGjCQ4+xCOass9g=` (`gates.live_matches_packet`). Any mismatch: STOP.
1. **Open the NEVER-2 ledger BEFORE any write:** `python .tools/deploy_ledger.py open ...`, slug `irpt-dashbd-cottonwood-alldays-rewrite-<YYYYMMDD of the day you open it>`, **naming yourself (`0.7.0_AE_CloudOps~IB2`) as the applier**; legs: L1 before reads; L2 scaling and dry runs; L3 rewrites; L4 pre-write diff; L5 canary; L6 full republish; L7 receipt. Commit its `.open_deploys` sentinel at once. Record `ledger_entry`.
2. **Before reads.** `days` = every landed gold day on or after 2026-07-10, ascending (read the gold prefix listing, every page, denominator printed; never list 2026-08-19, 2026-09-24 or 2026-09-25). `before` {`day_rows` (rows of each day's gold object), `day_versions` (each day's VersionId count), `not_measurable` (per day: rows whose `day_quality` is NOT_MEASURABLE), `abs_flow_cents` (per day: `int(round(sum(abs(v) for v in external_flow if v) * 100))` over the day's rows, so the checker's own recount equals yours), `gold_total_rows` (rows summed over every parquet object of the gold table, client-side, every page), `partitions` (the count of `date=` partitions), `series_prefixes` (939), `series_objects` and `series_versions` (every object and every version under the published prefix), `gold_code_sha256` (the live value read now), `publish_code_sha256` (expected `vYNB1EBTU2qEIINxTnhYQBBBEHBYFId7lllrIJM3YRE=`), `schedules` ({`account_return_daily`: ENABLED, `publish_daily`: DISABLED})}.
3. **The scaling run, then the events.** ONE synchronous `{"rewrite": {"start": "2026-07-24", "end": "2026-07-24"}, "dry_run": true}`; record `scaling` {`day`, `duration_s`, `max_memory_mb` from the REPORT line}. **STOP** if its duration is above 720 s or its Max Memory Used above 819 MB. Then cut `days` into EVENTS: maximal runs of consecutive trading days that are all landed (an event never spans an unlanded day), each at most 25 days and with `scaling.duration_s` times its day count at most 500 s; record `events` [{`first`, `last`, `days` (the list)}] in ascending order, partitioning `days`.
4. **The dry runs.** One synchronous `{"rewrite": {"start": "<first>", "end": "<last>"}, "dry_run": true}` per event, ascending. Record `dry_run` {`ok` (every event returned ok), `events` ([{`first`, `last`, `days`, `held`, `duration_s`, `max_memory_mb`}] one per event, from each response and REPORT line), `rows` (per day, from the responses), `gold_objects_before`, `gold_objects_after`, `gold_versions_before`, `gold_versions_after` (counts over the whole gold prefix read before the first and after the last event: EQUAL)}. **STOP** on any `held` above 0, a day's rows more than 2 percent from the issuer's read file (a day beyond that file: rows outside 840 to 1000), an exception, a timeout, Max Memory Used above 819 MB or a duration above 720 s.
5. **The rewrites.** The same events WITHOUT `dry_run`, ascending. Record `rewrite` {`events` (the same shape as the dry run's, from these runs), `rows` (per day, equal to the dry run's), `day_versions_after` (per day, before + 1), `prior_versions_kept` (each day's previous version still readable by its VersionId), `other_partitions_unchanged` (every other partition's object and version counts equal to step 2), `not_measurable_after` (per day), `abs_flow_after_cents` (per day, the same expression as step 2)}. **STOP before any republish** if any day OTHER THAN 2026-07-10 holds more than 15 percent NOT_MEASURABLE rows (the floor day has no previous day and stays NOT_MEASURABLE), if a day whose rows did not change (every day except the five named above) shows a HIGHER `abs_flow_after_cents` than before, or if any other partition moved.
6. **The pre-write read.** Run `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/cot_publish_offline_diff.py` from the worktree root (read only). Record `prewrite` {`accounts_gaining_by_day` (per changed-row day, 2026-07-22, 07-27, 07-29, 08-03 and 10-15: the series that would gain it; each at least 1), `other_field_changes_on_common_days` (the tool's by-field count of series with a changed value on a day present in BOTH versions, summed over every field OTHER than `total_return_daily`, `external_flow`, `day_quality` and `return_basis`: `value`, `income`, `holdings_price_return`; expected 0), `fields_changed` (the subset of those four fields with a non-zero count), `days_removed` (0), `refused` (at most 40)}. **STOP before any republish** if `other_field_changes_on_common_days` is above 0, `days_removed` is above 0 or `refused` is above 40.
7. **The dry build of the republish.** ONE synchronous `{}` to `irpt-cot-reporting-publish-lambda` (nothing uploaded). Record `publish_dry` {`published` (939), `refused` (at most 40; STOP above 40)}.
8. **The canary.** ONE synchronous `{"upload": true, "accounts": ["<one id>"]}` for the first account (sorted) that gains a changed-row day. Read its series back in memory against the PREVIOUS VERSION of the same object: `canary` {`account_digest12`, `dates_gained` (a non-empty subset of the five changed-row days), `common_fields_equal_except_movable` (every per-day field equal on every common day except `total_return_daily`, `external_flow`, `day_quality` and `return_basis`), `manifest_unchanged_but_dates` (the manifest's `publisher_version`, `history_scope` and claim equal to before)}. STOP on any difference.
9. **The full republish.** ONE synchronous `{"upload": true}` (900 s: wait; judge a lost response from the log). Record `publish_full` {`published` (939), `refused` (equal to step 7), `objects_before`, `objects_after` (equal), `versions_before`, `versions_after` (at least published minus refused more)}.
10. **The after-read and the receipt.** `after` {`gold_day_rows` (per day), `gold_total_rows` (before total minus the old counts plus the new), `partitions` (equal), `gold_code_sha256`, `publish_code_sha256`, `schedules` (equal to step 2), `series_prefixes` (939), `series_with_day` (per changed-row day: the number of current series that hold it, read client-side from every series), `sample_ok` (25 sorted-position series each compared in memory with its previous version: only the added days and the four movable fields on common days differ)}; `ledger_closed` false (the issuer closes it after verification); `reads` {`vendor_calls` 0, `secret_reads` 0}; `notes` (words: counts, the memory and duration of the largest event, and the three sentences "the rewrite changed <N> gold days", "the external flows of the landed days are no longer summed across overlapping transaction partitions" and "the YTD return still reads Not measured while any of 08-19, 09-24 or 09-25 is in the window"). Write `COT_ALLDAYS_APPLY_RECORD.json` and flip this order's status to complete as your last commit.

<criterion id="DBC201-1-AC1" cell_refs="DB-b-337"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p201_cot_alldays_apply.py" . DBC201-1-AC1</invocation><expect>DBC201-1-AC1 PASS</expect></criterion>
`DBC201-1-AC1` -- the record: both halves signed at the packet's sha256, the ledger, the before reads, the scaling run, every event's dry run in its band against the issuer's read file, the rewrites (version +1, the previous versions kept, flows fell), the pre-write diff inside its STOP lines, the canary, the full republish, the after-read, no id. Base: FAIL (no record).
<criterion id="DBC201-2-AC1" cell_refs="DB-b-337"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p201_cot_alldays_apply.py" . DBC201-2-AC1</invocation><expect>DBC201-2-AC1 PASS</expect></criterion>
`DBC201-2-AC1` -- FRESH live reads of the gold days: each current version holds the recorded rows and at most 15 percent NOT_MEASURABLE rows (the floor day excepted), each earlier version is kept, the absolute flows fell on every day whose rows did not change, the gold total and partition count equal the record's, the function's code and both schedules are as before. Base: FAIL.
<criterion id="DBC201-3-AC1" cell_refs="DB-b-337"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p201_cot_alldays_apply.py" . DBC201-3-AC1</invocation><expect>DBC201-3-AC1 PASS</expect></criterion>
`DBC201-3-AC1` -- FRESH live reads of the series: 939 prefixes, each changed-row day present in the recorded number of series, and 60 sampled series each differ from their previous version only by the added days and the four movable fields (the checker compares the data itself). Base: FAIL.

<expected_criteria>DBC201-1-AC1,DBC201-2-AC1,DBC201-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the AWS acts the packet names and nothing wider. Everything else is read, never edited.
- **The signed acts, and nothing wider.** Writes to AWS: the gold-day rewrites (a new version each), the canary (one series and manifest) and the full republish (the Cottonwood series and manifests at the same keys). No `update-function-code`, no Terraform, no delete of any object or version, no schedule change (the publish schedule's re-enable is a SEPARATE later act), no other gold day, no environment variable, no event other than the four named (the rewrite, its dry run, the dry build, the upload).
- **Stop rules.** A `Task timed out`, an `AccessDenied`, a Max Memory Used above 819 MB, a duration above 720 s, a dry run outside its band, a held day, a gold day above 15 percent NOT_MEASURABLE after the rewrites (the floor day excepted), a flow sum that rose on a day whose rows did not change, a pre-write read outside its STOP lines, a canary that breaks the previous-version invariant, a refusal above 40: STOP at once and report to the issuer. The rollback is the packet's section 6 (a copy of each kept previous version over its key, under the ledger; never a delete).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB12-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-337.apply-cottonwood-alldays-rewrite-and-republish.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 198 (round 150, workstream ALLDAYS), cell `DB-b-337`.
<owned_cells>DB-b-337</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC201-1-AC1, DBC201-2-AC1, DBC201-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-337.apply-cottonwood-alldays-rewrite-and-republish.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC201-1-AC1,DBC201-2-AC1,DBC201-3-AC1` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once, after step 10: each criterion's last line, the counts of the receipt, no id.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: no plan, no apply of infrastructure; the acts are data writes through two existing functions under the signed packet's stop lines.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM or grant changes; the two functions' roles are used as they are (the transaction stage's list grant is ~F2's separate, applied act).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched (read before and after only; the publish schedule's re-enable is a separate later act).
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the checker FAILS at the base and its selftest is red on 90 single-fault mutants of a synthetic record.
lane: the <paths> block and the signed pair ARE the grant.
</preflight>
