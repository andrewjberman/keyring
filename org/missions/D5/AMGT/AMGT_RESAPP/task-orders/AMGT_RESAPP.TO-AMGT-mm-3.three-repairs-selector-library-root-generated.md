# AMGT_RESAPP task order -- `AMGT-mm-3` -- THREE REPAIRS IN ONE CELL: THE WATCHLIST ROUTE MIRRORS THE SCOPED SELECTOR CONTRACT, A SET-BUT-MISSING LIBRARY ROOT REFUSES, A FILING SENTENCE CARRIES GENERATED FALSE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-mm-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~350</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- three modules and their tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no store read or write; tests stub everything.
comp-adversary: RUN at the cut (round88_prep/GROUP_SELECTOR_NOTES.md) -- (a) scoped_amgt `_firm_id` (:6417) reads the firm only from the edge header and reads NO selected_tenant; the scoped contract it must mirror is `infra/aws/lambda/investor-reporting/_scope/global.py:161-230` (an OPAL_GLOBAL principal off-list -> refusal FIRM_NOT_PERMITTED; a FIRM principal's selection IGNORED, never refused) with `_scope/resolve.py:223` classify_principal (OPAL_GLOBAL only from an explicit roster, empty by default); (b) `lib/research/corpus/library.py` `_resolve_root` skips a set-but-missing OPAL_RESEARCH_LIBRARY_ROOT silently (row S3); (c) `lib/research/drafting/schema.json` pins sentence.generated const true (row D1-W345-S2).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-350`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-mm-3` (round 88, decomposition s.96)

CTO~DELL1 round-87 analysis items 3-4 + carried row D1-W345-S2. Read `round88_prep/GROUP_SELECTOR_NOTES.md` whole first.
(a) D1-S18 in `lib/research/api/scoped_amgt.py`: GET watchlist refuses an off-list `selected_tenant` the way the scoped contract does
-- for the principal class that contract refuses (OPAL_GLOBAL), with its refusal code and HTTP status; a selection by any other
principal stays IGNORED (never refused: refusing tells a caller which firms exist); an absent selector is unchanged. Read the
contract's status mapping in the investor-reporting handler before coding. If it cannot be mirrored without packaging
investor-reporting code into this function, STOP that part, file a BLOCKING row naming why, and finish (b) and (c).
(b) row S3 in `lib/research/corpus/library.py`: a SET `OPAL_RESEARCH_LIBRARY_ROOT` that is not a directory raises, naming the path;
unset still derives as today.
(c) row D1-W345-S2: `lib/research/drafting/schema.json` lets `sentence.generated` be false for a sentence served as the filing's
own text (`quote_method: filing-sentence`), and `lib/research/filings/drafting_build.py` writes false for those; true stays
required otherwise. Tests: `lib/research/api/tests/test_watchlist_selector.py`, `lib/research/corpus/tests/test_library_root_refuses.py`,
`lib/research/filings/tests/test_filing_sentence_generated.py`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W350-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit the five modules named and the three new test files only.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_watchlist_selector.py
lib/research/corpus/library.py
lib/research/corpus/tests/test_library_root_refuses.py
lib/research/drafting/schema.json
lib/research/filings/drafting_build.py
lib/research/filings/tests/test_filing_sentence_generated.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~350/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-mm-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="/c/tmp/stubfitz;$(pwd)" py -3.12 -m pytest lib/research/api/tests/test_watchlist_selector.py lib/research/corpus/tests/test_library_root_refuses.py lib/research/filings/tests/test_filing_sentence_generated.py -q; echo "exit=$?"</invocation><expect>every test in the three new files passes (a selected_tenant from query, body or header is IGNORED, absent unchanged, no edge header still 401 -- part (a) stopped under its own STOP clause, AMENDMENT 1; a set-but-missing root raises naming the path, unset derives; a filing sentence validates with generated false and a model sentence still requires true); 0 failed; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-mm-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="/c/tmp/stubfitz;$(pwd)" py -3.12 -m pytest lib/research/filings/tests lib/research/drafting lib/research/corpus/tests -q; echo "exit=$?"</invocation><expect>the filings, drafting and corpus test folders pass with 0 failed; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~350 <0.9.0_WK_AMGT_RESAPP~350@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~350/AMGT_RESAPP.TO-AMGT-mm-3.three-repairs-selector-library-root-generated.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line (api folder on this box: 2 failed at the base, both `No module named 'pypdf'` -- name them, file no row);
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-87 analysis @08279f2a4f items 3 (D1-S18) and 4 (S3) + carried D1-W345-S2, batched as ONE repair cell. (a) and (c) reach the function at AMGT-mm-4. Checks dry-run at the base: AC1 base FAIL (no test files); AC2 base PASS (a bound).

<status>pending</status>
<round>88</round>
<slot>0.9.0_WK_AMGT_RESAPP~350</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending -- AMENDMENT 1 (issuer, 2026-10-09T21:0xZ) on row AMGT_RESAPP-D1-W350-S1 (BLOCKING): part (a) STOPPED under the order's own STOP clause, as the cut anticipated (round88_prep/GROUP_SELECTOR_NOTES.md recommended dismissal). The scoped contract refuses only an OPAL_GLOBAL principal, which exists only for a subject on an SSM roster (investor-reporting _scope/global.py:102); scoped_amgt has no roster, no ssm grant, no firm registry in its package, and the refusal carries no HTTP status -- the refusing branch would be unreachable. RULING: (a) is the selector IGNORED, as the contract treats every non-global principal (tests pin query/body/header ignored, absent unchanged, 401 without the edge header); AC1's expectation is amended to that. D1-S18 -> DISMISSED with that reason (goes to CTO~DELL1 with the round-88 packet; the analysis's item 3 asked for a refusal). (b) and (c) unchanged. Graded by to-pipeline-gate on a modification.</status>
<status>complete -- issuer close 2026-10-09T21:1xZ: merged @85777c27a8 (wk-AMGT_RESAPP-350 @aec426db72); proof re-recorded under AMENDMENT 1 @368b03881c, VALID. Issuer re-run on the merged tree: AC1 24 of 24 (selector ignored + absent unchanged + 401 without the edge header; a set-but-missing library root raises naming the path, unset derives; a filing sentence validates with generated false, a model sentence still requires true); AC2 863 passed. drafting_build writes generated = (no swap). Row D1-W350-S1 ruled (part a dismissed: unreachable in this function). Not in the order, noted for the analysis: narrative/entry.py _held_to_verified_firm DROPS an Opal caller's off-firm selection rather than refusing it -- the scoped routes do not all refuse. Served half (schema, ignored selector) ships under AMGT-mm-4 after the CVO grades this order.</status>
