# TO DSGN_IRPTV1.TO-IV-e-97 -- tooling hygiene: the lock refreshed once on purpose, playwright-core declared or its skip stated, the calendar's provenance made stable -- candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-97</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~53</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-17 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_17_20261011.md` @e4345abd6e, section 4 item 4 (rows D2-W49-S3, S4 and S1) | **Decomp cell:** `IV-e-97` (decomposition v17) | **outcome_ref:** FWD-1 | **depends_on:** IV-e-96.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's existing worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/`.

**Two repos, one worktree pair.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo). Its base for this order is the commit
your spawn prompt names. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your
author line (`git -c user.name="<serial>" -c user.email="<serial>@opal.agent" commit -F <msgfile> -- <paths>`); records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. Resolve bun
with `command -v bun`. Several tests in this scope diff or pin COMMITTED state: COMMIT FIRST, then run, then make any temporary mutant, and
revert a mutant only with `git checkout -- <file>` on a file that has NO uncommitted work of yours in it.

Measure your base first: one whole-scope run before any edit (`bun test src/pages/InvestorReporting`, about 100 seconds, output to a file under
`C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~53/`); the failing ids there are what `new_failing_ids` is measured
against (file path plus full test name, spelled as `deliverables/0.9.0_WK_DSGN_IRPTV1~43/SUITE_SAMPLE.json` spells them).

**The cell (`IV-e-97`).** Three parts, each its own portal commit; record each in `TOOLING.json`.

1. **The lock, refreshed once, on purpose** (row D2-W49-S3). The committed `bun.lock` is stale against `package.json`: any `bun add` or
   non-frozen install re-resolves five packages (the typescript-eslint plugin family and ts-api-utils) and prunes 57 entries. Do that ONCE, on
   its own commit: `bun install` (THIS order permits it, here only), with `package.json`'s dependencies, devDependencies and overrides
   UNCHANGED, so the lock states what `package.json` already asks for. Before and after: `bun run build` and one sha256 over the built
   folder's files in sorted order (the same method `deliverables/0.9.0_WK_DSGN_IRPTV1~49/TEST_HYGIENE.json` records) -- the hashes must be
   EQUAL; if they differ, revert the lock commit, record what moved, and STOP with a row. `happy-dom` stays at 20.14.5 (the override the CTO
   required). `lock`: {refreshed, package_json_dependencies_changed, packages_moved, moved: [{name, before, after}], pruned,
   build_hash_before, build_hash_after, build_equal, happy_dom}.
2. **playwright-core** (row D2-W49-S4). `iv-e-20.bands` and `iv-e-20.scrollbars` import a driver that `package.json` does not declare; they
   pass only where a shared install happens to hold it. Read both tests and decide from what they do: if they need the driver to run, DECLARE
   `playwright-core` as a devDependency at the exact version the shared install holds (`DECLARED`; that one addition is permitted, on its own
   commit, and the build hash must stay equal); if they already skip when it is absent, make the skip explicit and printed, so a tree without
   it reports SKIPPED with the reason, never a failed import (`SKIP_STATED`). `playwright_core`: {outcome, evidence}.
3. **The calendar's provenance** (row D2-W49-S1). The portal calendar generator writes a `calendarSource` string that depends on whether the
   box has `pandas_market_calendars`; two boxes write two strings for the same bytes. Read the generator (find it from
   `deliverables/0.9.0_WK_DSGN_IRPTV1~49/CALENDAR_FIX.json`). One of: the generator REFUSES to write from the hardcoded fallback
   (`REFUSES_FALLBACK`), or the output carries the source as a claim a reader can reject on, with the day data proven identical
   (`CARRIES_CLAIM`). If the generator is outside your grant, STOP that part with a row naming the file. A test holds the choice.
   `calendar_source`: {outcome, test_id, passes}.

Then one whole-scope run after; `suite_after`; `portal_commit`.

<criterion id="IV97-AC1" cell_refs="IV-e-97"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r17/p17_round17.py" . IV97-AC1</invocation><expect>IV97-AC1 PASS</expect></criterion>
`IV97-AC1` -- the lock is refreshed once with package.json's dependencies unchanged, the build is byte-equal, happy-dom is held, and no new id fails. Base: FAIL.

<criterion id="IV97-AC2" cell_refs="IV-e-97"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r17/p17_round17.py" . IV97-AC2</invocation><expect>IV97-AC2 PASS</expect></criterion>
`IV97-AC2` -- playwright-core is declared or its skip is stated, and the calendar's provenance is refused or carried as a claim, held by a test. Base: FAIL.

<expected_criteria>IV97-AC1,IV97-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no dev server; `bun install` and at most the ONE devDependency this order names, nothing else.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W53-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/
portal/src/pages/InvestorReporting/
portal/package.json
portal/bun.lock
portal/scripts/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-97.tooling-hygiene.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v17 (round 17), cell `IV-e-97`.
<owned_cells>IV-e-97</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV97-AC1,IV97-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/DSGN_IRPTV1.TO-IV-e-97.tooling-hygiene.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV97-AC1,IV97-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the portal commit hashes in order, each criterion's last line, every package the lock refresh moved with before and after and the prune count, both build hashes, the playwright-core decision with its evidence, the calendar decision with its test, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; package lock and test tooling; the production build is proven byte-equal and the candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the base state is measured by the check's own dry run, every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
