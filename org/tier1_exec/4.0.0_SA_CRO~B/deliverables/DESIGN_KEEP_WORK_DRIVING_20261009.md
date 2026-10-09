# Design -- keep the work driving: the open-calls scan, cross-adjudication files, and no empty drive tick

**Author:** 4.0.0_SA_CRO~B. **Order:** Andrew-direct 2026-10-09 ~00:0xZ, recorded verbatim at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md`
@8c3ff8bbf9. **Status:** built on box/laptop; the knobs in section 4 are defaults until Andrew's word.

## 1. What already existed (build ladder rung 2)

| piece | where | what it already does |
|---|---|---|
| the queue | `org/devices/state/<box>/open_calls.json`, `.tools/open-calls.py` | one list per box, one writer per box; every write also goes to `s3://opal-313476888478-globgrph/fabric/open-calls/v1/box=<box>/open_calls.json`, so any box reads every box with no git lag |
| the cross-box measurement | `open-calls.py scope` | `verdict=OWN-BOX` or `CROSS-BOX`, measured from order paths, placement, Terraform roots and shared registers |
| the adjudicate act | `/open-calls --adjudicate <CODE>` | the CTO builds cards, rules each, records `CTO_ADJUDICATION_<CODE>_<stamp>.md` |
| a per-box scheduled task | `.tools/box-sync-schedule.ps1` | the install/status/uninstall pattern, everything derived, staggered minute slots |
| the tool-written inbox file | `.tools/crossbox-call.py receive` | a tool writes ONE `.md` into a seat's watched inbox on its own box; the seat's `/watcher` Monitor fires on it |

What was missing is exactly Andrew's complaint: the queue "doesn't sponsor any action". Nothing reads it on a clock.

## 2. Mechanism 1 -- the 10-minute scan forces the box CTO to adjudicate

**`.tools/open-calls-scan.py`**, one pass, run by the per-box Windows scheduled task **`Opal open-calls scan`** every 10
minutes (installer `.tools/open-calls-scan-schedule.ps1`, slots staggered by box: laptop :01, sitez :04, dell1 :07,
dell2 :09, then every 10 minutes). No agent is involved; the task runs while the user is logged on.

Each pass, on box B:
1. Reads B's list. A row is **DUE** when it is `OPEN`, `kind` is `fork` (an `act` is Andrew's to do and never nudges a
   CTO), and it carries no `escalation` (already sent to cross-adjudication or held for Andrew).
2. Resolves B's CTO: the box's canonical CTO serial if its MCP process is alive, else any live `1.0.0_SA_CTO~*` lane on
   B. None live -> the nudge goes to B's MSTR (it spawns or unsticks seats), saying the CTO is absent.
3. Writes ONE inbox file to that seat: `[OPEN-CALLS SCAN] <n> call(s) to adjudicate on <box>`, listing each DUE call
   (id, project, age, verdict, subject, source) and the three legal outcomes (section 2a). It re-sends when the DUE set
   changes, or every 30 minutes while it is unchanged (knob K1).
4. Publishes a scan heartbeat `fabric/open-calls/v1/box=<B>/scan.json` (scanned_at, cto serial, cto live, due count).
5. **Adjudicator duty.** If B is the cross-adjudicator of record (section 2b), it lists PENDING cross-adjudication files
   from every box and nudges its own CTO the same way. If B originated a file that is now RULED, it nudges B's CTO to
   close the row on that ruling.

### 2a. The box CTO's three outcomes per call (nothing else clears the nudge)

- **RULE it** (own-box, in pattern, one clear answer): `/open-calls --adjudicate`, then
  `open-calls.py close --id <id> --by <serial> --ruling <record>`.
- **ESCALATE it** (open-ended, deeply architectural, out of pattern, or touching another box -- a `CROSS-BOX` verdict
  always lands here): write the cross-adjudication submission and `python .tools/xadj.py open --call-id <id> --body <file>`.
  The row gets `escalation: {to: xadj, ref: <XA id>}` and stops nudging this box.
- **HOLD it for Andrew** (money, vendor, a directive-level change, a hold he set by name):
  `open-calls.py hold --id <id> --by <serial> --reason "<one line>"`. The row gets `escalation: {to: andrew}` and stays
  in the queue for `/open-calls`.

### 2b. Cross-adjudication files (the new record type, on the model of change-management files)

- **Submission** (written by the box CTO): `## Context`, `## Position` (the CTO's recommended ruling), `## Why it gave
  pause` with `### Ambiguity` (how), `### Out of pattern` (the normal pattern, and why it does not fit), `### Other
  solutions` (each, and why better or worse). `xadj.py open` refuses a body missing any of these headings.
- **Transport:** S3, the same store as the open-calls cluster copy: `fabric/xadj/v1/<XA id>.json`. No git lag, no bus.
- **Adjudicator:** the laptop CTO. **Backup:** the site Z CTO, when the laptop's scan heartbeat is older than 30 minutes
  or reads no live CTO (knob K2). The backup is decided by measurement each pass, never by a seat.
- **Ruling:** `xadj.py rule --id <XA> --by <serial> --ruling "<(a)... because ...>"` writes the ruling to the S3 object
  (state RULED) and the **record** `org/critical_paths/cross_adjudication/<UTC stamp>_<XA id>.md` (submission verbatim +
  ruling) on the adjudicating box: one writer per record file, carried to every box by box-sync.
- **Close-out:** the originating box's scan sees RULED and nudges its CTO, who closes the row with
  `open-calls.py close --id <id> --ruling <record path> --xadj <XA id>`; a RULED cross-adjudication satisfies the close
  rule that a CTO-ruled `CROSS-BOX` call otherwise meets only with a CLOSED-BOTH cross-box file.

## 3. Mechanism 2 -- no empty drive tick

- **`/canonical-drive`** section 1: a tick whose every in-scope project reads NO-OP runs `/next-calls <CODE> --drive`
  per project and fires its SEQUENCE's NOW lines and its WHILE-BLOCKED lines the same tick. A call it surfaces goes to
  the queue with `open-calls.py add` (the scan then forces it), never into a pause. The tick is a true NO-OP only when
  `/next-calls --drive` returns zero actionable options; the row then reads `NOTHING-LEFT: <why>`.
- **`/closer-drive`** step 2: an empty next-list runs the same.
- **`/next-calls`** gains the **WHILE BLOCKED** branch: for every option that waits on a call, a seat or an event (a 7a
  pull tomorrow), list what else advances the same project outside that track (the other cells, the other surfaces,
  the ad-hoc QA run that tests ahead of the scheduled fire, the work the answer will need either way). And the
  `--drive` form: no waiting on Andrew; calls are queued, FREE and WHILE-BLOCKED options are executed in order.

## 4. Knobs (defaults chosen; Andrew's word changes them)

- **K1** re-nudge an unchanged DUE set every 30 minutes (every scan is 10 minutes; a new or changed call nudges at once).
- **K2** the laptop counts as down when its scan heartbeat is older than 30 minutes or reads no live CTO.
- **K3** a `CROSS-BOX` verdict always escalates. The measurement reads most calls CROSS-BOX today (any order touching
  `.tools`, `lib` or `infra/aws/terraform/shared-infra` hits); if the laptop CTO's queue swells, the knob to turn is
  the measurement's breadth, not the rule.

## 5. Known constraint

CLAUDE.md section 5 bars building a notification or monitor unless Andrew explicitly asks. He asked, for this one
mechanism ("a 'notification' function that scans that json per box every 10 min"); the scan is scoped to it and sends
nothing off the fabric (no SNS, no SES, no email): one inbox file to a seat on its own box.
