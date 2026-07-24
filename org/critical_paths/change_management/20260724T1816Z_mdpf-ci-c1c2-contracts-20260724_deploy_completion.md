# Deploy Completion Record
**Date opened:** 2026-07-24T18:16:43.276529+00:00
**Status:** OPEN
**Deploy:** MDPF_CHANNEL_INDEPENDENCE.CI-C1C2 -- C1/C2 event contracts. C1 found ALREADY LIVE on 8/8 feeds (row 1 re-scoped to prove+specify-migration, not build); C2 does-not-fire, target opal-assets-daily-aua. NOTHING LANDED THIS SESSION.
**Authored by:** 0.6.2_AE_PartnerETL~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | C1 per-feed proof across 8 wired configs | landed silver per bronze landing, per-object lag, denominators stated | C1 = fires, 8/8 wired configs, DENOMINATOR STATED (8 examined, 0 unexamined). Read live from get-bucket-notification-configuration, not from a doc. Per-object event property measured like-for-like: schwab 08242234 bronze .RPS.zip landed 2026-07-24T10:15:57Z -> silver fact_rps/date=2026-07-23/ landed 10:16:04Z = +7s; the same +4..+7s pattern holds for EVERY trading day of the 07-16..07-23 'freeze' (07-16->07-17T10:16:01Z, 07-17->07-18T10:16:00Z, 07-20->07-21T10:16:00Z, 07-21->07-22T10:16:01Z, 07-22->07-23T10:16:01Z). Cross-feed median lag 0.08-1.58 min. RETRACTED ONE OF MY OWN ROWS: I first reported silver-etf-filepoint does-not-fire (0 silver); FALSE -- it is a 1->2 fan writing pathfinder/{PFDE,PFOE}/silver/fact_holdings/ per etf_conversion.py:13, current through 2026-07-23, bronze 22:00:10Z -> silver 22:00:16Z. My census derived expected silver prefix FROM the bronze prefix, so a feed violating that assumption read ABSENT rather than UNMEASURED; three corroborating signals (empty silver prefix, DLQ depth 0, log filter 0 events) all shared the assumption or measured something else. Broken by reading deployed converter source. INSTRUMENT CAVEATS STATED IN THE REPORT rather than buried: the 67-71% schwab coverage figures are a denominator artifact (bronze dates across ALL feed types vs silver dates for ONE table), as is the -0.02m median lag. ARBITRARY-DATE: UNEXERCISED by CTO ruling -- I requested authorization to land a historical bronze object and was refused on Rule 17a AND on the ground that it would not prove the property anyway; took the weaker honest evidence. | CLOSED 20260724T181754Z |
| L2 | verify | C2 existence census across 3 candidate buckets | notification configs read live; target DDB table identified | C2 = does-not-fire. DENOMINATOR: 3 candidate buckets, 3 examined. opal-data-assets: 8 configs ALL bronze-prefixed, none silver->gold. opal-data-bd: 3 configs (bd-allocation-processor forwardfill_v2/allocations/, bd-gold-trigger silver/prices/20, bd-silver-merge bronze/*_BRONZE_COMPLETE.json) -- none matching schwab/silver/*. opal-data-mdpf: notification configuration EMPTY. Target identified as opal-assets-daily-aua (HASH run_date, RANGE cohort_id, 34,950 items). Flagged that opal-partner-49financial is NOT the gold row but a user/access table (email HASH, 11 items) -- the name invites the mistake. ALSO ROUTED, not actioned: opal-assets-daily-aua has StreamSpecification=null, so PRD 2.2's C3 (DDB-Stream-triggered) has no stream to subscribe to -- 0.7.0's row, CTO informed, changes their sequence. | CLOSED 20260724T181754Z |
| L3 | git | deliverable + TO status on CLOUD | commit hash (COMMIT ONLY -- push is COO's per Andrew ~1600Z) |  | OPEN |
| L4 | activation | C2 implementation + Terraform wiring | NOT STARTED -- see close note |  | OPEN |

## Log

- 20260724T181643Z OPENED by 0.6.2_AE_PartnerETL~C with 4 leg(s)
- 20260724T181754Z LEG L1 closed: C1 = fires, 8/8 wired configs, DENOMINATOR STATED (8 examined, 0 unexamined). Read live from get-bucket-notification-con
- 20260724T181754Z LEG L2 closed: C2 = does-not-fire. DENOMINATOR: 3 candidate buckets, 3 examined. opal-data-assets: 8 configs ALL bronze-prefixed, none 
