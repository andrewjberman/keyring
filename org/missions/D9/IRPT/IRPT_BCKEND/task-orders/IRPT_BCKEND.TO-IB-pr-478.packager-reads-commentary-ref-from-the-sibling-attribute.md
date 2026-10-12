# TO IRPT_BCKEND.TO-IB-pr-478 -- BUILD ONLY: the packager reads `commentary_ref` from the request item's sibling attribute (the record stays immutable), proven by a round trip from the writer to the packager

<to_id>IRPT_BCKEND.TO-IB-pr-478</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~333</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>166</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6503 (CTO ROUND-166 ANALYSIS section 2 row D2-W309-S2, section 3 item 4); read `deliverables/0.9.0_WK_IRPT_BCKEND~330/IB165-5_TWO_READS.md` | **Decomp cell:** `IB-pr-478` (decomposition section 158) | **outcome_ref:** FWD-8

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-333/` (bash `/c/dev/wk-irpt-bckend-333`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY. No AWS call, no Lambda invoked, no route called, nobody signs in. Nothing is deployed or uploaded. Every value in a test is SYNTHETIC; no real ticket, request or client appears in any file.

**Why (the read, from the previous round).** `commentary_ref` is WRITTEN by `infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py` (about lines 205-232) as a SIBLING attribute of the request item, by a conditional update; the immutable record attribute is never rewritten.
It is READ by `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py` (`handle_commentary_ready`, about line 153: `record.get('commentary_ref')`) from `ports["acceptance"].get(tenant, request_id)`. In the live runtime that port is a plain `DynamoAcceptance`
(`reports/resident_installed.py` about lines 334, 393-394, 433), whose `get` (`ycharts/generate/acceptance.py` about lines 68-71) returns only `json.loads(item["record"]["S"])`. So by the code a live packager raises `COMMENTARY_REF_ABSENT` on a request whose `commentary_ref` sits beside the record. No test crosses the writer and the reader: the packager's tests use a fake whose record holds
`commentary_ref` INSIDE it (`ycharts/research/tests/test_opal_packager.py` about lines 58-64).

**The CTO's ruling.** The reader moves; the record stays immutable. The packager reads `commentary_ref` from the item's sibling attribute: the accessor returns it BESIDE the record. Never write it into the record. The proof is a round-trip test that writes through the writer and reads through the packager, which no test does today.

**Build.**
1. Give the acceptance accessor a way to return the item's `commentary_ref` sibling attribute beside the unchanged record (choose the shape: a new method, or a second return value kept backward-compatible; every existing caller of `get` keeps working unchanged). The `record` that `get` returns is byte-for-byte what it is today.
2. `handle_commentary_ready` reads `commentary_ref` through it (and keeps its present refusals: `COMMENTARY_REF_ABSENT` when the attribute is absent or blank, `COMMENTARY_REF_MALFORMED` when it does not parse).
3. Wire the port in `reports/resident_installed.py` only as far as the new accessor needs. Do NOT change `commentary_draft_store.py` (the writer stays as it is).

**Tests (the build's own):** `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_commentary_ref_round_trip.py`, at least THREE tests, using an in-memory fake DynamoDB client that honours `get_item` and the writer's conditional `update_item` (build it in the test; extend an existing fake if one fits): (1) ROUND TRIP: write `commentary_ref` through the real `commentary_draft_store` writer, then `handle_commentary_ready` through the REAL `DynamoAcceptance` (not a fake port) reads it and attaches (the happy path reaches its attach port); (2) the record's bytes are IDENTICAL before and after the write (the immutability proof; name this test in the record as `record_immutable_test`); (3) an item with no `commentary_ref` still raises `COMMENTARY_REF_ABSENT`, and a malformed one `COMMENTARY_REF_MALFORMED`.
The research folder reads `302 passed` at base; the reports folder `202 passed`; after, no failure and at least 305 passed in research.

**Where it is deployed.** The CTO does not know whether the packager is deployed, or where. Read `infra/aws/lambda/ci/lambda-source-map.json` and `reports/build_resident_package.py` (and the resident package lists) and state in the record `deployed_where: {function_family, cite}`: which Lambda or resident package carries `opal_packager.py`, `acceptance.py` and `resident_installed.py`, or that none does. Nothing is built or deployed here.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~333/IB166-3_commentary_ref_record.json`: `{base_commit, files_changed, cites:[path:line of the writer, the accessor and the packager read after your change], reader_rule_in_words, record_immutable_test, deployed_where, hash_pins:[every place in the repo that pins a hash of a file you changed, with what you did about it], suites:{research_before, research_after, reports_before, reports_after}, request_sent:false, deployed:false}`.

<criterion id="IB166-3-AC1" cell_refs="IB-pr-478"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-3-AC1</invocation><expect>IB166-3-AC1 PASS</expect></criterion>
<criterion id="IB166-3-AC2" cell_refs="IB-pr-478"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-3-AC2</invocation><expect>IB166-3-AC2 PASS</expect></criterion>
<criterion id="IB166-3-AC3" cell_refs="IB-pr-478"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-3-AC3</invocation><expect>IB166-3-AC3 PASS</expect></criterion>

<expected_criteria>IB166-3-AC1, IB166-3-AC2, IB166-3-AC3</expected_criteria>

What the checks grade: AC1 your round-trip test file exists and at least 3 tests pass; AC2 the whole research test folder reads no failure and at least 305 passed; AC3 the record's form (resolving cites, a named immutability test, a `deployed_where` with a resolving cite), `request_sent` and `deployed` false, and that nothing outside
`ycharts/research/`, `ycharts/generate/`, `reports/`, your deliverables, rows and order changed. The reports folder (202 passed at base) is re-read by the issuer at the drain.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. The writer `commentary_draft_store.py` and the record's shape are NOT yours.
- **Refusal clause:** if the sibling attribute cannot be returned beside the record without changing the record, or the writer's conditional update cannot be faked faithfully, STOP, file a row and report. Never weaken a check or a test; do not edit `p166_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W333-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~333" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~333@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~333 <0.9.0_WK_IRPT_BCKEND~333@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~333/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-478.packager-reads-commentary-ref-from-the-sibling-attribute.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 158 (round 166, workstream ~P), cell `IB-pr-478`.
<owned_cells>IB-pr-478</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB166-3-AC1, IB166-3-AC2, IB166-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~333/IRPT_BCKEND.TO-IB-pr-478.packager-reads-commentary-ref-from-the-sibling-attribute.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the accessor's shape in a sentence; the round trip's three tests and the immutability test; where the packager is deployed (or that nothing carries it); the research and reports suites' last lines before and after; the hash pins found and what you did; each criterion's last line;
the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell changes the packager's reader and its accessor in the repo; nothing is deployed or invoked; a release of any carrying function goes under that function family's own pair (CTO ROUND-166 ANALYSIS row D2-W309-S2).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p166_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~19:3xZ: IB166-3 AC1 FAIL (the round-trip test is absent), AC2 FAIL (302 passed, need >= 305), AC3 FAIL (no record); commit-gate clean. Measured by the issuer at base: pytest ycharts/research/tests reads 302 passed; pytest reports reads 202 passed. The mismatch is read from code by worker ~330 and was not run.
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (an infra path); nothing is deployed.
</preflight>
