# AMGT_RESAPP task order -- `AMGT-ii-1` -- THE SOURCE LANGUAGE IS STAMPED FROM THE CUT SECTIONS, NOT THE DOCUMENT HEAD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ii-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~334</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one line and its test.
comp-iam: DECLARED-NOT-APPLICABLE -- the check reads cached filing texts in-process; no store read or write.
comp-adversary: RUN at the cut (round84_prep/GROUP_LANGUAGE_NOTES.md) -- fetch.py:417 runs detect_language on the first 40,000 chars of the whole filing, which in every cached 20-F is the XBRL header: BABA reads pt ('e', 'com'), SAP es ('y', 'se'); the same detector reads en on all 15 cut sections. analyze.py:397 then asks the model to quote in that language.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-334`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ii-1` (round 84, decomposition s.92)

Row AMGT_RESAPP-D1-W332-S1. Read `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/GROUP_LANGUAGE_NOTES.md`
WHOLE first, then `lib/research/filings/fetch.py` around :417. Stamp `language` from the cut sections the function already builds
(`excerpt_text`) instead of the document head; a genuinely non-English filing must still read its own language (the check plants a
Portuguese filing behind an XBRL-noise header). Add one test in `lib/research/filings/tests/` with that plant and an English filing
behind the same noise. Do not change `detect_language` itself, `battery.py` or `document.py`.

**Before the checks:** copy the cached filing texts from the base checkout into your worktree (gitignored, never committed):
`mkdir -p <your worktree>/.scratch && cp -r /c/Dev/ajb_workspace/.scratch/r82_20f <your worktree>/.scratch/`. PyMuPDF does not
load on this box; put an empty `fitz.py` on PYTHONPATH for the filings test folder.
Run `lib/research/filings/tests/` before your commit and report its last line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W334-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `fetch.py` and one test file only. Never fetch a filing (the cache is the input).

## 3. SURFACES

<paths>
lib/research/filings/fetch.py
lib/research/filings/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~334/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ii-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" py -3.12 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_language.py" --crit AC1; echo "exit=$?"</invocation><expect>all five cached English 20-F filings are stamped en and the planted Portuguese filing is stamped pt; L1-L2 PASS; R84 LANGUAGE AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ii-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_cut.py" --crit AC2; echo "exit=$?"</invocation><expect>the 10-K fixture and dd-1's 20-F fixture sections hash as at the base; R82 CUT AC2: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~334 <0.9.0_WK_AMGT_RESAPP~334@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~334/AMGT_RESAPP.TO-AMGT-ii-1.the-language-stamp-from-the-cut-sections.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the filings folder's last line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-83 analysis @ROUND_ANALYSIS.round83 R2 / enrichment item 2 (row D1-W332-S1, graduated to this seat). fetch.py is a site-Z producer path: the MERGE is a site-Z deploy under 1.0.0_SA_CTO~Z's half. Checks dry-run at the base: AC1 base: FAIL as expected (3 of 5 en; the plant reads en); AC2 base: PASS as expected (a bound).

<status>pending</status>
<round>84</round>
<slot>0.9.0_WK_AMGT_RESAPP~334</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
