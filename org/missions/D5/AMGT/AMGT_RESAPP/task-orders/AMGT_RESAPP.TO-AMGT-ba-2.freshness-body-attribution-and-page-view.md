# AMGT_RESAPP task order -- `AMGT-ba-2` -- THE /freshness BODY: ATTRIBUTE ITS BYTES BY FIELD, THEN BUILD THE PAGE VIEW THAT CARRIES ONLY WHAT THE PAGE RENDERS (CTO RULING 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~268</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one measurement and a pure projection module.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the /freshness view the function already serves; no new read path.
comp-adversary: RUN by the issuer at the cut -- the round-76 walk read /freshness in 2,665 ms for a 1.07 MB encoded body (round 75: 694 ms), while the cold route answers in 660-1,047 ms. The issuer's own read of deployed OVpDhfwD: 2,889,557 bytes decoded, 302 rows of which 95 are covered, and the `reads` records are 2,758,266 of those bytes. Your measurement confirms or corrects that; it is not taken on the issuer's word.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r77-268` (branch `wk-AMGT_RESAPP-268`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-268`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-2` (round 77, decomposition s.85)

CTO round-76 analysis @c8bbeeac10, ruling 3: "A round-77 measurement cell before any cut. Attribute the body's bytes by field
... Then serve the page only the fields and rows it renders." Two steps, in this order.

**Step 1 -- the measurement (before any code).** Read the /freshness body the DEPLOYED function serves (a direct invoke of
`opal-amgt-scoped-api` with the GET-shaped event the round-75 check uses:
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py` `_event`). Write
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~268/BODY_ATTRIBUTION.json`:
- `measured_on` (the function's CodeSha256) and `measured_at` (UTC);
- `total_bytes` (the decoded body) and `encoded_bytes` if you can read the gzip size;
- `by_top_level`: bytes per top-level key, summing to the total within 1%;
- `by_reads_record`: bytes per record inside `reads`, and inside the largest record, bytes per field;
- `by_row_field`: bytes per row field across all rows;
- `rows_total`, `rows_covered`, and the bytes of the covered rows against the others.
Write `BODY_ATTRIBUTION.md` beside it: the table, and ONE sentence naming where the bytes are.

**Step 2 -- the page view.** A NEW module `lib/research/freshness/page_body.py`. You do NOT edit `scoped_amgt.py`; the
adapter cell (ba-11) wires the route. The default /freshness body must stay exactly as it is: the round-75 pin (c59)
compares its rows, and /overlay reads the same view.

**Exports** (the names are the contract):
- `PAGE_ROW_FIELDS`: the row fields the page renders: `covered`, `name`, `security_key`, `last_refreshed`, `per_input`, `pack`.
- `page_view(view, annotate=None, lists=None) -> dict`: a NEW dict holding
  - `rows`: one entry per COVERED row of `view`, in served order, carrying `PAGE_ROW_FIELDS` with values EQUAL to the source
    row. When `annotate` is given (a callable `row -> row`, cell ba-1's `stale_rule.annotate_row` bound to today), each row
    is passed through it and the fields it adds are kept;
  - `generated_at`, `snapshot` and `snapshot_fallback` where the view has them;
  - `denominators`: only `covered_names` and `covered_read_error`;
  - `lists`: the `lists` argument as given (cell ba-3's owner line and out-of-date statement), omitted when None;
  - NO `reads`, no per-row `rot`, `source`, `reason` or `security_key_basis`.
  It never changes `view` in place.

**Plant tests** in `lib/research/freshness/tests/test_page_body.py`: covered rows only; kept values equal; `reads` absent;
`annotate` and `lists` passed through; the source view unchanged.

In your report, name the hookup ba-11 adds: the route answers `GET /freshness?view=page` with `page_view(...)` and answers
the plain `GET /freshness` exactly as today. Do not add it.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W268-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. The default /freshness body is unchanged (AC3). Nothing is removed from it in this cell.
3. The deployed read in step 1 is read-only: GET-shaped invokes only.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/freshness/page_body.py
lib/research/freshness/tests/test_page_body.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~268/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba2.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>the attribution file states the total, the per-key bytes summing to it within 1%, the row fields and both row counts, and names the body measured; C1-C3 PASS; R77 BA2 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba2.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>the page view holds exactly the covered rows, no read records, every kept field EQUAL to its source row, within 150,000 bytes; C1-C5 PASS; R77 BA2 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba2.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the default body still carries the read records and every row; C1 PASS; R77 BA2 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~268 <0.9.0_WK_AMGT_RESAPP~268@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~268/AMGT_RESAPP.TO-AMGT-ba-2.freshness-body-attribution-and-page-view.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the attribution table (top-level keys, the largest `reads` record and its largest field), and the page view's size against the full body;
- the hookup line for ba-11;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis @c8bbeeac10 ruling 3, enrichment item 2. Wave 0, chain A. Checks dry-run at the base: AC1 FAIL as expected, AC2 FAIL as expected, AC3 PASS as expected. Measured at the cut on OVpDhfwD (00:3xZ 10-07): body 2,889,557 B; top-level `reads` 2,758,266 B (seeking_alpha_bronze 2,139,211; bloomberg_bronze 611,254), `rows` 130,333 B (covered 43,965; other 85,764), all else under 1 KB; rows 302, covered 95. The analysis says 242 keys; the route returns 302 rows, so the count is the worker's to restate. The trim is a SEPARATE view (`?view=page`), never a cut of the default body: r75 c59 and /overlay's input_provenance read the default.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~268</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @e3861fc456; proof VALID (worktree checker); the /freshness body attribution (2,889,557 B; reads 95.5%, of which one last_modified map is 2,139,028 B) and page_body.page_view (22,855 B, 95 rows, kept fields equal 95 of 95); default body unchanged</status>
