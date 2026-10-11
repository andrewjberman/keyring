# r47 aw-10 stopped at STOP 3: the master template is not in the synced library, and the locate script's own exit code is what proved it -- 0.7.0_AE_CloudOps~ZC

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** AMGT_CORPUS.TO-WRITE-R47-aw10.template-put-sitez
**Status:** STOP 3, reported. Nothing written. The re-cut is the issuer's.

Fifth log of the day. Continues `zc_r45_au1_bronze_ingest_world_write.md`.

---

## Objective

A second WORLD write: put the master one-pager template, write-once, into the `research_template` bronze
table. Its precondition is that exactly one file in the synced library carries the master's name.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| crossbox-call.py | `ack/close/status --id 7056` | PASS | State read back after the act. |
| comp-schedule / comp-iam | not run | SKIPPED | Order's preflight declares both NOT-APPLICABLE; and no put occurred, so there was nothing to gate or to grant. |
| comp-blast | not run | SKIPPED | No infra change, and in the end no write at all. |
| aw10_locate.py | the issuer's check, read before running | PASS (after a path fix) | Reading it first is why its rc was interpretable -- see below. |

**What worked:** reading the check script's docstring before trusting its exit code. It documents exactly
two exits, 0 and 3, which is what made rc=1 legible as an instrument failure rather than a reading.

**What failed:** the order's step-3 invocation, as written. Filed as row Z-S92.

---

## The result

```
template_locate root C:\Users\Opal Bloomberg\OneDrive - Opal Capital\...\Research source env:OneDriveCommercial+relative
template_locate matches 0 of files_walked 378
template_locate expected_size 383839 size_equal None
```

rc=3, the script's documented "none or more than one". **STOP 3.** Per step 3 I wrote nothing further,
committed the evidence (`ec5c71c561`) and reported. No `--write` ran in either of its two ordered forms,
no bronze key exists, the library and every source file are untouched.

STOP 0, 1 and 2 cleared first: both halves signed (CTO line 6 begins `**SIGNED**`, read by printing the
bytes at the cited line with a positive control on the ref), the three blobs match the pair's prefixes,
and 0 of 70 python processes carried `lib.research.corpus.template` -- indeed 0 carried
`lib.research.corpus` at all.

## Why the zero is trustworthy

Three independent reasons, because a zero that stops a WORLD write should not rest on one instrument:

1. **The walk's own denominator.** `files_walked 378` equals the library census's file count, read twice
   today (02:38Z and 09:47Z, both `folders 102 files 378`). The zero covers the whole library, not a
   truncated walk.
2. **A second instrument, in a second language, 15 hours earlier.** Under `TO-READ-R44-at-4` this lane
   measured the same absence with PowerShell `Get-ChildItem -Recurse -Filter` -- not Python `os.walk` --
   and recorded `0 matches`, with a positive control of 79 `.xlsx` files and 0 enumeration errors, plus
   the nearest name being the un-prefixed `..._v1.xlsx` under Total Energies TTE FP (`2274227184`).
3. **The placeholder explanation is excluded.** Round 45's ingest hydrated all 11 OneDrive placeholders,
   and today's 09:47Z census reads `placeholders 0 of 378`. So no unhydrated placeholder is standing in
   for this file.

**The issuer is not contradicted.** Its SharePoint search found the item (site `Shared`, item
`01L6LHKF...MJXN`, 383839 bytes, modified 2026-07-24). Both readings are true, and the gap between them
IS the finding: the item exists in SharePoint and has not reached this device's OneDrive sync. That is a
sync question, not a search question, and it is the issuer's to route.

## The rc=1 trap, and why it mattered here

Step 3's invocation is `python org/.../checks/round47/aw10_locate.py`. That cannot work: `python <path>`
puts the SCRIPT's directory on `sys.path` and never the cwd, so `from lib.research.corpus import ...`
raises `ModuleNotFoundError` before the walk opens anything -- even with the cwd at the repository root,
which it was (printed beside the run). Control: `python -c 'print(sys.path[0])'` prints empty, i.e. the
cwd, which is why round 45's `python -m lib.research...` steps all ran, and why round 45's
`au1_accounting.py` ran (it imports only `re` and `sys`).

**The danger was not the broken import; it was that rc=1 could have been read as the STOP.** An executor
treating "non-zero means STOP 3" would have reported STOP 3 from an instrument that never looked at the
library, and a genuine absence would be indistinguishable in the record from a failed import -- on an
order whose entire purpose is deciding whether one object gets written. The discriminator was free and
sat in the script's own docstring: 0 and 3 are its only defined exits, so rc=1 is the instrument, never
the world.

I ran the same script byte-unmodified under `PYTHONPATH=.`, which changes only `sys.path`, and recorded
BOTH invocations whole in the evidence so the record shows what was ordered and what was run. Filed as
row `AMGT_CORPUS-Z-S92` (`02e7bad6fc`), OBSERVATION/INERT, disarm owner the issuer, with the note that it
generalises to every future `checks/<round>/*.py` that imports `lib.*` and is ordered as a bare path.

## On the criteria

AC1-AC4 read **0, 0, 0, 0** against expectations of 2, 1, 1, 1. That is the correct reading of a STOP'd
order and I said so in the evidence rather than leaving a grader to wonder: steps 4 to 7 are the steps
that emit the graded lines, and the order forbids reaching them once STOP 3 fires. I also did NOT run
step 3a's task census, because it is a pre-PUT condition with no put to gate, and running it would have
been manufacturing a criterion line past a STOP. The prior equivalent reading from round 45 is cited in
the evidence as context, explicitly not as this order's proof, and with the note that round 47's filter
adds a fifth token (`template`) that round 45's did not carry.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Treat rc=1 as an instrument failure, not STOP 3 | The script documents exits 0 and 3 only. A failure mode that is indistinguishable from a genuine negative is the thing to break, and here it was free to break. |
| Fix `sys.path`, not the script or the order | `PYTHONPATH=.` supplies exactly what the script's docstring assumes and changes nothing else. Editing the issuer's check or the order would be out of lane. |
| Record BOTH invocations whole | The record should show what was ordered and what was run. Showing only the working one would hide the defect. |
| Not run step 3a | It gates a put that will not happen. Running it to satisfy AC4 would be proceeding past a STOP for a number. |
| State the 0/0/0/0 reading explicitly | A grader seeing four zeroes on a WORLD order should not have to guess whether the proof failed or the order stopped. |
| Report the SharePoint/sync gap as the finding, not as a contradiction | Both readings are true. Framing it as the issuer being wrong would misdirect the re-cut away from the sync. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `.../deliverables/0.7.0_AE_CloudOps~ZC/evidence/r47_aw10_template_put_sitez.txt` | New -- 76 lines | Yes -- `ec5c71c561` (alone, per step 8) |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | Appended row Z-S92; 201 rows, gate re-graded only the 1 new row | Yes -- `02e7bad6fc` |
| `org/devices/crossbox/XB-20261011T170830Z-7056.json` | acked + closed to-side | pending commit at time of writing |

**World state changed by this seat: NOTHING.** No S3 object, no dossier, no schedule, no vendor call.
Every AWS and filesystem act in this block was a read.

---

## Blockers

None owned by this lane. Open elsewhere: the template's sync-to-site-Z question and the Z-S92 disarm
(`2.0.0_SA_COO~C1`), the r45 ledger close and AC5 (issuer / CVO), a18's routing (`2.0.0_SA_COO~T2`), the
`AGENTBUS_DEVICE` launcher fix (`0.0.0_AB_MSTR~Z`).

---

## Current State

`0.7.0_AE_CloudOps~ZC` is LIVE on site Z, watcher armed, TO queue empty. The r47 aw-10 cell is STOPPED at
its own precondition, correctly and with nothing written: the master template
`FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx` is absent from this device's synced library on two
independent readings 15 hours apart, while existing in SharePoint per the issuer's search -- a sync gap,
not a search miss. Nine commits stand on `box/sitez` from this session, all LOCAL (one writer; this seat
is correctly refused), awaiting the integrator's window.

---

## Next Steps

1. **[`2.0.0_SA_COO~C1`] Route the sync, then re-cut** -- the master exists in SharePoint and not in this
   device's OneDrive. Until it syncs, no site-Z executor can satisfy step 3, and a re-issue of the same
   order will stop at the same rung.
2. **[`2.0.0_SA_COO~C1`] Disarm Z-S92** -- one line: `PYTHONPATH=.` in the order, or ship the check as
   `python -m` with a package path.
3. **[`2.0.0_SA_COO~C1`] If the re-cut keeps step 3a, note the fifth token** -- round 47 adds `template`
   to the filter, so round 45's reading is not a substitute.
