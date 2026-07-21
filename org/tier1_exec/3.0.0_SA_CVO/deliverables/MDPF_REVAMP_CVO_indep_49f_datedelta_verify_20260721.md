# MDPF_REVAMP — CVO INDEPENDENT verify: 49F aggregate-aua date symmetric diff

**Verifier:** 3.0.0_SA_CVO (main CVO, base) · **Date:** 2026-07-21T14:41Z
**Scope:** independent second-source verify of the gate-critical named-delta (the 49F
aggregate-aua-timeseries date SET divergence) that gates whether an N=3 parity cycle can count.
**Grounding:** live S3 exercise (read-only) + `lib/trading_calendar.py` (canonical NYSE, the estate's
single frontier definition, NEVER#1). NOT a re-run of DS's `enumerate_49f_date_delta.py` and NOT
DS's `load_aum_daily` — my own from-scratch derivation (`scratchpad/cvo_indep_49f_datedelta.py`).

## Why (independent, not rubber-stamp)
CTO gate 135429Z/142516Z: "ANY date you cannot explain is a BUG"; the full symmetric diff must be a
FULLY-EXPLAINED named delta before N=3 counts. DS delivered the enumeration (producer self-report until
independently grounded). §8 assigns CVO the parity verify, grounded on the SERVED artifact, not the
producer. So I re-derived the SETS myself and classified every date against the canonical calendar.

## Method
- SERVED (legacy, ground truth): `s3://opal-data-portal-v2/json/mdpf/49financial/aggregate-aua-timeseries.json` → `dates[]`.
- SERVE-REAL axis: rebuilt directly from `s3://opal-data-assets/smartx/platform/silver/fact_model_aum_daily`
  latest partition (`date=2026-07-21`), distinct `day >= 2024-11-01`.
- Classifier: `lib.trading_calendar.is_trading_day` (source string: `NYSE/hardcoded-fallback-2024-2027`).
- Data-presence: per published-only date, count silver rows + nonzero `closing_equity` + sum.

## Result (grounded 2026-07-21T14:39Z) — CONFIRMS DS to the date
| set | n |
|---|---|
| SERVED (legacy) | 429 (2024-11-01 .. 2026-07-18) |
| SERVE-REAL | 428 (2024-11-01 .. 2026-07-20) |
| COMMON | 408 |
| SERVED-ONLY | 21 — **all 21 non-trading** (0 real days dropped) → synthetic holiday-fills correctly omitted |
| PUBLISHED-ONLY | 20 — **all 20 real NYSE trading days WITH real measured data** (8 rows/7 nonzero models each; `closing_equity` $1.119B→$1.425B scaling over time; 07-20 = 7 rows/7 nonzero) |
| **UNEXPLAINED** | **0** |

**VERDICT: CLEAN.** The 49F date symmetric diff is a fully-explained named structural delta; CTO's
"unexplained = BUG" bar is independently MET. Parity should be scored on the 408 COMMON dates, with the
21 served-only + 20 published-only as the KNOWN delta.

## Actionable catch (the value beyond confirmation) — vintage-frozen locked criteria
My derivation independently confirms the axis is now **428, not 427** (07-20 real trading tail added
since CTO's count). CTO's 142516Z LOCKED per-firm criteria `len==427` and `custody[-1]==$1,665,338,126.76`
are keyed to the 07-17/18 vintage and will **false-fail at stage time**:
- **len is dynamic** = n real NYSE trading days in `[2024-11-01 .. current aum frontier]` = 428 today, growing daily. Literal `len==427` false-fails.
- **positional `[-1]` is wrong-axis one level up.** Mine[-1]=07-20 (published-only); served[-1]=07-18 (a **Saturday synthetic fill**); last real served trading day = 07-17. The sound latest-tie is at the **LAST COMMON date = 07-17**: `mine[@07-17]==served[@07-17]`. The exact custody/model targets must be **re-derived at the stage-time frontier**, not frozen.

**Recommendation (sent to CTO + DT):** re-anchor the locked S3 re-verify criteria to date-key semantics
before staging — `len==(stage-time real-axis count)`, latest-tie + internal-identity checks evaluated at
the last-common date via DATE-JOIN, fresh tail recorded as a named published-only delta. Otherwise a
correct build false-fails and resets N=3 for nothing. (Verification Law #6: a rigorous instrument on the
wrong axis SURVIVES review.)

## Still pending (my stage-time verify, per §8)
The spine (`aggregate-aua-timeseries`) is NOT staged yet — only `account_distribution.json` for the 3
firms is on `s3://opal-data-assets/portal/model-portfolios/` (07-20). At stage time I run my independent
S3 pass in parallel with CTO's: `basis:schwab-rps` never-sum/never-substitute (distinct value_class:
custody vs model), the internal identities (`non_model[i]==custody[i]-model[i]`, `model[i]==Σ core by_model[i]`),
date-joined, and the F1 min-day floor (`min(day) ≤ 2024-11-01` per funded model) — two independent passes.
