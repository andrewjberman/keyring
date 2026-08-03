# Deploy completion — cottonwood slice rows 4+7 restructure (T1.C, ruling-gated)

**Deployer:** 0.2.0_DS_PortfolioAnalytics (Rule-13 DS gold lane) · **Opened/closed:** 2026-08-03 21:55–22:00Z (single-leg, in-session)
**What:** `s3://opal-data-mdpf/code/scripts/assets_gold/build_cottonwood_mdpf_slice.py` → repo HEAD @31af5a04f1 (md5 both sides `44db6559905d506352a06d4585e45ae6`; supersedes the G7-era pin `68539df870f6...` in the 20260729T0510Z ledger).
**Authority chain:** T1.C TO (COO GO @760e567895) → row-4 STOP fired per reprocess guard (parity diff: 5 measured weekend custody values) → **CONVERGED RULING CTO+COO 20260803T215349Z: (b) pure canonical axis + mandatory (b+) declaration rider; DO-NOT-DEPLOY lifted by the ruling.**

## The change (rows 4+7 + b+)

1. **Row 4 — self-derived axis:** canonical NYSE days `SERVED_AS_OF_FIRST..own measured frontier` (max of model/holdings legs); the GLOBAL-artifact axis import removed (was the 6d circularity's cause). Non-trading dates never enter (ruling ground: global unions feeder axes — dim `:1779`).
2. **Row 7 — pattern-parity emission:** `meta.source_vintage` (per-leg vintages, `frontier_basis` citing the T2.B RULING semantic — no clock value, clock-v2-safe), `trading_day_calendar`, `latest_cross_section`, informational `trading_days_behind` beside the DECLARED D+2 cadence (never a verdict alone).
3. **(b+) rider:** `meta.axis_rule` declares the rule + enumerates measured-but-excluded observations (computed self-maintaining; verified == the ruling's 5: 2026-06-13/14/19/20/21) with the never-measured padding class (9 dates) stated separately.

## Verification legs

| Leg | Check | Result |
|---|---|---|
| L1 | commit-gate | clean (both commits @4d442fac2a, @31af5a04f1) |
| L2 | Dry-run QA on live inputs | axis 436 NYSE days [2024-11-01..2026-07-31]; ALL GATES PASS; composed 445; source-vintage prints; rc=0; no writes |
| L3 | Past-date parity diff vs live artifact | 441/441 common dates IDENTICAL on model_aua/by_model/cohort_provenance; 9 live-only all-None padding; 4 new-only = frontier advance; the 5 measured-weekend drops RULED (b) with (b+) rider |
| L4 | Rider enumeration | computed set == the ruling's 5, exactly |
| L5 | Deploy + verify | `aws s3 cp` + md5==ETag MATCH (`44db6559905d...`) |

## Behavioral verification (pending, scheduled-run-only)

Next chain cycle reaching 6d (post-6c-repair, see 20260803T2125Z ledger) rebuilds the slice from the deployed copy: expect the served-side artifact to carry the new axis/meta after accrual+publisher propagate. Evidence window per T1.C row 12 (clock v2 apply pending AE). The 07-29-era live artifact stays served until then — correct, no hand-publish (NEVER#4a).
