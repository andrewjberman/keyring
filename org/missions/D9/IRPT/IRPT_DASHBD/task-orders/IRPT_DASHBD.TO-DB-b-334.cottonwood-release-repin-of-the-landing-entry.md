# TO IRPT_DASHBD.TO-DB-b-334 -- the RE-PIN of the Cottonwood landing function entry for the ONE code release: the late-posting reader (DB-b-333) and ~F2's late-window transaction stage (DB-f-2706) are on the trunk, so the entry's stale staged members get new pins and sha256 and the build-only package equals its sources (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-334</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~260</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>RELEASE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** RELEASE, round 150 | **Ordered by:** the CTO's ruling that the reader fix and ~F2's transaction stage ship as ONE code release (msgs 10591, 10598), and ~F2's request (msg 10610) that the release cell own the entry re-pin | **Decomp cell:** `DB-b-334` (decomposition section 195).

**Risk class WORLD (the gate's floor for a path under `infra/`):** one JSON edit in a workspace worktree; no Terraform command, no AWS write, no build for upload, no upload, no push. The release itself (build, signed pair, apply by the CloudOps lane) is a later order.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-260` (branch `wk-IRPT_DASHBD-260`, a FULL checkout cut from the current `box/dell2`). Work only there; never push; never commit the workspace `portal` gitlink. Counts, hashes and words only in anything you write; ASCII only. The repo's line endings are LF.

**Why.** `infra/aws/lambda/ci/function-map/irpt-cot-account-return-daily-lambda.json` pins every staged member to a full commit and the sha256 of the file at that commit. Since the pins were written, other cells changed pinned members: the Cottonwood adapter (the late-posting reader, DB-b-333) and shared files (`lib/opal_naming.py`, registry files). A build from a stale entry is refused by the entry's own check, and a pin that does not equal its file is a lie in the record.

**The cell (`DB-b-334`).**
1. **Read first, whole:** the entry file above; `lib/opal_lambda_map.py`; `infra/aws/lambda/ci/build-and-upload.sh` (the `BUILD_ONLY` mode; read only); the issuer's checker `C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p200_cot_release_repin.py` (your three criteria: it states the clauses exactly).
2. **The edit (ONE file: the entry file).** For each `staged_from` member whose file at HEAD no longer has the member's `sha256` (find them by hashing the files at HEAD), set `pin` to the full 40-hex commit that last changed that file (`git log -1 --format=%H -- <path>`; an ancestor of HEAD) and `sha256` to the hex sha256 of the file at HEAD (equal to `git show <pin>:<path>`). `repo_path` and `packaged_as` do not change. Every member that is not stale stays byte for byte; every other key of the entry (`files`, the deployed fields `artifact_sha256`, `last_deployed_commit`, `last_deployed_at`, `recorded_by`, the notes) stays byte for byte; no member is added or removed; no other file of the `function-map` folder changes. Write the JSON with LF endings and the file's own indentation. Re-run your hashing just before the commit: another seat may have edited a pinned file meanwhile; if so re-pin that member too and say so in a row.
3. **Commit** the file with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~260 <0.9.0_WK_IRPT_DASHBD~260@opal.agent>" -F <msgfile> -- <paths>` (the message file written with a non-shell writer; READ the whole gate output), BEFORE running criteria DBR200-2-AC1 and DBR200-3-AC1 (they read committed source).
4. **Run the three invocations below from your worktree root** and report each one's last line. Criterion DBR200-2-AC1 runs the function's tests and takes a few minutes; DBR200-3-AC1 builds the package under a temporary directory.

<criterion id="DBR200-1-AC1" cell_refs="DB-b-334"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p200_cot_release_repin.py" C:/dev/wk-irpt-dashbd-260 DBR200-1-AC1</invocation><expect>DBR200-1-AC1 PASS</expect></criterion>
`DBR200-1-AC1` -- the entry differs from the base only in its stale members' `pin` and `sha256` (each new pin an ancestor whose file bytes equal the sha256 and the file at HEAD); a member that was not stale is byte-identical; every member equals its pinned bytes; the worker's commits change only the entry file, the folder, the investigation file and task-order files. Base: FAIL.
<criterion id="DBR200-2-AC1" cell_refs="DB-b-334"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p200_cot_release_repin.py" C:/dev/wk-irpt-dashbd-260 DBR200-2-AC1</invocation><expect>DBR200-2-AC1 PASS</expect></criterion>
`DBR200-2-AC1` -- ~F2's criterion `DBF139-6-AC3` passes on your tree (the function's tests are green and the bundle criteria `DBF138-6-AC1` to `AC3` pass: the entry pins the files it packages and the handler imports the producer in the bundle layout). Base: FAIL (`DBF138-6-AC2`).
<criterion id="DBR200-3-AC1" cell_refs="DB-b-334"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p200_cot_release_repin.py" C:/dev/wk-irpt-dashbd-260 DBR200-3-AC1</invocation><expect>DBR200-3-AC1 PASS</expect></criterion>
`DBR200-3-AC1` -- the build-only package of the entry holds exactly the entry's `files` with every member's bytes equal to its source, and its third-party imports are pyarrow and pandas plus the runtime's (the layer holds them). Base: FAIL.

<expected_criteria>DBR200-1-AC1,DBR200-2-AC1,DBR200-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files and the layer (GET and LIST only, which the checker makes). Writes: the one entry file in your worktree. The `BUILD_ONLY` run writes a zip under a temporary directory only. No Terraform command, no AWS write, no upload, no push, no invoke.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W260-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. ASCII only; every `.py` you touch (none expected) passes ruff.

<paths>
infra/aws/lambda/ci/function-map/irpt-cot-account-return-daily-lambda.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~260/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-334.cottonwood-release-repin-of-the-landing-entry.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 195 (round 150, workstream RELEASE), cell `DB-b-334`.
<owned_cells>DB-b-334</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBR200-1-AC1, DBR200-2-AC1, DBR200-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~260/IRPT_DASHBD.TO-DB-b-334.cottonwood-release-repin-of-the-landing-entry.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBR200-1-AC1,DBR200-2-AC1,DBR200-3-AC1` BEFORE the status flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the re-pinned paths; the count of unchanged members; your last workspace commit (git read); what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one function-map entry's pins in a branch; nothing is built for upload, uploaded, planned or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is written.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the three criteria FAIL at base, the entry clause is the proven p172 check_repin_entry (10 single-fault arms) and the grant and lazy-import clauses have their own red arms in the selftest.
lane: the <paths> block IS the grant.
</preflight>
