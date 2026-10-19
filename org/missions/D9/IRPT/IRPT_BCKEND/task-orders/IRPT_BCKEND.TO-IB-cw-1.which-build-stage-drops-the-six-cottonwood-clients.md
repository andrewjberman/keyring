# TO IRPT_BCKEND.TO-IB-cw-1 -- READ ONLY: name the build stage that drops the 6 Cottonwood clients the runner's guard refused on 2026-10-14, and what they share, in hashed ids and counts (CTO ruling on row D2-S239, msg 10699, part (a); the parked account-to-advisor link is checked FIRST)

<to_id>IRPT_BCKEND.TO-IB-cw-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~456</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-cw-1` (decomposition section 251) | **outcome_ref:** FWD-7 (the directory is READY at all 3 firms) | **Ordered by:** the CTO's ruling `deliverables/1.0.0_SA_CTO~DELL2/RULING_D2_S239_COTTONWOOD_DIRECTORY_WEDGE_20261019.md` part (a) and the row `IRPT_BCKEND-D2-S239`. **This order READS. It writes nothing to AWS, nothing to S3, and changes no source file.**

---

## WORKER FACE

**Cell `IB-cw-1` (inlined).** Cottonwood's directory build for as-of 2026-10-14 was REFUSED by the runner's own guard (`data/assets/scripts/gold/investor_reporting/directory_runner.py`, `run_firm`, lines about 1282 to 1293): `BUILD_DROPS_SOURCE_ENTRY: 6 previous client(s) are still in the source snapshot but missing from this build; nothing is landed`. `held` there is what `carry_forward_removed(previous served entries, this build's entries, source_ids, completion_date)` returns: previous clients that are NOT in the build (`entries = BUILDERS["cottonwood"](data, ...)`) but ARE in the source snapshot (`source_ids = source_client_ids("cottonwood", data)`). So some stage between the source and the build's entry set drops six clients that the source still holds. **Find that stage, say what the six share, and say whether it is a build fault or a genuine removal. Do not fix anything.** The CTO's rule for this read: a build fault gets its own fix cell and pair; a genuine removal goes through the guard's documented path under a pair with evidence that the SOURCE itself ended them.

**Privacy (a hard rule, graded mechanically).** Hashed ids and counts only. A client is named in your files ONLY as the first 12 lowercase hex characters of `sha256(<its opaque id as a string>)`. No `cli_` or `acc_` id, no account or household number, no name, no e-mail, no digit run of 9 or more, and no hex string of any length other than exactly 12 (a full 64-hex sha256 of a source LINE is allowed; cite commits by their first 10 characters). Raw output of the replay stays in a scratch directory OUTSIDE the repository and is deleted when you finish. Your notes quote no output line that carries an id.

**Do, in this order:**
1. **Read the code (no data yet).** In `directory_runner.py` find: the refusal site; `carry_forward_removed`; `source_client_ids`; and `BUILDERS["cottonwood"]` with every function it calls to turn source rows into entries. Write in `IBcw1_notes.md` the stage order from the source read to the entry set as a numbered list of `file:line` and one clause each.
2. **The parked link FIRST.** The Cottonwood account-to-advisor map is parked for want of a source. Find that record (search the repository with the Grep tool or `comp-find`, for example for `account-to-advisor`, `advisor` with `cottonwood`, `PARKED`), say in one sentence what the parked item is, and whether the Cottonwood build reads that link anywhere (`used_by_build`; if true, cite the line).
3. **Replay the refusal, read-only.** From your worktree root: `python data/assets/scripts/gold/investor_reporting/directory_runner.py --firms cottonwood --as-of 2026-10-14 --dry-run` with **NO `--upload` and NO `--local-out`**, so nothing is written anywhere. It reads the source and the previous served directory (S3 reads under the agent identity the shell already holds). Direct its stdout to a file in your scratch directory. If it reads the same six, you can bisect the stages in a scratch script (outside the repository) that imports the runner functions and compares, stage by stage, the set of client ids in the source snapshot against the set after each stage, to find the FIRST stage at which the six are gone. **If any read is AccessDenied or the replay cannot reproduce the refusal, STOP, write what failed (prefix names only, no ids) into `IBcw1_notes.md` and `verdict` `UNDETERMINED`, and report; do not widen any access.**
4. **What the six share.** For the six dropped clients and for the retained clients as the control, count (in aggregate) the attributes that could explain the drop, for example: present in each source table the builder joins, has an advisor or account mapping, has a non-zero balance or a position on the as-of date, carries a closed or terminated marker. Each attribute is one record `{name, dropped_with, dropped_total (always 6), retained_with, retained_total}` in the findings.
5. **Write `IBcw1_findings.json`** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~456/` with exactly these fields (the check reads them):
```
{"firm":"cottonwood","as_of":"2026-10-14","dropped_count":6,
 "dropped_hashed_ids":["<12 hex>","<12 hex>","<12 hex>","<12 hex>","<12 hex>","<12 hex>"],
 "stage":{"file":"<repo-relative path>","line":<int>,"excerpt_sha256":"<64 hex: sha256 of that line, stripped, as it is at HEAD>","what":"<one sentence, 10 to 300 chars>"},
 "parked_link":{"checked_first":true,"what":"<one sentence>","used_by_build":<true|false>,"file":"<only when true>","line":<int, only when true>,"excerpt_sha256":"<only when true>"},
 "shared":{"attributes":[{"name":"...","dropped_with":<0..6>,"dropped_total":6,"retained_with":<int>,"retained_total":<int>}]},
 "verdict":"BUILD_FAULT" | "GENUINE_REMOVAL" | "UNDETERMINED",
 "evidence_for_verdict":"<10 to 400 chars, no ids>",
 "reads":{"aws_writes":0,"s3_puts":0,"raw_ids_in_artifacts":0}}
```
The `excerpt_sha256` is computed by the check from the line you cite, so cite the line that DOES the dropping (the join, filter or condition), not a nearby comment. Also write the proof instance named under proof_of_spec, validate it with `python .tools/proof-of-spec-check.py <instance>`, and write `IBcw1_criteria_output.txt` (AC1 and AC2 output verbatim, run BEFORE the commit; AC3 after).
6. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~456 <0.9.0_WK_IRPT_BCKEND~456@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): your deliverables folder and any surprise row. If safe-commit is slow it is waiting on other seats: wait, never run it twice at once, never amend. Do not push. Report once, under 150 words: the stage (file:line), the verdict, the counts, AC3's result.

**Criteria (run each under `timeout 300` from the repository root; AC3 reads `HEAD~1..HEAD`, so run it AFTER your one commit):**

<criterion id="IBCW1-AC1" cell_refs="IB-cw-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r257/p257_cells.py" . IBCW1-AC1</invocation><expect>IBCW1-AC1 PASS</expect></criterion>
<criterion id="IBCW1-AC2" cell_refs="IB-cw-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r257/p257_cells.py" . IBCW1-AC2</invocation><expect>IBCW1-AC2 PASS</expect></criterion>
<criterion id="IBCW1-AC3" cell_refs="IB-cw-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r257/p257_cells.py" . IBCW1-AC3</invocation><expect>IBCW1-AC3 PASS</expect></criterion>

<expected_criteria>IBCW1-AC1, IBCW1-AC2, IBCW1-AC3</expected_criteria>

What the checks grade: AC1 the findings file's shape, six distinct 12-hex ids, every cited `file:line` existing at HEAD with the stated hash, the parked-link check recorded first, consistent counts; AC2 that nothing in your deliverables folder carries a raw client identifier or an odd-length hex run; AC3 that your one commit touches only this order's paths. **They do not grade whether your answer is TRUE: the issuer re-traces the stage itself before it rules.** Do not edit the checks.

## BOUNDS

- **Grant:** write `deliverables/0.9.0_WK_IRPT_BCKEND~456/`; the surprise channel for rows; read the repository; read S3 and run the runner with `--dry-run` only (no `--upload`, no `--local-out`). **NO AWS write of any kind; NO S3 put; NO source, Terraform or registry change; NO Lambda invoke; NO SSM command; NO raw client identifier in any file; NO push.**
- **Refusal clause:** STOP and report, writing nothing further beyond the notes, if a read is denied, if the replay cannot reproduce the refusal, or if answering would need a write. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~456/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-cw-1.which-build-stage-drops-the-six-cottonwood-clients.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 251 (round 14, workstream ~PM), cell `IB-cw-1`.
<owned_cells>IB-cw-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBCW1-AC1, IBCW1-AC2, IBCW1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~456/IRPT_BCKEND.TO-IB-cw-1.which-build-stage-drops-the-six-cottonwood-clients.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only investigation; nothing is deployed or written, the replay is `--dry-run` with no upload and no local mirror, and the runner makes no put on that path (`run_firm` raises before any put only when a call WOULD write; a dry run records the same verdict).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed; the reads use the identity the shell already holds, and a denied read is a STOP, never a widening.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p257_cells.py IBCW1 dry-run at base on dell2 2026-10-19: AC1, AC2, AC3 FAIL (no findings). Positive control (control257.py) over synthetic git repos with a source file to cite: the clean findings, a findings with a used parked link carrying its citation, and a notes file holding a full sha256 and a ten-hex commit PASS; 17 AC1 negatives (a missing field, the wrong firm, a count of five, duplicate ids, an id not 12 hex, a wrong excerpt hash, a line out of range, a cited file absent, an empty stage sentence, the parked link not checked first, used without a citation, empty attributes, inconsistent counts, a dropped total not six, an invalid verdict, an AWS write, an S3 put), 5 AC2 negatives (a cli_ id, an acc_ id, a 12-digit run, an e-mail address, a 40-hex run) and 3 AC3 negatives (a file outside the paths, a write under data/, the findings not in the commit) each fail their own arm, 0 unexpected. NOT measured by me: whether the cited stage really drops the clients (the issuer's re-trace), the replay itself, any live read.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~456`. Class WORLD (the work reads live client data from S3 under the agent identity; it writes nothing).
</preflight>
