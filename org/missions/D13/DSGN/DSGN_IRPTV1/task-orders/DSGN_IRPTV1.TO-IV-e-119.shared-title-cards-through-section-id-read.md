# TO DSGN_IRPTV1.TO-IV-e-119 -- a READ, no build: for the 46 cards that share one title, does section_id through the census give distinct names, and how many stay shared

<to_id>DSGN_IRPTV1.TO-IV-e-119</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~67</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6344 (2026-10-12 ~02:17Z), on the issuer's read of the second walk (`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/WALK_2_RESULT_READ_20261012.md` @7db8985b06): "The 46 sharing a title: first a read, no build. For those 46, does section_id through the census give distinct names, and how many stay shared. If all 46 separate, the build is the page's; if not, the remainder goes to 2.0.0_SA_COO~P2 as a wire member." | **Rows:** NONE | **Decomp cell:** `IV-e-119` (decomposition v30) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** IV-e-116 (its field-slug read).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~67/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` is a real local install that another worktree junctions to: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~67/`) is your base for `new_failing_ids`.

**What the walk found.** On a served vendor report 46 cards carry the title "Fundamentals" (served `section_type` S18, 46 of 104)
and nothing on a card says which fundamental it is: the wire carries no field name. Every section does carry `section_id` (104 of
104). IV-e-116 read the producer's rule (`ycharts/extract/extract.py` near 704-707: `section_id` is
`"<census code>.<slug of the field>.c<column>"`) and found 58 of 58 derivable slugs map back to exactly ONE census field. That read
used the census file alone. The CTO now asks the question for the 46 themselves.

**The cell (`IV-e-119`).** A read. `product_change: false`: you edit no portal file and no workspace product file.
1. **The 46 section ids, from the best source you can lawfully read**, stated in `source` and `source_basis`:
   (a) `PRODUCER_RULE_ON_CENSUS`: apply the producer's rule to the census's S18 fields
   (`docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`), reading `extract.py` to learn how many COLUMNS a
   field row yields and what a column is (the compared securities? periods?). Say whether the rule yields 46 for S18 on a report of
   the walked shape, and if not, what count it yields and why the served count could differ;
   (b) `SERVED_ANSWER`: only if a retained answer of the producer already sits in the repo as a fixture or a recorded sample (the
   producer's own test fixtures under `infra/aws/lambda/investor-reporting/`): read its S18 `section_id` values. You make NO AWS
   call and NO live request in this cell; if no such file exists, say so and use (a).
2. **Through the census.** For each of the cards, resolve a NAME from its `section_id`: the census field the slug maps to, and what
   the column part adds (if two cards differ only by column, what would tell them apart on the face: is the column's meaning on the
   wire, in `section_id` alone, or nowhere?). `cards`, `named` (a census field resolved), `unnamed`, `distinct_names` (distinct
   resolved names, counting the column only if its meaning can be printed from what the wire carries), `still_shared` (the cards
   whose resolved name another card also carries, plus the unnamed), `groups` (the sizes of the groups that stay shared).
3. **The verdict**, by the CTO's own test: `ALL_SEPARATE` only if `still_shared` is 0; `SOME_SHARED` otherwise, with
   `remainder_needs` saying exactly what wire member would separate the remainder (its name is the backend's to choose: describe what
   it must carry); `NOT_ESTABLISHED` if neither source lets you count, with what is missing.
4. Do the same count, briefly, for the other six title groups the walk found with more than one card (S01 2, S03 6, S10 4, S14 5,
   S15 35, S16 5): `other_groups` [{section_type, cards, still_shared}], so the ruling is not made on S18 alone.
5. `method` (so another seat would count the same way), `limits`. Record `SHARED_TITLE_46.json`. A tracked script
   (`shared_title_count.py`) beside it produces every count; it must pass `bash .tools/commit-gate.sh`.

<criterion id="IV119-AC1" cell_refs="IV-e-119"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_round30.py" . IV119-AC1</invocation><expect>IV119-AC1 PASS</expect></criterion>
`IV119-AC1` -- for the cards that share one title it is counted how many take a distinct name through section_id and the census and how many stay shared, with the source of the section ids stated, and nothing is built. Base: FAIL.

<expected_criteria>IV119-AC1</expected_criteria>

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
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W67-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~67/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-119.shared-title-cards-through-section-id-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v30 (round 30), cell `IV-e-119`.
<owned_cells>IV-e-119</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV119-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~67/DSGN_IRPTV1.TO-IV-e-119.shared-title-cards-through-section-id-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV119-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; where the section ids came from and why; how many of the 46 take a distinct name, how many stay shared and in what groups; what the column part means and whether the wire lets the page print it; the verdict by the CTO's test and what the remainder would need; the same for the other six groups; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a count record and its script; nothing is built.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
