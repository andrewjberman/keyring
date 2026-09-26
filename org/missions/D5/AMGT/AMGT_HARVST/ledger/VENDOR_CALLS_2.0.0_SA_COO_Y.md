# VENDOR CALL LEDGER -- `2.0.0_SA_COO~Y`, AMGT_HARVST

**Why this file exists.** Andrew-direct 2026-09-26 ~03:xxZ, verbatim: *"Egress is permitted for API calls
this session -- no per-use word per vendor call, but every call is ledgered by the seat that makes it.
Spend, contracts, entitlements and hold-lifts are NOT covered."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md`
@`f3b85ff6a5` section 1, relayed as msg 25989. **Per-seat ledgering is a CONDITION, not a courtesy: a seat
that cannot ledger its call does not have the word.**

⛔ **THE LIFT IS ON THE AUTHORIZATION, NOT THE MECHANISM.** Every row below ran from the EXISTING SCRIPTED
PRODUCER invoked from a command line. A vendor byte fetched inside an agent turn is a FAIL ON MECHANISM even
if the data is right, and no row here may ever record one.

**No entry in this file covers spend, a contract, an entitlement or a hold-lift.** Those are outside the
word and stay sovereign.

---

## CALL 1 -- seeking-alpha, 2026-09-26T02:17:52Z

| field | value |
|---|---|
| seat | `2.0.0_SA_COO~Y` |
| vendor | seeking-alpha (`seekingalpha.com`) |
| endpoint class | REST, `/api/v3/symbols/{symbol}/news` (search/listing + article bodies) |
| mechanism | `python -m lib.opal_data_harvest run --publishers sa --harvest-grammar --security-json org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST/sa_one_security_992HK.json --max-jobs 1` |
| agent-turn fetch? | **NO.** Scripted producer, run from the main tree so the session vault resolves |
| scope | ONE security, `992_HK_Equity` (sa_symbol `LNVGY`), `--max-jobs 1` |
| authorization | **Andrew-direct ~02:1xZ, per-use and PRIOR to the session-wide lift**, verbatim: *"you have egress. hit the rest api with the existing token/auth, if that does not work, then we have the browser crawl sa harvest setup for the purpose of re-authenticating"* |
| credential used | the SAVED session envelope `.runtime/opal-data-harvest/secrets/sa.dpapi`, dated 2026-09-15 |
| re-auth fired? | **NO.** The saved envelope was still valid server-side, so `auth.py:23-24` short-circuited and `refresh()` -- the headed credentialed login -- was never reached. The authorized fallback went unused |
| result | rc 0, `status: complete_candidates`, `accepted: 5` |
| bytes retained | 1 listing page (137,260 B) + article records, into the LOCAL outbox |
| S3 written | **NONE by this call.** `run` writes only the local outbox; the S3 put is the separate `upload-harvest` |
| spend | none -- an entitlement already held; no metered or paid endpoint |
| evidence | `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST/sa_live_20260926/run1.log` + `STATE.json` |

**Follow-on, non-vendor and recorded here only because it shares the act's evidence:** `upload-harvest
--max-objects 40` rc 2, `ArrowNotImplementedError`. That call touches S3 and the local outbox and makes NO
vendor request. It failed on our own parquet writer (`themes` = `{}` types as `struct<>`, which parquet
cannot write) and is filed as row `AMGT_HARVST-Z-S28`. **The 20 listing rows remain `pending` in the outbox,
so nothing must be re-fetched from the vendor to complete the write.**

---

## THE CLOCK, and it is the part most likely to be missed

**The word is scoped to THIS SESSION.** A cell that sits in a queue past the session's end loses its
authorization SILENTLY -- nothing refuses, the seat simply no longer holds the word it thinks it holds.
Any future row in this file states the authorization it ran under at the time it ran, never the one that was
live when the cell was written.

---

## CALL 2 -- seeking-alpha symbol-resolution pass, 2026-09-26 ~19:3xZ (batch 1) and ~19:5xZ (batch 2)

| field | value |
|---|---|
| seat | `2.0.0_SA_COO~Y` |
| vendor | seeking-alpha (`seekingalpha.com`) |
| endpoint class | REST, `/api/v3/searches` (symbol search) + `/api/v3/symbols/{s}/news` (density corroboration) |
| mechanism | `python org/tier1_exec/4.0.0_SA_CRO/scripts/sa_symbol_resolve_pass.py --exclude-done <prior> --limit N --sleep 20 --out <batch>` |
| agent-turn fetch? | **NO.** The existing scripted producer, unchanged, run from the command line |
| authorization | **Andrew-direct 2026-09-26 ~19:2xZ, verbatim: "Run it right now."** Under the session egress term (@`f3b85ff6a5` s.1) |
| credential used | **NONE. This producer is deliberately UNAUTHENTICATED** -- direct HTTPS, no cookie, no proxy, no quota. Its own header records why: the vendor path returned a smaller, structurally corrupted payload than the direct GET |
| batch 1 | `--limit 20`, **54 calls, ZERO vendor refusals.** 38 records, 38 asked, 36 resolved, 2 REFUSED on evidence |
| batch 2 | `--limit 26`, **40 calls.** Stop guard fired on 3 consecutive refusals: 13 search-refused, 10 never reached. 64 records, 51 asked, 49 resolved, 2 refused on evidence |
| **net movement** | **sa_symbol resolved 18 -> 49 of 89.** Serveable at the density bar: **16 of 51 asked** |
| spend | none -- an unmetered public endpoint, no entitlement consumed |
| S3 written | **NONE.** Both batches write one local JSON artifact each |
| evidence | `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST/sa_symbol_pass_20260926/` (batch1/2 `.json` + `.log`) |

⛔ **THE BLOCKER WAS RATE LIMITING, NOT AUTHENTICATION, AND THIS SEAT HAD IT WRONG IN THE CARD IT
RAISED.** The card recommended running the pass "authenticated" and said tonight supplied "both things that
pass lacked: the egress word and a proven-valid session." **The producer takes no session and never has.**
What the word supplied was permission; what moved the number was that the 403 measured on 2026-09-14 had
DECAYED -- batch 1 took 54 calls without a single refusal. **The refusal then returned inside batch 2**, which
is the same intermittent, burst-sensitive behaviour the 09-14 artifact recorded, re-measured five days later.

⭐ **STOPPED RATHER THAN RETRIED.** The producer's stop guard fired at 3 consecutive refusals and this seat did
not re-run it. ~38 names remain unanswered (13 search-refused, 10 never reached, the rest not yet in
population). The block decays over hours; another burst now re-extends it and costs the headroom the remainder
needs.

---

## CALL 3 -- bloomberg.com, 2026-09-26 20:32Z (harvest 1), 20:46Z (crawl 1), 22:03Z (crawl 2), 22:26Z (harvest 2)

| field | value |
|---|---|
| seat | `2.0.0_SA_COO~Y` |
| vendors touched | **bloomberg.com** AND **api.moonshot.ai (Kimi-VL)** -- two, and the second is METERED |
| authorization | **Andrew-direct 2026-09-26, verbatim: "Run that after SA, we have a bbg harvest script designed for this that has succeeded. If we do not have a functioning cookie, then we need to be using that re-harvester crawl to get it, just like the pattern decrees."** |
| mechanism | `python -m lib.opal_data_harvest run --publishers bbg --harvest-grammar --runtime-root <main> --all-securities --max-jobs 8`; re-auth via `python bloomberg_harvest_session.py --max-steps N`; install via `import-session --publishers bbg` |
| agent-turn fetch? | **NO.** Existing scripted producers throughout, unchanged |
| harvest 1 | envelope `captured_at 2026-09-15T03:42:10Z`. `HTTP 200 bytes=549` -> verification fired -> repair was a NO-OP (`challenge_observed: false`, `script_actions: 0`) -> job `error` (HTTPError). `auth_refreshes: 0`. Jobs 2-8 `cooldown`, 0 attempts |
| crawl 1 | **FAILED rc=1.** Every Kimi classify/locate returned **HTTP 429** across 14 steps -- the account was OUT OF CREDITS (Andrew diagnosed and refilled). Never classified a screen, never reached OAuth. `resolved=False` |
| crawl 2 | **SUCCEEDED rc=0.** Press&Hold solved on a cached perceptual match, `signin_iframe` -> Continue with Google -> OAuth popup -> vision handoff -> step 9 **`resolved=True`, LOGGED_IN**, 47 auth events, 124 cookies. Bundle written, 142 cookies |
| install | `import-session --publishers bbg` -> DPAPI envelope rewritten 18:18 local (44,358 B) |
| harvest 2 | envelope `captured_at 2026-09-26T22:07:12Z` (20 minutes old, LOGGED_IN). **`HTTP 200 bytes=549` AGAIN -> verification -> `request_rejected`.** `auth_refreshes: 0` |
| spend | ⛔ **Kimi/moonshot credits WERE consumed by crawl 2.** Metered third party. Andrew refilled the account himself immediately before authorising the retry, so the spend is his act and his word; it is recorded here rather than inferred to be free. bloomberg.com itself: an entitlement already held, nothing metered |
| S3 written | **NONE.** No object reached bronze or silver from any bbg run |
| evidence | `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST/bbg_run_20260926/` (`run.log`, `reauth_crawl.log`, `reauth_crawl2.log`, `run2.log`) |

⛔ **THE CRAWL WAS NOT NEEDED AND THE MEASUREMENT PROVES IT. Andrew-direct, verbatim: "if you have a long
term cookie that is working, then you do not need to do the crawl, the only reason you need to do the crawl
is if the long term trust token is not working."** This seat inferred the token was bad from a verification
challenge and escalated straight to a credentialed headed crawl **without first testing the token.**

⭐ **THE DISCRIMINATING PAIR, same code path, only the token differs:** a **5-day-old** envelope and a
**20-minute-old LOGGED_IN** envelope both produced `HTTP 200 bytes=549` and both died at the same
verification wall (`error`, then `request_rejected`). `auth_refreshes: 0` in both. **A fresh trust token
changed NOTHING, so the token was never the failing axis.**

⭐ **THE FREE CHECK THAT WAS SKIPPED IS IN BOTH LOGS: THE 549-BYTE HTTP 200.** A signed-in search response is
not 549 bytes -- that is an interstitial. Reading that body costs one read and answers "is this token
working" before anyone spends a credentialed crawl and a metered vision quota. **COST: one read of a
response already fetched. NON-APPLICATION: a failure whose first response never arrives at all.**

**WHAT bbg's BLOCKER ACTUALLY IS:** a PerimeterX press-and-hold at REQUEST time that the in-run solver cannot
clear -- *"no checkmark or peak detected within 12s ... releasing anyway"*, twice -- then `request_rejected`.
Job 1's rejection cooled the publisher, so 7 of 8 jobs never attempted. **Identity is fine; the wall is the
problem.** `Z-S14`'s original classification of bbg as "a verification challenge" stands and is now measured
twice more.

**ONE THING THE SUCCESSFUL CRAWL DID BUY, unrelated to the harvest:** Bloomberg's identity cookies are now
KNOWN -- `_user-id`, `_user-jwt`, `_user-role`, `_user-token`, `_breg-uid`, `_breg-user`.
`bloomberg_harvest_session.py`'s own header records that this was unknown as of 2026-09-11 and asks for
`IDENTITY_COOKIES` to be hardcoded once a real success reveals them. That is an open item for that script's
owner, not a change made here.

⚠ **CREDENTIAL HYGIENE, and it was a live exposure:** the crawl wrote its 142-cookie bundle to
`org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_session_20260926T220354Z.json` -- **inside the repo and NOT
gitignored**, one `git add -A` from being committed. It was imported to DPAPI and then deleted, with absence
verified by a read. The harvester's ROE says the only persisted artifact is the session bundle; it does not
say the bundle's default home is safe.
