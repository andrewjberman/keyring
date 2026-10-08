# AMGT_RESAPP task order -- `AMGT-cc-5` -- THE TWO BUILD-SIDE REPAIRS OF THE SCOPED FUNCTION: THE STALE GENERATED STAMP, AND THE READ GRANT ON THE COLLECTOR'S JOB-RECORD PREFIX (TEXT ONLY, NOTHING APPLIED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cc-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~312</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_E_NOTES.md) -- At CLOUD HEAD the build's own generated-prefixes gate exits 1 (the registry hash went stale after another project's registry edits), and the function has no read grant on the job-record prefix. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r79-312` (branch `wk-AMGT_RESAPP-312`, cut from the issuance commit with `--portal-ref d1b21c97`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r79-312`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-cc-5` (round 79, decomposition s.87)

The scoped research function is built by a script that first checks one generated file against the address builder. That
check fails today, so the next build would stop. Separately, the function is about to read a new folder of small records
(one per finished Seeking Alpha collection job) and its role has no read grant on that folder. You make both repairs IN TEXT
ONLY. You run no `terraform` command of any kind, no `safe-apply`, no `aws` command that writes, no build script
(`build-and-upload-scoped-amgt.sh` is NOT run), and you install and download nothing. Another order applies the grant.

Work from the repo root: `cd "$(git rev-parse --show-toplevel)"`. Every command below is run there.

Read first, whole: `infra/aws/terraform/harvest/gen_harvest_prefixes.py` and
`lib/research/api/tests/test_harvest_prefixes.py`. In `infra/aws/terraform/harvest/scoped-amgt-api.tf` read lines 94 to 120,
lines 184 to 190 (how the filing-attempt state prefix is granted: one list entry) and lines 256 to 332.

1. **The generator.** In `infra/aws/terraform/harvest/gen_harvest_prefixes.py`, function `compute()`, add ONE entry after the
   `BRIGHT_DATA_SERP_BRONZE_PREFIX` line:
   `"SEEKING_ALPHA_JOB_RECORD_STATE_PREFIX": _table_prefix("seeking-alpha", _SCOPE, "state", "job_record"),`
   Do not change `_SOURCES` (it already holds `seeking-alpha`), `scoped_registry_hash`, `main` or the two helper functions.
   Where the file's text says "the four constants" (the module docstring, the `scoped_registry_hash` docstring, and the header
   line inside `render`), write "the constants". Change nothing else in `render`.
2. **Regenerate. Never edit the generated file by hand.** Run
   `PYTHONPATH="$(pwd)" python infra/aws/terraform/harvest/gen_harvest_prefixes.py --write`
   then
   `PYTHONPATH="$(pwd)" python infra/aws/terraform/harvest/gen_harvest_prefixes.py --check; echo "exit=$?"`
   The second must print `OK:` and `exit=0`. Open `lib/research/api/_harvest_prefixes.py` and confirm: `REGISTRY_HASH`
   changed, the four old constants read exactly as before (`bloomberg/harvest/bronze/`, `bright-data/harvest/bronze/serp/`,
   `amgt/harvest/state/filing_attempt/`, `seeking-alpha/harvest/bronze/`), and the one new constant is there. If any of the
   four old values differs, STOP, change nothing further, and report it: that would move a served address.
3. **The test.** In `lib/research/api/tests/test_harvest_prefixes.py`, function `_fresh_constants`, add ONE entry after the
   `BRIGHT_DATA_SERP_BRONZE_PREFIX` line:
   `"SEEKING_ALPHA_JOB_RECORD_STATE_PREFIX": _table_root("seeking-alpha", "harvest", "state", "job_record"),`
   Where the file's docstring says "four constants", write "constants". Leave `test_ii_b` alone: its set of four SOURCES is
   still right. Run `PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests/test_harvest_prefixes.py -q -p no:cacheprovider`
   and see 6 passed.
4. **The grant.** Print the prefix from the generated file, do not compose it yourself:
   `PYTHONPATH="$(pwd)" python -c "from lib.research.api import _harvest_prefixes as h; print(h.SEEKING_ALPHA_JOB_RECORD_STATE_PREFIX)"`
   In `infra/aws/terraform/harvest/scoped-amgt-api.tf`, in the list `scoped_amgt_pool_prefixes`, add ONE entry as the LAST
   entry of the list, after the line `"issuer-site/harvest/silver/filing_source/",` and before the closing `]`: the printed
   value in double quotes followed by a comma, on its own line, indented four spaces like its neighbours. It ends in a slash.
   Above it write a comment of a few lines, each starting `#`, that says: AMGT_RESAPP round 79, cell AMGT-cc-5; the freshness
   view's reader of the Seeking Alpha collector's job records lists this prefix and then reads its objects; one entry grants
   both limbs because the list is read twice below; the spelling is the generated constant
   `SEEKING_ALPHA_JOB_RECORD_STATE_PREFIX`, which is the address builder's output; the trailing slash is mandatory; READ ONLY,
   the collector writes these records and this role never does; the grant is this table and not the whole state tier. Write
   the comment in plain ASCII and do not write the prefix itself inside the comment.
5. **Change nothing else in that file.** No new statement, no new variable, no new action, no edit to lines 322 or 330, no
   edit to any other list entry or comment. Do not edit `build-and-upload-scoped-amgt.sh`, any other `.tf`, anything under
   `infra/logic/registry/`, `lib/opal_naming.py`, or any file under `lib/` other than the two named above.
6. Run the three criteria below. Your report states: the old and new `REGISTRY_HASH`; the four old values, each "unchanged";
   the new constant's value; the line number of the new list entry; and that you ran no terraform, no apply, no build and no
   AWS write.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W312-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no build run, no store write, no vendor call, no download of any kind.
2. `upload_verified.sh`, `content_diff.py` and every `.tf` file in the folder are READ, never edited.
3. You run NO `terraform` command, no `safe-apply` and no AWS write: the apply is a leg of the redeploy order under its own pair.
4. No S3 address is typed: every prefix is the generator's output.
5. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
6. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
7. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/gen_harvest_prefixes.py
infra/aws/terraform/harvest/scoped-amgt-api.tf
lib/research/api/_harvest_prefixes.py
lib/research/api/tests/test_harvest_prefixes.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~312/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cc-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc5.py" --crit AC1; echo "exit=$?"</invocation><expect>the generator's own check exits 0, its test file passes whole (6 or more passed, 0 failed), the four prefix values of the cut are byte-equal to the cut, and the new job-record constant is in the generated module and in the generator and equals the address builder's output; G1-G5 PASS; R79 CC5 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cc-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc5.py" --crit AC2; echo "exit=$?"</invocation><expect>read as text with no terraform run, the prefix list is the cut's 33 entries in order plus exactly the builder's job-record prefix, the whole state tier is not granted, the one object-read expression and the one list-condition expression are the cut's, no action was added or removed, and no other code line changed; T0-T5 PASS; R79 CC5 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cc-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc5.py" --crit AC3; echo "exit=$?"</invocation><expect>from the base commit to HEAD and in the working tree, nothing under the harvest terraform folder or the generated files changed except the cell's four files; B0-B2 PASS; R79 CC5 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~312 <0.9.0_WK_AMGT_RESAPP~312@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~312/AMGT_RESAPP.TO-AMGT-cc-5.the-build-side-repairs.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO ruling msg 31672 term one (the grant); the stale gate was found by the issuer at the cut. Drafted in `deliverables/2.0.0_SA_COO~Z/round79/GROUP_E_NOTES.md` (cell E1), committed before the cut, in the issuance commit's ancestry. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>79</round>
<slot>0.9.0_WK_AMGT_RESAPP~312</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @646167b6df; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads SERVED: YES; the build's gate exits 0; 4 of 4 old prefix values equal; the list reads 34 entries; nothing applied: the grant is cc-7's leg</status>
