<task_order>
<metadata>
  <to_id>NFRA.W2</to_id>
  <project>NFRA (Cloud / Shared-Resource Cost Governance)</project>
  <title>Fleet telemetry coverage — wire the fixed runner-telemetry profiler across the runner fleet so right-sizing has real p5/median/mean/p95 inputs; validate on SCHEDULED nightly runs ONLY</title>
  <assigned_to>0.6.0_AE_PartnerETL (a) · 0.4.0_DS_ClientPlatform (b) · 0.7.0_AE_CloudOps (c)(d), NFRA owner</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-03</issued_date>
  <status>active — (a) GO'd to 0.6.0 [deploy gated on CTO profiler-swap nod, COO routing]; (b) routed DS; (c)(d) queued behind 0.7.0 Andrew-live security</status>
  <dispatch_held>false</dispatch_held>
  <priority>HIGH on (a) — must DEPLOY before tomorrow's nightly bd-gold run so the SCHEDULED run validates it at zero extra compute (Andrew compute-discipline). (b)/(c)/(d) NORMAL.</priority>
  <references>
    <ref type="greenlight">Andrew-direct 2026-06-03 (relayed 0.6.0 180303Z): NFRA greenlit for decomposition + COMPUTE-DISCIPLINE constraint (no ad-hoc gold runs; validate on tomorrow's nightly)</ref>
    <ref type="routing">0.6.0 175653Z: runner-telemetry memory-fix DONE (fe907a974) + (a)/(b)/(c)/(d) wiring breakdown</ref>
    <ref type="brief">docs/briefs/nfra-cloud-cost-governance-prd-request-20260601.md ask #2 (fleet telemetry coverage)</ref>
    <ref type="root-cause">both profilers reported tree-summed RSS = CoW-inflated (phantom TB peaks); true physical ~1.2GB/128GB. Fix = tree-summed PSS + sys_mem (instance-level = the right-sizing number).</ref>
  </references>
</metadata>

<scope>
Core defect ALREADY FIXED (0.6.0, fe907a974, .tools): runner-telemetry suite now reports tree-summed PSS true-physical (+ RSS fallback, retains memory_rss_mb), ADDS sys_mem_used_mb/pct (instance-level right-sizing number), and analyze emits per-script p5/median/mean/p95/max for cpu + mem(PSS) + sys_mem. Validated locally + gate-clean. This TO ROLLS IT OUT.

## (a) Wire + deploy — 0.6.0_AE [CRITICAL PATH; deploy GATED on CTO nod]
Wire runner-telemetry into the gold dispatch (gold_dispatch.sh, CLOUD_OPS_OR_ETL surface) replacing the gold_prof.py per-script wrapper; deploy to opal-runner-shared. The profiler SWAP (gold_prof -> runner-telemetry) needs CTO ratification — COO is routing that nod now. PREP NOW; HOLD the deploy for the CTO nod. SEQUENCING TARGET: land the deploy BEFORE tomorrow's nightly bd-gold run so the scheduled run captures true telemetry (Andrew: "installed + actually working") at ZERO extra compute. DO NOT trigger an ad-hoc bd-gold run to "prove" it — tomorrow's nightly IS the test.

## (b) gold_prof.py PSS parity OR deprecate — 0.4.0_DS [data/black_diamond/scripts/gold/** = POD4]
Apply the same tree-summed-PSS fix to gold_prof.py, OR deprecate it in favor of runner-telemetry (coordinate w/ 0.6.0 on which — if (a) makes gold_prof redundant on the gold chain, deprecate; if gold_prof stays the canonical perf_report.json emitter elsewhere, port the PSS fix). No ad-hoc run to validate — confirm on the next scheduled run that consumes it.

## (c) Fleet rollout + fix inf cpu:null — 0.7.0_AE [NFRA owner; AFTER Andrew-live security]
Roll the fixed profiler across inf/smartx/mdpf/t3 runner chains; fix the inf-gold cpu:null (psutil not active). Validate each on its OWN next scheduled run.

## (d) Monthly perf-rollup cadence — 0.7.0_AE/NFRA
Stand up the monthly runner-telemetry-analyze p5/median/mean/p95 rollup per runner (feeds W3 right-sizing). Cadence artifact, not a run.
</scope>

<acceptance>
- [ ] (a) runner-telemetry wired into gold_dispatch + deployed to opal-runner-shared; CTO profiler-swap nod obtained; deploy lands before tomorrow's nightly; tomorrow's SCHEDULED bd-gold run captures true PSS/sys_mem telemetry (no ad-hoc run). RAVC2 to COO post-nightly.
- [ ] (b) gold_prof PSS-parity-or-deprecate decided + shipped, coordinated w/ 0.6.0; validated on next scheduled consumer run.
- [ ] (c) fleet rollout inf/smartx/mdpf/t3 + inf cpu:null fixed; each validated on its own scheduled run.
- [ ] (d) monthly perf-rollup cadence armed.
- [ ] COMPUTE-DISCIPLINE honored throughout: zero manufactured gold runs; all validation on scheduled nightlies.
</acceptance>
</task_order>
