# Deploy Completion Record
**Date opened:** 2026-08-04T04:15Z
**Status:** OPEN -- closes when every leg below carries proof (unclosed at session end = COO alarm)
**Deploy:** MDPF_GLOBAL.T2C wave apply -- the canonical-clock activation (clock v2 @5a20433a5c). Sovereign checkpoint bound: today's FIRST FLOOR FIRE 11:00 ET, all four scopes advancing together to the 2026-08-03 frontier by ~12:15 ET, reported to Andrew (COO 040816Z, Andrew eyewitness verbatim "All of these should be running at the same time every day for all scopes").
**Authored by:** 0.7.0_AE_CloudOps
**Window:** apply must complete comfortably before 11:00 ET (15:00Z) today.
**Andrew-direct verbatims carried on this record (durable per the RECORD+BROADCAST protocol):** (1) ~0335Z my terminal: "This all makes sense, hold is released, and Leg B disclosure doesnt matter here." (2) ~0115Z at ~B's terminal (fork OPEN, gate-rebuild half of leg 1 held on it): "actually dont care about this freshness checker or its artifacts id terminate the whole thing." (3) ~0405Z at COO's terminal: "All of these should be running at the same time every day for all scopes."

## Manifest

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | lambda deploy | mdpf-daily-trigger @8311f1178 (leg-1a :769 floor-bypass; gate-rebuild half HELD on the terminate-vs-rebuild fork -- NOT in this deploy) | build+upload zip; TF apply picks new artifact; live get-function sha changes; tests 7/7 pre-commit | pending | OPEN |
| L2 | tf apply | mdpf-pipeline root: floor Scheduler set (mdpf-scheduled-floor 11:00 ET daily @America/New_York + role + permission) + accrual re-anchor cron(45 11) ET + DLQ list fix (@4957e6050f) | safe-apply; post-apply 0-diff; live get-schedule x2 shows ET expressions; 22a battery on the new scheduler role (one resource per call + separate positive control) | pending | OPEN |
| L3 | ec2-code deploy | dispatch S3 sync: repo mdpf-daily-dispatch.sh (35,320B) -> s3://opal-data-mdpf/code/ (replaces 32,077B @07-23) -- closes THREE compounded holds in one deliberate act: row-18 FATAL guard @3baf759022+@ccb5718c3a, Stage-4 underscore-twin kill @cc35d80925, A2-retirement Stage-3.5 @32e953198a (CTO aggregate-vintage finding 020556Z, disposition (a) accepted 020758Z) | aws s3 cp + head-object size/ETag verify; the twin-kill's effect (zero underscore writes) reads at the first scheduled cycle's write census | pending | OPEN |
| L4 | tf apply | opal-assets root: publisher rule->ET-Scheduler migration @1af2bf526 (12:15 ET both regimes + scheduler role; rule trio destroyed) | safe-apply; 0-diff; live get-schedule; old rule absent; 22a on the new role | pending | OPEN |
| L5 | records | roster inflection-window provenance @1af2bf526 (already committed; no apply surface) + tags on both series + MSTR push | tags cited; push confirmed | pending | OPEN |
| L6 | first-fire verify | 11:00 ET floor fire: per-stage rc reads (status.json fields, marker-blind per amendment #2) + all four scopes' served hyphen artifacts Last-Modified inside 11:00-12:15 ET + frontier == 2026-08-03 (lib/trading_calendar.py) | per-stage read to COO + DS immediately on completion; day 1 of the 3-TD proof | pending | OPEN |

**Serve-correction slot (shared event, separate ledger sections per the joint GO):** DS's DC1 family + Leg B fire on THIS ledger's close ping (DS armed, sub-5-min leg).
**Held out of this deploy, explicitly:** the gate-rebuild/partner-model half of leg 1 (terminate-vs-rebuild fork at Andrew; whichever branch lands cuts as its own change + deploy). The floor never needed the gate (its own declared requirement) -- nothing in this window depends on the fork.

## Log
- 20260804T0415Z OPENED with 6 legs by 0.7.0_AE_CloudOps
