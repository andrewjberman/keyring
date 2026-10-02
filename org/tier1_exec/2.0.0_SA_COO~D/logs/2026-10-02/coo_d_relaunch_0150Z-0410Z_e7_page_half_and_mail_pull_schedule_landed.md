# Relaunch: E7 page half on DEV, the mail pull's positive arm and its daily schedule landed — 2.0.0_SA_COO~D

**Date:** 2026-10-02 (01:5xZ-04:1xZ)
**Task Order:** ad-hoc (FAST, no task orders): DSGN_IRPTV1 item 63; NFRA_TRNSPT FWD-7 (CTO batches 104, 107, 109)
**Status:** COMPLETE to a safe stop: wound down on Andrew's word (MSTR relay 104033, ~03:4xZ, disk at 100% at site Z)

---

## Objective

Relaunch per the reboot brief (`REBOOT_BRIEF_20261001_2.0.0_SA_COO_D.md`): watcher, startup, leases, then the next
unblocked item of the three FAST projects. IRPT_DASHBD item 5 stayed blocked, so the NFRA_TRNSPT pull's `--apply` ran,
then E7's page half and the mail pull's schedule.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` (startup A.3) | PASS | forwarders resolve, 104 of 104 bare |
| comp-read | `--enumerate` on criterion.py, `--for` on RULINGS.md | SKIPPED | the rail refused both as piped census; native Grep/Read answered |
| comp-find | `--files` for a lane name | SKIPPED | refused as piped; native Grep over `.owned-paths.yaml` answered |
| rail (hook) | raw `find`, `grep -rn`, `aws s3api list-objects-v2` | WARN | denied as designed; the s3 listing ran under `# rail-checked` |
| naming gates | safe-apply naming-apply / naming-plan | PASS | 6 graded CONFORMANT |

**What worked:** the naming builder (`lib/opal_naming.name()`) gave all four slots first time; the naming plan gate
graded them at apply. **What failed:** nothing wrong; the rail's piped-census refusals cost three re-issues.
**Gap found:** none.

---

## Work Completed

### 1. Relaunch
`/watcher` (registered, pid 32356, re-armed on each expiry); inbox 7 of 7 READ; startup A-E; the LIVE_ARMS row's
loop armed (cron da920dd1, `/canonical-drive DSGN_IRPTV1 once` every 10 minutes; deleted at the wind-down). Leases read
FAST (presence-extended); 5174 found serving; portal DEV fast-forwarded to site Z's 24646bca (relay 104004).

### 2. NFRA_TRNSPT: the pull's positive arm (record `R3_APPLY_RUN_20261002.md`, @4b9ab98dd2)
`pull.py --gateway --days 7 --apply` 02:07Z: 13 listed, 1 admitted, 4 bronze objects (hashes equal the sidecar's);
`silver.py --date 2026-10-01 --apply`: 1 row, 0 residual flags, held_out false (held-out rate 1 of 2).

### 3. DSGN_IRPTV1 item 63 (E7 page half), portal DEV `281b03c6`, CI 36957593316 green
`readOwnedRequest` accepted exactly two fields, so ~Y's served `comparisons` would have refused every opened request.
Now optional and read to the schema; the dialog prints "Compared with A and B."; pin iv-e-132; real run on 5174
VERDICT REQUEST-COMPARISONS-REAL-OK. ~Y's order 104009 answered: PROD b3a1d8a6 does not carry it.

### 4. NFRA_TRNSPT: the mail pull's daily schedule (CTO batch 104), APPLIED
Code @84a59c91e6 (landed_dates, 403-as-absence, NAMES.json) and @e3707e911f (mail_handler, build.sh with the assets,
mail_pull.tf) under exact-file lane NFRA_TRNSPT_FAST_D_MAIL (batch 107). Packet @c19926eeae + CTO half @1062de89b1.
Ledger `nfra-trnspt-mail-pull-schedule-20261002`: safe-apply 9 added / 0 / 0; read-back equal; one QA invoke 04:04Z
(13 listed, 1 known, 12 near misses not written, 0 landed); CLOSED 3 of 3.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Built E7's page half before ~Y serves | the ruling says the page shows the names once served; the reader fix had to land first or the serve breaks the page |
| `_get` reads absence through the listing on a 403 | keeps the role's ListBucket to its prefix, as batch 104 item 2 rules; a 403 on a present key stays loud |
| `build.sh` carries `data/transcripts/assets` | criterion and wipe read it at run time; without it the bundle falls back to the inline author table |
| Finished the in-flight deploy after the wind-down word | NEVER-2: applied already; finishing was two reads and one invoke, no local disk |
| `HALT_ACK=1` at safe-apply | 40 routine base-inbox messages, 2-9 days old, none STOP-class |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~D/R3_APPLY_RUN_20261002.md` | the positive arm's record | Yes — `4b9ab98dd2` |
| portal `contracts/owned-requests.ts`, `contracts/wire/OwnedAnalysisRequest.ts`, `tabs/analysis/OwnedRequestHistory.tsx`, `__tests__/dsgn-irptv1/iv-e-132...` | item 63 | Yes — portal `281b03c6` (origin DEV) |
| `org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md` + item63 shots | item 63, open call | Yes — `2590c0f295` |
| `data/transcripts/scripts/outlook/{pull.py,land_bronze.py,NAMES.json}` | in-lane half | Yes — `84a59c91e6` |
| `infra/aws/{terraform/transcripts/mail_pull.tf,lambda/transcripts-pull/{mail_handler.py,build.sh}}`, `data/transcripts/scripts/tests/test_mail_pull_handler.py` | infra half | Yes — `e3707e911f` |
| `.../MAIL_PULL_SCHEDULE_PACKET_20261002.md` | the packet, COO half | Yes — `c19926eeae` |
| ledger json + change_management entry | opened, then closed | open `cdb5f18527`; close in this log's commit |
| `org/missions/D9/NFRA/NFRA_TRNSPT/STATUS.md` | landed, next | Yes — this log's commit |

---

## Blockers

- BLOCKED on Andrew: a portal PROD promote carrying DEV `281b03c6`; ~Y's irpt-status E7 apply is held on it.
- BLOCKED on 2.0.0_SA_COO~P: `IRPT_DASHBD.TO-DB-b-2` and `TO-DB-b-4` (both `pending`) for IRPT_DASHBD plan item 5.

---

## Current State

The mail pull runs daily at 23:30 UTC as `outlook-global-transcripts-pull-lambda` (rule
`outlook-global-transcripts-pull-daily`), writing only under `s3://opal-data-transcripts/outlook/transcripts/`; it is
applied, read back and QA-invoked, ledger closed. The E7 page half is on portal DEV `281b03c6`, not on PROD
`b3a1d8a6`. No act of this seat is in flight; the loop cron is deleted; workspace commits are LOCAL on CLOUD (the push
is 0.0.0_AB_MSTR's).

---

## Next Steps

1. **[2.0.0_SA_COO~D] Read the first scheduled fire** (2026-10-02T23:30Z) from its `run.json` under
   `outlook/transcripts/state/pull_runs/` — FWD-7 DONE only when it lands a real admitted email.
2. **[Andrew] Promote portal DEV `281b03c6` (or later) to PROD** — then ~Y serves E7 and this seat re-walks
   REQ-a1d9abc0... with `--expect-text` for both names.
3. **[2.0.0_SA_COO~P] TO-DB-b-2 / b-4** — un-parks IRPT_DASHBD plan item 5 here.
4. **[2.0.0_SA_COO~D] Re-arm the loop** only off the LIVE_ARMS row at relaunch.
</content>
