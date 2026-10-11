# TO DSGN_IRPTV1.TO-IV-e-99 -- the portal's history reader admits the contract's new members (and still the two-key answer), so irpt-status release 5 can return -- candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-99</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~55</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 4806 (2026-10-11 ~11:18Z): irpt-status release 5 is rolled back because the portal's history reader refuses its answer; "The release returns only with the portal's reader admitting the new members first, on PROD, in that order." Record: `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/FIVE_FIXTURES_VS_CONTRACT_20261011.md` (row DSGN_IRPTV1-D2-W53-S4) | **Decomp cell:** `IV-e-99` (decomposition v19) | **outcome_ref:** FWD-1 (the page reads the service's answer) | **depends_on:** none (its own portal worktree; it touches no file IV-e-96 touches).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-55` (branch `wk-dsgn-irptv1-r19-55`); run everything from its root unless a step says the
portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~55/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-55/portal` is a PORTAL worktree (its own git repo, branch `wk-dsgn-irptv1-r19-55`) at the portal DEV tip
your spawn prompt names. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status
commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` there is a read-only junction to another worktree's install: do NOT run `bun install`, do not add a package, do not write
into `node_modules`. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only
with `git checkout -- <file>` on a file that has no uncommitted work of yours.

**What is wrong.** `readOwnedHistory` in `portal/src/pages/InvestorReporting/contracts/owned-requests.ts` (near line 79) admits EXACTLY the
top-level keys `items` and `next_cursor`. The ratified contract's history answer
(`docs/contracts/investor-reporting/v1/OwnedAnalysisRequestHistory.schema.json`, read in the workspace, never edited) also carries
`unreadable_rows`, and each item carries `client_id` and `client_claim`. When the service served that answer, every history read on the page
threw "Invalid owned request history". The service is being rolled back to the two-key answer; it returns once the page can read both.

**The cell (`IV-e-99`).** Minimal, and strict:

1. **Read the contract first** and print, with file and line, the declaration of each member involved: `unreadable_rows`, the item's
   `client_id` and `client_claim` (their types, whether required, whether null is admitted, the enum of `client_claim`), and `items` /
   `next_cursor` as they stand (`contract_lines`: [{member, file, line, text}]).
2. **The reader admits BOTH answers the service can serve:** the two-key answer (live after the rollback) and the contract's answer with the
   new members. It admits them exactly as the contract types them, and it still REFUSES: any other top-level key, any other item key, an
   `unreadable_rows` of the wrong type, a `client_claim` outside the contract's enum. If the contract makes a member REQUIRED, the two-key
   answer would be a contract violation: in that case STOP with a row before writing any code, because which answer the reader must take is
   then the CTO's ruling, not yours.
3. **Carry, do not invent.** The wire type and the view carry the new members as the contract types them (absent stays absent; null stays
   null; never coalesced). Whether the page SHOWS them (a client column, an unreadable-rows note) is a separate page half and is NOT this
   cell: change no rendering unless the type change forces a compile-level touch, and list anything a user could see differently under
   `rendered_changes` (expected: an empty list). If the wire type lives in the generated folder (`contracts/wire/`), do NOT hand-edit a
   generated file: stop on that point with a row and carry the members in the hand-written reader's own type instead; the folder's
   regeneration is another cell (IV-e-98).
4. **A test** under the scope's `__tests__/dsgn-irptv1/`: the reader accepts (a) a two-key answer, (b) the contract's answer, (c) the
   producer's own fixture `infra/aws/lambda/investor-reporting/_contracts/fixtures/OwnedAnalysisRequestHistory.valid.json` (its `instance`,
   wrapped in the response envelope and read through `parseIrEnvelope('analysis-request-history', ...)`, wrapped exactly as the existing
   smoke entries wrap a payload); and refuses each of the four malformed answers of item 2. One temporary mutant (the old exact-two-keys check
   restored) makes it fail. `accepts`, `refuses`, `test` {id, passes, mutant {what, failed}}.
5. `bun run typecheck` reads 0 errors. One whole-scope run before any edit (your base; expect 7 failing) and one after: `suite_after`
   {failed, fixed_ids, new_failing_ids}. Existing tests that pinned the exact-two-keys behaviour are brought to the new rule and listed with
   before and after. `carried`, `product_files_changed`, `portal_commit`.

<criterion id="IV99-AC1" cell_refs="IV-e-99"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r19/p19_round19.py" . IV99-AC1</invocation><expect>IV99-AC1 PASS</expect></criterion>
`IV99-AC1` -- the reader takes the two-key answer, the contract's answer and the producer's fixture, refuses four malformed ones, a test holds it and a mutant breaks it. Base: FAIL.

<criterion id="IV99-AC2" cell_refs="IV-e-99"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r19/p19_round19.py" . IV99-AC2</invocation><expect>IV99-AC2 PASS</expect></criterion>
`IV99-AC2` -- the new members are carried, what a user could see differently is listed, typecheck reads 0 errors and no new id fails. Base: FAIL.

<expected_criteria>IV99-AC1,IV99-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request to any service, no vendor call, no secret read,
  no `bun install`, no package change, no dev server.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W55-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~55/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-99.history-reader-admits-new-members.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v19 (round 19), cell `IV-e-99`.
<owned_cells>IV-e-99</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV99-AC1,IV99-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~55/DSGN_IRPTV1.TO-IV-e-99.history-reader-admits-new-members.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV99-AC1,IV99-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the portal commit hashes in order with one line each, each criterion's last line, the contract lines for each member, the reader's rule before and after, what it accepts and refuses with the test and its mutant, what is carried and whether anything a user sees changes, every existing test updated with before and after, typecheck, `product_files_changed`, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one reader function and its type on a client-facing page; the candidate is read by the CTO before DEV, and PROD waits on Andrew's word.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; both criteria FAIL at base (no record); the issuer's own probe at portal 11f25102 measured the refusal this cell removes.
lane: the <paths> block IS the grant.
</preflight>
