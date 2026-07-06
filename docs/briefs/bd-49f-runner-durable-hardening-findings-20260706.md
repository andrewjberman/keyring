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

## Finding 2 — bearer-TOKEN expiry mid-txn-sweep, mis-classified as cookie-death (the durable blocker)

**Precise mechanism (was loosely "cookie-lifetime"; it is the bearer TOKEN, not the cookie).**
`bd-49f-runner` mints ONE DataMining bearer token at run-start (`lambda_function.py:124`
`mod.get_datamining_token(cookie)`) and reuses it for the whole run. The txn chunk sweep pulls the
newest tile first (85 MB on 07-02) then older tiles; the multi-minute sweep **outlives the token TTL**,
so 401s **begin mid-sweep and persist** on every later call (older tiles + allocations/realized/unrealized).

**Grounded (reproduced 3× on 2026-07-06 — 13:59 / 14:05 / 14:15Z, identical):** each run — `auth OK`
→ txn tile 1 (85 MB) OK → later tiles 401 → allocations `AUTH ERROR ... HTTP 401` → `auth_dead:True`
→ 3/4 failed → RuntimeError → **sentinel correctly withheld**. The cookie is LIVE throughout
(keepalive OK, minted 00:02:36Z, run-2 last night landed all 4 on it). So the 401 is **token-expiry,
not cookie-death** — but the runner treats every 401 as fatal cookie-death.

**The bug is a WIRING gap, not missing capability.** The table-loop handler catches a 401 at
`lambda_function.py:147` (`_is_auth_error`) and **short-circuits to `auth_dead=True` + break — no retry**.
The re-mint-the-bearer recovery **already exists at L158-159** ("re-mint the bearer in case it lapsed
mid-run") but sits in the transient branch **below** L147, so it is unreachable for a 401. The
deliberate anti-401-storm design (docstring L23-28) never anticipated a re-mintable token-expiry 401.

### Path A — the durable fix (CTO pre-approved-in-principle 2026-07-06; 0.6.0 authors runner .py / AE deploys via TF; CTO formal-gates the diff)
On `_is_auth_error(exc)`: re-mint the bearer ONCE from the same (live) cookie and retry the call;
only a re-mint that **itself** auth-fails (or a retry still 401-ing after `MAX_RETRIES=3`) is true
cookie-death → the existing cookie-death path + alarm. Bounded by MAX_RETRIES → no storm; it's the
L158 wiring made reachable for 401s. **CTO conditions to bake in:** (1) IDEMPOTENT mid-sweep resume —
the retry must re-do only the failed tile, not double-write/corrupt partial progress (txn tiles write
per-date `TRANSACTIONS_DAILY_{tiledate}.xlsx`, so a per-tile re-do is clean) — *the one real risk*;
(2) crisp re-mint-succeeds→retry / re-mint-fails→cookie-death binary; (3) optional pre-emptive re-mint
at the TTL boundary on a known-long sweep (enhancement, not required); (4) exercise-gated — not done
until a clean all-real run emits the sentinel + silver rolls to parity + N-nightly. **Keep the
classification consistent with A-prime's schwab OAuth-refresh (§2.3)** — same re-mintable-transient-vs-
session-death discipline (CTO pattern note).

### Path A2 — compute-tier (COO/CTO steer, Andrew-engaged; AE infra leg when sequenced)
Move the heavy/backfill txn pull OFF the 15-min Lambda onto EC2/SSM (sequential, no retry-storm, no
token-TTL race against a Lambda ceiling); keep the Lambda for the light daily delta. Removes the
root time-pressure that the token TTL loses against.

### Path B — immediate un-freeze tonight (0.6.0's invoke lane; AE verifies sentinel+merge)
Pull the stub tables (allocations/unrealized) **individually** — short single-table pulls survive the
token TTL — → **verify REAL @07-02 (not 3746 B/4591 B stubs) BEFORE** a `force=false` skip-all run
(COO-bound guard, because `_already_landed()` is existence-only per Finding 1) → the skip-all run emits
the sentinel on all-REAL → my `bd-v2.47.0` grant fires it → `bd-silver-merge` → silver. Un-freezes
today without waiting on Path A; Path A prevents recurrence.

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
