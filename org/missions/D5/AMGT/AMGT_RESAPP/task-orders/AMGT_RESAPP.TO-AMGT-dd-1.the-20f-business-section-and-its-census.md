# AMGT_RESAPP task order -- `AMGT-dd-1` -- A 20-F'S BUSINESS SECTION IS CUT FROM ITS OWN HEADING, AND A CENSUS SAYS WHERE EACH STORED 20-F ITEM CAME FROM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-dd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~315</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module, one constant, one new reader and their tests.
comp-iam: DECLARED-NOT-APPLICABLE -- the census reads the silver store read only through the existing lib/research/harvest/store.py reader; no new read path, no grant.
comp-adversary: RUN at the cut (round80/GROUP_R1_NOTES.md) -- at the base no 20-F key named business exists (document.py 20-F keys risk/mdna/officers; fetch.EXCERPT_ITEMS 20-F = risk, mdna); 4 of 5 stored 20-F risk items came from a fallback heading the code no longer has; 0 of 5 hold a business section. AC1 and AC2 FAIL at the base, AC3 PASSES there; literal outputs in the notes.
EGRESS CLASS, declared: NONE. No SEC, vendor, model or Bloomberg call.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-315`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-dd-1` (round 80, decomposition s.88)

A 20-F's "Item 4.B Business overview" says what the company does. The filing cutter never cuts it: its 20-F keys are
risk, mdna and officers. ASML NA's stored text is therefore share-capital and board-holdings text, and the page has
nothing that describes the business. Add the business section to the cutter, and build a read-only census that says,
for every stored 20-F, which heading each stored item came from.

Read `lib/research/filings/document.py`, `lib/research/filings/fetch.py` (around `EXCERPT_ITEMS`, line ~89) and
`lib/research/filings/tests/test_document.py` whole first.

1. `document.py`: add a 20-F key `business`, label `"Item 4.B. Business Overview"`. Start patterns (compacted form, as
   the file's other patterns are written): Item 4 B Business overview, and B Business overview. End patterns: C
   Organizational (or Organisational) structure, Item 4A Unresolved, Item 5 Operating. Add `ITEM_CAPS["business"] = 60000`.
   It is cut by the same bounded mode the other 20-F keys use. A 20-F with no Business overview heading reads the
   business section's status as failed WITH a reason, as the other keys do when absent. The 10-K patterns, the three
   existing 20-F keys and `sections_to_excerpt` do not change.
2. `fetch.py`: `EXCERPT_ITEMS["20-F"]` becomes `["business", "risk", "mdna"]`. Nothing else in `fetch.py` changes.
3. New `lib/research/filings/section_census.py`, run as `python -m lib.research.filings.section_census --stored`. It reads
   the latest silver `filing_source` rows for vendors `sec` and `issuer-site` through
   `lib.research.harvest.store.silver_latest(vendor, "filing_source", ("security_key", "accession"))` and
   `lib.research.harvest.filings.source_object_from_row(row)`, keeps the objects whose form or family is `20-F`, and prints
   one line per name:
   `<security_key> <parser_version> | risk: <CLASS> "<first heading words>"; mdna: <CLASS> ...; business: <CLASS> ...`
   CLASS is OWN-HEADING (today's start patterns for that key match the first TWO lines after the item label: NU's "Item 5.
   Operating" heading wraps a line), FALLBACK (the stored text starts with a bare "risk factors" heading that today's
   patterns do not accept), NONE (the item is absent) or OTHER. The last line reads exactly:
   `SECTION CENSUS: <k> of <n> stored 20-F names carry a business section from its own heading; <j> of <n> risk items came from their own heading`.
   It writes nothing.
4. Tests: add plant cases to `test_document.py` (a 20-F fixture whose Business overview is cut from its own heading and
   closed before C / Item 5; a 20-F with no such heading reads failed with a reason) and a new
   `lib/research/filings/tests/test_section_census.py` on plants (no store read in a test).

**dell1 environment:** PyMuPDF (`fitz`) does not import on this box. `document.py` imports it at the top and `cut()`
never uses it, so the filings test folder errors at collection here. In your NEW test file, stub `fitz` exactly as the
check does (`try: import fitz` / `except Exception: sys.modules["fitz"] = types.ModuleType("fitz")`) before importing
the module. Report the folder's collection errors in your report and file no row for them.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W315-S<k>`,
`disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No store write, no deploy, no schedule, no SEC, vendor, model or Bloomberg call.
2. You do not re-cut or re-fetch any company's filing. The census reads; it never writes.
3. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/filings/document.py
lib/research/filings/fetch.py
lib/research/filings/section_census.py
lib/research/filings/section_coverage.py
lib/research/filings/tests/test_document.py
lib/research/filings/tests/test_section_coverage.py
lib/research/filings/tests/test_section_census.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~315/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-dd-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_dd1.py" --crit AC1; echo "exit=$?"</invocation><expect>a 20-F's business section is cut from its own heading and closed before C / Item 5; a 20-F without it reads failed with a reason; fetch.EXCERPT_ITEMS 20-F carries business; A1-A3 PASS; R80 R1 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-dd-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_dd1.py" --crit AC2; echo "exit=$?"</invocation><expect>the census names every stored 20-F the checker reads itself, its SECTION CENSUS denominator equals that count, and ASML_NA_Equity's line reads risk: FALLBACK; C0-C4 PASS; R80 R1 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-dd-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_dd1.py" --crit AC3; echo "exit=$?"</invocation><expect>the 10-K fixture's three sections and the 20-F risk, mdna and officers sections hash as at the base, every B line PASS; R80 R1 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~315 <0.9.0_WK_AMGT_RESAPP~315@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~315/AMGT_RESAPP.TO-AMGT-dd-1.the-20f-business-section-and-its-census.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the census's full output;
- your new test file's result and the filings folder's collection-error count;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~Z round-79 analysis R1, enrichment item 1 (`ledger/ROUND_ANALYSIS.round79.md` @c249be336b). Drafted in
`deliverables/2.0.0_SA_COO~R1/round80/GROUP_R1_NOTES.md`. Checks dry-run at the base (box/dell1 @3131126320): AC1 base: FAIL as
expected (A2, A3 FAIL; SERVED: NO; exit=1); AC2 base: FAIL as expected (C0 module absent; exit=1); AC3 base: PASS as expected
(B lines PASS; SERVED: YES; exit=0). This cell is the CODE half of R1. The STORE half (re-fetching ASML NA's 20-F from SEC,
its silver row, the re-analysis and the draft rebuild) is SEC and model egress: it is held for Andrew's per-use word and is
not cut. MERGE HOLD: `document.py` / `fetch.py` are imported by `filings/battery.py`, a named site-Z hand-run (census
@6a308cd424 row 28); RULED a site-Z producer path by 1.0.0_SA_CTO~DELL1 msg 1394. The worker executes now; the drain-merge is a
site-Z deploy under a never-widen pair and waits for 1.0.0_SA_CTO~Z's half.

<status>pending</status>
<round>80</round>
<slot>0.9.0_WK_AMGT_RESAPP~315</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>in_progress -- REOPENED by the issuer 2026-10-09T02:1xZ at the drain (AMENDMENT 1). The worker's commit 12e33085f3 reads VALID, but the drain's hygiene run on its branch FAILS lib/research/filings/tests/test_section_coverage.py::test_wanted_table_equals_the_producers: section_coverage._WANTED (the Lambda's copy of fetch.EXCERPT_ITEMS) lacks the new 20-F business key. Grant added to paths: lib/research/filings/section_coverage.py. Graded by no gate limb (a modification; LIMB 6 fires on newly-added orders only). Served effect: at the next redeploy (dd-4) each 20-F name's passage_coverage lists Item 4.B as wanted; dd-4's pair names it.</status>
<status>in_progress -- AMENDMENT 2 by the issuer 2026-10-09T02:4xZ on row AMGT_RESAPP-D1-W315-S1: grant lib/research/filings/tests/test_section_coverage.py; test_one_section_lists_the_other_as_not_covered's 20-F expectation lists business before mdna, which follows from the wanted table the producer now carries. Graded by no gate limb (a modification).</status>
