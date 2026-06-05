# 0.6.0_AE_PartnerETL session log — 2026-06-05 work_1304Z (DEMOAUTH.002 bring-up: verify -> root-cause -> durability-fix -> relaunch)

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, VALIDATE

## Bring-up (MSTR, COO TOP priority / Andrew-direct)
- /watcher: registered (was NOT REGISTERED, PID 2096), persistent inbox Monitor armed (task b457p7lxr). No stale cron.
- /work 20m cron armed (de6408be). HALT-gate clean.

## FIRST task — verify ADVI_DEMOAUTH.002 Pass-2 write landed: IT DID NOT (demo REGRESSED)
Mid-write death msg was "Pass-2 NOW WRITING 22424 objs". Verified actual S3 state:
- opal-data-demo/platinum = **6601 objs** (accounts 6600 + 1). firm/clients/advisors = **0**.
- Prior-state (pre-.002) was 9282 (firm 0, clients 1795, advisors 886, accounts 6600). So the failed run made it WORSE — deleted the 1795 clients + 886 advisors that WERE there.
- demo-reclone systemd unit: ran 2026-06-03 20:58Z -> 23:35Z (2h40m), exit 1/FAILURE.

## Root cause (read the failure log /tmp/demo_reclone_20260603_205805.log)
apply_transform (Pass 2) does a destructive snapshot-clean of the ENTIRE target BEFORE writing, then crashed:
```
snapshot-clean: TOTAL deleted 9281 object(s)
... 6000 / 22424 written
botocore.errorfactory.NoSuchKey ... GetObject ... key does not exist
  (worker -> get_json line 766; as_completed -> raise exc line 793)
```
A single 404 on a SOURCE read (key listed in Pass-1, vanished by Pass-2 read = bd-source drift / TOCTOU) aborted the whole destructive run. Confirmed live: bd advisors drifted 169->165 folders; fresh run lists 22414 not 22424.

## Durability fix (commit a6b83b042, pushed CLOUD, deployed S3 demov1/)
- worker() catches ClientError NoSuchKey/404/NotFound on the source get_json -> counts skipped_missing (per-subpath) + continues. PII-leak HardError abort path UNCHANGED (R5 gate intact).
- Completion gate: written+skipped==listed => complete (404'd source = accounted-for, not truncation). Per-subpath summary + report.json + log surface skip count + sample.
- No x3/transform-logic change (per COO "no new x3 code"). ds-commit-gate clean (py_compile+AST+ruff). +49/-6.
- Residual fragility (clean-before-write destroys target on any uncaught mid-write fail) noted for a future write-then-swap follow-up; out of scope.

## Relaunch (demo-reclone2, 12:59:54Z)
systemd-run transient unit demo-reclone2 (survives). PATH-B-GATE 12/12 PASS -> Pass-1 mapping built (165 adv / 2985 clients / 6764 accts / 22414 listed) -> Pass-2 snapshot-clean (deleted 6600 accts, rest already 0) -> WRITING. Telemetry wrapping (psutil installed -> demov1/logs/telemetry). ~2.7h.

## RAVC2 + coordination
- RAVC2 LAUNCH -> COO (130225Z): regression finding + root cause + fix + relaunch.
- COO ACK (130322Z): verify-discipline praised, DEMOAUTH.002 ADVANCING, awaits completion RAVC2.
- 0.7.0_AE_CloudOps PEER-ASK (130241Z): cost-audit wants to terminate i-03343a60 ($61/mo). Replied NEEDED-NOW (run active) -> terminate-at-close.
- COO idle-ceiling coordination: replied GO on auto-STOP add (restartable), hold full TERMINATE until .002 close.

## Gates remaining before close
pii_leak_scan R5 (Phase C of the run, must PASS) -> DS PII-verify (DS owns final clean sign-off, tomorrow) -> Andrew visual smoke. NO external demo until DS confirms PII-clean.

## Open / next
Monitor demo-reclone2 to completion (next /work ticks); on DONE: read leak_result.json (R5), transform_report (per-subpath written/skipped), telemetry perf; RAVC2 completion to COO w/ external-use boundary flag; CC CTO + DS.
