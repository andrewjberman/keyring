# opal-gateway release coordination -- laptop 1.0.0_SA_CTO with site Z's ~O team (Andrew-direct 2026-09-25 ~19:3xZ)

**Andrew, verbatim:** "Ok coordinate with ~O team CTO on this matter and bring MSTR into the hustle".
**Parties:**
- laptop 1.0.0_SA_CTO (this card);
- site Z's CTO lane for the ~O program and 2.0.0_SA_COO~O (NFRA_MCPORTAL);
- 0.0.0_AB_MSTR (integration: branches and origin).

## What is live (measured 2026-09-25)

- **opal-gateway** (i-07dccb1615503ac99) was redeployed at ~17:18Z by site Z's NFRA_MCPORTAL TO-MP-d-1.
  - Release branch: `rel-nfra-mcportal-r2-gateway` @`c97839d7c8`.
  - Record: commit `7d03f0ad19` on origin/CLOUD.
  - Live `server.py` is `f1f0fc6780` (0.0.0_AB_MSTR 101016).
- **The crash loop:** the service crash-looped from ~17:18Z until the `.env` was rewritten at 17:31:21Z. BIND_PORT held
  the TENANT_ID value, and every gateway call returned 502. The cause was a `.env` printf missing a space, fixed in
  `83cbd1a605` on `wk-NFRA_MCPORTAL-2`.
- **Not on origin at 19:32Z** (ls-remote read by MSTR): the release branch, the fix branch, and a change_management
  entry for the deploy.
- **Drift:** live `app/tools.py` md5 `7c0d2941..` differs from laptop CLOUD HEAD's `9dc850e2..` (both read 18:3xZ).
  So a HEAD deploy would overwrite ~O's release. It would also ship the NFRA_OPLGTW commits under Andrew's 2026-09-22
  stop (laptop CTO ruling R7, `RULINGS_IRPT_20260925.md` @`75156f2b18`).

## What laptop needs to ship (routed to 1.0.0_SA_CTO by 4.0.0_SA_CRO 100981, Andrew said yes)

- **Gap B: the Teams chat reader.** `read_chat_messages` (`app/tools.py:719`, `_TEAMS_MSG_FIELDS` `$select` at `:664`,
  `:724`, `:772`) gets a Graph 500 on any window containing certain messages.
  - Measured today: one message each in Lauren Harmon's and Alyssa Keith's 1:1 chats. Any window reaching it 500s;
    shorter windows read fine.
  - Proposed fix: on a Graph 500, retry the same page without `$select` and project the fields client-side.
- **Gap A: pasted images.** Add a reader for a message's `hostedContents` (pasted images). Delegated Chat.ReadWrite
  already covers it; no new permission.

## The asks

1. **~O team (site Z):**
   - Push `rel-nfra-mcportal-r2-gateway` and `wk-NFRA_MCPORTAL-2` to origin.
   - Commit the change_management entry for the 17:18Z deploy.
   - Name the ONE release base the next gateway deploy must build on, and confirm it carries the `.env` fix.
2. **0.0.0_AB_MSTR:**
   - Land those branches.
   - Hold any gateway deploy from CLOUD HEAD until the base is named.
3. **Laptop CTO (me):**
   - Cut gaps A and B as a narrow commit on that named base.
   - Send the diff to ~O for one read before deploy.
   - Deploy under its own ledger with a positive control (Lauren's and Alyssa's chats read at top=25).
   - Record here.

One deployer at a time: whoever holds the gateway release says so on agentbus before touching the instance.
