# AMGT_RESAPP round 78 -- TO-AMGT-bb-18 LEG 0, cell AMGT-bb-23: pyarrow and rpds-py come out of the deployed package

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

Serial: `0.7.0_AE_CloudOps~A` | Window: 2026-10-07 17:50Z -> 18:55Z (session start; prior log
`round77_ba20_code_redeploy_and_route_swap.md`) | Order:
`org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-bb-18.the-code-redeploy.md`
AMENDMENT 1 | Issuer: `2.0.0_SA_COO~Z` | risk WORLD, proof_genre DEPLOY

---

## Current State

**LEG 0 is complete and on CLOUD. Legs 1 and 2 are STAGED and blocked on the issuer.**

Andrew's word of 2026-10-07 is that no package may be fetched from the internet on this box. The
build of `opal-amgt-scoped-api` downloaded seven Python packages; five arrive as files and are
not this cell's concern. The other two, pyarrow 16.1.0 and rpds-py 2026.6.3, are now COPIED out
of the package the function is running now, under the CTO's ruling (msg 31206): the local zip's
sha256 must equal the live `CodeSha256` read at build time or the build stops, with no download
fallback, and the two packages in the new zip must equal the deployed zip's byte for byte.

Two files, both under `infra/aws/terraform/harvest/`:

1. **`vendor_from_deployed.py` (new, 137 lines).** Standard library only, ASCII, py39, with
   `from __future__ import annotations`. It imports `argparse`, `base64`, `hashlib`, `os`, `sys`,
   `zipfile` and nothing else -- no `urllib`, `http`, `socket`, `ssl`, `ftplib`, `subprocess`,
   `boto3`, `botocore`, `requests` or `pip` appears anywhere in the file, and that absence is the
   proof there is no second source. The sha256 comparison is the first act and the only way in;
   no option skips it. The dest folder is created ONLY after the sha gate, the empty-dest check,
   the four-folder check and the path-safety check have all passed, so every refusal leaves no
   folder behind that could be mistaken for a partial copy. The four folder names are typed WITH
   their versions, so a zip carrying `pyarrow-17.0.0.dist-info/` and no `pyarrow-16.1.0.dist-info/`
   is refused rather than served -- a version change goes back through intake.
2. **`build-and-upload-scoped-amgt.sh`,** the eight edits S1-S8 the amendment names and no line
   outside them. S1 inserts the zip requirement, the live-`CodeSha256` read and the helper call
   before any pip command (`set -e` makes a non-zero helper exit stop the build there). S3 cuts
   `PYARROW_PIN` and leaves `VENDOR_PINS` the five pure pins. S6 now refuses EVERY non-pure
   pip-downloaded wheel. S7 replaces the two-native-wheels demand with a walk of the filled folder
   that passes no file through `VENDOR_PRUNE` or any other filter, because filtering there would
   break the byte-for-byte equality the ruling requires.

Commits: cell `e01c130815` (authored in my own linked worktree per Rule 14b), drained to CLOUD as
`9e42b6cdb7` via `.tools/safe-merge.sh` (tree check: branch needed 2 files, dropped 0, foreign 0;
index check: 0 of 2 merged paths differ from HEAD). The worktree `C:/tmp/ae-a-bb23` and its branch
`ae-a-amgt-bb23` are removed and pruned.

**Push state, MEASURED at 18:52Z:** LOCAL. `origin CLOUD @a30d12d8fd` (`git ls-remote` read);
`9e42b6cdb7` is an ancestor of local CLOUD but not of `FETCH_HEAD`. This seat does not push shared
branches.

Two requirements of the PROTECTED range (lines 544-741, which the order forbids editing) depend on
this change and are graded by no criterion, so I measured them directly against the deployed copy:
the verify step's `native_ext` predicate (`rpds/` + `cpython-311-x86_64-linux-gnu`) is satisfied by
`rpds/rpds.cpython-311-x86_64-linux-gnu.so`, and of the eight `VENDORED_PACKAGES` members the two
compiled ones (`rpds/__init__.py`, `pyarrow/__init__.py`) come from the deployed copy while the
other six come from the five surviving pure pins. The full build still cannot be exercised here.

## Deployment Sequence + Verification (AE role addition)

**NO DEPLOY RAN. This cell applies nothing, builds nothing and writes no store** -- that is why
AMENDMENT 1 states it needs no never-widen pair and could begin at once. No NEVER-2 ledger entry
was opened, because there is no deploy to leave half-landed. Per the amendment's rules: the build
script was NOT run (with or without `--build-only`), no `pip download`, no `pip install`, no
`terraform`, no AWS write. `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/SITEZ_INSTALL_DOWNLOAD_LINE_CENSUS_20261007.md`
confirms the build script carries fetching lines at 135 and 560 (pre-edit numbering), which is
exactly why it did not run; `.tools/commit-gate.sh`'s only census hit is a COMMENT at line 46, and
`safe-commit.sh` / `safe-merge.sh` have no hits. The three check scripts made one
`lambda get-function-configuration` read each and no other AWS call.

Criteria were run TWICE: once in my worktree at `f8a61834fd`, then re-graded on the COMMITTED bytes
in the shared tree at CLOUD HEAD `9e42b6cdb7`, because a merge's self-report is not evidence that
the work landed. Both passes are identical. Actual output of the shared-tree re-grade:

```
AC4 -- r78_bb23.py --crit AC1
   deployed zip C:/tmp/ba20-r77-14a36147bd.zip: 41981131 bytes, sha256 MkM9Kf37nmI+thEmZR+ij8ybbxGrHxqtsonjyI7N5eg=; entries under the four folders 147 [132, 6, 4, 5]
PASS C1 the zip's sha256 equals the live CodeSha256 zip MkM9Kf37nmI+thEmZR+ij8ybbxGrHxqtsonjyI7N5eg= live MkM9Kf37nmI+thEmZR+ij8ybbxGrHxqtsonjyI7N5eg=
PASS C2 the helper exists and exits 0 rc=0 OK: 147 file(s) copied
PASS C3 the filled folder equals the zip's entries byte for byte 147 of 147 equal; mismatched 0, missing 0, extra 0 []
PASS C4 the per-folder counts are the measured ones filled [132, 6, 4, 5] zip [132, 6, 4, 5] measured [132, 6, 4, 5]; pyarrow 138 of 138, rpds 9 of 9
R78 BB23 AC1 SERVED: YES
exit=0

AC5 -- r78_bb23.py --crit AC2
PASS P0 the helper exits 0 on the right sha and copies the files rc=0 files 147
PASS N1 a wrong expected sha stops the helper and nothing is copied rc=1 files 0 ERROR: sha256 mismatch: ... reads MkM9Kf37... the expected value is pB32LZ9S...; nothing was copied
PASS N2 one changed byte inside a pyarrow member fails the sha gate byte 1560511 of the copy, inside pyarrow/__init__.py; copy sha256 fkdn26kQvDqPbF+0mruqSG2/sZO6CdvVVM9OTCkAgs4=; rc=1 files 0
PASS N3 the comparer reports the one flipped byte before the flip 147 of 147 equal, mismatched 0; after it 146 of 147 equal, mismatched ['pyarrow/libarrow.so.1601']
PASS N4 a zip whose pyarrow dist-info is another version is refused, its sha being right rc=1 files 0 ERROR: the zip ... holds no entry under pyarrow-16.1.0.dist-info/
R78 BB23 AC2 SERVED: YES
exit=0

AC6 -- r78_bb23.py --crit AC3
PASS C1 VENDOR_PINS expands to exactly the five pure pins 5 pin(s) ['attrs==26.1.0', 'jsonschema-specifications==2025.9.1', 'jsonschema==4.26.0', 'referencing==0.37.0', 'typing_extensions==4.16.0']; beyond the five []; of the five absent []
PASS C2 no pip download that names --platform names pyarrow or rpds pip download commands 2 at lines [154, 592]; with --platform 1; of those naming one of the two []
PASS C3 the script requires the zip, reads the live CodeSha256 and calls the helper before any pip download AMGT_DEPLOYED_ZIP required at line 134; CodeSha256 read at line 136; helper called at line 139 (MSYS2_ARG_CONV_EXCL on the call: True); first pip download at line 154
PASS C4 no other fetch route in the script or the helper fetch tokens in the script []; helper imports ['__future__', 'argparse', 'base64', 'hashlib', 'os', 'sys', 'zipfile'], network modules among them []
PASS C5 the script's prune list removes nothing from the deployed four folders VENDOR_PRUNE ('pyarrow/include/', 'pyarrow/src/', '/tests/', '/testing/'); removed 0 of 147 []
PASS C7 the packaging step is handed the filled folder and no longer demands two native wheels packaging step at line 168, handed $FROM_DEPLOYED: True; the two-native-wheels refusal still in the text: False
PASS C6 bash -n on the script exits 0 rc=0
R78 BB23 AC3 SERVED: YES
exit=0
```

Landed-bytes control, run instead of trusting the drain's own report: `git rev-parse HEAD:<path>`
equals `git rev-parse e01c130815:<path>` for BOTH files
(`cb41fea9cf9aa71fcee77d395d13a78ec65df5d3`, `c4313420ff894c6b19c738c138561618e749b9c3`), so the
bytes the criteria graded ARE the bytes at HEAD. A peer commit landed during the window and moved
local HEAD to `5133f144fb`; both blobs re-read UNCHANGED at that HEAD. The `merge-base --is-ancestor`
read was run with its reversed negative control, which refuses as it must.

**What this cell does NOT prove.** The full no-network build. The five pure wheels are not on this
machine, so the script cannot run to a zip; by the amendment's rule 1 it must not be tried. Term 2
of the ruling in its own words -- the two folders in the NEW ZIP equal the deployed zip's -- is read
at bb-18 on the zip the build makes, by `r78_bb23.py --compare-zip <built zip>`. AC4 proves the same
equality one step earlier, on the folder the packaging step reads.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-tool PATH rail | `org/XXX.md` A.3 census + forwarder exercise | PASS | 104 of 104 resolve bare; `comp-which` forwarder RAN |
| comp-pulse (pre-commit risk reflex) | ridden by `safe-commit.sh`, `diff days=7 top=8` | PASS | DENOMINATOR 2 files vs 1662 danger nodes; ANSWER STATE `PRESENT_WITH_ZERO_RESULTS`; REFLEX CLEAN, a measured result not a default |
| commit-gate | `bash .tools/commit-gate.sh` on each file | PASS | helper: py_compile + AST + ruff `--target-version py39 --extend-select FA` clean; script: `bash -n` + comp-shell scan 0 findings |
| surprise-row-gate | ridden by `safe-commit.sh` and `safe-merge.sh` (MERGED index) | PASS | 0 rows, denominator 2 dispatched paths, graded on the UNION |
| naming-gate | ridden by `safe-commit.sh` | PASS | denominator 1 path in domain, 0 graded, 0 unseen |
| to-pipeline-gate | ridden by both commits | PASS | no `task_orders/*.md` staged; merge commit exempt |
| audit-archive-invoker | `python .tools/audit-archive-invoker.py` | WARN | pre-existing, owned classes (see Blockers) |

**What worked.** Reading the ORACLE (`r78_bb23.py`, 438 lines) in full BEFORE writing either file,
then running the check's own parsers (`logical_lines`, `shell_vars`, `expand`, `PIP_DOWNLOAD`)
against the UNEDITED script to establish the base state. That turned three criteria into a
mechanical target: it told me in advance that C2 needs at least one surviving `--platform`
download, that C3 grades the ORDER of three line numbers against the first pip download, and that
C4's fetch-token census already read 0 at the base -- so I knew which of my edits could break it.
All three criteria passed first try as a result.

**What failed.** Two rail denials. A standalone `grep` segment in Bash is DENIED per CLAUDE.md Rule
21 and the denial ABORTS THE WHOLE CALL, so the later segments in that call became silent no-ops --
the first symptom was an empty result that looked like a true absence. Recovered by using the native
`Grep` tool and pipe-receiver greps. Second: the Bash tool resets CWD to the primary working
directory between calls, so every worktree command needed `cd` inside its own segment.

**Gap found.** `comp-blast` was NOT run on the infra change. The AE role minimum names it before
infra changes; my justification is that this commit applies nothing (no `.tf` edit, no apply, no
AWS write) and the two files are a build script plus a new helper that no deployed resource reads
until leg 1 builds a zip -- the `comp-pulse` reflex covered the committed diff instead. That
substitution is a judgment, not an equivalence, and it is named here rather than left implicit. The
real blast read belongs at leg 1, where an artifact actually moves. Second gap: `check-inbox` does
not resolve bare on PATH on this device although `org/XXX.md` step B and the `/watcher` skill both
spell it that way; `bash org/mcp/check-inbox.sh <serial>` works. Not filed as a surprise row -- it
is device PATH hygiene, outside this project's domain, and it misleads no AMGT_RESAPP consumer.

## MCP traffic

3 messages total. Inbound 2, both acked (30699, 31241): the 06:26Z relay of Andrew's word to wind
down site Z, SUPERSEDED by 31241, which records the 08:16Z reboot that brought the site back and
seats this lane on bb-18 LEG 0. Acting on the stale one would have ended the session instead of
starting it. Outbound 1: the LEG 0 completion report to `2.0.0_SA_COO~Z` (no ask). The CTO was not
copied -- Rule 31 reserves that for decisions.

## Files Modified

See commit messages: `e01c130815` (cell), `9e42b6cdb7` (drain). Both files under
`infra/aws/terraform/harvest/`; 196 insertions, 27 deletions across 2 files.

| File | Change |
|---|---|
| `vendor_from_deployed.py` | NEW. The sha-gated copy out of the deployed zip. Stdlib only, no network module. |
| `build-and-upload-scoped-amgt.sh` | Edits S1-S8 only. Protected range 544-741 untouched; `content_diff.py`, `upload_verified.sh`, `gen_harvest_prefixes.py`, every `.tf` and everything under `lib/` untouched. |

## Blockers

**Legs 1 and 2: BLOCKED on the issuer `2.0.0_SA_COO~Z`, evidence-cited.** The order's section 1
says "Begin only when the GO names the build commit and both halves are committed", and the ISSUER
GO block states legs 1 and 2 "stay STAGED: they wait on the six files by Taildrop and on the pair,
which also states `AMGT_DEPLOYED_ZIP`, `PIP_NO_INDEX=1`, `PIP_FIND_LINKS`, the `--compare-zip` read
of the built zip, the `dossier.py` change (51 values in 35 names, CTO msg 31204) and that the
then-deployed zip is KEPT on disk after the apply." None of those is this seat's to produce. Not
assumption-blocked: the GO text is the evidence.

**Not a blocker, surfaced without an owner claim:** `audit-archive-invoker.py` reports
`INTEGRITY/NON-APPEND-EDIT` on `org/mcp/agent-spawn-audit.log` (first divergence line 13871 col
363) plus five `INTEGRITY/ERROR-FAILCLOSED` baseline-missing rows and two
`COVERAGE/UNCOVERED-AUDIT-LOG` rows against the `2026-10-07T082230Z` archive. These are
pre-existing classes with an owner (`0.0.0_AB_MSTR~Z`'s audit surface), so per `org/XXX.md` I did
not re-file them; noted here only so the window's record is complete.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Issue the GO for legs 1 and 2 when the six files and the pair are ready.
   The GO must name the build commit EXACTLY (the order forbids "at or after"), fill
   `round78/checks/r78_deployed_cells.txt` and state its line count -- `r78_deployed.py` reads
   `NO CELLS LISTED` exit 2 while that file holds only its two comment lines, so bb-18 AC1 cannot
   pass until it is filled. The pair must also state `AMGT_DEPLOYED_ZIP`, since the build script now
   stops at once without it.
2. **[`0.7.0_AE_CloudOps~A`, this seat]** On the GO: open the ONE NEVER-2 entry, union the
   `.open_deploys/` of EVERY live worktree (`git worktree list --porcelain` then
   `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`) and measure the
   artifact before acting on any entry found -- that read is deliberately NOT pre-computed in this
   log, because the live worktree set changes (I removed one this window) and a stale denominator
   quoted at leg 1 would be worse than no read. Then the code leg, the snapshot event, bb-18
   AC1-AC3, `--compare-zip` on the built zip, and the `proof_of_spec.json` instance at
   `deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-bb-18.the-code-redeploy.proof_of_spec.json`
   reading VALID on committed bytes.
3. **[`0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z`]** `9e42b6cdb7` is LOCAL; it reaches origin on Andrew's
   word with the next trunk push. Nothing in this cell needs it pushed to be graded.
