# TO DSGN_IRPTV1.TO-IV-e-110 -- the Holdings securities table says in a sentence how much of the total sits in sleeves it does not itemise, and why -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-110</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~60</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5447 (2026-10-11 ~17:17Z): "when the listed securities sum to less than the card, the table says in a sentence how much sits in sleeves it does not itemise, and names the two reasons the producer gives: cash only, or detail withheld. The amount is the card less the listed rows, from the served nodes." | **Rows:** DSGN_IRPTV1-D2-S18 | **Decomp cell:** `IV-e-110` (decomposition v24) | **outcome_ref:** FWD-1 (the Holdings hop) | **depends_on:** IV-e-108 (the same slot and the same face; it runs after it).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-57` (the slot's worktree; branch `wk-dsgn-irptv1-r21-57`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~60/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-57/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` here is a LINK to the other slot's real install: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~60/`) is your base for `new_failing_ids`.

**What is wrong (row D2-S18, ruled a product defect).** The securities table lists SECURITY nodes only. A served holdings answer does
carry sleeves with no security node beneath them: IRPT_BCKEND's read of one firm's publication for one day found 1,229 of 7,620 sleeves
so, 333 with a nonzero amount, most cash only, 8 labelled as a withheld drill; by the producer's rule the gold runner emits such a
sleeve when the drill is withheld or it holds cash only (2.0.0_SA_COO~P2's cell IB-pr-440; read its record under
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/` if it has drained to your tree, and say if it has not). So the table can list less than
the total card and says nothing. The producer is NOT changed: withholding a drill is its rule.

**The cell (`IV-e-110`).** It runs after IV-e-108 on this slot, on top of its commits; read its record first
(`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~60/HOLDINGS_FACE.json`). Read `portal/CLAUDE.md` (Color law) and
`portal/DESIGN.md`: the sentence is navy text inside the table's white panel; no new band, colour or component.
1. **The amount** is the total the card shows less the sum of the listed rows, computed from the served nodes the page already holds
   (`amount_rule`: say exactly which nodes and members). No new request. When an account is picked, the same rule over that account.
2. **The sentence**, under the table, only when that amount is above zero (a rounding tolerance of one cent): it says how much of the
   total is held in sleeves the table does not itemise, as an amount and a share, and names the two reasons the producer gives: cash
   only, or detail withheld. If a served node says which of the two applies to it (read the contract and the producer's fixture:
   `infra/aws/lambda/investor-reporting/_contracts/`), say each amount by its reason; if it does not, name both reasons without
   apportioning, and say so in the record. `sentence` {text (as rendered for the fixture), where {file, line}}; `reasons_named` (the two
   phrases as printed).
3. **Absent when whole.** When the listed rows sum to the card, no sentence. `cases`: [{case, sentence_shown}] with at least one of
   each, from a rendered test under `__tests__/dsgn-irptv1/` with one temporary mutant (`test` {id, passes, mutant {what, failed}}).
4. **A screenshot, read by you**, from a build with the corrected driver and the synthetic two-account fixture (its two SMA sleeves
   have no securities: 250,000 of 1,000,000): the sentence under the table. `screenshots`, `screenshots_read`. Synthetic data only.
5. `lint_errors`, `typecheck_errors`, `suite_after`, `product_files_changed`, `portal_commit`. Record `UNLISTED_SLEEVES.json`.

<criterion id="IV110-AC1" cell_refs="IV-e-110"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r24/p24_round24.py" . IV110-AC1</invocation><expect>IV110-AC1 PASS</expect></criterion>
`IV110-AC1` -- when the listed securities sum to less than the card the table says in a sentence how much it does not itemise and names the two reasons, the sentence is absent when the rows sum to the card, a rendered test holds it, and a screenshot was read. Base: FAIL.

<expected_criteria>IV110-AC1</expected_criteria>

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
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W60-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~60/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-110.holdings-table-states-unlisted-sleeves.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v24 (round 24), cell `IV-e-110`.
<owned_cells>IV-e-110</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV110-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~60/DSGN_IRPTV1.TO-IV-e-110.holdings-table-states-unlisted-sleeves.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV110-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the sentence as rendered and where it is drawn; the amount's rule; whether a node says which reason applies; the cases; the test and its mutant; what the screenshot shows; `product_files_changed`; lint, typecheck and suite; the portal commit; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one sentence under one table on a client-facing page, from numbers the page already holds; no request, route or contract change. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
