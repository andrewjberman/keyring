# Deploy completion — THE SERVE-CORRECTION EVENT (DC1 three-site collapse + C1impl Leg B)

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

## LEG 2 — C1impl Leg B, emitter cot_total collapse (0.7.0_AE_CloudOps) — IN-WINDOW

AE lands the emitter change as its own targeted leg before today's 09:00 ET fire (their 043101Z: emitter artifact state verified vs the C1impl TO first). Sections to be appended by AE.

---

**Event-scope notes:** the trigger freshness-gate cut is NOT in this event (sequenced after-or-atomic-with the WS-E stale-minuend rider per CTO 042836Z + amended-grant thread — the gate stays intact today, the legacy plane stays guarded). Clock v3 live per the 0415Z wave ledger; the first corrected cycle carries BOTH legs' evidence + AE's proof-day-1 per-stage reads on ONE cycle.
