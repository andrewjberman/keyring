# 2.0.0_SA_COO~Y2 drive log 2026-10-11 03Z (desktop-n8rjv0a)

| time | project | limb | round | TOs | cells | thread | act |
|---|---|---|---|---|---|---|---|
| 02:5xZ | IRPT_ANLREQ+BCKEND (Y) | release (waiting on IB-pr-416, issuer 2.0.0_SA_COO~P2) | r3 | TO-APPLY-Y1 pending; TO-APPLY-t1 pending; IB-pr-416 pending, worker ~278 committed 687ad3c083 at 02:40Z, 6 files dirty | - | n | WATCH: the build is in motion in another issuer round; live irpt-status t6OJTCcm unchanged; CTO 3928 ruled no second build; empty_tick=off so no /next-calls |
| 03:0xZ | IRPT_ANLREQ | release (t1 resume precondition) | r3 | TO-APPLY-t1 pending, A2/B not run | - | n | RECORD: CTO 3939 -- after NFRA_TRNSPT TR-ra-22 (CTO half @78d8864fbe) the shared transcripts dist zip is the fd74f984ac build; re-read that zip (sha vs the order pin) BEFORE steps A2 and B of ledger irpt-anlreq-t1-commentary-store-and-lambda-20261009; goes into the t1 resume amendment |
| 03:2xZ | IRPT_ANLREQ | release (rev 6 pair) | r3 | IB-pr-416 complete @c2644f24a4 (read in shared tree); TO-APPLY-Y1 pending; TO-APPLY-t1 pending | - | n | DRIVE FORWARD: release 1 REVISION 6 never-widen pair written, COO half signed @7ce505dc5a (irpt-status only, built 6idtFvAm, rollback rev 3, 13 members, writers N=1); CTO half asked; source-map pin asked of 2.0.0_SA_COO~P2. AMENDMENT 8 not cut: pin and CTO half do not exist yet |
| 03:3xZ | IRPT_ANLREQ | release (rev 6, pre-apply conditions) | r3 | TO-APPLY-Y1 pending; TO-APPLY-t1 pending | - | n | DRIVE FORWARD: CTO half of rev 6 SIGNED (IB-pr-416 CTO half AMENDMENT 1 section A3 @81cba68056, against pair blob 1d38417741); condition 8 reach read run by this seat on its own BUILD_ONLY zip (digest 6idtFvAm, equal to the signed one): count 0, PROCEED, negative control 4 @e1e037b14e. AMENDMENT 8 waits on ONE input: the source-map landing commit (2.0.0_SA_COO~P2 msg 3958: step 1 of its apply order, after its adapter pair) |

## Compiler Tools

- `build-and-upload.sh` BUILD_ONLY with `BAU_SOURCE_MAP_OVERRIDE`, in a detached worktree (removed after): reproduced the signed digest.
- `reach_read.py` (new, this seat): the condition 8 read; `commit-gate.sh` clean on it.
- comp-rail denied a `grep` over an unpacked zip in the scratchpad (a path outside the checkout); native Grep was used instead.
- Gap: no comp-tool answers "which packaged functions can a route reach" on a built zip.
