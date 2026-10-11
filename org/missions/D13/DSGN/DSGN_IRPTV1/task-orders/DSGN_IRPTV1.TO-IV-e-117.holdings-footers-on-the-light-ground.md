# TO DSGN_IRPTV1.TO-IV-e-117 -- the Holdings tab passes PanelFooter its light ground, removing the navy footer strips this page draws; no shared component is restyled -- a small product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-117</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~65</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 5852 (2026-10-11 ~21:07Z): "the shared src/ui components are not restyled by this project. Inside your grant, one cell: the Holdings tab passes PanelFooter its light ground, which removes two of the five. The three header strips go to the design system's owner." | **Rows:** DSGN_IRPTV1-D2-W62-S3 | **Decomp cell:** `IV-e-117` (decomposition v29) | **outcome_ref:** FWD-1, the Holdings tab | **depends_on:** IV-e-116 (on portal DEV as ad774c6f9e).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-57` (the slot's worktree; branch `wk-dsgn-irptv1-r21-57`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~65/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-57/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` here is a LINK to the other slot's real install: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~65/`) is your base for `new_failing_ids`.

**What is wrong (row D2-W62-S3, ruled by the CTO).** The Holdings tab draws five full-width navy strips from the shared panel
components: three headers and two footers. `portal/DESIGN.md` C3 says navy is text and hairline only, never a container fill. The
shared components under `src/ui/` belong to the design system and are NOT restyled here; the header strips go to its owner. The
footers are this page's to fix, because the shared `PanelFooter` already takes a `ground` prop: `'band'` (the default, navy) or
`'light'` (no band, a hairline above, the muted ink of a footnote on white): `src/ui/components/panels/PanelFooter.tsx`, read it.

**The cell (`IV-e-117`).** Read IV-e-114's record and measurements first
(`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~62/`, `measure-prod-before.json` and how it counted the bands).
1. **The change.** Every `PanelFooter` the Holdings tab renders passes `ground="light"`: the call sites are under
   `src/pages/InvestorReporting/tabs/holdings/` (three files call it today: `SecurityList.tsx`, `HoldingsTreemap.tsx`,
   `AllocationBars.tsx`; verify, and say which of them render on the tab and in which view, since the row measured two footer strips).
   Change every one that the tab can render, so no view of the tab keeps a navy footer. `footers`: [{file, line, ground: "light",
   renders_when}]. You change NO file under `src/ui/` (`shared_ui_changed: false`) and no other tab's footer.
2. **The light footer must sit on a light ground.** Read what is behind each footer: the light variant paints no background of its
   own, so if the panel that holds it is itself dark (a `Panel` variant that resolves to the band), the muted ink would land on navy.
   For each footer say what ground it sits on after the change and measure the footer text's contrast against it from the built page
   (computed colours, as IV-e-114 measured): `footer_text_contrast` {ratio, ink, ground, how}; it must be 4.5 or more. If a footer's
   panel is dark, do not restyle the shared Panel: say so in the record and file a row, and leave that one footer on the band.
3. **Measured before and after** on a build with the synthetic fixture IV-e-114 used: `navy_strips` {before, after, removed, how}
   counting full-width navy fills on the Holdings tab exactly as IV-e-114's measure did (reuse its script from its folder; copy it into
   yours, do not edit theirs). The three header strips stay: say that they do.
4. A rendered test under `__tests__/dsgn-irptv1/` (each Holdings footer renders without the band's background class and with the
   hairline; the source words and the day still print), one temporary mutant reverted. The existing footer tests still pass
   (`iv-e-117.footer-source-words.test.tsx` is an older cell's file of another numbering: name your new file
   `iv-e-117b.holdings-footers-light-ground.test.tsx` and do not edit the older one unless it fails, and then say why).
5. A screenshot of the Holdings tab from the build (each view that shows a footer), read by you: `screenshots`, `screenshot_read`.
   `lint_errors`, `typecheck_errors`, `suite_after`, `product_files_changed`, `portal_commit`. Record `HOLDINGS_FOOTER_LIGHT.json`.

<criterion id="IV117-AC1" cell_refs="IV-e-117"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r29/p29_round29.py" . IV117-AC1</invocation><expect>IV117-AC1 PASS</expect></criterion>
`IV117-AC1` -- the Holdings tab's footers sit on the light ground with no shared component changed, at least two navy strips are gone by measurement, the footer text keeps its contrast, a rendered test holds it, and a screenshot was read. Base: FAIL.

<expected_criteria>IV117-AC1</expected_criteria>

## AMENDMENT 1 (2.0.0_SA_COO~D2, 2026-10-11 ~22:5xZ) -- the suite clause: no NEW failure over the measured base

The check required `suite_after.fail` 0. The issuer wrote that without measuring the base at the time of the cut: the slot's
workspace half was brought to trunk for this order, and trunk now carries a contract change (the optional `commentary_requested` on
`AnalysisSubmissionRequest`, IRPT_BCKEND IB-pr-455 @74bbdbb322) that the portal's committed wire file does not yet hold. Two portal
tests that compare the two fail at the BASE (`iv-e-26` IVE26-AC3, `iv-e-98` IVE98), before any edit of this cell. They are not this
cell's and regenerating the wire file is outside its grant; the worker refused to do it, correctly.

The check now reads: `suite_base.fail` and `suite_after.fail` are counts, `suite_after.fail` is no greater than `suite_base.fail`,
and `suite_after.new_failing_ids` is `[]`. Nothing else in the criterion changes. The record already carries those members; re-run
the criterion, set the proof instance's row to what it prints, and flip the status if it passes.

Gate limb that graded this modification: none (LIMB 6 fires on a newly added order only).

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
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W65-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~65/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-117.holdings-footers-on-the-light-ground.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v29 (round 29), cell `IV-e-117`.
<owned_cells>IV-e-117</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV117-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~65/DSGN_IRPTV1.TO-IV-e-117.holdings-footers-on-the-light-ground.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV117-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; which footers changed (file and line) and when each renders; what ground each sits on and the measured contrast; the navy strip count before and after and how counted; that no shared component changed; the test and its mutant; lint, typecheck and suite lines; what the screenshot shows; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; the footer strip of the Holdings tab's panels turns from navy to a hairline on white; no shared component and no other tab changes. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
