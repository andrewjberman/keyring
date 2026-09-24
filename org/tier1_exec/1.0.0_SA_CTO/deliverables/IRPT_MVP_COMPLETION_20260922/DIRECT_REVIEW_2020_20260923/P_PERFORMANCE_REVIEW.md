# P performance direct review - 2026-09-23 20:27 UTC

Backend a70f6e3b715aa082ccc35969f622ca33e37a7743; Portal a0fa8137f50c5b9f5cf3c21f6ba2e2c21c47e6dc.

**Bounded backend verdict: REWORK on returned custody identity; not ready for served COT acceptance.** Existing exact numeric account/level controls pass, but external identity parity is missing. CRO0d0fd and the current COT contract require the returned accountInfo.accountId AND externalId to agree with the authoritative mapping before its namespace is treated as confirmed. bd_selected._account checks the numeric ID only. CTO retained the exact author fixture and substituted a mapping external ID; both removing the response externalId and replacing it with another external ID still produce contract_validated=true and both provider calls. Synthetic values only; no vendor request.

Observed controls:
- Author test_bd_selected.py subset exact_account_period_series_and_source_identity or returned_identity:7 passed,14 deselected,0.98s.
- New missing externalId: contract_validated=true,2 calls (should refuse before series for bad period response).
- New different externalId: contract_validated=true,2 calls (should refuse).
- Portal performance-wire-journey.test.ts:4 passed,18 expects,881ms. Bounded source PASS for wire window/units/value normalization; full browser race proof remains author's evidence, not newly replayed CTO evidence.

Repair: preserve the actual source external account key in the server-owned mapping, require it on both period and series responses, and refuse missing/mismatch. A malformed mapping must refuse before I/O. If COT's actual served endpoint lacks this identity, report that exact missing contract; do not drop the check or infer namespace from matching numeric IDs. One matching and missing/mismatch controls suffice; no full-suite rerun requested.

The two initial scratch runs could not collect because the archive omitted _ids then data/firm_registry.json; both dependencies were restored from the SAME a70f pin before the successful run. These were review setup gaps, not implementation findings.

P's live trace reports token+period request HTTP200 with empty arrays and sentinel dataDate, responseSHA d94a5ecd795b0e35b3b738b7ba1bb442d1844a3b997aa806d2405d436e697061. Series was not called. This proves neither namespace nor entitlement. handler.run remains unwired and retained repository composition is still open. Continue building that composition while CRO/M resolve the actual source facts. No live PASS, alternate-account retry or new vendor call is implied by this review.

Reproduction uses test_bd_selected.case.__wrapped__(), adds mapping vendor_external_id=z0901234567, mutates levels[0].accountInfo.externalId in both fixture bodies to missing or z0999999999, then calls the author's run(case). Both currently return contract_validated=true. Stored fixture account IDs are synthetic.
