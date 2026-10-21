# DELL1 self-drive box -- ticks 221-222, 2026-10-21 ~05:19-05:49Z (hour floor; the G switch scopes neither the list nor the exports -- design fork to the CRO; backfill driven at the rep level)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 05:49Z. Acked since tick 220: 8989, 8991.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool.

## Acts and rulings
- **Ruled** (04:53Z, msg to P1): the switch scopes the DOWNLOADS, not the list; probe v3 = switch + account.txt for three ordinals
  against the 5009-row file. P1 cut FT-s-10 (@83a888fca62), REPAIR 1 (refused-switch handling) and REPAIR 2 (an explicit day
  argument after the first run queried the just-rolled New York day and read elements=0).
- **Probe 2G-v2** (NFRA1 @941e79283e9, 05:46-05:47Z, one sign-in, 11 requests, restore ok): ordinals 0, 1 and 15 all list the SAME six
  export ids (sha8 d79c7806) and account.txt is BYTE-IDENTICAL (3,794,367 B, 5009 rows, sha8 94a0f611, the landed file). With
  2Pv2 (accountList available=5204 under all 31), the G switch scopes neither the account list nor the exports: the exports are
  rep-level and the switch is a view.
  - **Design fork, routed to the CRO** (Step 1 table): asked `4.0.0_SA_CRO~FIDELITY` for two reads from the HARs and the UI bundle,
    no sign-in: (1) which calls change with the G and whether any returns a per-G account set (the membership the split needs);
    (2) whether the export wizard offers a per-G scope (account group, branch, rep) so a per-G profile could exist. I rule the
    split mechanism on that record. Nothing goes to Andrew until the mechanism is known; the only conceivable act of his is the
    export-profile one already listed as conditional.
  - **Ruled** (05:50Z, msg to P1): HOLD further G probes (no sign-ins on this question). Deliverable 2 does not wait: run backfill
    probe 1 (FT-s-7's adapter, the CRO's date-range method) at the rep level under the cap, landing by content date under
    `fidelity/alongside/bronze/`; the per-G split of the backfill follows the daily's mechanism once found.
- **AMGT_HARVST:** no change; co-7 stage 7 waits for its apply span.

## Scope state
- **NFRA_FIDUPL:** FT-s-8, FU-s-11, FU-x-1 pending (plus FU-s-10's rolling deliveries, 25 so far). 19 objects under
  `fidelity/alongside/bronze/` (6 data, 13 run records). Rules ENABLED (first fire 09:45Z). No firm prefix; no backfill
  earliest-date row yet. The stop condition's "split to firms" half is blocked on the mechanism the CRO is reading for.
- **AMGT_HARVST:** round 100, co-7 stage 7 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated or per-G Fidelity export profile, only if the wizard's scope or date field cannot be automated
  (CRO 8916; the mechanism read pending).

## Compiler Tools
- `git show` of the probe records (counts and hashes only).
- `list-objects-v2` (counts only).
