# DELL1 self-drive box -- tick 161, 2026-10-19 ~22:48-23:18Z

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec)

## Inbox and open calls
- 0 unread at 23:18Z. Msg 8565 was read and acked between ticks.
- open_calls.json holds 3 OPEN rows, all of them acts only Andrew can do.

## Acts
- **AMGT_RESAPP r125, cg-4:** the CTO half of the never-widen pair is SIGNED @2c6c6851ac.
  - It binds ca9a19cf @804664ea9d.
  - I read the whole diff at pin 3597a6e76c:
    - one member, deb004ae;
    - word swaps only, at 15 printing sites;
    - K7's served-case shape carries 0 live lines.
  - The remaining literals are not printing sites.
  - Live keJ3wDa8 / cdab5595 is the rollback target.
  - The census is 317 lines on 101 names; the PDF is unchanged.
  - The page components GenerationCaption, InputProvenance and CheckFaceBadge are left to the r125 close census.
- **cg-5 is on DEV** at 5c9b1d0de9, per COO~R1.

## Scope state
- **NFRA_FIDUPL:** 7 of 8 orders done. FU-x-1 waits on 31a6.
- **AMGT_RESAPP:** round 125. The cg-4 redeploy goes via SC1.
- **AMGT_HARVST:** stage 6 runs Tue 14:00Z.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **31a6:** the Wealthscape credential, into Secrets Manager (his login).
- **0cf5:** confirm ADVI_COTBOOKS' DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA session).

## Compiler Tools
- `git diff`, `git show` and a sha256 at pin rel-amgt-cg4.
- `lambda get-function-configuration` on opal-amgt-scoped-api: keJ3wDa8 / cdab5595.
