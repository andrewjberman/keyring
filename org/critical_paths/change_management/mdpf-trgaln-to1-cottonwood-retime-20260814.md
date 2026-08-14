# DEPLOY LEDGER — MDPF_TRGALN.TO-1 Cottonwood retiming (§3 rows 4/5/7)

**Opened:** 2026-08-14T05:20Z by 0.7.0_AE_CloudOps (deploy-start; NEVER#6)
**Status:** OPEN
**GO:** 2.0.0_SA_COO 051505Z citing proof_TO-0.json rev 1 @772787a1e1 VALIDATED
**PRD:** docs/architecture/MDPF_TRGALN_PRD.md v1.1 @f50ee7223b §3 rows 4/5/7

## Legs (all must close or roll back in-session)

| Leg | Root | Resource | Edit | Status |
|---|---|---|---|---|
| 1 | cot-pipeline | cot-bd-session-daily-et | cron(30 16)→cron(30 7) ET (schedule-et.tf:88) | OPEN |
| 2 | opal-assets | opal-assets-ingest-mirror-cot-daily-et | cron(30 18)→cron(45 7) ET (mirror.tf:155) | OPEN |
| 3 | opal-assets | opal-assets-silver-blackdiamond-sweep-daily | cron(0 5Z)→cron(0 13Z) (silver.tf:162) | OPEN |

Both opal-assets legs ride ONE targeted apply (-target mirror_cot_et + silver_sweep["blackdiamond"];
plan READ; daily-aua row = dirty plan = STOP).

## Cutover-gap statement (pre-apply, per TO-1)

- Row 4: old fire 16:30 ET has NOT yet run today (apply ~01:20 ET); new 07:30 ET is later today →
  exactly ONE fire today at the new time. No skip, no double-run.
- Row 5: old 18:30 ET not yet run; new 07:45 ET later today → ONE fire at new time. No skip/double.
- Row 7: old 05:00Z ALREADY FIRED today (~05:00Z, pre-apply); new 13:00Z will also fire today →
  DOUBLE-RUN today (05:00Z + 13:00Z), acceptable: idempotent backstop sweep (TO-1 expected shape).

## Interaction statement (TO-1/TO-2 mirror caveat)

The mirror is NO LONGER all-rows: handler reads `event.get("firm")` (opal-assets-ingest-mirror
handler :400) and TF passes firm-scoped inputs (mirror.tf: cot scheduler input {"firm":"cot"},
inf rule {"firm":"inf"}). The row-5 (cot) retime therefore does NOT move the inflection mirror
leg; row 6 (inf mirror) moves separately in TO-2. cot-bd-session-trigger is a FOUR-entry function
(cot-bronze-complete, cot-session-complete, cot-silver-complete event rules + this scheduler);
this retime moves ONLY the scheduler entry.

## Rollback

Same-window cron revert: re-apply prior strings (verbatim in the table above) via the same
targeted mechanics. No data mutation in this deploy — schedule strings only.

## Close (checked only when TRUE, with evidence)

- [ ] safe-commit hash: ______ ; plans READ (no daily-aua row); applies landed both roots
- [ ] Post-apply 0-diff re-plans clean; live APPLIED reads == §3 targets verbatim (3/3)
- [ ] Tags pushed --follow-tags: ______
- [ ] CLOSED at: ______ with proof_TO-1.json commit: ______
