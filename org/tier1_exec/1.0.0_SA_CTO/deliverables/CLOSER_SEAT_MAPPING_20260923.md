# CLOSER SEAT MAPPING -- the `G00` activation record

**2026-09-23, `1.0.0_SA_CTO~Z`.** `CLOSER_CONTRACT.md:3` requires that *"exact seat assignments and
operating authority are recorded at activation; S/H/C/R below are logical responsibilities, not
serials."* **This is that record.** It does not seat, deploy, or authorize a vendor act.

## ANDREW-DIRECT, VERBATIM

> **"Yeah the whole idea is that the ~Z agent was on RESAPP so RESAPP work goes to them, and they read
> the claude COO~Z handoff.. This is the same plan for all the others"**

**The principle is SERIAL CONTINUITY: each closer inherits the project its predecessor Claude lane held,
and reads that lane's handoff as its context.**

## THE MAPPING

| serial | project | contract mandate | handoff to read |
|---|---|---|---|
| `2.0.0_SA_COO~X` | **`AMGT_CORPUS`** | **C** -- Corpus | `org/tier1_exec/2.0.0_SA_COO~X/handoffs/2026-09-23_1414Z.md` @`281d65b54d` |
| `2.0.0_SA_COO~Y` | **`AMGT_HARVST`** | **H** -- Publications | `org/tier1_exec/2.0.0_SA_COO~Y/handoffs/2026-09-23_1425Z.md` @`b87a99e1ef` |
| `2.0.0_SA_COO~Z` | **`AMGT_RESAPP`** | **S** -- Security data | `org/tier1_exec/2.0.0_SA_COO~Z/handoffs/` @**`4c1e845de3`** ⚠ corrected twice |

⭐ **Three of the four contract mandates map cleanly to a project and a predecessor handoff.** C/`AMGT_CORPUS`
and H/`AMGT_HARVST` are one-to-one. S is `AMGT_RESAPP`'s identity, numeric, filings, management and peers
work, which is what `~Z`'s lane actually ran.

## ⛔ WHAT THIS RECORD DOES **NOT** RESOLVE: **R HAS NO SEAT**

**R -- Report Experience** owns, per `CLOSER_CONTRACT.md:12` and `:25-28`: the per-part analysis, the gated
platinum report, five-tab consumption, history/rerun, same-revision export, **and the integration of the
common API / frontend / IaC changes FOR ALL FOUR LANES.**

⛔ **Serial continuity cannot assign R, and the reason is structural rather than an oversight: R has no
predecessor lane because the report chain was never built.** `4.0.0_SA_CRO~Z`'s own finding -- corroborated
by this seat on a wider denominator -- is that **no platinum analysis producer exists**: zero platinum
objects across `opal-data-harvest` (2,277) **and** `opal-data-assets` (795,470). **There is no handoff to
inherit because there was no seat.**

⚠ **AND R IS NOT MERELY A FOURTH WORKLOAD -- IT IS THE INTEGRATION POINT FOR THE OTHER THREE.** `:25-28`
make R the sole integration owner of `scoped_amgt.py`, the shared API client/types/hooks/routes, and the
shared `portal/src/pages/SecurityAnalysis/**`. ⛔ **S, H and C each deliver narrow patches INTO surfaces R
owns.** With R unheld, three closers implement against an integration point that has no one to land it.

### THE CTO's REC, PUT TO ANDREW AND NOT DECIDED HERE

⭐ **Do NOT fold R into `2.0.0_SA_COO~Z` alongside S.** S is the busiest existing pipeline (`AMGT_RESAPP`
carries 191 orders and the live filings work); making one seat both the busiest implementer and the sole
integrator for three peers creates a single bottleneck **exactly where the schedule's critical path runs.**

**Preferred: a fourth seat for R.** ⚠ **Second-best, and genuinely defensible: `4.0.0_SA_CRO~Z`**, which
authored the `I5`/`I6`/`I7` interface specifications and the report design. **The reservation against it is
real and should be stated: the contract makes R an IMPLEMENTER and an INTEGRATOR, and that seat's standing
role is research.** ⛔ **Either way it is Andrew's call, not mine, and not a thing three closers should wait
on.**

## WHAT PROCEEDS NOW

**S, H and C activate on this record and begin Wave 0.** Their `G00` exits -- valid seat/path ownership,
named independent reviewer, durable evidence home, versioned example payloads -- **do not depend on R
being seated.** ⚠ **What DOES depend on R is any lane's first delivery INTO a shared surface**, and each
closer states that dependency rather than routing around it.

⛔ **Standing, unchanged by this record:** `infra/logic/registry/` has no decided owner
(`3.0.0_SA_CVO~Z`, @`419263793d`); `portal/**` is `POD_DE_ANY`; `.scratch` has no entry. **A cell blocked
only on a registry row states the gap as a full result. No seat grants itself access.**

-- `1.0.0_SA_CTO~Z`
