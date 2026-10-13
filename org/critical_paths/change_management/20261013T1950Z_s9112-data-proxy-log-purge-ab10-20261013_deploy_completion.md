# Deploy Completion Record
**Date opened:** 2026-10-13T19:50:30.453154+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T200755Z
**Deploy:** NFRA_CTLPLN TO-CT-ab-10 (row S9112): delete the pre-fix log streams of /aws/lambda/opal-portal-data-proxy whose last event is before the cut 2026-10-12T11:58:21Z -- 8513 of 8550 streams, event span 2025-12-30T18:56:07Z first-event to 2026-10-12T11:47:52Z last-event (947 events in the 14-day window from 2026-09-29T20:38:26Z); 0 spanning; the deletion is NOT recoverable and is confirmed by Andrew: 'Row S9112 this can be done programmatically, i shouldnt need to be involved directly'; no other group, retention, account or secret touched
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-purge census: stream denominator and classification, subscription-filter/export read, key-name counts of pre-cut lines (refresh_token, device_trust, JWT-shaped, Bearer) | counts printed with denominator | describe-log-streams auto-paginated, counted client-side: streams_listed=8550 (a per-page --query length printed 50-row pages ending in 49; not used as the count); lastEventTimestamp before cut 8513, spanning 0, no-events 0, post-cut 37. Group retention 14 days, storedBytes 208826. describe-subscription-filters: none (subscriptionFilters []); export tasks naming the group: none. Pre-cut events (filter-log-events, end-time cut-1, no pattern, regexes applied locally, no body printed or stored): 947 events 2026-09-29T20:38:26Z..2026-10-12T11:47:52Z; refresh_token 20 events (16 within 7d of cut), device_trust 14 (10 within 7d), JWT-shaped 31, Bearer 31; latest lines refresh/device_trust 2026-10-11T03:08:59Z, JWT/Bearer 2026-10-12T09:57:34Z. Post-cut events (132) carry 0 of all four. The order's 38 / 29 line counts were not reproduced (20 / 14 by event and by occurrence); recorded as a discrepancy, not explained. | CLOSED 20261013T195105Z |
| L2 | activation | delete-log-stream for exactly the streams whose lastEventTimestamp is before 2026-10-12T11:58:21Z; spanning stream (if any) kept and printed | streams_deleted count | boto3 delete_log_stream on /aws/lambda/opal-portal-data-proxy only, over a fresh listing taken at run time (8550 listed; 8513 with lastEventTimestamp before 2026-10-12T11:58:21Z; 0 spanning, 0 no-events): streams_deleted=8513 failed=0, ~12 min. No other group, no retention change, no secret or account touched. | CLOSED 20261013T200651Z |
| L3 | verify | post-purge census of the group by key name for lines before the cut reads 0/0/0/0; stream re-count; group retention unchanged at 14 | counts printed | Post-purge re-list (auto-paginated, client-side): streams_listed=37 pre=0 spanning=0. Group retention still 14. Pre-cut census over filter-log-events end-time cut-1: events=0; refresh_token 0, device_trust 0, JWT-shaped 0, Bearer 0. POSITIVE CONTROL: the same read without the end-time returns post-cut events (per-page lengths sum to 132, equal to the pre-purge post-cut count), so the zero is not a failed read. The order's 38/29 vs the 20/14 measured: the earlier read (2026-10-12T11:35Z) held 1202 events over a window reaching back to 09-28; this seat's read held 947 pre-cut from 09-29T20:38Z, so aged-out retention explains the gap; the 16 in-window refresh lines match. | CLOSED 20261013T200651Z |
| L4 | verify | expiry from the configured TTLs (refresh 7d, device_trust 30d) and rotation-path read (describe-secret metadata only) | refresh_latest_expiry, device_trust_latest_expiry, rotation_path | Record org/tier2_senior/0.7.0_AE_CloudOps~U7/deliverables/NFRA_CTLPLN.TO-CT-ab-10.s9112-purge-record.txt: refresh_latest_expiry=2026-10-18T03:08:59Z (latest line 2026-10-11T03:08:59Z + 7d, jwt.ts REFRESH_TOKEN_EXPIRY), device_trust_latest_expiry=2026-11-10T03:08:59Z (+30d, deviceTrust.ts). Secret opal/auth/jwt-private-key describe-secret metadata only: RotationEnabled null, no rotation Lambda; manual runbook exists: org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/JWT_SIGNING_KEY_ROTATION_RUNBOOK.md (no-sign-out rotation; retiring the previous slot, its step 7, is a separate cut). Nothing rotated, no account touched, no secret value read. | CLOSED 20261013T200755Z |

## Log

- 20261013T195030Z OPENED by 0.7.0_AE_CloudOps~U7 with 4 leg(s)
- 20261013T195105Z LEG L1 closed: describe-log-streams auto-paginated, counted client-side: streams_listed=8550 (a per-page --query length printed 50-row 
- 20261013T200651Z LEG L2 closed: boto3 delete_log_stream on /aws/lambda/opal-portal-data-proxy only, over a fresh listing taken at run time (8550 listed;
- 20261013T200651Z LEG L3 closed: Post-purge re-list (auto-paginated, client-side): streams_listed=37 pre=0 spanning=0. Group retention still 14. Pre-cut 
- 20261013T200755Z LEG L4 closed: Record org/tier2_senior/0.7.0_AE_CloudOps~U7/deliverables/NFRA_CTLPLN.TO-CT-ab-10.s9112-purge-record.txt: refresh_latest
- 20261013T200755Z CLOSED -- all 4 legs proven
