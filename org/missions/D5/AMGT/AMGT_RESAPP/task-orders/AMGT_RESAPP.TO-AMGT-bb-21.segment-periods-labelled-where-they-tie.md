# AMGT_RESAPP task order -- `AMGT-bb-21` -- THE SEGMENT TABLE'S PERIOD AND CURRENCY, LABELLED ONLY WHERE THEY TIE TO STORED REVENUE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-21</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~305</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_D_NOTES.md) -- Of the 76 names with revenue rows, Period 1's top-level sum equals a stored fiscal year's revenue on 72 and does not on 4; none lacks stored revenue. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-305` (branch `wk-AMGT_RESAPP-305`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-305`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-21` (round 78, decomposition s.86)

The stored segment table of a company has five columns named only "Period 1" to "Period 5", and no currency. A careful reader
cannot tell which year a column is. For most companies the column can be named from figures we already hold: when the level-1
rows of a column add up to the company's stored revenue for a fiscal year, that column is that fiscal year. Build the function
that names a column ONLY where that tie holds. It is a pure module: it reads no store.

Create `lib/research/api/segment_period.py` (standard library only) exporting ONE function:

`label_periods(period_sums, revenue_by_year, currency)` returns `{"periods": [...], "currency": <text or None>, "reason": <text or None>}`.
- `period_sums` maps a column number (1 to 5) to the sum of that column's level-1 rows, or `None` when no level-1 row carries
  a value in that column.
- `revenue_by_year` maps a fiscal-year label as stored (text such as "2025") to the stored revenue for that year, in the same
  units as the table.
- `currency` is the company's stored reporting currency (text such as "USD"), or `None`.

Rules:
1. Work through the columns in number order. A column TIES to a year when its sum is a number, the year's revenue is a number
   above zero, and the two differ by 0.5 percent of the revenue or less.
2. When a column ties to more than one year, take the year whose revenue is closest. A year already given to an earlier column
   is not given again: one stored year names one column.
3. Each entry of `periods` is `{"period": <n>, "fiscal_year": <year text or None>, "sum": <the sum or None>, "reason": <text or None>}`,
   one per key of `period_sums`, in number order.
4. A column that ties carries its `fiscal_year` and `reason: None`.
5. A column with a sum that ties to no year carries `fiscal_year: None` and this reason: "The rows of this column do not add up
   to the company's reported revenue for any year we hold, so the year is not stated."
6. A column with no sum carries `fiscal_year: None` and this reason: "No top-level row carries a figure in this column."
7. **Never name a column from its neighbour.** A column that does not tie is not given the year before or after a column that
   does.
8. `currency` in the result is the `currency` handed in when one or more columns tie, and `None` otherwise: the currency is
   stated only when a tie shows the table is in the units of the stored figures.
9. When `revenue_by_year` is empty: every column is unlabelled, `currency` is `None`, and the top-level `reason` is "We hold no
   reported revenue for this company to name these columns from." Otherwise the top-level `reason` is `None`.
10. No sentence uses: identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger,
    bronze.
11. The function reads nothing, calls nothing and does not change its arguments.

Plant tests in `lib/research/api/tests/test_segment_period.py`: a tie, a near miss just outside 0.5 percent, a column with no
sum, the two-columns-one-year case of rule 2, an empty `revenue_by_year`, and a `None` currency with a tie.

You do NOT edit `lib/research/api/scoped_amgt.py` or `lib/research/api/segment_table.py`. Your report names the hookup: the
level-1 sums come from the segment table another cell builds (`segment_table.read_segment_table`), the revenue by year from the
company's stored fiscal-year figures (`SALES_REV_TURN`, scope `fiscal_year_line_item`) and the currency from the stored header
figure `EQY_FUND_CRNCY`; say exactly where each is already in hand when `/thesis` is assembled.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W305-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. `lib/research/api/segment_table.py` is another cell's file: do not create or edit it.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/segment_period.py
lib/research/api/tests/test_segment_period.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~305/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-21"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb21.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>a column that ties is labelled with its fiscal year and the currency is stated; a column that ties to no stored year is not labelled and says why; a column with no sum is not labelled; with no stored revenue nothing is labelled; one stored year is given to one column only; no served sentence uses a system word; C1-C6 PASS; R78 BB21 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-21"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb21.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>AMD's Period 1, summed from the newest stored segment table that carries revenue rows and set against the stored revenue figures, reads fiscal year 2025 in USD; S1 PASS; R78 BB21 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~305 <0.9.0_WK_AMGT_RESAPP~305@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~305/AMGT_RESAPP.TO-AMGT-bb-21.segment-periods-labelled-where-they-tie.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO ruling msg 31077; reads/SEGMENT_PERIOD_LABEL_READ.md. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_D_NOTES.md` (cell D4), committed in the issuance commit's parent. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~305</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @be6b1ad6f7; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads exit 0 and SERVED: YES; built, NOT served this round</status>
