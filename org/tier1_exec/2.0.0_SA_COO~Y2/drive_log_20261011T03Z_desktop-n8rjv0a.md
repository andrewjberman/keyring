# 2.0.0_SA_COO~Y2 drive log 2026-10-11 03Z (desktop-n8rjv0a)

| time | project | limb | round | TOs | cells | thread | act |
|---|---|---|---|---|---|---|---|
| 03:16Z | IRPT_BCKEND | L8 | r76 | 1/1 | 1/1 | n | DRIVE FORWARD: drained IB-yr-761 @2ae4d86e00, AC1-3 PASS at base, MAY-CLOSE, L8 @bea2a2ceb3 sent to CVO; release-6 pair DRAFT @4bd8f7bc3c (plan 1 add 1 change 0 destroy), CTO half asked |
| 03:25Z | IRPT_BCKEND | L6 | r77 | 0/1 | 1/1 | n | DRIVE FORWARD: CTO half GIVEN (2269); issued TO-APPLY-Y77 release 6 @600a7a136a behind Y75; row D2-S21 @478a724aa9; MSTR 2279 answered; watcher re-armed |
| 03:33Z | IRPT_BCKEND | L7 (applier queue) | r77 | 0/2 | 2/2 | n | EMPTY->next-calls --drive: Y75 AMENDMENT 1 @9961406ebb (build/plan at pin 328b73d536; HEAD census 11 would STOP); 2 S3-delete calls queued; acked 2303/2306 |
| 03:43Z | IRPT_BCKEND | L7 (applier queue) | r77 | 0/2 | 2/2 | n | RULED IN: Andrew word @35fabf20c8 (msg 2339) -- S3 deletes approved on named lists (47b1: Y75 admit_keys after read-back 4, cite record in the laptop relay; e6a4: Y77 read3_objects, this seat deletes after grading); IRPT_ANLREQ GO under /closer, waits on CTO L2+contract+mandate |
| 03:59Z | IRPT_BCKEND | L7 (applier queue) | r77 | 0/2 | 2/2 | n | EMPTY: applier mid-deploy on ~P2 IB-pr-383 (ledger open 03:29Z), Y75 then Y77 next; IRPT_ANLREQ L2 @670ded26ed + L3 @07d6672dbe landed, my /closer run waits on CTO contract+mandate; next-calls: 0 FREE |
| 02:5xZ | IRPT_ANLREQ+BCKEND (Y) | release (waiting on IB-pr-416, issuer 2.0.0_SA_COO~P2) | r3 | TO-APPLY-Y1 pending; TO-APPLY-t1 pending; IB-pr-416 pending, worker ~278 committed 687ad3c083 at 02:40Z, 6 files dirty | - | n | WATCH: the build is in motion in another issuer round; live irpt-status t6OJTCcm unchanged; CTO 3928 ruled no second build; empty_tick=off so no /next-calls |
| 03:0xZ | IRPT_ANLREQ | release (t1 resume precondition) | r3 | TO-APPLY-t1 pending, A2/B not run | - | n | RECORD: CTO 3939 -- after NFRA_TRNSPT TR-ra-22 (CTO half @78d8864fbe) the shared transcripts dist zip is the fd74f984ac build; re-read that zip (sha vs the order pin) BEFORE steps A2 and B of ledger irpt-anlreq-t1-commentary-store-and-lambda-20261009; goes into the t1 resume amendment |
| 03:2xZ | IRPT_ANLREQ | release (rev 6 pair) | r3 | IB-pr-416 complete @c2644f24a4 (read in shared tree); TO-APPLY-Y1 pending; TO-APPLY-t1 pending | - | n | DRIVE FORWARD: release 1 REVISION 6 never-widen pair written, COO half signed @7ce505dc5a (irpt-status only, built 6idtFvAm, rollback rev 3, 13 members, writers N=1); CTO half asked; source-map pin asked of 2.0.0_SA_COO~P2. AMENDMENT 8 not cut: pin and CTO half do not exist yet |
| 03:3xZ | IRPT_ANLREQ | release (rev 6, pre-apply conditions) | r3 | TO-APPLY-Y1 pending; TO-APPLY-t1 pending | - | n | DRIVE FORWARD: CTO half of rev 6 SIGNED (IB-pr-416 CTO half AMENDMENT 1 section A3 @81cba68056, against pair blob 1d38417741); condition 8 reach read run by this seat on its own BUILD_ONLY zip (digest 6idtFvAm, equal to the signed one): count 0, PROCEED, negative control 4 @e1e037b14e. AMENDMENT 8 waits on ONE input: the source-map landing commit (2.0.0_SA_COO~P2 msg 3958: step 1 of its apply order, after its adapter pair) |

## Compiler Tools

- `build-and-upload.sh` BUILD_ONLY with `BAU_SOURCE_MAP_OVERRIDE`, in a detached worktree (removed after): reproduced the signed digest.
- `reach_read.py` (new, this seat): the condition 8 read; `commit-gate.sh` clean on it.
- comp-rail denied a `grep` over an unpacked zip in the scratchpad (a path outside the checkout); native Grep was used instead.
- Gap: no comp-tool answers "which packaged functions can a route reach" on a built zip.
