# TO DSGN_IRPTV1.TO-IV-e-116 -- a vendor card whose Label equals its title prints the title once; and a read of whether the wire's section id carries a field slug the census can name exactly -- a small product change and a read; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-116</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~64</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 5782 (2026-10-11 ~20:31Z): "next cell, row W63-S2: a card whose label equals its title prints the title once. Two cards reading 'Key Stats / Key Stats' tell nobody which statistic." | **Rows:** DSGN_IRPTV1-D2-W63-S2 | **Decomp cell:** `IV-e-116` (decomposition v28) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** IV-e-115 (on portal DEV as 1bf9e1f3).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-57` (the slot's worktree; branch `wk-dsgn-irptv1-r21-57`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~64/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-57/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` here is a LINK to the other slot's real install: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~64/`) is your base for `new_failing_ids`.

**What is wrong (row D2-W63-S2).** After IV-e-115 a vendor card's title AND its Label both read the census section name
(`contracts/adapt.ts`, `adaptAnalysisSections`: `title: vendorSectionTitle(section.section_type)` and the value's
`label: vendorSectionTitle(section.section_type)`). The producer emits one card per FIELD row under one section code, so several cards
read "Key Stats" twice over and nothing says which statistic each is. The wire carries no field name; `section_id` holds a slug.

**The cell (`IV-e-116`).** Read IV-e-115's record first
(`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~63/SECTION_NAMES_UNITS.json`) and the screenshot beside it.
1. **Printed once (the product change).** When a vendor value's Label equals its card's title, the card does not print the same words
   twice: the Label cell for that row is left out or reads empty in a way a reader does not take for missing data (read how the card
   draws the row, `tabs/analysis/NativeSections.tsx` near lines 164-176, and choose the smaller change; say which and why). A Label
   that DIFFERS from the title prints as today (`label_differs_unchanged`). An Opal card is unchanged (`opal_unchanged`), shown by a
   test that pins it. `label_equals_title` {printed_once, where {file, line}}.
2. **The field slug: a READ, no product change** (`field_slug_read.product_change: false`). The pinned census
   (`docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`, a workspace file you READ and never edit) lists
   `fields` under each of its 33 sections. Read how the producer builds `section_id` for a field row (IV-e-113's record cites
   `extract.py` near lines 707-714 and 777: verify the lines): does `section_id` contain a slug that identifies the census field?
   Count: `census_fields` (how many field rows the census holds), `slugs_derivable` (for how many of them the producer's rule yields a
   slug you can compute from the census alone), `exact_matches` (how many of those slugs map back to exactly ONE census field name,
   with no collision inside its section). State the `method` exactly. Do NOT wire it into the page: if the mapping is exact for every
   field, say so and the reviewer rules whether the Label reads the census field name; a guess is worse than a blank.
3. A rendered test under `__tests__/dsgn-irptv1/` (a vendor report with two cards of one section: the title appears once per card; a
   card with a differing Label unchanged; an Opal card unchanged), one temporary mutant. A screenshot of an opened vendor report from a
   build with a synthetic fixture, read by you. `lint_errors`, `typecheck_errors`, `suite_after`, `product_files_changed`,
   `portal_commit`. Record `LABEL_ONCE.json`.

<criterion id="IV116-AC1" cell_refs="IV-e-116"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r28/p28_round28.py" . IV116-AC1</invocation><expect>IV116-AC1 PASS</expect></criterion>
`IV116-AC1` -- a vendor card whose Label equals its title prints the title once, a differing Label and an Opal card are unchanged, the section id's field slug is read against the census with no product change for it, a rendered test holds it, and a screenshot was read. Base: FAIL.

<expected_criteria>IV116-AC1</expected_criteria>

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
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W64-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~64/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-116.vendor-card-title-once-and-field-slug-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v28 (round 28), cell `IV-e-116`.
<owned_cells>IV-e-116</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV116-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~64/DSGN_IRPTV1.TO-IV-e-116.vendor-card-title-once-and-field-slug-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV116-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; what a card prints now when Label equals title, and where the change is; that a differing Label and an Opal card are unchanged and how shown; the field-slug read: the producer's rule for section_id with file and line, the three counts and the method, and whether the mapping is exact; the test and its mutant; what the screenshot shows; `product_files_changed`; lint, typecheck and suite; the portal commit; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one repeated word removed from a vendor card; the field-name question is read, not built. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
