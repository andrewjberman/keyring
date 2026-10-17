# TO IRPT_DASHBD.TO-DB-b-329 -- APPLY the signed pair (packet sha256 `8596f43f`): rewrite the Cottonwood gold day 2026-07-27 from the now-full carrier delivery (dry run first), then republish the series (CTO msgs 10344, 10354, 10360) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-329</to_id>
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
<workstream>GOLD0727</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_COTTONWOOD_GOLD_REWRITE_20260727_AND_REPUBLISH_COO_HALF.md` @3a3680e93e and CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_GOLD_REWRITE_20260727_AND_REPUBLISH_CTO_HALF.md`, both bound to the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_COTTONWOOD_GOLD_REWRITE_20260727_AND_REPUBLISH.md` (sha256 `8596f43f1d0f06ba3944da6640c490c19e8440bc3426ec367f32e550b6b9252e`) | **Decomp cell:** `DB-b-329` (decomposition section 189).

**Risk class WORLD, served output:** ONE gold day is rewritten (a new version; the 3-row version kept) and the Cottonwood series are republished (new versions at the same keys). No code, role, schedule or other gold day changes. The six other absent days are NOT touched (dell1's carrier lane).

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying the packet, both halves and the read tool); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No account id, name or response body appears in any file, commit message, row, log line or message you send: an account is named only by the first 12 hex of the sha256 of its id. Counts, statuses and words only.

**Read first (all in your worktree):** the packet (whole) and both halves; `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (`lambda_handler`, `_rewrite`, `_run`); `infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py` (the republish events) and the read tool `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/cot_publish_offline_diff.py`; your own earlier Cottonwood republish `IRPT_DASHBD.TO-DB-b-315...` and its record; the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p195_cot_gold_rewrite_apply.py` (the record's exact keys). **Lessons applied here:** every invoke uses `--cli-read-timeout 0 --invocation-type RequestResponse --log-type Tail`; a lost client response is judged from the Lambda log, never retried blind; no act between 12:05 and 13:15 UTC on a weekday (today is Saturday); the sequence is the packet's and a STOP line stops the pair.

**Do, in this order. Record every value named in `COT_GOLD_REWRITE_APPLY_RECORD.json` as you go.**

0. **Gates, read only.** (a) The packet's sha256 equals the one above; both halves read SIGNED at it (`gates.packet_sha256`, `gates.coo_half_signed`, `gates.cto_half_signed`). (b) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (print the denominator) has an OPEN LEG on `irpt-cot-account-return-daily-lambda`, `irpt-cot-reporting-publish-lambda`, the gold prefix `irpt/cottonwood/gold/account_return_daily/` or the published prefix `irpt/cottonwood/platinum/reporting/` (`gates.one_change_at_a_time`: `worktrees_read`, `open_markers_naming_this_surface` = open legs on this surface, 0). (c) The live state equals the packet's section 2 (`gates.live_matches_packet`). Any mismatch: STOP.
1. **Open the NEVER-2 ledger BEFORE any write:** `python .tools/deploy_ledger.py open ...`, slug `irpt-dashbd-cottonwood-gold-rewrite-20260727-and-republish-20261017`, **naming yourself (`0.7.0_AE_CloudOps~IB2`) as the applier**; legs: L1 before reads; L2 dry run; L3 rewrite; L4 pre-write diff; L5 canary; L6 full republish; L7 receipt. Commit its `.open_deploys` sentinel at once. Record `ledger_entry`.
2. **Before reads** `before` {`day_rows` (rows of the gold object for `date=2026-07-27`: expected 3), `day_objects` (1), `day_versions` (the object's VersionId count), `full_day_rows` (rows of `date=2026-07-21`: expected 879), `gold_total_rows` (rows summed over every parquet object of the gold table, client-side, every page, denominator printed), `partitions` (the count of `date=` partitions), `series_prefixes` (the `account=` prefixes of the published prefix, one delimiter listing: 939), `series_objects` and `series_versions` (every object and every version under the published prefix), `gold_code_sha256` (expected `+iYXakKx7zhK33lv6W0jDAY1QsLYUNqNCuHHIA7owD0=`), `publish_code_sha256` (expected `vYNB1EBTU2qEIINxTnhYQBBBEHBYFId7lllrIJM3YRE=`), `schedules` ({`account_return_daily` the state of `irpt-cot-account-return-daily-daily`: ENABLED, `publish_daily` the state of `irpt-cot-reporting-publish-daily`: DISABLED})}.
3. **The dry run.** ONE synchronous `{"rewrite": {"start": "2026-07-27", "end": "2026-07-27"}, "dry_run": true}` to `irpt-cot-account-return-daily-lambda`. Record `dry_run` {`ok`, `days`, `held`, `rows` (the day's rows from the response), `gold_objects_before`, `gold_objects_after`, `gold_versions_before`, `gold_versions_after` (counts over the whole gold prefix read before and after: EQUAL)}. **STOP** on `held` above 0, rows outside 840 to 920, an exception, a timeout, Max Memory Used above 819 MB or a duration above 600 s.
4. **The rewrite.** The same event WITHOUT `dry_run`. Record `rewrite` {`rows` (equal to the dry run's), `day_versions_after` (before + 1), `prior_version_kept` (the 3-row version still readable by its VersionId), `other_partitions_unchanged` (every other partition's object and version counts equal to step 2)}.
5. **The pre-write read.** Run `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/cot_publish_offline_diff.py` from the worktree root (read only). Record `prewrite` {`accounts_gaining_the_day` (series that would gain 2026-07-27), `other_field_changes_on_common_days` (changes on a day present in BOTH versions in any field other than `total_return_daily`, `day_quality`, `return_basis`; and any change in those three on a day other than 2026-07-28: expected 0), `changed_dates` (the sorted set of common dates that change in the three fields: a subset of ["2026-07-28"]), `days_removed` (0), `refused` (0)}. **STOP before any republish** if `other_field_changes_on_common_days` is above 0, `changed_dates` holds any date but 2026-07-28, `days_removed` is above 0 or `refused` is above 0. If the tool cannot report the date set, derive it yourself from the dry build and say so in `notes`.
6. **The dry build of the republish.** ONE synchronous `{}` to `irpt-cot-reporting-publish-lambda` (nothing uploaded). Record `publish_dry` {`published` (939), `refused` (the earlier republish's count, 40; STOP above 10 percent of 939)}.
7. **The canary.** ONE synchronous `{"upload": true, "accounts": ["<one id>"]}` for the first account (sorted) that gains the day. Read its series back in memory against the PREVIOUS VERSION of the same object: record `canary` {`account_digest12`, `dates_gained` (exactly ["2026-07-27"]), `common_fields_equal` (every field equal on every common day except `total_return_daily`, `day_quality`, `return_basis` on 2026-07-28), `only_next_day_three_fields_differ`, `manifest_unchanged_but_dates` (the manifest's `publisher_version`, `history_scope` and claim equal to before)}. STOP on any difference.
8. **The full republish.** ONE synchronous `{"upload": true}` (900 s: wait; judge a lost response from the log). Record `publish_full` {`published` (939), `refused` (equal to step 6), `objects_before`, `objects_after` (equal), `versions_before`, `versions_after` (at least published minus refused more)}.
9. **The after-read and the receipt.** `after` {`gold_day_rows`, `gold_total_rows` (before total minus 3 plus the day's rows), `partitions` (equal), `gold_code_sha256`, `publish_code_sha256`, `schedules` (equal to step 2), `series_prefixes` (939), `series_with_day` (the number of current series that hold 2026-07-27, read client-side from every series), `sample_ok` (25 sorted-position series each compared in memory with its previous version: only the added day and the three fields on 2026-07-28 differ)}; `ledger_closed` false (the issuer closes it after verification); `reads` {`vendor_calls` 0, `secret_reads` 0}; `notes` (words: counts, the memory and duration of the largest event, and the sentences "the rewrite changed one gold day" and "the daily return of 2026-07-28 moved from not measurable to measured"). Write `COT_GOLD_REWRITE_APPLY_RECORD.json` and flip this order's status to complete as your last commit.

<criterion id="DBC195-1-AC1" cell_refs="DB-b-329"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p195_cot_gold_rewrite_apply.py" . DBC195-1-AC1</invocation><expect>DBC195-1-AC1 PASS</expect></criterion>
`DBC195-1-AC1` -- the record: both halves signed at the packet's sha256, the ledger, the before reads, the dry run in its band, the rewrite (version +1, the prior kept), the pre-write diff inside its STOP lines, the canary, the full republish, the after-read, no id. Base: FAIL (no record).
<criterion id="DBC195-2-AC1" cell_refs="DB-b-329"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p195_cot_gold_rewrite_apply.py" . DBC195-2-AC1</invocation><expect>DBC195-2-AC1 PASS</expect></criterion>
`DBC195-2-AC1` -- FRESH live reads of the gold day: the current version holds the recorded rows, the 3-row version is kept as the previous one, the gold total and partition count equal the record's, both functions and both schedules are as before. Base: FAIL.
<criterion id="DBC195-3-AC1" cell_refs="DB-b-329"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p195_cot_gold_rewrite_apply.py" . DBC195-3-AC1</invocation><expect>DBC195-3-AC1 PASS</expect></criterion>
`DBC195-3-AC1` -- FRESH live reads of the series: 939 prefixes, the day present in the recorded number of series, and 60 sampled series each differ from their previous version only by the added day and the three fields on 2026-07-28 (the checker compares the data itself). Base: FAIL.

<expected_criteria>DBC195-1-AC1,DBC195-2-AC1,DBC195-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the AWS acts the packet names and nothing wider. Everything else is read, never edited.
- **The signed acts, and nothing wider.** Writes to AWS: the ONE gold-day rewrite (a new version), the canary (one series and manifest) and the full republish (the Cottonwood series and manifests at the same keys). No `update-function-code`, no Terraform, no delete of any object or version, no schedule change, no other gold day, no environment variable, no event other than the four named.
- **Stop rules.** A `Task timed out`, an `AccessDenied`, a Max Memory Used above 819 MB, a dry run outside its band, a held day, a pre-write read outside its STOP lines, a canary that breaks the previous-version invariant, a refusal above 10 percent: STOP at once and report to the issuer. The rollback is the packet's section 6 (a copy of the kept prior version over the key, under the ledger; never a delete).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB10-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-329.apply-cottonwood-gold-rewrite-20260727-and-republish.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 189 (round 150, workstream GOLD0727), cell `DB-b-329`.
<owned_cells>DB-b-329</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC195-1-AC1, DBC195-2-AC1, DBC195-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-329.apply-cottonwood-gold-rewrite-20260727-and-republish.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC195-1-AC1,DBC195-2-AC1,DBC195-3-AC1` BEFORE the flip (the ids as ONE comma-joined argument); each row's recorded invocation must equal the order's criterion text exactly; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the dry run's rows, the pre-write counts, the canary's digest and verdict, the republish totals, the memory and duration of the largest event, and what is NOT proven. Counts and words only. Tell the issuer at once when step 4 (the rewrite) is done.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the two functions are the only writers of the changed objects; the write set is one gold day and the Cottonwood series and manifests; no resource is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant changes; the two functions' existing roles are used.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; their states are read and recorded and the checker requires them unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache is touched by the applier.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base (no record), the checker selftest is red on 56 single-fault arms, and its series clause compares sampled data with the previous version of its own object.
lane: the <paths> block IS the grant.
</preflight>
