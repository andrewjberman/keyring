# AMGT_RESAPP task order -- `AMGT-ba-3` -- FWD-14, THE LISTS: THE NAMED OWNER ON BOTH LISTS, AND AN OWNER LINE AND OUT-OF-DATE STATEMENT FOR THE /freshness PAGE. NO ALERT IS BUILT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~269</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence. The standing moratorium holds: no alert, mail, topic, notification or checker is built. A line on a page is not one.
comp-iam: DECLARED-NOT-APPLICABLE -- the two list files are packaged in the function's artifact; no store read or write.
comp-adversary: RUN by the issuer at the cut -- both list files read `owner_status` UNASSIGNED (row AMGT_RESAPP-Z-S78; `lib/research/lists/build_lists.py:129` and `:156`). Andrew owns both lists (his word, relayed in CTO msg 30312, record @b5f90bbf8d). Nothing on /freshness names an owner or says whether a list is out of date.
EGRESS CLASS, declared: NONE. No DNS lookup, no vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r77-269` (branch `wk-AMGT_RESAPP-269`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-269`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-3` (round 77, decomposition s.85)

CTO round-76 analysis @c8bbeeac10, enrichment item 8: "FWD-14: the owner line and the out-of-date statement on /freshness
(owner: Andrew, both lists). No alert is built." This cell is the DATA half. The page (cell ba-4) renders what you return;
the adapter cell (ba-11) wires it into the route. You do NOT edit `scoped_amgt.py`.

1. **The owner, on both lists.** In the two committed list files
   (`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/publishers.json` and `social_accounts.json`;
   the build packages these two files into the function) set `owner` to `Andrew` and `owner_status` to `ASSIGNED`. Change
   ONLY those two fields: `reviewed_at`, `review_interval_days` and every entry stay byte-for-byte as they are. A review
   date is the owner's act, not this cell's, so do NOT regenerate the files with the script (it would re-stamp them).
   Then make `lib/research/lists/build_lists.py` emit the same owner and status, so a later regenerate does not undo it.
2. **The statement.** A NEW module `lib/research/lists/owner_line.py` exporting
   `lists_statement(register, now=None) -> dict`. `register` is what `scoped_amgt.read_list_register()` returns:
   `{"lists": {<list name>: {"owner", "owner_status", "reviewed_at", "review_interval_days", "entries_total", ...}}, ...}`.
   It returns:
   - `owner_line`: one plain sentence naming who owns the lists, e.g. "Andrew owns the publisher list and the social
     account list.";
   - `out_of_date`: one plain sentence per list, joined: a list whose `reviewed_at` plus `review_interval_days` is before
     `now` reads "... is out of date: its review fell due on <YYYY-MM-DD>."; otherwise "... is in date: reviewed
     <YYYY-MM-DD>, next review due <YYYY-MM-DD>.";
   - `lists`: per list `{"name", "owner", "reviewed", "due", "out_of_date": bool}` for a caller that wants the parts.
   A register with no list read still returns words for both sentences (say that the lists could not be read), never an
   empty string. Use plain list names ("publisher list", "social account list"). The words a person reads must not
   contain "rot", "register", or a field name.
3. **Plant tests** in `lib/research/lists/tests/test_owner_line.py`.

In your report, name the hookup ba-11 adds (one line: the page view's `lists` argument is
`owner_line.lists_statement(read_list_register())`). Do not add it.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W269-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. No alert, mail, topic, queue, notification or scheduled check (AC3). The statement is read when a person opens the page.
3. No entry is admitted, removed or re-dated in either list. No DNS lookup.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/lists/build_lists.py
lib/research/lists/owner_line.py
lib/research/lists/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/publishers.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/social_accounts.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~269/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1200)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba3.py" --crit AC1; echo "exit=$?"</invocation><expect>both lists name Andrew with status ASSIGNED; review dates, intervals and entry counts unchanged (2 and 267 entries, reviewed 2026-09-10T22:42Z); the generator emits the same owner; C1-C3 PASS; R77 BA3 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba3.py" --crit AC2; echo "exit=$?"</invocation><expect>the owner line names Andrew; the planted list past its interval reads out of date with its due day 2026-07-01; the list in date says so; an unread register still returns words; C1-C5 PASS; R77 BA3 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba3.py" --crit AC3; echo "exit=$?"</invocation><expect>the lists package builds no alert, mail, topic, queue or schedule: 0 lines; C1 PASS; R77 BA3 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~269 <0.9.0_WK_AMGT_RESAPP~269@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~269/AMGT_RESAPP.TO-AMGT-ba-3.lists-named-owner-and-out-of-date-statement.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the two sentences the statement returns on the real list files today;
- the diff of each list file (two fields only), and `lib/research/lists/tests/` last line;
- the hookup line for ba-11;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis @c8bbeeac10 enrichment item 8 (data half); COO adjudication @fb9ca91ad5 section C (row Z-S78 rides this cell). Wave 0, chain A. Checks dry-run at the base: AC1 FAIL as expected (C1 and C3 fail, C2 holds), AC2 FAIL as expected, AC3 PASS as expected. Measured at the cut: publishers 2 entries, interval 90 days, reviewed 2026-09-10T22:42Z; social_accounts 267 entries, interval 30 days, reviewed 2026-09-10T22:42Z. So on 2026-10-07 the publisher list is in date (due 2026-12-09) and the social account list is in date until 2026-10-10: it reads out of date three days after this cut unless the owner reviews it. The list files sit in worker ~5's deliverables folder because the build packages them from there (`build-and-upload-scoped-amgt.sh:219-224`); the paths block grants the two files only.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~269</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @4e5cdb7ff9; proof VALID (worktree checker); both lists name Andrew as owner (ASSIGNED, two fields each, not regenerated); owner_line.lists_statement; AC1 3 of 3, AC2 5 of 5, AC3 no alert-shaped line; lists tests 15 passed</status>
