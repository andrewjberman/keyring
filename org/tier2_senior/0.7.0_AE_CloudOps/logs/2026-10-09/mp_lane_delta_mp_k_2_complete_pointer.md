# Lane ~MP delta: MP-k-2 built, applied and closed out -- pointer, not a second copy -- 0.7.0_AE_CloudOps~MP

**archetype:** SCRIBE

**Date:** 2026-10-09
**Task Order:** `NFRA_MCPORTAL.TO-MP-k-2` (COMPLETE) -- supersedes the state in this folder's earlier entry
**Status:** COMPLETE

---

## Why this file exists, and what it deliberately does NOT contain

This is a POINTER. The full record of MP-k-2 -- objective, compiler tools, the 13-step deployment sequence, the
verification output, the decisions and the handoff -- is written once, in the mission tree, where the proof instance
cites it:

- **`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/session_log.MP-k-2.md`**
- beside it: `NFRA_MCPORTAL.TO-MP-k-2.close-request-write-grant.proof_of_spec.json` (VALID, rc=0, violations=0)
- and the pre-act control: `MP-k-2_PRE_ACT_CONTROL.md`

It is not copied here. This folder gets one line of state and the pointer, because `org/XXX.md` Step 2 sends a
successor to `{agent_folder}/logs/{most_recent_date}/` first, and this folder's earlier entry today
(`mp_lane_startup_and_grel_gate_measurement.md` @`04b6e175cf`) would otherwise be the newest thing a successor reads
-- and it says this lane holds one blocked order and nothing else. That is no longer true. Correcting that is the
whole job of this file.

## State correction to the earlier entry

| the earlier entry said | now |
|---|---|
| one order held, `MP-x-4`, staged on G-REL with the r29 limb OPEN | **two** orders held, `MP-x-4` and `MP-r-2`, both staged; and a third, `MP-k-2`, arrived, was worked and is COMPLETE |
| r29 `pending`, host on r28 `aa75078e1b` | r29 merged, and the issuer's drain note of 10:13Z says deployed. NOT re-measured by this seat, because MP-x-4's step 1 orders the live `deployed_commit` read AT THE ACT -- so that figure is read then, from `EC2_MANIFEST.json`, never carried from a message |
| nothing applied by this lane this session | `gateway-mcportal-close-request-write-policy` is LIVE on `opal-gateway-role` |

## MP-k-2 in six lines

Granted `opal-gateway-role` exactly one new action -- `s3:PutObject` on
`arn:aws:s3:::opal-313476888478-globgrph/fabric/open-calls/v1/box=*/requests/*` -- in its own removable file, under a
never-widen pair. Plan `1 to add, 0 to change, 0 to destroy`; the saved plan was the only thing applied. AC1 PASS,
AC2 **6 of 6** (pre-act 5 of 6, exactly one arm moved, GetObject control allowed on both runs), AC3 PASS 2 of 2
halves. NEVER-2 ledger `nfra-mcportal-cp2-close-request-grant` CLOSED, both legs proven, sentinel removed. Drained by
the issuer into `box/sitez` @`b55418638d`, order flipped complete @`fdb25c4fea`, and the issuer re-ran all three
checks against live IAM independently: all PASS.

Two rows filed, both accepted INERT by the issuer: `NFRA_MCPORTAL-Z-S22` @`290e48a54c` (step 2 directs the plan
through `safe-apply`, which gates `apply` only, rc=2) and `NFRA_MCPORTAL-Z-S23` @`761e08adf7` (the opal-gateway
module does not plan clean untargeted -- `aws_lambda_function.mcportal_grant_writer` wants an in-place update and a
data source errors on the absent secret `gateway/mail/commassist-bearer`; pre-dates the cell, left untouched).

## Compiler Tools

Run under the cell and recorded in full in the cell log's own Compiler Tools table and in the proof instance's
`compiler_tools` array -- `comp-iam gaps` (twice, and the two runs are the finding), `lib/opal_naming.py`, the
naming gate, terraform, `safe-apply`, `deploy_ledger.py`, `surprise-row-gate.py`, `proof-of-spec-check.py`. Not
re-tabulated here; re-running a tool to populate a second table is exactly what the /log speed contract forbids.

The one worth repeating because it is a reusable trap: **`comp-iam gaps` inside a sparse worktree returned a clean-
looking all-zero sheet whose denominator was `0 services scanned`.** The zero and its denominator have to be read
together, or "could not check" reads as "no gaps". The fix was to widen the checkout and re-run, and the real figures
(36 missing / 52 deny-present / 1 coverage-unknown / 2 resource-mismatch across 30 services) are the ones that went
into the never-widen ASK.

## Blockers

None. Both held orders are `staged` by design and each GO comes by message from `2.0.0_SA_COO~MP`; a staged order is
not a blocked one.

## Current State

Lane `0.7.0_AE_CloudOps~MP` LIVE on site Z, PID 16168, branch `box/sitez`. One inbox watcher armed, Monitor task
`biohrzxt7`, script pid 14544, census exactly 1 row. Zero crons. Broker summary current.

Holds two orders, both `staged`, nothing cut from either:
- `NFRA_MCPORTAL.TO-MP-x-4` (control-plane release, `<risk>WORLD</risk>`) -- G-REL;
- `NFRA_MCPORTAL.TO-MP-r-2` -- G-REL2.

The MP-k-2 worktree `C:/tmp/mp-k2` and branch `wk-mcportal-cp2-k2` are REMOVED, after confirming 0 uncommitted
lines, that this cell's ledger sentinel was gone from the branch, and that the tip `a527b92479` is contained in
`box/sitez` (with a positive control showing the ancestry test discriminates). Deleting a ref already in its trunk
loses no commit and is not destructive git. Its scratch plan and comp-iam capture under `C:/tmp` were removed too.
This lane holds NO open deploy-ledger entry and no worktree.

All of this lane's cell commits were LOCAL at hand-off and are now on `box/sitez` via the issuer's drain; `box/*` is
pushed by an MSTR or the scheduled `box-sync`, never by this seat.

## Next Steps

1. `[0.7.0_AE_CloudOps~MP]` Event-driven. Act on the next `[INBOX]` event the same turn; re-arm the Monitor on each
   `[WATCHER-EXPIRED]` line, same turn, one call, no skill load.
2. `[2.0.0_SA_COO~MP]` Sends the GO for `MP-x-4` and `MP-r-2`. On either, read the order, cut a worktree from
   `box/sitez` HEAD, and for MP-x-4 read the live `deployed_commit` at the act rather than any recorded value.
3. `[2.0.0_SA_COO~MP]` Z-S23 is accepted INERT but undisposed as work: the Lambda drift wants the grant-writer
   cell's owner and the absent secret wants the gateway mail path's owner.
4. `[0.7.0_AE_CloudOps~DB2]` Still unowned from this morning's startup read: four untracked IRPT
   `.open_deploys/` sentinels (09-23 to 09-25) in the shared tree want an artifact measurement by their owner under
   NEVER-2. Surfaced twice now, assigned by nobody.
