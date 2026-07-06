# bd-49f-runner durable-hardening findings (WS-5 robustness) — 2026-07-06

**Filed by:** 0.7.0_AE_CloudOps (runner-infra lane) · **Co-surfaced:** 0.6.0_AE_PartnerETL (`_already_landed` stub-skip)
**Context:** surfaced while grounding the P0 BDAPIMIG silver-freeze root cause (fixed in `bd-v2.47.0`
= `bd-49f-runner-role` +`s3:PutObject` on `opal-data-bd/bronze/*`, unblocking the bronze sentinel).
**Sequencing (COO-directed):** both are durable-hardening, NON-urgent, land AFTER the exercise-proof
un-freeze; pair with 0.6.0 (their `.py` author lane + my deploy). Same class as 0.6.1's PPLINF
completion-alarm gap.

---

## Finding 1 — `_already_landed()` idempotency skip is existence-only (stub-skip silent-freeze)

**Grounded (code):** `infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py:87-98`.
`_already_landed(table, run_date)` returns `True` IFF `head_object` succeeds on
`forwardfill_v2/{table}/{TABLE}_DAILY_{run_date}.xlsx` — **existence-only, no content/size check.**
Line 132 then skips the pull and counts the table as `landed`.

**Failure mode:** a stub / zero-byte / partial-write bronze object that merely *exists* is treated as
a complete landing → skipped on every subsequent run (unless `force=true`) → the table can be
silently frozen at a bad/empty partition with no re-pull. `emit_bronze_sentinel`'s re-confirm is also
`head_object` existence-only, so a stub can pass both gates. (0.6.0 observed a run that "landed STUBS";
the code path confirms the mechanism.)

**Proposed fix:** add a content floor to the idempotency skip — a min-bytes threshold and/or a
per-table completeness sidecar (the holdings-completeness-sidecar pattern), so a stub does NOT count
as landed and re-pulls. Fail-open bias preserved (skip only on a *validated* landing).

## Finding 2 — cookie-lifetime-vs-runtime race on the txn chunk sweep

**Grounded (runner log, `bd-49f-runner` 2026-07-06):** run 1 (invoked 00:02:43Z) ran the 5-tile txn
chunk sweep for **Duration 574,531 ms (~9.6 min)** (one tile = 59 MB). The session cookie **died
mid-run** → `AUTH ERROR ... HTTP 401` on the tables pulled AFTER transactions
(allocations/realized/unrealized), `auth_dead: True`, `3/4 tables did not land`.

**Failure mode:** the heavy txn sweep can outlive the cookie's live window, starving the tables ordered
after it. Currently self-heals via the session-complete event-chain re-mint (run 2 skips txn
idempotently and completes the rest), but that is fragile — it depends on a second invoke firing on a
freshly re-minted cookie, and on txn bronze having landed in run 1.

**Proposed fix options (pick at pairing):** (a) re-mint / re-auth immediately before the sweep, or
refresh the token between tiles; (b) pull transactions in a separate invocation from the light tables
so a txn-sweep timeout can't starve them; (c) shorten `BD_TXN_CHUNK_DAYS` window / parallelize tiles
to keep total sweep under the cookie lifetime. (a) or (b) preferred — deterministic, not tuning-luck.

---

## Not-in-scope / already-cured (for the record)
- **Auth durability: WORKING** — box `i-0fa1846f` self-mints the cookie nightly (07-06 00:02:36Z proven,
  datacenter subnet, device-trust set). **Proxy-gap hypothesis FALSIFIED** (login succeeds unaided; no
  `blackdiamond/49f/proxy` secret exists; the interim bridge only *reads* the secret).
- **Silver trigger: WIRED** — `bd-silver-merge` fires on the `bronze/{date}/_BRONZE_COMPLETE.json`
  S3 notification (s3-notifications.tf); it was starved, not broken. Cured by `bd-v2.47.0`.

## Approved least-privilege follow-up (trivial, post-exercise-proof)
Tighten the `bd-v2.47.0` grant `opal-data-bd/bronze/*` → `opal-data-bd/bronze/*/_BRONZE_COMPLETE.json`
(source-confirmed the runner writes ONLY the sentinel under `bronze/`). COO-approved as the trivial
follow-up; holding to not race 0.6.0's live invoke.
