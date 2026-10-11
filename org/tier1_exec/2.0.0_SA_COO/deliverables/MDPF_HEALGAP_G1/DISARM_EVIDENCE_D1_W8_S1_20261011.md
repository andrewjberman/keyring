# Disarm evidence: MDPF_HEALGAP-D1-W8-S1 (ARMED, BLOCKING) -- `2.0.0_SA_COO~G1`, 2026-10-11 ~05:3xZ

**Row:** `MDPF_HEALGAP-D1-W8-S1`, `org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md` (surfaced by
`0.9.0_WK_MDPF_HEALGAP~8` at 04:04:00Z; `disarm_owner` = `2.0.0_SA_COO~G1`).
**Hazard as filed:** HG3-t11-AC2's checker could not fail its failed-read arm, so a document that skips the pull on a failed guard
read still printed `SSMGUARD-OK` and AC2 was no evidence for that arm.

## The act that answers it

- **Fix (issuer, in its own decomposition):** `e844a20917` amends `R3_CHECKS/hg_t11_assetdim.py` on `box/dell1`: the failed-read arm now
  tests the PULL call (the `RUNUSER ... pull_bd_asset_dim_rest.py pull` line), not the substring the staging line already wrote. It is the
  file's last commit at HEAD. `8e197ccf1e` is the same correction carried onto the worker branch; `git merge-base --is-ancestor` reads
  both as ancestors of HEAD.
- **Merged under it:** `8e130c8c55` (HG-t-11 worker merge, proof VALID after the issuer corrected the check).

## Measured at 2026-10-11T05:3xZ against the checker at HEAD

| input | invocation | printed | rc |
|---|---|---|---|
| the real document `infra/aws/ssm/opal-bd-asset-dim-download.json` | `python R3_CHECKS/hg_t11_assetdim.py --ssm` | `SSMGUARD-OK guard between staging and pull; exists -> skip + shutdown armed; read failed (rc 1,2) -> download runs` | 0 |
| mutant: the one guard test `if [ $GUARD_RC -eq 0 ]` changed to `-ge 0` (a failed read taken as exists) | `HG_T11_DOC=<mutant> ... --ssm` | `SSMGUARD-BAD guard read FAILED (rc 1) but the pull did not run ...; ... (rc 2) ...` | 1 |
| mutant: both skip-path `shutdown -h +2 &` lines removed | same | `SSMGUARD-BAD guard read OK but the shutdown was not armed` | 1 |

The first mutant is the worker's own failing case (row evidence line 2): before `8e197ccf1e` it printed `SSMGUARD-OK` rc=0. Now it
prints BAD rc=1, so the failed-read arm discriminates. Denominator: the guard test occurs once in the document (count printed 1).

## What the world holds

The document the checker grades is the one that is live: SSM `opal-bd-asset-dim-download` DefaultVersion 6, `Hash` equal to the sha256 of
the repo file (change-management entry `healgap-r3-act3-asset-dim-reattempt-20261011`, legs L1-L3 closed `fff25caf2f`). The row's
`world_is` ("the document itself runs the pull on rc 1 and 2") stands unchanged.

## What this does not do

This seat does not write the clock. `disarm.state` ARMED -> DISARMED is the CVO's to write (R-15) at the round-3 compile. Residual,
named: the guard's behaviour on a real failed read is graded by the document's own shell under stubbed tools, never by a live read
failure; the live negative arm is the first day the 22:10Z fire fails on a lapsed session.
