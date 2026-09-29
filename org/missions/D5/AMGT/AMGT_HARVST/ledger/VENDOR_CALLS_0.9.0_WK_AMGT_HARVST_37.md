# VENDOR CALL LEDGER -- `0.9.0_WK_AMGT_HARVST~37`, AMGT_HARVST (task order `HVST-w-5`)

**Why this file exists.** The ledger is a condition of Andrew's word (ANDREW_DIRECT_20260928_1805Z ruling 2), not
paperwork. Same shape as `VENDOR_CALLS_0.9.0_WK_AMGT_HARVST_22.md` beside it.

**No entry here covers spend, a contract, an entitlement or a hold-lift.** No re-authentication, browser or
vision call is covered or was reached.

---

## CALL 1 -- bloomberg.com, 2026-09-28T23:44:30Z -> 23:44:35Z

| field | value |
|---|---|
| seat | `0.9.0_WK_AMGT_HARVST~37` (worker of `2.0.0_SA_COO~H`, task order `HVST-w-5`, AC1) |
| vendor | bloomberg (`www.bloomberg.com`, `login.bloomberg.com`) |
| endpoint class | REST: `GET login.bloomberg.com/user-info` (session check) and `GET www.bloomberg.com/nemo-next/api/search/query?query=Lenovo` |
| mechanism | `python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/ac1_one_call_pair.py` -- imports `check` and `search` from `org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py` (curl_cffi chrome impersonation) on the parked session `bloomberg/session`; `lib.opal_data_harvest` NOT imported; a recording proxy refuses any repeat call |
| agent-turn fetch? | **NO.** Scripted transport run from a command line; the worker constructed no HTTP client and pasted no payload. The script printed classifications only; no 200 body is retained or printed |
| scope | exactly 2 calls: 1 x `/user-info`, 1 x `search/query` (query `Lenovo`); no retry, no second security |
| authorization | Andrew-direct 2026-09-28 ~18:05Z, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_1805Z_OPEN_CALLS_FOUR_RULINGS.md` ruling 2, verbatim answer "2.) Rec approved." -- `w-5` YES, one bounded run, diagnostic only, no data written, scripted producer, ledgered by the seat that runs it. Spend, contracts, entitlements and hold-lifts NOT covered |
| credential used | the PARKED session envelope in AWS Secrets Manager `bloomberg/session` (GetSecretValue, the transport's designed read); captured_at `2026-09-11T05:13:28.386718Z`, age at call 426.52 h, 63 cookies; VALUES never printed or written |
| re-auth fired? | **NO -- measured.** login_attempted=False, browser_started=False, vision_call=False; only the two recorded calls reached the network (hosts ['login.bloomberg.com', 'www.bloomberg.com']) |
| result | `/user-info` HTTP 200 (549 B); `search/query` HTTP 403 (535 B, title None, markers ['px-cloud', 'captcha', 'blockScript', 'appId', 'jsClientSrc'], 535-byte body: True) |
| bytes retained | `ac1_capture.json`: status/bytes/header names+values (set-cookie names only)/classification for both calls; the refusal body text ONLY if non-200 (it is a bot-wall page, not data); NO 200 body |
| S3 written | none |
| spend | none |
| evidence | `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/ac1_capture.json`, `ac1_output.txt` |
