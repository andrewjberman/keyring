# /canonical-drive NFRA_MCPMSP -- 2.0.0_SA_COO~MS -- 2026-10-01 10:0xZ-15:2xZ (site Z, host opal_bloomberg)

No cron (no ~MS row in `org/ref/LIVE_ARMS.md`). Lease FULL. Event-driven off the inbox.

| tick | project | limb | round | act fired |
|---|---|---|---|---|
| 5 (~11:1xZ) | NFRA_MCPMSP | L7 | 2 | OG-rl-1 landed daa56d81ac (~O 27770). Re-checked MS-d-2's surfaces on the new host: d2.AC3 PASS with EXPECT_KEYS=46; d2.RB READS-OK (firm 4313 B, global 1296 B) |
| 6 (~14:0xZ) | NFRA_MCPMSP | L7 | 2 | R7 met (~MI 27861: MX-r-8 e3567ce5f7). Measured e1z.AC1 unrouted=0, AC2 pre-state all allowed, AC3 control 9 of 9, role inline 5712 of 10240. Never-widen ask + COO half @1fde6055b7; CTO half @ae72f3bcbb |
| 7 (~14:1xZ) | NFRA_MCPMSP | L7 | 2 | MS-dn-1 A1 + pending @13269e4db8; handed to slot ~5 |
| 8 (~15:2xZ) | NFRA_MCPMSP | L7 | 2 | Deny APPLIED (plan 1/0/0), ledger CLOSED; ~O told so it could release the OG-rl-2 hold; drained @515e3a6cfa; issuer e1z.AC1-AC4 PASS; AC5 sha256 10 of 10; complete @08772a9c10 |

**Coordination:** 2.0.0_SA_COO~O held OG-rl-2's host deploy until our ledger closed (msg 27893), so its restart could
not land inside e1z.AC3's host read.

**Round 2:** 21 of 24 orders terminal. MS-sv-1, MS-rn-1 and MS-rx-1 wait on G-MSPID (Andrew "Not yet", 27426), so
there is no L8 compile or L10 slug yet. AC5 of MS-dn-1 goes to `3.0.0_SA_CVO~O` at L9 in that compile.

## Compiler Tools
- Ran the e1z/d2 check scripts as the issuer re-grade. Each check printed its own denominator: 20 sites / 3 files,
  9 of 9, and 22 of 22 sentinels.
- `deploy_ledger.py list` was used as the TF-act-in-flight census before the ask.
- No rail denials this hour.
