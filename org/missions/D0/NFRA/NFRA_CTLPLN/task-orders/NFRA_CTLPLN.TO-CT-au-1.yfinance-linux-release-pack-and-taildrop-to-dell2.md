# TO NFRA_CTLPLN.TO-CT-au-1 -- workstream OUTCOME round 23 (cell CT-au-1): the organic journey, step 4 -- the 17 checked yfinance-closure wheels are released on the CTO's signed check 8, packed, verified locally and sent to dell2 by Taildrop (FWD-15, FWD-16)

<to_id>NFRA_CTLPLN.TO-CT-au-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~133</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-au-1` (`decompositions/NFRA_CTLPLN_DECOMP.round27.md`, amendment 4) | **outcome_ref:** FWD-15, FWD-16 |
**depends_on:** CT-at-1 (complete, merge e0b9a21bc0)

---

## WORKER FACE

### THE CELL

The organic journey of dell2's `yfinance==1.2.0` Linux closure (call `XB-20261016T052534Z-983c`). Done: the closure, the exact file names, dell2's CTO's approval of the 17 (recorded in git at `f6871291ff`), the 17 wheels fetched and held at `C:/opal-intake/holding/intake-20261016-yfinance-linux/` with checks 1-7 recorded (`org/devices/intake/records/intake-20261016-yfinance-linux/`, merge `e0b9a21bc0`), and the laptop CTO's check 8 SIGNED for the batch of 17 files (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md` @4c20c2bb3c: read it whole, including what he accepts). THIS cell releases the 17, packs them, verifies the pack locally and sends it to dell2 by Taildrop. The receiving side is dell2's: its manager `0.0.0_AB_MSTR~DELL2` collects into its own folder (`C:/opal-intake/inbound/yfinance-linux-cp312/`, outside every git tree); the install on the host is dell2's own act under its own order. The laptop uploads NOTHING to S3 or any AWS location. Read first: `org/devices/intake/README.md` (hops 5 and 6), `.claude/skills/tdrop/SKILL.md` (stage files under `$HOME/tdrop/out/`; nothing sent by Taildrop is ever committed except the record of what was sent), the shape of the last time this was done (`org/devices/intake/records/intake-20261016-tabulate/TAILDROP_RECORD.md` and `.tools/tests/test_round25_journey_record.py` `--release`, `--pack`, `--taildrop`), and `.tools/tests/test_round27_yfinance_batch.py` (its `--fetch`, `--check` and `--requires` are the batch test you extend).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. `org/tier1_exec/1.0.0_SA_CTO/deliverables` (the CTO's check-8 file) and `.claude/skills/tdrop` are outside that set: add them.

### BUILD

1. **Release** the 17 files, one at a time: `python org/devices/intake/intake_check.py release --batch intake-20261016-yfinance-linux --file <file_name>` (read `--help` and the tool first). It must read the CTO's signed check-8 file and move the file to `C:/opal-intake/release/intake-20261016-yfinance-linux/`. **The issuer read all 17 check records: each reads check 8 `awaiting` with `path: None`, because the checks ran before the signature existed (the same happened to the tabulate batch).** So for EVERY file, FIRST re-run `python org/devices/intake/intake_check.py check --batch intake-20261016-yfinance-linux --file <file_name> --approved-by C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md --signed-by org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md` (under `timeout 280`; the tool, not you, then records check 8 from the signed file; the main-tree absolute path of the approval file is used because your worktree may hold an older copy), THEN `release`. The re-run repeats checks 1-7 on the file as it sits on disk: if any of checks 1-7 reads differently from the earlier record (a verdict or its evidence), that is a FINDING: STOP and report it before releasing that file. Say in your report that all 17 needed the re-run, or which did not. If it refuses for any other reason, STOP and file a BLOCKING row with the printed refusal: do not edit the check-8 file or any check record by hand. Commit the updated records after each 5 files and at the end.
2. **Pack:** `python org/devices/intake/intake_check.py pack --batch intake-20261016-yfinance-linux --out "$HOME/tdrop/out/intake-20261016-yfinance-linux" --released-only`. The folder must hold, for each of the 17 wheels, the wheel, its `.check.json` and its `.delivery.txt`, plus `MANIFEST.json`: 52 files. Then verify the pack LOCALLY, read only: `AGENTBUS_DEVICE=laptop python org/devices/intake/intake_receive.py verify --from "$HOME/tdrop/out/intake-20261016-yfinance-linux"` and keep its LAST line (`INTAKE-VERIFY pack=<dir> wheels=17 verified=17 checked=17 stray=0 ok=True` expected). Do NOT run `prove` or `install` on the laptop (these are Linux wheels: `install` would refuse, and nothing is installed here).
3. **Taildrop to dell2**, once each: confirm dell2 is online (`tailscale status`), list the 52 files, then send them with `tailscale file cp <files...> dell2:` (the trailing colon) in calls of at most 13 files, so 4 calls; record each call's file list, exit code and UTC time. Write `org/devices/intake/records/intake-20261016-yfinance-linux/TAILDROP_RECORD_DELL2.md` (ASCII; the name, bytes and SHA-256 of every file, written BEFORE the sends, then each call's command, exit code and time after it; no file content). Send EACH file at most once; never re-send on a re-run of the test. If a call fails, report the printed error and STOP (a partial delivery is dell2's to ignore; say which files went). Say in the record that a Taildrop has no read receipt and that the Windows client may save a delivery to the receiving user's Downloads before `tailscale file get` runs (site Z's case): delivery is proven only by dell2's own record of each file's name, size and sha256, which dell2's manager reads.
4. Extend `.tools/tests/test_round27_yfinance_batch.py` (keep `--fetch`, `--check`, `--requires` and their output; their post-release states stay ok: `--fetch` and `--check` read the files in the release folder after the move, as the round-25 test does) with `--release` printing `BATCH-RELEASE released=<n> check8=<SIGNED|OTHER> names_equal=<True|False> sha_equal=<True|False> ok=<True|False>` (read-only: the release folder holds exactly the 17 files, their bytes equal the fetch records' SHA-256, every check record shows check 8 passed and names the CTO's signed file, and the holding folder holds none of them), `--pack` printing `BATCH-PACK files=<n> manifest_ok=<True|False> verify=<the INTAKE-VERIFY last line> ok=<True|False>` (read-only: re-runs `verify` locally, never sends) and `--taildrop` printing `BATCH-TAILDROP files_sent=<n> failed=<f> target=dell2 ok=<True|False>` (reads ONLY `TAILDROP_RECORD_DELL2.md` and the pack folder's hashes; it never calls Tailscale; ok: 52 files each in exactly one call with exit code 0, every command targets `dell2:`, the SHA-256 values equal the pack files on disk). Give `--taildrop` two mutant cases (a call with a nonzero exit code; a call naming another device) that must read `held=True`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~133/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. NO request to the package index or any outside host: the only network act is the Taildrop. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~132/NFRA_CTLPLN.TO-CT-at-1.yfinance-linux-fetch-and-checks-one-to-seven.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W133-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. Report: the `verify` last line, each Taildrop call with its exit code and time, how many files needed a `check` re-run before `release`, and the SHA-256 and size of each of the 17 wheels as the release folder holds them.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTau1-AC1" cell_refs="CT-au-1"><invocation>python .tools/tests/test_round27_yfinance_batch.py --release</invocation><expect>ok=True</expect></criterion>
`CTau1-AC1` -- the 17 checked wheels are released with check 8 signed and nothing else is in the release folder for this batch (base: the flag does not exist; the release folder does not hold the batch); report the whole line.

<criterion id="CTau1-AC2" cell_refs="CT-au-1"><invocation>python .tools/tests/test_round27_yfinance_batch.py --pack</invocation><expect>ok=True</expect></criterion>
`CTau1-AC2` -- the pack holds the 52 files and `verify` reads wheels=17 verified=17 checked=17 stray=0 ok=True (base: the flag does not exist); report the whole line.

<criterion id="CTau1-AC3" cell_refs="CT-au-1"><invocation>python .tools/tests/test_round27_yfinance_batch.py --taildrop</invocation><expect>ok=True</expect></criterion>
`CTau1-AC3` -- all 52 files were sent to dell2 by Taildrop, each exit code recorded (base: the flag does not exist); report the whole line and the record.
</proof_of_spec>

<expected_criteria>CTau1-AC1,CTau1-AC2,CTau1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~133/NFRA_CTLPLN.TO-CT-au-1.yfinance-linux-release-pack-and-taildrop-to-dell2.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTau1-AC1,CTau1-AC2,CTau1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round27.md</decomp_doc>
<owned_cells>CT-au-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/records/intake-20261016-yfinance-linux/
.tools/tests/test_round27_yfinance_batch.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the Taildrop is a tailnet transfer of one file set to dell2; no credentials; nothing is uploaded to S3.
comp-adversary: RUN -- a second send of the same files (the test never calls Tailscale; each file at most once); a file other than the 52 sent (the pack folder is the only source; list it before sending); the release taking place without the CTO's signature (the tool must refuse; the test requires check8=SIGNED); a wheel executed or installed on the laptop (the cell runs verify only, never prove or install; these are Linux wheels); the pack committed into a git tree (it lives under the user's tdrop folder, outside every tree); a Taildrop to the wrong device (the target is dell2: the trailing colon form, confirm in `tailscale status` first; dell1, site Z and the tabulate pack are NOT part of this send); a check-8 file edited to make a release pass (forbidden by the face); the Windows client auto-saving a delivery to the receiving user's Downloads (site Z's case, recorded in the face); BLIND: whether the files arrived (no read receipt; dell2's manager reads each file's name, size and sha256), the install on the host (dell2's own order), and the risks the CTO accepted in check 8 stand.
risk: SERVED -- a release record, a local pack of 52 files (about 39 MB) and one file set sent to one box on the tailnet, nothing installed or run; reversible by dell2 deleting its Taildrop inbox.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/records/` and the intake tools are NFRA_CTLPLN's laptop-side intake route (C-INTAKE); the CTO signed check 8 (@4c20c2bb3c) and ruled the delivery's end (XB-983c ruling @5740f0d341 term 4).
</preflight>

Base checks, dry-run by the issuer before the cut: CTau1-AC1, AC2 and AC3 FAIL as expected (the flags do not exist; nothing is released, packed or sent). Gate dry-run by the issuer: the CTO's check-8 file exists at the path every check record names; `tailscale status` lists dell2 online; the holding folder holds 17 files and the release folder none of this batch.
Source: CTO check 8 @4c20c2bb3c (msg 109644); CTO ruling @5740f0d341 term 4; MSTR msg 109615 (dell2's collector); FWD-15, FWD-16.
