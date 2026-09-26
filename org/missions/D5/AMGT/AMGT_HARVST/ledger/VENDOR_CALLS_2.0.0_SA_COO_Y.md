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
