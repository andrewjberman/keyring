# AMGT_RESAPP task order -- `AMGT-bb-20` -- THE LINE-ENDING CELL: NINE FILES RE-COMMITTED WITH UNIX LINE ENDINGS (ROW Z-S362)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-20</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~304</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_D_NOTES.md) -- 45 tracked files carry CR in the index under eol=lf; 34 of 41 .py fail the commit gate as they stand; 7 sit under infra/aws/lambda/; 9 are landable. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-304` (branch `wk-AMGT_RESAPP-304`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-304`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-20` (round 78, decomposition s.86)

Nine tracked files carry Windows line endings in git while their own attribute says they must carry Unix ones, so `git status`
calls them modified or clean depending on a cache, not on their content. Re-commit those nine with Unix line endings, and
change nothing else.

The nine are listed, one per line, in
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/HYGIENE_LANDABLE_FILES_20261007.txt`. Read it; it is your
whole write set under `data/` and `infra/`.

1. For each listed file, make the committed bytes equal the bytes at the base with every carriage return removed, and nothing
   else: `git add --renormalize -- <file>` does this for a file whose attribute says `eol=lf`. Check with `git ls-files --eol
   -- <file>` that it then reads `i/lf`.
2. Commit the nine in ONE commit through `.tools/safe-commit.sh` (the commit gate runs on the `.py` files; each of the six
   `.py` passed it at the cut).
3. **Touch no other file under `data/smartx/` or `infra/aws/`.** 36 more files have the same defect and are NOT yours: 34 fail
   the commit gate as they stand, and every file under `infra/aws/lambda/` is a function's source, whose package would change
   at its next deploy. If `git status` shows any of them modified after your commit, leave them and say so.
4. **Apply nothing.** No `terraform` command, no deploy, no upload. The three `.tf` files change only their line endings.
5. Print in your report: the nine files with `i/lf`, and the count still reading `i/crlf` under `eol=lf` in the whole
   repository (expected 36), from one `git ls-files --eol` pass.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W304-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no `terraform` command, no upload, no store write, no vendor call.
2. A line-ending change and nothing else: no file's content changes once carriage returns are set aside.
3. No file under `infra/aws/lambda/` is touched. No gate override of any kind.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
data/smartx/scripts/check_packages.py
data/smartx/scripts/lambda_smartx_query.py
infra/aws/connection_pool/__init__.py
infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/check_packages.py
infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/lambda_smartx_query.py
infra/aws/scripts/create_causality_v2_tables.py
infra/aws/terraform/nfra-agentbus-alyssa01/iam.tf
infra/aws/terraform/nfra-agentbus-alyssa01/main.tf
infra/aws/terraform/seeking-alpha/main.tf
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~304/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-20"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb20.py" --crit AC1; echo "exit=$?"</invocation><expect>the list holds 9 files and none is a Lambda source; every listed file reads i/lf in the index (9 of 9); C0-C1 PASS; R78 BB20 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-20"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb20.py" --crit AC2; echo "exit=$?"</invocation><expect>with carriage returns removed, every listed file equals its bytes at the base (9 of 9); R78 BB20 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-20"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb20.py" --crit AC3; echo "exit=$?"</invocation><expect>nothing else under data/smartx or infra/aws changed since the base; R78 BB20 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~304 <0.9.0_WK_AMGT_RESAPP~304@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~304/AMGT_RESAPP.TO-AMGT-bb-20.nine-files-recommitted-with-lf-endings.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO rulings file @f97be3fd6f (C1). Row Z-S362 stays OPEN: the drain prints the landed list beside 45. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_D_NOTES.md` (cell D3), committed in the issuance commit's parent. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~304</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
