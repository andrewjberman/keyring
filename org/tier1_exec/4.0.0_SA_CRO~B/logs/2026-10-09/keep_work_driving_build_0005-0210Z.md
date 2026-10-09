# 4.0.0_SA_CRO~B -- keep the work driving: open-calls scan, cross-adjudication, /keep-driving switch, context+REC fields

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

**Window:** 2026-10-09 ~00:05Z -> 02:10Z (session start; no prior log this session).
**Order:** Andrew-direct 2026-10-09 ~00:0xZ, recorded by 1.0.0_SA_CTO at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md`
@8c3ff8bbf9; two follow-on Andrew-directs recorded by this seat (below).

## What was done

1. **Mechanism 1 -- the queue sponsors action** (87450d92e8, merged 593cda3601, in CLOUD per 0.0.0_AB_MSTR msg 107557):
   `.tools/open-calls-scan.py` (one pass; an OPEN fork with no escalation drops one `[OPEN-CALLS SCAN]` inbox file to the box
   CTO, else the box MSTR; re-sent every 30 min unchanged; heartbeat to S3), `.tools/open-calls-scan-schedule.ps1` (per-box
   task `Opal open-calls scan`, every 10 min, pythonw, slots laptop :01 sitez :04 dell1 :07 dell2 :09), `.tools/xadj.py`
   (cross-adjudication files: open/list/show/rule/adjudicator; laptop CTO rules, site Z when the laptop measures down; record
   dir `org/critical_paths/cross_adjudication/`), `.tools/open-calls.py` (`escalation`, `hold`, `close --xadj`).
2. **Mechanism 2 -- no empty drive tick** (same commit): `/canonical-drive`, `/closer-drive` run `/next-calls <CODE> --drive`
   on an empty tick; `/next-calls` gained WHILE BLOCKED and `--drive`; `/open-calls` gained the scan section.
3. **GC asks from 0.0.0_AB_MSTR (107412/107416/107453)**, done by a fork of this seat: 8ef00e34f1, merged 3be885041e --
   kill-maint DECLARED + WORKTREE exemptions (`.tools/detached-job.sh`), worktree_gc forced MERGED removal.
4. **CTO gate-owner ruling msg 107528** (status = LAST `<status>` tag; removing an earlier duplicate is not a flip): built in
   surprise-row-gate.py, to-pipeline-gate.py, owned-paths-validate.py; lane LOOP_MECHANISM refused my commit, so the patch
   went as a deliverable (ba0b4675ad) and 0.0.0_AB_MSTR landed it @ace2b3fa52 (CLOUD 71aac4e90d, validated by fetch).
5. **Andrew-direct ~00:4xZ / ~00:5xZ -- cloud switch** (record ANDREW_DIRECT_20261009_005xZ_KEEP_DRIVING_CLOUD_SWITCH.md;
   d9d313c5e0, merged 03a17ea6eb): `s3://opal-313476888478-globgrph/fabric/open-calls/v1/mode.json`, `open-calls.py mode`,
   skill `/keep-driving`; scan and empty tick read it first; absent/unreadable = ON. Drawn for him first (/draw).
6. **Andrew-direct ~01:1xZ -- context + REC fields** (record ANDREW_DIRECT_20261009_011xZ_OPEN_CALL_CONTEXT_AND_REC_FIELDS.md;
   40baa3aad1, merged 6ac0d356df): `add --context` required, `--rec` required on a fork, inbox-path sources refused.
7. **/next-calls "go"**: relayed to site Z (via 0.0.0_AB_MSTR) to close two Bloomberg asks Andrew's 23:0xZ word point 4
   covers; measured and DROPPED a lexical prior-ruling check (see Compiler Tools); removed worktree wt-cro-b-xadj and four
   merged scratch branches.

## Live evidence

- All four boxes scanning (S3 heartbeats): laptop 00:36Z, dell1 01:07Z, dell2 01:09Z, sitez 01:24Z -- every CTO live.
- First organic positive arm: sitez 01:24Z `due=2 target=1.0.0_SA_CTO~Z sent=yes` (two Bloomberg forks).
- First cross-adjudication record by 1.0.0_SA_CTO: XA-20261009T005240Z-625e RULED (7052d73c3f).
- `mode get` live: source=absent, every part ON on all four boxes. Inbox-source refusal exercised live (rc=1, nothing written).

## MCP traffic

Received and acked 107412, 107416, 107453, 107509, 107528, 107557, 107558, 107575, 107590. Sent: GC report and scan-install ask
to 0.0.0_AB_MSTR; build line and switch line to 1.0.0_SA_CTO; patch handoff and site Z close relay to 0.0.0_AB_MSTR.

## Compiler Tools

| tool | result | note |
|---|---|---|
| comp-which (x2) | FAIL | no curated rule for "open-calls queue" or "scriptable broker send"; found both by reading the skills directly |
| open-calls.py scope --selftest | PASS | 24 -> 27 -> 32 cases across three builds |
| open-calls-scan.py --selftest | PASS | 11 -> 13 -> 14 cases |
| xadj.py --selftest | PASS | 9/9 |
| to-pipeline-gate / surprise-row-gate / owned-paths-validate --self-test | PASS | 116/116, 230/230, 16/16 on the patched tree |
| commit-gate.sh | PASS | every .py touched |
| safe-merge.sh | PASS | 5 drains; one REFUSED empty merge correctly when the commit had been refused |

- **What worked:** S3 as the cross-box transport (no git lag); real-bytes check of TO-DELL-1 before shipping the status fix.
- **What failed:** a lexical prior-ruling matcher (whole-record and line-level IDF) missed the real ruling for both site Z asks
  ("model-block pull" vs "daily bloomberg price requests"); not built.
- **Gap found:** no tool answers "has Andrew already ruled on this?"; re-asking is caught only by a reader of meaning.

## Blockers

None.

## Current State

- Code on box/laptop: scan + xadj + switch + context/REC at 6ac0d356df (LOCAL at write; 593cda3601 and 3be885041e on origin
  CLOUD). Scheduled task `Opal open-calls scan` installed and Ready on laptop, sitez, dell1, dell2 (log
  `<git common dir>\open-calls-scan-task.log` on each).
- S3: `fabric/open-calls/v1/box=<box>/{open_calls.json,scan.json}`, `fabric/open-calls/v1/mode.json` (not yet written),
  `fabric/xadj/v1/<XA>.json`.
- Open on site Z: sitez-20261009T011758Z-107a and -493c, covered by Andrew's 23:0xZ point 4; close relayed via 0.0.0_AB_MSTR.
- Design: `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/DESIGN_KEEP_WORK_DRIVING_20261009.md`.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Close the two covered Bloomberg asks `--ruled-by andrew` (relay in flight via 0.0.0_AB_MSTR).
2. **[4.0.0_SA_CRO~B]** Watch the first organic cross-box escalation's close-out leg (event-gated).
3. **[Andrew, carried]** A standing-rulings register (topic -> standing answer, written by the CTO when it records an answer
   that says "never ask again") is the sound form of the prior-ruling check; proposal only.
