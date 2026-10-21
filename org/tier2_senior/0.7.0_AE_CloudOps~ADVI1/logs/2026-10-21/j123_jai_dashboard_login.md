# J123 -- Jai Opal dashboard login (0.7.0_AE_CloudOps~ADVI1, 2026-10-21)

**archetype:** VALIDATE

Order: org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADHOC.J123.jai-opal-dashboard-login.md (amended twice by 1.0.0_SA_CTO~DELL1).

## What this seat did
- Registered, armed the inbox watcher (script pid 22052), read the brief and CTO msg 9150.
- Found the route: users/scripts/create_user_v2.py --firm opal-capital (internal tier). Read-only: jai@opalinvest.com ABSENT from opal-users-v2 (email-index).
- Reported the name gap (9155/9156). The CTO amended the order: J2 insert and J3 draft belong to 4.0.0_SA_CRO~JAI1.
- Flagged the J1 conflict (CRO ran on a calendar-invite name, not Andrew's word; 9166/9167). CTO ruled in 9170 that a legal gateway read of Opal records satisfies J1.
- Took the reads: BEFORE 16:58:39Z Count 0 and 17:00:16Z Count 0; AFTER 17:01:10Z Count 1 (table opal-users-v2, index email-index).
- Did NOT run the insert or the draft; the CRO did (msgs 9173, 9174).

## Compiler Tools
- aws dynamodb query/get-item (read-only, via .tools/aws): worked; PK-only projection needed (the index projects keys only).
- proof-of-spec-check.py: see the instance.
- Gateway search_email / list_chats / list_calendar: worked but found no surname; list_chats was broader than needed. Gap: the gateway has no staff-directory tool.
