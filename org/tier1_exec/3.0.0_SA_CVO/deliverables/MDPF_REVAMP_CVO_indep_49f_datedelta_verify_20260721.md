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

## F1 min-day floor (§9 F1 — CVO fold) — INDEPENDENTLY CLEARED
Ran per-model `min(day)` on the current smartx silver (`smartx/platform/silver/fact_model_aum_daily`
partition `date=2026-07-21`; rmid→model_key via the canonical crosswalk bridge). All served core models
meet/precede the 2024-11-01 floor **except UST** — one named note, fully discriminated:
- `opal_ultra_short_term` (UST, funded $51.5M) serve-real starts **2025-01-16** (2.5mo past floor).
- **Discriminator (real launch vs silver gap):** served UST `model_value` = **0.0 for all 54 dates
  pre-2025-01-16**, first real **$27,294,573.69 at 2025-01-16 == the silver min_day exactly**. → UST
  **legitimately launched 2025-01-16** (F1: "later-start = named note, not redesign"), NOT a silver gap.
- **None-vs-0.0 parity risk — already handled:** builder D4 zero-pads core `None→0.0`
  (`dim_mdpf_aggregate_aua_timeseries.py:435 @6eb54c186`), so revamp UST pre-launch = 0.0 = served's 0.0.
  No None-vs-0.0 mismatch (the silent-null class DT's harness watches).
- The 2 SMAs (div/growth) carry FULL silver history; builder correctly None-pads pre-`SMA_DEPTH_START`
  (2026-05-18) per the served shape.

**NET: min-day floor SATISFIED.** Both smartx first-conversion prerequisites now independently grounded:
silver-current (07-21 partition) + min-day floor confirmed. Asked DS to ledger the UST launch date as a
named note (like `INFLECTION_MODEL_LAUNCH`).

## A4 basis structural check (CTO's stage check, pre-grounded) — CONFIRMED TO THE CENT
Independent served pull of global+49F+inflection aggregate-aua (`[-1]` @07-18):
- `enterprise_total` $1,782,163,983.16 == global_model $1,534,471,753.80 + 49F_non_model $247,692,229.36 → **diff 0.00** (enterprise structurally EXCLUDES inflection).
- global custody-non_model $312,170,328.70 == 49F $247,692,229.36 + inflection $64,478,099.34 → **diff 0.00**.
- the $247.69M(enterprise) vs $312.17M(firm-sum) gap == inflection's non_model $64.48M **exactly**.

A4 = `enterprise_total − model` = $247.69M is the 49F-FIRM non_model; the inflection-exclusion is by
construction, not a numeric fluke → the never-substitute distinction is real. CTO's stage-time check
(served A4 headline == $247.69M, not $312.17M) is armed; the served A4 non_model_assets artifact is NOT
under `.../mdpf/` (aggregate-aua + account-dist only) — I'll LOCATE its real source at stage time.

## A3/A7 account_distribution — INDEPENDENTLY PARITY-CLEAN (the one full artifact already staged)
Verified `s3://opal-data-assets/portal/model-portfolios/{firm}/account_distribution.json` vs served
`.../mdpf/{firm}/account-distribution.json`. Both firms clean:
- **Structural:** staged shape == served (`total{...}` + `by_model`), PLUS the correct `basis: schwab-rps`
  label served lacks, sourced from MONOLITH silver (49F `fact_allocation_valuation`; inflection eclipse
  `fact_portfolios_full`) — the inversion working. 49F by_model = 5 core (SMAs correctly excluded per 7→5);
  inflection = 5 core + 2 blends. No MISSING cohort.
- **Value (vintage-aware):** 49F staged(07-20) vs served(07-21) — total_aum −0.41%, account_count −0.18%,
  median +0.18%, per-model counts off 0-8 → exactly one trading day of drift, not a defect. Inflection
  staged(07-19) vs served(07-18) — **byte-identical** (0.00% everywhere).

**A3/A7 independently parity-clean.** At full-stage the staged refreshes to current and the 49F ~0.4% drift closes.

## 3-PASS GATE (spine STAGED 15:55Z) — INDEPENDENT VERDICT (pass 3 of 3)
Staged `s3://opal-data-assets/gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json` — ETags confirmed
match CTO's (49F `6e072745` / infl `a9778de4` / global `7d574a2d`, Rule 22a identity). Own from-scratch
re-derivation (`scratchpad/cvo_indep_spine_verify.py`).

**SPINE = PASS, all 3 firms:**
- Date-join clean all 3: staged 427 / served 429 / common 407 / staged-only 20 (all fresh trading) /
  served-only 22 (all non-trading holiday-fills). 0 unexplained. (Staged axis = canonical
  `trading_days_between` = 427 — the correct NYSE axis per NEVER#1; my earlier silver-distinct 428 had one
  non-canonical day the staged rightly drops.)
- Internal identities 0-mismatch @all 407 common: 49F/inflection `model==Σcore` AND `non_model==custody−model`
  to the cent. Global `model==Σ(9 core)` shows 48 diffs but **max $0.02** (count>$0.05 = 0) = sum-of-9-rounded-cohorts
  float artifact, not a defect → PASS.
- 49F @07-17: custody **D-2 = +$20,344,172.42 EXACT**; model F2 −0.0932% (in band); basis `schwab-rps`; 0 Nones.
- inflection @07-17: model+custody tie served EXACT (no D-2); 6 Nones all at feed-gaps; 0 unexpected.
- global @07-17: model F2 −0.0849% (in band); 6 Nones at feed-gaps.
- **CTO composition CONFIRMED to the cent:** global & 49F non_model staged−served @07-17 = +$21,647,872.00
  = D-2 $20,344,172.42 + F2 $1,303,699.58. Zero unexplained residual.
- Frontier 07-20 structural + sane (past served) → fresh-tail named delta.

**A4 (`gold/mdpf_revamp/global/non_model_assets.json`, 433 vs served 455):**
- 2-term CORRECT: `non_model == enterprise_total − model` @all 427 common, 0 mismatch. Served A4 is ALSO
  2-term → methodologies match. Date-join clean (427 common + 6 staged-only fresh trading + 28 served-only
  = 27 holiday-fills + 05-21 feed-gap correctly omitted). 0 unexplained.
- **INTENT FLAG — RULED (CTO 160830Z): A4 = NAMED-DELTA PASS.** Staged A4 does NOT tie served $247.69M —
  staged non_model @07-17 = $268,061,032.32 vs served $246,413,160.32 = +$21,647,872.00 = **D-2 + F2 (NOT
  SMA-drop; both 2-term)**. Cause: staged A4 enterprise_total = $1,803,111,389.71 = served + D-2 (the
  full-envelope custody). **My catch corrected a real error in CTO's criterion:** "$247.69M" is the SERVED
  *partial-cash* latest; the revamp serves the *full-envelope* (D-2) enterprise_total, so A4 SHOULD NOT tie
  $247.69M — that's serve-real. The D-2+F2 delta is fully explained, 0 unexplained → A4 PASS. SIGNED.

## Status — CYCLE 1 of N=3 = CLEAN + SIGNED (spine 3/3 + A4 named-delta), CTO 160830Z
Spine 3/3 independent concur (me + DT + CTO, to the penny); A4 named-delta PASS (criterion corrected).

## Still pending
- **Cycles 2 & 3 of N=3:** re-run my independent pass each next scheduled cycle; every named delta ruled;
  an unexplained delta resets the streak. Then never-widen co-sign (CTO+COO) → re-point.
- **Cutover co-sign cross-page item (NOT N=3-blocking):** A4 PRE-cutover enterprise_total (legacy v0_9
  passthrough, ties served-A4) vs the aggregate/spine serve-real `opal_aggregate_aua` PRE-cutover diverge
  (match post-cutover). Whether a user comparing the Portfolio-Analytics header (aggregate) vs the non-model
  page (A4) sees two enterprise_totals for the same pre-cutover date → reconcile or documented pre/post
  basis note. Weigh in at the cutover package (CTO flags when up).
- **49F account_distribution ~0.4% vintage drift** re-confirm to ~0 at a same-vintage full-stage refresh.
