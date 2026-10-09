# AMGT_RESAPP task order -- `AMGT-gg-1` -- THE 20-F CUTTER CUTS EACH STORED FILING'S OWN ITEM HEADINGS: BUSINESS, RISK AND MD&A FROM THE BODY, NOT THE CONTENTS PAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~323</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; the cutter and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- the check reads five cached filing texts in-process; no store read or write.
comp-adversary: RUN at the cut (round82_prep/GROUP_CUT_NOTES.md) -- on the five real stored 20-F filings the merged cutter cuts 6 of 15 cells: ASML and PBR (integrated reports: item headings only in a closing cross-reference table) cut nothing; NU's risk body heading is 'A. Risk Factors'; SAP's business body heading is 'ITEM 4. INFORMATION ABOUT SAP'. AC1 FAILs at the base (6 of 15), AC2 PASSes.
EGRESS CLASS, declared: NONE (the five filings are cached; no fetch).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-323`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-gg-1` (round 82, decomposition s.90)

Round 81's store half stopped because the merged 20-F cutter (`lib/research/filings/document.py`) cut NO item from ASML NA's real
20-F: every start pattern matched only a contents line. Measured on all five stored 20-F filings, it cuts 6 of 15 (name x
business/risk/mdna) cells. Repair the cutter so each of the five cuts business, risk and MD&A from the BODY, proven on the real
filings before anything is ever written.

Read `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/GROUP_CUT_NOTES.md` WHOLE first: it names, per
filing, every candidate heading line, why `_cut_bounded` rejects it, and the real body heading. Then read `document.py` whole.

1. **Risk:** accept a line whose whole text is `Risk Factors`, with an optional `A.`-`D.` item prefix; among the qualified lines
   take the FIRST in the body, not the last, so the cybersecurity cross-reference that broke parser 1.0.0 stays excluded. Give it an
   end that closes before the next item, so PBR's risk section does not run to the cap.
2. **Business:** when no `4.B Business Overview` heading exists, fall back to the `Item 4. Information on/about <company>` heading
   and cut the whole of Item 4 (SAP).
3. **Integrated reports (ASML, PBR):** a cross-reference mode -- read the report's closing 20-F cross-reference table, map each
   item (4.B, 3.D, 5) to the report section it names, and cut that section from the body by its own heading. The mode runs only
   when the standard heading cut finds no body heading for an item.
4. The 10-K patterns and every existing fixture's cut stay byte-identical (AC2). A section the filing truly lacks reads FAILED with
   a reason, never a contents-page cut.
5. Tests in `lib/research/filings/tests/test_document.py`: one plant per new rule (whole-line risk heading, first-not-last, the
   Item 4 fallback, a cross-reference table mapping), each with a contents-page decoy that must NOT be cut.

**Before running AC1:** copy the cached filing texts from the base checkout into your worktree (they are gitignored, never
committed): `cp -r /c/Dev/ajb_workspace/.scratch/r82_20f <your worktree>/.scratch/` -- AC1 reads `.scratch/r82_20f/`. PyMuPDF does
not load on this box; `document.py` imports it lazily since round 81, so nothing needs a stub except the filings test folder's
subprocess test (put an empty `fitz.py` on PYTHONPATH for the folder run).

Run `lib/research/filings/tests/` before your commit and report its last line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W323-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `document.py` and its test file only. Never pass `--write-pool`; never fetch a filing (the cache is the input).

## 3. SURFACES

<paths>
lib/research/filings/document.py
lib/research/filings/tests/test_document.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~323/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gg-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_cut.py" --crit AC1; echo "exit=$?"</invocation><expect>the five cached real 20-F filings each cut business, risk and mdna from their own body headings, 15 of 15 cells OK with plausible lengths (or FAILED with a named reason the check accepts); R82 CUT AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gg-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_cut.py" --crit AC2; echo "exit=$?"</invocation><expect>the 10-K fixture and dd-1's 20-F fixture sections hash as at the base; R82 CUT AC2: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~323 <0.9.0_WK_AMGT_RESAPP~323@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~323/AMGT_RESAPP.TO-AMGT-gg-1.the-20f-cutter-cuts-each-filings-own-headings.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines (AC1's 5 x 3 grid in full);
- the filings folder's last line;
- anything the real filings showed that the notes did not;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-81 analysis @284169f039 R1 / enrichment item 1 (row D1-W321-S1). Grounded round82_prep/GROUP_CUT_NOTES.md @57ab64a630. document.py is a site-Z producer path: the MERGE is a site-Z deploy under 1.0.0_SA_CTO~Z's half, and 1.0.0_SA_CTO~Z is down for the site Z reboot (msgs 1924, 1933): the worker builds now; the merge waits. Checks dry-run at the base: AC1 base: FAIL as expected (6 of 15); AC2 base: PASS as expected.

<status>pending</status>
<round>82</round>
<slot>0.9.0_WK_AMGT_RESAPP~323</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- issuer close 2026-10-09T08:1xZ: merged @9f252e010a (safe-merge of wk-AMGT_RESAPP-323 @780001dc22, 4 paths) as a SITE-Z DEPLOY under COO @7b84cfc5a9 + 1.0.0_SA_CTO~Z @83b31c3fa9 (signed for that head; its writer-census correction -- section_census, translate, proxy_officers also import document, all hand-run -- leaves DELTA = 0); NEVER-2 entry amgt-resapp-r82-gg1-sitez-cutter-merge CLOSED 2 of 2. On the merged tree: filings suite 233 passed (stub fitz, py3.12); r82_cut AC1 YES 15 of 15; AC2 YES. Row D1-W323-S1 (PBR wrong scope) is disarmed by gg-2 AMENDMENT 1 and carried to round 83.</status>
