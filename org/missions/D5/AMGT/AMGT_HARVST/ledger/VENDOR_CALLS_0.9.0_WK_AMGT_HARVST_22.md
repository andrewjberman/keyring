# VENDOR CALL LEDGER -- `0.9.0_WK_AMGT_HARVST~22`, AMGT_HARVST (task order `HVST-v-2`)

**Why this file exists.** Standing clause 3 of `HVST-v-2`: **the ledger is a condition of the word, not
paperwork** -- a seat that cannot ledger its call does not have the word. Same shape as
`VENDOR_CALLS_2.0.0_SA_COO_Y.md` beside it, which is this file's template.

⛔ **THE LIFT IS ON THE AUTHORIZATION, NOT THE MECHANISM.** The one row below ran from the EXISTING SCRIPTED
PRODUCER invoked from a command line. No vendor byte in this cell was fetched inside an agent turn: no URL was
opened, no payload pasted, no HTTP client constructed by the worker.

**No entry here covers spend, a contract, an entitlement or a hold-lift.** Those stay sovereign. In
particular **no re-authentication was attempted or reached** -- see the `re-auth fired?` row, which is
measured from the producer's own receipt and event log, not asserted.

---

## CALL 1 -- seeking-alpha, 2026-09-26T09:44:47Z -> 09:47:18Z

| field | value |
|---|---|
| seat | `0.9.0_WK_AMGT_HARVST~22` (worker of `2.0.0_SA_COO~Y`, task order `HVST-v-2`, AC2) |
| vendor | seeking-alpha (`seekingalpha.com`) |
| endpoint class | REST: `/api/v3/account/{id}/info`, `/api/v3/symbols/{symbol}/news`, `/api/v3/articles/{id}` |
| mechanism | `python -m lib.opal_data_harvest run --publishers sa --harvest-grammar --runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest" --all-securities --max-jobs 8` -- AC2's LITERAL invocation, run from the repo top-level of worktree `C:/tmp/wk-hvst-v2` (branch `wk-harvst-7-22`) |
| agent-turn fetch? | **NO.** Scripted producer only; the runtime root of the MAIN tree was passed so the saved session vault resolved (clause 4 / the round-6 failure) |
| scope attempted | 8 jobs of 89 (`--max-jobs 8` caps JOBS, not securities -- row `AMGT_HARVST-Z-W22-S1`): ASML, Adobe, Air Liquide, Alibaba, America Movil, AstraZeneca, BB Seguridade, BNP Paribas |
| scope actually queried | **1 of 8** -- `security-81a74ed057551e58` (ASML, sa_symbol `ASML`). Jobs 2-8 finished `status: cooldown, accepted: 0` in 30 ms after job 1's Timeout set a publisher-level cooldown (row `AMGT_HARVST-Z-W22-S2`) |
| requests made | **4**, all HTTP 200, from the producer's own `events.jsonl`: `/api/v3/account/1btfwdu/info` (5,149 B), `/api/v3/symbols/asml/news` (154,875 B), `/api/v3/articles/4640871` (10,354 B), `/api/v3/articles/4640637` (9,868 B) |
| authorization LIVE AT THE TIME OF THE RUN | **Andrew-direct 2026-09-26 ~03:xxZ, session-wide**, verbatim: *"Egress is permitted for API calls this session -- no per-use word per vendor call, but every call is ledgered by the seat that makes it. Spend, contracts, entitlements and hold-lifts are NOT covered."* Recorded at `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md` section 1 (relayed as msg 25989), and restated to this worker in `HVST-v-2` standing clause 3. **This is the authorization live AT 09:44Z when the call ran, not the earlier per-use word of 02:1xZ** that covered the COO's own CALL 1 |
| credential used | the SAVED session envelope `.runtime/opal-data-harvest/secrets/sa.dpapi` in the MAIN tree, reached only because `--runtime-root` pointed there |
| re-auth fired? | **NO -- measured.** The run receipt `runs/20260926T094447Z-sa-ee1fa71c16.json` reads `"auth_refreshes": 0, "verification_repairs": 0`; `events.jsonl` holds NO `reauth_started`/`verification_started` row in the window; no browser was launched. Clause 4's hard stop was never reached |
| result | producer rc 0. Job 1 `status: error`, `error_type: "Timeout"` on the 3rd of up to 5 article bodies, with 2 articles already ACCEPTED; jobs 2-8 `cooldown`, 0 accepted |
| bytes retained | 1 listing page (154,875 B) + 2 article bodies (10,354 B, 9,868 B) into the LOCAL outbox |
| S3 written | **not by this call.** `run` writes the local outbox only. The separate `upload-harvest` leg (no vendor request) then put: bronze `news_listing` +1, silver `listing_hit` +20 rows, silver `article` +2 parts -- all under `seeking-alpha/harvest/` in `opal-data-harvest` |
| spend | none -- an entitlement already held; no metered or paid endpoint |
| evidence | `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~22/ac2_run_output.txt` (the invocation's whole stdout), `ac2_upload_output.txt` (the upload leg), `ac2_ceiling_output.txt` (the ceiling, measured zero-network before the call) |

**Follow-on, non-vendor, recorded here because it shares this act's evidence:** two `upload-harvest
--max-objects 40` invocations (AC1's, for the rows held since 02:17:52Z, and AC2's, for what this call
captured) both returned rc 0. Neither makes a vendor request; both touch S3 and the local outbox only.
`AMGT_HARVST-Z-S28` is now exercised against real sa bytes and the write succeeds.

---

## THE CLOCK

**The word is scoped to THIS SESSION.** This row ran at 09:44Z inside the session that opened with the
~03:xxZ directive; a later cell must state the authorization live when IT runs, never this one.
