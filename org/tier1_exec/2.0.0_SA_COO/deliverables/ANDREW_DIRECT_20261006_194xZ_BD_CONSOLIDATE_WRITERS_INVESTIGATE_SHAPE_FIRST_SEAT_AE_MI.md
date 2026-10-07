# ANDREW-DIRECT 2026-10-06 ~19:4xZ -- consolidate the BD writers; investigate the shape first; seat 0.7.0_AE_CloudOps~MI

**Channel:** typed at the `2.0.0_SA_COO~MI` terminal (site Z), ~19:4xZ (clock read 2026-10-06T19:41:53Z). He was
answering this seat's `/open-calls` card: "Change the BD production pipeline to consolidate writers? (a) yes, ship it /
(b) no, drop it from this round". That card was the scope question 1.0.0_SA_CTO~O put to him, msg 30220.

**Verbatim:**

> Yes we can consolidate writers. I need you to investigate first. I need you to check what the shape of the morning
> run is (is it rest api? what fields/data come back? does it have as of provenance in any metadata BD-side?). Then i
> need you to compare that to the evening run, which im guessing is a manual ec2 browser crawl thing. If the morning one
> is in better condition, more rich data, id rather get rid of the night one. But we need to confirm the shape first
> before making that move. What id recommend is bringing on a 0.7.0_AE_CloudOps~MI which will be your ~MI AE agent to
> handle these operations. If it turns out that the evening one is extraneous, then the agent can decommission that run,
> and you proceed with your work on the MCPINDEX side

**Context (not part of the word):**

- **The two runs, as this seat has measured them** (the mapping is to be confirmed by the investigation):
  - **"Morning" run:** `bd-49f-runner` (Lambda, `bd-49f-session-daily` cron 00:00Z), which lands
    `forwardfill_v2/` bronze plus the `bronze/<date>/_BRONZE_COMPLETE.json` sentinel. The sentinel fires
    `bd-silver-merge`, which writes `silver/{transactions,realized,allocations,unrealized}/`.
  - **"Evening" run:** the SSM documents `opal-bd-transaction-download` and `opal-bd-realized-download` (rules
    21:45Z / 21:53Z MON-FRI), which run on an EC2 instance and merge into the same two silver tables.
- **Order of acts in the word:**
  1. The investigation of shape (transport, fields, BD-side as-of provenance) comes first.
  2. The decommission of the evening run follows only if the investigation finds it extraneous.
  3. The NFRA_MCPINDEX round-7 BD chain (MX-s-17/s-18/s-19) proceeds after that.

**Scope:** as written. This record does not widen or narrow it.

-- 2.0.0_SA_COO~MI
