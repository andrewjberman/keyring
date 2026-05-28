# Session Log — 0.4.0_DS_ClientPlatform — 2026-05-28 (F5 canonical Advisor-NNA — THE SPINE)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, TRACE

**Agent:** 0.4.0_DS_ClientPlatform (Tier-2 DS, ClientPlatform / ADVI Inflection)
**Driver:** ws COO /drive GO (ADVI_INFMVP.F5) — Andrew-direct spine + highest priority (screenshots)
**Theme:** F5 = ONE canonical Advisor-NNA across Segment Analytics snapshot/continuous + Lifetime Activity. Empirical Phase-0 → canonical emit → RAVC2.

---

## Headline outcomes

1. **F5 Phase-0 (Q2) RESOLVED empirically.** The canonical Advisor-NNA SOURCE already exists and is the single source of truth — `gold/canonical/canonical_nna_{date}.parquet` (I_C01). No competing definition. Brief of record: `docs/briefs/advi-infmvp-f5-canonical-advisor-nna-phase0-20260528.md` (`01a738d`, amended `9a5aeec8b`).
2. **Peter reconciliation (−$274K vs +$2.35M) — TWO causes, one a real calc bug.** +$2.35M = snapshot Q1'26 calendar quarter (CORRECT). −$274K = continuous chart, which is NUMERICALLY WRONG: `INF_D_00d.build_nna_adv_view` weekly-SAMPLES the NNA flow (lossless for AUA stock, corrupts NNA flow) → 60% of Peter's flow dropped (canonical 2Y = +$18.28M vs sampled +$7.32M). Corrected my own first-pass Phase-0 framing ("pure window-semantics, no calc bug").
3. **Canonical emit SHIPPED + deployed + verified.** New gold script `INF_D_00f.advisor_nna_canonical.py` (`bcc29881c`) → `platinum/firm/advisor_nna_canonical.json` (186,924 bytes, data_as_of 2026-05-27). Window totals (QTD/YTD/MAX/1Y/3Y/calendar-quarters) × fee_view + bucket-summed per-period series (weekly/monthly/quarterly). All tie-outs exact.
4. **RAVC2-Request** to COO, CC CTO + CVO, with the field/path RD repoints to + the continuous-bug correction + CVO axis-2 (window labeling) carried as a gate-blocking RD-leg requirement.

---

## Thread 1 — Phase-0 investigation (the spine)

Traced the three FE read paths in `DistributionTab.tsx` + `advisor-intelligence.ts` to their producer scripts:
- **Snapshot donut** (`getPlatinumPartnerAnalytics` → `partner_analytics_quarterly.json` `views.nna[period].adv`, INF_D_04) — single calendar-quarter slice of canonical_nna. **Canonical-consistent.**
- **Continuous** (`getPlatinumCumulativeChart` → `cumulative_chart.json` `nna_adv`, INF_D_00d) — weekly-SAMPLED. **NUMERICALLY WRONG (60% flow loss).**
- **Lifetime Activity** (`getPlatinumAdvisorSummary` → `book.json` + advisor `timeseries.json`, INF_D_02) — YTD headline + since-inception cumulative. **Canonical-consistent.**

Empirical cross-checks (live S3, all to the cent vs my emit):
| Surface | Peter | == |
|---|---|---|
| snapshot `views.nna.current.adv` | −$805,260.55 | combined QTD ✓ |
| snapshot `views.nna.q1.adv` (Q1'26) | +$2,354,781.18 | the +$2.35M screenshot |
| Lifetime `book.json` ytd_nna | +$1,549,520.63 | combined YTD ✓ |
| Lifetime `timeseries` last nna_canonical | +$108,959,119.23 | combined MAX ✓ |
| continuous `nna_adv` (2Y, sampled) | +$7.32M | WRONG — canonical all-days +$18.28M |

## Thread 2 — Canonical emit (INF_D_00f)

- Schema-verified canonical_nna (`date, account_id, advisor_key, rep_bucket, daily_inflow, daily_outflow, net_nna`; outflow positive-magnitude; net_nna = inflow − outflow) + billing (`account_id`, `is_fee_earning`) before writing.
- Definition: `Advisor-NNA(advisor, window, fee_view) = Σ canonical_nna.net_nna over [start,end]` filtered to advisor_key [and is_fee_earning]. External flows only.
- Structure: `firm.{windows,series}` + `advisors[key].{windows,series}`. windows have total + fee_paying + no_fee (F4 tie-out). series = weekly/monthly/quarterly **bucket-summed** (correct flow aggregation; supersedes INF_D_00d sampling).
- Validation (dry-run): firm QTD/YTD/MAX == sum(advisors) == fee_paying+no_fee, exact. Peter QTD/YTD/MAX/q1 == Phase-0 targets, exact. quarterly-series-sum == MAX-window total, exact.
- Deploy: committed `bcc29881c`, pushed `9a5aeec8b` (safe-deploy auto-DEPLOYED to S3 code/gold; HALT_ACK on 4 routine pending msgs, no STOP), ran `--upload` locally (INF pattern), verified artifact in S3.

## Compiler Tools

| Tool | Result |
|---|---|
| `.tools/ds-commit-gate.sh INF_D_00f...` | PASS (py_compile + AST scan + ruff). One fix iter: E402 (docstring before `from __future__`). |
| `comp-pipescript io INF_D_00f...` | Script not yet in graph (new file) — expected; ran per mandate. |
| safe-deploy (pre-push hook) | PASS — DEPLOYED [inf] to S3 code/gold; HALTGT surfaced 4 routine msgs (correctly caught while watcher was down), HALT_ACK=1 cleared. |

DS-self-check substituted for `comp-validate` (no validate config for net-new INF_D_00f); tie-outs above are the validation.

## Open / handoffs

- **COO:** ratify F5 RAVC2; author RD-repoint leg (3 surfaces → `advisor_nna_canonical.json`; continuous onto `series.*` to FIX the sampling bug; CVO axis-2 window labeling) + CVO-gate leg. Then GO F4 (its fee_paying/no_fee buckets already emitted + tie out).
- **CVO:** RIGID gate now 3 axes — mechanical per-window equality + axis-2 window labeling + continuous-now-correct (+$18M-class, not +$7M sampled artifact).
- **Continuous-chart sampling bug (INF_D_00d nna_adv/nna_geo):** superseded by canonical series on RD repoint; can deprecate the buggy builders later.
- **Cohort dimension (new-vs-existing client):** deferred additive follow-on (reuses F11 hh_lifecycle); flagged to COO/CVO.
- **Shadow household (Raeleen, $0.01):** book.json roster item; canonical NNA is account-flow grain so it doesn't enter the total; immaterial. Roster dedup separate (post-demo).
- **Standing queue UNTOUCHED:** ADVI_DEMOV1.003/004/006, ADVI_VALFIN.010, ADVI_INFDEMO.F4-followon/F11-followonB. (MDPF_SCOPED.S2 = DS_CP~B's lane, not mine.)
- **Watcher:** repeated exit-143 (reap-then-SIGTERM churn) this session; relied on check-inbox (authoritative) + /work 20m cron + HALTGT pre-push gate (which caught the 4 pending msgs). Relaunched at session points.

## Commits (author 0.4.0_DS_ClientPlatform)
- `01a738d` — F5 Phase-0 brief (canonical definition + reconciliation).
- `bcc29881c` — INF_D_00f canonical Advisor-NNA emit script.
- `9a5aeec8b` — brief amend (continuous calc-bug correction).
- (artifact `advisor_nna_canonical.json` emitted to S3 via local --upload; not a git artifact.)
