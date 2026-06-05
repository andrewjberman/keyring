# AWS Cost Audit — 2026-06-05 (COO-driven, Andrew-direct)

**Account:** 313476888478 (Andrew_Berman) · **Audit by:** 2.0.0_SA_COO · **As of:** 2026-06-05T12:55Z
**Trigger:** Andrew — "hemorrhaging costs lately... feels like there are EC2s running."

## Bottom line
Not a hidden runaway. Spend is **steady ~$600/mo**, dominated by **two scheduled gold-layer
runners (53% of the bill)**. Andrew's instinct is half-right: **2 small EC2 boxes ARE running
24/7** (inf-exporter 34d, demo-transform-runner 13d) — because the auto-shutdown enforcer
explicitly excludes them with no idle backstop. No NAT/EIP leaks; EBS modest.

## Spend shape (Cost Explorer, UnblendedCost)
| Month | Total | EC2-Compute | S3 | EC2-Other(EBS) | Lambda |
|---|---|---|---|---|---|
| Apr (from 04-06) | $471 | $327 | $61 | $26 | $24 |
| May | $603 | $356 | $83 | $65 | $22 |
| Jun (01-05, 5d) | $99 | $66 | $13 | $8 | $3 |

Daily trend: stable ~$20/day through May; brief bump to **$36.70 on 06-01**, then **$13.52 on
06-04** (fabric went dark). **Not accelerating in June** — flat-to-down. The "lately" feeling
is the steady $600/mo run-rate + the Apr→May step, not a new spike.

## EC2-Compute by instance type (last 30d) — THE cost center
| $/30d | Type | Instance | Note |
|---|---|---|---|
| **$194.85** | c6i.16xlarge | bd-gold-layer-runner (+qa) | nightly bd-gold. By-design; ~57 hrs/mo. Known (34% historical). |
| **$123.70** | c6a.4xlarge | inf-gold-layer-runner | **~200 hrs/mo ≈ 6.7 hrs/day — anomalously high for a nightly runner. INVESTIGATE.** |
| $30.26 | t3.medium | inf-exporter + scheduled | inf-exporter always-on portion |
| $24.65 | t3.large | demo-transform-runner + others | demo-transform always-on portion |
| $1.14 | t3.xlarge | historical-prices-fetcher | episodic, fine |

**Two scheduled gold runners = $318.55/mo = 53% of bill.** This is the lever, and it's mostly
by-design (memory: validate on scheduled nightly, never ad-hoc — c6i.16xlarge is the long pole).

## Running EC2 right now (the "boxes that shouldn't be running")
| Instance | Type | Up since | ~$/mo | Verdict |
|---|---|---|---|---|
| inf-exporter | t3.medium | 2026-05-02 (**34d**) | ~$30 | **LEAK candidate** — excluded + no idle-ceiling = never reaped |
| demo-transform-runner | t3.large | 2026-05-23 (**13d**) | ~$61 | **LEAK candidate** — same gap; 0.6.0_AE owns demo, may need it now |
| inf-bronze-runner | t3.small | 2026-06-05 12:43Z | — | scheduled, started w/ fabric; fine |

All big runners (c6i.16xlarge ×2, c6a.4xlarge) are **stopped** at audit time — they cycle on schedule.

## Root cause — auto-shutdown-enforcer exclusion gap
`infra/aws/lambda/ec2-auto-shutdown-enforcer/main.tf`. Enforcer runs every 5 min, idle-stops at
CPU<3% for 15min. But:
- `EXCLUDED_INSTANCES` = `i-083ad9ae(inf-bronze), i-081ae6aa(inf-exporter), i-0ed5afded(inf-gold),
  i-03343a60(demo-transform), i-02448edb(mdpf-daily)` — exempt from idle-stop.
- `IDLE_CEILING_INSTANCES` backstop (branch c, reaps an excluded box idle past 3h) covers
  **ONLY `i-0ed5afded` (inf-gold)**.
- → **inf-exporter + demo-transform-runner are excluded AND have no ceiling backstop = nothing
  reaps them.** This is the EXACT gap the enforcer's own docstring (lines 13-15) warns about.

## Other (ruled out / minor)
- **No NAT gateways, no Elastic IPs** billed anywhere — classic silent killers ABSENT. Good.
- EBS: 29 vols / 866 GB / **~$69/mo**. **4 unattached** (44 GB, ~$4/mo, from Feb 17:
  docker-builder-temp + 3 bd-snapshot vols) — safe cleanup. 1 snapshot, 30 GB (~$2/mo), negligible.
- 16 other EC2 instances all **stopped** (daily-runner pattern: bd-allocations/transactions/
  assets/fees, mdpf-daily, historical-prices-fetcher ×N, seeking-alpha, moltbot).
- All resources in **us-east-1**; other 16 regions clean.

## Remediation (routed to 0.7.0_AE_CloudOps)
1. **inf-exporter (34d):** check CloudWatch CPU — is it a persistent service or an idle episodic
   exporter? Confirm with inf owner. If episodic → stop + add to `IDLE_CEILING_INSTANCES` (not
   just stop, or it recurs). ~$30/mo.
2. **demo-transform-runner (13d):** confirm with 0.6.0_AE (live, owns demo). If not needed for
   DEMOAUTH.002 work → stop + add to idle-ceiling. ~$61/mo.
3. **inf-gold-layer-runner c6a.4xlarge:** investigate the ~6.7 hr/day runtime — run frequency,
   run duration, prompt-stop. Biggest single right-sizing lever after by-design bd-gold. ($124/mo)
4. **Close the enforcer gap generally:** any instance in `EXCLUDED_INSTANCES` that isn't a true
   always-on service should also be in `IDLE_CEILING_INSTANCES`. Make ceiling-coverage the default
   for excluded batch runners (the docstring already prescribes this).
5. **Delete 4 unattached volumes** (~$4/mo) after snapshot-need check.

**Cost discipline:** do NOT trigger ad-hoc gold runs to validate — verify on the scheduled
nightly (memory: c6i.16xlarge = 34% of bill). All remediation is stop/config, no manufactured runs.
