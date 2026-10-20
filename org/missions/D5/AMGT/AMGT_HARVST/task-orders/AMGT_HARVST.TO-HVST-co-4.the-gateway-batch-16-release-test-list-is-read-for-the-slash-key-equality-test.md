# AMGT_HARVST task order -- `HVST-co-4` -- ROUND 100, workstream GATEWAY-TESTLIST: A READ-ONLY CELL READS WHETHER `tests/test_cj2_slash_key_one_form.py` IS IN THE TEST LIST OF SITE Z'S BATCH-16 GATEWAY RELEASE (ORDER `NFRA_OPLGTW.TO-OG-rl-17`, WINDOW 2026-10-21 06:00Z TO 06:45Z) -- THE CTO'S BINDING CONDITION (CTO round-99 analysis item 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-co-4.the-gateway-batch-16-release-test-list-is-read-for-the-slash-key-equality-test</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-co-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~188</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- NO AWS call at all. Your only reads are local git objects (`git show <ref>:<path>`, `git cat-file -e`), one `git ls-remote origin` (read-only), and local files of this worktree. NO write, NO network beyond that one `ls-remote`, NO edit of any source file, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a grep that reads zero because the pathspec was mangled by the shell (a `git show <ref>:<path>` with a slashed ref needs `MSYS_NO_PATHCONV=1`; run a POSITIVE control beside every absent verdict: the same read on a file that exists), a count taken on the wrong order (the batch-16 release order is `NFRA_OPLGTW.TO-OG-rl-17`, round 47, not `OG-ap-50`), a "named" read that matches a longer file name containing the test's name, a base tree read from the wrong ref (the base is the live gateway ref `13917ef993207bee6b8df0124eec5444da4d62cd`, branch `rel-nfra-oplgtw-batch15` at origin), and a verdict edited to match what the issuer expects.
</preflight>

## 0. THE CELL

The CTO ruled (cross-adjudication `org/critical_paths/cross_adjudication/20261019T1238Z_XA-20261018T094750Z-cbaa.md`) that the gateway keeps a ~20-line copy of the crosswalk slash-key rule and that **`infra/aws/ec2/opal-gateway/tests/test_cj2_slash_key_one_form.py` is in EVERY opal-gateway release's test list, whichever box releases**; a release that does not run it is not a release of that rule. Site Z's batch-16 release is order `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-rl-17.round-47-sixteenth-batched-release-the-client-fences-the-size-caps-and-the-in-flight-guard.md`, window 2026-10-21 06:00Z to 06:45Z; its release tree will be `C:/tmp/og-rel-batch16` on branch `rel-nfra-oplgtw-batch16` on site Z's host (not on this box). **Read whether the test is in that release's test list, from the order and from what exists in this repository, before the window.** Read only.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. Read first: the `rl-17` order (its "take list", its PHASE A test steps, "the seven new test files, the two edited, the existing admin, client, breakdown and window test files in BOTH orders using `.../deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh`; the full suite's failing set compared with the LIVE REF's") and its check scripts under `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/` and `.../r38/checks/_bothorders.sh`.
b. **Write `co4_batch16.sh`** (bash, Git Bash only) in your deliverables folder and run it once in the FOREGROUND, stdout to `co4_batch16.out`, printing in this order:
   1. `CONTROL-POSITIVE named_test=test_og_mg3 order_mentions=<n>` (the count of that name in the `rl-17` order text; expect at least 1) and `CONTROL-NEGATIVE named_test=test_zz_not_a_test order_mentions=0`.
   2. `B16-ORDER named_in_order=<yes|no> count=<n>` for `test_cj2_slash_key_one_form` in the `rl-17` order text; `B16-CHECKS named_in_checks=<yes|no> count=<n>` for the same name over the two check locations above (name each file searched on a `NOTE` line; native Grep or `grep` on those NAMED folders only).
   3. `B16-BASE in_base_tree=<yes|no> blob=<the blob id or none> base=13917ef993` from `MSYS_NO_PATHCONV=1 git cat-file -e 13917ef993:infra/aws/ec2/opal-gateway/tests/test_cj2_slash_key_one_form.py` and `git rev-parse 13917ef993:<that path>` (the object is in this box's store; if it is absent, say `in_base_tree=unread` and why).
   4. `B16-SUITE full_suite_run_stated=<yes|no>`: whether the `rl-17` order's Phase A states a full-suite run that would include every file of the release tree's `tests/` (quote the clause's line number on a `NOTE` line).
   5. `B16-REF release_branch_at_origin=<yes|no>` from `git ls-remote origin 'refs/heads/rel-nfra-oplgtw-batch16'` (an empty answer is `no`; print the ls-remote line count beside it).
   6. The last line, exactly: `CJ2-IN-BATCH16 named_in_order=<yes|no> named_in_checks=<yes|no> in_base_tree=<yes|no|unread> full_suite_run_stated=<yes|no> release_branch_at_origin=<yes|no> verdict=<IN|PARTIAL|ABSENT>` with the rule: `IN` if named in the order or the checks; `PARTIAL` if not named but in the base tree and a full-suite run is stated; `ABSENT` otherwise. Do not soften the verdict.
c. **If the verdict is not `IN`, file ONE surprise row (OBSERVATION)** naming what you read: the test is not NAMED in batch 16's test list (it would run only inside a full-suite comparison, if at all), so the CTO can send MSTR to MSTR before the window. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~188/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-co-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~188/co4_batch16.out</invocation><expect>(?ms)^CONTROL-POSITIVE named_test=test_og_mg3 order_mentions=[1-9]\d*$.*^CONTROL-NEGATIVE named_test=test_zz_not_a_test order_mentions=0$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-co-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~188/co4_batch16.out</invocation><expect>(?m)^CJ2-IN-BATCH16 named_in_order=(yes|no) named_in_checks=(yes|no) in_base_tree=(yes|no|unread) full_suite_run_stated=(yes|no) release_branch_at_origin=(yes|no) verdict=(IN|PARTIAL|ABSENT)$</expect></criterion>
</proof_of_spec>

- AC1 holds the controls (the finder sees a test the order names and does not see one it does not); AC2 is the finding (the verdict word is the finding). **If a line reads otherwise, DO NOT edit the expectation or the script to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-20 ~16:46Z):** both FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W188-S1`. The channel file has MIXED line endings and is append-only: READ ITS TAIL for the id sequence, append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body AND run the gate against your row WITHOUT the override first.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~188/AMGT_HARVST.TO-HVST-co-4.the-gateway-batch-16-release-test-list-is-read-for-the-slash-key-equality-test.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-co-4.the-gateway-batch-16-release-test-list-is-read-for-the-slash-key-equality-test` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-co-4.the-gateway-batch-16-release-test-list-is-read-for-the-slash-key-equality-test.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-99 analysis item 4 and his cj-2 binding condition (`XA-20261018T094750Z-cbaa`). Deadline: before the window, Wed 2026-10-21 06:00Z. What I have read already (not the worker's word, and to be re-read by it): the `rl-17` order text does not name `test_cj2_slash_key_one_form` (a native Grep of the NFRA_OPLGTW tree found it only in a surprise row about dell1's harvest paths); `rl-17` Phase A runs named test files and a full-suite failing-set comparison against the live ref; `origin` carries `rel-nfra-oplgtw-batch10`, `batch11` and `batch15`, no `batch16` at ~16:46Z.
- Chain D of round 100 (its own worker `~188`: no dependency on another chain; disjoint write set). Slot ~188, worktree `C:/dev/wk-harvst-188`, branch `wk-AMGT_HARVST-188`. **Sparse set at provision (each named file CHECKED BY NAME):** `.claude/agents`, `infra/aws/ec2/opal-gateway/tests`, `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders`, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks`, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks`. The base blob is read from the object store (`13917ef993` is present on this box; MSTR read it at 07:44Z).

- **COMPLETE (issuer, 2026-10-20 ~18:1xZ):** worker `~188`, branch merged `d8ab429992` (read and row `b9e3bcc3c1`, proof `b148c36cb4` VALID rc 0). THE FINDING: `CJ2-IN-BATCH16 named_in_order=no named_in_checks=no in_base_tree=yes full_suite_run_stated=yes release_branch_at_origin=no verdict=PARTIAL`: batch 16's order (`OG-rl-17`) names `test_cj2_slash_key_one_form` 0 times and none of its 89 check files names it; the test is in the base tree `13917ef993` (blob `2bcec39195223f106a76e64405a748ddebbe53e9`); Phase A states a comparison of the full suite's failing set against the live ref's; no `rel-nfra-oplgtw-batch16` ref at origin yet. READ BY ME: the order text (0 mentions of the test, 2 of the control `test_og_mg3`), the base blob id, the full-suite clause, and `git ls-remote` (0 lines). READING CAVEAT: the clause says the full suite's failing set is compared; it does not say each `tests/` file is named, so the test runs only if the suite collects it and shows only if it differs from the live ref. WHERE THE CTO READS IT: row `AMGT_HARVST-D1-W188-S1` (OBSERVATION, INERT) is the carrier, per the files-not-messages rule; no broker message sent. The release window is Wed 2026-10-21 06:00Z.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>100</round>
<workstream>GATEWAY-TESTLIST</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
