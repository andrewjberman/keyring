# COT re-smoke -- Distribution POPULATES (DS emit verified) + geo-unassigned display finding (delta since db64e140b)
**archetype:** VALIDATE

**Agent:** 0.4.0_DE_ClientPlatform · **Window:** 2026-06-22 ~20:04Z -> ~20:10Z · **Task:** COT ADVI v1 go-live re-smoke (gate#2 final step, COO /drive) · 0 code commits · ~4 significant MCP.

## Current State
DS emitted partner_analytics_quarterly for COT (the P1 gap I caught). Re-smoked the populated Distribution. RESULT: Distribution POPULATES (gap resolved) + one new DISPLAY finding (geo unassigned $24.5M not shown/reconciled) -> polish-item, routed CVO/Andrew.

## Findings (grounded)
- DS EMIT [SERVED-CONFIRMED, boto3]: platinum/firm/partner_analytics_quarterly.json now PRESENT (141KB, emitted 2026-06-22T19:59Z), data_as_of=06-18, correct PartnerAnalyticsResponse shape (periods + views.geo current/q1/q2/q3), donut metrics.aua ties $395,300,238.06. (Verified the producer's emit on the served artifact per never-trust-self-report.)
- POPULATED RENDER [OBSERVED, data-injected re-smoke]: Distribution "AUM BY STATE" renders -- Texas 87.4% (309 acct), Florida 4.0%, California 4.0%, NC 1.4%, OH 1.3%, NY/OK/KY/MO, Other 0.4%. NO "Analytics data unavailable". Header $395M@06-18 holds; GEO-only cohort holds (disabled-non-leakage intact); q1/q2/q3=N/A (04-22 onboard, expected). 
- GEO-UNASSIGNED DISPLAY FINDING: the donut's state %s are of the STATE-ATTRIBUTED sum $370.8M (TX 324.1M/370.8M=87.4%) but the donut LABELS "Total AUM $395M". The ~$24.5M (6.2%) un-stated AUA is NEITHER a slice NOR reconciled on-view ("Other 0.4%" = small-states bucket, not the unassigned). The emitted artifact's geo.current.donut has 14 state segments summing to $370.8M, NO unassigned segment -> the FE can't show it. MY READ: polish-item (data correct, renders clean), not a blocker, but the non-reconciling %s-vs-$395M-label is a clarity risk for the Distribution-centric main view. Fix = DS adds an "Unassigned/Not-state-attributed" segment to the geo donut (reconciles to $395M + labels the gap) OR a FE footnote. CVO rules acceptability; Andrew first-impression.

## Method caveat (Rule 22)
Data-injected render (pulled the emitted artifact -> served from dev public/ -> rendered the cottonwood session). NOT a live-CF-authed-200 render (dev-bypass fake token still 401s /auth/refresh, unchanged by the emit). So this certs FE-POPULATES-correctly with the real emitted data; the live-CF-200 cert + per-user-scope (AC2) isolation ride provisioning / CVO. Vite SPA-fallback handled (present-vs-absent judged by content, this pass added an explicit HTML-detect).

## Blockers
None on my leg (delivered). COT go-live now: CVO re-verify + the geo-unassigned acceptability ruling (now-fix vs fast-follow) + provisioning (live-CF-200 + AC2). Prior gates event-pending (TO-2/DS TO-1, P2-1/AE P2-2).

## Next Steps
- **[3.0.0_SA_CVO]** re-verify the populated render + rule the geo-unassigned acceptability.
- **[2.0.0_SA_COO/Andrew]** geo-unassigned: launch-now (fast-follow polish) vs pre-launch fix. If FE-footnote chosen = my DE lane; if Unassigned-segment = DS data-layer.
- **[0.4.0_DE]** if a FE polish is GO'd (footnote/unassigned-slice), implement; else event-driven on the other gates.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| boto3 head/get (not raw-aws) | opal-data-cot partner_analytics_quarterly.json | emit verified present 19:59Z, 06-18, ties $395.30M, geo donut 14 states summing $370.8M (no unassigned segment) |
| playwright (browser) | data-injected re-smoke w/ emitted artifact | Distribution POPULATES (AUM BY STATE, TX 87.4%...); geo $24.5M unassigned not shown/reconciled |

## MCP traffic (this window)
~4: COO gate#2 re-smoke GO + my ACK (200454Z); RAVC re-smoke result + geo-read to COO (200941Z) + CVO (200949Z).
