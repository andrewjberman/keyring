# AMGT_RESAPP task order -- `AMGT-ba-11` -- THE ADAPTER CELL: /refresh REMOVED, A REASON BESIDE AN ABSENT AXIS, THE PRINT'S DEAD TEXT STEP CUT, AND EVERY HOOKUP OF THE ROUND

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~277</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read path; /resolve reads the crosswalk the function already loads. The gateway route list changes as TEXT here; applying it is the redeploy order's act.
comp-adversary: RUN by the issuer at the cut -- r77_ba11 AC1 FAILS at the base on every clause (POST /refresh answers 200 "declared"; no /resolve; chatter and price are bare None; the band uses the last settled day; no served sentence carries a translation key); AC3 PASSES at the base (the mount test, 6 passed).
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r77-277` (branch `wk-AMGT_RESAPP-277`, cut from the issuer's tree AFTER every wave-0 cell of round 77 has drained, with `--portal-ref 13509c52`, the portal DEV head at the cut (the api suite reads a portal fixture)). Work and commit only there. Start every shell call with `cd /c/tmp/r77-277`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-11` (round 77, decomposition s.85)

You are the ONLY cell of round 77 that writes `lib/research/api/scoped_amgt.py`. The other cells built their work in their own
modules and are already merged into your base; you connect them and make three changes of your own. Line numbers are as read at
the cut; re-find each by its text.

**(a) PRD v0.41: the re-run button is RETIRED, so the `/refresh` no-op goes** (Andrew's word, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_211xZ_ALL_RECS_APPROVED_CTOZ_OPEN_CALLS_FOUR_CARDS.md`).
- Remove the handler branch `if rest == ["refresh"] and method == "POST":` (about line 6910; it answers 200 with
  `"refresh": "declared"` and does nothing).
- Remove `"POST {0}/refresh"` from `scoped_amgt_route_table()` (about line 7045), and `PULL_ENQUEUE_ROUTE` / `PULL_QUEUE_NAME`
  (about lines 6208-6214) if nothing else reads them (census first, and say what you found).
- A POST to `/refresh` then answers the handler's ordinary 404.
- NOT touched: `refresh_freshness_snapshot`, `SCHEDULED_ACTIONS` and the scheduled event. They are the /freshness snapshot's
  writer and share only the word.

**(b) Row Z-S278: a reason beside an absent chatter or price axis.** In `read_security_overlay`'s bundle (about lines
3467-3468) `chatter` and `price` are `by_axis.get(...)`: a bare `None` when the axis has no row, on a payload whose other blocks
each say why they are absent. Add two fields beside them, `chatter_absent_reason` and `price_absent_reason`:
- when the axis value is `None`: the plain `absent_reason` the matching `axis_reads` entry already carries (the same lookup
  `breakout_miss` uses at about line 3447), or, if that entry has none, a plain sentence saying no ranking row is stored for this
  name on that axis;
- when the axis value is present: `None`.
`chatter` and `price` themselves keep their values and types. Do the same for `breakout_price` only if it is free (one more
field, `breakout_price_absent_reason`); say which you did.

**(c) Row Z-S218: the print route does only the work its response needs.** `_print_pack` (about line 7005) runs
`pdf_path, _ = build_pack(display_form, block)` and returns the PDF only. `lib/research/print/render_pack.py build_pack`
(line 631; the text step is at about lines 750-758) re-reads the finished PDF with pypdf and writes a `.txt` on EVERY call,
0.22-0.40 s that the served route throws away.
- First CENSUS every caller of `build_pack` and every reader of its `txt_path` across the repository, and list them in your
  report.
- Then give `build_pack` a keyword (default: the text step still runs, so every other caller keeps its bytes) that skips the
  pypdf text step, and have `_print_pack` pass it. `build_pack` still returns a 2-tuple. Touch ONLY `build_pack`'s signature
  and that text step in `render_pack.py`: `build_rich_text` and the export path were changed by another cell of this round and
  are already in your base. One plant case in `lib/research/print/tests/test_ba11_skip_text_step.py`.
- Bodies EQUAL: before any edit, capture the PDF route's body for BA_US_Equity, AMD_US_Equity and ASML_NA_Equity into
  `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~277/before/`. Write
  `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~277/print_equal.py`, which rebuilds the three and prints
  `EQUAL n of 3`. Compare the PDFs' page count and extracted text (a PDF carries its creation time, so raw bytes may differ; say
  which comparison you used and why).

**(d) THE HOOKUPS.** Each is one call or one entry; the module already exists in your base.

HOOKUPS (appended by the issuer at the cut)
1. AMGT-ba-8 -> `_overlay_top_band` (about line 3295): replace the `prev_trading_day` day and the `top_band.news_items(rows, day)`
   call with `top_band.news_items_newest(rows, asked)` where `asked` is the date already parsed from `as_of_date` (today when
   none is asked for). Keep the two plain-reason fallbacks (no matched company; the read did not complete). Fix the docstring.
2. AMGT-ba-9 -> a new route `GET {prefix}/resolve?q=`: in the handler, beside the `/freshness` and `/lists` branches (about line
   6903), answer `_response(200, name_search.resolve_query(q))` with `q` from the query string (a missing `q` is the empty
   query). Add `"GET  {0}/resolve"` to `scoped_amgt_route_table()` where `/refresh` was, and in
   `infra/aws/terraform/harvest/scoped-amgt-api.tf` swap the list entry `"POST /api/scoped/amgt/refresh"` (line 548) for
   `"GET /api/scoped/amgt/resolve"`, with a one-line comment naming this order. The non-greedy count stays 18, so the file's
   construction check still holds. You edit the TEXT only: no `terraform` command of any kind.
3. AMGT-ba-10 -> every served drafted sentence: merge `translated_text.served_translation(sentence)` into the served sentence
   dict at each site ba-10's report lists (the sections builder at about lines 2962-2970 is one). The original `text` is
   untouched.
4. AMGT-ba-1, ba-2, ba-3 -> the /freshness route (about line 6905, `return _response(200, serve_coverage_freshness())`). The plain
   `GET /freshness` answers exactly as today. With `?view=page` it returns
   `page_body.page_view(view, annotate=lambda row: stale_rule.annotate_row(row, today), lists=owner_line.lists_statement(read_list_register()))`
   where `view` is `serve_coverage_freshness()`, `today` is today's UTC date, and the imports are `lib.research.freshness.page_body`,
   `lib.research.freshness.stale_rule` and `lib.research.lists.owner_line`. The annotation runs at SERVE time; the stored snapshot
   stays the unannotated view.
5. AMGT-ba-6 -> the `thesis_driver_chart` filing branch (about line 3880): call
   `table_class.driver_refusal(thesis_driver, <the first point's passage text>)`. When it is not None, return `status: "ABSENT"`
   with `plain_reason` set to the refusal, `refused: True` and `points: []`.
6. AMGT-ba-6 -> `read_segment_breakdown` (about line 3778): call `table_class.segment_refusal(rows)`. A refused analysis is not
   `best`; if every analysis is refused, return `{"rows": [], "reason": <the refusal>, "source": None}`.
7. AMGT-ba-7 -> the `/thesis` body (about line 3678):
   `bundle["passage_coverage"] = section_coverage.read_section_coverage(resolved_key or security_key, _pool_client, pool_reader.POOL_BUCKET)`.
   The import for 5-7 is `from lib.research.filings import section_coverage, table_class`, beside the import at about line 131.
8. AMGT-ba-15 -> `lib/research/identity/build_universe.py` (about line 145): return
   `one_pager_precedence.ordered(folder_path, matches)` in place of `sorted(matches)`, with the import from
   `lib.research.identity.one_pager_precedence`. This is the one hookup outside `scoped_amgt.py`.
Verify every line reference at your base before you edit; the names are the contract, the numbers are a guide.

**AMENDMENT 1 (issuer, from the nine exporters' drained reports, before the spawn). Where it differs from a hookup above, this binds:**
- **Hookup 1 (ba-8).** Call `top_band.news_items_newest(rows, as_of)` with `as_of` the SAME date the caller passes today as
  `day` (the last settled trading day; the function reads no clock; `window_days` defaults to 30). `rows` must be the name's
  gold mention rows for the WHOLE 30-day window ending at `as_of`: the caller's read fetches one day today, so widen that read
  to the window, or the rule cannot find an older day. `top_band(description, news)` is unchanged and still passes `day`,
  `items`, `items_reason` and `items_without_link`.
- **Hookup 2 (ba-9).** `name_search.resolve_query(q)` answers 200 for all three statuses (`exact`, `candidates`, `none`). It
  RAISES when the crosswalk cannot be loaded: answer that as a 500 with a plain reason, never as `none`.
- **Hookup 3 (ba-10).** TWO sites take `**translated_text.served_translation(sentence)`: the sections builder (about lines
  2962-2970) and the description header (about lines 5152-5160; it copies named fields, so it needs its own merge). The
  read-boundary re-check (about lines 2793-2807) serves nothing and takes none.
- **Hookup 3b (issuer ruling on ba-10's finding).** The served chart object `thesis_driver_chart` is built from `series`,
  `unit`, `points` and `resolution` only, so it drops the stored driver's translated fields. Where the stored driver carries
  them, the chart also serves `series_translated`, `unit_translated` and `why_translated` as ADDED keys beside the originals
  (null when the driver has none). No existing key changes.
- **Hookups 5-6 (ba-6).** The first point's passage text is `points[0].get("passage_text") if points else None`.
- **Hookup 7 (ba-7).** `read_section_coverage` takes an optional `passage_map=`: pass the analysis passage map when it is
  already in hand, which saves a read. The block carries `sections`, `not_covered`, `passages_outside_sections`, `source` and
  `reason`, and it never raises.
- **Hookup 8 (ba-15).** In `build_universe.py` the change is the last line of `_find_one_pager_files` (about line 145).
- **One deployed-shape check to add to your report** (not a criterion): the body of `GET /freshness?view=page` on your local
  adapter: its size in bytes, its row count, the stale count, and the owner line. ba-2 measured 22,855 B and 95 rows on the
  module alone; ba-1 measured 3 stale of 95.

For each hookup: the import is lazy or at module scope as the neighbouring code does it; a module a hookup needs that is ABSENT
from your base is a BLOCKING row for that hookup only, and you finish the rest.

Run `lib/research/api/tests/` before your commit and report its last line (fix a test only where this order changed the behaviour it asserts, and list each one). If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W277-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no `terraform` command, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. No existing /overlay, /thesis or print field changes value. The changes are: one route removed, one route added, and ADDED fields.
3. The other cells' modules are called, never edited. A defect you find in one is a row, not a patch.
4. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
5. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/print/render_pack.py
lib/research/print/tests/test_ba11_skip_text_step.py
lib/research/api/tests/
infra/aws/terraform/harvest/scoped-amgt-api.tf
lib/research/identity/build_universe.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~277/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-11"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba11.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>POST /refresh answers 404 and is off the route table; GET /resolve answers a name and an exact form; every absent chatter or price axis carries its reason; every top band shows the newest news day in 30 days or "No news in the last 30 days"; every served sentence carries the three translation keys; C1-C5 PASS; R77 BA11 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-11"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~277/print_equal.py"; echo "exit=$?"</invocation><expect>EQUAL 3 of 3; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-11"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba11.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the mount test passes: the route table and the gateway route list agree after the swap; R77 BA11 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~277 <0.9.0_WK_AMGT_RESAPP~277@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~277/AMGT_RESAPP.TO-AMGT-ba-11.the-adapter-cell.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line, and each test you changed and why;
- the `build_pack` caller census and the print time before and after on the three names;
- each hookup: done, or the row that blocks it;
- the gateway route change the redeploy order must carry (one route removed, one added);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** RISK is WORLD by the gate's path floor only (one `infra/` text line); this order applies nothing and runs no `terraform` command; the apply is ba-20's, under its pair. CTO round-76 analysis items 7 and 10; PRD v0.41 (ADDENDUM E); COO adjudication @fb9ca91ad5 section A rows Z-S278 and Z-S218. Wave 1: spawned only after every wave-0 cell drains, because every hookup's module must be in its base. The `/refresh` -> `/resolve` gateway swap makes the round's redeploy NOT code-only: its pair must name one route removed and one added. The portal client's `refresh` call (`portal/src/api/endpoints/amgt*.ts`, about line 132) and its control are the page lane's. Checks dry-run at the base: ba-11 AC1 base FAIL as expected; AC2 is the worker's own script (absent at the base, FAIL as expected); AC3 base PASS as expected.

<status>staged</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~277</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
