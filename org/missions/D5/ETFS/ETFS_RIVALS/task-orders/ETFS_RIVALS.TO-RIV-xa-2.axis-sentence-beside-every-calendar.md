# ETFS_RIVALS task order -- `RIV-xa-2` -- THE AUDIT PAGE'S DAY-AXIS SENTENCE SITS BESIDE EVERY CALENDAR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-xa-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~38</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-xa-2` -- the audit page's day-axis sentence sits beside EVERY calendar, inside each fund's own article (round-29 analysis ruling 1; row D1-C-S19; recut of RIV-xa-1) -- APPENDED 2026-10-14, revision 1.30
- Measured (the 2026-10-14 13:00Z page): the sentence is on the page once, in the trades-section legend (`render.py:2471`); the BIDD, CGIC and SCHY
  calendars render 13,384, 19,461 and 20,425 px below it, so with a calendar centred the legend is out of view (3 of 3). Round 28's ruling 2.1 asked
  for the sentence "next to the calendar"; RIV-xa-1 put `render._calendar` out of bounds, so the fault was the cut.
- Interface (`data/etfs/scripts/rivalfunds/render.py` only): a module constant `CALENDAR_AXIS_SENTENCE` holds the sentence EXACTLY as the legend
  carries it today (ASCII; the apostrophe is U+0027): `Each calendar column is the day a holdings report was expected; a cell reads repeat when the
  report received that day is the same holdings window as the previous report. Trade windows are dated by the report's own date, so a window can end
  on a day this calendar marks repeat.` The legend paragraph reads it from the constant and its bytes do not change. `render._calendar(f)`, when it
  renders the calendar table (the `ok` status), returns `<p class="muted" data-calendar-axis>` + the sentence (HTML-escaped as the file's `_e` does) +
  `</p>` IMMEDIATELY BEFORE `<div class="calwrap">`, with nothing between them. When `f.get("calendar")` is empty (the `unavailable` status) `_calendar` is
  unchanged: no sentence, because no calendar renders. The cell markup, hover titles, statuses and every other word of the page are unchanged.
- Out of bounds: the legend's other words, any status rule, `_trades`, `gold_holdings_coverage.py`, `publish_page.py`, every file but `render.py`
  and the cell's one new test file.
- Checks: `round30/checks/xa2_axis_beside_calendar_check.py` (AC1 and AC2; base FAIL 2). J1 (the CVO's): on the served audit page at the production URL
  after the deploy and the next 13:00Z sweep, the BIDD, CGIC and SCHY calendars each have the sentence visible in the same viewport as the calendar
  when the calendar is centred (3 of 3).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xa2_axis_beside_calendar_check.py`. It FAILS at
  the base (2 failed) and is your target; do not edit it. It publishes the audit page into a local sink through the real stage (`publish_page.handler_entry`)
  with G2 coverage rows for TXUE and BASG (two calendars that render) and none for IDVZ (an `unavailable` calendar: it must carry NO sentence).
- `render._calendar` is at `render.py:359`; it has two returns (the `unavailable` div and the `ok` table). The fund block that calls it is `render_fund`
  (`render.py` about line 514): `body = _trades(f, wmax) + _calendar(f) + _fund_checks(f)`. The legend paragraph is the string at about `render.py:2469`
  in `_render_audit_body`. The page total the check expects is one legend copy plus one copy per rendered calendar.
- `render.validate_audit(html, n_trades)` must keep reading True on a published page; `python -m pytest -q rivalfunds/tests` is the regression net.
- The sentence has an apostrophe ("report's"): the check reads the page text after HTML unescaping, so `_e` escaping it is correct.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~38/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search), any Secrets Manager call, any environment gate flip outside a test.
A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W38-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_riv_xa2_axis_beside_calendar.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- every rendered calendar has the sentence once, in its own fund's article, as the paragraph directly before its table; an unavailable calendar has none.
- **AC2** -- the section legend keeps its copy, and the page total is one plus the number of rendered calendars.
- **J1** -- the CVO's read of the served page, not yours.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xa-2"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xa2_axis_beside_calendar_check.py -k ac1</invocation><expect>1 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-xa-2"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xa2_axis_beside_calendar_check.py -k ac2</invocation><expect>1 passed</expect></criterion>
  <criterion id="J1" cell_refs="RIV-xa-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Add `rivalfunds/tests/test_riv_xa2_axis_beside_calendar.py`: one test asserting the constant `render.CALENDAR_AXIS_SENTENCE` equals the sentence above and
that `render._calendar({"calendar": None})` carries no `data-calendar-axis`. Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from
`data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~38/ETFS_RIVALS.TO-RIV-xa-2.axis-sentence-beside-every-calendar.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-xa-2.axis-sentence-beside-every-calendar`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why (none is expected); rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Round 30, workstream `page`, ONE issuance on `ledger/ROUND_ANALYSIS.round29.md` section 3 items 1 and 2 (msg 5567).
Decomposition revision 1.30. Check file dry-run at the base before the cut: xa2 base: FAIL (2 failed) as expected. Chain A (one file, `render.py`); no edge.
Deploy of the page code and the CVO's J1 read at the production URL follow in the round's apply leg (a CloudOps seat), as round 29's TO-APPLY-R29 did.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>30</round>
<workstream>4</workstream>
<slot>~38</slot>
<fabric>dell1</fabric>
