# Lane ~MP delta: MP-x-4 is PREPPED and HELD with a live ledger entry -- read this before touching the gateway -- 0.7.0_AE_CloudOps~MP

**archetype:** SCRIBE

**Date:** 2026-10-09
**Task Order:** `NFRA_MCPORTAL.TO-MP-x-4` (`pending`, `<risk>WORLD</risk>`) -- act HELD, nothing deployed
**Status:** IN PROGRESS

---

## Why this file exists

The previous entry in this folder (`mp_lane_delta_mp_k_2_complete_pointer.md`) says this lane holds
`MP-x-4` and `MP-r-2` "both staged". That is now materially wrong, and a successor who read only that
would miss the thing that matters most: **there is a LIVE deploy-ledger entry for a WORLD-risk gateway
release, held open on an external gate, with this seat named as its author.** Under NEVER-2 an entry a
device left open proves only that THIS device saw no completion, so the next reader must measure the
artifact before acting on it. The measurement is already done and recorded; this file points at it.

## The one thing to know

**Nothing has been deployed.** No artifact was built or uploaded, no SSM deploy was dispatched, the
gateway was not restarted. The live `deployed_commit` is still NFRA_OPLGTW r29 and
`app/admin_fabric.py` is still ABSENT from `/opt/opal-gateway/app` (confirmed on three separate SSM
reads). Service `active`, MainPID `857046` unchanged across every pre-act read.

## State

| thing | where it is |
|---|---|
| Ledger entry | `org/critical_paths/change_management/20261009T1414Z_nfra-mcportal-r5-control-plane-release_deploy_completion.md` -- **HELD-PRE-APPLY** @`b8fc617e2e`, `not-started=['L1','L2','L3','L4']`, gate `external/` OG-ap-4's ledger close, re-read event = the issuer forwards that close commit |
| The full pre-act record | `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/MP-x-4_PRE_ACT_RECORD.md` @`0b4deae4f4` -- census, four cold samples, rollback, halt-gate pre-flight, tool surface BEFORE. **The issuer ratified this file as step 4's record** (msg 32819); post-act proofs go in it too |
| Release tree | `C:/tmp/mp-x4-rel`, branch `rel-nfra-mcportal-r5-control-plane` @`d1bc9dfbe3` -- cut from `91811b648a`, MP-x-1 `06bfb80b54` cherry-picked, `mcportal_commit` = `d60b4e0`. Stays local and unmerged, like every prior gateway release branch |
| Trunk tree | `C:/tmp/mp-x4`, branch `wk-mcportal-r5-x4` -- carries the ledger and will carry the manifest RECORD, per the r29 precedent (`91811b648a` lives only on `rel-nfra-oplgtw-r29`; its ledger and manifest landed on the trunk @`5f1400c4a2`) |

## Why it is held

Issuer msg 32796: `1.0.0_SA_CTO~Z` (msg 32788, relayed by `2.0.0_SA_COO~O` msg 32795) put NFRA_OPLGTW
`OG-ap-4` -- an env-only 4-meeting allowlist with all halves signed -- AHEAD of MP-x-4, because only one
gateway release is in flight at a time. Preparation was expressly permitted and is complete.

The HOLD arrived at 14:19:14Z; the entry had been opened at 14:14:25Z @`fe4b132e3d`, about five minutes
earlier. The instruction landed after the fact, not against it, and the issuer was told so plainly.

## What MUST be redone at the act, not reused

**The recorded base `91811b648a` will be STALE.** OG-ap-4 lands first, so the live ref becomes r29 plus
the allowlist value. Step 1 already requires reading `deployed_commit` from `EC2_MANIFEST.json` AT THE
ACT, so:

1. re-read the live `deployed_commit` (never carry a value from a message or from this file);
2. re-cut the release tree from that base and re-apply the cherry-pick;
3. re-run the census against it. OG-ap-4 is env-only with no code change, so the four-file census is
   EXPECTED to hold -- that is a prediction, and it gets measured, not assumed;
4. re-read the cold `_compute(6)` on the new base before the cutover;
5. the rollback target changes with the base: the versioned artifact key for the NEW live commit, not
   `opal-gateway-91811b648a.tar.gz`, and never `latest` (the act overwrites `latest`).

## Two findings from the prep, both already routed

- **`NFRA_MCPORTAL-Z-S24`** @`b23823ad78` (BLOCKING/ARMED as filed): `deploy_ledger.py hold` regenerates
  the entry and silently discards prose appended to it -- rc=0, stdout says OK, and a following `check`
  still reports the entry healthy. It deleted 115 lines of the required record. **DISARMED for this
  project by `Z-S25`** @`c69b8129d7` (verified at the trunk: `adjudicates: ['NFRA_MCPORTAL-Z-S24']`),
  and the tool defect itself is routed to `0.0.0_AB_MSTR~Z`. Z-S24 still reads ARMED in place, which is
  correct -- a surprise row is superseded by a new citing row, never edited.
  **Operational consequence that outlives the row:** never put evidence only in a ledger entry.
- **The GO's halt-gate remedy is aimed at the wrong check.** It said to materialise
  `org/tier2_senior/0.7.0_AE_CloudOps~MP`; that folder exists nowhere in the repo (0 paths under it), yet
  the gate ADMITS (`halt-gate-check.sh` standalone from the release worktree: rc=0). Reason:
  `halt_gate_validate_serial` matches the BASE by substring (`*"$base"*`) over `org/tier*_*/*/`, and this
  worktree carries 20 folders matching `0.7.0_AE_CloudOps`; the second check, `lane-no-inbox`, reads the
  SHARED root's `org/mcp/inbox/0.7.0_AE_CloudOps/~MP`, which exists. The real requirement is "materialise
  at least one folder matching the BASE" -- a no-cone `org/` list satisfies it. Creating the lane folder
  would add a directory the tree does not have.

## Compiler Tools

Run under the cell; recorded in `MP-x-4_PRE_ACT_RECORD.md` rather than re-tabulated here. The reusable
one: a cold figure measured ONCE is not a figure. Four samples of the same read spanned 13.615-16.767 s
(23% of min), and the issuer's single earlier reading of 21.3 s sat above all four while scanning FEWER
records -- so a one-sample pass against a 30 s bar would have been luck either way.

## Blockers

**BLOCKED (evidence-cited), and correctly so:** the act waits on OG-ap-4's ledger close commit, forwarded
by `2.0.0_SA_COO~MP`. Owner is the issuer; this seat does not chase OG-ap-4. `MP-r-2` is also held with
this lane, `staged`, carrying AMENDMENT 4 (it adopts the pre-act-record pattern up front); its GO comes
by message.

## Current State

Lane LIVE on site Z, PID 16168. Watcher armed, Monitor task `bg7gt1ka1`. Zero crons. Two worktrees live
(`C:/tmp/mp-x4-rel`, `C:/tmp/mp-x4`) -- **do not remove either**: one holds the prepared release, the
other the held ledger. One HELD deploy-ledger entry, named above.

Push state, measured by `ls-remote` with a self-ancestry positive control: `b23823ad78` (row Z-S24) is ON
ORIGIN; `d1bc9dfbe3`, `fe4b132e3d`, `ca9b6c05f0`, `b8fc617e2e`, `0b4deae4f4` are **LOCAL**. `box/*` is
pushed by an MSTR or the scheduled `box-sync`, never by this seat.

## Next Steps

1. `[2.0.0_SA_COO~MP]` Forwards OG-ap-4's ledger close commit. That is the only thing the act waits on.
2. `[0.7.0_AE_CloudOps~MP]` On that message: release the hold
   (`deploy_ledger.py hold --slug nfra-mcportal-r5-control-plane-release --release`), then do the five
   re-dos above IN ORDER before any upload.
3. `[0.7.0_AE_CloudOps~MP]` Then the act, `/health` inside 90 s or the named rollback AT ONCE, tool
   surface AFTER (BEFORE was 66, difference must be empty), manifest record on `wk-mcportal-r5-x4`, close
   every leg with proof, commit the close BEFORE the AC reads, then AC1/AC2/AC3.
4. `[0.0.0_AB_MSTR~Z]` Holds the `deploy_ledger.py` prose-loss defect (routed by the issuer).
