# TO DSGN_IRPTV1.TO-IV-e-114 -- one hygiene cell on the Holdings tab: the React colgroup warning, the low-contrast eyebrow text, and the navy bands counted against the design law -- a visual change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-114</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~62</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5562 (2026-10-11 ~18:27Z) on the laptop's rendered walk (`org/tier1_exec/4.0.0_SA_CRO/deliverables/XB_C5CE_IRPT_DEV_WALK_RESULT_20261011.md`): "S23: one hygiene cell." | **Rows:** DSGN_IRPTV1-D2-S23 | **Decomp cell:** `IV-e-114` (decomposition v26) | **outcome_ref:** FWD-1 (the Holdings hop's face) | **depends_on:** IV-e-113 (the same slot; it runs after it).

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

**What was seen (row D2-S23).** The laptop's walk, on the Holdings tab: one React warning, "whitespace text nodes cannot be a child of
colgroup" (a hydration-error class); 32 to 36 text elements under 3:1 contrast (the lavender eyebrow text such as ALL CATEGORIES on
the light canvas); 5 full-width navy bands where `portal/DESIGN.md` C3 allows one per page.

**The cell (`IV-e-114`).** Read `portal/CLAUDE.md` (Color law) and `portal/DESIGN.md` (C1 to C12) whole before any edit.
1. **The colgroup warning.** Reproduce it in a rendered test or a build's console (`colgroup_warning.present_before`, `how_measured`),
   find the `<colgroup>` whose JSX leaves a whitespace text node, fix it, and show it gone (`present_after: false`).
2. **Contrast.** Measure the text elements on the Holdings tab whose colour against their own background is under 3:1 (state your
   method: computed styles in the built page through the driver, with the count and the distinct colour pairs): `failing_before`.
   Fix the ones on the LIGHT canvas or a white panel by using the design system's own ink tokens (navy for text on the canvas; the
   lavender eyebrow is legal on the dark band only); do not invent a colour. `failing_after`, with what remains and why (a text on
   the dark band that already passes there is not a failure).
3. **The bands.** Count the full-width navy bands on the Holdings tab and classify each by the design law's own words: is a panel's
   header strip or footer strip a "band" under C3, or is C3's band the one deliberate full-bleed section? Quote the clause
   (`per_design_law`), give `count` and `where` (file and component for each). If the law, as written, counts panel header strips,
   do NOT restyle every panel in this cell: say so and file a row for a design ruling; change only what a clause unambiguously
   forbids and you can fix within the page's own files.
4. A screenshot of the Holdings tab from a build after your changes, read by you (`screenshots`, `screenshots_read`), saying in a
   sentence what changed visibly. `lint_errors`, `typecheck_errors`, `suite_after`, `product_files_changed`, `portal_commit`.
   Record `HYGIENE_26.json`.

<criterion id="IV114-AC1" cell_refs="IV-e-114"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r26/p26_round26.py" . IV114-AC1</invocation><expect>IV114-AC1 PASS</expect></criterion>
`IV114-AC1` -- the colgroup warning is gone, the count of low-contrast texts does not rise and its fix uses the design system's tokens, the bands are counted against the design law's own clause, and a screenshot was read. Base: FAIL.

<expected_criteria>IV114-AC1</expected_criteria>

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
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-114.hygiene-colgroup-contrast-bands.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v26 (round 26), cell `IV-e-114`.
<owned_cells>IV-e-114</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV114-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~62/DSGN_IRPTV1.TO-IV-e-114.hygiene-colgroup-contrast-bands.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV114-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the colgroup fix (file:line); the contrast count before and after, the colour pairs, and what remains; the band count, the clause quoted, and whether a design ruling is needed; what the screenshot shows; `product_files_changed`; lint, typecheck and suite; the portal commit; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; markup and ink-token changes on one tab; no request, route or contract change. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
