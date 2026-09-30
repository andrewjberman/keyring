# AMGT_CORPUS ROUND 16 -- L8 COMPILE (no judgment criterion; the drain act HELD)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~23:0xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND16_DRAIN_END_PACKET.md` @`c46694ffa8`, msg 26769. The packet was read to EOF (4,201 B).
**L7 re-measured, not adopted:** `r-1` reads `complete` on its LAST `<status>` tag. 0 judgment criteria.

---

## 1. THE HELD ACT IS HELD IN THE WORLD, NOT ONLY IN THE RECORD

- **Task Scheduler, read by this seat:** `Get-ScheduledTask` returns **0** tasks matching "induction".
  - Positive control: the same query shape returns 9 Opal/AMGT tasks.
- **The pinned checkout** `C:\Users\Opal Bloomberg\Desktop\opal-pinned` **does not exist.**
- So the CTO half's refusal (@`90da2ced53`) left the world unmoved, as the packet says. No half-landed registration exists.

**The refusal's ground, weighed.**
- A non-empty scheduled fire would append registration rows only to the PINNED checkout's `registrations.json`.
- The next CLOUD-side `write_pool` rebuilds from CLOUD inputs and drops them.
- That is a silent loss of the registration the schedule exists to make, with 13 writers of the file.
- **This seat agrees the refusal is correct.** The remedy is the invariant the CTO half names: the pool never drops a served
  record except by explicit retirement. It belongs before the registration, not after it.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S59` (`safe-merge --continue` committed foreign staged paths) | **GRADUATED** | The fix landed @`ccf2a27c6b` (0.0.0_AB_MSTR~Z, `.tools/safe-merge.sh`, +19/-1). It names this row and AMGT_HARVST `Z-S37`, and `Z-S62` records the disarm. ⚠ This seat read the fix's landing, not a conflicted drain exercising it. The first conflicted `--continue` on a shared index is its real test. |
| `Z-S62` (the disarm of `Z-S59`) | **GRADUATED** | as above |
| `Z-S63` (ARMED: a non-empty scheduled fire forks the registration ledger) | **CARRIED** -> the analysis | Graded real by the CTO half. The remedy is the round-17 invariant cell, and the registration re-signs after it. |
| `Z-S61` (the schedule registers EVIDENCED folders only; a name-only folder like Hitachi never registers) | **CARRIED** -> the analysis | widen the rule, or accept that a name-only folder is a manual act |
| `Z-W2-S11` (BLOCKING/ARMED), `Z-S3`, `Z-S6`..`Z-S9` (ARMED) | **CARRIED**, unchanged | as in v16-v18 |

## 3. FOR THE ROUND-16 ANALYSIS

1. **The invariant cell's write set is cross-project** (packet section 6): `crosswalk.py` is AMGT_RESAPP's identity module, with 13
   writers. Name the issuing project, and grade the invariant against a planted pool record, a planted retirement, and today's
   237-in/237-out round-trip. Its AC should also run one CLOUD-side `write_pool` after a pinned-side append, which is the exact
   fork `Z-S63` names.
2. **The 13:00Z start time** is the worker's call; the order named none. It is exposed as `-AtUtc`, and the trading-calendar
   question (is 13:00Z after the T-1 library settles?) belongs to the re-sign.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 1 of 1. The drain act was held on a refusal, not failed half-way. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S63` CARRIED with its remedy named; the older ARMED set CARRIED. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S19",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T23:05:00Z",
    "one_line": "L8 round 16: the held registration is held in the world -- 0 scheduled tasks match 'induction' (control: 9 Opal/AMGT tasks) and the pinned checkout path does not exist; the CTO half's refusal on Z-S63 is agreed; Z-S59 and its disarm Z-S62 graduate on the safe-merge fix @ccf2a27c6b (landing read, not exercised).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-CRPS-r-1 reads 'complete' on its LAST <status> tag.",
        "PowerShell Get-ScheduledTask | Where TaskName -match 'induction' -> 0; control -match 'opal|amgt|OPAL' -> 9; Test-Path C:\\Users\\Opal Bloomberg\\Desktop\\opal-pinned -> False.",
        "git log ccf2a27c6b: 0.0.0_AB_MSTR~Z 2026-09-29 18:24:30 -0400 'fix(safe-merge ...): the conflict state is what the MERGE could stage, not what the shared index holds -- disarms AMGT_HARVST-Z-S37 / AMGT_CORPUS-Z-S59'; .tools/safe-merge.sh +19/-1."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S59",
      "AMGT_CORPUS-Z-S62"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @c46694ffa8 asserts r-1 VALID and merged, the registration HELD on the CTO half's refusal with nothing registered and no checkout created, and Z-S62 disarming Z-S59 by the safe-merge fix.",
    "world_is": "True as read on Task Scheduler, the filesystem and git. The safe-merge fix is landed; its first real exercise is a conflicted drain on a shared index.",
    "notes": "FOR THE ROUND-16 ANALYSIS: name the project that issues the pool-never-drops invariant cell (crosswalk.py, 13 writers); its AC should include one CLOUD-side write_pool after a pinned-side append (Z-S63's exact fork); the 13:00Z start time is for the re-sign against the trading calendar."
  }
]
```
