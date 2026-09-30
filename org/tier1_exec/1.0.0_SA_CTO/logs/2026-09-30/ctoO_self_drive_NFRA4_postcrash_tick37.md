# /self-drive NFRA four -- ticks 36-37: Andrew's three answers, the naming-gate gap, MX-r-6 v2 signed (1.0.0_SA_CTO~O, site Z, 2026-09-30 12:5xZ-13:3xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4
- **Previous log:** tick 35 @bd3b7a3369.

## Carried tick line

- tick 36 12:50Z: 16 of 187 open. The MX-r-6 re-cut was pending. 0 calls.

## Acts and receipts since tick 35

1. **Andrew-direct ~13:0xZ,** VERBATIM: "yes thats fine on naming exception. Regarding schwab, sure. advi tool, what not
   yet are you referring to? but yeah certainly whatever needs to be lifted should be lifted".
   - Record @1eba868308. It gives R20 yes for the two read-only legacy keys, allows one Schwab grant widening to
     `dim_transaction`, and lifts the platinum/advi NOT YET.
   - Relayed to 2.0.0_SA_COO~MI. The issuer amended MX-t-12 A1 and MX-r-6 A5 @d4753af0d2.
2. **The naming-gate gap:** `.tools/naming-gate.py:1413` and `:1444-1446` refuse NEW literals before any waiver, and
   the gate reads no R20 entry.
   - Asked of laptop 1.0.0_SA_CTO (the gate owner) and 4.0.0_SA_CRO (register rows X11 and X12) via 0.0.0_AB_MSTR~Z:
     bus 22edd112, acked by laptop MSTR at 13:18Z (fc0cc999), then relayed to fresh laptop sessions after the 07:52Z
     reboot.
   - Laptop's earlier relay (msg 27167, bus ddb1b296 from 03:45Z, late because this site's bus consumer was unarmed)
     put the `platinum/etfs` ETFS_CANON remediation row on HEAD @fd3b3b7bf2.
   - COO~MI's gate run on MX-t-10's frozen 03a19ac282 still reads REFUSE 3, NEW OUT-OF-PATTERN (msg 27174).
   - MX-t-10, MX-t-13 and MX-r-7 stay HELD on the gate edit.
3. **MX-r-6 v2: G-A PASS and CTO half SIGNED @16998169d5** (ask @17259505a2, msg 27178).
   - This seat read the live base ITSELF: in S3 `ec2/opal-gateway/`, `-latest` has the same ETag as `288fa78c93`
     (`be161c825e...`), and no key is newer.
   - The tree `bf741bd45a` is equal at `63d6094823` and `2e2254156e`.
   - The diff against live is 21 files, with no MCPMSP file among them. `tenant_registry.py` and `firm_role.py` are
     byte-identical, and `FIRM_ROLE_ARNS` is kept.
   - The half is conditional on the targeted plan reading 0/1/0, and it covers the one A5 grant. 3.0.0_SA_CVO~O's half
     is still owed.

## Measured (13:2xZ)

- **Inbox:** 0 unread.
- **Open TOs:** 16 of 187.
  - NFRA_OPLGTW 4 of 54.
  - NFRA_OPALAI 4 of 35.
  - NFRA_MCPORTAL 2 of 18.
  - NFRA_MCPINDEX 6 of 80.
- **Completion:** 0 of 4. 1 REACHABLE (MCPINDEX), 3 UNREACHABLE (acts per the tick-11 log).

## Calls

No open calls in the four projects (ticks 36-37). The naming-gate edit is an act owed by another fabric's gate owner.
It is not a call.

## Acts only Andrew can do (each cited)

- **R20:** GIVEN. **Schwab grant widening:** GIVEN. **advi hold:** LIFTED.
- **Unchanged:**
  - G-ACCT step 5 and G-AUTH (his login or spend);
  - MCPORTAL G-2ND and G-CLOSE;
  - OPLGTW G-D and Part D;
  - NFRA_MCPMSP G-USER, G-IT-INF, G-ADVISOR, G-FIRM and G-KEY.
- G-C is external, at Opal IT.

## Compiler Tools

- `.tools/aws s3api list-objects-v2` over the artifact prefix, sorted by LastModified (the live-base read).
- `git rev-parse <pin>:infra/aws/ec2/opal-gateway`, `git diff --stat 288fa78c93 63d6094823`, and blob equality on the two
  MCPMSP files.
- Last-tag `<status>` census over the four projects' task-order files.
