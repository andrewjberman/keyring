# TO IRPT_DASHBD.TO-DB-b-332 -- APPLY the signed Cottonwood RE-LAND pair (packet sha256 `37ce1e48`): EIGHT gold days rewritten through the function's own explicit rewrite event (dry run first) and the series republished ONCE: gates and live reads, ledger, eight dry runs, eight rewrites, the pre-write read, the dry build, ONE canary, the full republish, the after-read (CTO ruling after msg 10575; CTO half @e5d081d262) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-332</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>RELAND</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_COTTONWOOD_RELAND_PAIR_COO_HALF.md` and CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_RELAND_PAIR_CTO_HALF.md` @e5d081d262, both bound to the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_COTTONWOOD_RELAND_PAIR.md` (sha256 `37ce1e48bb2abd4e1cb150dd8cb672bea86534ec3ac6c206e4b06fc5e0938e23`) | **Decomp cell:** `DB-b-332` (decomposition section 193).

**Risk class WORLD, served output:** EIGHT gold days are rewritten (a new version each; the previous version kept) and the Cottonwood series are republished (new versions at the same keys). No code, role, schedule or other gold day changes. The three days with no transactions partition (08-19, 09-24, 09-25) are NOT touched.

**The days.** The four RE-LANDED days (the packet's DAYS): 2026-07-22, 2026-07-27, 2026-07-29, 2026-08-03. The four NEXT days (each follows a re-landed day and is NOT_MEASURABLE in the gold itself): 2026-07-23, 2026-07-28, 2026-07-30, 2026-08-04. The eight gold days, ascending: 07-22, 07-23, 07-27, 07-28, 07-29, 07-30, 08-03, 08-04.

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying the packet, both halves and the read tools); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No account id, name or response body appears in any file, commit message, row, log line or message you send: an account is named only by the first 12 hex of the sha256 of its id. Counts, statuses and words only.

**Read first (all in your worktree):** the packet (whole) and both halves; `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (`lambda_handler`, `_rewrite`, `_run`); `infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py` (the republish events); the read tools `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/cot_publish_offline_diff.py` (it now prints the dates gained, dropped and changed, by count) and `.../reads/cot_relanding_state_read.py`; your own earlier Cottonwood republish `IRPT_DASHBD.TO-DB-b-315...` and its record; the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p198_cot_reland_apply.py` (the record's exact keys). **Lessons applied here:** every invoke uses `--cli-read-timeout 0 --invocation-type RequestResponse --log-type Tail`; a lost client response is judged from the Lambda log, never retried blind; no act between 11:30Z and 14:15Z on a weekday (today is Saturday); the sequence is the packet's and a STOP line stops the pair; your TO-DB-b-329 stop (a dry run outside its band, nothing written) is the model for every dry run below.

**Do, in this order. Record every value named in `COT_RELAND_APPLY_RECORD.json` as you go; a per-day value is an object keyed by the ISO date, for the eight days (or for the four re-landed days where stated).**

0. **Gates, read only.** (a) The packet's sha256 equals the one above; both halves read SIGNED at it (`gates.packet_sha256`, `gates.coo_half_signed`, `gates.cto_half_signed`). (b) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (print the denominator) has an OPEN LEG on `irpt-cot-account-return-daily-lambda`, `irpt-cot-reporting-publish-lambda`, the gold prefix `irpt/cottonwood/gold/account_return_daily/` or the published prefix `irpt/cottonwood/platinum/reporting/` (`gates.one_change_at_a_time`: `worktrees_read`, `open_markers_naming_this_surface` = open legs on this surface, 0). (c) The live state equals the packet's section 2 (`gates.live_matches_packet`). Any mismatch: STOP. Record `days` = the four re-landed days.
1. **Open the NEVER-2 ledger BEFORE any write:** `python .tools/deploy_ledger.py open ...`, slug `irpt-dashbd-cottonwood-reland-pair-20261017`, **naming yourself (`0.7.0_AE_CloudOps~IB2`) as the applier**; legs: L1 before reads; L2 dry runs; L3 rewrites; L4 pre-write diff; L5 canary; L6 full republish; L7 receipt. Commit its `.open_deploys` sentinel at once. Record `ledger_entry`.
2. **Before reads** `before` {`day_rows` (the rows of each of the eight days' gold objects: the four re-landed days PARTIAL, at most 500 rows (expected 157, 3, 1, 159); the four next days full-sized, 850 or more (expected 879, 881, 881, 888)), `day_versions` (each day's VersionId count), `full_day_rows` (rows of `date=2026-07-21`: expected 879), `gold_total_rows` (rows summed over every parquet object of the gold table, client-side, every page, denominator printed), `partitions` (the count of `date=` partitions), `series_prefixes` (the `account=` prefixes of the published prefix, one delimiter listing: 939), `series_objects` and `series_versions` (every object and every version under the published prefix), `gold_code_sha256` (expected `+iYXakKx7zhK33lv6W0jDAY1QsLYUNqNCuHHIA7owD0=`), `publish_code_sha256` (expected `vYNB1EBTU2qEIINxTnhYQBBBEHBYFId7lllrIJM3YRE=`), `schedules` ({`account_return_daily` the state of `irpt-cot-account-return-daily-daily`: ENABLED, `publish_daily` the state of `irpt-cot-reporting-publish-daily`: DISABLED})}. Also read each day's count of `day_quality` NOT_MEASURABLE rows and put the eight counts in `notes`.
3. **The dry runs.** EIGHT synchronous events, one per day in ascending order, `{"rewrite": {"start": "<day>", "end": "<day>"}, "dry_run": true}` to `irpt-cot-account-return-daily-lambda`. Record `dry_run` {`ok` (true when every event returned ok), `days` (the eight days), `held` (the sum over the events: 0), `rows` (per day, from each response), `gold_objects_before`, `gold_objects_after`, `gold_versions_before`, `gold_versions_after` (counts over the whole gold prefix read before the first and after the last event: EQUAL)}. **STOP** on any `held` above 0, any day's rows outside 840 to 960, an exception, a timeout, Max Memory Used above 819 MB or a duration above 600 s.
4. **The rewrites.** The same eight events WITHOUT `dry_run`, in ascending order. Record `rewrite` {`rows` (per day, equal to the dry run's), `day_versions_after` (per day, before + 1), `prior_versions_kept` (each day's previous version still readable by its VersionId), `other_partitions_unchanged` (every other partition's object and version counts equal to step 2)}. Then read each day's gold object again: **STOP before any republish** if any day holds more than 15 percent `day_quality` NOT_MEASURABLE rows or any other partition moved.
5. **The pre-write read.** Run `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/cot_publish_offline_diff.py` from the worktree root (read only; it prints, by count, the dates gained, the dates dropped and the common dates changed, with the fields). Record `prewrite` {`accounts_gaining_by_day` (per re-landed day: the series that would gain it), `other_field_changes_on_common_days` (changes on a day present in BOTH versions in any field other than `total_return_daily`, `day_quality`, `return_basis`; and any change in those three on a day other than the four next days: expected 0), `changed_dates` (the sorted set of common dates that change in the three fields: a subset of 07-23, 07-28, 07-30, 08-04), `days_removed` (0), `refused` (at most 40)}. **STOP before any republish** if `other_field_changes_on_common_days` is above 0, `changed_dates` holds any other date, `days_removed` is above 0, `refused` is above 40, or a date is GAINED that is neither a re-landed day nor a next day (the CTO half allows a next day to be gained when its gold count rises above its landed count).
6. **The dry build of the republish.** ONE synchronous `{}` to `irpt-cot-reporting-publish-lambda` (nothing uploaded). Record `publish_dry` {`published` (939), `refused` (at most 40; STOP above 40)}.
7. **The canary.** ONE synchronous `{"upload": true, "accounts": ["<one id>"]}` for the first account (sorted) that gains a re-landed day. Read its series back in memory against the PREVIOUS VERSION of the same object: record `canary` {`account_digest12`, `dates_gained` (a non-empty subset of the eight days), `common_fields_equal` (every field equal on every common day except `total_return_daily`, `day_quality`, `return_basis` on the four next days), `only_next_days_three_fields_differ`, `manifest_unchanged_but_dates` (the manifest's `publisher_version`, `history_scope` and claim equal to before)}. STOP on any difference.
8. **The full republish.** ONE synchronous `{"upload": true}` (900 s: wait; judge a lost response from the log). Record `publish_full` {`published` (939), `refused` (equal to step 6), `objects_before`, `objects_after` (equal), `versions_before`, `versions_after` (at least published minus refused more)}.
9. **The after-read and the receipt.** `after` {`gold_day_rows` (per day), `not_measurable` (per day: the count of NOT_MEASURABLE rows now, at most 15 percent of that day's rows), `gold_total_rows` (before total minus the eight old counts plus the eight new), `partitions` (equal), `gold_code_sha256`, `publish_code_sha256`, `schedules` (equal to step 2), `series_prefixes` (939), `series_with_day` (per re-landed day: the number of current series that hold it, read client-side from every series), `sample_ok` (25 sorted-position series each compared in memory with its previous version: only the added days and the three fields on the four next days differ)}; `ledger_closed` false (the issuer closes it after verification); `reads` {`vendor_calls` 0, `secret_reads` 0}; `notes` (words: counts, the memory and duration of the largest event, the eight NOT_MEASURABLE counts before and after, and the three sentences "the rewrite changed eight gold days", "the daily returns of the four days after the re-landed days moved from not measurable to measured" and "the YTD return still reads Not measured while any of the three days with no transactions partition is in the window"). Write `COT_RELAND_APPLY_RECORD.json` and flip this order's status to complete as your last commit.

<criterion id="DBC198-1-AC1" cell_refs="DB-b-332"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p198_cot_reland_apply.py" . DBC198-1-AC1</invocation><expect>DBC198-1-AC1 PASS</expect></criterion>
`DBC198-1-AC1` -- the record: both halves signed at the packet's sha256, the ledger, the before reads, the eight dry runs in their band, the eight rewrites (version +1, the previous versions kept), the pre-write diff inside its STOP lines, the canary, the full republish, the after-read, no id. Base: FAIL (no record).
<criterion id="DBC198-2-AC1" cell_refs="DB-b-332"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p198_cot_reland_apply.py" . DBC198-2-AC1</invocation><expect>DBC198-2-AC1 PASS</expect></criterion>
`DBC198-2-AC1` -- FRESH live reads of the eight gold days: each current version holds the recorded rows and at most 15 percent NOT_MEASURABLE rows, each earlier version is kept, the gold total and partition count equal the record's, both functions and both schedules are as before. Base: FAIL.
<criterion id="DBC198-3-AC1" cell_refs="DB-b-332"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p198_cot_reland_apply.py" . DBC198-3-AC1</invocation><expect>DBC198-3-AC1 PASS</expect></criterion>
`DBC198-3-AC1` -- FRESH live reads of the series: 939 prefixes, each re-landed day present in the recorded number of series, and 60 sampled series each differ from their previous version only by the added days and the three fields on the four next days (the checker compares the data itself). Base: FAIL.

<expected_criteria>DBC198-1-AC1,DBC198-2-AC1,DBC198-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the AWS acts the packet names and nothing wider. Everything else is read, never edited.
- **The signed acts, and nothing wider.** Writes to AWS: the EIGHT gold-day rewrites (a new version each), the canary (one series and manifest) and the full republish (the Cottonwood series and manifests at the same keys). No `update-function-code`, no Terraform, no delete of any object or version, no schedule change, no other gold day, no environment variable, no event other than the four named (the rewrite, its dry run, the dry build, the upload).
- **Stop rules.** A `Task timed out`, an `AccessDenied`, a Max Memory Used above 819 MB, a dry run outside its band, a held day, a gold day above 15 percent NOT_MEASURABLE after the rewrites, a pre-write read outside its STOP lines, a canary that breaks the previous-version invariant, a refusal above 40: STOP at once and report to the issuer. The rollback is the packet's section 6 (a copy of each kept previous version over its key, under the ledger; never a delete).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB11-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-332.apply-cottonwood-reland-pair-eight-gold-days-and-republish.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 193 (round 150, workstream RELAND), cell `DB-b-332`.
<owned_cells>DB-b-332</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC198-1-AC1, DBC198-2-AC1, DBC198-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-332.apply-cottonwood-reland-pair-eight-gold-days-and-republish.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC198-1-AC1,DBC198-2-AC1,DBC198-3-AC1` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once, after step 9: each criterion's last line, the counts of the receipt, no id.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: no plan, no apply of infrastructure; the acts are data writes through two existing functions under the signed packet's stop lines.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM or grant changes; the two functions' roles are used as they are.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched (read before and after only).
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the checker FAILS at the base and is red on 77 single-fault mutants of a synthetic record.
lane: the <paths> block and the signed pair ARE the grant.
</preflight>
