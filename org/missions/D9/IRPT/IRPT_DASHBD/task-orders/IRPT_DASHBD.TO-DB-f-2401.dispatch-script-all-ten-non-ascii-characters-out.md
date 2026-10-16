# TO IRPT_DASHBD.TO-DB-f-2401 -- ALL TEN NON-ASCII CHARACTERS OUT of `data/inf/scripts/gold/orion-gold-dispatch.sh`, ONE cell: eight em dashes and two section signs, one per line on ten lines, replaced by the fixed ASCII mapping; no other character of the file changes; the CTO's round-135 ADDENDUM 1 (msg 10025, CLAUDE.md section 4)

<to_id>IRPT_DASHBD.TO-DB-f-2401</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2401</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>137</round>
<workstream>F2ASCII</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2ASCII (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-135 ADDENDUM 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_135_20261016.md` @0527421847, msg 10025): "you own the 10 non-ASCII characters in orion-gold-dispatch.sh (all out)"; CLAUDE.md section 4: in a file that already carries non-ASCII the only two safe moves are ALL non-ASCII out, or every reader explicit, never a subset | **Rows:** IRPT_DASHBD-D2-W2401-S<k> | **Decomp cell:** `DB-f-2401` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R137_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2401` (branch `wk-IRPT_DASHBD-2401`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2401/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. Offline only; **no AWS call of any kind, and the script is NOT uploaded or run** (the live copy on the runner is the pre-round-135 one; deploying this is a later release's act). No client data. Write files with the Edit or Write tool or a small python script FILE, not shell heredocs (the shell eats backslash sequences). Do not grep or find recursively over the repo; read named files.

**Why.** The dispatch script carries exactly ten non-ASCII characters, all in comments or messages: eight EM DASHES (U+2014) and two SECTION SIGNS (U+00A7), one per line on lines 50, 659, 986, 1254, 1270, 1352, 1433, 1594, 1596 and 2000 of the base. A file that already carries non-ASCII is read wrongly by a default cp1252 reader without any error, so the rule is ALL out. The base is the repo copy as it stands after the round-135 insertion (sha256 `70b5774422c6...`, pinned at `deliverables/2.0.0_SA_COO~F2/checks/r136/dispatch_r137_base.sh.txt`).

**The cell (`DB-f-2401`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_ascii.py` (your two criteria; `mapped` and `line_problems` are the exact spec; it has a `--selftest`) and the test file `data/inf/scripts/gold/tests/test_dispatch_txn_block.py` (its tests that compare the file with the round-135 pinned base `checks/r135/dispatch_base.sh.txt` read a pure insertion, which this edit is no longer; see step 3).
2. **The edit: ONE file, `data/inf/scripts/gold/orion-gold-dispatch.sh`, ten characters.** Each em dash becomes TWO hyphen-minus characters (`--`), keeping the spaces around it; each section sign (always directly before a digit) becomes the word `section` and one space (`brief section 4.3.`). Nothing else changes: the same number of lines, every other character of every line identical, LF endings kept. `bash -n` passes.
3. **The tests: ONE file, `data/inf/scripts/gold/tests/test_dispatch_txn_block.py`.** The tests that compare the script with the round-135 base (the pure-insertion test and the added-lines-ASCII test, and any test reading the base's lines) must now read: the script equals the base plus the round-135 insertions AND the ten fixed replacements (compute the expected text from the pinned base by applying the same mapping to the base's non-ASCII lines before diffing; do not weaken a test to pass it). Add ONE test whose name holds `whole` and `ascii` asserting the ENTIRE file is ASCII (`bytes.decode("ascii")` succeeds). The file then holds at least 29 tests, and it and the three existing dispatch-related test files pass: `test_aor_resolution.py`, `test_aor_fold_derivation.py` and `data/inf/manual_api/test_pull_inflection_scope_account_returns.py`.
4. **Run the checks yourself:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_ascii.py" . DBF137-4-AC1`, then `DBF137-4-AC2`.
5. **One mutant** (temporary, reverted): put one em dash back on one of the ten lines; the whole-file ASCII test and the checker must fail. Say which.

<criterion id="DBF137-4-AC1" cell_refs="DB-f-2401" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_ascii.py" . DBF137-4-AC1</invocation><expect>DBF137-4-AC1 PASS</expect></criterion>
`DBF137-4-AC1` -- the dispatch script holds no non-ASCII character; against the pinned base it has the same lines, every line of the base without a non-ASCII character is identical, and each of the ten others equals the base line with the fixed mapping applied (two hyphens for the em dash, `section ` for the sign); `bash -n` passes; LF endings. Base: FAIL.
<criterion id="DBF137-4-AC2" cell_refs="DB-f-2401" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_ascii.py" . DBF137-4-AC2</invocation><expect>DBF137-4-AC2 PASS</expect></criterion>
`DBF137-4-AC2` -- the dispatch test file holds at least 29 tests including one named for the whole file being ASCII, and it and the three existing dispatch-related test files pass. Base: FAIL (28 tests).

<expected_criteria>DBF137-4-AC1,DBF137-4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the pinned base copies, every other script, the launcher, the other tests, every Terraform file.
- **AWS: none. NOT UPLOADED. NOT RUN.** The neighbour's advisory HOLD (`org/critical_paths/HOLD_INF_CANONICAL_NNA_REBUILD_20260713.md`, now a standing release since its AMEND 62) concerns the `build_assets_dim.py` collision between `code/gold` and `code/silver`; this edit touches repo text only and no S3 object.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker rule and this order disagree, follow this order and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2401-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait. ASCII only in anything you write. If a commit is refused because the order is `complete`, stop and report.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2401/
data/inf/scripts/gold/orion-gold-dispatch.sh
data/inf/scripts/gold/tests/test_dispatch_txn_block.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2401.dispatch-script-all-ten-non-ascii-characters-out.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R137_F.md</decomp_doc> round 137, workstream F2ASCII (F-SHIP), cell `DB-f-2401`.
<owned_cells>DB-f-2401</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF137-4-AC1, DBF137-4-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2401/IRPT_DASHBD.TO-DB-f-2401.dispatch-script-all-ten-non-ascii-characters-out.proof_of_spec.json`
(copy the shape of the instance at `deliverables/0.9.0_WK_IRPT_DASHBD~2103/`). Validate it with `python .tools/proof-of-spec-check.py <instance> DBF137-4-AC1,DBF137-4-AC2 --governing-order <this order>` (from the repo root, the order path repo-relative) BEFORE you finish; pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the test count; the mutant and what failed; the commit hash(es); anything off-task (as row ids). No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: ten comment and message characters in a script in a branch; nothing is uploaded, scheduled or run.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the worker has no AWS access.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF137-4-AC1 and AC2 FAIL at base (ten non-ASCII characters; 28 tests), the checker's helpers are exercised by its self-test (8 arms) and the intended mapping applied to a scratch copy passes AC1.
lane: the <paths> block IS the grant.
</preflight>
