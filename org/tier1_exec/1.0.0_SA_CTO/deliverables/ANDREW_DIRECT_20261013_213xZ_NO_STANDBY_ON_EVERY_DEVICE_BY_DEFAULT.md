# ANDREW DIRECT -- every device stays on: no standby, set by default (2026-10-13 ~21:3xZ)

**Channel:** Andrew at the `1.0.0_SA_CTO~Z` terminal (site Z). **VERBATIM:**

> give me the command that keeps this device on, no standby. I want to make sure that all devices have this command set by default.

## The command (Windows, the active power plan)

```powershell
powercfg /change standby-timeout-ac 0
powercfg /change standby-timeout-dc 0
powercfg /change hibernate-timeout-ac 0
powercfg /change hibernate-timeout-dc 0
powercfg /setacvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 0
powercfg /setdcvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 0
powercfg /setactive SCHEME_CURRENT
```

- `0` means never for the four timeouts.
- `LIDACTION 0` means "do nothing" on lid close; it matters only on a laptop.
- The display may still turn off; that is not standby.
- The settings bind the ACTIVE plan only. A box switched to another plan must have them re-applied.

**Read-back:** `powercfg /query SCHEME_CURRENT SUB_SLEEP`. Sleep after, Hibernate after and Allow hybrid sleep each read
`0x00000000` on AC and DC.

## State per box

| box | state |
|---|---|
| site Z | **Already applied.** Read by `1.0.0_SA_CTO~Z` ~21:3xZ: active plan Balanced (381b4222-...); Sleep after, Allow hybrid sleep and Hibernate after all read 0x00000000 on AC and DC. Lid action not read (desktop) |
| laptop | **Unread.** Andrew's 2026-10-06 word applied sleep-never on AC only (`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261006_035xZ_OPEN_CALLS_1A_KEEP_DURATION_LADDER_LOCK_2_BLOCKED_3A_4A.md` item 4); DC, hibernate and lid were not set by that word |
| dell1, dell2 | **Unread** |

## Owner

Device infrastructure is MSTR's (CLAUDE.md rule 32). Each box's MSTR applies the command and reads it back.
`0.0.0_AB_MSTR~Z` relays this record to the laptop, dell1 and dell2 MSTRs. "By default" means part of each box's
standing provisioning, so a rebuilt or new box gets it too; where that step lives is the MSTRs' call.

-- recorded by 1.0.0_SA_CTO~Z
