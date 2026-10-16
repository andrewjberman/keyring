# TO IRPT_DASHBD.TO-DB-b-304 -- the RE-PIN of three function entries after the drain of cells DB-b-302, DB-b-303 and DB-b-305 (round 149): the stale staged members of the Cottonwood landing, the 49 Financial publish and the Cottonwood publish entries get new pins and sha256; nothing else in the map moves

<to_id>IRPT_DASHBD.TO-DB-b-304</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~244</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>REPIN2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** REPIN2, round 149 | **Ordered by:** the issuer's own decomposition (section 166), on the drain of `DB-b-303` (merge `d011411480`: the Cottonwood adapter), `DB-b-302` (merge `aec0df87fc`: the 49 Financial publish handler and the shared publisher) and `DB-b-305` (merge `b4f813d26e`: the handler's pass), which changed pinned members of three function entries | **Decomp cell:** `DB-b-304` (decomposition section 166).

**Risk class WORLD** is the floor of the path below (`infra/` path): one JSON edit, no Terraform command, no AWS write, no upload, no push. The re-pin makes the next bundle build of each function equal what its pins say; the builds, the uploads and the applies are the applier's, under later signed pairs.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-244` (branch `wk-IRPT_DASHBD-244`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~244/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value. Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~244/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Each function entry in `infra/aws/lambda/ci/lambda-source-map.json` pins every staged member to a full commit and its sha256. The three drains changed pinned members of three entries: the adapter of `irpt-cot-account-return-daily-lambda` (the first-row rule), the handler and the shared `publisher.py` of `irpt-49f-reporting-publish-lambda` (the hop-2 reader, the validator, the pass), and the shared `publisher.py` of `irpt-cot-reporting-publish-lambda`; other seats may also have changed shared registry files. A build from a stale entry is refused by the entry's own check, and a pin that does not equal its file is a lie in the record. The deployed fields of the 49 Financial publish entry were last moved by the applier's upload (`DB-b-298`); they stay as they are.

**The cell (`DB-b-304`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p172_repin_after_reader.py` (your three criteria) and the proven clause it applies to each entry, `check_repin` in `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p158_repin.py` (the exact spec of what may differ from the base); `infra/aws/lambda/ci/lambda-source-map.json`, the three entries `irpt-cot-reporting-publish-lambda`, `irpt-49f-reporting-gold-lambda` and `irpt-cot-account-return-daily-lambda` (their `staged_from`); `infra/aws/lambda/ci/build-and-upload.sh` (the `BUILD_ONLY` mode; read only); your own sibling order `IRPT_DASHBD.TO-DB-b-297...` (the same edit for three entries, done once already; its facts record is the model).
2. **The edit (ONE file, `infra/aws/lambda/ci/lambda-source-map.json`, three entries only).** For each `staged_from` member of each of the three entries whose file at HEAD no longer has the entry's `sha256` (find them by hashing the files; the stale ones are expected to be the adapter of the landing entry, the handler and publisher of the 49 Financial publish entry, and the publisher of the Cottonwood publish entry, plus any shared member another seat changed), set `pin` to the full 40-hex commit that last changed that file (`git log -1 --format=%H -- <path>`; an ancestor of HEAD) and `sha256` to the hex sha256 of the file at HEAD (equal to `git show <pin>:<path>`). `packaged_as` and `repo_path` do not change. Every other member (byte for byte), every other key of each entry (INCLUDING `artifact_sha256`, `deployed_code_sha256`, `last_deployed_commit`, `last_deployed_at`, `recorded_by` and the notes), every other entry and every top-level key stay byte for byte; no member is added or removed. Commit the file BEFORE running the build (it reads committed source). Re-run your hashing just before your commit: another seat may have edited a pinned file meanwhile; if so re-pin that member too and say so in a row. Write the JSON with LF line endings and the file's own indentation.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p172_repin_after_reader.py" . DB172-1-AC1`, then AC2 (this runs the build-only package of each of the three entries and the import check against the layer; it takes a few minutes), then AC3.
4. **Record** `RD_REPIN_THREE_FACTS_R149B.json` in your folder with EXACTLY these fields: `entries` (["irpt-cot-account-return-daily-lambda", "irpt-49f-reporting-publish-lambda", "irpt-cot-reporting-publish-lambda"]); `repinned` (an object from each entry name to the list of repo paths you re-pinned in it, possibly empty); `unchanged_members` (an object from each entry name to the count of its members you left byte-identical); `build_only_sha256_b64` (an object from each entry name to the base64 sha256 that the `BUILD_ONLY` run prints for it at your committed tree); `words` (one paragraph, 80 to 1800 characters: what moved and why, that no deployed field moved, and what is NOT proven: nothing is built for upload, uploaded or deployed, and a pinned file edited by another seat after your commit makes an entry stale again).

<criterion id="DB172-1-AC1" cell_refs="DB-b-304"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p172_repin_after_reader.py" . DB172-1-AC1</invocation><expect>DB172-1-AC1 PASS</expect></criterion>
`DB172-1-AC1` -- each of the three entries differs from the base only in its stale members' `pin` and `sha256` (each new pin an ancestor commit whose file bytes equal the sha256 and the file at HEAD); a member that was not stale is byte-identical; no other key (the deployed fields included), no other entry and no top-level key moved; at the end every staged member of the three entries equals its pinned bytes. Base: FAIL.
<criterion id="DB172-1-AC2" cell_refs="DB-b-304"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p172_repin_after_reader.py" . DB172-1-AC2</invocation><expect>DB172-1-AC2 PASS</expect></criterion>
`DB172-1-AC2` -- the `BUILD_ONLY` package of each of the three entries holds exactly the entry's `files` with every member's bytes equal to its source, and its third-party imports are pyarrow plus the runtime's (the layer holds it). Base: FAIL.
<criterion id="DB172-1-AC3" cell_refs="DB-b-304"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p172_repin_after_reader.py" . DB172-1-AC3</invocation><expect>DB172-1-AC3 PASS</expect></criterion>
`DB172-1-AC3` -- the facts record equals the checker's recount (the re-pinned paths per entry, the unchanged counts, the three build-only hashes) and the worker's commits change only the source map, the folder, the investigation file and task-order files. Base: FAIL.

<expected_criteria>DB172-1-AC1,DB172-1-AC2,DB172-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files, the layer (`aws lambda list-layer-versions` and `get-layer-version`, GET and LIST only, which the checker also makes). Writes: the one source-map file and your private folder. The `BUILD_ONLY` run writes a zip under a temporary directory only. No Terraform command, no AWS write, no upload, no push, no invoke.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W244-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~244/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-304.repin-three-entries-after-the-reader-and-the-first-row.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 166 (round 149, workstream REPIN2), cell `DB-b-304`.
<owned_cells>DB-b-304</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB172-1-AC1, DB172-1-AC2, DB172-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~244/IRPT_DASHBD.TO-DB-b-304.repin-three-entries-after-the-reader-and-the-first-row.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB172-1-AC1,DB172-1-AC2,DB172-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the re-pinned paths per entry; the unchanged-member counts; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: three source-map entries' pins in a branch; nothing is built for upload, uploaded, planned or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the re-pin clause is the proven p158 check_repin (validated in round 149 against a real re-pin computed from git and 10 single-fault arms) applied to each entry; the package clause reuses the proven checkers of rounds 147 to 149.
lane: the <paths> block IS the grant.
</preflight>
