# TO IRPT_BCKEND.TO-IB-cw-3 -- READ ONLY: list every reader of the directory's client key in this repository and say what a re-key (an account moving from an account-level key to a relationship-level key) moves for each, with the file:line of each reader and of the release path (CTO ruling on row D2-S239, msg 10788; ruling 481d; pause lifted msg 11047)

<to_id>IRPT_BCKEND.TO-IB-cw-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~459</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-cw-3` (decomposition section 253) | **outcome_ref:** FWD-7 (the directory is READY at all 3 firms) | **Ordered by:** the CTO's msg 10788 (S239: "In the pair, list every reader of the client key (pages, HMAC lists, exports) and state what the re-key moves for each") and msg 11047. **This order READS the repository only. It reads no S3 object, writes nothing to AWS or S3, and changes no source file.**

---

## WORKER FACE

**Cell `IB-cw-3` (inlined).** The Cottonwood directory's build is refused by the runner's drop guard (`data/assets/scripts/gold/investor_reporting/directory_runner.py`, `carry_forward_removed`, about line 993) because 11 previous client keys are missing from the new build. A read has shown each of the 11 is an ACCOUNT that was keyed at account level in the served directory and is now keyed at relationship level (the account is still served, under a different `ids.client_id`). The CTO has approved a guard that counts such a key as retained, under a never-widen pair, and the pair must list **every reader of the client key and say what the re-key moves for each**. **Find those readers in this repository, give the file and line of each, and classify what a re-key does to each. Do not fix or change anything.**

Terms: the directory entry carries `ids.client_id` (or, for a relationship entry, `ids.relationship_id`); `entry_key(e)` in the runner returns the one the refresh compares; an entry also carries `ids.account_ids` (the accounts it holds). A RE-KEY means: the same account ids, a different client key.

**Privacy (a hard rule, graded mechanically).** This read touches NO client data, so no id of any kind belongs in your files: no `cli_` or `acc_` id, no digit run of 9 or more, no e-mail, and no hex string of any length other than exactly 12 (a full 64-hex sha256 of a source LINE is allowed; cite commits by their first 10 characters).

**Do, in this order:**
1. **Search the repository with the Grep tool** (never recursive `grep` in a shell: the repo's rail refuses it) for these terms, over `data/assets/scripts/gold/investor_reporting`, `infra/aws/lambda/investor-reporting`, `lib`, `infra/logic` and `docs`: `client_id`, `entry_key`, `relationship_id`, `ids.client_id`, `account_ids`, `directory.json`, `hmac_list_forms`. Record the terms you searched and, from the Grep results, how many files were scanned and how many held a hit (`census`). If a count is not available from a tool, scan the folder listings and say so in the notes. The portal is a separate repository (a submodule not in your worktree): say in the notes that it is NOT READ here and name no portal reader.
2. **Decide which hits are READERS of the client key** (code that takes a directory entry's client key, or the directory's entries keyed by it, and does something with it), and give each an id `R01`, `R02`, ... with: `kind` (PAGE, API, HMAC_LIST, EXPORT, REFRESH_COMPARE, RUNNER, TEST, OTHER), `file`, `line` (the line that reads or compares the key), `excerpt_sha256` (sha256 of that line, stripped, as it is at HEAD), `keyed_on` (client_id, relationship_id, entry_key, account_ids, other), `rekey_effect`, and `what` (one sentence, 10 to 300 characters, saying what the reader does with the key and what changes for it when the key of an unchanged account set changes).
   - `rekey_effect`: `NONE` (the reader does not depend on the old key value); `KEY_CHANGES_ENTRY_REMAINS` (the entry stays and carries the new key, so anything the reader stored or compared under the old key value no longer matches); `ENTRY_LOST` (the reader would drop or hide the entry on a re-key); `UNKNOWN` (you cannot tell from the code: say why in the `what`).
   - There MUST be at least four readers, and among them at least one `REFRESH_COMPARE` (the Lambda side compares keys between the previous and the new directory: start in `infra/aws/lambda/investor-reporting/directory/refresh.py`, `_entry_key`), one `HMAC_LIST` (the account-id list producer: `hmac_list_forms` and `emit_hmac_list` in the runner) and one `RUNNER` (the runner's own guard, `carry_forward_removed` and `entry_key`).
3. **The release path.** Say how a changed `directory_runner.py` reaches the host that builds the directory (the bundle or the repository path the build command runs), as ONE record `release_path` with `file`, `line`, `excerpt_sha256` and `what` (10 to 300 characters). Start from the SSM dispatch in `refresh.py` (`SsmBuildDispatcher`, `bundle_uri`).
4. **Write `IBcw3_findings.json`** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~459/` with exactly these fields (the check reads them):
```
{"firm":"cottonwood",
 "readers":[{"id":"R01","kind":"REFRESH_COMPARE","file":"<repo-relative path>","line":<int>,"excerpt_sha256":"<64 hex>","keyed_on":"entry_key","rekey_effect":"KEY_CHANGES_ENTRY_REMAINS","what":"<10 to 300 chars>"}, ...],
 "census":{"terms":["client_id","entry_key","relationship_id", ...],"files_scanned":<int > 0>,"files_with_hits":<int, at least the number of distinct files your readers cite>},
 "release_path":{"file":"...","line":<int>,"excerpt_sha256":"<64 hex>","what":"<10 to 300 chars>"},
 "reads":{"aws_writes":0,"s3_puts":0}}
```
   Also write `IBcw3_notes.md` (the search you ran, the hits you judged NOT to be readers and why in one line each, and the NOT READ list: at least the portal), the proof instance named under proof_of_spec (validate it with `python .tools/proof-of-spec-check.py <instance>`), and `IBcw3_criteria_output.txt` (AC1 and AC2 output verbatim, run BEFORE the commit; AC3 after).
5. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~459 <0.9.0_WK_IRPT_BCKEND~459@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): your deliverables folder and any surprise row. If safe-commit is slow it is waiting on other seats: wait, never run it twice at once, never amend. Do not push. Report once, under 150 words: the reader count by kind, the `rekey_effect` counts, AC3's result.

**Criteria (run each under `timeout 300` from the repository root; AC3 reads `HEAD~1..HEAD`, so run it AFTER your one commit):**

<criterion id="IBCW3-AC1" cell_refs="IB-cw-3"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r259/p259_cells.py" . IBCW3-AC1</invocation><expect>IBCW3-AC1 PASS</expect></criterion>
<criterion id="IBCW3-AC2" cell_refs="IB-cw-3"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r259/p259_cells.py" . IBCW3-AC2</invocation><expect>IBCW3-AC2 PASS</expect></criterion>
<criterion id="IBCW3-AC3" cell_refs="IB-cw-3"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r259/p259_cells.py" . IBCW3-AC3</invocation><expect>IBCW3-AC3 PASS</expect></criterion>

<expected_criteria>IBCW3-AC1, IBCW3-AC2, IBCW3-AC3</expected_criteria>

What the checks grade: AC1 the findings file's shape, at least four readers with distinct ids and closed-set fields, the three required kinds present, every cited `file:line` existing at HEAD with the stated hash, the census terms and consistent counts, the cited release path; AC2 that nothing in your deliverables folder carries a raw identifier or an odd-length hex run; AC3 that your one commit touches only this order's paths. **They do not grade whether your answer is TRUE: the issuer re-reads the cited lines itself before it rules.** Do not edit the checks.

## BOUNDS

- **Grant:** write `deliverables/0.9.0_WK_IRPT_BCKEND~459/`; the surprise channel for rows; read the repository. **NO S3 read or write; NO AWS call of any kind; NO source, Terraform or registry change; NO Lambda invoke; NO SSM command; NO identifier of any kind in any file; NO push.**
- **Refusal clause:** STOP and report, writing nothing further beyond the notes, if a required kind (REFRESH_COMPARE, HMAC_LIST or RUNNER) has no reader in the repository, or if answering would need a write. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~459/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-cw-3.who-reads-the-cottonwood-client-key-and-what-a-rekey-moves.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 253 (round 16, workstream ~PM), cell `IB-cw-3`.
<owned_cells>IB-cw-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBCW3-AC1, IBCW3-AC2, IBCW3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~459/IRPT_BCKEND.TO-IB-cw-3.who-reads-the-cottonwood-client-key-and-what-a-rekey-moves.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only search of the repository; nothing is deployed, written or fetched from AWS.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed and no AWS identity is used.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p259_cells.py IBCW3 dry-run at base on dell2 2026-10-19: AC1, AC2, AC3 FAIL (no findings). Positive control (control259.py) over synthetic git repos with a source file to cite: the clean findings, and a notes file holding a full sha256 and a ten-hex commit PASS; 22 AC1 negatives (a wrong firm, three readers, duplicate and malformed reader ids, an invalid kind, no REFRESH_COMPARE, no HMAC_LIST, no RUNNER, invalid keyed_on and rekey_effect, a wrong excerpt hash, a line out of range, a cited file absent, a short `what`, a missing census term, no files scanned, hits above scanned, hits below the cited files, a missing census, a missing release path, a wrong release-path hash, an AWS write), 5 AC2 negatives (a cli_ id, an acc_ id, a 12-digit run, an e-mail address, a 40-hex run) and 3 AC3 negatives (a file outside the paths, a write under data/, the findings not in the commit) each fail their own arm, 0 unexpected. NOT measured by me: whether each reader behaves as classified (the issuer re-reads the cited lines), the search itself, anything outside this repository (the portal submodule).
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~459`. Class LOCAL (a repository read in a worktree; it touches no client data and no AWS).
</preflight>
