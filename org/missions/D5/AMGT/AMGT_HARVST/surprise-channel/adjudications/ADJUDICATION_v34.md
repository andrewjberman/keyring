# AMGT_HARVST ROUND 25 -- L8 COMPILE (no judgment criterion; a SERVED/WORLD round)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~06:0xZ
**Input:** `2.0.0_SA_COO~H`'s `round25/ROUND25_DRAIN_END_PACKET.md` @`b635dadc66`, msg 26932. The packet was read to EOF (6,484 B).
**L7:** `o-1`..`o-5` terminal and VALID per the packet. 0 judgment criteria. Class: SERVED/WORLD.

---

## 1. THE SERVED PLANE, RECONCILED BY THIS SEAT ON S3

This seat listed every object in `opal-data-harvest` written since 2026-09-30T04:39Z, per top-level root:

| root | new objects | whose act |
|---|---|---|
| `bloomberg/harvest/bronze` | 13 | o-5 |
| `bloomberg/harvest/silver` | 15 | o-5 |
| `wsj/harvest/bronze` | 14 | o-5 |
| `wsj/harvest/silver` | 15 | o-5 |
| `seeking-alpha/harvest/silver` | **3** | o-4 (the 3 new parts) |
| `amgt/harvest/gold/research_dossier` | 87 | not this project (the AMGT_CORPUS dossier rewrite) |
| `derived/model_block/{6501,8035,9433}_JP_Equity` | 1 each | not this project (AMGT_CORPUS re-derives) |
| `filings/v1/ASML_NA_Equity` | 1 | not this project |

- **o-5:** bronze 13 + 14 = **27** and silver 15 + 15 = **30**, so **57, under `bloomberg/` and `wsj/` only**. That equals the packet.
  0 objects landed under `ft/` or `barrons/` (the challenged and rejected runs), and 0 under `seeking-alpha/harvest/bronze`.
- **o-4:** exactly 3 new sa silver parts.
- **The pairs held on the output:** no HARVST object landed outside the two named acts' roots in the window.

**The Scheduled Task (o-2's "Disabled, 0 triggers"): CONFIRMED.** `Export-ScheduledTask` for "Opal Data Harvest - Local
Publications" has an empty `<Triggers>` element and `Settings Enabled false`. Its last run was 2026-09-15. ⚠ An instrument note:
this seat's first read, `@($_.Triggers).Count`, printed **1**, which is PowerShell counting an empty collection as one element.
The XML is the authority.

## 2. THE CLOSE RUN'S TWO FAILs -- AGREED AS EXPLAINED, ONE WITH A CHECK-DESIGN NOTE

- **o-5 AC1 "sa: 3 new object(s)":** these are o-4's parts, which land after o-5 by design. This seat's S3 read (section 1) puts
  exactly 3 sa silver objects in the window.
- **o-2 AC1:** its "base script" is `git merge-base HEAD CLOUD`, which on the trunk after the drain IS the merged script. **A check
  whose baseline is computed from HEAD can only pass on the worker's branch.** It is not repeatable at close, so the close run's
  FAIL tells us nothing either way. The pinned re-run against `65aa9251bc` PASSes. For the check template: **pin the base commit
  in the check at cut time, never derive it from HEAD.**

## 3. FOR THE CTO'S GRADE (not grades)

1. **FWD-9's reach is one name, two publishers.** For Lenovo, bbg spans 273 of 273 days, but wsj spans 8. ft was rejected,
   barrons was challenged, and sa is pending renewal. Only bbg reaches the floor on the one name backfilled.
2. **FWD-7 is built and moves 0 of 5,730 name-days,** because no span-bearing run record exists yet. o-5 ran on pre-o-1 code.
3. **FWD-3 carries the CTO's own condition:** answered rows on `NM5NLQ6K50XZ01` and on the wsj URL/UUID key split.
4. **The issuer's proposed process fix is agreed:** before signing a WORLD half for a producer, trace argv to its config defaults
   and to the actual put call, and name the command that reaches it. Both o-5 misses (`jobs_per_run: 1`, and the outbox queue in
   front of `upload-harvest`) are that class. A stub-client put-count dry run catches both.

## 4. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W65-S1`, `Z-W65-S3` (BLOCKING: o-5's cut-time misses) | **GRADUATED** | Disarmed by AMENDMENTS 1 and 2. The act then landed inside its pair, and this seat's S3 read shows 57 objects under the two named roots only (section 1). |
| `Z-W53-S3`, `Z-W53-S4` | **CARRIED** | The sa rows are rebuilt (3 parts on S3). They graduate at round 26's mention rebuild, which gives the new rows their `mention_count` and backs the company query. |
| `Z-W58-S1` (ARMED, disarmed), `Z-W56-S2` | **CARRIED** | The gold flip waits on span-bearing run records. `--harvest-grammar` is in `run-local.ps1`, and the task stays Disabled until Andrew re-arms it. |
| `Z-W61-S1..S3`, `Z-W63-S1`, `Z-W65-S2`, `S4`, `S5` | **CARRIED**, INERT | as the packet |

## 5. L10 PRECONDITION

1. **Every task order terminal:** 5 of 5. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W65-S1`/`S3` GRADUATED; the rest CARRIED with conditions. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S44",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T06:00:00Z",
    "one_line": "L8 round 25: the served plane reconciles on S3 -- o-5 put 57 objects (27 bronze + 30 silver) under bloomberg/ and wsj/ only, o-4 exactly 3 sa silver parts, nothing under ft/ or barrons/; the harvest task is Disabled with an empty <Triggers>; o-2's close-run FAIL is a check that derives its base from HEAD and so cannot pass after the drain.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S3 opal-data-harvest objects with LastModified >= 2026-09-30T04:39Z: bloomberg/harvest/bronze 13, bloomberg/harvest/silver 15, wsj/harvest/bronze 14, wsj/harvest/silver 15, seeking-alpha/harvest/silver 3; others (amgt/harvest/gold/research_dossier 87, derived/model_block x3, filings/v1/ASML 1) belong to other projects.",
        "Export-ScheduledTask 'Opal Data Harvest - Local Publications': <Triggers> empty, Settings Enabled false; Get-ScheduledTaskInfo LastRunTime 2026-09-15; @($_.Triggers).Count printed 1 (empty-collection artifact).",
        "Packet s.1: o-2 AC1 base = 'git merge-base HEAD CLOUD'; pinned re-run against 65aa9251bc PASSes."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W65-S1",
      "AMGT_HARVST-Z-W65-S3"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @b635dadc66 asserts 5 of 5 terminal, o-4 and o-5 landed under signed pairs, 57 new objects only under bloomberg/ and wsj/, and a close run of 10 of 12 with 2 explained FAILs.",
    "world_is": "True as read on S3 and Task Scheduler. The one check that cannot be trusted at close is o-2 AC1, by design of its baseline.",
    "notes": "FOR THE ROUND-25 ANALYSIS: pin a check's base commit at cut time (never merge-base with HEAD); agree the issuer's argv-to-put trace before signing a producer's WORLD half; FWD-9 reach is bbg 273/273 and wsj 8/273 on one name."
  }
]
```
