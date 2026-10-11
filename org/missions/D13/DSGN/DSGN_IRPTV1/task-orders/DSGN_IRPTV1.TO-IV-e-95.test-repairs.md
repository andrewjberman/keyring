# TO DSGN_IRPTV1.TO-IV-e-95 -- the test repairs: the excused set pinned by name, the smoke map at 22 with two named excuses, two stale goldens, the newline pins -- test and fixture files only

<to_id>DSGN_IRPTV1.TO-IV-e-95</to_id>
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

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-17 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_17_20261011.md` @e4345abd6e, section 4 items 1 and 3, and the pin and golden rows of section 3 | **Decomp cell:** `IV-e-95` (decomposition v17) | **outcome_ref:** FWD-1 | **depends_on:** IV-e-94 (drained).

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

**The cell (`IV-e-95`).** Test and fixture files only: NO product file changes in this order. Four parts, each its own portal commit; record
each in `TEST_REPAIRS.json`.

1. **The excused set, by name** (row DSGN_IRPTV1-D2-W49-S9). `fe-s-14/envelope.test.ts` and `fe-s-57/carry.test.ts` now count DECLARED routes
   "with and without a response schema" and print the ones that have none. As written, a route that LOSES its schema silently joins the excused
   group and the test still passes. Make each test assert the excused set BY NAME: an explicit list of the routes allowed to have no response
   schema today, compared exactly against what the contract's `routes.json` shows. Then show it can fail: one temporary mutant per test (the
   list with one name removed, or a route added to the no-schema group in a test-local copy), run, fails, reverted, never committed.
   `excused_sets`: [{test_file, excused_by_name, mutant {what, failed}}].
2. **The smoke map at 22** (row D2-W49-S8; the CTO ruled 22: one entry per scoped route is the map's stated purpose).
   `fixtures/smoke/default.json` goes from 12 keys to one per scoped route. Bodies come from the producer's own fixtures in the workspace
   (`docs/contracts`, read, never edited): never invent a body. Exactly TWO routes have no producer fixture (`custody-report-read`,
   `custody-report-persist`): they are EXCUSED BY NAME inside the fe-s-1 test, with the reason "no producer fixture until IRPT_BCKEND publishes
   one", and the test fails if a third route is missing or if an excused route gains an entry without the excuse being removed. The portal
   test pinning 12 (`fe-s-14/published-map.test.ts`) follows to the new statement, as strict as before. The PRODUCER's pin
   (`infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py`, `CONSUMER_SMOKE_ENTRIES`) is another project's file and is NOT
   in your grant: record it as `producer_pin` {file, outcome: "PLACED", owner: "2.0.0_SA_COO~P2"} and do not edit it.
   `smoke_map`: {keys, excused: [{route, reason}], pins_followed: [{file, before, after}], producer_pin}.
3. **Two stale goldens** (the table `deliverables/0.9.0_WK_DSGN_IRPTV1~50/FAILING_ID_TABLE.json`, rows for IVE115 and IVE69, both
   RETIREMENT_ASKED with their reasons). Each test's expected value was left behind by a ruled product change:
   - IVE115: the expected-rank literal still has nine entries after Multi-Asset was removed as a class (the table cites Andrew's word of
     2026-10-07 and portal a6868784). Bring the literal in line with the eight-entry order the same test already states.
   - IVE69: the OBJECT_NOT_COVERED wording was re-worded by a cited CTO ruling (portal 74d27b1b); iv-e-39 was re-goldened and iv-e-69 was
     missed. Bring iv-e-69's expected text in line with the product's current words, which you print from the product source.
   For each: print the product's current value from its source file and line, and change ONLY the stale expected value. If the product's
   current value does NOT match what the cited ruling says, STOP on that id with a row. `regold`: [{id, outcome, ruling, before, after, row}].
4. **Newline-anchored pins** (row D2-W52-S3). A source-text pin whose regex anchors on a bare LF fails on a CRLF checkout. Search the scope's
   test files for pins that read a source file's text and anchor on a newline (state the search and its file count), and widen each anchor to
   accept either line ending, exactly as iv-e-116 was. `newline_pins`: {files_searched, found, fixed, list}.

Then one whole-scope run after; `suite_after` {failed, fixed_ids, new_failing_ids}; `portal_commit` (your last); `product_files_changed` must be [].

<criterion id="IV95-AC1" cell_refs="IV-e-95"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r17/p17_round17.py" . IV95-AC1</invocation><expect>IV95-AC1 PASS</expect></criterion>
`IV95-AC1` -- the two excused sets are pinned by name and each can fail; the two stale goldens are re-goldened to their rulings or stopped with a row. Base: FAIL.

<criterion id="IV95-AC2" cell_refs="IV-e-95"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r17/p17_round17.py" . IV95-AC2</invocation><expect>IV95-AC2 PASS</expect></criterion>
`IV95-AC2` -- the smoke map holds 22 entries with exactly two routes excused by name, the portal pin follows, and the producer's pin is placed with its owner. Base: FAIL.

<criterion id="IV95-AC3" cell_refs="IV-e-95"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r17/p17_round17.py" . IV95-AC3</invocation><expect>IV95-AC3 PASS</expect></criterion>
`IV95-AC3` -- newline-anchored pins are searched for and fixed, and no new id fails. Base: FAIL.

<expected_criteria>IV95-AC1,IV95-AC2,IV95-AC3</expected_criteria>

## AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~10:4xZ): part 2's premise was wrong -- the excused set is MEASURED, not the two routes this order named (row DSGN_IRPTV1-D2-W53-S1)

The order said `custody-report-read` and `custody-report-persist` have no producer fixture. They do: IRPT_BCKEND IB-pr-412 published response
schemas and valid/invalid fixtures for both (@5020b450a7, 2026-10-09; the stat read by the issuer). The worker measured ONE declared route with
no producer fixture, `analysis-request-original`, and correctly built nothing on a false reason. The defect is the issuer's: it carried an
earlier worker's statement and the analysis's count without reading the fixtures.

**Part 2 now reads:** the smoke map holds one entry per scoped (DECLARED) route THAT HAS A PRODUCER FIXTURE, each body sourced from that
fixture (`sourced`: [{route, source}], one per key). A route is excused only when you MEASURED that no producer fixture exists for it
(`excused`: [{route, reason, searched}], where `searched` states where you looked); the fe-s-1 test names the excused routes, fails if any
other route is missing, and fails if an excused route gains a fixture entry while still excused. By your measurement that is 21 entries and
one excuse; build what you measure. If more than two routes turn out to have no producer fixture, STOP with a row. `routes_declared` is the
contract's count (22). `fe-s-14/published-map.test.ts` follows to the same statement, as strict as before. The producer's pin stays PLACED.

Parts 1, 3 and 4 stand as committed (IV95-AC1 and IV95-AC3 PASS on the worker's run). Criterion IV95-AC2's check is amended to this statement;
its id and invocation are unchanged. The CTO's ruling (one entry per scoped route, excuses by name) is unchanged in kind; the count it named
is corrected by measurement and is reported to it with the candidate.

**Gate limb that graded this modification:** none. A modified order without `<placeholders>` is not graded.

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no package change, no dev server.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W53-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-95.test-repairs.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v17 (round 17), cell `IV-e-95`.
<owned_cells>IV-e-95</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV95-AC1,IV95-AC2,IV95-AC3. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/DSGN_IRPTV1.TO-IV-e-95.test-repairs.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV95-AC1,IV95-AC2,IV95-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the portal commit hashes in order with one line each, each criterion's last line, the excused names per test and each mutant, the smoke map's 22 keys by source and the two excuses, each golden's before and after with the product line it was read from, the newline search and what it found, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; test and fixture files only, and the candidate is read before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the base state is measured by the check's own dry run, every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
