# TO DSGN_IRPTV1.TO-IV-e-118 -- a page never prints an unmapped code as a title: where the census names nothing the card takes its section's name; the word for the chart row is proposed and lands in the census -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-118</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~66</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6344 (2026-10-12 ~02:17Z), on the issuer's read of the second walk (`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/WALK_2_RESULT_READ_20261012.md` @7db8985b06): "A page never prints an unmapped code as a title. Where the census names nothing, the card takes its section's name. That is a rule, one cell. The WORD for source_chart_representation is yours to propose from what the row shows; it lands in the census, not in the page." | **Rows:** NONE | **Decomp cell:** `IV-e-118` (decomposition v30) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** IV-e-116 (on portal DEV as ad774c6f9e).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-57` (the slot's worktree; branch `wk-dsgn-irptv1-r21-57`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~66/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-57/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` here is a LINK to the other slot's real install: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~66/`) is your base for `new_failing_ids`.

**What the walk found.** On a served vendor report (104 cards) 103 titles read a census name and ONE reads the raw token
`source_chart_representation`. The producer sends that `section_type` for a chart row
(`infra/aws/lambda/investor-reporting/ycharts/extract/extract.py` near line 773; `publication.py:71`); the pinned census names 33
S-codes and nothing for it; `portal/src/pages/InvestorReporting/contracts/vendorSectionNames.ts` (`vendorSectionTitle`, near line 63)
prints an unmapped code as itself. That was IV-e-115's own rule ("the page never invents a name"). The CTO has now ruled the other
half: a raw code is never a title.

**The cell (`IV-e-118`).** Read the issuer's record of the walk (`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/WALK_2_RESULT_READ_20261012.md`) and IV-e-116's record
(`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~64/LABEL_ONCE.json`: its `field_slug_read` shows how `section_id` is built).
1. **The rule (the product change).** A vendor card's title is never a `section_type` token the census does not name. Where the map
   holds no name for the row's `section_type`, the card takes the name of the SECTION the row belongs to. Read how the producer
   builds a chart row's `section_id` (it carries the section: verify at `extract.py` near 760-780 whether that is the S-code, a slug
   of the section title, or both) and resolve the section's census name from it. Say exactly what the page reads and cite the
   producer lines. If a row's section cannot be resolved either, the card prints a fixed plain word for "a section the census does
   not name" (choose the wording once, in one constant, and say it), NEVER the token. `rule` {file, line, unmapped_code_printed:
   false, resolves_from}.
2. **The word, proposed, in the census.** What a `source_chart_representation` row IS should be said to the reader (for example as
   the card's Label or a suffix beside the section's name, so a chart card is not mistaken for a value card of the same section):
   propose the word from what the row shows (its `units` token is `chart`; read `certify.py:173` and `:359` for what the producer
   says the row represents). The word lands in the CENSUS file `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json` (in your grant for this
   order), as a new entry in a member that names row types, NOT as a 34th section name: the 33 section names stay byte-for-byte
   (`census.section_names_unchanged: 33`). The page reads the word from the census through the same vendored path the 33 names take
   (IV-e-115's drift test compares the page's map with the census: read it, extend it to the new member, it must pass:
   `census.drift_test_passes`). `chart_card` {title_from: "SECTION_NAME", word_proposed, word_basis, where_printed}. The word is a
   PROPOSAL: the CTO reads it in the candidate.
3. A rendered test under `__tests__/dsgn-irptv1/` named `iv-e-118.no-unmapped-code-title.test.tsx` (a chart row renders its
   section's name and the census word, never the token; an S-code row unchanged; a row whose section cannot be resolved prints the
   fixed wording), one temporary mutant reverted. Measure the suite BEFORE any edit (`suite_base` {pass, skip, fail}) and after
   (`suite_after` {pass, skip, fail, new_failing_ids}).
4. A screenshot of an opened vendor report from a build with a synthetic fixture that includes a chart row, read by you.
   `lint_errors`, `typecheck_errors`, `product_files_changed`, `portal_commit`. Record `UNMAPPED_TITLE_RULE.json`.

<criterion id="IV118-AC1" cell_refs="IV-e-118"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_round30.py" . IV118-AC1</invocation><expect>IV118-AC1 PASS</expect></criterion>
`IV118-AC1` -- no unmapped code is printed as a title, the chart card takes its section's name, a word for the chart row is proposed and lands in the census with the 33 names unchanged, a rendered test holds it, and a screenshot was read. Base: FAIL.

<expected_criteria>IV118-AC1</expected_criteria>

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
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W66-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~66/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-118.no-unmapped-code-as-a-title.md
docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v30 (round 30), cell `IV-e-118`.
<owned_cells>IV-e-118</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV118-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~66/DSGN_IRPTV1.TO-IV-e-118.no-unmapped-code-as-a-title.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV118-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the rule, where it is, and what the page resolves the section from (with the producer lines); the word you propose for a chart row, why, and where it prints; what you added to the census and that the 33 names are unchanged; the test and its mutant; lint, typecheck, and the suite before and after; what the screenshot shows; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one card title on a vendor report changes from a raw token to its section's name plus a census word; the census gains one member. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
