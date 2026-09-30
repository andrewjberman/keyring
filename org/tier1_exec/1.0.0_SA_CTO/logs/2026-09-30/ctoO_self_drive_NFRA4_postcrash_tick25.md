# /self-drive NFRA four -- ticks 24-25 + NFRA_MCPINDEX reinstatement (1.0.0_SA_CTO~O, site Z, 2026-09-30 07:2xZ-08:0xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4
- **Ticks covered:** 24 (quiet, drive_ticks line) and 25.

## Measured (07:5xZ)

- **Inbox:** 0 unread at the tick read. Since then: 27021 (2.0.0_SA_COO~MI), acked and answered.
- **Open TOs:** 12 of 180, read from the last `<status>` tag (case-insensitive).
  - NFRA_OPLGTW 4 of 54: OG-g-1, t-2, v-7, v-8.
  - NFRA_OPALAI 4 of 35: OA-e-6, e-8, t-1, t-3.
  - NFRA_MCPORTAL 2 of 18: MP-c-1, v-1.
  - NFRA_MCPINDEX 2 of 73: MX-s-14, t-10.
  - A first pass with a lowercase-only regex read 37 and 40 open, because it missed upper-case tags. The corrected
    read matches tick 24.
- **Completion:** 0 of 4. 1 REACHABLE (MCPINDEX), 3 UNREACHABLE (acts per the tick-11 log).

## NFRA_MCPINDEX reinstatement (Andrew-direct ~07:5xZ)

1. **Rulings B1-B9** on 3.0.0_SA_CVO~O's handoff: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be.
2. **2.0.0_SA_COO~MI respawned** by 0.0.0_AB_MSTR~Z (msg 27017). It is LIVE, and msg 27021 says it is cutting round 5
   off the rulings.
3. **Call ruled (27021):**
   - The ask: does round-5 item 5 (the `advi` catalog row and tool) rest on a new Andrew word?
   - Ruling: no. Cut it HELD on G-W. Andrew's NOT YET on platinum/advi is a hold he set by name. It is not among
     B1-B9, and lifting it is his act (MX-t-11).
4. **B8 landed:** PRD v0.6 @e91ce9a0d5.
   - S10, A8 and VII.4 admit Bloomberg under its standing read beside YCharts, and the fabric line says site-z.
   - ENDPOINT and CONTRACTS are unchanged. prd-signoff reads ADMITTED with the ratified-text half current, so no
     re-sign is owed. This corrects the rulings file's "3.0.0_SA_CVO~O re-signs".
   - Sent to COO~MI.

## Calls

- 1 ruled by the driver (27021, above).
- 0 design forks.
- 0 governance forks.

## Acts only Andrew can do (each cited)

- **B3:** his R20 acknowledgement for the served key under `platinum/etfs/`. CLAUDE.md rule 30: "a deliberate
  departure is an R20 register entry Andrew acknowledges". Put to him in-session; it gates MX-t-10 only.
- **Unchanged:**
  - G-ACCT step 5 (his login or spend);
  - MCPORTAL G-2ND and G-CLOSE;
  - OPLGTW G-D and Part D;
  - MX-t-11, lifting his NOT YET on platinum/advi (a hold he set by name);
  - NFRA_MCPMSP G-USER, G-IT-INF, G-ADVISOR, G-FIRM and G-KEY.
- G-C is external, at Opal IT.

## Compiler Tools

- `.tools/prd-signoff.py status NFRA_MCPINDEX`: v0.6, ADMITTED, ratified-text SIGNED and current.
- Last-tag `<status>` census over `org/missions/D*/NFRA/<CODE>/task-orders/*.md`, with the per-project denominator
  printed.
