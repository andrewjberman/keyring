# TO NFRA_GATSCP.TO-GS-e-3 -- round 2 GS-e-3: an order to a seat on another box travels without a hand relay, and never before origin has it

<to_id>NFRA_GATSCP.TO-GS-e-3</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~4</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-e-3` (`decompositions/NFRA_GATSCP_DECOMP.round2.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

Seats on different boxes do not share an inbox. A cross-box order travels as a "crossbox file" `org/devices/crossbox/XB-*.json`,
made by `.tools/crossbox-call.py` (owned by NFRA_CTLPLN; extend it here, do not redesign its file protocol). Only the two boxes'
managers (`0.0.0_AB_MSTR` lanes) talk across boxes, over the agent bus. Today:
- `crossbox-call.py open --kind ORDER --to-device <box> --to-serial <serial> --from-serial <serial> --subject ... --body <path>`
  writes the file (refusing an uncommitted body); `line --id <XB id>` prints the one bus line (refusing an uncommitted crossbox
  file; it stamps the commit from a local `git log -1`, :304-311); a manager then sends that line BY HAND with
  `bash .tools/agentbus-sqs.sh send <device> <from-serial> "<line>"` and records it with `sent --id --bus-message-id`. On the
  receiving box, `receive --line` answers PULL-FIRST (exit 5) when the commit is not in its tree (:352-355).
- The committed-body checks are LOCAL only (`tracked_clean`, :229-236): nothing checks origin, so a line can go out before the
  receiver can fetch the commit, and the receiver sits in PULL-FIRST. Nothing links a task order's issuance to `open`, and nothing
  sends automatically. Times are UTC already (`stamp`, `parse_utc`, :85-100).
- Serial to box: only site Z has lane letters (`org/devices/DEVICES.json` `devices.sitez.lane_letters == ["Z"]`), so a serial
  whose `~lane` starts with `Z` (e.g. `0.7.0_AE_CloudOps~ZQ`) is on sitez. No other box has letters.
- Exit codes today: 0, 2, 3 REFUSED, 5 PULL-FIRST. `--selftest` (no hyphen) prints `CROSSBOX-SELFTEST cases=k/n ok=True`.
  Global flags `--root`, `--device`.

### THE CELL

`GS-e-3`. Crossbox delivery: `line` refuses until the order's and the crossbox file's commits are on origin; `issue --order` opens
the crossbox file for an addressee on another box; `send-pending` (a manager only) sends what is admitted; all times UTC.

**Build** in `.tools/crossbox-call.py`:
1. `line --id`: additionally refuse (exit 3, `REFUSED: commit <c> is not on origin yet ...`) unless the crossbox file's commit AND
   the body's commit are each contained in at least one `refs/remotes/origin/*` ref of `--root` (`git branch -r --contains`, or
   `merge-base --is-ancestor` per remote ref). The tool does not fetch; the caller does.
2. `issue --order <task-order path> [--to-device <box>]`: read `<issued_to>`, `<issued_by>` and the `# TO ...` title from the
   order (committed). Resolve the addressee's box: `--to-device` if given; else a `~lane` starting with a box's lane letter in
   DEVICES.json; else this box. If the box is this box: print `XBOX-ISSUE local <serial>` and open nothing (exit 0). Else run
   `open` (kind ORDER, from = `<issued_by>`, body = the order file) and print `XBOX-ISSUE opened <XB id> <box> <serial>`.
3. `send-pending [--dry-run]`: refuse (exit 3) unless the acting serial (`OPAL_AGENT_SERIAL`, else the session serial file) is a
   `0.0.0_AB_MSTR` serial or lane. For every crossbox file from this box with state OPEN and no `sent`: compute the line as in (1);
   if refused, print `HELD <id> <reason>`; else send it with the command in env `CROSSBOX_SEND_CMD` (default:
   `bash .tools/agentbus-sqs.sh send`), called as `<cmd> <to_device> <from_serial> "<line>"`, read the bus message id from its
   stdout, and record `sent` exactly as `sent --id --bus-message-id` does, with the UTC time. `--dry-run` sends nothing and
   prints what it would send.
4. Write `.tools/tests/test_crossbox_deliver.py`: it builds a throwaway git repo with a bare `origin` in a temp dir (with the
   files `--root` needs), and asserts:
   (a) `line` is REFUSED while the commit is local-only, then ADMITTED after a push to the bare origin (the difference control);
   (b) `issue` on an order to `0.7.0_AE_CloudOps~ZQ` opens a crossbox file to sitez; on an order to a serial with no lane letter
       and no `--to-device` it prints `XBOX-ISSUE local` and opens nothing;
   (c) `send-pending` under an MSTR serial with `CROSSBOX_SEND_CMD` set to a fake command (which echoes a bus id) records `sent`
       with a time matching `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$` for the pushed item, and prints `HELD` for a local-only item;
       under a non-MSTR serial it exits 3 and records nothing.
   It prints one last line `XBOX-DELIVER ok=<True|False> cases=<passed>/<total>`. It needs no network and touches no file
   outside its temp dir.

### ACCEPTANCE

<criterion id="GE3-AC1" cell_refs="GS-e-3"><invocation>python .tools/tests/test_crossbox_deliver.py</invocation><expect>XBOX-DELIVER ok=True</expect></criterion>
`GE3-AC1` -- the three behaviours above, each with its control arm, in a throwaway repo with a bare origin.

<criterion id="GE3-AC2" cell_refs="GS-e-3"><invocation>python .tools/crossbox-call.py --selftest</invocation><expect>CROSSBOX-SELFTEST cases=</expect></criterion>
`GE3-AC2` -- the tool's own selftest still runs; its last line must read `ok=True` (report it whole; a `ok=False` is a FAIL of this
criterion, recorded as such).

<expected_criteria>GE3-AC1,GE3-AC2</expected_criteria>

AC1 FAILs at the base (the test file does not exist). You write the test; the face above fixes what it must assert, so the
assertions are not yours to soften. Each invocation's last line is matched.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- No edit outside the grant. Send nothing on the real agent bus; open no real crossbox file in the repository's
  `org/devices/crossbox/`; every exercise runs in the temp repo.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W4-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the test
  or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not
  block.

<paths>
.tools/crossbox-call.py
.tools/tests/test_crossbox_deliver.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular `org/devices/` and `.tools/agentbus-sqs.sh`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round2.md</decomp_doc> (round 2), cell `GS-e-3`.
<owned_cells>GS-e-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GE3-AC1, GE3-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~4/NFRA_GATSCP.TO-GS-e-3.proof_of_spec.json` with `to_id`
`NFRA_GATSCP.TO-GS-e-3`, validated with `python .tools/proof-of-spec-check.py <instance> GE3-AC1,GE3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; every case name of the test with its verdict; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule; send-pending is a verb, its caller (a /govern step) is a hookup routed to 0.0.0_AB_MSTR at the merge.
comp-iam: DECLARED-NOT-APPLICABLE no IAM; the bus send is faked in the test.
comp-adversary: RUN -- AC1 (a) is a difference control (local-only refused, pushed admitted); (c) refuses a non-manager. BLIND: the real bus send and a real receiving box are not exercised here; GS-e-2 and the issuer's next real cross-box order are.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @5c65160327 item 2, ruling R3; PRD C-DELIVER; decomposition round 2. Base dry-run (box/dell1
7611122124): GE3-AC1 FAIL as expected (the test file is absent); GE3-AC2 PASS as expected (`CROSSBOX-SELFTEST cases=21/21 ok=True`).
