# TO NFRA_CTLPLN.TO-CT-al-4 -- workstream OUTCOME round 14 (cell CT-al-4): the package journey, steps release, pack and taildrop -- the one checked duckdb wheel is released, packed and sent to dell1 by Taildrop; the install on dell1 is dell1's (FWD-15/16/18/19)

<to_id>NFRA_CTLPLN.TO-CT-al-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~122</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the main tree after the merge 8d757213ea (worker wk-NFRA_CTLPLN-122 @0929dc56fb): JOURNEY-RELEASE released=1 check8=SIGNED file=duckdb-1.5.0-cp314-cp314-win_amd64.whl sha256=11ae50aaeda2 ok=True; JOURNEY-PACK files=4 manifest_ok=True verify=INTAKE-VERIFY ... wheels=1 verified=1 checked=1 stray=0 ok=True; JOURNEY-TAILDROP files_sent=4 failed=0 target=dell1 ok=True (the record of 2026-10-15T20:24:27Z to 20:24:28Z; the issuer did not re-send); proof VALID. The earlier order CT-al-1's flags stayed reproducible after the release because the issuer ruled them state-aware (rows W122-S4, S5): --fetch now reads ok=True where=release, --check reads check8=SIGNED released=True ok=True, and CT-al-1's proof is VALID again in the main tree. The release needed the checks re-run with the CTO's signed file because the 19:28 check record named no signature (W122-S1); the tool decided what was re-recorded, nothing was edited by hand. DELIVERY TO dell1 IS NOT PROVEN by this order: a Taildrop has no read receipt. The issuer's call XB-20261015T204024Z-7bc4 to 1.0.0_SA_CTO~DELL1 (tailscale file get, verify, prove, install --target, the lane's read) is the proof.</status_reason>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-al-4` (`decompositions/NFRA_CTLPLN_DECOMP.round22.md`) | **outcome_ref:** FWD-15, FWD-16, FWD-18, FWD-19 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

AMENDMENT 1 to round 22 (issuer, after the CTO signed check 8): the cell `CT-al-1` ended with the wheel fetched and checks 1-7 passed. The CTO has now SIGNED check 8 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_DUCKDB_20261015.md`, @051808678b: 'release, pack and taildrop may proceed for this one file'; read it whole, including the risks it accepts). The dependency of this cell is met, so it is cut now. The batch is `intake-20261015-duckdb`; the single wheel is `duckdb-1.5.0-cp314-cp314-win_amd64.whl` (sha256 `11ae50aaeda2...`, 13,575,130 bytes), held at `C:/opal-intake/holding/intake-20261015-duckdb/`. The receiving box is dell1 (tailnet address 100.79.95.44, online), for lane `2.0.0_SA_COO~D1`; the install and the lane's read are dell1's and come after the delivery. Read first: `org/devices/intake/README.md` (hops 5 and 6), `.claude/skills/tdrop/SKILL.md` (the Taildrop recipe: stage files under `$HOME/tdrop/out/`, nothing sent by Taildrop is ever committed), `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~8/INTAKE_RECEIVE_COMMANDS.md` (what dell1 will run on the pack), and the earlier delivery record `org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-v-3.receive.txt` (how the click wheel travelled).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **Release** the one file: `python org/devices/intake/intake_check.py release --batch intake-20261015-duckdb --file duckdb-1.5.0-cp314-cp314-win_amd64.whl` (read `--help` and the tool first). It must read the CTO's signed check-8 file (the check record names it) and move the file to `C:/opal-intake/release/intake-20261015-duckdb/`; if it refuses, STOP and file a BLOCKING row with its printed refusal; do not edit the check-8 file or the check record by hand. Re-run the checks only if the tool says it must (then the tool, not you, decides what is re-recorded). Commit the updated records under `org/devices/intake/records/intake-20261015-duckdb/`.
2. **Pack**: `python org/devices/intake/intake_check.py pack --batch intake-20261015-duckdb --out "$HOME/tdrop/out/intake-20261015-duckdb" --released-only`. The folder must hold the wheel, its `.check.json`, its `.delivery.txt` and `MANIFEST.json` (4 files). Then verify the pack LOCALLY, read only: `AGENTBUS_DEVICE=laptop python org/devices/intake/intake_receive.py verify --from "$HOME/tdrop/out/intake-20261015-duckdb"` and keep its LAST line (`INTAKE-VERIFY pack=<dir> wheels=1 verified=1 checked=1 stray=0 ok=True` expected). Do not run `prove` or `install` on the laptop.
3. **Taildrop to dell1**, once: `tailscale file cp <each of the 4 files> dell1:` (the trailing colon; one `tailscale file cp` per file or one call with all four; use the `--name` flag only if a name needs fixing). First confirm dell1 is online (`tailscale status`). Record each command, its exit code and the time in `org/devices/intake/records/intake-20261015-duckdb/TAILDROP_RECORD.md` (ASCII; the SHA-256 of each file sent; no file content). Send EACH file at most once; never re-send on a re-run of the test. If any `tailscale file cp` fails, report the printed error and STOP (a partial delivery is dell1's to ignore; say which files went). A Taildrop has no read receipt: the delivery is proven by dell1's own `tailscale file get` and `verify`, which the issuer asks of dell1's manager next; say so in the record.
4. Extend `.tools/tests/test_round22_journey_record.py` (the round-22 test merged at 3c3d04d4ec; keep its three flags) with `--release` printing `JOURNEY-RELEASE released=<n> check8=<SIGNED|OTHER> file=<name> sha256=<12 hex> ok=<True|False>` (read-only: the release folder holds exactly the one file, its bytes equal the fetch record's sha256, the check record shows check 8 passed and names the CTO's signed file), `--pack` printing `JOURNEY-PACK files=<n> manifest_ok=<True|False> verify=<the INTAKE-VERIFY last line> ok=<True|False>` (read-only: re-runs `verify` locally, never sends), and `--taildrop` printing `JOURNEY-TAILDROP files_sent=<n> failed=<f> target=dell1 ok=<True|False>` (reads ONLY `TAILDROP_RECORD.md`; it never calls Tailscale).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~122/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W122-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTal4-AC1" cell_refs="CT-al-4"><invocation>python .tools/tests/test_round22_journey_record.py --release</invocation><expect>ok=True</expect></criterion>
`CTal4-AC1` -- the one checked wheel is released with check 8 signed and nothing else is in the release folder for this batch (base: the flag does not exist; the release folder does not hold the batch); report the whole line.

<criterion id="CTal4-AC2" cell_refs="CT-al-4"><invocation>python .tools/tests/test_round22_journey_record.py --pack</invocation><expect>ok=True</expect></criterion>
`CTal4-AC2` -- the pack holds the 4 files and `verify` reads wheels=1 verified=1 checked=1 stray=0 ok=True (base: the flag does not exist); report the whole line.

<criterion id="CTal4-AC3" cell_refs="CT-al-4"><invocation>python .tools/tests/test_round22_journey_record.py --taildrop</invocation><expect>ok=True</expect></criterion>
`CTal4-AC3` -- all four files were sent to dell1 by Taildrop, each exit code recorded (base: the flag does not exist); report the whole line and the record.
</proof_of_spec>

<expected_criteria>CTal4-AC1,CTal4-AC2,CTal4-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~122/NFRA_CTLPLN.TO-CT-al-4.duckdb-release-pack-and-taildrop.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTal4-AC1,CTal4-AC2,CTal4-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round22.md</decomp_doc>
<owned_cells>CT-al-4</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/records/intake-20261015-duckdb/
.tools/tests/test_round22_journey_record.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the Taildrop is a tailnet transfer of one file set to dell1; no credentials.
comp-adversary: RUN -- a second send of the same files (the test never calls Tailscale; each file at most once); a file other than the 4 sent (the pack folder is the only source; list it before sending); the release taking place without the CTO's signature (the tool must refuse; the test requires check8=SIGNED); the wheel executed or installed on the laptop (the cell runs verify only, never prove or install); the pack committed into a git tree (it lives under the user's tdrop folder, outside every tree); a Taildrop to the wrong device (the target is dell1: the trailing colon form, confirm in `tailscale status` first); BLIND: whether the files arrived (no read receipt; dell1's manager reads them next), the install and the lane's read are later steps, and the risks the CTO accepted in check 8 stand.
risk: SERVED -- a release record, a local pack and one file set sent to one box on the tailnet, nothing installed or run; reversible by dell1 deleting its Taildrop inbox.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/records/` and the intake tools are NFRA_CTLPLN's laptop-side intake route (C-INTAKE); the CTO signed check 8 and ruled the journey (@9735e81b15, @29a69ec1c5).
</preflight>

Base checks, dry-run by the issuer before the cut: CTal4-AC1, AC2 and AC3 FAIL as expected (the flags do not exist; nothing is released, packed or sent). Pre-state read by the issuer 2026-10-15 ~20:1xZ: the release folder holds only intake-20261008-a; `tailscale status` lists dell1 online.
Source: CTO round-21 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round21.md` @a558191b7c), msg 109483; FWD-15, FWD-16, FWD-18, FWD-19.
