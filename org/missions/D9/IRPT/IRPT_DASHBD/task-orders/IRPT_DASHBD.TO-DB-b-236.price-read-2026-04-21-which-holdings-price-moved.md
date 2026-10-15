# TO IRPT_DASHBD.TO-DB-b-236 -- the 2026-04-21 PRICE READ (round 119, workstream B-49F): which holdings price moved, or failed to, on the day the flow guard disagreed for 943 accounts; the account-level profile of IRPT_BCKEND's holdings performance gold for those accounts (recounted by the checker) and, where the holdings gold carries security grain, the securities whose price return is flat or absent with their price source and security class; counts only; nothing written

<to_id>IRPT_DASHBD.TO-DB-b-236</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~190</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>119</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 119 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-119 ANALYSIS (B-49F) section 2 ruling 4 and section 3 cell 4 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_119_20261015.md` @d856067e84: "The 04-21 next read: which holdings price moved, or failed to. For the VALUE rows, name the securities whose price return on that day is flat or absent while the position value moved, and the price source of each. Counts by source and by security class; no client value. No repair this round") | **Rows:** IRPT_DASHBD-D2-W190-S<k> | **Decomp cell:** `DB-b-236` (decomposition section 117) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-190` (branch `wk-IRPT_DASHBD-190`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~190/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row or your report; never an account id or a client value (a return, a value, a flow, a position). A SECURITY identifier (a ticker or CUSIP of a listed security) with a count of accounts is not a client value and may be named in the record.

**Why.** Round 118 found that on 2026-04-21 the 49 Financial account gold has 943 `GRADED_DISAGREED` rows, 941 of them `VALUE` (the account value changed while the holdings price return did not agree) and 2 `FLOW_AND_VALUE` (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~186/RD_FLOW_GUARD_READ_R118.json`, first date). The issuer's own look at the persisted columns (counts only): for these 943 accounts the value return of the day, V/V0 - 1, sits in a narrow band of about -1.1 percent for nearly all of them, while the holdings price return the guard compares with runs from about -2.4 to -1.4 percent (median about -1.9 percent); the holdings gold reports every one of them status OK and almost none with an excluded security. So the account value and the holdings price return fell by different amounts for one cohort on one day. The CTO asks which holdings price moved, or failed to. The producer is this project's `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`; the neighbour it compares against is IRPT_BCKEND's `holdings_performance_daily` gold (account grain: `daily_return`, `account_value`, `excluded_count`, `excluded_weight`, `status`, `held_count`). A READ: nothing is changed, deployed or written outside your folder; any repair is a later round's packet under a never-widen pair.

**The cell (`DB-b-236`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r119/p119_priceread.py` (your criterion: the record's exact fields and what the checker recounts are in its docstring and clauses); round 118's record above and its script `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~186/flow_guard_read_r118.py` (how the 49 Financial gold partitions are addressed and read: copy what you need into YOUR script); the producer's guard and its neighbour read (`account_return_daily.py`, `HOLDINGS_TABLE`, `comparability`, `guard_state_of`, and where it reads `daily_return`; record file and line); `lib/opal_naming.py`, `lib/trading_calendar.py`.
2. **The account-level profile (the checker recounts it).** Read, with a read-only reader derived from `address("irpt", "49financial", "gold", <table>, "date=2026-04-21", ...)` and nowhere else: the `account_return_daily` partition of 2026-04-21 (columns `account_id, guard_state`) and the `holdings_performance_daily` partition of 2026-04-21 (columns `account_id, status, excluded_count, excluded_weight`). For the accounts whose `guard_state` is GRADED_DISAGREED record `account_profile`: `accounts` (their count), `no_holdings_row` (those with no row in the holdings partition), `by_status` (an object: each holdings `status` value to its count, over the accounts that hold a row), `excluded_count_zero` and `excluded_count_positive` (accounts with `excluded_count` 0 or above 0; a null counts as 0), `excluded_weight_bands` (an object with exactly the keys `zero`, `le_1pct`, `1_to_10pct`, `gt_10pct`: `excluded_weight` null or 0; above 0 and at most 0.01; above 0.01 and at most 0.10; above 0.10), and `claim`. The counts over the accounts that hold a row must add up (the bands, the two excluded counts and the statuses each sum to `accounts` minus `no_holdings_row`).
3. **`value_rows`** = round 118's `VALUE` plus `FLOW_AND_VALUE` for 2026-04-21 (read from the record above; the checker requires equality).
4. **The security level (where the source exists).** Locate, with `comp-estate --resource`, `comp-pipescript io` or the file tools, whether IRPT_BCKEND's gold carries SECURITY-grain price returns for 2026-04-21 (a table with one row per account or per security per day with a price return and a price source), and read it with the same read-only discipline (its address from `address()` or from its own registry row; no typed bucket). If it exists (`security_level.state` "READ"): for the accounts of step 2, name the securities (the public identifier) whose price return on 2026-04-21 is zero or null (flat or absent) while the account's position value moved: `securities` (at most 25 entries, the most affected first, each {`security`, `security_class`, `price_source`, `price_state` ("flat" or "absent"), `accounts_affected` (a count of the step-2 accounts holding it), `claim`}), `by_price_source` and `by_security_class` (objects of counts over the (account, security) pairs you counted; the two sums are equal), `source` {`file`, `table`, `words`} and `words`. If no such source exists (`state` "ABSENT"): {`state`, `words` (what you searched and why no security grain exists), `claim` "absent"}; the account-level profile then stands as the answer. Never invent a security.
5. **A positive control.** Run YOUR selection function on a synthetic set (a flat-price security with a moving position, an absent price, a moving price, an excluded security) and show each lands as expected (`positive_control`: description, expected, observed, passed true).
6. **Write your analysis as a tracked script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~190/price_read_0421_r119.py` (no write call to AWS; names no other firm's place; writes ONLY a private file under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~190/`).
7. **Record** `RD_PRICE_READ_0421_R119.json` in your folder, counts, dates and words only, with EXACTLY these fields: `date` ("2026-04-21"), `value_rows`, `account_profile` (step 2), `security_level` (step 4), `positive_control`, `method_words` (words: what you read and how, and what the profile says in one paragraph), `analysis` {`file`, `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim`, `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256` or `vintage` field; no account id; no client value.

<criterion id="DB119-4-AC1" cell_refs="DB-b-236"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r119/p119_priceread.py" . DB119-4-AC1</invocation><expect>DB119-4-AC1 PASS</expect></criterion>
`DB119-4-AC1` -- `RD_PRICE_READ_0421_R119.json` has exactly the form of step 7; `value_rows` equals round 118's VALUE plus FLOW_AND_VALUE for 2026-04-21; the account profile EQUALS the checker's own recount from the gold (the GRADED_DISAGREED accounts of the 2026-04-21 `account_return_daily` partition against the 2026-04-21 `holdings_performance_daily` partition: accounts, no holdings row, statuses, excluded counts, excluded-weight bands) to the unit and every part sums as step 2 says; the security level is READ (1 to 25 securities, each with a class, a price source, a state, a count of accounts, and the two count objects summing equal) or ABSENT with words; the positive control passed; the analysis script is tracked, hashed as recorded, names no other firm's place and holds no write call; every claim is in the four-word set; zero writes, no push or deploy flags, and no run of 8 or more digits outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB119-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `account_return_daily.py`, `sources.json`, every contract, module and test, every adapter, round 118's script and record, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the 49 Financial irpt gold prefixes `account_return_daily` and `holdings_performance_daily` (the `date=2026-04-21` partitions) and, if you find one, ONE security-grain source of IRPT_BCKEND's gold for the same firm and date (its address from `address()` or its registry row), read-only. Writes: the repo files of the grant and the private folder named in step 6. No put, copy or delete of any kind, no deploy, no push, no vendor call, no secret read, no read of another firm's place, no Terraform, NO edit of the producer.
- **Client data.** The gold partitions and anything you derive from them are client data: counts, dates, hashes and words (and security identifiers with counts) only in the repo, a row or your report; never an account id or a client value.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a partition cannot be read, record the source `absent` with the refusal named, file a BLOCKING row with counts and stop on that point; an unreadable source is never a zero. If your account profile differs from the checker's recount, report both numbers in a BLOCKING row; do not adjust either. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W190-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~190/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-236.price-read-2026-04-21-which-holdings-price-moved.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 117 (round 119, workstream B-49F), cell `DB-b-236`.
<owned_cells>DB-b-236</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB119-4-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~190/IRPT_DASHBD.TO-DB-b-236.price-read-2026-04-21-which-holdings-price-moved.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB119-4-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the account profile (accounts, no holdings row, statuses, excluded counts and weight bands); the security level (READ with the top securities, their classes and price sources and the two count objects, or ABSENT with the words); the positive control; reads and writes. Counts, dates and words only: no account id and no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a tracked analysis script with a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the S3 reads are GET and LIST of prefixes of one firm already read by the firm's own producers and the round-111 to round-118 drivers.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB119-4-AC1 FAILS at base (no record) and its recount and consistency clauses are exercised by the checker's self-test (band and profile arms, one green and ten red record arms); its recount was dry-run by the issuer against the real gold in 1.4 seconds.
lane: the <paths> block IS the grant.
</preflight>
