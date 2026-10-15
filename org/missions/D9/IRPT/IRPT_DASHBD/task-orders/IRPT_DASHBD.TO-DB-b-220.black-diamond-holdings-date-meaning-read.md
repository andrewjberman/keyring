# TO IRPT_DASHBD.TO-DB-b-220 -- READ the meaning of the Black Diamond holdings date on Investor Reporting: is a holdings partition's date the close its prices reflect, or the day it was pulled; measured as an offset distribution over a printed denominator of dated partitions with a positive control, and where the holdings citation takes its date today; read only

<to_id>IRPT_DASHBD.TO-DB-b-220</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~177</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>110</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-110 ANALYSIS section 1 (row "The Black Diamond date's meaning on Investor Reporting") and section 2 cell 3(a) (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_110_20261014.md`: "A READ: is the BD holdings file's date the close the holdings reflect, or the day it was pulled? If it is the pull day, the citation carries the holdings' own date") | **Rows:** IRPT_DASHBD-D2-W177-S<k> | **Decomp cell:** `DB-b-220` (decomposition section 112) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-177` (branch `wk-IRPT_DASHBD-177`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~177/`. Never push; never commit the workspace `portal` gitlink. The portal is READ-ONLY for you: read it at `C:/dev/ajb_workspace/portal/src/pages/InvestorReporting/` (your worktree's `portal` may be empty). Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes and words only in the repo, a row or your report; an account id, a client name or a figure (a value, a price) is never recorded.

**Why.** Andrew saw "as of 5 PM ET, October 14" at 2:37 PM on a Black Diamond (Cottonwood) page: the page cites a date and a time for its holdings. The CTO asks first what the holdings file's DATE means: the close the holdings reflect, or the day the file was pulled. A holdings partition `date=D` was ruled (CTO rulings batch 63 item 2, row IRPT_BCKEND-S245) to hold D's OWN close, INFERRED from 10 of 81 partitions read against Schwab's own-date anchor, with a minority of lagged prices (the read is `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/HOLDINGS_SOURCE_DATE_BASIS_READ_20261001.md`; the declaration is `partition_close` in `data/assets/scripts/gold/irpt_holdings_performance/sources.json`, channel `blackdiamond_z09`). This cell measures it for Black Diamond's own file, over far more partitions, so the citation can carry the holdings' own date if the file's date is the pull day. Nothing is changed.

**The grant of the S3 reads (BY PREFIX).** LIST and GET under the ONE prefix `holdings_performance.py` resolves for the channel `blackdiamond_z09` as `positions_prefix` (`s3://opal-data-assets/blackdiamond/<scope>/silver/fact_holdings/`: compute it with that module's own `resolved_prefix` and registry derivation by a read-only import, never by typing the scope), and nowhere else. No put, copy or delete. Read the `date=` partition keys and object metadata (LastModified) of ALL partitions of that prefix; read the CONTENTS of every weekday partition of the window that has a weekday predecessor partition (state the count), and only the columns `Ticker`, `Units` and `Market Value` plus the date or time columns (step 3). The ONE other read this cell makes is the served model series GET through `model_series_windows` (step 3).

**The cell (`DB-b-220`): a READ. Nothing is changed, deployed or written (outside your folder).**
1. **Read first.** The prior read and the declaration above; `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (how it reads a partition and which column is the price); the portal's date citation: `portal/src/pages/InvestorReporting/index.tsx` (the `dataAsOf=` prop near line 429), `portal/src/pages/InvestorReporting/contracts/adapt.ts` (`businessAsOf`, near lines 158-167, 804-818 and 1229-1233) and `portal/src/components/DataAsOf.tsx` with `portal/src/lib/dateUtils.ts`, to find where Investor Reporting's HOLDINGS citation takes its date today.
2. **Name every carrier of a date.** For a Black Diamond holdings partition: the partition key `date=`, the object's LastModified (the day it was written to S3), any date or time column inside the file (name each one and say whether it is a business date, a price date or a load stamp), and the bronze or pull stamp if one exists. Record `evidence.date_carriers`: one entry per carrier with `surface` (the file, key or column, by name), `carries` (words: what date it holds) and `claim`.
3. **Measure the offset by correlation with the served model series (issuer amendment, row `W177-S1`: the independent series is named here).** The independent series is the served dated model series (`s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json`: four named series, each with a daily `index_benchmark_return`), read through `data/assets/scripts/gold/irpt_reporting/adapters/model_series_windows.py` (one GET; it is not derived from the holdings file). Denominator: ALL partitions of the prefix over the last 120 calendar days (print how many; `evidence.denominator.dated_files`). Securities: the bond ETFs `BIV`, `VCIT`, `VCSH` and `VGSH`, taken only if held in at least 60 weekday partitions of the window (name the ones you use). For each partition, a security's price is the modal value of `Market Value` divided by `Units` over that ticker's rows with Units above zero. For each weekday partition date D whose previous weekday also has a partition and where both days are trading days (`lib/trading_calendar.py`), the security's change on D is the percent change of its price from that previous partition to D. For each security and each of the four served series compute the Pearson correlation, over all such dates, between the security's change on D and the series' daily return on the date at OFFSET k: offset 0 = the series date D itself (the file dated D reflects D's own close); offset 1 = the previous trading day of D (the file dated D reflects the prior trading day's close); offset -1 = the next trading day (print it as a check). Each security-and-series PAIR whose best absolute correlation over the three offsets is at least 0.5 gives ONE estimate: the offset with the highest correlation. Record `evidence.offset_estimates` (the number of such pairs; at least 4 are needed, else the answer is `UNDETERMINED` with claim `held` and the correlations you measured), `evidence.offset_distribution_days` (offset as text to count of estimates; the counts sum to `offset_estimates`) and `evidence.files_compared` (the number of partition dates used, 1 to the denominator), `evidence.offset_definition` (the words above) and, as words and counts, how the LastModified day relates to the partition date (same day, next day, later). ALSO record `evidence.calendar_signature` (words and counts, not checked): for the partition pairs 2026-06-12 to 2026-06-15 and 2026-06-18 to 2026-06-22 (weekend files exist for 13, 14, 20 and 21 June; 19 June was a market holiday), the share of the securities in `BIV VCIT VCSH VGSH GLD VEA VUG QQQ IEMG` whose price is unchanged between each consecutive pair of partitions (print the pair and the share).
4. **A positive control.** Run your same offset method on a synthetic copy of one comparison with the price series shifted one trading day, and show it reads offset 1 (`positive_control`: description, expected, observed, passed true). A method that cannot read a planted shift reads nothing.
5. **The answer.** `answer.holdings_date_means`: `CLOSE_DATE` (at least 80 percent of the compared files at offset 0), `PULL_DATE` (at most 20 percent at offset 0), `MIXED` (between), or `UNDETERMINED` (say why, claim held or absent). `answer.words`: one to three sentences.
6. **The citation today and what follows.** `citation_today`: `file` (an EXISTING repo-relative file), `line` (where the date is taken), `takes_date_from` (the field or function) and `words` (what the holdings citation prints today for a Black Diamond account and from what: a date only, or a clock, and the source of each). `consequence`: `citation_must_change` (true when the answer is `PULL_DATE`; false when `CLOSE_DATE`; your judgment when `MIXED` or `UNDETERMINED`) and `words`.
7. **Record** `RD_BD_DATE_R110.json` in your folder with exactly: `answer` {`holdings_date_means`, `words`, `claim`}; `evidence` {`date_carriers`, `files_compared`, `denominator` {`dated_files`, `scope_words`}, `offset_definition`, `offset_distribution_days`, `claim`}; `positive_control`; `citation_today` {`file`, `line`, `takes_date_from`, `words`, `claim`}; `consequence` {`citation_must_change`, `words`}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer)}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`: a figure you counted is `measured`, a rule taken from a prior read is `inferred`. Counts, names and words only: no account id, no price or value, no run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256` or `vintage` field.

<criterion id="DB110-5-AC1" cell_refs="DB-b-220"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_reads.py" . DB110-5-AC1</invocation><expect>DB110-5-AC1 PASS</expect></criterion>
`DB110-5-AC1` -- the record names at least two date carriers each with a claim; the denominator and the compared count are printed and the offset counts sum to the offset estimates (at least 4); the answer agrees with the distribution (CLOSE_DATE at 80 percent or more at offset 0, PULL_DATE at 20 percent or less, MIXED between; UNDETERMINED carries held or absent); a passed positive control; the citation's file exists and its line is stated; `citation_must_change` is true for PULL_DATE and false for CLOSE_DATE; every value group carries a claim in the four-word set; no write, push or deploy; no run of 8 or more digits outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB110-5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `sources.json`, `holdings_performance.py`, every portal file and the issuer's check files.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the one prefix above; the one served-series GET through `model_series_windows`. Writes: your folder only. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read.
- **Client data.** The holdings partitions are client data: counts, names and words only in the repo, a row or your report.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Never compare the file with a series derived from itself; if fewer than 4 security-and-series pairs reach a correlation of 0.5 the answer is UNDETERMINED (a finding, not a block). An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W177-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~177/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-220.black-diamond-holdings-date-meaning-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 112 (round 110), cell `DB-b-220`.
<owned_cells>DB-b-220</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB110-5-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~177/IRPT_DASHBD.TO-DB-b-220.black-diamond-holdings-date-meaning-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB110-5-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the answer (CLOSE_DATE, PULL_DATE, MIXED or UNDETERMINED) with the partitions compared out of the denominator and the offset counts; the date carriers you found (names only); where the holdings citation takes its date today (file and line) and whether it must change; the independent series you measured against; the S3 reads count; row ids. No account id, client name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and one record in the worker's folder; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and GET of one registry-derived Black Diamond silver prefix of the monolith bucket; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB110-5-AC1 FAILS at base (no record) and the checker's 9-arm self-test refuses a distribution that disagrees with its answer, a failed control and an identifier-length digit run.
lane: the <paths> block IS the grant.
</preflight>
