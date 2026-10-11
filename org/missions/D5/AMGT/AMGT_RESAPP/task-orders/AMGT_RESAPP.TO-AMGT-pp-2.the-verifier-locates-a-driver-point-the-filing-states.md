# AMGT_RESAPP task order -- `AMGT-pp-2` -- THE VERIFIER LOCATES A DRIVER POINT THE FILING STATES, AND STILL REFUSES ONE IT DOES NOT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-pp-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~372</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-pp-2.the-verifier-locates-a-driver-point-the-filing-states</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a verifier change and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the check reads three stored filing objects and the silver filing_source rows with the caller's own credentials (GET only); no role changes.
comp-adversary: RUN at the cut -- r91_locator.py FAILs L1-L4 at the base (held: "no period label for FY2025 was located in the excerpt" x2; "value not found as a whole number inside the block" x2) and PASSes K1, E1, X1-X7; a throwaway candidate reached 13 of 13 only after its first version failed X1 (a column map that ran past its own table verified BABA FY2025 = 158,132 from another table), which is the discrimination the X arms exist for.
EGRESS CLASS, declared: NONE (S3 GETs of stored objects; no vendor, SEC or model call).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-372`, cut from the current branch head). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE CELL -- `AMGT-pp-2` (round 91, decomposition s.99)

CTO~DELL1 round-90 analysis item 2 (row Z-W266-S3). `lib/research/filings/analyze.py` re-verifies every emitted driver point against the
filing excerpt in ONE function, `_apply_point_verification(points, excerpt_text, passage_map, anchor)` (about line 1282): a fresh run
and `reverify_stored_thesis_driver` both take it. A point verifies only when its value is found, as a whole number, inside the block
that carries ITS OWN period label, or in the structural columnar layout `_columnar_verify` reads. Four stored points that the filing
does state are held, and one that it does not is held correctly:

| name | period, value | held reason | what the excerpt actually carries |
|---|---|---|---|
| BABA | `FY2025`, 118,028 | no period label for FY2025 was located | the segment table's header is the standalone lines `2024`, `2025`, `2026`, then the column-unit lines `RMB`, `RMB`, `RMB`, `US$`, then rows of FOUR numbers: `Cloud Intelligence Group` / `106,374` / `118,028` / `158,132` / `22,924`. The period is printed as `2025`, never `FY2025` |
| BABA | `FY2026`, 158,132 | no period label for FY2026 was located | the same row, third column |
| SAP | `2023`, 13,745 | value not found as a whole number inside the block carrying the 2023 label | an inline prior-period parenthetical in the same sentence as the 2024 figure: `... to <euro sign>18,078 million in 2024 (2023: <euro sign>13,745 million)` |
| SAP | `2025`, 21.05 | value not found as a whole number inside the block carrying the 2025 label | `... increased <euro sign>2.97 billion, or 16%, to <euro sign>21.05 billion in 2025 (2024: <euro sign>18.08 billion)`; `_WHOLE_NUMBER_RE` splits `21.05` into `21` and `05` |
| PBR | `2025`, 2.99 mboed | value not found as a whole number inside the block carrying the 2025 label | NOT in the excerpt (`2.99`, `2,99`, `2.9` and the series name occur 0 times). It must stay HELD |

Make the verifier accept the four structural forms below and nothing looser. Every rule is anchored on BOTH the value and the period;
none is a search for the number anywhere:

1. **Period alias.** A period emitted as `FY2025` or `FY 2025` (case-insensitive) is located by its four-digit year token. The point keeps
   its emitted period string in its output.
2. **Columnar run with unit columns.** A header run of two or more standalone four-digit year lines (distinct, ascending order as printed),
   followed by `m` column-unit lines (`RMB`, `US$`, `$`, a currency code, `YoY % Change`), `m` at least the number of years, gives rows of
   exactly `m` numbers; the point's value must equal the number at the position of its year in the header run. Bind the mapping to the
   table the header introduces: stop the row scan at the next standalone year line or at prose (a long line); a row scan that runs on
   into a later table verifies the wrong period's figure.
3. **Inline prior-period parenthetical.** `<period>: <up to 3 non-digit characters><value>` (for example `(2023: <euro sign>13,745 million)`),
   the value not being part of a longer number.
4. **A decimal is one number.** `21.05` is one token that equals 21.05; it never equals `21`, `5`, `1.05` or `21.5`, and `1.05` never
   matches inside `21.05`. The existing integer forms (thousands separators) are unchanged. A value stated "in <period>" in the same
   sentence (`<value> <up to two words> in <period>`) is accepted where the period's own block does not carry it.

Refusals that must keep holding (the check pins each): a value the filing states for a DIFFERENT period (BABA `FY2025` = 158,132, BABA
`FY2026` = 118,028, SAP `2023` = 18,078, SAP `2025` = 18.08 which is `2024`'s figure in the same sentence); a near-miss number (21.5,
1.05); a period the excerpt never labels (`FY2019`); PBR's value. The verified SAP `2024` point keeps its stored span `[129709, 129715]`
and passage id.

ONE verification path stays: do not add a second function a fresh run does not take. `reverify_stored_thesis_driver` must not be called
without `dry_run=True` in anything you run: this cell changes code and tests only; no stored object is rewritten, no model call is made.

Add `lib/research/filings/tests/test_verify_locator_forms.py` (pure, no network): small synthetic excerpts, one positive test per form
above and one refusal test per refusal above, including a two-table excerpt in which the same value sits in a DIFFERENT column of the
second table.

ASCII only. Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W372-S<k>`,
`disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. The check's S3 GETs and silver reads are permitted; nothing else is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit `analyze.py` minimally: do not reformat it and do not touch `fetch.py`, `passages.py`, `drafting_build.py` or any served reader.
5. Do not run `reverify_stored_thesis_driver` with `dry_run=False`, and do not call it in any way that writes.

## 3. SURFACES

<paths>
lib/research/filings/analyze.py
lib/research/filings/tests/test_verify_locator_forms.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~372/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-pp-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round91_prep/checks/r91_locator.py"; echo "exit=$?"</invocation><expect>PASS L1 (BABA FY2025 118,028 verifies), PASS L2 (BABA FY2026 158,132), PASS L3 (SAP 2023 13,745), PASS L4 (SAP 2025 21.05), PASS K1 (SAP 2024 keeps span 129709-129715), PASS E1 (PBR 2.99 stays held with a reason), PASS X1-X7 (the seven refusals); R91 LOCATOR: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-pp-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/filings/tests/test_verify_locator_forms.py lib/research/filings/tests/test_own_column_gate.py lib/research/filings/tests/test_reverify_dry_run.py lib/research/filings/tests/test_hold_unspanned.py lib/research/filings/tests/test_filings.py lib/research/filings/tests/test_splice_driver.py -q; echo "exit=$?"</invocation><expect>the new test file and the five existing verifier test files pass with 0 failed, and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~372 <0.9.0_WK_AMGT_RESAPP~372@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~372/AMGT_RESAPP.TO-AMGT-pp-2.the-verifier-locates-a-driver-point-the-filing-states.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of `analyze.py`, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-90 analysis @b462a02d8a item 2; round-90 ISSUER_READS.md oo-2 (the five held points, measured against the stored source and analysis objects). The producer-side act that makes the served charts change is a stored-object re-verification (`reverify_stored_thesis_driver(..., dry_run=False)` per name, a store write that moves what the page serves); it is NOT in this cell and needs its own never-widen pair. This cell closes on the check: 4 LOCATOR points verify and PBR's EXCERPT point stays held (analysis close). Risk LOCAL (code and tests; the check's reads are GETs). The `X` arms are the discrimination: an earlier candidate failed X1 by scanning past its table, so a worker that satisfies L1-L4 with a looser rule fails here. Note the legacy `filings/v1/<key>/<accession>.source.json` excerpt is NOT the text the production re-verification reads (the silver `filing_source` row is: the stored SAP span 129709-129715 lies beyond the legacy excerpt's 113,823 characters); the check reads silver. Checks dry-run at the base: AC1 FAIL (L1-L4; K1, E1, X1-X7 PASS); AC2 PASS at the base for the five existing files (62 passed) and FAIL until the new file exists.

<status>pending</status>
<round>91</round>
<slot>0.9.0_WK_AMGT_RESAPP~372</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- issuer close 2026-10-11T07:4xZ (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-372 @9376f3bc6b merged @3b27cc580f, proof instance VALID (worker run and issuer re-run); issuer re-run in the worktree: AC1 R91 LOCATOR YES (13 of 13: L1-L4 verify, K1 keeps span 129709-129715, E1 PBR held, X1-X7 refused), AC2 78 passed; drain checks py_compile rc 0, ruff clean, lib/research/filings 318 passed. Issuer regression read (the production dry-run over all 12 stored analysis objects, base against worker, nothing written): 4 points gained (BABA FY2025, FY2026; SAP 2023, 2025), 0 supported points lost, 0 spans changed, and 1 point REMOVED that was a base false positive: ASML 2025 = 4 verified on the final digit of `12.4` (the old pattern split a decimal). Rows ruled: S1 (the excerpt prints a bare 2019 in prose; X6 holds because an FY alias locates only by a standalone year line) stands, the check's wording on X6 is imprecise and stays; S2 (every standalone header of a period is tried, each bound to its own table) stands; S3 (ARMED: a last-located period's block runs to the excerpt's end, so a synthetic excerpt verifies 2025 = 18.08) is PRE-EXISTING and not widened by this cell: ruled carried, a later cell bounds that block with a refusal arm on a synthetic excerpt (round 92 candidate); S4 (the 80-character prose threshold is unmeasured) stands. The producer-side store write that makes the served charts change is not in this cell and needs its own pair.</status>
