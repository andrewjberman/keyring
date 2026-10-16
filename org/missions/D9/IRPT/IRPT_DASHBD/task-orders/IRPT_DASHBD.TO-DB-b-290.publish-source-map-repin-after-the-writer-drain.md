# TO IRPT_DASHBD.TO-DB-b-290 -- the RE-PIN of the Cottonwood publish function's source-map entry after the writer drain (round 149): the four staged members that changed since the entry was pinned get new pins and sha256; nothing else in the map moves

<to_id>IRPT_DASHBD.TO-DB-b-290</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~234</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>PUBWRITE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** PUBWRITE, round 149 | **Ordered by:** the issuer's own decomposition (section 151), on the drain `ff6c0633a7` that changed the publisher, the series contract and (by other seats) two registry files | **Decomp cell:** `DB-b-290` (decomposition section 151).

**Risk class WORLD** is the floor of the path below (`infra/` path): one JSON edit, no Terraform command, no AWS write, no upload, no push. The re-pin is what makes the next bundle build equal what its pins say; the build and the upload are the applier's, under a later signed pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-234` (branch `wk-IRPT_DASHBD-234`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~234/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~234/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The source-map entry `irpt-cot-reporting-publish-lambda` pins each staged member to a full commit and its sha256 (DB-b-281). Four members changed since: `infra/aws/lambda/investor-reporting/reporting-publish/publisher.py` and `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (the writer drain `ff6c0633a7`), and `infra/logic/registry/systems.json` and `.../scopes.json` (other seats' edits). A build from the stale entry would be refused by the entry's own check, and a pin that does not equal its file is a lie in the record.

**The cell (`DB-b-290`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p158_repin.py` (your three criteria; `check_repin` is the exact spec); `infra/aws/lambda/ci/lambda-source-map.json`, the one entry `irpt-cot-reporting-publish-lambda` (its `staged_from`); `infra/aws/lambda/ci/build-and-upload.sh` (the `BUILD_ONLY` mode; read only).
2. **The edit (ONE file, `infra/aws/lambda/ci/lambda-source-map.json`).** For each `staged_from` member whose file at HEAD no longer has the entry's `sha256` (there are four; find them by hashing the files), set `pin` to the full 40-hex commit that last changed that file (`git log -1 --format=%H -- <path>`; an ancestor of HEAD) and `sha256` to the hex sha256 of the file at HEAD (equal to `git show <pin>:<path>`). Every other member, every other key of the entry (INCLUDING the deployed `artifact_sha256`, `last_deployed_commit`, `last_deployed_at` and `recorded_by`), every other entry and every top-level key stay byte for byte. Commit the file BEFORE running the build (it reads committed source). Re-run your hashing just before your commit: another seat may have edited a pinned file meanwhile; if so re-pin that member too and say so in a row.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p158_repin.py" . DB158-1-AC1`, then AC2 (this runs the build-only package, the import check against the layer and the writer's behaviour check on the UNPACKED handler; it takes a few minutes), then AC3.
4. **Record** `RD_PUBLISH_REPIN_FACTS_R149.json` in your folder with EXACTLY these fields: `entry` ("irpt-cot-reporting-publish-lambda"); `repinned` (the repo paths you re-pinned, as a list); `unchanged_members` (the count of members you left byte-identical); `build_only_sha256_b64` (the base64 sha256 the `BUILD_ONLY` run prints at your committed tree); `words` (one paragraph, 80 to 1800 characters: what moved and why, that no deployed field moved, and what is NOT proven: nothing is uploaded or deployed, and a pinned file edited by another seat after your commit makes the entry stale again).

<criterion id="DB158-1-AC1" cell_refs="DB-b-290"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p158_repin.py" . DB158-1-AC1</invocation><expect>DB158-1-AC1 PASS</expect></criterion>
`DB158-1-AC1` -- the entry differs from the base only in the stale members' `pin` and `sha256` (each new pin an ancestor commit whose file bytes equal the sha256 and the file at HEAD); a member that was not stale is byte-identical; no other key of the entry (the deployed fields included), no other entry and no top-level key moved.
<criterion id="DB158-1-AC2" cell_refs="DB-b-290"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p158_repin.py" . DB158-1-AC2</invocation><expect>DB158-1-AC2 PASS</expect></criterion>
`DB158-1-AC2` -- the `BUILD_ONLY` package holds exactly the entry's `files` with every member's bytes equal to its source; the bundle's third-party imports are pyarrow plus the runtime's and the layer holds it; and the handler UNPACKED from the package passes the writer's behaviour on a fake S3 (the stored series carry `income_claim` absent beside null income, the manifests carry `calendar_source` and publisher 0.3.0, the 14 summary keys, the guard).
<criterion id="DB158-1-AC3" cell_refs="DB-b-290"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p158_repin.py" . DB158-1-AC3</invocation><expect>DB158-1-AC3 PASS</expect></criterion>
`DB158-1-AC3` -- the facts record equals the checker's recount (the re-pinned paths, the build-only hash) and the worker's commits change only the source map, the folder, the investigation file and task-order files.

<expected_criteria>DB158-1-AC1,DB158-1-AC2,DB158-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files, the layer (`aws lambda list-layer-versions` and `get-layer-version`, GET and LIST only, which the checker also makes). Writes: the one source-map file and your private folder. The `BUILD_ONLY` run writes a zip under a temporary directory only. No Terraform command, no AWS write, no upload, no push, no invoke.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W234-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~234/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-290.publish-source-map-repin-after-the-writer-drain.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 151 (round 149, workstream PUBWRITE), cell `DB-b-290`.
<owned_cells>DB-b-290</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB158-1-AC1, DB158-1-AC2, DB158-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~234/IRPT_DASHBD.TO-DB-b-290.publish-source-map-repin-after-the-writer-drain.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB158-1-AC1,DB158-1-AC2,DB158-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the re-pinned paths; the unchanged-member count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one source-map entry's pins in a branch; nothing is built for upload, uploaded, planned or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its re-pin clause was validated by the issuer against a real re-pin computed from git (green) and 10 single-fault arms (all red); its package and behaviour clauses reuse the proven checkers of rounds 147 and 148.
lane: the <paths> block IS the grant.
</preflight>
