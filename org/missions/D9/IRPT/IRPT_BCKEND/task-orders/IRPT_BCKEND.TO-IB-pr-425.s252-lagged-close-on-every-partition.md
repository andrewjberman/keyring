# TO IRPT_BCKEND.TO-IB-pr-425 -- row S252 measured on EVERY trading-day partition of Cottonwood's declared holdings source: which securities carry the prior day's close, on how many days (read only)

<to_id>IRPT_BCKEND.TO-IB-pr-425</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~284</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>123</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 4729 (FWD-3's Cottonwood thread is row S252, measured whole), on this seat's read `deliverables/2.0.0_SA_COO~P2/FWD3_COTTONWOOD_WAITS_ON_AND_CANONICAL_HOLDINGS_READ_20261011.md` @e13ac2fcf7 | **Decomp cell:** `IB-pr-425` (decomposition section 116) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-284/` (bash `/c/dev/wk-irpt-bckend-284`). Work only there. **READ ONLY: S3 reads and local analysis. No
write to AWS, no deploy, no product source edit, no vendor call.**

**The question.** Cottonwood's declared holdings source is `opal-data-assets`, prefix
`blackdiamond/<scope>/silver/fact_holdings/date=YYYY-MM-DD/` (entry `blackdiamond_z09` of
`data/assets/scripts/gold/irpt_holdings_performance/sources.json`; resolve `<scope>` the way the gold script does, never by typing a
firm name into a file). Its declared basis is one close per partition, `OWN_DATE`, basis `inferred`. Row IRPT_BCKEND-S252 found, on 10 of
81 partitions, that a minority of securities carry the PRIOR trading day's close: on five of the ten days, 3.4 to 5.9 percent of the
securities that moved. Nobody knows which securities, or what the other partitions read. The holdings gold cannot be served for
Cottonwood until that minority is identified and stated. Measured by the issuer today: the prefix holds 91 dated partitions,
2026-06-09 to 2026-10-09, with 86 of 86 trading days present.

**Method -- reuse, do not reinvent.** Read first:
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/HOLDINGS_SOURCE_DATE_BASIS_READ_20261001.md` and its instruments in that folder,
above all `partition_close_anchor_sweep.py` (EVERY trading-day partition of a range, graded against the Schwab own-date close) and
`partition_close_anchor.py`. Copy what you need into your deliverables folder and extend the copy; leave the originals untouched. The
price is Market Value over Units (PRD v0.19 ruling 4). A security "moved" on day D when its ANCHOR close on D differs from its anchor
close on the prior trading day; only moved securities can tell an own-date close from a prior one. Trading days come from
`lib/trading_calendar.py`.

**Build:**
1. **Every trading-day partition.** List the prefix (auto-paginate; count client-side) and grade EVERY trading-day partition in it, not
   a sample. For each day D with a prior trading-day partition: among the securities that moved on D and are priced in the partition,
   count those at D's own anchor close, those at the prior trading day's close, and those at neither. Use the tolerance the existing
   instrument uses and state it.
2. **Which securities.** For every security that reads the prior close on at least one day: its identifier (ticker or CUSIP; a security
   identifier is not client data), its class as the source or the anchor names it (fund, equity, ETF, bond, cash, other), the number of
   days it read the prior close and the number of days it moved. Say whether the lagged set is the SAME securities day after day or a
   changing one, and whether one class explains it.
3. **A control.** A small synthetic fixture with ONE planted lagged security and one clean copy; the instrument must report the planted
   one alone, and nothing on the clean copy.
4. **Output** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~284/IB123-1_s252_all_partitions.json`:
   `{source:{bucket, prefix_template, anchor}, tolerance, partitions_listed, trading_day_partitions_listed,
   days:[{date, state:"GRADED"|"FIRST_DAY_NO_PRIOR"|"UNGRADEABLE", reason, moved, own_close, prior_close, neither}],
   lagged_securities:[{security, class, days_lagged, days_moved}], lagged_by_class:{class:count},
   control:{planted, reported:[...], clean_fixture_reported:[...]}}`. For a GRADED day, `own_close + prior_close + neither == moved`.
   `sum(days_lagged)` over the securities equals `sum(prior_close)` over the graded days.
5. **A one-page read** `IB123-1_S252_READ.md` beside it, for the CTO: the share of moved securities at the prior close per day (min,
   median, max, and the count of days above 1 percent); the classes; the top securities by days lagged; whether the minority is stable;
   what a "neither" security is, if you can tell; and what you did NOT measure. Standard technical English, short sentences.

**Client data.** Position rows carry account ids and balances. NONE of that goes in any file you commit: counts, security identifiers,
classes, dates and percentages only. Downloaded partitions stay OUTSIDE the worktree (for example `C:/dev/_scratch284/`) and are deleted
file by file at the end; report what remains.

<criterion id="IB123-1-AC1" cell_refs="IB-pr-425"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r123/p123_cells.py" . IB123-1-AC1</invocation><expect>IB123-1-AC1 PASS</expect></criterion>
<criterion id="IB123-1-AC2" cell_refs="IB-pr-425"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r123/p123_cells.py" . IB123-1-AC2</invocation><expect>IB123-1-AC2 PASS</expect></criterion>
<criterion id="IB123-1-AC3" cell_refs="IB-pr-425"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r123/p123_cells.py" . IB123-1-AC3</invocation><expect>IB123-1-AC3 PASS</expect></criterion>

<expected_criteria>IB123-1-AC1, IB123-1-AC2, IB123-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Read only on AWS (`.tools/aws` shim). Do not edit `sources.json`, the gold script,
  or the instruments in `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/`.
- **Do not propose or make the declaration change.** This cell measures. What the basis is declared as is the CTO's ruling on your read.
- **Refusal clause:** if a partition cannot be graded, it is a day row with `state: "UNGRADEABLE"` and its reason, never a dropped
  day. If the anchor does not cover a date range, say which and stop short of it rather than grading against something else. If a
  criterion cannot be met as written, stop, file a row and report. Never weaken a check; do not edit `p123_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W284-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~284" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~284@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~284 <0.9.0_WK_IRPT_BCKEND~284@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~284/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-425.s252-lagged-close-on-every-partition.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 116 (round 123, workstream ~P), cell `IB-pr-425`.
<owned_cells>IB-pr-425</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB123-1-AC1, IB123-1-AC2, IB123-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~284/IRPT_BCKEND.TO-IB-pr-425.s252-lagged-close-on-every-partition.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: partitions listed and graded; the per-day share at the prior close (min, median, max, days above 1
percent); the number of lagged securities and their classes; the five securities with the most lagged days; whether the set is
stable; each criterion's last line; the proof checker's result; any row ids; what scratch remains.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only measurement; nothing is built, deployed or written to AWS.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p123_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~10:5xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no output file); commit-gate clean.
lane: the <paths> block IS the grant; ~P's holdings-basis thread.
</preflight>
