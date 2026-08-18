# Deploy completion — THE SERVE-CORRECTION EVENT (DC1 three-site collapse + C1impl Leg B)

**Status:** CLOSED 2026-08-04 (Leg B landed + deployed 0-diff same day; AE's append never happened -- record gap, not work gap)
<!-- disposition act 2026-08-18 by 0.0.0_AB_MSTR (RED-disposition, org/tier0_exec/0.0.0_AB_MSTR/deliverables/DEPLOY_LEDGER_RED_DISPOSITIONS_20260818.md); evidence in the CLOSE block at foot. -->

**One ledger, two legs, per the JOINT GO (CTO 034247Z; CTO half 034007Z + COO co-sign 034119Z; Andrew correct-forward ruling @94f0cbef2 — disclosure dead).** Slot boundary: fired on AE's wave-ledger-close ping (0428Z → slot-open 043101Z).

---

## LEG 1 — DC1 held-family deploy (0.2.0_DS_PortfolioAnalytics) — CLOSED 04:31Z

**What:** the DC1-held builder family → repo HEAD @b50324d6f8, deployed to `s3://opal-data-mdpf/code/scripts/assets_gold/`:
relationship-grain collapse at all three sites (@3accc408f8) + Andrew's grain note (@d32695760e) + cottonwood participation-LITE (@b50324d6f8) — ONE deploy for the family, as the GO bound.

| File | Pre-state ETag (pinned pre-GO) | Post-deploy ETag (md5==ETag verified) |
|---|---|---|
| build_cottonwood_mdpf_slice.py | `44db6559905d506352a06d4585e45ae6` | `1ebf89f44225f23efab4b98b94563956` |
| build_cottonwood_mdpf_pair.py | `3c6496d869b670acd774a20cff1c093a` | `23b71cfee6ea6bebb275a9652f650ebd` |
| build_dim_model_portfolio.py | `56c82788a2539767ca258c8a62c0b18a` | `c9bb31400ad22ef499cf89ee4d5d7eca` |

**Evidence carried (built + exercised under the hold, @3accc408f8):** collapse to (AccountID, AssetID) with the BINDING equality assert (0 unequal pairs verified across all 42 live partitions before arming); exercises TIE-EXACT at every cell — 07-31 delta **−$205,070.77 exactly** at all three sites, clean-day 07-20 delta 0.00, 07-22 anchor reproduces **$457,984,488.00**; LITE fold value-output IDENTICAL pre/post with 4 honest tail exceptions.

**PRE-REGISTERED INTERPRETATION (COO co-sign text, binding):** at first corrected publish the served cottonwood series **steps DOWN by the dual-day delta — EXPECTED, CORRECT, NOT A REGRESSION**; the DDB cohort tie re-derives to the collapsed truth. The June-episode served residue corrects forward in the same event.

**Rule-22a behavioral verification (pending, scheduled-run-only):** the first v3 cycle (floor 09:00 / accrual 09:40 / publisher 09:50 ET today) rebuilds via the corrected builders; DS exercises the served artifact at first corrected publish (step-down read + participation meta presence) and reports per RAVC. A dry QA replay is not production evidence.

### Interim classification (CTO ask 044357Z, grep-grounded 044728Z): THE INTERIM SPLITS BY ROW

`channel_sources.py:446` `cot_total` reads **RAW `fact_holdings`** (`COT_HOLDINGS` :64) — the custody
channel row is **STATUS-QUO** (overstated on dual days) until Leg B lands. `cot_models` (`:472`)
reads **the COLLAPSED SLICE artifact** (`COT_PAIR_SERIES_KEY` :68-69, one-writer law) — the model
overlay row **CORRECTS EARLY** at the first slice rebuild after Leg 1 (this morning's 09:00 ET fire).
Both rows' step-downs land under the one pre-registered interpretation.

### Sequencing rider satisfied (CTO amended grant 043122Z): WS-E stale-minuend guard LANDED

@e2ae8f898d deployed + MATCH pre-gate-cut: `detect_stale_partners` self-detection (feeder content
vintages vs 2 td window incl. the mixed-vintage spread class; env = audited override only) + the
`:1012` inversion for self-detected partners (tainted block dropped → unchanged executor rolls;
stamp = worst content vintage, never max-published). Three exercise legs, the discriminator leading:
present-but-tainted DROPPED-AND-ROLLED; fresh-day empty + sha-identical; forced-stale through the
new source w/ the loud path reachable. **AE's freshness-gate cut is released to sequence.**

## LEG 2 — C1impl Leg B, emitter cot_total collapse (0.7.0_AE_CloudOps) — IN-WINDOW

AE lands the emitter change as its own targeted leg before today's 09:00 ET fire (their 043101Z: emitter artifact state verified vs the C1impl TO first). Sections to be appended by AE.

---

**Event-scope notes:** the trigger freshness-gate cut is NOT in this event (sequenced after-or-atomic-with the WS-E stale-minuend rider per CTO 042836Z + amended-grant thread — the gate stays intact today, the legacy plane stays guarded). Clock v3 live per the 0415Z wave ledger; the first corrected cycle carries BOTH legs' evidence + AE's proof-day-1 per-stage reads on ONE cycle.


---

## CLOSE (2026-08-18, 0.0.0_AB_MSTR disposition act)

Leg B (emitter cot_total collapse, 0.7.0_AE_CloudOps): landed `bf502e3c4e` (2026-08-04T17:09Z -- cot_total collapses
relationship grain before summing, vendored DC1 collapse, dual-day 07-30 delta ties DC1's 205,070.77 to the cent, tests
59/59); deployed `4634ab4fe9` (2026-08-04T18:06Z, the ONE post-17:15Z window, targeted 0/1/0, 0-diff, live CodeSha256
oV2seRZK EQUAL, emitter deploy ledger closed same-session). Current source (`opal-assets-daily-emitter/channel_sources.py`)
still carries the split this ledger bound: cot_total reads raw COT_HOLDINGS then `_collapse_relationship_grain` with the
binding equality assert; cot_models reads COT_PAIR_SERIES_KEY. `bf502e3c4e` is the last commit touching that file.
INFERRED (marked per Rule 22): the running package was re-deployed 08-11 (CodeSha n/Tu1ns1); no later commit touched
channel_sources.py, so Leg B's presence in the CURRENT package is inferred, not byte-verified -- that package belongs to
the 08-11 deploy's own ledger, not this one. This ledger's scope (the 08-04 event) is fully discharged.
