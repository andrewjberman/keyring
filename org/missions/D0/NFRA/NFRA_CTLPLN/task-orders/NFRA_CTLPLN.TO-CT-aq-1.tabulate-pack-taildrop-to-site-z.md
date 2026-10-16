# TO NFRA_CTLPLN.TO-CT-aq-1 -- workstream OUTCOME round 19 (cell CT-aq-1): FWD-18 on site Z, laptop half -- the released, checked tabulate pack is sent to site Z by Taildrop, once each, and recorded

<to_id>NFRA_CTLPLN.TO-CT-aq-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~129</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-129 @ffb2ae4fed) and again in the main tree after merge 4471df360a: CTaq1-AC1 JOURNEY-TAILDROP-SITEZ files_sent=4 failed=0 target=sitez ok=True (2 of 2 mutants held); CTaq1-AC2 JOURNEY-PACK files=4 manifest_ok=True verify=INTAKE-VERIFY pack=intake-20261016-tabulate wheels=1 verified=1 checked=1 stray=0 ok=True ok=True; proof VALID; diff paths inside the order. Taildrop: four `tailscale file cp ... sitez:` calls, each exit 0 at 05:05:26Z-05:06:26Z, printed output empty; NO read receipt, so delivery is NOT proven until site Z's own `tailscale file get` and `verify` (the issuer's call to site Z). In the sparse worker tree the older flags `--release` and `--check` read ok=False (the CTO's check-8 file is outside the sparse set); in the main tree after the merge every flag of the journey test reads ok=True (--taildrop-sitez, --pack, --taildrop, --release, --fetch, --check). Row W129-S1 OBSERVATION, INERT (the cell said the dell1 flag carries two mutants; in code it carried none; the new flag carries its own two). The worker reported a mistyped redirect that made a stray file outside the worktree, removed in the same session. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-aq-1` (`decompositions/NFRA_CTLPLN_DECOMP.round27.md`) | **outcome_ref:** FWD-18 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcome FWD-18 (`prd/NFRA_CTLPLN_PRD.md` line 201): a download tried on purpose and stopped on a Dell and on site Z, and the delivered file then installed on each. The CVO's C-S80 (`surprise-channel/adjudications/ADJUDICATION_v28.md`) reads it stopped on both, installed on dell1, and NOT yet installed on site Z. The CTO's round-26 analysis (`ledger/ROUND_ANALYSIS.round26.md` section 3 item 1) asks for the install on site Z "as on dell1". This cell is the laptop half: the `tabulate-0.9.0-py3-none-any.whl` pack is ALREADY fetched, checked 1-8 (the CTO signed check 8, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md`), released and packed at `$HOME/tdrop/out/intake-20261016-tabulate` (4 files: `MANIFEST.json`, the wheel, its `.check.json`, its `.delivery.txt`) and was already Taildropped to dell1. Nothing is fetched, checked or released again. You send the SAME four files to site Z (tailnet name `sitez`, address 100.99.180.19, online at the cut) and record it. The install on site Z is a later call by the issuer to site Z's CTO. Read first: `org/devices/intake/records/intake-20261016-tabulate/TAILDROP_RECORD.md` (the dell1 send, the shape to copy), `.claude/skills/tdrop/SKILL.md` (the Taildrop recipe: nothing sent by Taildrop is ever committed except the record of what was sent), `.tools/tests/test_round25_journey_record.py` (its `--taildrop` flag is the shape).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. `.claude/skills/tdrop` is outside that set: add it.

### BUILD

1. **Check the pack first, read only:** `AGENTBUS_DEVICE=laptop python org/devices/intake/intake_receive.py verify --from "$HOME/tdrop/out/intake-20261016-tabulate"` must print `INTAKE-VERIFY pack=intake-20261016-tabulate wheels=1 verified=1 checked=1 stray=0 ok=True`; keep the last line. If it does not, STOP and file a BLOCKING row with the printed output; send nothing. Do not run `prove` or `install` on the laptop.
2. **Taildrop to site Z**, once each: confirm `sitez` is listed and not offline (`tailscale status`), list the four files, then `tailscale file cp "<file>" sitez:` (the trailing colon; one call per file). Write `org/devices/intake/records/intake-20261016-tabulate/TAILDROP_RECORD_SITEZ.md` (ASCII; names, bytes and SHA-256 of the four files, written BEFORE the sends; then each command, its exit code and the time in UTC after it; no file content). Send EACH file at most once to site Z; never re-send on a re-run of the test. If a `tailscale file cp` fails, report the printed error and STOP (a partial delivery is site Z's to ignore; say which files went). Say in the record that a Taildrop has no read receipt: delivery is proven only by site Z's own `tailscale file get` and `verify`.
3. Extend `.tools/tests/test_round25_journey_record.py` (keep every existing flag and its output) with `--taildrop-sitez` printing `JOURNEY-TAILDROP-SITEZ files_sent=<n> failed=<f> target=sitez ok=<True|False>` (reads ONLY `TAILDROP_RECORD_SITEZ.md`; it never calls Tailscale; ok: 4 rows with exit code 0, 0 failed, the four SHA-256 values equal those of the pack's files read from disk, every command targets `sitez:`, distinct commands). Add the same two kinds of mutant cases the `--taildrop` flag carries (a row with a nonzero exit code; a row naming another device) and require `held=True`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~129/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~128/NFRA_CTLPLN.TO-CT-ao-2.tabulate-release-pack-and-taildrop.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W129-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaq1-AC1" cell_refs="CT-aq-1"><invocation>python .tools/tests/test_round25_journey_record.py --taildrop-sitez</invocation><expect>ok=True</expect></criterion>
`CTaq1-AC1` -- all four files were sent to site Z by Taildrop, each exit code recorded and each SHA-256 equal to the pack's file on disk (base: the flag does not exist); report the whole line and the record.

<criterion id="CTaq1-AC2" cell_refs="CT-aq-1"><invocation>python .tools/tests/test_round25_journey_record.py --pack</invocation><expect>ok=True</expect></criterion>
`CTaq1-AC2` -- the pack is unchanged after the send: 4 files and `verify` reads wheels=1 verified=1 checked=1 stray=0 ok=True (a control that holds at the base and after); report the whole line.
</proof_of_spec>

<expected_criteria>CTaq1-AC1,CTaq1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~129/NFRA_CTLPLN.TO-CT-aq-1.tabulate-pack-taildrop-to-site-z.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaq1-AC1,CTaq1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round27.md</decomp_doc>
<owned_cells>CT-aq-1</owned_cells>
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
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the Taildrop is a tailnet transfer of one file set to site Z; no credentials.
comp-adversary: RUN -- a second send of the same files to site Z (the test never calls Tailscale; each file at most once); a file other than the 4 sent (the pack folder is the only source; list it before sending); a Taildrop to the wrong device (the target is `sitez:`, confirmed in `tailscale status` first; dell1 already holds this pack and must not get it twice); the wheel executed or installed on the laptop (the cell runs `verify` only); the pack committed into a git tree (it lives under the user's tdrop folder); a pack altered by the send (AC2 re-verifies it); BLIND: whether the files arrived (no read receipt; site Z's own `tailscale file get` and `verify` say), the install on site Z is the issuer's later call, and the risks the CTO accepted in check 8 stand.
risk: SERVED -- one file set sent to one box on the tailnet, nothing installed or run; reversible by site Z deleting its Taildrop inbox. The same acts as `CT-ao-2` step 3.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/records/` and the intake tools are NFRA_CTLPLN's laptop-side intake route (C-INTAKE); the CTO signed check 8 (@9aed0e1263) and ruled the route's use for this pack (round-24 analysis @6b8e48b0d5; round-26 analysis @82ec4bb123 item 1).
</preflight>

Base checks, dry-run by the issuer before the cut: CTaq1-AC1 FAIL as expected (the flag does not exist); CTaq1-AC2 PASS as expected (a control: the pack verifies today). Pre-state read by the issuer 2026-10-16 ~04:5xZ: `tailscale status` lists sitez online; the pack folder holds the 4 files.
Source: CTO round-26 analysis section 3 item 1 (`ledger/ROUND_ANALYSIS.round26.md` @82ec4bb123), msg 109600; CVO C-S80; FWD-18.
