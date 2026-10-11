# TO DSGN_IRPTV1.TO-IV-e-113 -- an opened vendor report reads section codes for titles and 'Unit: unknown' on every card: page or producer -- a read, no product change

<to_id>DSGN_IRPTV1.TO-IV-e-113</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~62</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5562 (2026-10-11 ~18:27Z) on the laptop's rendered walk (`org/tier1_exec/4.0.0_SA_CRO/deliverables/XB_C5CE_IRPT_DEV_WALK_RESULT_20261011.md`): "S21: page or producer is the first cell, not a guess. For that vendor report, the served sections answer's key names and whether title and unit are sent, beside what the adapter does with them." | **Rows:** DSGN_IRPTV1-D2-S21 | **Decomp cell:** `IV-e-113` (decomposition v26) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** IV-e-112 (the same slot; it runs after it).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~62/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` is a real local install that another worktree junctions to: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~62/`) is your base for `new_failing_ids`.

**What was seen (row D2-S21).** In the laptop's walk (face 7 of the result file named above), an opened vendor report on a served
answer showed 104 section cards whose title and Label each read as a section code of the form `S03`, "Unit: unknown" on all 104, the
token `source_chart_representation` twice, no validation line and no "Source:" line on the face. Every synthetic fixture this project
rendered carried titles and units, so no screenshot showed it. You change NO product file.

**The cell (`IV-e-113`).** For each of TITLE and UNIT (and, in `also`, the validation line and the source line), three reads:
1. **The contract.** The analysis-report response schema and the report document schema it references (workspace
   `infra/aws/lambda/investor-reporting/_contracts/` and `docs/contracts/investor-reporting/v1/`; if a path named here is not in your
   tree, find the same schema by name and say where): does a section DECLARE a human title (or label) and a unit, required or
   optional? `contract_declares`, `contract_where` (file and JSON pointer).
2. **The producer's own fixtures.** `_contracts/fixtures/AnalysisReport*.valid.json` and any vendor-report fixture: does a section
   carry them? `producer_fixture_sends`, `fixture_where`. Then the producer's CODE for a vendor report's sections (the gold or Lambda
   path that builds them: find it from the route's handler under `infra/aws/lambda/investor-reporting/`): where would a title and a unit
   come from, and can they be absent or equal to the section code for a real vendor document? Say what you read (file and line).
3. **The adapter and the card.** `contracts/adapt.ts` (the sections adapter) and the section card component: which wire member
   becomes the card's title and its Label, and its unit; what the card prints when that member is absent, null or equals the code
   (`adapter_reads`, `adapter_where`, `page_prints_when_absent`). Where does the literal "Unit: unknown" come from?
4. **A served answer.** No dell2 seat can sign in. If a captured served sections answer exists in the tree or in the private
   evidence folders (`C:/dev/_irpt_private_evidence_20261009/`; search by the route's operation name; read in place, counts and key
   names only, no value), read its key names: `served_answer_read: true` with `served_answer_how`. If none exists,
   `served_answer_read: false` with why, and what exact read 2.0.0_SA_COO~P2 (the producer's issuer) would make.
5. **Verdict**, with its reason: `PAGE` (the wire carries a title and a unit and the page drops or mislabels them), `PRODUCER` (the
   served answer does not send them, or sends the code as the title), `BOTH`, or `NOT_ESTABLISHED` (say exactly which read is
   missing). `product_files_changed: []`. Record `SECTION_TITLE_UNIT.json`.

<criterion id="IV113-AC1" cell_refs="IV-e-113"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r26/p26_round26.py" . IV113-AC1</invocation><expect>IV113-AC1 PASS</expect></criterion>
`IV113-AC1` -- title and unit are each traced through the contract, the producer's fixture and the adapter, what the card prints when they are absent is stated, and the verdict is the page, the producer, both or not established. Base: FAIL.

<expected_criteria>IV113-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The contract and the producer's fixtures (workspace files)
  are read, never edited. No file under `contracts/wire/` is hand-edited (generated; one command regenerates it:
  `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no
  `bun install`, no package change, no dev server on any port.
- **Every portal commit is followed by `bun run lint` and `bun run typecheck`**; a lint ERROR is fixed before you report (the count goes in
  the record as `lint_errors`, and typecheck's as `typecheck_errors`).
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W62-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~62/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-113.section-title-and-unit-page-or-producer.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v26 (round 26), cell `IV-e-113`.
<owned_cells>IV-e-113</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV113-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~62/DSGN_IRPTV1.TO-IV-e-113.section-title-and-unit-page-or-producer.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV113-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; for title and for unit: what the contract declares, what the producer's fixture and code send, what the adapter and card do, where 'Unit: unknown' comes from; the same in a line each for the validation and source lines; whether a served answer was read; the verdict and why; what the producer's issuer would need to read; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a read; no product file changes.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
