# TO IRPT_DASHBD.TO-DB-b-92 -- E3: verify-persisted also checks the persisted object's sha256 against the index entry, not only the index (W64-S1)

<to_id>IRPT_DASHBD.TO-DB-b-92</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~67</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>44</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 11 (msg 3288; CVO ADJUDICATION_v25 @5f365678bf), enrichment item E3 | **Decomp cell:** `DB-b-92` (decomposition section 46) | **outcome_ref:** FWD-12 | **depends_on:** DB-b-89 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-67`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~67/`.

**The cell (`DB-b-92`).** DB-b-89 re-cut the runner `C:/dev/wk-irpt-dashbd-67/data/assets/scripts/gold/irpt_custody/e2a_real_statement.py` onto
IB-pr-405 `persist_inputs`. Its row W64-S1 says `verify-persisted` now checks only that the route's `report_index` matches the refs. The CTO ruled
(ADDENDUM 11, item 3) that it also verifies the persisted object's sha256 against the index entry.

1. Make `verify-persisted` compare the persisted object's sha256, as IB-pr-405's response or its index entry exposes it, to the sha256 the
   refs recorded at `run`. A mismatch prints `PERSISTED MISMATCH` and exits non-zero.
   - If the route exposes no sha256 for the persisted object, file a row naming the missing field, and keep the index check.
   - Read IB-pr-405's contract at @2f6fe31ad8.
2. Add tests: a match passes, and a mismatch is refused. Use the recorded fixture
   `data/assets/scripts/gold/irpt_custody/tests/fixtures/persist_inputs_route_fixture.json`, extended only with fields the contract defines.
3. Record `RUNNER_SHA.json` {tests: {passed, failed, new_test}}.

No live call.

<criterion id="DB44-3-AC1" cell_refs="DB-b-92"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r44/p44_round44.py" . DB44-3-AC1</invocation><expect>DB44-3-AC1 PASS</expect></criterion>
`DB44-3-AC1` -- verify-persisted checks the persisted object's sha256, with a match test and a mismatch test. Base: FAIL.

<expected_criteria>DB44-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the runner and its tests folder. No live call.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~67/
data/assets/scripts/gold/irpt_custody/e2a_real_statement.py
data/assets/scripts/gold/irpt_custody/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-92.runner-verify-sha256.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 46 (round 44), cell `DB-b-92`.
<owned_cells>DB-b-92</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB44-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~67/IRPT_DASHBD.TO-DB-b-92.runner-verify-sha256.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB44-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the sha256 source in the route, the tests, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an offline runner change and tests; nothing runs live.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB44-3-AC1 FAIL at base (no record). Row W64-S1; CTO ADDENDUM 11 item 3.
lane: the <paths> block IS the grant.
</preflight>
