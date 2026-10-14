# self-drive dell2-box -- tick 8 (2026-10-14 ~04:0xZ; covers 03:1xZ to 04:0xZ)   state: ARMED   cadence: 60m   job: d242bd20

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_2034Z_SELF_DRIVE_DELL2_BOX.md`.

## Open calls in scope
- **dell2's open_calls.json:** 41 rows, 7 open, 0 forks. All 7 are acts or approvals only Andrew can give. Inbox: 0 unread at 04:07Z.
- **Calls from mail since tick 7:** 7, all ruled the same turn they arrived.
  1. **D2 7490 (DB-b-190):** ruled that round 102 builds the Cottonwood adapter first. Correction taken: the 19/17 column counts were carried, not measured.
  2. **D2 7494 (wrong bucket):** agreed. 7490's build cells are held until the re-read at the `address()` prefixes, since Cottonwood
     gold already holds `account_return_daily` from 2013. The benchmark read may run.
  3. **CVO 7497 (IRPT_BCKEND round 189 slug):** round-190 analysis @6e527b13c6.
     - Cross-page call RULED: `apply_cash_rule` is also called at the fallback return (Cottonwood 215, Inflection 67, to be re-read).
     - The exemption repair is recorded. The producer census comes before the pair. One packet for one release.
  4. **AQ2 7499 / Y2 7503 (O1 blocker, D2-S93):** the door has no `ordinary_authorizer` producer, so the partner advisor was refused.
     RULED: build it next round. It admits a non-Opal viewer only when:
     - the firm comes from the verified token;
     - that firm equals the request's firm and is in allowedFirmIds;
     - the user row is active and a partner row exists.
     It carries negative tests and ships under a new never-widen pair.
  5. **Y2 7504:** yes to re-running D1-D4 and C1 as one synthetic Opal-internal viewer, as a pair addendum.
  6. **Y2 7506:** release 28 ADDENDUM 1 CTO half SIGNED on blob `909ca2c466` (verified by hash-object), @daf0a6043e.
  7. **D2 7508:** a wrong figure in the private render (returns printed at 100x) plus three wording and layout defects.
     - RULED: these are round 102's item 1, cut in the one issuance after the CVO slug, not a second issuance into round 101.

## Pivot priority
- **O1 (IRPT_ANLREQ):** ticket arms 8 of 8 PASS live. The door's answers are being proven by the internal-viewer sitting. The partner
  advisor path waits on the authorizer build and its pair, which is the critical path for FWD-1.
- **FWD-21 (IRPT_DASHBD):** round 101 drained (section check PASS: 46 of 117 filled, 6 sections PARTIAL). Round 102 waits on the CVO slug.

## Session note
The signed-in Claude account is unchanged (andrew@fideles.capital). The access token's stated expiry is 04:23Z, and a refresh token is
present, so it renews itself. No act is owed.

## Acts only Andrew can do
1. **Five client-facing approval rows:** `7773`, `3635`, `8500`, `7b45`, `fde0`. Citation: CLAUDE.md Agent Autonomy (a client-facing PROD
   page waits on his word), and the NFRA_DEVPLN approval route.
2. **His PROD analysis submission and execution ID**, row `f61b`. Citation: his ~17:0xZ word, row IRPT_BCKEND-D2-S140.
3. **Pending:** an S3 delete of the two synthetic stored inputs Addendum 1 leaves in 49financial's intake store, once the report names
   their ids. Citation: CLAUDE.md Agent Autonomy (S3 deletes need human confirmation).

`e260` is held on his own word and not raised.

## Completion test
NOT DONE: 0 of 9 active dell2 projects complete (ADVI_COTBKF on hold).

state: ARMED

## Compiler Tools
open-calls.py list, git hash-object (blob check), safe-commit.sh, MCP send/ack/check_inbox.
