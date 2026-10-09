# AMGT_RESAPP task order -- `AMGT-dd-2` -- A CITATION HEADING IS NEVER A BARE NUMBER OR PERCENTAGE: AT THE PARSE AND AT THE THREE SERVE POINTS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-dd-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~316</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; two modules and their tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read path: AC2 and AC3 read drafting/v1 read only through the read the function already makes; no grant.
comp-adversary: RUN at the cut (round80/GROUP_R2_NOTES.md) -- at the base 4 of 272 served citations carry a heading with no letter (ASML NA P0064 "5.09%", P0065 "0.01%"; SAP GY P0139, P0143 a zero-width space); 41 of 1122 stored drafting records and 74 of 3675 stored analysis locations do. AC1 and AC2 FAIL at the base, AC3 PASSES there.
EGRESS CLASS, declared: NONE. No SEC, vendor, model or Bloomberg call.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-316`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-dd-2` (round 80, decomposition s.88)

A cited passage names where it came from: `<item> / <heading> / paragraph N`, which the page draws as
"ITEM 3.D. RISK FACTORS > 5.09% > PARAGRAPH 65". "5.09%" is a table cell, not a section. It became a heading because
`build_passage_map` in `lib/research/filings/passages.py` (lines ~207-213) treats every excerpt line shorter than 60
characters as the heading of the next passage. Fix it at the parse, so future analyses store clean locations, and at the
three points where `lib/research/api/scoped_amgt.py` serves a stored location, so what is stored today is served clean
without a re-run.

Read `lib/research/filings/passages.py` whole, and in `lib/research/api/scoped_amgt.py` read `_resolved_evidence`
(~:2850), `_driver_point_passages` (~:2866) and the segment-row cite (~:3789-3810), first.

1. `passages.py`: add `heading_has_words(line)`: True when the line holds at least one alphabetic character
   (`str.isalpha`). In `build_passage_map`, a short line with no letter is neither a heading nor a passage: skip it, and do
   NOT let it clear a real heading that is pending. Passage ids, spans and texts stay exactly as today.
2. `passages.py`: add `clean_location(location)`: split on `" / "`, keep the first segment (the item) and the last
   (`paragraph N`) as they are, drop every middle segment that has no letter, join with `" / "`. A location with nothing
   to drop is returned unchanged, byte for byte. Non-string input is returned unchanged.
3. `scoped_amgt.py`: apply `clean_location` to the `location` served at the three points above. Import it at FUNCTION
   scope, the way the module already imports `lib.research.filings.section_coverage` (~:3745). No other served key and no
   other byte changes. Stored objects are never rewritten.
4. Tests: a new `lib/research/filings/tests/test_passage_headings.py` (plants: "5.09%", "0.01%", "1", "(1)",
   "2025 2024 2023", "$1.19 ($20.38)", a lone zero-width space U+200B; a real short heading such as "General Meeting." is
   kept; a letterless line between a real heading and its passage leaves the real heading in place) and a new
   `lib/research/api/tests/test_citation_headings.py` covering all three serve points, including the segment-row cite.

Run `lib/research/api/tests/` before your commit and report its last line. At the base on this box it reads
`2 failed, 866 passed`: both failures are `ModuleNotFoundError: No module named 'pypdf'`, not installed here. Name them
and file no row for them. The filings test folder may error at collection here (PyMuPDF does not import on this box);
your new filings test imports only `passages`, which needs nothing outside the standard library.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-R1-W316-S<k>`,
`disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No store write, no deploy, no schedule, no SEC, vendor, model or Bloomberg call.
2. AC2 and AC3 read the real drafting store read only into a temporary folder. Neither they nor you write to it.
3. You do not edit `lib/research/filings/analyze.py`, `lib/research/filings/drafting_build.py` or any print module.
4. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
5. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/filings/passages.py
lib/research/filings/tests/test_passage_headings.py
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_citation_headings.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~316/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-dd-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_dd2.py" --crit AC1; echo "exit=$?"</invocation><expect>heading_has_words and clean_location exist; no location built from the plant carries a letterless heading; ids, spans and texts unchanged; P1-P7 PASS; R80 R2 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-dd-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_dd2.py" --crit AC2; echo "exit=$?"</invocation><expect>every stored drafting document served through the function; the positive control still finds letterless headings in the store; 0 of the served citations names a letterless heading, denominator printed; S1-S3 PASS; R80 R2 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-dd-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_dd2.py" --crit AC3; echo "exit=$?"</invocation><expect>what is served differs from the stored records only in location, and only where the stored location carried a letterless heading; drift 0; B1 PASS; R80 R2 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~316 <0.9.0_WK_AMGT_RESAPP~316@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~316/AMGT_RESAPP.TO-AMGT-dd-2.a-citation-heading-is-never-a-bare-number.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api test folder's last line and your two new test files' results;
- the served count of letterless headings before and after (AC2's lines);
- the hookup the redeploy must carry (the function-scope import), or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~Z round-79 analysis R2, enrichment item 2 (`ledger/ROUND_ANALYSIS.round79.md` @c249be336b). Drafted in
`deliverables/2.0.0_SA_COO~R1/round80/GROUP_R2_NOTES.md`. Checks dry-run at the base (box/dell1 @3131126320): AC1 base: FAIL as
expected (P6, P7 among the FAILs; SERVED: NO; exit=1); AC2 base: FAIL as expected (S3 4 of 272 served; exit=1); AC3 base: PASS as
expected (drift 0; SERVED: YES; exit=0). Served on the live function only through AMGT-dd-4. NO merge hold: `passages.py` is not a
producer path while site Z's -FilingsAnalyzer task stays disabled (1.0.0_SA_CTO~DELL1 msg 1394).

<status>pending</status>
<round>80</round>
<slot>0.9.0_WK_AMGT_RESAPP~316</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @a06f7f9c20 (worker build be1966317b, proof 982274ab01 VALID rc=0; branch row withdrawn @91465662e7 and carried as AMGT_RESAPP-D1-S2). AC1 FAILed on P6 alone, an issuer check defect; AMENDMENT 1 fixed r80_dd2.py P6 (None returned unchanged, as the order says). Re-run by the issuer on the shared tree: R80 R2 AC1, AC2 (0 of 272 served letterless; 41 of 1122 stored), AC3 (4 changed, drift 0) all SERVED: YES. api suite on the branch 2 failed (pypdf absent on dell1), 896 passed. Served on the live function only through dd-4.</status>
