# TO NFRA_CTLPLN.TO-CT-ao-2 -- workstream OUTCOME round 18 (cell CT-ao-2): the absent-package arm, steps release, pack and Taildrop -- the one checked tabulate wheel is released on the CTO's signed check 8, packed, verified locally and sent to dell1 (FWD-15, FWD-16)

<to_id>NFRA_CTLPLN.TO-CT-ao-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~128</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ao-2` (`decompositions/NFRA_CTLPLN_DECOMP.round25.md`, amended) | **outcome_ref:** FWD-15, FWD-16 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

AMENDMENT 2 to round 25 (issuer, after the CTO signed check 8): the cell `CT-ao-1` ended with the wheel fetched and checks 1-7 passed. The CTO has now SIGNED check 8 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md`, @9aed0e1263; read it whole, including the risks it accepts). The dependency of this cell is met, so it is cut now. The batch is `intake-20261016-tabulate`; the single wheel is `tabulate-0.9.0-py3-none-any.whl` (sha256 `024ca478df22...`, 35,252 bytes), held at `C:/opal-intake/holding/intake-20261016-tabulate/`. The receiving box is dell1 (tailnet address 100.79.95.44, online at the cut); it receives the pack on a SCRATCH target and deletes the scratch (a later issuer call to dell1). Read first: `org/devices/intake/README.md` (hops 5 and 6), `.claude/skills/tdrop/SKILL.md` (the Taildrop recipe: stage files under `$HOME/tdrop/out/`, nothing sent by Taildrop is ever committed; add `.claude/skills/tdrop` to the sparse set if it is absent), and the earlier cell's record of the same steps for the duckdb batch, `org/devices/intake/records/intake-20261015-duckdb/TAILDROP_RECORD.md`, with its test `.tools/tests/test_round22_journey_record.py` (the `--release`, `--pack` and `--taildrop` flags are the shape).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. The CTO's check-8 file is under `org/tier1_exec/1.0.0_SA_CTO/deliverables/`: add that folder if it is absent.

### BUILD

1. **Release** the one file: `python org/devices/intake/intake_check.py release --batch intake-20261016-tabulate --file tabulate-0.9.0-py3-none-any.whl` (read `--help` and the tool first). It must read the CTO's signed check-8 file (the check record names it) and move the file to `C:/opal-intake/release/intake-20261016-tabulate/`; if it refuses, STOP and file a BLOCKING row with its printed refusal; do not edit the check-8 file or the check record by hand. Commit the updated records under `org/devices/intake/records/intake-20261016-tabulate/`.
2. **Pack**: `python org/devices/intake/intake_check.py pack --batch intake-20261016-tabulate --out "$HOME/tdrop/out/intake-20261016-tabulate" --released-only`. The folder must hold the wheel, its `.check.json`, its `.delivery.txt` and `MANIFEST.json` (4 files). Then verify the pack LOCALLY, read only: `AGENTBUS_DEVICE=laptop python org/devices/intake/intake_receive.py verify --from "$HOME/tdrop/out/intake-20261016-tabulate"` and keep its LAST line (`INTAKE-VERIFY pack=<dir> wheels=1 verified=1 checked=1 stray=0 ok=True` expected). Do not run `prove` or `install` on the laptop.
3. **Taildrop to dell1**, once: confirm dell1 is online (`tailscale status`), then `tailscale file cp <each of the 4 files> dell1:` (the trailing colon; one `tailscale file cp` per file or one call with all four). Record each command, its exit code and the time in `org/devices/intake/records/intake-20261016-tabulate/TAILDROP_RECORD.md` (ASCII; the SHA-256 of each file sent; no file content). Send EACH file at most once; never re-send on a re-run of the test. If any `tailscale file cp` fails, report the printed error and STOP (a partial delivery is dell1's to ignore; say which files went). A Taildrop has no read receipt: the delivery is proven by dell1's own `tailscale file get` and `verify`, which the issuer asks of dell1's CTO next; say so in the record.
4. Extend `.tools/tests/test_round25_journey_record.py` (merged at 5834b9f30e; keep its two flags) with `--release` printing `JOURNEY-RELEASE released=<n> check8=<SIGNED|OTHER> file=<name> sha256=<12 hex> ok=<True|False>` (read-only: the release folder holds exactly the one file, its bytes equal the fetch record's sha256, the check record shows check 8 passed and names the CTO's signed file), `--pack` printing `JOURNEY-PACK files=<n> manifest_ok=<True|False> verify=<the INTAKE-VERIFY last line> ok=<True|False>` (read-only: re-runs `verify` locally, never sends), and `--taildrop` printing `JOURNEY-TAILDROP files_sent=<n> failed=<f> target=dell1 ok=<True|False>` (reads ONLY `TAILDROP_RECORD.md`; it never calls Tailscale). Its existing `--check` flag already accepts the post-release state (check8 SIGNED and released) if you keep it state-aware as `test_round22_journey_record.py` does; keep it passing.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~128/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~127/NFRA_CTLPLN.TO-CT-ao-1.tabulate-fetch-and-checks-one-to-seven.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W128-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTao2-AC1" cell_refs="CT-ao-2"><invocation>python .tools/tests/test_round25_journey_record.py --release</invocation><expect>ok=True</expect></criterion>
`CTao2-AC1` -- the one checked wheel is released with check 8 signed and nothing else is in the release folder for this batch (base: the flag does not exist; the release folder does not hold the batch); report the whole line.

<criterion id="CTao2-AC2" cell_refs="CT-ao-2"><invocation>python .tools/tests/test_round25_journey_record.py --pack</invocation><expect>ok=True</expect></criterion>
`CTao2-AC2` -- the pack holds the 4 files and `verify` reads wheels=1 verified=1 checked=1 stray=0 ok=True (base: the flag does not exist); report the whole line.

<criterion id="CTao2-AC3" cell_refs="CT-ao-2"><invocation>python .tools/tests/test_round25_journey_record.py --taildrop</invocation><expect>ok=True</expect></criterion>
`CTao2-AC3` -- all four files were sent to dell1 by Taildrop, each exit code recorded (base: the flag does not exist); report the whole line and the record.
</proof_of_spec>

<expected_criteria>CTao2-AC1,CTao2-AC2,CTao2-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~128/NFRA_CTLPLN.TO-CT-ao-2.tabulate-release-pack-and-taildrop.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTao2-AC1,CTao2-AC2,CTao2-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round25.md</decomp_doc>
<owned_cells>CT-ao-2</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/records/intake-20261016-tabulate/
.tools/tests/test_round25_journey_record.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the Taildrop is a tailnet transfer of one file set to dell1; no credentials.
comp-adversary: RUN -- a second send of the same files (the test never calls Tailscale; each file at most once); a file other than the 4 sent (the pack folder is the only source; list it before sending); the release taking place without the CTO's signature (the tool must refuse; the test requires check8=SIGNED); the wheel executed or installed on the laptop (the cell runs verify only, never prove or install); the pack committed into a git tree (it lives under the user's tdrop folder, outside every tree); a Taildrop to the wrong device (the target is dell1: the trailing colon form, confirm in `tailscale status` first); BLIND: whether the files arrived (no read receipt; dell1's own `tailscale file get` and `verify` say), the install on dell1 is the issuer's later call, and the risks the CTO accepted in check 8 stand.
risk: SERVED -- a release record, a local pack and one file set sent to one box on the tailnet, nothing installed or run; reversible by dell1 deleting its Taildrop inbox. (The decomposition's first table said WORLD; the issuer's amendment sets SERVED as `CT-al-4` carried for the same acts.)
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/records/` and the intake tools are NFRA_CTLPLN's laptop-side intake route (C-INTAKE); the CTO signed check 8 (@9aed0e1263) and ruled the drive (round-24 analysis @6b8e48b0d5).
</preflight>

Base checks, dry-run by the issuer before the cut: CTao2-AC1, AC2 and AC3 FAIL as expected (the flags do not exist; nothing is released, packed or sent). Pre-state read by the issuer 2026-10-16 ~03:3xZ: the release folder holds only intake-20261008-a and intake-20261015-duckdb; `tailscale status` lists dell1 online.
Source: CTO round-24 analysis rulings 1 and 2 (`ledger/ROUND_ANALYSIS.round24.md` @6b8e48b0d5); check 8 @9aed0e1263; FWD-15, FWD-16.
