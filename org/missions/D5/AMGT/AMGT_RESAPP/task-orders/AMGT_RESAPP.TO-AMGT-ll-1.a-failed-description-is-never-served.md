# AMGT_RESAPP task order -- `AMGT-ll-1` -- THE LIVE READER WITHHOLDS A COMPANY DESCRIPTION WHOSE OWN VERDICT IS FAILED; A PASSED ONE STILL SERVES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ll-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~346</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one reader change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the stored drafts read-only (AC2's local arm); writes no store.
comp-adversary: RUN at the cut -- `read_drafted_sections` (scoped_amgt.py ~:2945-3030) computes `company_description_verdict` (:4266) on the served sentences and SERVES them even when it reads FAILED: live, NU serves 1 sentence under verdict FAILED (a Colombia launch metric). The verdict exists on company_description only.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-346`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ll-1` (round 87, decomposition s.95)

CTO~DELL1 round-86 analysis R1 (`ledger/ROUND_ANALYSIS.round86.md`). In `lib/research/api/scoped_amgt.py` `read_drafted_sections`:
when the company_description section's own verdict (`company_description_verdict`) reads FAILED, serve it with `sentences: []`, keep
`description_verdict_state: FAILED` and its reason, and add `withheld_failed: <n>` (the count withheld), so the page shows the
section's empty state. A PASSED or NO_SENTENCES section is unchanged. Every other section is unchanged. Tests in
`lib/research/api/tests/test_failed_description_withheld.py`: a FAILED description is withheld (0 sentences, state FAILED, count
printed); a PASSED description still serves its sentences (negative arm); another section unchanged. Code only, no deploy.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W346-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `scoped_amgt.py` and the new test file only.
8. CLIENT DATA (0.0.0_AB_MSTR~DELL1 msgs 2720/2747/2766/2804): never open, search, copy or `git show` any
   `org/**/W73_S*_EVIDENCE.json`, the COTBKF ~74 / ~66 / ~70 cottonwood manifests, or the IRPT_DASHBD tie-out files, in the tree or
   in history. Search only inside named paths, never the whole repository.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_failed_description_withheld.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~346/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ll-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="/c/tmp/stubfitz;$(pwd)" py -3.12 -m pytest lib/research/api/tests/test_failed_description_withheld.py -q; echo "exit=$?"</invocation><expect>every test passes: a FAILED description serves 0 sentences with its state and withheld count, a PASSED one still serves, another section unchanged; 0 failed; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ll-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="/c/tmp/stubfitz;$(pwd)" py -3.12 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round87_prep/checks/r87_withheld.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>through the handler in your worktree, over the five stored drafts, no FAILED description carries a sentence and every name answers with the section; W1-W2 PASS; R87 WITHHELD AC1: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~346 <0.9.0_WK_AMGT_RESAPP~346@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~346/AMGT_RESAPP.TO-AMGT-ll-1.a-failed-description-is-never-served.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line (api folder on this box: 2 failed at the base, both `No module named 'pypdf'` -- name them, file no row);
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-86 analysis @2eba7c172b R1. Deploys under AMGT-ll-3. AC2's local arm reads the stored drafts: graded BEFORE AMGT-ll-2 empties NU (ll-2 is staged behind this order's report), so NU's FAILED sentence is the live negative case. Checks dry-run at the base: AC1 base FAIL (no test file); AC2 base FAIL as expected (NU FAILED with 1 sentence, local handler).

<status>pending</status>
<round>87</round>
<slot>0.9.0_WK_AMGT_RESAPP~346</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
