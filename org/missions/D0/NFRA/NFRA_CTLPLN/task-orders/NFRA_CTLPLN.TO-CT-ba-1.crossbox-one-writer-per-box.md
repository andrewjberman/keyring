# TO NFRA_CTLPLN.TO-CT-ba-1.crossbox-one-writer-per-box -- workstream OUTCOME round 27 (cell CT-ba-1): cross-box call files get ONE writer per box: the from-side file and one answer file per answering box, read as one call (FWD-8)

<to_id>NFRA_CTLPLN.TO-CT-ba-1.crossbox-one-writer-per-box</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~139</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>open</status>
<status_reason>Issued by the issuer 2.0.0_SA_COO~C in the round-29 issuance, per the CTO's round-28 analysis (ROUND_ANALYSIS.round28.md @3894648aa3, msg 109677).</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ba-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** FWD-8 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Every box-sync merge conflict of 2026-10-16 (2 of 227 merges; 3 paths) was on an `org/devices/crossbox/XB-*.json` file that two or three boxes write: the sending box writes `sent` and `closed.from_*`, the answering box writes `ack` and `closed.to_*`, into the SAME file. The CTO ruled (`org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round28.md`, ruling 1; read it): the call keeps its id, but each side writes only its own file: the from-side writes `XB-<id>.json` (the ask and the from-side close); each answering box writes `XB-<id>.<box>.json` (ack, answer, close); the tool reads them as one call. Tests: a from-side close and a to-side answer committed on two boxes merge with zero conflicts; the existing calls read the same through the new reader.

Read first, whole: `.tools/crossbox-call.py` (1316 lines): the module docstring (the file shape and the "each box writes only its own fields" rule), `check_call` (line 154), `derive_state` (194), `dump` (200), the `Box` class (213): `read` 245, `save` 256, `open` 265, `sent` 444, `receive` 476, `ack` 558, `acked` 571, `close` 591, `withdraw` 607, `supersede` 648, `status_of` 702, `listing` 731, `merge` 749; and its `selftest`/`run_cases`/`merge_cases`. Then every consumer of the call files, each of which you read to see whether it reads a call file DIRECTLY (by JSON) or through the tool: `.tools/open-calls.py` (the link by `call_id`), `.tools/crossbox-deploy-check.py`, `.tools/crossbox-matrix.py`, `.tools/merge-resolve-known.py` (box-sync's known multi-writer resolver), and read-only: `.tools/owned-paths-validate.py`, `.tools/hooks/coo-drive-tick-gate.py`, `.tools/git-hooks/mstr-ledger-check.sh`. A consumer that parses a call file itself must go through the one reader after your change; a consumer that only names the folder needs no change. List each consumer in your report with `reads directly | through the tool | names the folder only` and what you changed.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### THE DESIGN (pinned; the issuer decided these, do not redesign)

1. **Layout 2.** From-side file `org/devices/crossbox/XB-<id>.json` with `schema` `"crossbox/2"` and the from-side fields only: `schema, id, kind, call_id, from_device, to_device, from_serial, to_serial, subject, body_path, opened_at, sent {at, bus_message_id}, ack_bus_message_id (null or a string: the bus id the sender records for the answer, today inside `ack`), closed_from {at, by}`, plus whatever fields `withdraw` and `supersede` write today (they are the issuing box's acts and stay in the from-side file). Answer file `org/devices/crossbox/XB-<id>.<box>.json` (`<box>` = the answering box's device name = the call's `to_device`) with `schema` `"crossbox-answer/1"` and `id, box, ack (null or {at, by}), closed_to {at, by} (nulls until set)`. `state` is NOT stored: it is derived by the reader exactly as `derive_state` does today.
2. **One reader.** `Box.read(call_id)` returns a document in the OLD merged shape (the one `check_call` validates today, with `ack {at, by, bus_message_id}` assembled from the answer file's `ack` and the from-side file's `ack_bus_message_id`, and `closed {from_at, from_by, to_at, to_by}` assembled from both), so every method and consumer that reads a call keeps working unchanged. For a `crossbox/1` file (all of the 235 existing ones) the reader behaves exactly as at the base.
3. **Writers route by side.** In layout 2: `open`, `issue`, `sent`, `acked`, `close --side from`, `withdraw`, `supersede`, `send-pending` write only the from-side file; `receive` (if it records a receipt), `ack`, `close --side to` write only the answer file of THIS box. A box refuses (`Refused`) to write the other side's file (the existing `need_box` rule, extended: `ack` and `close --side to` on a box whose device is not the call's `to_device`; `close --side from`, `sent`, `acked` on a box whose device is not the call's `from_device`). For a `crossbox/1` file every writer behaves exactly as at the base (single file), because the other box may still carry the old tool.
4. **`merge`** on a layout-2 call writes nothing and prints `CROSSBOX-MERGE <id> NOTHING-TO-FOLD (layout 2: each side writes its own file)`; on a `crossbox/1` call it behaves exactly as at the base.
5. **The switch.** `open` writes layout 2 only when the committed text file `org/devices/crossbox/LAYOUT` exists and its first line is `2`; otherwise it writes `crossbox/1` exactly as at the base. Do NOT create that file: the issuer commits it later, after every box carries the new tool (a box whose tool does not know `crossbox/2` refuses the schema loudly, which is the wanted behaviour, and the switch keeps that from happening in the meantime).
6. **No file is rewritten or renamed** by the change: the existing `crossbox/1` files stay byte-for-byte as they are.

### BUILD

Implement the design in `.tools/crossbox-call.py`; make the smallest changes in the consumers that parse a call file directly; extend `selftest`/`test_crossbox_call.py` only with what the layout needs. Then:

1. **The base is RED in its own suite and you fix its stale case.** `python .tools/tests/test_crossbox_call.py` reads `CROSSBOX-TEST cases=69/70 ok=False` at the base: the case `writer and watcher comparison` fails with `ValueError: substring not found` (a stale assumption in the case about the tool's text). Find why, repair THAT case to the tool's intended behaviour, change no other existing case, quote the old and new assertion in your report, and file one OBSERVATION row (the suite was red at the base).
2. **The test**, a NEW file `.tools/tests/test_round29_crossbox_split.py` (standard library plus the tool; temporary git repositories and a temporary bare remote only; no network; ASCII output) with arms: (a) with `LAYOUT` containing `2`, `open` writes exactly one file `XB-<id>.json` of schema `crossbox/2` and no answer file; (b) on the answering box (a second clone), `ack` writes only `XB-<id>.<box>.json` and leaves the from-side file byte-identical; (c) from-side `close --side from` committed on clone 1 and to-side `ack` plus `close --side to` committed on clone 2, then `git merge` of one into the other: ZERO conflicts (exit 0, no conflict markers), and `status` then reads `CLOSED-BOTH`; (d) the wrong side is refused for each writer named in design 3; (e) with no `LAYOUT` file `open` writes `crossbox/1` exactly as at the base (compare with the base tool, below); (f) the existing calls read the same: copy the real `org/devices/crossbox/` directory into a temporary root, run `list` and `status --id <each id>` with the base tool (`git show 7d4aef5b93:.tools/crossbox-call.py` written to a temporary file; skip the arm with exit 2 and a printed reason if that object is absent) and with the new tool, and require byte-identical output for all of the files; (g) `merge` on layout 2 prints NOTHING-TO-FOLD and writes nothing, on `crossbox/1` it folds as at the base; (h) `open-calls.py close` finds and closes through a layout-2 call by `call_id` (read how its reader works and drive the real function in a temporary root); (i) an unknown schema value is refused loudly; (j) control arms: a mutant of the reader that reads only the from-side file must make arm (c)'s CLOSED-BOTH assertion fail. Last line `CROSSBOX-SPLIT arms=<k>/<n> ok=<True|False>`.
3. **Lane check, read only.** Run `python .tools/owned-paths-validate.py --check-agent` (read its usage) for `org/devices/crossbox/XB-example.dell1.json` against the serials `0.0.0_AB_MSTR~DELL1`, `1.0.0_SA_CTO~DELL1`, `1.0.0_SA_CTO~DELL2`, `1.0.0_SA_CTO~Z`, `0.0.0_AB_MSTR` and report PERMIT or REFUSE for each (the answering box's seats must be able to commit their answer file). A REFUSE is a row, not a change: `.owned-paths.yaml` is not yours.
4. **Neighbouring suites.** Run and report the whole last line of each: `python .tools/crossbox-call.py --selftest`, `python .tools/tests/test_open_calls.py`, `python .tools/tests/test_crossbox_deliver.py`, `python .tools/tests/test_apply_who_and_crossbox.py`, `python .tools/tests/test_round13_batch.py`, `python .tools/tests/test_round23_hygiene_b.py`; base values: selftest `CROSSBOX-SELFTEST cases=40/40 ok=True`, open-calls `OPEN-CALLS-TEST cases=19/19 ok=True`, deliver `XBOX-DELIVER ok=True cases=16/16` (run the other three at the base in your worktree first to learn their base values).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~139/`. Every experiment runs in a temporary folder or repository; never write under the real `org/devices/crossbox/` and never open, ack or close a real call. NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W139-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTba1-AC1" cell_refs="CT-ba-1"><invocation>python .tools/tests/test_round29_crossbox_split.py</invocation><expect>ok=True</expect></criterion>
`CTba1-AC1` -- two boxes' writes to one call merge with zero conflicts, each side writes only its own file, every existing call file reads identically through the new reader, and the layout switch defaults to the old layout (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTba1-AC2" cell_refs="CT-ba-1"><invocation>python .tools/crossbox-call.py --selftest</invocation><expect>ok=True</expect></criterion>
`CTba1-AC2` -- the tool's own selftest passes with the layout's cases added (base: `CROSSBOX-SELFTEST cases=40/40 ok=True`, a control); report the whole last line.

<criterion id="CTba1-AC3" cell_refs="CT-ba-1"><invocation>python .tools/tests/test_crossbox_call.py</invocation><expect>ok=True</expect></criterion>
`CTba1-AC3` -- the tool's suite passes, its one stale case repaired (base: `CROSSBOX-TEST cases=69/70 ok=False`, a red base); report the whole last line.
</proof_of_spec>

<expected_criteria>CTba1-AC1,CTba1-AC2,CTba1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280` (the suites build temporary git repositories and can take about two minutes: if one hits the bound, run it alone once more and say so); record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~139/NFRA_CTLPLN.TO-CT-ba-1.crossbox-one-writer-per-box.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTba1-AC1,CTba1-AC2,CTba1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round29.md</decomp_doc>
<owned_cells>CT-ba-1</owned_cells>
</decomp_ref>

<paths>
.tools/crossbox-call.py
.tools/tests/test_crossbox_call.py
.tools/tests/test_round29_crossbox_split.py
.tools/tests/test_open_calls.py
.tools/tests/test_crossbox_deliver.py
.tools/open-calls.py
.tools/crossbox-deploy-check.py
.tools/crossbox-matrix.py
.tools/merge-resolve-known.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; temporary git repositories only.
comp-adversary: RUN -- a writer touching the other side's file (design 3 refusals and arm d); the reader dropping a field so a call reads OPEN when it is CLOSED-BOTH (arm c and the mutant of arm j); the 235 existing files read differently (arm f against the base tool, byte-identical); a box on the OLD tool reading a layout-2 file and mis-reading it (it refuses the unknown schema loudly; the LAYOUT switch is absent until the issuer commits it after every box carries the tool); a legacy file rewritten (design 6: none is); the lane refusing the answer file name (item 3 reports it; `.owned-paths.yaml` is the issuer's to ask for); box-sync's resolver treating an answer file as a conflict class it does not know (the files never conflict by construction; `.tools/merge-resolve-known.py` is read and reported); BLIND: this seat cannot start a second real box, so the two-box merge is exercised on two clones of a temporary repository, not on two real checkouts.
risk: LOCAL -- a change to a cross-box tool and its tests in temporary repositories; no real call file is written and nothing is pushed. It becomes live on a box only through box-sync, and layout 2 only when the issuer commits the LAYOUT switch.
lane: the <paths> block IS the grant (worker RULING 1). The CTO ruled the design (round-28 analysis ruling 1, msg 109677); the issuer pinned the layout, the switch and the routing above.
</preflight>

Base checks, dry-run by the issuer before the cut: CTba1-AC1 FAIL as expected (the test does not exist); CTba1-AC2 PASS as expected (control: `CROSSBOX-SELFTEST cases=40/40 ok=True`); CTba1-AC3 FAIL as expected (`CROSSBOX-TEST cases=69/70 ok=False`).
Source: CTO round-28 analysis ruling 1 and enrichment item 1; E8 read `E8_BOX_SYNC_CONFLICTS_SINCE_20261016.txt`; FWD-8.
