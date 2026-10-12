# TO DSGN_IRPTV1.TO-IV-e-124 -- the unsupported-card reason on an UNCERTIFIED vendor report is worded like the face's one validation sentence, with no producer token -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-124</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~73</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6671, round-32 analysis section 2 item 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_32_20261012.md`): "the unsupported-card reason on an UNCERTIFIED vendor report is worded like the face's one validation sentence, with no producer token." | **Rows:** D2-W70-S4 | **Decomp cell:** `IV-e-124` (decomposition v32) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** none (portal DEV cf52fdbf00f2 is the base).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-73` (branch `wk-DSGN_IRPTV1-73`); run everything from its root unless a step says the portal. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~73/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-73/portal` is a PORTAL worktree (its own git repo, branch `wk-DSGN_IRPTV1-73-portal`) at portal DEV `cf52fdbf00f2`. Do not amend or revert anything
committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with
`.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` here is a LINK to the main portal checkout's real install:
no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only
with `git checkout -- <file>` on a file that has no uncommitted work of yours. ONE whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~73/`) is your base for `new_failing_ids`; the issuer measured the base at the previous head
as 1216 pass, 27 skip, 1 fail (F14-AC3, a diff check against DEV 1f3ce9f0, a known base failure).

**What is wrong.** IV-e-122 (on DEV) put ONE plain sentence on a vendor-kind report's face for the report's validation (`vendorValidationSentence` in
`portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx`), worded without the producer's status token. Each UNSUPPORTED card of the same report still prints the
older per-card reason from `unsupportedReason(validation)` in the same file (near line 137): "the producer's extraction validation is <code>; N value(s) could not be
confirmed", where `<code>` is the producer's own word (for example UNCERTIFIED) and the page's `reasonCode`. So the face says one thing in words and each card says it again
in the producer's vocabulary. The Opal report's card reason is `opalUnsupportedReason(validation)` (near line 201 the face chooses between the two); it is not this cell's.
Row D2-W70-S4 (`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md`, search the row id) holds the worker's account.

**The cell (`IV-e-124`).**
1. **The change.** `unsupportedReason` (the VENDOR path) returns a plain sentence for an unsupported card in the register of `vendorValidationSentence` (read it first, and
   match its wording and tone): it says the producer could not confirm this figure and how many values it could not confirm, with no producer status word
   (`CERTIFIED`, `UNCERTIFIED`, `FAILED`), no `reasonCode`, and no phrase "extraction validation". Choose the wording once, in one constant or one function, and say it
   (`reason_sentence` in the record is the exact sentence the card prints for a synthetic UNCERTIFIED report with a stated count). `opalUnsupportedReason` and every other
   Opal face stay byte-for-byte as before (`vendor_only true`, `opal_report_unchanged true`, shown by a rendered comparison of one synthetic Opal report before and after).
2. **The test and the suite.** One rendered test `__tests__/dsgn-irptv1/iv-e-124.unsupported-card-reason.test.tsx` (a vendor report whose validation is UNCERTIFIED prints the
   new sentence on each unsupported card and none of the three status words; an Opal report's cards are unchanged; a SUPPORTED card prints no reason), one temporary mutant
   (restore the old reason) that the test catches, then reverted. Re-golden an existing test only where it asserts this reason's old wording, and say which (the issuer expects
   `iv-e-122.vendor-validation-and-source.test.tsx` or an older analysis test may assert it). `suite_base`, `suite_after` {pass, skip, fail, new_failing_ids},
   `lint_errors`, `typecheck_errors` (run `bun run lint` and `bun run typecheck` after your last portal commit), `product_files_changed`, `portal_commit` (40 hex), and a
   screenshot of an opened synthetic UNCERTIFIED vendor report showing two unsupported cards, read by you. Record everything in `UNSUPPORTED_REASON.json` with the keys named in the
   criterion below.

<criterion id="IV124-AC1" cell_refs="IV-e-124"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py" . IV124-AC1</invocation><expect>IV124-AC1 PASS</expect></criterion>
`IV124-AC1` -- the unsupported-card reason on a vendor report is a plain sentence with no producer status word, an Opal report is unchanged, a rendered test and a mutant hold it, and a screenshot was read. Base: FAIL (no record).

<expected_criteria>IV124-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every file under `contracts/wire/` (generated) and `tabs/holdings/` (the other cell's, IV-e-123).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change. A dev server is
  allowed only for your own screenshot, on a port other than 5174, started from YOUR worktree and stopped when you finish.
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
  Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W73-S<k>`, with the real current UTC time; append as BYTES, never re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~73/
portal/src/pages/InvestorReporting/tabs/analysis/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-124.*
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-122.vendor-validation-and-source.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-124.unsupported-card-reason-in-words.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v32 (round 32), cell `IV-e-124`.
<owned_cells>IV-e-124</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV124-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~73/DSGN_IRPTV1.TO-IV-e-124.unsupported-card-reason-in-words.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV124-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the sentence a card now prints and where it is built; the Opal-report comparison; the test and its mutant; lint,
typecheck, and the suite before and after; what the screenshot shows; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one sentence on unsupported cards of a vendor-kind report changes wording. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
