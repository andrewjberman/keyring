# TO DSGN_IRPTV1.TO-IV-e-94 -- ONE batched repair cell: the CTO's three retirement rulings applied, two stale source pins re-pinned, five absent-to-null coalesces settled; three items explicitly deferred -- candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-94</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~52</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's retirement rulings msg 4446 and its ROUND-13 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_13_20261011.md` @72e8e2bb59 section 2 item 2 (a failing test is a regression with an owner or an assertion retired by a cited ruling), on the table `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~50/FAILING_ID_TABLE.json` | **Decomp cell:** `IV-e-94` (decomposition v16) | **outcome_ref:** FWD-1 (the suite bar) | **depends_on:** IV-e-90, IV-e-91 (both drained).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's existing worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~52/`.

**Two repos, one worktree pair.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo) at commit `7e8fa4fd`: DEV tip
`f74706ad` plus the contract catch-up candidate, approved for DEV by the CTO (msg 4554). Do not touch, amend or revert it. Portal files commit in the
portal repo with plain git and your author line (`git -c user.name="<serial>" -c user.email="<serial>@opal.agent" commit -F <msgfile> -- <paths>`);
records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace
`portal` gitlink. `node_modules` is a real local install: do NOT run `bun install`, do not touch `package.json` or `bun.lock`. Resolve bun with
`command -v bun`. Several tests in this scope diff or pin COMMITTED state: commit in small steps and re-run the affected file after each commit.

**The cell (`IV-e-94`).** At `7e8fa4fd` the Investor Reporting scope fails 20 ids. Read the table and its `.md` first: every id has an owner and a
cell, or a retirement asked. The CTO ruled the retirements (msg 4446). Do these SIX items, each its own portal commit, and record each under
`items` in `REPAIRS.json` {outcome: DONE or STOPPED, ids, evidence, row (when STOPPED)}:

1. **`diff_arms`** (5 ids: IVE109, IVE110, IVE111, IVE112, IVE25-AC2). RETIRED: "this file equals the commit my session started from" proves one
   cell once; it is not a standing property of a file other projects edit. Remove ONLY the `git diff <BASE> -- ModelPortfolios.tsx` arm from each
   test. **The behavioural arms stay and must pass**: show each test's remaining arms by name, and that the test still fails if its behavioural
   subject is broken (one mutant per test, made temporarily and reverted, never committed; say which mutant). A test left with no arm is not
   retired by this ruling: stop on that id with a row.
2. **`ycharts_token`** (1 id: fe-s-1 source-bounds). RETIRED as a source-token check, because the ratified report contract names its provider
   branch by that word. **Duty:** state from the entry's own commit what it guarded (`git log -S` on the token in that test's forbidden list, then
   read that commit's message and diff): `guarded` {commit, what}. If it guarded that the page never SHOWS the vendor's name, that becomes an
   assertion on RENDERED text in this same cell (`rendered_text_assertion: ADDED`, with the test and what it renders); if it guarded something
   else, say what and why no rendered assertion follows (`NOT_NEEDED`). Remove only that one token from the list; the other tokens stay.
3. **`business_date`** (2 ids: F25-AC2, the explicit-null arm). NOT retired until the contract's line is read. Print the contract's line for that
   field from the workspace `docs/contracts` (file, line, text). `NULL_ADMITTED_REGRESSION`: the contract admits null, so the parser's refusal
   (`requirePublicStatus`, portal c09fea54) is the regression: fix the product so an explicit null is admitted and rendered as the test expects.
   `NULL_FORBIDDEN_RETIRED`: the contract forbids null, so the arm is retired, citing that line, and replaced by "the parser refuses an
   explicit-null business_date". Absent and null stay two things either way.
4. **`ive116_pin`** and 5. **`ive137_pin`** (stale source-text pins after the tenant fix: the press branch now reads `submitWithTenant(scope, ...)`;
   `GenerateComposer.tsx` line ~267 now also tests `tenantMissingFor(scope, scopeRef)`). Re-pin each to the current source, and show the re-pinned
   test still FAILS on the pre-fix behaviour it was written to catch (the hand-over inside the guard; the resolve-before-add): one mutant each.
6. **`adapt_coalesces`** (1 id: F25-AC3). Five `?? null` coalesces in `src/pages/InvestorReporting/contracts/adapt.ts` (near lines 312, 941, 977,
   990, 1360) turn an absent member into null. For EACH site: carry absent as absent (`ABSENT_CARRIED`), or cite the contract line that admits null
   for that member (`CONTRACT_ADMITS_NULL`, with the line). A site whose consumer cannot take an absent value without a wider change is STOPPED
   with a row, not forced.

**Three items are DEFERRED, and you record them so (`outcome: DEFERRED`, `owner`, `reason`) and touch none of them:**
- `ive26_wire_generator` (IVE26-AC3): the generator cannot render members the contract declares as empty schemas; an open question for IRPT_BCKEND.
- `smoke_map` (fe-s-1 fixtures): the file is pinned at 12 keys by two other tests (row D2-W49-S8); the CTO rules which pin stands.
- `unprojected_grant` (five ids, row D2-W49-S7): waits on IRPT_BCKEND declaring the member on two response schemas.

Then run the whole scope once (`bun test src/pages/InvestorReporting`, output to a file under
`C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~52/`) and record `suite_after` {failed, fixed_ids, retired_ids: [{id,
ruling}], new_failing_ids} against the 20 ids failing at your base (measure that base set first, with one run before any edit). An id whose
assertion was retired is listed under `retired_ids` with the ruling (msg 4446 item, or the contract line); a renamed or removed test never silently
drops out of the count. `REPAIRS.json` also carries `portal_commit` (your last) and `product_files_changed`. Every portal commit that changes a
product file is a CANDIDATE for the CTO.

<criterion id="IV94-AC1" cell_refs="IV-e-94"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r16/p16_round16.py" . IV94-AC1</invocation><expect>IV94-AC1 PASS</expect></criterion>
`IV94-AC1` -- each of the six repair items is done or stopped with a row, with the evidence its ruling asks for, and the three deferrals are named with their owners. Base: FAIL.

<criterion id="IV94-AC2" cell_refs="IV-e-94"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r16/p16_round16.py" . IV94-AC2</invocation><expect>IV94-AC2 PASS</expect></criterion>
`IV94-AC2` -- after the repairs no new id fails, and every id of a done item is either passing or retired with its ruling. Base: FAIL.

<expected_criteria>IV94-AC1,IV94-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no package change,
  no dev server.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion the rulings did not retire. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W52-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~52/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-94.batched-repairs.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v16 (round 16), cell `IV-e-94`.
<owned_cells>IV-e-94</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV94-AC1,IV94-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~52/DSGN_IRPTV1.TO-IV-e-94.batched-repairs.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV94-AC1,IV94-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the portal commit hashes in order with one line each, each criterion's last line, each of the six items with its outcome and evidence, the contract line for business_date and the decision, what the ycharts entry guarded, the five coalesce sites, the three deferrals, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; the cell edits Investor Reporting tests, one parser decision and five lines of the page's adapter, and every product-file commit is a candidate the CTO reads before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the base state is measured by the check's own dry run, IV94-AC1 and IV94-AC2 FAIL at base (no record).
lane: the <paths> block IS the grant.
</preflight>
