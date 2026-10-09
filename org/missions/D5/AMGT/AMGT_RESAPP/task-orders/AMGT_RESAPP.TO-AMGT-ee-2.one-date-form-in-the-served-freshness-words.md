# AMGT_RESAPP task order -- `AMGT-ee-2` -- ONE DATE FORM IN THE SERVED /freshness WORDS: THE HOUSE LONG FORM IN THE SENTENCES, ISO IN THE FIELDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ee-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~319</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one helper, two sentence builders, their tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no read or write path changes.
comp-adversary: RUN at the cut -- the served /freshness words carry ISO days ('Seeking Alpha last read 2026-09-22.', 'reviewed 2026-09-10, next review due 2026-12-09'; row AMGT_RESAPP-D1-S1) while the page draws its own days in the house long form. No date helper exists under lib/ (comp-find, 0 of 693 files). AC1 FAILs at the base, AC2 PASSes.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-319`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ee-2` (round 81, decomposition s.89)

The /freshness page prints the server's sentences as served, and the page's own days are in the house long form
(`September 22nd, 2026`: the date part of `formatDateWithOrdinal` in `portal/src/lib/dateUtils.ts`). The server's sentences still
carry `YYYY-MM-DD`, so one page shows two date forms. Put the sentences in the long form; keep every structured date field ISO.

1. New `lib/research/freshness/long_day.py`, standard library only, with `long_day(value)`: a string starting `YYYY-MM-DD` (a bare
   day or an ISO timestamp, whose first ten characters are read as the day, no time-zone shift) -> `<Month> <day><st|nd|rd|th>,
   <YYYY>` (1st, 2nd, 3rd, 4th-20th, 21st, 22nd, 23rd, 24th-30th, 31st; 11th, 12th and 13th take th). Anything else, `None`
   included, is returned unchanged.
2. `lib/research/freshness/collector_record.py`: the `read` sentence (`Seeking Alpha last read %s.`, ~:92) and the `checked`
   sentence (~:96) take `long_day(...)` of the same day. `last_read` and the other fields stay as they are.
3. `lib/research/lists/owner_line.py` (~:55-61): the `out of date` and `in date` sentences take `long_day(...)` of `due` and
   `reviewed`; `part["reviewed"]` and `part["due"]` stay ISO.
4. Tests: a new `lib/research/freshness/tests/test_long_day.py` (the ordinal table, timestamps, non-dates unchanged); in
   `test_collector_record.py`, `test_page_body.py` and `test_owner_line.py` change ONLY the expected sentence strings.

Run `lib/research/freshness/tests/`, `lib/research/lists/tests/` and `lib/research/api/tests/` before your commit and report each
last line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W319-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You do not edit `page_body.py`, `collector_read.py` or `scoped_amgt.py`.

## 3. SURFACES

<paths>
lib/research/freshness/long_day.py
lib/research/freshness/collector_record.py
lib/research/lists/owner_line.py
lib/research/freshness/tests/test_long_day.py
lib/research/freshness/tests/test_collector_record.py
lib/research/freshness/tests/test_page_body.py
lib/research/lists/tests/test_owner_line.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~319/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ee-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81/checks/r81_ee2.py" --crit AC1; echo "exit=$?"</invocation><expect>long_day gives the house long form and returns other input unchanged; the read and checked sentences carry the long form and no YYYY-MM-DD day while last_read stays ISO; owner_line builds through long_day; D1-D4 PASS; R81 EE2 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ee-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81/checks/r81_ee2.py" --crit AC2; echo "exit=$?"</invocation><expect>the two modules' own test files pass; B1 PASS; R81 EE2 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~319 <0.9.0_WK_AMGT_RESAPP~319@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~319/AMGT_RESAPP.TO-AMGT-ee-2.one-date-form-in-the-served-freshness-words.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line (api folder on this box: 2 failed at the base, both `No module named 'pypdf'` -- name them, file no row);
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-80 analysis @6d8d699c09 enrichment item 3 (row D1-S1). Checks dry-run at the base: AC1 base: FAIL as expected (D0 long_day absent); AC2 base: PASS as expected (25 passed). The item's close is one served /freshness read after AMGT-ee-6's snapshot leg.

<status>pending</status>
<round>81</round>
<slot>0.9.0_WK_AMGT_RESAPP~319</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
