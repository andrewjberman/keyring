# NFRA Cost-Reduction Scorecard (running tally)

**Companion to:** `docs/architecture/NFRA_COSTRED_PRD.md` (R1-R8) + audit `docs/briefs/aws-cost-audit-20260605.md`
**Maintained by:** 2.0.0_SA_COO — updated as each item's RAVC2 / validation lands.
**Baseline:** ~$600/mo total AWS (May $603; June run-rate ~$600). Account 313476888478.
**Last updated:** 2026-06-05T14:40Z

> Purpose: a single honest view of cost-reduction work — what's banked, what's applied-but-not-yet-validated, what's forecast, and what's preventive — so the savings claim never over-states reality. Each row firms up as its validation gate clears.

## Status legend
- BANKED — applied + independently verified; off the bill.
- APPLIED-VALIDATING — change is live; savings real but the exact figure / no-regression confirms at a named gate (usually the next scheduled nightly).
- PENDING — owner actively working; staged or in-design; gated on a named step (often an Andrew apply-GO for destructive items).
- DEFERRED / FUTURE — identified, not being worked now.
- *Preventive* — avoids future waste rather than cutting the current bill (no double-count into the bill-% rollup).

## Line items

| # | Item | What it does | Owner | Status | Monthly savings | Validation gate |
|---|------|--------------|-------|--------|-----------------|-----------------|
| R8 | Universal 3h idle-aware cap (enforcer-v1.1.1) | Auto-stops idle boxes fleet-wide; kills the runaway/zombie class; IDLE_CPU_THRESHOLD=1.0 (I/O-bound-calibrated), zero exemptions | 0.7.0_AE | BANKED | *Preventive* ~$50-90/mo avoided runaway | Live + **CVO-PASS empirical** (c7b9ae116): inf-gold longest all-<1% stretch 45min << 180min reap window. PROBABILISTIC (relies on >1% bump every <3h) — durable I/O-runner launch-tag = P2 structural backstop |
| R4 | inf-exporter stopped | Removed the 34-day always-on zombie | 0.7.0_AE | BANKED | **~$30/mo** | Verified reversible; auto-restarts on schedule (CVO PASS) |
| R5a | 4 orphan EBS volumes deleted | Unattached disk (Feb-17) | 0.7.0_AE | BANKED | **~$4/mo** | All snapshotted pre-delete; CVO PASS |
| R1 | Cost-allocation tags | Makes the bill attributable by pipeline | 0.7.0_AE | BANKED (backfill ongoing) | **$0 direct** (enabler) | 4 keys active since ~13:00Z (CE ~24h clock); buckets aaii/pm/imo tagged; bd/inf/shared held for nightly-complete |
| R3a | bd-gold right-size c6i.16xlarge→r6i.4xlarge | Sheds wasted cores (64→16), keeps 128GB RAM | 0.6.0_AE | APPLIED-VALIDATING | **~$75-160/mo** | Tonight's nightly: +wall acceptable, sys_mem<128GB, perf_report intact (confirm tomorrow AM) |
| R3b | bd-gold Spot + on-demand fallback + per-script resume | Spare-capacity discount on top of right-size | 0.6.0_AE | PENDING (design) | **+~$40-50/mo** (stacks to ~85% off bd-gold) | Design draft → COO/CTO review → build → separate nightly (after R3a validates) |
| R2 | Time Machine retention 90d→35d (NoncurrentVersionExpiration) | Trims S3 restore-version retention to the coherent floor | 0.4.0_DS | PENDING (safety proof + GB audit) | **~$25-45/mo** (precise GB pending) | HARD GATE: prove delete-set is pure supersession-snapshots (zero only-copy data) + exact GB → Andrew apply-GO (destructive/irreversible) |
| R5b | Release idle Elastic IP (bd-gold) | EIP idle on stopped bd-gold runner | 0.7.0_AE | BANKED | **~$3.6/mo** | RELEASED (eipalloc-08cbaa75); describe-addresses confirms gone. smartx EIP CLOSED-AS-KEEP (Andrew: leave it — SmartX-side allowlist load-bearing, $3.6/mo not worth breaking the feed). |
| — | moltbot decommission | Last stopped zombie box + last AutoShutdown exemption | Andrew + 0.7.0_AE | BANKED | **~$2/mo** + zero-exemptions | Andrew terminated (`!`); AE cleaned vol+manifest (snapshot retained). R8 now has TRULY zero exemptions fleet-wide. |
| SEC | Orphaned moltbot GitHub PAT + IAM role | Live `github/moltbot-pat` secret (repo access to ajb_workspace+portal) now consumer-less; MoltbotEC2Role unused | Andrew-gate | PENDING-ANDREW | $0 (security, not cost) | **Security cleanup:** revoke the PAT on GitHub (kills the token) + delete the AWS secret + drop MoltbotEC2Role. Orphaned repo-access credential = unnecessary attack surface. Routed to Andrew. |
| — | moltbot terminate | Last stopped zombie box (also clears final exemption) | 0.7.0_AE | PENDING (Andrew `!`) | **~$2/mo** + hygiene | `! aws ec2 terminate-instances --instance-ids i-0b784d4908e320fc4` (snapshotted; AE auto-cleans vol+manifest) |
| R7 | Secrets Manager caching | Cut per-call API charges | — | DEFERRED | ~$5-10/mo if pursued | Not scoped this cycle |
| R3c | bd-gold A_03 memory chunking → 64GB box | Further right-size below r6i.4xlarge | 0.6.0_AE | FUTURE | TBD (additional step-down) | Needs perf_history variance data (archival shipped 06-05; accrues per nightly) |

## Rollup (vs ~$600/mo baseline)

| Bucket | Items | Monthly | Confidence |
|--------|-------|---------|-----------|
| **Banked** | inf-exporter + EBS | **~$34/mo** | Verified, off the bill |
| **Applied-validating** | bd-gold right-size | **~$75-160/mo** | Live; confirms tomorrow AM |
| **Forecast-pending** | Spot + R2 + EIPs + moltbot (+Secrets opt.) | **~$75-110/mo** | Owners working; gated |
| **Preventive** | R8 cap (+ R1 attribution) | ~$50-90/mo avoided | Not counted in bill-% |
| **TOTAL (banked+applied+forecast)** | | **~$185-300/mo** | **~30-50% of bill** |

Tracks the PRD's original ~40-65% estimate; toward the conservative end because (a) the *coherent* 35d Time Machine cut recovers less than an aggressive 14d, and (b) right-size shown at the low end of its range until tonight validates.

## Soft-number caveats
1. **bd-gold right-size (the big one)** is applied but NOT yet validated — tomorrow's nightly confirms the real figure + no unacceptable slowdown. Until then it's a range.
2. **R2 is the softest** — exact GB is being computed from a streaming version-age audit; the 35d cut recovers the 36-90d noncurrent band only (0-35d retained for the Time Machine). Could move up if bloat is age-weighted to that band.
3. **R8 inf-gold sparing is empirical/probabilistic**, not structural — robust at the observed cadence (~45min bumps << 3h) but a hypothetical 3h+ pure-sub-1% I/O phase would still reap. Durable structural backstop (AutoShutdown=disabled launch-tag on the self-shutdown gold runners) is a flagged P2 follow-on — note it reintroduces a (safe, self-limiting) exemption, so it needs an explicit Andrew weigh vs the current zero-exemption posture.

## Update protocol
COO updates this doc as RAVC2s / validations land:
- R3a → after tomorrow's nightly: move APPLIED-VALIDATING→BANKED, replace range with measured $.
- R2 → after DS safety-proof + GB audit: fill exact $, then after Andrew apply-GO + apply: PENDING→BANKED.
- R3b Spot → after design review + build + validating nightly.
- R5b EIPs / moltbot → after Andrew-gated apply.
Each move appends a dated line to the Change log.

## Change log
- 2026-06-05T14:34Z — Scorecard created (COO). Initial state: R8/R4/R5a/R1 BANKED; R3a APPLIED-VALIDATING (rides tonight's nightly); R2/R3b/R5b/moltbot PENDING. Baseline ~$600/mo.
- 2026-06-05T14:40Z — Relocated to docs/briefs/ (docs/architecture is CTO-lane). Folded CVO-PASS empirical on enforcer-v1.1.1 (c7b9ae116) + the R8 probabilistic caveat #3.
- 2026-06-05T14:58Z — inf-gold R8 residual EMPIRICALLY CLOSED for tonight (CVO e17be80e4): i-0ed5 self-stopped at ~2h on chain-complete, never reached the 3h ceiling, NOT reaped — cap never in play this run. Durable AutoShutdown=disabled launch-tag remains P2 margin only for nights the chain exceeds 3h at <1%.
