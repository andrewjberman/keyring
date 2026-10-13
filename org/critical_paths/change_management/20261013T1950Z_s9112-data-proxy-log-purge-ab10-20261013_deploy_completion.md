# Deploy Completion Record
**Date opened:** 2026-10-13T19:50:30.453154+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN TO-CT-ab-10 (row S9112): delete the pre-fix log streams of /aws/lambda/opal-portal-data-proxy whose last event is before the cut 2026-10-12T11:58:21Z -- 8513 of 8550 streams, event span 2025-12-30T18:56:07Z first-event to 2026-10-12T11:47:52Z last-event (947 events in the 14-day window from 2026-09-29T20:38:26Z); 0 spanning; the deletion is NOT recoverable and is confirmed by Andrew: 'Row S9112 this can be done programmatically, i shouldnt need to be involved directly'; no other group, retention, account or secret touched
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-purge census: stream denominator and classification, subscription-filter/export read, key-name counts of pre-cut lines (refresh_token, device_trust, JWT-shaped, Bearer) | counts printed with denominator |  | OPEN |
| L2 | activation | delete-log-stream for exactly the streams whose lastEventTimestamp is before 2026-10-12T11:58:21Z; spanning stream (if any) kept and printed | streams_deleted count |  | OPEN |
| L3 | verify | post-purge census of the group by key name for lines before the cut reads 0/0/0/0; stream re-count; group retention unchanged at 14 | counts printed |  | OPEN |
| L4 | verify | expiry from the configured TTLs (refresh 7d, device_trust 30d) and rotation-path read (describe-secret metadata only) | refresh_latest_expiry, device_trust_latest_expiry, rotation_path |  | OPEN |

## Log

- 20261013T195030Z OPENED by 0.7.0_AE_CloudOps~U7 with 4 leg(s)
