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
