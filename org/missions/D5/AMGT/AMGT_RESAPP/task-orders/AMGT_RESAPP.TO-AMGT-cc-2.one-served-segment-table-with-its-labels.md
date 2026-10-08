# AMGT_RESAPP task order -- `AMGT-cc-2` -- ONE SERVED SEGMENT TABLE WITH ITS PERIOD AND CURRENCY LABELS (FWD-1, CTO MSG 31077)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cc-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~309</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_A_NOTES.md) -- 76 of 85 stored names serve rows; Period 1 ties to stored revenue on 72 and does not on 4; nothing serves the table today. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r79-309` (branch `wk-AMGT_RESAPP-309`, cut from the issuance commit with `--portal-ref d1b21c97`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r79-309`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-cc-2` (round 79, decomposition s.87)

We hold, for 76 companies, Bloomberg's table of revenue by business line. Two pieces were built last round and neither is
served: a reader of the stored table, and a function that names a column of the table with a fiscal year only where the
column adds up to the company's reported revenue. Build the ONE function that puts them together and returns the block the
`/thesis` route will serve under the key `segment_table`. Another cell connects it to the route.

Read first, whole: `lib/research/api/segment_table.py`, `lib/research/api/segment_period.py`, and their tests in
`lib/research/api/tests/`. Do not edit them.

Create `lib/research/api/segment_served.py` exporting ONE function:

`serve_segment_table(security_key, fiscal_year_figures, header_figures, client=None)`

- `security_key`: the company, underscore form (`AMD_US_Equity`, `BP/_LN_Equity`), or None.
- `fiscal_year_figures`: a list of stored figure entries (dictionaries with `scope`, `fiscal_year`, `mnemonic`, `value`,
  `unit`), possibly empty, possibly None.
- `header_figures`: a list of stored header entries (dictionaries with `mnemonic`, `value`), possibly empty, possibly None.
- `client`: a store client, handed on untouched.

It returns a dictionary with EXACTLY these ten keys:

| key | value |
|---|---|
| `status` | `"served"` when revenue rows are served, else `"none"` |
| `rows` | the reader's `rows`, unchanged: each `{"segment", "level", "values"}` with five values, a number or None |
| `operating_income_rows` | the reader's `operating_income_rows`, unchanged |
| `periods` | a list of five column entries (rule 5), or `[]` |
| `period_note` | one plain sentence about how the columns are named, or None |
| `currency` | the reporting currency code, stated only where a column ties (rule 6), else None |
| `units` | the units of the figures in lower case (for example `"millions"`), stated only where a column ties, else None |
| `currency_note` | one plain sentence about the currency and units, or None |
| `reason` | the reader's `reason`, unchanged (None when rows are served) |
| `source` | the reader's `source`, unchanged |

Each entry of `periods` has EXACTLY these five keys: `period` (1 to 5), `label` (`"Fiscal year 2025"` when the column is
named, else `"Period 3"` with its own number), `fiscal_year` (the stored year text such as `"2025"`, or None),
`top_level_sum` (the sum the column was tested with, or None), `note` (None when the column is named, else one plain
sentence saying why it is not).

Rules:
1. **The store is read only through the reader.** Import the module (`from lib.research.api import segment_period,
   segment_table`) and call `segment_table.read_segment_table(security_key, client=client)` exactly ONCE, by that dotted
   name, so a test can replace it. Import no store library and call no store method yourself.
2. **Nothing to show.** When the reader returns no `rows`: `status` is `"none"`, `rows` is `[]`, `operating_income_rows`,
   `reason`, `source`, `period_note` and `currency_note` are the reader's own values, `currency` and `units` are None.
   `periods` is `[]`, except when the reader returned operating income rows: then it is five entries, each
   `{"period": n, "label": "Period n", "fiscal_year": None, "top_level_sum": None, "note": None}`.
3. **The column sums.** For each column n from 1 to 5: take `row["values"][n - 1]` of every row of `rows` whose `level` is
   exactly 1, keep the values that are not None and are larger than 1e-6 in size, and add them. A column with no value kept
   has the sum None. Rows of level 2 and deeper are never added.
4. **The stored figures.** Revenue by year: from `fiscal_year_figures`, every entry that is a dictionary with `mnemonic`
   equal to `"SALES_REV_TURN"`, `scope` equal to `"fiscal_year_line_item"`, a `fiscal_year` that is not None and a `value`
   that is a number (a true/false value is not a number); the key is `str(fiscal_year)`, and the first entry seen for a year
   wins. Keep each year's `unit` beside it. Currency: the `value` of the first entry of `header_figures` that is a
   dictionary with `mnemonic` equal to `"EQY_FUND_CRNCY"` and a non-empty text value, stripped; None when there is none.
   Anything that is not a list, or an entry that is not a dictionary, is passed over without error.
5. **Naming the columns.** Call `segment_period.label_periods(sums, revenue_by_year, currency)` once. For each entry it
   returns, in order: `period` and `fiscal_year` as returned; `top_level_sum` is its `sum`; `label` is `"Fiscal year "` plus
   the year when it has one, else `"Period "` plus the number; `note` is None when it has a year, else the result's own
   top-level `reason` when that is not None (no reported revenue is held), else the entry's `reason`. Never name a column
   yourself and never carry a year from one column to the next: the function you call is the only thing that names one.
6. **Currency and units.** `currency` is the `currency` that call returned (it is None unless one or more columns tie).
   `units` is the stored `unit` of the revenue figure of the lowest-numbered named column, stripped and in lower case, or
   None when no column is named or that unit is not text.
7. **`period_note`**, one of four exact sentences:
   - no reported revenue was held (the call's top-level `reason` is not None): "We hold no reported revenue for this company
     to name these columns from, so they keep Bloomberg's own period numbers."
   - revenue held, no column named: "No column adds up to the company's reported revenue for any year we hold, so the
     columns keep Bloomberg's own period numbers."
   - all five named: "Each column is named with the fiscal year whose reported revenue its top-level rows add up to."
   - otherwise: "A column is named with a fiscal year where its top-level rows add up to the company's reported revenue for
     that year. The other columns keep Bloomberg's own period numbers."
8. **`currency_note`**, one of four:
   - no column named: the reader's `segment_table.CURRENCY_NOTE`;
   - named, currency and units both known: "Figures are in <units> of <currency>, the units and currency of the reported
     revenue these columns add up to." (for AMD: "Figures are in millions of USD, ...");
   - named, currency known, units not: "Figures are in <currency>, the currency of the reported revenue these columns add up
     to; the units are not stated.";
   - named, no currency held: "We hold no reporting currency for this company, so the currency of these figures is not
     stated."
9. **It never raises.** Wrap the whole body: on any exception return `status` `"none"`, `rows` `[]`,
   `operating_income_rows` `[]`, `periods` `[]`, `reason` equal to `segment_table.REASON_FAILED`, and None for the other
   five keys.
10. It does not change its arguments, and it does not change the dictionary the reader returned in a way that alters
    `rows`, `operating_income_rows` or `source`.
11. No sentence uses: identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input
    ledger, bronze.

Plant tests in `lib/research/api/tests/test_segment_served.py`, with a small fake client like the one in
`test_segment_table.py`: one case per rule 2 to 9 (both halves of rule 2; each of the four sentences of rules 7 and 8), a
figures list holding entries of another mnemonic and another scope that must not be counted, arguments left unchanged, and
the reader replaced by a recorder to show it is called once with the client handed in.

You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/api/segment_table.py`,
`lib/research/api/segment_period.py` or their tests. Criterion AC2 reads the real store (read only) and takes about a
minute. Run `lib/research/api/tests/` before your commit and report its last line. Your report states the hookup the adapter
cell must make: the call, its three arguments as they are named in `read_thesis_bundle`, and the served key.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W309-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. `lib/research/api/segment_table.py` and `segment_period.py` are READ, never edited: another cell edits the first.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/segment_served.py
lib/research/api/tests/test_segment_served.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~309/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cc-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc2.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>a column that ties is labelled with its fiscal year with currency and units stated and the rows unchanged; a column that ties to no year and a column with no figure are unlabelled and each says why; with no figures the table is still served unlabelled; nothing to show reads a plain reason and never raises; every answer carries exactly the ten keys and every period entry its five; no served sentence uses a system word; the store is read only through read_segment_table, once; F1-F7 PASS; R79 CC2 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cc-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc2.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>AMD US serves its revenue rows with Period 1 labelled fiscal year 2025 in millions of USD; 8766 JP serves its rows with Period 1 unlabelled and a plain note; a name with no stored table and a stored name with no revenue lines each read their own plain reason; every stored name is served and its Period 1 is labelled exactly when its level-1 rows tie to a stored year (N of N); S1-S4 PASS; R79 CC2 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cc-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc2.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the plant tests of the reader, the period labels and the filing-text breakdown pass; B1 PASS; R79 CC2 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~309 <0.9.0_WK_AMGT_RESAPP~309@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~309/AMGT_RESAPP.TO-AMGT-cc-2.one-served-segment-table-with-its-labels.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO round-78 analysis R1 (FWD-1); CTO ruling msg 31077 (label only where the tie holds). Drafted in `deliverables/2.0.0_SA_COO~Z/round79/GROUP_A_NOTES.md` (cell A2), committed before the cut, in the issuance commit's ancestry. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>79</round>
<slot>0.9.0_WK_AMGT_RESAPP~309</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @bdd1a55638; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads SERVED: YES; 85 of 85 stored names served, 72 labelled, 4 not; row Z-W309-S1 (the stale-hash test) answered by cc-5; served only after cc-6</status>
