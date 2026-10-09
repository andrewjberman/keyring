# AMGT_RESAPP task order -- `AMGT-kk-2` -- THE DRAFTED COMPANY DESCRIPTION IS DRAWN FROM THE BUSINESS ITEM ONLY, AND IS EMPTY FOR A NAME WITH NO BUSINESS TEXT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-kk-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~342</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no store read or write.
comp-adversary: RUN at the cut (round86_prep/GROUP_DESCRIPTION_NOTES.md) -- drafting_build.py:66-67 fills company_description from item CLASSES (segments, commentary) and never checks where an item's evidence sits: live, 24 of 25 description sentences across the five 20-F names cite Item 5 or 3.D.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-342`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-kk-2` (round 86, decomposition s.94)

CTO~DELL1 round-85 analysis R5. Read `round86_prep/GROUP_DESCRIPTION_NOTES.md` whole, then `lib/research/filings/drafting_build.py`
(:66-67 and `Drafter.draft` :289-327). The `company_description` section takes only items whose evidence sits in the business item
(20-F Item 4.B / Item 4 Information on the Company; 10-K Item 1); a name with none gets an EMPTY section. Every other section is
unchanged. Tests in `lib/research/filings/tests/test_description_business_only.py`: a business-cited item kept, an Item 5 and an
Item 3.D item dropped, a name with no business item drafts an empty section, and another section unchanged by the rule.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W342-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `drafting_build.py` and the new test file only.

## 3. SURFACES

<paths>
lib/research/filings/drafting_build.py
lib/research/filings/tests/test_description_business_only.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~342/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-kk-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="/c/tmp/stubfitz;$(pwd)" py -3.12 -m pytest lib/research/filings/tests/test_description_business_only.py -q; echo "exit=$?"</invocation><expect>every test in the new file passes (a business item kept; Item 5 and 3.D dropped; no business text drafts empty; other sections unchanged), 0 failed; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-kk-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="/c/tmp/stubfitz;$(pwd)" py -3.12 -m pytest lib/research/filings/tests lib/research/drafting -q; echo "exit=$?"</invocation><expect>the filings and drafting folders pass with 0 failed; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~342 <0.9.0_WK_AMGT_RESAPP~342@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~342/AMGT_RESAPP.TO-AMGT-kk-2.company-description-from-the-business-item-only.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-85 analysis R5 (producer half of DSGN zzo-1/zzp-1). Future drafts only; stored drafts move under AMGT-kk-3. Checks dry-run at the base: AC1 base FAIL (no test file); AC2 base PASS (a bound).

<status>pending</status>
<round>86</round>
<slot>0.9.0_WK_AMGT_RESAPP~342</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
