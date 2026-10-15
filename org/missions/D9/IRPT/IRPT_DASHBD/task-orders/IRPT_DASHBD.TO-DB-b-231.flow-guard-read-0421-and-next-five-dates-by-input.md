# TO IRPT_DASHBD.TO-DB-b-231 -- the FLOW-GUARD READ: the 49 Financial account return gold's GRADED_DISAGREED rows on 2026-04-21 and on the next five dates by households broken (2026-07-02, 2026-10-13, 2026-09-22, 2026-10-06, 2026-09-16), each classified by which input disagrees (the flow, the value, both, neither, or no prior day) with the sign, size and next-day behaviour of the value gap; counts only; nothing written

<to_id>IRPT_DASHBD.TO-DB-b-231</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~186</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>118</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ANALYSIS ANSWERING ROUND 113 section 2 ruling 1 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ANSWERING_ROUND_113_20261015.md` @5934ffcedc: "a READ of the flow guard's disagreement on 2026-04-21 and on the next five dates (07-02, 10-13, 09-22, 10-06, 09-16). For each date and household-sense account, it asks which input disagrees: the flow, the value, or the guard's tolerance. Counts by cause, with no client value copied. No repair in this round, because a repair moves served numbers and needs a never-widen pair") | **Rows:** IRPT_DASHBD-D2-W186-S<k> | **Decomp cell:** `DB-b-231` (decomposition section 116) | **outcome_ref:** FWD-2, FWD-21 (Andrew's P1: the performance reporting tab functional for all clients at all firms) | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-186` (branch `wk-IRPT_DASHBD-186`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~186/`. Never push; never commit the workspace `portal` gitlink (you have no portal work). Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row or your report; a household or account id, a name and a figure that is a client value (a return, a value, a flow) is never recorded.

**Why.** Round 113 found that the 858 households broken on 2026-04-21 are broken by the flow guard, not by link breaks: 943 of that date's account rows are `guard_state` GRADED_DISAGREED (`day_quality` FLOW_UNRECONCILED, `total_return_daily` null: the producer serves nothing when the guard graded and disagreed). The producer is this project's own `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`. The guard compares the account's own daily return with the holdings price return (`holdings_price_return`); it disagrees when the two differ by more than the tolerance. The CTO asked which INPUT disagrees. The gold carries only persisted columns, so this read classifies each disagreeing account-day from them by the rule below, and profiles the value gap. A READ: nothing is changed, deployed or written outside your folder; any repair is a later round's packet under a never-widen pair.

**The cell (`DB-b-231`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r118/p118_flowguard.py` (your criterion `DB118-2-AC1`: the cause rule and the value-gap profile are written in its docstring and its pure functions `cause_of`, `split_rows`, `profile_rows`; the checker RECOMPUTES every count of your record from the gold itself and they must equal yours to the unit); the producer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (the guard: `comparability`, `guard_state_of` around line 1090, and the block around lines 1430 to 1530 that sets FLOW_UNRECONCILED; record the file and line of each site you describe); the account contract `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (`columns`, `enums`); `lib/trading_calendar.py` (`prev_trading_day`, `is_trading_day`); `lib/opal_naming.py`; round 113's record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~184/RD_NOT_MEASURABLE_R113.json` and its tracked script `not_measurable_read_r113.py` (how the firm's gold partitions are addressed and read: copy what you need into YOUR script, never import or edit it).
2. **The dates, in this order:** 2026-04-21, 2026-07-02, 2026-10-13, 2026-09-22, 2026-10-06, 2026-09-16. For each date D read, with a read-only reader, ONLY (a) the 49 Financial `account_return_daily` gold partition `date=D` (`data.parquet`, columns `account_id, market_value_eod, external_flow, holdings_price_return, guard_state, day_quality`, and its `manifest.json`), and (b) the partition of the previous trading day (`prev_trading_day(D)`), and (c) the partition of the NEXT trading day (the first trading day after D; its partition may be absent: say so). Every address is `lib/opal_naming.py address("irpt", "49financial", "gold", "account_return_daily", "date=<day>", ...)` derived from the firm's registry row exactly as round 113's script does; never type a bucket or a prefix.
3. **The tolerance** `tau` is the one the date's OWN `manifest.json` carries (`thresholds.tolerance`). Record the file and key path as `tolerance_source`. If a manifest lacks it, BLOCKING row and stop on that date.
4. **The cause of a GRADED_DISAGREED row** (account a, date D; V = `market_value_eod`, F = `external_flow`, p = `holdings_price_return`; V0 = the account's `market_value_eod` on the previous trading day): `NO_PRIOR` when the account has no row on the previous trading day, or V0 is not above zero, or V, F or p is null. Otherwise v = V / V0 - 1, s = |F| / V0, `value_gap` is |v - p| > tau and `flow_big` is s > tau: `FLOW` when flow_big and not value_gap; `VALUE` when value_gap and not flow_big; `FLOW_AND_VALUE` when both; `NEITHER` when neither. These five are the whole domain: `by_cause` has exactly these five keys and sums to `rows_graded_disagreed`. Claim `inferred` for the classification (it is read from persisted columns, not from the producer's internal comparison).
5. **The value-gap profile** per date over the rows whose cause is VALUE or FLOW_AND_VALUE, gap = v - p: `value_gap_rows`; `gap_positive`, `gap_negative` (by the sign of gap); `band_le_1pct`, `band_1_to_5pct`, `band_gt_5pct` (by |gap| at most 0.01, at most 0.05, above); and by the account's row on the NEXT trading day: `reversal_next_day` (the row exists, its V0 is this day's V above zero, p is not null and its own gap v' - p' has the opposite sign with |gap'| above tau), `not_reversed` (the row exists and is not a reversal), `no_next_day_row` (no row, or the partition is absent). The signs sum to `value_gap_rows`, the three bands sum to it, and the three next-day counts sum to it.
6. **Per date also record** `rows` (the partition's rows), `rows_graded_disagreed` (rows with guard_state GRADED_DISAGREED), `rows_flow_unreconciled` (rows with day_quality FLOW_UNRECONCILED) and `tolerance`.
7. **A positive control.** Run YOUR classifier on a synthetic row set built to hit each of the five causes, plus a null prior value, and show each lands in its cause (`positive_control`: description, expected, observed, passed true).
8. **Write your analysis as a tracked script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~186/flow_guard_read_r118.py` (it holds no write call to AWS and names no other firm's place; it writes nothing to the repo except through your record; it may write ONLY a private file under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~186/`).
9. **Record** `RD_FLOW_GUARD_READ_R118.json` in your folder, counts, dates and words only, with EXACTLY these fields: `dates` (a list of exactly 6 entries in the order of step 2, each {`date`, `tolerance` (the manifest's number), `rows`, `rows_graded_disagreed`, `rows_flow_unreconciled`, `by_cause` ({FLOW, VALUE, FLOW_AND_VALUE, NEITHER, NO_PRIOR} to counts), `value_gap_profile` ({value_gap_rows, gap_positive, gap_negative, band_le_1pct, band_1_to_5pct, band_gt_5pct, reversal_next_day, not_reversed, no_next_day_row} to counts), `claim`}); `totals` {`rows_graded_disagreed` (the sum over the dates), `by_cause` (the sum per cause), `claim`}; `classification` {`words` (the rule of step 4 in your own words, one paragraph), `claim` "inferred"}; `tolerance_source` {`file` (the manifest's key pattern, for example the path form of the partition's manifest.json), `key_path` ("thresholds.tolerance"), `words`}; `positive_control` {`description`, `expected`, `observed`, `passed` true}; `analysis` {`file` "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~186/flow_guard_read_r118.py", `sha256`, `tracked` true}; `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent` (a count you made is `measured`). No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256` or `vintage` field; no household or account id; no client value.

<criterion id="DB118-2-AC1" cell_refs="DB-b-231"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r118/p118_flowguard.py" . DB118-2-AC1</invocation><expect>DB118-2-AC1 PASS</expect></criterion>
`DB118-2-AC1` -- `RD_FLOW_GUARD_READ_R118.json` has exactly the form of step 9; for each of the six dates the rows, the graded-disagreed rows, the flow-unreconciled rows, the tolerance, the five-way `by_cause` and the value-gap profile EQUAL the checker's own recount from the gold (read by the checker, GET only) to the unit; every split sums to its total; the totals are the sums over the dates; the positive control passed; the analysis script is tracked, hashed as recorded, names no other firm's place and holds no write call; every claim is in the four-word set; zero writes, no push or deploy flags, and no run of 8 or more digits outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB118-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `account_return_daily.py`, `sources.json`, every contract, module and test, every adapter, round 113's script and record, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of exactly one prefix of the firm 49 Financial, the irpt gold `account_return_daily` (the `date=` partitions of the six dates and of their previous and next trading days, `data.parquet` and `manifest.json` only), derived by `lib/opal_naming.py address()` and nowhere else. Writes: the repo files of the grant and the private folder named in step 8. No put, copy or delete of any kind, no deploy, no push, no vendor call, no secret read, no read of another firm's place, no Terraform, NO edit of the producer (this is a READ: any repair is a later round's packet under a never-widen pair).
- **Client data.** The gold partitions and anything you derive from them are client data: counts, dates, hashes and words only in the repo, a row or your report; never a household or account id.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a partition or a manifest cannot be read, record the source `absent` with the refusal named, file a BLOCKING row with counts and stop on that point; an unreadable source is never a zero. If your counts differ from the checker's recount on any date, report both numbers in a BLOCKING row; do not adjust either. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W186-S<k>` (the next free number: read the file's last id first), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~186/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-231.flow-guard-read-0421-and-next-five-dates-by-input.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 116 (round 118), cell `DB-b-231`.
<owned_cells>DB-b-231</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB118-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~186/IRPT_DASHBD.TO-DB-b-231.flow-guard-read-0421-and-next-five-dates-by-input.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB118-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; for 2026-04-21 the rows, the graded-disagreed rows, the five-way cause split and the value-gap profile (signs, bands, next-day split); the same split for each of the other five dates in one line each; the totals; the file and line of the producer's guard sites you read; the positive control; reads and writes. Counts, dates and words only: no household or account id and no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a tracked analysis script with a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the S3 reads are GET and LIST of one prefix of one firm already read by the firm's own producers and the round-111 to round-113 drivers.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB118-2-AC1 FAILS at base (no record) and its recount and consistency clauses are exercised by the checker's self-test (the cause rule, the profile and 13 red record arms); the issuer's own dry run of the recount read the six dates in 5 seconds.
lane: the <paths> block IS the grant.
</preflight>
