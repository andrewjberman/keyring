# AMGT_RESAPP task order -- `AMGT-gg-5` -- A PER-DAY PRICE SERIES ON THE TIMELINE ROUTE, READ FROM THE STORED PRICE HISTORY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gg-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~327</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one reader and one optional loader.
comp-iam: RUN at the cut (round82_prep/GROUP_API_NOTES.md item 4a) -- the function's role already reads bloomberg/harvest/bronze/*; no grant moves.
comp-adversary: RUN at the cut -- the timeline route serves no price series today; the stored price history (bronze price_history_px_last, 5 objects, 95 tickers, AMD 276 points) is read only by a reader under integrations/, which the function's package does not carry. AC1 FAILs at the base.
EGRESS CLASS, declared: NONE (stored prices only; never a vendor call).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-327`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-gg-5` (round 82, decomposition s.90)

DSGN's timeline page wants a per-day price series (DSGN round-58 analysis R6). The prices are already stored:
`s3://opal-data-harvest/bloomberg/harvest/bronze/price_history_px_last/date=*/{year_pull,daily_30d}.json`. Read
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/GROUP_API_NOTES.md` item 4a whole first.

1. New `lib/research/price/price_history.py`: a small reader of those stored objects for one security -> a date-ordered list of
   `{date, close}`, the newest object winning on a duplicate date, with its source objects named. It maps the security key to
   the ticker through the crosswalk (`lib/research/identity/crosswalk.py`), never by stripping `_Equity`. Nothing stored -> an
   empty series with a plain reason.
2. `lib/research/harvest/timeline_api.get_timeline` gains an OPTIONAL `price_loader` argument; when given, the timeline body carries `price_series`.
   With no loader, the body is byte-identical to today's.
3. Tests: a new `lib/research/price/tests/test_price_history.py` on plants (ordering, duplicate days, no data, crosswalk mapping).
4. Do NOT edit `scoped_amgt.py`: the one wiring line that passes the loader (~:6728) is the issuer's, at the merge. Name it in
   your report.

Run `lib/research/price/tests/` and `lib/research/api/tests/` before your commit and report each last line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W327-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You never call a price vendor; the stored objects are the only input.

## 3. SURFACES

<paths>
lib/research/price/price_history.py
lib/research/price/tests/test_price_history.py
lib/research/harvest/timeline_api.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~327/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gg-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_timeline.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>the timeline route for the named securities carries a date-ordered per-day price series read from the stored price history; R82 TIMELINE AC1 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~327 <0.9.0_WK_AMGT_RESAPP~327@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~327/AMGT_RESAPP.TO-AMGT-gg-5.a-per-day-price-series-on-the-timeline.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line (api folder on this box: 2 failed at the base, both `No module named 'pypdf'` -- name them, file no row);
- anything your read of the code found that this order did not say;
- any row.
- the exact wiring line the issuer must add in scoped_amgt.py at the merge.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-81 analysis enrichment item 4a (msg 1880). The scoped_amgt.py wiring line is the issuer's at the merge (C10). Check dry-run at the base: AC1 base FAIL as expected. Served only through AMGT-gg-7.

<status>pending</status>
<round>82</round>
<slot>0.9.0_WK_AMGT_RESAPP~327</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
