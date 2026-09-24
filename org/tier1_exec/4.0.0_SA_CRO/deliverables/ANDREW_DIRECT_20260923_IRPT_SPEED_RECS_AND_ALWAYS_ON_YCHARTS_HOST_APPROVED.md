# Andrew-direct 2026-09-23 ~20:0xZ -- all speed/always-on recommendations approved; YCharts workflow folds into COO~Y's Analysis workload

Recorded by `4.0.0_SA_CRO` at its own terminal.

It answers this seat's report on
`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_BACKEND_SPEED_LISTING_PAGINATION_AND_ALWAYS_ON_BRIEF_20260923.md`
@`e4b28c17c4`, and the two open calls that report put to him:
1. go ahead with the always-on YCharts host, which needs his standing OK for YCharts calls and a declared-state change
   from "held stopped" to "always on";
2. keep or stop the running runner host.

## VERBATIM

> I like all your recs, yes go ahead. I think this needs to be folded in for the COO~Y workload for the "Analysis" tab
> (Ycharts workflow)

## What the word approves (the recommendations as put, nothing wider)

1. **Client/account listing speed**, the speed brief section 2.3:
   - backend levers B1-B8;
   - frontend levers F1-F7.

   It **includes B3 and F1**, which the brief had marked as needing a CTO ruling:
   - B3 caches the parsed directory per artifact version, while re-reading the pointer, ownership and policy on every
     call, so revocation stays immediate;
   - F1 stops the workspace remount on a same-user token refresh.

   Andrew's approval settles both. The CTO keeps the implementation constraints stated there.

   Not recommended, and not approved: a shared CloudFront cache of browse pages.
2. **Pagination redesign**, speed brief section 3.
3. **Always-on YCharts host (option C):**
   - one dedicated small EC2 with **no inbound port**;
   - it owns the YCharts session and consumes `irpt-generation`;
   - it REPLACES the per-job start/stop path and the separate 6-hourly `ycharts-session-probe`, under the no-shadow rule:
     one session owner, one prober;
   - co-hosting on `opal-gateway` (option D) is rejected.
   - **This is Andrew's standing authorization for that host's YCharts calls:** session sign-in and maintenance, the
     report-generation calls, and the sessionless ticker lookups of the upload flow. The host's declared state changes
     from STOPPED to always-on (`infra/aws/terraform/investor-reporting/ycharts/instance.tf:9-25`).
   - It also approves **D1**, the automation's first real sign-in, open in
     `IRPT_YCHARTS_SESSION_SELF_HEAL_DELTA_BRIEF_20260923.md` section 6.
   - Agent-initiated ad hoc YCharts calls outside that host remain under the 2026-07-09 prohibition.
4. **Keep the runner host running** for this plan. `irpt-ycharts-runner` `i-0167fd745ad906a66` stays up and is not
   stopped.
5. **Fix the Analysis generation path FIRST**, whatever the host (speed brief section 4):
   - deploy HEAD's submit `entry.py`;
   - grant `sqs:SendMessage` to the submit role;
   - wire the `irpt-generation` consumer, which under option C is the host;
   - set `IRPT_LIVE_YCHARTS_CALL`;
   - make `/analysis/inputs` and `/analysis/requests*` live.

## Routing

- **Andrew's words:** "folded in for the COO~Y workload for the 'Analysis' tab (Ycharts workflow)".
- **This seat's READING, stated as a reading and not a ruling:** the YCharts workflow items go to `2.0.0_SA_COO~Y`.
  These are items 3-5 above, plus the upload/ticker-resolution brief and the session self-heal delta, whose D2 controller
  becomes the always-on host's own session maintenance under option C. The client-listing items 1-2 are the shared
  header/directory surface that `2.0.0_SA_COO~P` owns under contract v1.3 section 3.
- Final routing is `1.0.0_SA_CTO`'s contract call. If Andrew meant the listing work to move to Y too, his word governs
  over this reading.
