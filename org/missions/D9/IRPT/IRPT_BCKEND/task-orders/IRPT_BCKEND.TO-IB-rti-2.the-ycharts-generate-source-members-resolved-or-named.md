# TO IRPT_BCKEND.TO-IB-rti-2 -- THE YCHARTS-GENERATE SOURCE MEMBERS RESOLVED TO TRUE SOURCES, OR HONESTLY NAMED UNRESOLVABLE: `irpt-ycharts-generate` cannot be rebuilt from HEAD by `build-and-upload.sh` (row S102): its `files[]` in `lambda-source-map.json` declares `firm_registry.json` and `settings.json`, and neither has a tracked source on disk (`infra/aws/lambda/investor-reporting/ycharts/generate/` holds only `job.py`, `recipe.py`, `templates.json`, `transport.py`, `entry.py`), while the LIVE zip serves both. `3.0.0_SA_CVO~B` confirmed it is NOT fixed: round 8's `S111` amended only the acceptance DENOMINATOR (7 -> 6 buildable), it did not repair the build. The CTO cut it in round 9 (wave 1 item 2).

<to_id>IRPT_BCKEND.TO-IB-rti-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~10</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B 2026-09-21 ~22:3xZ (round 9, wave 1, chain B, decomp v0.13 s.R9.1). On the CTO's round-8 analysis @8e0f9a127e (msg 99299) and row IRPT_BCKEND-S102. INVESTIGATE FIRST, READ-ONLY. REBUILD-AND-COMPARE ONLY: no upload, no apply, no update-function-code -- a served change is a NEW packet and both halves, never a rider on this order.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 9 (wave 1) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 (no addendum) | **Decomp cell:** `IB-rti-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.13, s.R9.1) | **outcome_ref:** FWD-2 / FWD-4 (the export chain) | **Rows:** `IRPT_BCKEND-S102` (ARMED, disarm_owner `2.0.0_SA_COO~B`), `W4-S34`, `S96` (the hand copy that was rejected), `S111` (its denominator amendment, REMEDIATED for that mismatch only)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~10`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~10;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-9-10` on branch `wk-irpt_bckend-9-10`, cut from CLOUD HEAD AFTER this order's own commit lands and verifies THIS FILE is present in it before spawning. First act: `cd /c/tmp/wk-irpt-9-10`, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-2.the-ycharts-generate-source-members-resolved-or-named.md` -- absent means STOP and file a row as row `IRPT_BCKEND-W7-S1` did. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing `/c/tmp/wk-irpt-9-10/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~10 <0.9.0_WK_IRPT_BCKEND~10@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`. Capture `safe-commit.sh` output to a file; ask `git log` whether it committed, never read its prose.
- Python `py -3.12`; AWS via `.tools/aws` (READ calls only in this cell). A recursive grep/find in Bash is rail-DENIED and aborts the WHOLE call: use Read/Grep/Glob and keep a gated read in its own call.

## THE CELL

- **(a) INVESTIGATE FIRST -- read-only, no write of any kind.** Read `infra/aws/lambda/ci/lambda-source-map.json`'s `irpt-ycharts-generate` entry in full (its `files[]`, `staged_from`, and its own `_staged_from_note`), rows `S102`/`W4-S34`/`S96`, and `infra/aws/lambda/ci/build-and-upload.sh` / `build-zip.sh`. **Print a RESOLUTION TABLE with its denominator: every declared member of `files[]` (the entry says 32) against the LIVE zip's members (row S102 says 31 -- ACCOUNT FOR THE DIFFERENCE by name, do not assume it away).** Obtain the live zip by reading the function's served package (`get-function` code location, then download; a READ of served bytes) and hash each member. For each of the two members with no source on disk, `firm_registry.json` and `settings.json`, search the repo AT HEAD for a TRACKED file or a tracked PRODUCER that yields it (start with `data/firm_registry.json`, which exists; find what produces `settings.json`) and compare BYTES with the live member: sha256 both sides, printed. Record each member as RESOLVED (source path @ commit, byte-identical to live) or UNRESOLVED (what you searched, what differed).
- **(b) THE BRANCHES -- decided by (a)'s table, never by preference.** RESOLVED for both: declare each member's TRUE source in that entry's `staged_from` (a producer or the tracked source of truth), touching nothing else in the source map. A member that is byte-different from live, or satisfiable ONLY by committing the live bytes as a new file: **STOP with a row** -- inventing the members, or committing a copy of served bytes for the purpose, is the hand copy S96 rejected. The CVO's diagnostic on the original row adds one FACT you must check rather than trust: the function's registry resolves through `IRPT_FIRM_REGISTRY=/var/task/firm_registry.json` (the packaged copy) and the diagnostic suggests it needs only `raw_keys.json` -- whether either declared member is even REQUIRED at runtime is a finding for the CTO and the issuer, NOT a licence to drop a declared member (that changes the served package and is its own packet).
- **(c) REBUILD-AND-COMPARE, LOCAL ONLY (only if (b) resolved both).** Build the function's zip from HEAD into a scratch directory using the repo's own staging logic. **NO upload to S3, NO Terraform, NO `update-function-code`, NO change to any live object.** Compare the rebuilt zip's members to the live zip's, member by member, sha256 both sides. Every member byte-identical, or each difference NAMED with its cause; a difference in a member's BYTES that is not explained is a STOP (that would change what is served).
- **(d) LANE.** The source map is lane-gated (row `W1-S48`: this project's own COO commit to it was refused, and the fix landed under an AE lane's authority). If the lane gate refuses a path in your `<paths>`, that is a BLOCKING row and a STOP -- never an override; the issuer re-addresses the order to an AE lane holding the grant, exactly as `IB-rth-1` was.

## DELIVERABLE
The resolution table (denominator printed, the 32-vs-31 difference accounted); the branch taken and why; the `staged_from` declarations (only if (b) resolved both); the local rebuild and member-comparison output; the result.md; the proof instance.

## BOUNDS
- READ-ONLY until (b) resolves both members; after that the ONLY writes are the two `staged_from` declarations in `lambda-source-map.json` and this cell's own deliverables.
- **No upload, no apply, no `update-function-code`, no live object changed.** No committing of the live zip's members as new source files.
- No change to any other function's entry, and no change to `S102`'s siblings (`S111`'s denominator amendment stands).
- A lane refusal is a BLOCKING row, never an override; `GIT_COMMIT_AUTHOR_OVERRIDE` is never used by a worker.
- The forward-looking-criterion bar; R-40 (content hash per artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; NO LIVE VENDOR CALL.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W10-S<k>` starting at 1, appended as a NEW fenced JSON block (CRLF, UTF-8, `grounding` AND `disposition` required, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); validate every fence still parses before committing; then keep working. Never edit this face, never widen the order.

<expected_criteria>R92-AC1, R92-AC2, R92-AC3</expected_criteria>
<criterion id="R92-AC1" cell_refs="IB-rti-2"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~10/battery_ib_rti_2.py --arm resolve</invocation><expect>IBR92-EVERY-DECLARED-MEMBER-RESOLVED-OR-NAMED-UNRESOLVED</expect></criterion>
**`R92-AC1` -- PASSES BY OUTPUT:** the resolution table covers EVERY declared member of `files[]` against the live zip (denominators printed on both sides, the declared-vs-live difference accounted by name), each member RESOLVED (a tracked source, byte-identical, sha256 both sides) or UNRESOLVED with what was searched. The token prints when the table is COMPLETE, whichever way each member resolves -- this criterion grades the measurement, not the outcome.

<criterion id="R92-AC2" cell_refs="IB-rti-2"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~10/battery_ib_rti_2.py --arm rebuild</invocation><expect>IBR92-YCHARTS-REBUILDS-FROM-HEAD-MEMBER-IDENTICAL-TO-LIVE</expect></criterion>
**`R92-AC2` -- PASSES BY OUTPUT, and ONLY on the resolved branch:** the local rebuild from HEAD contains both previously-missing members, every member's sha256 equals the live zip's (or each difference is named with a cause that does not change served behaviour), nothing was uploaded and nothing applied. If (a)/(b) left either member unresolved, NO token prints: the instance row carries the non-verdict status with the reason, the order stays open, and the STOP row plus the result IS the report -- an honest partial, never a manufactured pass.

<criterion id="R92-AC3" cell_refs="IB-rti-2" judgment="true"/>
**`R92-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED. THE BAR:** State for `3.0.0_SA_CVO~B`. PASS iff, for EACH of the two members, the `staged_from` names a path that is (i) tracked at HEAD and (ii) a TRUE source -- the checked-in file IS the source of truth, or it is the documented output of a tracked producer the entry's note names -- and (iii) is NOT a copy of the served bytes committed for the purpose (the shape row S96 rejected). FAIL if any member is satisfied by committing the live bytes. An honestly documented UNRESOLVED with a STOP is a PASS of THIS judgment (the honest outcome) and a non-verdict of `R92-AC2`. No verdict from the worker; every line citation carries `@<commit-ish>`.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-2.the-ycharts-generate-source-members-resolved-or-named.md
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/investor-reporting/ycharts/generate/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.13, cell `IB-rti-2` (s.R9.1).
<owned_cells>IB-rti-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired; this cell changes no live resource.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only reads of one function's served package under the operator identity; BLIND to whether the operator identity can `get-function` this function until the first read runs (a refusal is a BLOCKING row).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). `lambda-source-map.json` is LANE-GATED (row W1-S48) and is admitted here only while this order is non-terminal; a refusal is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R92-AC1, R92-AC2 (may carry the non-verdict status), R92-AC3 (judgment). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~10/IRPT_BCKEND.TO-IB-rti-2.the-ycharts-generate-source-members-resolved-or-named.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT (commit the battery, output and result BEFORE the instance); a blob pin is written `blob <hash>`; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO~B`. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND `R92-AC1` AND `R92-AC2` PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together. If `R92-AC2` carries its non-verdict status the order stays OPEN and that IS the correct final report.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why, and explicitly which branch of (b) you took).
