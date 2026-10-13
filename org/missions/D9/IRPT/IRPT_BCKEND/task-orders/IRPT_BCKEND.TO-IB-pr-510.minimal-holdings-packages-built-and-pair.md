# TO IRPT_BCKEND.TO-IB-pr-510 -- the host-bundle pair: ONE minimal holdings package per firm (live bytes plus only the two merged changes), BUILT, censused, scratch-installed, with its never-widen packet (CTO round-177 analysis section 2 item 1; RE 6858 and 6859)

<to_id>IRPT_BCKEND.TO-IB-pr-510</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~362</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>177</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-177 ANALYSIS (msg 6863) section 2 item 1, the CTO's RE 6859 and the issuer's row D2-S131 | **Decomp cell:** `IB-pr-510` (decomposition section 169) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-510` (inlined):** the 49 Financial and Inflection builders run on the runner host from per-firm packages (`investor-reporting-holdings.tar.gz`; keys in `deliverables/0.9.0_WK_IRPT_BCKEND~361/IB176-1_holdings_packages_census.json`: `49financial`, `inflection`, `cottonwood`, 45 members each). Round 176 showed the live packages are NOT HEAD (25 of 45 members differ in each; they were built from other trees). The CTO's rule (RE 6859): **one minimal package per firm: the live package's members by hash, plus only the temp-file fix and the `account_id` builder member(s)** (49F gets both; a firm whose builder does not need `account_id` gets the temp-file fix only if it carries that code path, else nothing). The pair prints each package's member diff against live (exactly those members) and a scratch-install read. Rollback per firm: the live object version. **BUILD ONLY: nothing is uploaded, applied, deployed or invoked; no AWS write; no host start.** The apply comes later, by an order to `0.7.0_AE_CloudOps~IB2`, at the host's next SCHEDULED Online, once the pair is signed.

**The three allowed changes (all already merged on this branch; a member is built as LIVE BYTES with these commits' hunks applied, NEVER as the HEAD bytes):**
- `135fc3509e` (the 49F builder's temp-file fix): hunks in `data/assets/scripts/gold/investor_reporting/holdings_49f.py` and `.../holdings_snapshot.py` (`retained_capture` and its caller);
- `7ace854890` (the builder's `account_id`): hunks in `holdings_49f.py`, `holdings_snapshot.py` and the schema copy `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`;
- `aa5778d962` (the Inflection builder's temp-file fix): the hunk in `.../holdings_inf.py`.
Everything else in a package stays at today's live bytes: in particular `rebalancer_schemas.py` (HEAD's imports `opal_strategy_matcher`, which the live packages do not carry), `lib/opal_naming.py`, the registries, and the four members the census flagged `unattributed` (`49financial`: `infra/logic/registry/reporting_policies.json` and `infra/logic/registry/resources.json`; `inflection` and `cottonwood`: `infra/logic/registry/resources.json`), which the pair carries UNCHANGED and names by path and sha256. `holdings_snapshot.py` at HEAD differs from live by FOUR other commits (`69679b90e3`, `3a5e564561`, `e2021e6a5d`, `6c962b0a52`) whose hunks must NOT be in the candidate.

**Build (work in your worktree; scratch OUTSIDE the repository, `C:/dev/_scratch362/`, deleted file by file at the end with a short bounded script):**
1. **The plan per firm, first.** For each firm in `holdings_snapshot.BUILDERS`, read which builder it runs and decide, from the code (cite file and line), which of the three changes its package needs: the temp-file fix iff its builder reaches `retained_capture` (49F's Tax snapshot, Inflection's Eclipse capture), `account_id` iff its builder is 49F's. Because `holdings_snapshot.py` is one shared module, a firm that needs either change in it receives that module's hunks of THAT change only. Write the plan into the record (`plan`) before you build; if a firm needs a change that would drag in a hunk of a fifth commit, STOP and file a row.
2. **Per member: live bytes plus the allowed hunks.** Download each firm's live package to scratch (read only), extract it, and for each member to replace apply the allowed commits' diffs for that path onto the LIVE bytes (`git diff <commit>^ <commit> -- <path>` applied with `git apply --3way`/`patch` to a copy of the live member; if a hunk does not apply cleanly, say which). Store, for each replaced member, the live bytes and the candidate bytes as files in YOUR folder: `deliverables/0.9.0_WK_IRPT_BCKEND~362/live/<firm>/<name>` and `.../candidate/<firm>/<name>` (code only, no client data). Rebuild the package deterministically (sorted members, fixed mtime and owner, `SHA256SUMS` regenerated for the replaced members only and checked with `sha256sum -c`). Pack TWICE to byte-identical output; record `candidate_package_sha256`. Upload nothing.
3. **The member diff against live** per firm: `member_diff_vs_live` = `{"changed":[names of the replaced members plus "SHA256SUMS"],"unchanged_count":N,"total":45}`; every other member's sha256 equals live (say so with the count).
4. **Scratch install.** Extract each candidate package to a fresh scratch directory; run `sha256sum -c SHA256SUMS` (record `OK` only if it passes for every member); `python -I -c "import holdings_snapshot, holdings_49f, holdings_inf"` from that directory with its own paths first (record `import_ok`); and run the issuer's seam probe against the EXTRACTED modules for the 49F package: with a stub S3, a build that raises and a build that returns leave NO new `-taxsma_workbook_projected_snapshot.json` file in the temp folder, and a file named by the operator's env var survives (you may copy the probe from `deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py` `probe_builder()`; point its import at the extracted package). Record `temp_file_probe` `{"raise_leaves":0,"return_leaves":0,"operator_file_kept":true}`.
5. **The packet** `deliverables/0.9.0_WK_IRPT_BCKEND~362/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-510.md`, in IB-pr-482's form (read `deliverables/0.9.0_WK_IRPT_BCKEND~337/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-482.md` and `.../~348/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-498.md`): the change in words per firm (what the host will run differently: the temp file is removed; `account_id` is written on 49F ACCOUNT nodes, which the serving function passes through (round 173) and the builder validates (round 174); no figure moves); the live and candidate package sha256 per firm; the member diff; **Branch A** (apply: at the host's next SCHEDULED Online, no seat starts the host for it; `aws s3 cp` of each candidate to its key with the live object's VersionId named and re-read before the write) and **Branch B** (restore the live object version per firm, named, with the rollback per key); the order of the act (the three firms, one at a time, each read back by its ETag and sha256); the **first read after the apply**: the leftover temp-file count on the host (counts only; a person deletes any found); the four unchanged members named by path and sha256; the pair: `2.0.0_SA_COO~P2`'s COO half (write it, unsigned) and the CTO half. State the apply as gated by the host's next scheduled Online.
6. **The record** `deliverables/0.9.0_WK_IRPT_BCKEND~362/IB177-1_candidate_packages.json`:
`{"plan":{"<firm>":{"builder":"...","needs":["temp_file_fix","account_id_builder"],"cited":[{"file":"...","line":N,"quote":"..."}]}},"packages":[{"firm_id":"...","live_key":"...","live_etag":"...","live_object_sha256":"...","rollback_version_id":"<the live object's S3 VersionId>","candidate_package_sha256":"...","built_twice_identical":true,"members_replaced":[{"name":"...","repo_path":"...","live_member_sha256":"...","candidate_member_sha256":"...","commits_applied":["135fc3509e"],"live_file":"deliverables/.../live/<firm>/<name>","candidate_file":"deliverables/.../candidate/<firm>/<name>"}],"member_diff_vs_live":{"changed":[...],"unchanged_count":N,"total":45},"unchanged_named":[{"repo_path":"...","sha256":"..."}]}],"scratch_install":{"sha256sum_c":"OK","import_ok":true,"temp_file_probe":{"raise_leaves":0,"return_leaves":0,"operator_file_kept":true}},"packet":"deliverables/0.9.0_WK_IRPT_BCKEND~362/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-510.md","aws_writes_made":0,"objects_uploaded":0,"functions_invoked":0,"ssm_commands_sent":0,"hosts_started":0,"accounts_written":0,"figures_written":0}`.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB177-1-AC1" cell_refs="IB-pr-510"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r177/p177_cells.py" . IB177-1-AC1</invocation><expect>IB177-1-AC1 PASS</expect></criterion>
<criterion id="IB177-1-AC2" cell_refs="IB-pr-510"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r177/p177_cells.py" . IB177-1-AC2</invocation><expect>IB177-1-AC2 PASS</expect></criterion>
<criterion id="IB177-1-AC3" cell_refs="IB-pr-510"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r177/p177_cells.py" . IB177-1-AC3</invocation><expect>IB177-1-AC3 PASS</expect></criterion>

<expected_criteria>IB177-1-AC1, IB177-1-AC2, IB177-1-AC3</expected_criteria>

What the checks grade: AC1 one package per `BUILDERS` firm; replaced members inside the allowed set (`holdings_49f.py`, `holdings_inf.py`, `holdings_snapshot.py`, the schema copy); the member diff `changed` list equals the replaced members plus `SHA256SUMS`; `total` 45; 49financial replaces `holdings_49f.py`, `holdings_snapshot.py` and the schema copy; AC2 for each replaced member `commits_applied` is a non-empty subset of `135fc3509e`, `7ace854890`, `aa5778d962`, the stored live and candidate files hash to the recorded sha256 and differ, and EVERY line the candidate changes against the live file is a line one of those commits changed in that path (so a hunk of any other commit fails it); AC3 `scratch_install` `sha256sum_c` OK, `import_ok` true, the probe reads 0 / 0 / kept, the seven bound counters read 0, the packet exists and carries Branch A, Branch B, the COO half, the CTO half, the rollback, the scheduled-Online gate and the unchanged members (`reporting_policies.json`, `resources.json`), and each package names its `rollback_version_id`. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory. Allowed AWS calls (READ ONLY): `s3api head-object` / `s3 cp` of each firm's package to scratch, `s3api list-object-versions` for the live object's VersionId. No upload, no copy to any bucket, no SSM command, no host start or stop, no deploy, no Lambda invoke, no vendor call; `.tools/aws` from the worktree root only.
- **Refusal clause:** STOP, file a row, change nothing more, if a candidate member would carry a line from any commit outside the three, if an allowed hunk does not apply to the live bytes (say which and why), if a package cannot be built byte-identical twice, if `sha256sum -c` fails on a candidate, or if the live object's VersionId cannot be read. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W362-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition with `.tools/safe-commit.sh`; ASCII only. Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~362/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-510.minimal-holdings-packages-built-and-pair.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 169 (round 177, workstream ~P), cell `IB-pr-510`.
<owned_cells>IB-pr-510</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB177-1-AC1, IB177-1-AC2, IB177-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~362/IRPT_BCKEND.TO-IB-pr-510.minimal-holdings-packages-built-and-pair.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- BUILD ONLY: the order builds three candidate packages in scratch from the three live objects and reads them; nothing is uploaded, applied or deployed. The consumers of the packages are the runner host's holdings refresh (refresh_dispatch.py:65 and :75) and nothing else; the apply is a later order under the signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; read calls only under the session's existing principal.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched and the host is not started.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p177_cells.py dry-run at base on dell2 2026-10-13 ~08:1xZ: IB177-1 AC1, AC2, AC3 FAIL (no record). Positive control: a synthetic record replacing holdings_49f.py with the blob at 135fc3509e against the blob at its parent passes AC2 with the commit declared (the hunk-subset test re-derives from git).
lane: the paths block IS the grant; worker slot ~362 of IRPT_BCKEND. Class WORLD (the `infra/`-adjacent host package; build only).
</preflight>
