# /self-drive dell1 box open calls -- tick 17 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~15:26Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. Cron 4e032862 (:17). **state: ARMED**

## Measured

- **Box list:** rows=76, **open=2**:
  - `c822`: a client-facing approval, HELD for Andrew;
  - `2fc4`: ADVI_FIRMBKTS M02 fence roles, CROSS-BOX, escalated this tick as **XA-20261014T152700Z-54ff**. REC: census first, `exemptions.json` rows only for roles in use; `role/inf-*`
    refused.
- **Cross-adjudications:** 16 RULED and 1 pending (54ff).
- **Inbox:** 0 unread. Msgs 5609 to 5627 since tick 16 were acked and acted on.

## Acts since tick 16

| item | ruling / act | record |
|---|---|---|
| CVO 5609: RESAPP round-105 AIFILL slug (un-parked), FWD-41 NOT MET | Answered by the existing FWD-41 ruling. Seven defects map to round 106; **(g) recency/cross-block and (h) clause integrity go to round 107**. The hold stands | `AMGT_RESAPP/ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md` ADDENDUM 1 @5caf97b965 |
| `~V1` 5611: RIVALS r30 deploy pair | **CTO half SIGNED with C1:** an inferred row can double-count a split the vendor already reports. ARMED row D1-S16, plus a round-31 precedence cell | `ETFS_RIVALS/ledger/NEVER_WIDEN_R30_DEPLOY_CTO_HALF.md` @35d1f02bc3 |
| `~V1` 5614: D1-S16 disarm | Detect-and-void **accepted**, timed before the readers (10:50Z and 12:50Z), not the hourly tick | msg |
| Call `f6f8` (CANON CN-h-1 naming gate) | Escalated as XA-c328 and RULED (3) by the laptop: a registry row, not R20. **CLOSED** with `--xadj` after MSTR's box pass. The CRO then MEASURED that `key_rulings` cannot clear a typed literal, so it was executed as a `legacy_addresses.json` row (@81453d51cf). The builder was exercised: it returns the live prefix. The laptop was told via MSTR | `org/critical_paths/cross_adjudication/20261014T1503Z_XA-20261014T145816Z-c328.md` |
| Call `2fc4` (FIRMBKTS M02 fence) | Escalated as XA-54ff | above |

**Instrument note:** the c328 ruling named a registry file whose reader the gate never reaches for a typed literal. The CRO measured that before writing, and no wrong row
landed. The ruling's substance (a registry row, no R20, the key verbatim) held, so the change of file was this seat's to make, and it was reported back to the ruler.

## Completion test

Box scope: **NOT DONE**. The stop is Andrew's stand-down. REACHABLE calls: 1 at cross-adjudication. 1 is HELD for an act only Andrew can do.

## ACTS ONLY ANDREW CAN DO (cited)

- **Be at the dell1 console for the FWD-11 restart at 21:00Z (17:00 ET)** (msg 5483).
- **Approval c822 and its PROD promote** (`/positioning` is partner-facing; CLAUDE.md Agent Autonomy).
- **The MDPF_SECCLASS client-facing BD Mix PROD push** (CLAUDE.md push law).
- **One session from his own work Claude through the gateway** (NFRA_OPLGTW FWD-21).
- **Lifting the ASTN FT hold** ("Dont attempt FT until I return").
- **Optional:** a fresh WSJ/Barron's sign-in (it un-parks HARVST's Z-S121; call 8c66).
- **Later, at the moment it runs:** the Door 6 marker's S3 delete.

## Compiler Tools

`open-calls.py list/close --xadj`; `xadj.py open/show/list`; `lib/opal_naming.legacy_address` (exercised); reads of `key_rulings.json`, `legacy_addresses.json`, `exemptions.json` `_about`;
a background wait on the record's arrival before the close. **Worked:** the CRO measured the gate before writing, which caught a ruled route that could not work. **Gap:** a cross-box
ruling cannot see which registry file the gate actually reads for a given literal type. Any ruling that names a registry file should say "or the file the gate reads for this type".

-- 1.0.0_SA_CTO~DELL1
