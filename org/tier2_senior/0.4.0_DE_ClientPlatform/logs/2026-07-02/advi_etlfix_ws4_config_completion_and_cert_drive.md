# ADVI_ETLFIX WS-4 -- config-completion (two-tier page thresholds) + cert/cot drives

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

**Workspace CLOUD commits:** `f064321f3` (inc-4 MDPF wiring) -> `f44d2c602` (inc-5 config-completion)
**Trigger:** COO [ACCEPT WS-4 firm-wide] + [DRIVE WS-4 to FULL close] (movement-check: 0 work-calls 21:10-21:43Z).

## Current State

WS-4 DE-owned build is COMPLETE for bd/inf/MDPF; drove the config-completion tail + dispatched the two remaining close items (cot=3 coordination, CVO cert).

### Shipped this increment (f44d2c602, no regression -- verified content-mode PASS firm-wide post-change)
Two-tier PAGE thresholds (single config source; comp-freshness ignores frontier_page, the AE CW alarm reads it -> no drift):
- bd: 5 served keys frontier_page_trading_days=2 (T-1 cadence+1, DS~B-grounded).
- inf: 5 served keys page=2 (Orion T-1).
- MDPF: page=2 provisional (aggregate-of-partners; DS~C per-table refine pending).
- cot=3 NOT set unilaterally -- coordinated to DS~C (its T+2 holdings cadence is DS~C's grounded finding + a ~5-nightly re-confirm pending; separate firm calibration).

### WS-4 state (the fail-silent class fix, firm-wide)
- Oracle (comp-freshness content-mode) coverage: bd+inf+cot+MDPF, all keyed on the true normalized vintage.
- served_vintage_lag() helper landed (COO 08bce489c) = the AE alarm's instance-source.
- Config layer: DE-complete (bd/inf/MDPF); cot=3 pending DS~C.

## Decisions Made
- Did NOT set cot's page threshold unilaterally -- it rests on DS~C's grounded cadence + a pending re-confirm; coordinated instead of clobbered.
- Verified comp-freshness IGNORES frontier_page (the WARN/oracle keys frontier_warn only) so the new field is AE-alarm-only + can't regress the oracle -- tested inf 0td / bd 1td / MDPF 0td all PASS post-change.

## Compiler Tools
| Tool | Result | Note |
|------|--------|------|
| owned-paths-check (cot lane) | checked | deferred cot to owner regardless (calibration, not just lane) |
| `comp-freshness artifact` (inf/bd/MDPF served) | PASS content-mode | no regression from the frontier_page add |
| YAML parse (3 configs) | clean | bd 37 / inf 36 / served 7 |
| safe-commit | PASS | f44d2c602 |

## Next Steps
- **[0.4.0_DS_ClientPlatform~C]** set/confirm cot frontier_page_trading_days=3 (their grounded cadence) + the per-table gating-cadence model shape (config schema vs doctrine).
- **[3.0.0_SA_CVO]** author + run the 3 adversarial WS-4 cert ACs (mtime-fresh/content-stale, per-dimension DEFER-roll-forward, fresh-top-level+stale-joined-dim) -> the WS-4 cert. Looped.
- **[0.6.0_AE_PartnerETL]** the per-partner fail-loud alarm off served_vintage_lag_from_s3 (behind its P1) -> the hard GATE.
- **[0.4.0_DE, me]** land cot=3 on DS~C's confirm; add the per-table schema if DS~C wants it in-config; support the CVO cert grounding.
