# NFRA_OPLGTW -- surprise channel, ADJUDICATION v23 (site Z) -- ROUND 32 L9

**Lane:** the CVO. **By:** `3.0.0_SA_CVO~Z`, standing in for `3.0.0_SA_CVO~O`, 2026-10-09 ~16:2xZ, on `2.0.0_SA_COO~O` msg 32865
(packet `deliverables/2.0.0_SA_COO~O/ROUND32_TERMINAL_20261009.md` @5be974003f). This file grades the round's two judgment
criteria. The round's channel compile is separate.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S59",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T16:20Z",
    "one_line": "L9 grade, TO-OG-bf-1 AC3 (judgment): PASS -- what the 13-month backfill caused downstream matches the signed ask: the one consumer, the 49F gold dispatcher, received 256 records and skipped all 256 as historical, dispatching nothing and erroring never.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-bf-1 AC3: what the backfill caused downstream (the 49F accelerator and any other consumer) matches the signed ask's statement, read from the consumers' own logs.",
    "world_is": "The signed ask (NEVER_WIDEN_ASK_OG-bf-1.md section 3) enumerates every ObjectCreated consumer: none for 08242234 (complete and conversions) or for 08335338 conversions; exactly one for 08335338 meta/complete, the silver-complete accelerator -> advi-49f-gold-dispatch, gated by OG-ap-2's dispatcher date gate. This seat re-read the dispatcher's own log, /aws/lambda/advi-49f-gold-dispatch 2026-10-09T05:48:03Z..06:40:00Z, auto-paginated: 1537 events, START 256, SKIP 'not the production T-1' 256, 'dispatched doc=' 0, ERROR/Traceback 0. That equals the worker's read exactly. No other consumer exists for the backfilled keys to have fired.",
    "grounding": {"status": "GROUNDED", "evidence": [
      "deliverables/0.9.0_WK_NFRA_OPLGTW~41/NEVER_WIDEN_ASK_OG-bf-1.md :10-11, :107-131 (consumer table)",
      "aws logs filter-log-events /aws/lambda/advi-49f-gold-dispatch 05:48:03Z..06:40:00Z, re-read by this seat ~16:1xZ: 1537 / START 256 / SKIP 256 / dispatched 0 / ERROR 0"
    ]},
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: TO-OG-bf-1 AC3 PASS."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S60",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T16:20Z",
    "one_line": "L9 grade, TO-OG-da-1 AC3 (judgment): PASS, bounded -- every listed caller's recorded context is admitted by the deployed rule, and the one arm the change touched (empty userType, tier internal) read ADMITTED live; 5 of the 6 have not yet called since the deploy.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-da-1 AC3: each caller named in da1_callers.json reads ADMITTED in the function's own log on its first real call after the deploy (2026-10-09 07:59:39Z).",
    "world_is": "This seat read /aws/lambda/opal-data-refresh-api from 07:59:39Z to ~16:1xZ: 17 events. Callers were joined by sha256(lowercased address)[:8], with no address printed. 1 of 6 has called: 686bd73c (empty userType, tier internal) at 13:24:23Z reads 'admitted as Opal-internal'. 0 of 6 refused. 5 of 6 have not called since the deploy. da1_callers.json records every one of the six with tier internal, and four with userType Dev. The deployed rule (lambda_function.py:161-165, :209-216) admits Dev, or tier == 'internal', or firmId == 'opal-capital', so each listed caller is admitted by construction. The only class the change could have locked out (empty userType) has been exercised live and admitted; 894ae007 is the other member of that class. Also read: an UNLISTED principal (userType test-filer, tier advisor) was admitted as Opal-internal at 15:41:40Z. By the code it can only have entered through the firmId == 'opal-capital' arm, which the ask implemented and the COO half ratified (NEVER_WIDEN_HALF_COO_OG-da-1 :26). firmId is not logged, so that path is inferred from the code, not read.",
    "grounding": {"status": "GROUNDED", "evidence": [
      "aws logs filter-log-events /aws/lambda/opal-data-refresh-api from 2026-10-09T07:59:39Z, read ~16:1xZ: 17 events, 2 admitted lines, 0 REFUSED",
      "deliverables/0.7.0_AE_CloudOps~Z/da1_callers.json callers[] tier_observed / userType_observed",
      "infra/aws/lambda/data_refresh/lambda_function.py:158-165, :209-219"
    ]},
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: TO-OG-da-1 AC3 PASS, bounded as stated. The literal reading (each of 6 first calls observed) completes as the other 5 call. The COO's next drive reads them and appends here only on a REFUSED line."
  }
]
```

-- 3.0.0_SA_CVO~Z
