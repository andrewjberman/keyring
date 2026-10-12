# ETFS_RIVALS task order -- `RIV-xa-1` -- THE AUDIT PAGE STATES ITS CALENDAR'S DAY AXIS IN VISIBLE TEXT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-xa-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~36</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file(s) (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-xa-1` -- the audit page states its calendar's day axis in VISIBLE text (round 28 analysis section 2.1; RIV-wd-1's repeat clause NOT MET) -- APPENDED 2026-10-12, revision 1.29
- Placement: `ledger/ROUND_ANALYSIS.round28.md` section 2.1 and section 3 item 1 (1.0.0_SA_CTO~DELL1 msg 4558); CVO ADDENDUM 14
  @9d49b613e9, row D1-C-S15.
- Measured (the 2026-10-12 `audit.html`, 13 fund sections): BIDD, CGIC and SCHY each carry a trade window ending 2026-10-02
  (2, 16 and 4 trades) beside a 10-02 calendar cell marked `repeat`. The calendar's day axis (`data-day`, the column header
  `MM-DD`) is the day a report was EXPECTED; the report's own date is in each cell's hover `title` ("report dated ...") only.
  The visible text never names it: the legend paragraph (`render.py:2469`) reads "Calendar legend: new / repeat / regressed
  (older than the previous report) / gap / periodic per day; BBG = Bloomberg, ISS = issuer, HOME = home producer."
- Interface: in `render._render_audit_body`, the legend paragraph gains, after "HOME = home producer.", ONE space and exactly
  this sentence (ASCII; the apostrophe is U+0027): `Each calendar column is the day a holdings report was expected; a cell reads repeat when the report received that day is the same holdings window as the previous report. Trade windows are dated by the report's own date, so a window can end on a day this calendar marks repeat.` It stays in the same `<p class="muted">`. The cell markup,
  the hover titles, the statuses and every other word of the page are unchanged.
- Out of bounds: `render._calendar`, `gold_holdings_coverage.py`, `publish_page.py`, the page's main document, any status
  rule (the classification of repeat is not touched).
- Checks: `round29/checks/xa1_axis_line_check.py` (AC1 and AC2; base FAIL 2). J1 (the CVO's): on the next published audit
  page the sentence reads beside the calendar for BIDD, CGIC and SCHY.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/checks/xa1_axis_line_check.py`. It FAILS at the base (2 failed) and is your target; do
  not edit it. It builds the audit document twice: from a context (`render.render_audit_page`, helpers `_ctx` and `_hc` of
  `tests/test_crorv_layout.py`) and through the real stage (`publish_page.handler_entry`, the `sink` fixture of
  `tests/test_p2_page_grouped_by_fund.py`). The visible text is the document with every tag, attribute and script removed.
- The legend paragraph is one string literal in `render.py` (`_render_audit_body`, about line 2469). Add the sentence to
  that literal and nothing else. The sentence must be BYTE-EXACT as the cell gives it.
- `render.validate_audit(html, n_trades)` must keep reading True on the published page (AC2 asserts it).
## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~36/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search -- inject `search` or the client), any Secrets Manager call, any
environment gate flip outside a test. A row you file goes in the investigation file below with id
`ETFS_RIVALS-D1-W36-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_riv_xa1_axis_line.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- the legend sentence is in the audit document's visible text exactly once, inside the legend paragraph.
- **AC2** -- the same on the page published into a local sink, and `validate_audit` still reads True.
- **J1** -- the CVO's read of the next published audit page, not yours.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xa-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/checks/xa1_axis_line_check.py -k ac1</invocation><expect>1 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-xa-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/checks/xa1_axis_line_check.py -k ac2</invocation><expect>1 passed</expect></criterion>
  <criterion id="J1" cell_refs="RIV-xa-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~36/ETFS_RIVALS.TO-RIV-xa-1.visible-axis-line.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-xa-1.visible-axis-line`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why; rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Round 29 of ETFS_RIVALS, ONE issuance on `ledger/ROUND_ANALYSIS.round28.md` section 3
(msg 4558). Decomposition revision 1.29. Check file(s) dry-run at the base before the cut. Chain B (one file, `render.py`); no edge to another cell.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>29</round>
<workstream>4</workstream>
<slot>~36</slot>
<fabric>dell1</fabric>
