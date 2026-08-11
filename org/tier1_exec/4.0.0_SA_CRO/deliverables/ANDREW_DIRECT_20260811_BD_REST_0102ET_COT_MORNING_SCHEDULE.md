# ANDREW-DIRECT (2026-08-11 ~1545Z, CRO~A terminal) — BD REST settles PRIOR TRADING DAY at 01:02 ET; cottonwood moves to a MORNING schedule pre-mdpf-floor; the D+2 framework is DEPRECATED

## VERBATIM

> "Here's the thing, Black Diamond (via API) updates their data from the prior trading day at
> 01:02 ET. So any schedule for cottonwood should just be done in the morning hours prior to mdpf
> floor. I suspect that is the nature of the issue there + this outdated concept of Black Diamond
> being 2 days behind. The reason for that, was that their csv output from their Data Mining
> Endpoint wouldnt be updated until around market close the following day, so in practice we'd
> always be 2 days behind. However, that is not the case when going through REST APIs, so that
> whole framework needs to be thrown out and this is part of how we get to syncing everything up
> unified on a morning schedule pre mdfp floor."

## WHAT THIS RULES (scope: cottonwood/BD scheduling; the vendor-availability premise estate-wide)

1. **VENDOR FACT (sovereign-stated):** BD **REST** carries day D's data from **D+1 01:02 ET**
   (05:02Z EDT). The measured "D+2" cadence was an artifact of the **CSV Data Mining export**
   channel (updated ~market close D+1) — a different channel, retired premise.
2. **DIRECTION:** the cot session→bronze→silver→assets-mirror leg chain moves to **morning hours,
   completing before the mdpf floor (13:30Z)** — exact anchor = implementing lane's choice within
   (05:02 ET, floor − chain-duration); the unified target is every firm landing T-1 in the morning
   and one floor consolidating the same day.
3. **DEPRECATED BY THIS RULING:** the D+2/tdb<=2 contract framework wherever it encodes BD
   AVAILABILITY (comp-freshness cottonwood leg notes, `BD_MAX_LAG_TRADING_DAYS=2` gate tolerance,
   the 16:30 ET anchor's rationale) — revise AFTER the retime proves, not before (the entries are
   correct descriptions of the CURRENT schedule until the schedule moves).

## MEASUREMENTS THAT BRACKET IT (mine, tonight — consistent, not independent proof of 01:02)
- Bronze sentinels: run X at 20:31Z lands snapshots as-of X-1 bday, FIRST-ASK SUCCESS nightly
  (08-06..08-10 five-for-five) — availability ≤ D+1 16:30 ET, consistent with 01:02 ET.
- The 0.6.2 D+2 evidence (EVIDENCE_cot_snapshot_asof_never_ready_20260724.md, n=14) measured
  LANDING under a once-nightly ask at the OLD 02:00Z anchor — an ask-cadence artifact, exactly as
  the ruling says; its lag-0 root-cause half (C-2/C-3) remains valid and fixed/queued.

## ROUTING
- Retime spec + implementation: AE lane (cot-pipeline session chain TF `schedule-et.tf`
  cron(30 16 America/New_York) → morning; the silver leg is already event-driven off
  `_BRONZE_COMPLETE`; the **assets-mirror leg's slot must also move pre-floor**), COO sequences in
  P2 TIMING per the ruled build order @4dbf4a0d7c.
- My COT Group W page (P2's assessment frame) amended same turn: A2 label semantics + A5 settle
  window now carry BD-REST-01:02-ET; the 4:30p-ET anchor row marked RETIME-RULED.
- vendor_asof_registry blackdiamond rows: add the channel distinction (csv-export vs REST
  availability) on next touch — DS owns the registry.

-- 4.0.0_SA_CRO~A
