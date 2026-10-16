# TO IRPT_DASHBD.TO-DB-f-2203 -- the FWD-5 49 FINANCIAL GOLD BUNDLE GAINS THE TRANSACTION PRODUCER, ONE CELL (W2b): the source-map entry `irpt-49f-reporting-gold-lambda` lists `account_transaction.py` and `transaction_words.json` as members with their pins; nothing else in the file moves; the CTO's round-135 analysis, item 1 (msg 9837)

<to_id>IRPT_DASHBD.TO-DB-f-2203</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2203</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>136</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-135 analysis @8d48df1751 (msg 9837), item 1: the 49 Financial transaction wiring; the issuer's plan names the bundle members and their pins as the sibling of the handler and Terraform cells | **Rows:** IRPT_DASHBD-D2-W2203-S<k> | **Decomp cell:** `DB-f-2203` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R136_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

**Risk class WORLD** is the floor of the path below (`infra/` path): one JSON entry in a branch; no build, no upload, no AWS call, no push. The build and the apply are the applier's under a later signed pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2203` (branch `wk-IRPT_DASHBD-2203`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2203/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS in this order: make no AWS call of any kind and run no build script.** Client data is not involved. Write files with the Write or Edit tool or a small python script file, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** The 49 Financial gold Lambda's artifact is built from `infra/aws/lambda/ci/lambda-source-map.json`, entry `irpt-49f-reporting-gold-lambda`: `source_dir` plus a `files` list (what the zip holds) and a `staged_from` list (a pin, a commit and the sha256 of the file at it, for each member that is not under `source_dir`). The transaction producer `data/assets/scripts/gold/irpt_reporting/account_transaction.py` and its words file `transaction_words.json` are in neither list, so a bundle built today cannot import them and the handler's guarded import (sibling order DB-f-2201) would fail by name. The producer imports `account_return_daily`, `opal_naming` and `trading_calendar` (already members) and pandas and pyarrow (the layer).

**The cell (`DB-f-2203`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_sourcemap.py` (your two criteria; `entry_problems`, `ac1` and `import_problems` are the exact spec; it has a `--selftest`) and its pinned base shape `checks/r136/sourcemap_base_entry.json`; the entry in the source map (read only the entry `irpt-49f-reporting-gold-lambda`).
2. **The edit: ONE file, `infra/aws/lambda/ci/lambda-source-map.json`, ONE entry, additions only.**
   - `files`: append, LAST and in this order, `data/assets/scripts/gold/irpt_reporting/account_transaction.py` and `data/assets/scripts/gold/irpt_reporting/transaction_words.json`.
   - `staged_from`: append, LAST and in the same order, two objects with EXACTLY the keys `repo_path`, `pin`, `packaged_as`, `sha256`: `repo_path` and `packaged_as` both the member's repo path; `sha256` the sha256 of the file's bytes now; `pin` the FULL 40-hex commit hash of the last commit that changed that file on your branch (`git log -1 --format=%H -- <path>`), and `git show <pin>:<path>` must hash to the same sha256.
   - Do NOT touch any other key of the entry (the notes, the deploy records, the artifact hash), any existing member's pin, or any other function of the file. Do NOT run the build. Keep the file's existing formatting (indentation, key order, line endings) so the diff is the added lines only; ASCII.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_sourcemap.py" . DBF136-3-AC1`, then `DBF136-3-AC2`.
4. **Record** `RD_BUNDLE_MEMBERS_FACTS_R136.json` in your folder with EXACTLY these fields: `entry` ("irpt-49f-reporting-gold-lambda"); `files_before` and `files_after` (integers); `staged_before` and `staged_after` (integers); `pins` (a list of two objects `{repo_path, pin, sha256}`); `imports_outside_the_bundle` (a list, expected empty); `words` (one paragraph, 80 to 1800 characters: what changed, and what is NOT proven: nothing was built, uploaded or applied, the existing members' pins were not re-pinned, and whether the bundle imports the producer is read at the applier's build and the first fire).

<criterion id="DBF136-3-AC1" cell_refs="DB-f-2203" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_sourcemap.py" . DBF136-3-AC1</invocation><expect>DBF136-3-AC1 PASS</expect></criterion>
`DBF136-3-AC1` -- the entry is the base's paths plus the two members appended last, in order; its other keys are the base's; the two `staged_from` objects carry exactly the four keys, the file's sha256 now, and a full commit hash at which the file hashes to that same sha256. Base: FAIL.
<criterion id="DBF136-3-AC2" cell_refs="DB-f-2203" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_sourcemap.py" . DBF136-3-AC2</invocation><expect>DBF136-3-AC2 PASS</expect></criterion>
`DBF136-3-AC2` -- the closure: every import of the producer is stdlib, the layer, or a member of the entry's `files`; the file keeps its top-level keys, the entry, and ASCII. Base: FAIL.

<expected_criteria>DBF136-3-AC1,DBF136-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other entry of the source map, the build script, the producer, the words file, the handler and every Terraform file.
- **AWS: none; no build; no push.** The source map is shared with other lanes (re-pins of other entries): if your merge conflicts, you do not resolve it; the issuer does.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2203-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES (the file is shared and append-only). Commit with `.tools/safe-commit.sh`; run its gates in the background and wait. ASCII only. If a commit is refused because the order is `complete`, stop and report.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2203/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2203.fwd5-49f-gold-bundle-gains-the-transaction-producer.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R136_F.md</decomp_doc> round 136, workstream ~F2 (F-SHIP), cell `DB-f-2203`.
<owned_cells>DB-f-2203</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF136-3-AC1, DBF136-3-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2203/IRPT_DASHBD.TO-DB-f-2203.fwd5-49f-gold-bundle-gains-the-transaction-producer.proof_of_spec.json`
(copy the shape of the instance at `deliverables/0.9.0_WK_IRPT_DASHBD~2101/`). Validate it with `python .tools/proof-of-spec-check.py <instance> DBF136-3-AC1,DBF136-3-AC2 --governing-order <this order>` (from the repo root, the order path repo-relative) BEFORE you finish; pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the facts record's numbers and the two pins; the commit hash(es); anything off-task (as row ids). No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one JSON entry edited in a branch; no build, upload or apply.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the worker has no AWS access.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF136-3-AC1 and AC2 FAIL at base, the checker's helpers are exercised by its self-test (7 arms) and the intended edit applied to a scratch copy passed both clauses.
lane: the <paths> block IS the grant.
</preflight>
