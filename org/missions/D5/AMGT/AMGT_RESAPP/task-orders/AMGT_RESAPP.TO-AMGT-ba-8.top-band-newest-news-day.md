# AMGT_RESAPP task order -- `AMGT-ba-8` -- THE TOP BAND SHOWS THE NAME'S NEWEST NEWS DAY INSIDE 30 DAYS, DATED (FWD-16, RULING 5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~274</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a pure function and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no store read or write; the rows are handed in.
comp-adversary: RUN by the issuer at the cut -- on deployed OVpDhfwD the band served 3 news items across 95 names on 2026-10-05 (row Z-W263-S1); r77_ba8 AC1 FAILS at the base (no `news_items_newest`), AC2 PASSES (23 plant cases).
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r77-274` (branch `wk-AMGT_RESAPP-274`, cut from the issuance commit with `--portal-ref 13509c52`, the portal DEV head at the cut (the api suite reads a portal fixture)). Work and commit only there. Start every shell call with `cd /c/tmp/r77-274`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-8` (round 77, decomposition s.85)

CTO ruling 5 (round-76 analysis @c8bbeeac10). Today `lib/research/api/top_band.py news_items(rows, day)` counts only articles
published on ONE day the caller picks (the last settled trading day). Most names have no item on any given day, so the band is
nearly always empty. The rule becomes: **the band shows the name's NEWEST day with news inside the last 30 days, dated.**

Add to `lib/research/api/top_band.py`, as a pure function (no store read, no clock read; the caller hands in the date):

`news_items_newest(rows, as_of, window_days=30)` returns `{day, items, items_reason, items_without_link, window_days}`.
1. Among the name's rows published on a UTC day from `as_of - window_days` to `as_of` inclusive, find the NEWEST day that has at
   least one followable article (a non-empty `url` and `title`). Serve that day's items exactly as `news_items` does today: the
   same item fields, most-discussed first, then newest, capped at `ITEMS_CAP`. `day` is that day as an ISO date.
2. If no day in the window has a followable article, serve `items: []`, `day: None` and `items_reason` EXACTLY
   `"No news in the last 30 days"` (the number is `window_days`). The same for a name with no rows at all. Never an empty band
   with no words, and never yesterday's absence shown as today's fact.
3. `items_without_link` counts the unfollowable articles inside the window. `window_days` is echoed.
4. `news_items(rows, day)` stays as it is (its 23 plant cases still pass). `top_band(description, news)` needs no change; if you
   add a key to the band, add it there and say so in your report.

Add plant cases for the new function to `lib/research/api/tests/test_top_band_provenance.py`.

**You do NOT edit `lib/research/api/scoped_amgt.py`.** The call site (`_overlay_top_band`, about line 3295, which today computes
`prev_trading_day` and calls `news_items`) is switched to your function by the round's adapter cell, AMGT-ba-11. Your report names
the exact hookup: the function, its arguments, and what the caller passes for `as_of`.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W274-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. No existing function changes its answer; only the one added function (and any band key you report).
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/top_band.py
lib/research/api/tests/test_top_band_provenance.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~274/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba8.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>the newest followable news day inside 30 days is chosen and ordered; older-only and no-row names read "No news in the last 30 days"; C1-C4 PASS; R77 BA8 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba8.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>every plant case in test_top_band_provenance.py passes (the 23 of round 76 plus yours); R77 BA8 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~274 <0.9.0_WK_AMGT_RESAPP~274@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~274/AMGT_RESAPP.TO-AMGT-ba-8.top-band-newest-news-day.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the hookup the adapter cell needs (function, arguments, the `as_of` the caller passes);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis item 4, ruling 5; row Z-W263-S1. The call-site switch is AMGT-ba-11's hookup; the page work rides DSGN round 45. Checks dry-run at the base: ba-8 AC1 base FAIL as expected, AC2 base PASS as expected.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~274</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
