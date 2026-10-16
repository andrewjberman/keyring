# TO IRPT_DASHBD.TO-DB-f-2205 -- the RE-PIN of the two STALE members of the 49 Financial gold bundle, ONE cell: `lib/trading_calendar.py` and `infra/logic/registry/systems.json` in the source-map entry `irpt-49f-reporting-gold-lambda` take the pin and sha256 of their current content; nothing else in the file moves; the cause of the apply's STOP at Act 3 (IB2 msgs 9990 and 9994)

<to_id>IRPT_DASHBD.TO-DB-f-2205</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2205</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>137</round>
<workstream>F2REPIN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2REPIN (the re-pin after the apply's STOP, `~F2`) | **Ordered by:** the issuer, on `0.7.0_AE_CloudOps~IB2`'s STOP of `TO-DB-f-2204` at Act 3 (msgs 9990 and 9994: the transaction stage raised `AttributeError: module 'trading_calendar' has no attribute 'first_trading_day_on_or_after'` on every day, because the bundle's `trading_calendar.py` member is pinned at `b2b748866020`, which predates the function); the CTO's round-136 analysis (msg 9966) for the apply | **Rows:** IRPT_DASHBD-D2-W2205-S<k> | **Decomp cell:** `DB-f-2205` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R137_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

**Risk class WORLD** is the floor of the path below (`infra/` path): one JSON entry in a branch; no build, no upload, no AWS call, no push.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2205` (branch `wk-IRPT_DASHBD-2205`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2205/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS in this order: make no AWS call of any kind and run no build script.** Client data is not involved. Write files with the Write or Edit tool or a small python script FILE (not shell heredocs: backslash sequences break). Do not grep or find recursively over the repo; read named files.

**Why.** The artifact of the 49 Financial gold Lambda is built from `infra/aws/lambda/ci/lambda-source-map.json`, entry `irpt-49f-reporting-gold-lambda`: each `staged_from` object pins a member to a commit and the sha256 of the file at it, and the build packages the PINNED blob (`git show <pin>:<path>`), not the working file. A read of all 23 pins found TWO stale: `lib/trading_calendar.py` (pin `b2b7488660...`, sha256 `9bc467c6ce4d...`) and `infra/logic/registry/systems.json` (pin `21c6720238...`, sha256 `0aba15f9cc...`). The other 21 equal their files now. The transaction producer calls `trading_calendar.first_trading_day_on_or_after`, which the old pinned blob lacks, so the deployed stage failed.

**The cell (`DB-f-2205`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_repin.py` (your two criteria; `ac1`, `ac2`, `wanted_attributes` and `top_level_names` are the exact spec; it has a `--selftest`) and the cut's shape `checks/r136/sourcemap_entry_r137_base.json`; read only the entry `irpt-49f-reporting-gold-lambda` in the source map.
2. **The edit: ONE file, `infra/aws/lambda/ci/lambda-source-map.json`, ONE entry, TWO objects.** For each of the two stale members: set `pin` to the FULL 40-hex hash of the LAST commit that changed that file on your branch (`git log -1 --format=%H -- <repo_path>`), and `sha256` to the sha256 of the file's bytes now; `git show <pin>:<path>` must hash to the same sha256. Change NOTHING else: not the other 21 pins, not `files`, not any other key of the entry (the notes, the deploy records, the artifact hash), not any other function of the file. Keep the file's formatting (indentation, key order, line endings) so the diff is exactly the changed `pin` and `sha256` lines; ASCII.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_repin.py" . DBF137-1-AC1`, then `DBF137-1-AC2`. If AC2 names a member that is not one of the two, STOP on it: file a BLOCKING row naming the module, the attribute and the pin, and do not repair it.
4. **Record** `RD_REPIN_FACTS_R137.json` in your folder with EXACTLY these fields: `entry` ("irpt-49f-reporting-gold-lambda"); `members_checked` (23); `stale_before` (the list of the two repo paths); `repinned` (a list of two objects `{repo_path, old_pin, new_pin, old_sha256, new_sha256}`); `stale_after` (0); `attribute_closure` ({`consumers` (the checker's two files), `attributes_checked` (an integer: the number of `module.attr` and imported names the checker verified), `missing` (0)}); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: nothing was built, uploaded or applied; the bundle's behaviour is read at the applier's next build and dry run).

<criterion id="DBF137-1-AC1" cell_refs="DB-f-2205" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_repin.py" . DBF137-1-AC1</invocation><expect>DBF137-1-AC1 PASS</expect></criterion>
`DBF137-1-AC1` -- every staged member of the entry is CURRENT: its sha256 equals the file's sha256 now, its pin is a full commit hash that is an ancestor of HEAD, and the file at that commit hashes to the same sha256; the entry's files, staged (repo_path, packaged_as) pairs and other keys are the cut's, unchanged. Base: FAIL (two stale).
<criterion id="DBF137-1-AC2" cell_refs="DB-f-2205" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_repin.py" . DBF137-1-AC2</invocation><expect>DBF137-1-AC2 PASS</expect></criterion>
`DBF137-1-AC2` -- the attribute closure: every `module.attr` the gold handler and the transaction producer read from a bundle member, and every name they import from one, is defined at the top level of that member's PINNED blob. Base: FAIL (`trading_calendar.first_trading_day_on_or_after` is not in the pinned blob).

<expected_criteria>DBF137-1-AC1,DBF137-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other entry of the source map, the build script, every member file, the handler, every Terraform file.
- **AWS: none; no build; no push.** The source map is shared with other lanes (stamps of other entries' artifact hashes): if your merge conflicts, you do not resolve it; the issuer does.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2205-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES (the file is shared and append-only). Commit with `.tools/safe-commit.sh`; run its gates in the background and wait. ASCII only. If a commit is refused because the order is `complete`, stop and report.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2205/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2205.re-pin-the-two-stale-members-of-the-49f-gold-bundle.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R137_F.md</decomp_doc> round 137, workstream F2REPIN (F-SHIP), cell `DB-f-2205`.
<owned_cells>DB-f-2205</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF137-1-AC1, DBF137-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2205/IRPT_DASHBD.TO-DB-f-2205.re-pin-the-two-stale-members-of-the-49f-gold-bundle.proof_of_spec.json`
(copy the shape of the instance at `deliverables/0.9.0_WK_IRPT_DASHBD~2203/`). Validate it with `python .tools/proof-of-spec-check.py <instance> DBF137-1-AC1,DBF137-1-AC2 --governing-order <this order>` (from the repo root, the order path repo-relative) BEFORE you finish; pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the facts record's numbers and the two new pins; the commit hash(es); anything off-task (as row ids). No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one JSON entry's two objects edited in a branch; no build, upload or apply.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the worker has no AWS access.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF137-1-AC1 and AC2 FAIL at base with the two named reasons (two stale pins; the missing function in the pinned blob) and the checker's helpers are exercised by its self-test (5 arms).
lane: the <paths> block IS the grant.
</preflight>
