# ws-charter cycle:0025 — 2026-06-03 1903Z

**archetype:** VALIDATE
**Agent:** 1.0.0_SA_CTO (ws CTO). **Class:** FIX (NFRA-arc continuation — concurrence + guardrail; no new authored artifact). **Trigger:** off-cycle /ws-charter (Andrew-fired) + COO DRIVE 3-item FYI/concur-check.

## Inbox (DRIVE, COO — 3 items)

1. **NFRA W2(a) RE-SCOPE (concur-check)** → CONCUR, no re-open.
2. **render-smoke FIX TO authored** (FABRIC_RSMOKEREAP) → RAVC-closed on my 185712Z disposition.
3. **NFRA W4 cost-cap (Andrew-direct, enforcer TF)** → CONCUR + idle-cap guardrail.

## Actions

### 1. NFRA W2(a) port-tonight / defer-swap — CONCUR (no re-open)
0.6.0+DS surfaced that the bare runner-telemetry swap WITHOUT a merge_perf_report rewrite = empty perf_report tomorrow = my cond-b failure (runner-telemetry emits per-tick JSONL; gold_prof's perf_report.json contract feeds merge_perf_report on BOTH bd + orion/inf chains). Re-scope: port PSS INTO gold_prof.py (`c07c52383`, cp to opal-runner-shared) carries tonight (both chains true-physical, contract intact, zero ad-hoc compute); the full swap-to-runner-telemetry defers to a deliberate move built WITH the merge rewrite + validation.
- **Architectural read:** strictly better risk posture. Satisfies cond-b (contract intact) AND cond-c (gold_prof now has PSS-parity; swap/deprecate = deferred deliberate move). My nod's intent (true PSS validated free on the nightly) fully preserved; only mechanism moved swap-now→port-now.
- **Release gate UNCHANGED, now both chains:** tomorrow's perf_report showing PSS+sys_mem populated+sane (~1.2GB/128GB, not phantom-TB) on bd AND orion/inf.
- **Deferred-swap condition:** build it WITH the merge_perf_report rewrite, validate as its own move, do NOT race a cutoff.

### 2. render-smoke FIX TO — RAVC-closed
FABRIC_RSMOKEREAP captures my disposition faithfully (FIX-class, 0.7.0, queued-behind-security, normal-pri, launch-time-PID-registry + timeout-bounded-reap acceptance core, NOT a new project code, parented under LD-0144 line). Micro-note to COO: AC must EXPLICITLY forbid name-based `taskkill /im msedge.exe` (PID-scoped only) — the load-bearing safety property.

### 3. NFRA W4 cost-cap — CONCUR + idle-cap guardrail
Andrew-direct <=3h cap on inf-gold-layer-runner i-0ed5 (remove from EXCLUDED_INSTANCES; TF via safe-apply) after a $30 idle-burn (watchdog-disarmed + enforcer-excluded). **Guardrail sent to COO + 0.7.0 directly (pre-irreversible-TF delivery):** make the cap IDLE-time-scoped (or active-job-aware), NOT blind wall-clock kill. The runner was excluded to protect scheduled gold runs; defect was idle-burn, so fix = make IDLE reapable. A wall-clock "alive>3h→kill" would truncate a legit >3h gold nightly mid-run (silent data-incompleteness > the $30 saved). Andrew's <=3h = idle ceiling.

## Project-state-sweep (origin/CLOUD @ ee462b4f7)

- **CVO BACK LIVE** (MSTR respawned PID 28144) — last tick's dark flag RESOLVED. Producing: spot-check cycle 10, CMPAWS PASS-1.
- **ADHC_CMPAWS** — hand-audit PASS-1 JOINTLY SIGNED (CVO oracle + AE co-sign, `98998ec85`): 19 drift→14-confirmed-shadow + 5-accept-external, zero false-pos; 76/88/111 reconciled; Q3 IMDSv2 corrected. Node axis GREEN; edge+IAM-drift = PASS-2 (AE-build-gated). Healthy; not CTO-blocked.
- **v2.1.114** — DT RE-VERIFIED on 7-commit head (`bba3b6a4a`), byte-identical, tsc+build green; caught+fixed local-PROD pollution. **Andrew-GO-gated.**
- **PMTRDX.001** — handed to AE; CVO e2e now unblocked (CVO live).
- **NFRA** — W2(a) port tonight, W2(b) PSS-parity met via port, W4 cost-cap routed. In motion.

No REPAIR-AMENDMENT (no CVO finding). No NOVEL (no Andrew new-PRD direction). No CVO_CONSULT.

## Next-cycle expected state

NFRA PSS port lands tonight → tomorrow's nightly = free validation (BOTH chains) = my release gate. v2.1.114 awaits Andrew GO. render-smoke + W4 in-lane (0.7.0, queued behind security). CMPAWS PASS-2 AE-build-gated. Next cron tick 30m.
