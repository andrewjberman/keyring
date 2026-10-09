# AMGT_RESAPP task order -- `AMGT-hh-1` -- THE PASSAGE MAP AT PARAGRAPH GRAIN: A WRAPPED LINE JOINS ITS PARAGRAPH, SO A NARROW-COLUMN BUSINESS SECTION BECOMES PASSAGES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-hh-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~329</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one function and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- AC1 reads one stored silver part read-only; no write.
comp-adversary: RUN at the cut (round83_prep/GROUP_PASSAGE_NOTES.md) -- build_passage_map makes one passage per line and drops every line under 60 chars as a heading: ASML's Item 4.B (median line 38 chars) keeps 8 passages, 627 of 58,260 chars (1.1%); cross-line quotes fail the one-passage verbatim gate (19 of 83 citations verbatim in one cited passage). The live function imports passages.clean_location, so AC2 guards the serve-path definitions.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-329`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-hh-1` (round 83, decomposition s.91)

Row AMGT_RESAPP-D1-W324-S1: ASML NA's re-cut business text never reached the served /thesis because
`lib/research/filings/passages.py` `build_passage_map` makes ONE passage per excerpt line and treats every line under
`_MIN_PASSAGE_CHARS = 60` as a heading. Read `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/GROUP_PASSAGE_NOTES.md`
WHOLE first, then `passages.py` whole.

Repair `build_passage_map` only: build passages at PARAGRAPH grain. A wrapped line joins the passage it continues with a single
space; the passage keeps its start and end offsets into the excerpt. A line continues the passage when the passage so far does
not end in sentence-final punctuation (`. ! ? :`) and the line is not a heading; a short line is a heading only when a new
paragraph follows it. A passage's text must still re-locate verbatim in the excerpt under the module's own normalisation (the
verbatim gate in `lib/research/drafting/verbatim.py` is NOT changed: loosening it would admit glued words that are not in the
filing). `clean_location`, `Locator` and `cjk_share` stay byte-identical: the live function and two other modules import them.

Tests in `lib/research/filings/tests/` (the existing passages test file, or a new `test_passage_paragraphs.py`): a planted
narrow-column paragraph becomes one passage; a true short heading followed by a paragraph stays a heading; a quote that spans
two wrapped lines is a substring of ONE passage. Run `lib/research/filings/tests/` and `lib/research/drafting/` before your
commit (put an empty `fitz.py` on PYTHONPATH for the filings folder; PyMuPDF does not load on this box) and report both last lines.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W329-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `passages.py` and one test file only.

## 3. SURFACES

<paths>
lib/research/filings/passages.py
lib/research/filings/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~329/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-hh-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" py -3.12 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_passages.py" --crit AC1; echo "exit=$?"</invocation><expect>ASML NA's stored Item 4.B is covered by passages at 50% or more of its characters and 0 adjacent passage pairs glue a word; P1-P2 PASS; R83 PASSAGES AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-hh-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_serveguard.py"; echo "exit=$?"</invocation><expect>clean_location, Locator and cjk_share are unchanged from the base; R83 SERVEGUARD: YES 3 of 3; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~329 <0.9.0_WK_AMGT_RESAPP~329@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~329/AMGT_RESAPP.TO-AMGT-hh-1.passages-at-paragraph-grain.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines (AC1's per-item coverage table in full);
- the filings and drafting folders' last lines;
- anything the code showed that the notes did not;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-82 analysis @c600e61f91 R1 / enrichment item 1 (row D1-W324-S1). Grounded round83_prep/GROUP_PASSAGE_NOTES.md. passages.py is imported by the live function (clean_location only) and by document.py, analyze.py, translate.py, drafting_build.py, ceo_search.py; site-Z: the analyzer task is disabled (CTO msg 1267 rule) and no scheduled site-Z task runs these -- the merge re-reads that census before it lands. Checks dry-run at the base: AC1 base: FAIL as expected (1.1%, 391 of 488 glued); AC2 base: PASS as expected (a bound).

<status>pending</status>
<round>83</round>
<slot>0.9.0_WK_AMGT_RESAPP~329</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- issuer close 2026-10-09T09:2xZ: merged @ac6ad315b6 (wk-AMGT_RESAPP-329 @729f832051, 4 paths). On the merged tree: r83_passages AC1 YES (ASML Item 4.B 218 passages, 102.4% -- the joined text carries the added spaces; risk 98.7%, OFR 98.4%; 0 of 401 adjacent pairs glue a word); r83_serveguard YES 3 of 3 (only _ends_sentence and build_passage_map moved); filings + drafting 262 passed (stub fitz, py3.12). Served DELTA = 0: no serve-path definition moved and no deploy; not a site-Z producer path while the analyzer task is disabled (1.0.0_SA_CTO~Z's census @83b31c3fa9: all importers hand-run, no schedule or Lambda). Row D1-W329-S1 (CJK sentence-final marks added, with a test) is INERT.</status>
