# ETFS_RIVALS task order -- `RIV-ml-1` -- ROUND 19 (REPAIR): THE MONTH-BY-MONTH BUYING STRIP LABELS EACH CELL WITH THE MONTH IT IS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ml-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~9</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (two render functions and one stylesheet string)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check file and the round-18 real-run record
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). **This order, round 19, is one small repair of that strip.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ml-1` -- the month-by-month buying strip labels each cell with the month it is (FWD-23; row Z-S58)
- Measured (round-18 real run, day 2026-10-06): the page holds 393 month strips, every one labelled January to December
  by cell position; gold buying_trend's `trend_mark` months run from the window start's month, oldest first, through the
  page day's month. 248 of 349 R365 rows carry 13 month tokens (the strip draws the first 12 and drops the newest); the
  R30 and R90 strips (2 and 4 cells) read "Jan, Feb" for September and October.
- Interface: `render._month_chart(mark, end=None)` and `render._month_words(mark, end=None)`. `end` is the trend row's
  `window_end` (ISO string or date). With `end`: the LAST token is `end`'s month and each earlier token one month before;
  at most the last 12 tokens are drawn or named; every cell carries its month as `data-m=<Jan..Dec>`. With `end` None:
  tokens are labelled from January, as before, and each cell still carries `data-m`. `render.MONTH_CSS` prints the label
  from the cell (`content:attr(data-m)`); the twelve positional rules go. Every call site passes the trend row's
  `window_end` (the dialog's buying section and the sector tag's hover words).
- Rulings at the cut (issuer): the month is counted back from `window_end`, never forward from `window_start` (a clipped
  window's start is not its mark's first month on every row). A row with no `window_end` gets the legacy labels. No
  year is printed: at most 12 cells, so a month name is unique in a strip. The audit page is untouched unless it draws
  the same strip through the same function.
- **Organic trigger:** any fund panel's trend and any security dialog on the live page; the issuer's real run reads the
  strips against the listed trades.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 5be2c73b12 or later)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ml-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where the docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- `render.py` today: `_MON` is the twelve short month names; `_month_words(mark)` (near line 1161) and `_month_chart(mark)` (near line 1167) label by position; `MONTH_CSS` (near line 1180) writes one `.rf-months i:nth-child(n)::before{content:"<Mon>"}` rule per month plus the bought / sold / no trade / no data words, which stay. The two call sites are near lines 1195 (`_month_words(r.get("trend_mark"))`) and 1756 (`_month_chart(tr.get('trend_mark'))`); the trend rows they read come from gold buying_trend, whose columns include `window_start`, `window_end` and `trend_mark`.
- In gold, `gold_buying_trend._months(day, start)` writes the mark's months from the window start's month through `day`'s month, oldest first; read it (do not edit it) to confirm the last token is the row's `window_end` month. If you find a row shape where that is not so, file one row and build to the ruling.
- A cell is written without quotes today (`<i class=u></i>`); keep the page's byte budget in mind: `data-m=Oct` unquoted is 11 bytes a cell.
- Existing package tests pin the old strip markup and the old positional CSS in places; re-pin them and say which in the report.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~9/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r19ml1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the strip and the hover words count months back from the window end, keep the last 12, carry each label on the cell; the stylesheet prints it from the cell; pd-2.AC1, pd-2.AC2 and md-1.AC2 still PASS; control: with no end the legacy labels hold (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ml-1.AC1.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run, never by you): on the real page a strip's bought and sold months are the months of the trades listed beside it.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ml-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ml-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-ml-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~9/ETFS_RIVALS.TO-RIV-ml-1.the-month-strip-labels-each-cell-with-the-month-it-is.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ml-1.the-month-strip-labels-each-cell-with-the-month-it-is`. Report once: the mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; each call site and the value it now passes as `end`; what you read in gold about the mark's last month; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.9 (round 19 appended). Source: row ETFS_RIVALS-Z-S58 @3a0526171e (BLOCKING, INERT), ruled by the issuer inside cell RIV-pd-2's surface: no ENDPOINT text changes. Chain `~9`, slot `~9`, position 1 of 1. Check written and dry-run at base 5be2c73b12 by the issuer: ml-1.AC1 FAIL 5 failures as expected (arms a to e; arm f and the control g PASS).

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>19</round>
<slot>~9</slot>
<fabric>site-z</fabric>
<status>complete</status>
