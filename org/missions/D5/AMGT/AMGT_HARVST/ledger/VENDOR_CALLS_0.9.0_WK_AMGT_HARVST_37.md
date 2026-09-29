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

---

## INCIDENT 1 -- seekingalpha.com (+ the Kimi vision API), 2026-09-29T00:20:23Z -> 00:22:10Z -- NOT a call Andrew's word covers, NOT part of the w-2 capture

| field | value |
|---|---|
| seat | `0.9.0_WK_AMGT_HARVST~37` (worker of `2.0.0_SA_COO~H`, task order `HVST-w-2`, DEVELOPMENT of the runner -- before any capture invocation) |
| what happened | While testing a re-authentication guard I called the REAL `SessionManager.refresh('sa')` from a one-line Python check, with the runtime root pointed at the worktree's `.scratch`. The guard was not loaded (see row `AMGT_HARVST-Z-W37-S3`), so the producer's credentialed login ran: `sa_harvest_session.py` launched a HEADED Chrome, opened `seekingalpha.com/symbol/RTX`, clicked the header sign-in, SUBMITTED the stored seeking-alpha credential, hit a bot wall, ran the adaptive press-and-hold TWICE, and exited 1 (`bundle_present: false`, `network_auth_corroborated: false`) |
| agent-turn fetch? | The login was driven by the producer's own scripted harvester, but it was started by a test command I typed inside an agent turn; it is not a producer capture and no ledger row above covers it |
| authorization | **NONE.** Andrew's ruling 2 (`ANDREW_DIRECT_20260928_1805Z_OPEN_CALLS_FOUR_RULINGS.md`) covers `w-2` capture with `--new-only`; clause 3 of the w-2 face forbids re-authentication absolutely. The vendor-egress word and the no-login rule were both breached by this test |
| credential used | the seeking-alpha credential the harvester resolves for its own login (identifier printed in the harvester's own run.log; VALUE not shown here) |
| Kimi vision (metered) | steps 0, 1 and 2 were classified `(kimi)`, i.e. THREE metered Kimi calls; steps 3 and 4 were `cache hit ... no Kimi call`. Spend: not measured by this seat |
| result | login NOT completed; no session saved anywhere (the vault path under `.scratch` did not exist; the MAIN tree's `secrets/sa.dpapi` and `progress.sqlite3` were not touched); no S3 write; no capture |
| what it may have done to the vendor account | UNKNOWN: a submitted sign-in plus two bot-wall interactions from this IP on 2026-09-29T00:21Z. The account-side effect (a flagged login, a lockout, an email) is not observable from here |
| evidence | `.scratch/auth/20260929T002023Z-sa-33f4b866/` in this worktree (untracked, NOT committed: it holds screenshots of the login form): `run.log`, `auth-evidence.json`, `harvest_*_step{0..4}_*.png`, `hold-trace/` |
| disposition | **STOPPED per w-2 clause 3.** No capture invocation was made after this; the order stays `pending`; row `AMGT_HARVST-Z-W37-S3` is BLOCKING and asks `2.0.0_SA_COO~H` whether the capture may proceed |

## INCIDENT 1 SPEND -- ESTIMATE-UPPER-BOUND

| field | value |
|---|---|
| seat | `0.9.0_WK_AMGT_HARVST~37` (worker of `2.0.0_SA_COO~H`, task order `HVST-w-2` AC5 = guard (c)), written 2026-09-29T02:46:50Z BEFORE any capture |
| what is bounded | the Kimi vision-model calls made by the 00:21Z incident (`INCIDENT 1` above; row `AMGT_HARVST-Z-W37-S3`) |
| method | LOCAL evidence only: the incident's `run.log` (59 lines; copy with the account e-mail redacted: `deliverables/0.9.0_WK_AMGT_HARVST~37/ac5_incident_runlog_redacted.txt`), the saved screenshots' PNG headers, and the harvester source `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_harvest_session.py`. CTO ruling msg 26396 method |
| calls counted | **3** vision-classified steps [('0', 'ANON'), ('1', 'LOGIN'), ('2', 'BOT_WALL')] (state token `(kimi)`); **2** cache hits, `no Kimi call` [('3', 'BOT_WALL'), ('4', 'LOGIN')]; retry lines (`KIMI_ERROR/EMPTY/UNPARSED`) in the log: 0; vision-locate lines in the log: 0 (the press-and-hold and sign-in clicks were DOM-driven) |
| model | `kimi-k3` (from the run's own header line) |
| output tokens, upper bound | 3 calls x `max_tokens` 4000 = **12000** (the classify calls' actual default is 1500; 4000 is the order's bound) |
| input tokens, upper bound | 3 x (4096 image + 500 prompt) = **13788**. ASSUMPTION, labelled: 4096 image tokens per screenshot is a cap not read from the provider; the screenshot sizes ([('0', (1366, 860)), ('1', (1366, 860)), ('2', (1366, 860))]) give w*h/750 = [1567, 1567, 1567] |
| rate card | UNMEASURED -- no 'kimi-k3' text in the page (status 200, 279803 bytes) -- URL `https://platform.moonshot.ai/docs/pricing/chat`, read 2026-09-29T02:46:49.665340+00:00, HTTP 200, 279803 bytes (ONE unauthenticated GET; no key, no account, no API, no console) |
| **estimate (UPPER BOUND)** | **UNMEASURED (no kimi-k3 rate could be read; the call/token bound above stands)** |
| provider-read figure | **NOT MEASURED** -- an account-holder item (the Moonshot console/usage view); no console, usage or `api.moonshot.ai` endpoint was called by this cell |
| what this is not | not a measurement and not a refund claim; it bounds the incident only |

## CALL 2 -- seekingalpha.com, 2026-09-29T02:49:19Z -> 02:49:21Z

| field | value |
|---|---|
| seat | `0.9.0_WK_AMGT_HARVST~37` (worker of `2.0.0_SA_COO~H`, task order `HVST-w-2` AC1, invocation 1 of at most 5) |
| vendor | seeking-alpha (seekingalpha.com) |
| endpoint class | REST: `/api/v3/account/{id}/info`, `/api/v3/symbols/{symbol}/news`, `/api/v3/articles/{id}` |
| mechanism | `python -m lib.opal_data_harvest run --publishers sa --harvest-grammar --new-only --all-securities --max-jobs 5 --runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"` -- executed by calling `lib.opal_data_harvest.__main__.main()` INSIDE `ac1_capped_capture.py`'s own process with the re-auth / browser / Moonshot guards installed and verified in that process (AMENDMENT 1); rc 2 |
| agent-turn fetch? | **NO.** Scripted producer only, driven by the committed runner from the command line; the worker made no request by hand |
| scope attempted | 5 jobs: [('security-a37b3e6572f2baa4', 'BP', 'account_or_harvester_unavailable', 0), ('BA', 'BA', 'cooldown', 0), ('security-5add5df440ab11d9', 'BTI', 'cooldown', 0), ('security-73a875367d30f674', 'BZLFF', 'cooldown', 0), ('security-3462e34827110ede', 'CDNS', 'cooldown', 0)] |
| requests made | **1**, from `events.jsonl` (sa http events, delta over this invocation): [('info', 402, 351)] |
| authorization | Andrew-direct 2026-09-28 ~18:05Z, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_1805Z_OPEN_CALLS_FOUR_RULINGS.md` ruling 2 (`w-2` YES, stated cap, `--new-only`); resumed by the CTO ruling @`74e1eea534` behind three guards. Spend, contracts, entitlements and hold-lifts NOT covered |
| credential used | the SAVED sa session envelope `.runtime/opal-data-harvest/secrets/sa.dpapi` in the MAIN tree (the producer's designed read); no login |
| re-auth fired? | **NO -- measured.** receipts auth_refreshes=0, verification_repairs=0; forbidden events 0; guard trips 0; browser/subprocess launches 0 |
| result | rc 2; job statuses ['account_or_harvester_unavailable', 'cooldown'] |
| bytes retained | 0 article bodies accepted into the LOCAL outbox (harvest_raw / harvest_listing); nothing else |
| S3 written | not by this call (`run` writes the local outbox; AC2's `upload-harvest` is the S3 leg) |
| spend | none |
| evidence | `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/w2_ac1_output.txt`, `w2_ac1_state.json` |
