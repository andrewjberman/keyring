# TO IRPT_BCKEND.TO-IB-pr-443 -- READ ONLY: the five one-day-off security-days, each set beside a THIRD dated value -- which witness sits on the wrong day?

<to_id>IRPT_BCKEND.TO-IB-pr-443</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~301</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>140</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5501 (ruling on IB-pr-442's sizing) | **Decomp cell:** `IB-pr-443` (decomposition section 132) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-301/` (bash `/c/dev/wk-irpt-bckend-301`). Work only there. READ ONLY toward AWS. ONE external source
only: Yahoo Finance through the reader below, ONE call for the four tickers, each asked once; if it returns nothing for one, record
it, do not ask again, try no other source. NO YCharts call, NO Bloomberg call. Nothing built into the product, nothing served, no
claim re-graded, and NO CLASS IS ADMITTED by this cell.

**Why.** Under PRD ADDENDUM v0.39 (read the last section of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`) a type of
security is admitted to the second witness of the date basis only when, over the securities both witnesses carry, its
one-day-off column is EMPTY. IB-pr-441 found five one-day-off security-days in 64,536, in two fund types that are therefore left
out. One of them, the institutional share class (71 securities outside the first witness), is what most of the still-blank
account-days wait on: 6,960 would be freed by it alone. The CTO does not admit it on the smallness of two days. But "one day
off" says the two witnesses DISAGREED, not which was wrong. This cell sets a third dated value beside them.

**The five security-days** are in IB-pr-441's output, `one_day_off_detail` of
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~299/IB138-2_type_overlap_and_fund_check.json` (in your worktree):
MEIIX on 2026-07-02 and MISIX on 2026-10-09 (the institutional class), and SHM on two dates and PZA on one (the fund type whose
share class the source gives as not available). Take the exact five from that file; say `the_five_are_those_of_ib_pr_441: true`
only if yours are those.

**Your instruments** are in your worktree: `~299/` (the overlap measure, the transactions-table read with its Price and trade
date, the one-day-off classifier), `~300/`, `~296/`, `~294/`. Copy what you need into YOUR folder; write nothing into another
worker's folder. The first witness is the Schwab anchor's `closing_price` by CUSIP in its daily partition; the second is the
reader's unadjusted Close (`fetch_yahoo` in `data/assets/scripts/silver/commonwealth_price_basis_census.py`, `read_yahoo_close`
in `data/assets/scripts/silver/commonwealth_daily_valuation.py`); your own cache `C:/dev/_scratch301/yahoo/`; window 2026-06-20
to 2026-10-13. Tolerance: relative 1e-4, and also say "equal to the cent". Scratch is OUTSIDE the worktree and deleted file by
file at the end.

**For each of the five security-days (ticker, date t):**
1. Both witnesses' values for the prior trading day, day t and the next trading day (`first_witness: {prior_day, day, next_day}`,
   `second_witness: {...}`; `null` where a witness has no value, with the reason). Prices of a public security are not client
   data and are written.
2. **A third dated value** (`third_value`): every priced trade (a Buy or a Sale with a Price above 0; say also if a dividend
   reinvestment row exists) of THAT security in the transactions table with a trade date on t or within three trading days either
   side: the trade date, the settle date if the table has one, the kind, the Price (no account, no quantity, no amount). A mutual
   fund's purchase or redemption is struck at its trade date's net asset value; an exchange-traded security's trade price is an
   intraday price and need not equal a close, so say which kind this security is and what its trade price can and cannot tell.
   If no trade exists in that span: `found: false`, `where_looked`, and then the weaker evidence: each witness's own series for
   five trading days either side, and whether one witness's series shows a value REPEATED across two days at t (a carried or
   stale value) while the other moves. Also read the Cottonwood holdings partition's own mark for that security on those days
   (Market Value / Units; the most common value across rows; no account): it is the custodian's mark, not independent, but it is
   a dated value; label it so.
3. **One verdict** per security-day: `FIRST_WITNESS_OFF` (the anchor's value for t belongs to another day),
   `SECOND_WITNESS_OFF` (the reader's bar for t belongs to another day), or `CANNOT_BE_TOLD`; its `claim` (`measured` only where
   a struck trade price or an equally hard dated value decides it; `inferred` where only the series' shape does; `absent` with
   `CANNOT_BE_TOLD` when nothing decides); a one-sentence `reason`; and `deciding_evidence` for any verdict that names a witness.
   Do not prefer either witness. If the evidence points both ways, it cannot be told.
4. Whether day t is a distribution day for that fund, IF the estate already shows it (a dividend or a reinvestment row for that
   security in the transactions table on or beside t); ask no source for distributions.

**The last day.** 2026-10-09 is the window's last trading day. Is the first witness's partition for it actually the prior
day's? Over EVERY security both witnesses carry that has a value in the first witness's 2026-10-09 partition (IB-pr-441 counted
894 securities in all): how many equal the second witness's bar for 2026-10-09 and how many equal its bar for 2026-10-08 (count
only those whose two bars differ), and the partition object's LastModified. Answer `is_the_prior_days` (true, false, or null if
it cannot be told) with its claim. Use bars already implied by IB-pr-441's result where its output carries them; you may not
re-ask the reader for the 890 tickers: if the per-day values are not in `~299`'s outputs, answer from the 2026-10-09 row of its
per-type table (how many security-days of that date read equal, one day off, neither) by re-running its measure over the
first-witness partition and ITS cached classification only if that needs no fetch; otherwise say it cannot be told from what is
on the trunk and why (`is_the_prior_days: null`, claim `absent`).

**Control** (`control.planted` must equal `control.read`): three planted security-days with a struck trade: one where the first
witness is a day late, one where the second is, one where the trade matches neither.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~301/`: `IB140-1_five_days_third_value.json` with
`{the_five_are_those_of_ib_pr_441, security_days:[{ticker, cusip, type_pair, date, first_witness:{prior_day, day, next_day},
second_witness:{prior_day, day, next_day}, custodian_mark:{...}, third_value:{found, values:[{trade_date, settle_date, kind,
price}], where_looked}, series_either_side:{...}, distribution_on_or_beside_the_day, verdict, claim, reason, deciding_evidence}],
verdict_counts:{FIRST_WITNESS_OFF, SECOND_WITNESS_OFF, CANNOT_BE_TOLD}, last_day_first_witness_partition:{is_the_prior_days, claim,
securities_compared, equal_to_second_witness_same_day, equal_to_second_witness_prior_day, last_modified_utc, how_read},
fetch:{calls:[{tickers}], distinct_tickers_asked, tickers_asked_more_than_once:0}, control:{planted, read},
classes_admitted_by_this_cell:0, other_sources_asked:0}`; and a one-page `IB140-1_FIVE_DAYS_THIRD_VALUE_READ.md`: one short
block per security-day with the three-day values of both witnesses, the third value, and the verdict.

<criterion id="IB140-1-AC1" cell_refs="IB-pr-443"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r140/p140_cells.py" . IB140-1-AC1</invocation><expect>IB140-1-AC1 PASS</expect></criterion>
<criterion id="IB140-1-AC2" cell_refs="IB-pr-443"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r140/p140_cells.py" . IB140-1-AC2</invocation><expect>IB140-1-AC2 PASS</expect></criterion>
<criterion id="IB140-1-AC3" cell_refs="IB-pr-443"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r140/p140_cells.py" . IB140-1-AC3</invocation><expect>IB140-1-AC3 PASS</expect></criterion>

<expected_criteria>IB140-1-AC1, IB140-1-AC2, IB140-1-AC3</expected_criteria>

The checks grade that the five are tabled with both witnesses over three days, that each has one verdict with a claim and (where
it names a witness) its deciding evidence, the last-day answer's shape, the one-pass bound and the control. Which witness is off
is UNMEASURED by the issuer; `CANNOT_BE_TOLD` passes as well as a named witness. The three verdict words are this cell's own
output vocabulary for five rows; they are not a contract value and nothing is to be built on them.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file, no PRD, no `sources.json`, no gold script, no ADVI_COTBKF file.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row and report. Never weaken a check; do not edit
  `p140_cells.py`. Do not make a verdict: the evidence makes it.
- **Row ids** are `IRPT_BCKEND-D2-W301-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~301" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~301@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~301 <0.9.0_WK_IRPT_BCKEND~301@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Write no firm name as a literal in any file, and no token beginning `z09` in the two outputs.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~301/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-443.five-one-day-off-days-against-a-third-dated-value.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 132 (round 140, workstream ~P), cell `IB-pr-443`.
<owned_cells>IB-pr-443</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB140-1-AC1, IB140-1-AC2, IB140-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~301/IRPT_BCKEND.TO-IB-pr-443.five-one-day-off-days-against-a-third-dated-value.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: for each of the five security-days, both witnesses over the three days, the third value (or
that none exists and what the series show), any distribution on or beside the day, and the verdict with its claim; the verdict
counts; the last-day answer with its counts; the control; each criterion's last line; the proof checker's result; scratch
deleted; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only measurement of five security-days written to the worker's own deliverables folder; no product file, route, function or served byte.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; S3 reads and one public market-data call through a reader the estate already runs.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p140_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~18:0xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The two named security-days are the CTO's (msg 5501); SHM's and PZA's dates are taken by the worker from IB-pr-441's merged output, not typed here. Rule 24 on the three verdict words: they are a worker output's vocabulary over five rows (two witnesses and the complement), not a contract value; the face says so.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only). Egress: Yahoo Finance through ADVI_COTBKF's existing reader, one call, four tickers. IB-pr-442's drain is in progress at this cut; this cell reads only folders already merged (~299 and earlier; ~300 if present).
</preflight>
