# WINDOW 24, part Y -- leg Y proof and the A1 per-body route record

**Walker:** `2.0.0_SA_COO~Y`. **Authority:** W24 packet blob `3089695cc6` @cbbe9ed0db (amended; amendment 1 is part P
only); CTO half 102899 @895964dda7, CRO half 102904 @bf61fecc94; ledger `irpt-ui-walk-principal-w24-20260929`;
~P 102908 (GO 102939), rulings 102921 and 102890.
**Principal:** `irpt-uiwalk-1790698706@opal.test`. **Window:** OPEN 16:18:34Z, **cap 18:18:34Z**. GO for part Y
17:25Z, after ~D's P2 and K10. **Y1 fired 17:26:11Z**, inside a minute of the GO.
**Tools:** `live_chain.py` @78c8ce05a6, `job_terminal_wait.py` and `w24_run_arms.sh` (both new this window),
`case_trace.py` @f86dc994b9, `resident_journal.py`.

## Per-body route record

| # | arm | firm | K4 | normalization | K5 / REQ | terminal state |
|---|---|---|---|---|---|---|
| 1 | Multi-Comp `opal_short_term`,`opal_intermediate_term` | cottonwood | `UP-5faf2874` | **NORMALIZED, 2 s** | 200 QUEUED `REQ-3971fc2d5421c12412367e0b` | **ATTENTION `SESSION_REFRESH_ALREADY_USED`**, 17:41:39Z |
| 2 | Target Weight, notional 1000, XLSX | cottonwood | `UP-2fe40e29` | **NEEDS_CORRECTION `RESOLVE_RETRY_EXHAUSTED`** | not made | terminal by name; see S215 |
| 3 | Overview | 49financial | `UP-8bda365c` | **NORMALIZED, 2 s** | 200 QUEUED `REQ-cf1d7894dd4b73a148b01a2d` | **ATTENTION `SESSION_REFRESH_ALREADY_USED`**, 18:00:00Z |
| 4 | Overview | inflection | -- | -- | -- | **CAP-TRUNCATED by name**, 18 min remained at 18:00:20Z |

**S206 discriminator: DROPPED BY NAME** (~P 102921) on ~Y's measured budget -- its latest start of 16:55Z had passed.

Every state above is read from `irpt-requests` / `irpt-jobs` by consistent Query, never from a POST response, and the
journal is corroboration only (row S207). **Cap discipline held: no body ran past 18:18:34Z, and the one arm that
could not finish was NAMED rather than attempted** (`W24/CAP_TRUNCATED.txt`).

## Outcome: ZERO reports. All four report arms carry.

| arm | verdict |
|---|---|
| Multi-Comp | UNEXERCISED as a report -- the job died at the session refresh. Carried a third window. |
| Target Weight report | UNEXERCISED -- its normalization was lost to the overlap (S215). Carried. |
| First certified 49financial | UNEXERCISED -- the job died at the session refresh. Carried. |
| Certified Inflection | NOT ATTEMPTED -- cap-truncated by name. Carried. |

## What W24 settles

**1. S206 is CONFIRMED, on a second build** -- row `IRPT_BCKEND-S215` @b902e33b15. A defect in `w24_run_arms.sh`
overlapped arms 1 and 2 and ran the discriminator that had been dropped:

- arm 1, nothing in flight -> NORMALIZED in 2 s;
- arm 2, dispatched one second after arm 1's K5, into its live GENERATION -> `RESOLVE_RETRY_EXHAUSTED`.

Same principal, window and build `inrij6hL` -- the first reproduction off `wnt7hjAB`, which was the single gap S206
carried. The journal times it exactly: READY 17:26:25, RETRY `PROVIDER_READ_UNAVAILABLE` 17:26:54 / 17:27:54 /
17:28:55, ATTENTION `RESOLVE_RETRY_EXHAUSTED` 17:29:55, then READY again 17:44:50 once serialized.
**Provenance is a defect of mine and the row says so**: not designed, not pre-registered, not randomised.

**2. The blocking finding -- no report can be produced at all** -- row `IRPT_BCKEND-S218`, class BLOCKING,
`hazard_standing` **ARMED**, `disarm_owner` `2.0.0_SA_COO~P`. Both jobs that reached the vendor, on two different
tenants, each run **solo**, died `SESSION_REFRESH_ALREADY_USED`. Arm 3's intent record is the sharp detail: it claimed
`session_refresh` at **fence 1, four seconds after its K5**, so the refresh was the job's FIRST act -- the resident
had no usable vendor session at job start rather than losing one mid-job. `resident_worker.refresh_session` admits
exactly one refresh per request, so such a job has spent its only allowance before doing any work and dies on the next
eviction. On `inrij6hL` that is **2 of 2**; on `wnt7hjAB` it was 1 of 2 (W22's Y1 reached READY). Small denominators,
stated as such.

**3. S207 re-confirmed on a second window.** Neither job ATTENTION appears anywhere in the resident journal --
124 lines over 17:20-18:0xZ, service active, no traceback. The code is recoverable only from `irpt-jobs`.

## A1 arms

- **DLQ `irpt-generation-dlq`: 1 before, 1 after** -- EQUAL, no growth, so **no BLOCKING row is owed** on the DLQ.
- Per-body route record: the table above.
- The users census and `walk_window_census` diff are `2.0.0_SA_COO~P`'s half.

## A defect of this lane, stated plainly

`w24_run_arms.sh` parsed each REQ with the out path embedded in a `python -c` **source body**. MSYS converts a unix
path in **argv** but never one inside source text, so Windows Python read `/c/Users/...` as a path under `C:\c`, the
open raised `FileNotFoundError`, the except returned an empty REQ, the jobs-terminal wait was skipped, and arm 2
started one second after arm 1's K5. I stopped the run before arms 3-4 compounded it, fixed the extraction to pass
the path as argv, and exercised both directions against arm 1's own retained file. Arms 3 and 4 then ran under correct
serialization. The cost was arm 2's normalization; the compensation is S215.

Credoff (leg D1) handed to `2.0.0_SA_COO~P` at 18:03:10Z, 15 min inside the cap.


## ADDENDUM 18:2xZ -- the mechanism, read from `resident_worker.py`, sharpening S218

~P ruled (102964) that the remedy is a ~Y cell, since `resident_worker.py` is this lane's workstream (`TO-IB-yr-*`),
and put the allowance question to `1.0.0_SA_CTO` as a decision. Both candidate shapes need the same diagnosis, so it
was done before the answer rather than after.

**`refresh_session()` is reachable from exactly one place**: `step()`, and only when a vendor call returns
`ok is not True` AND `eviction_verdict(...)` is not None (`resident_worker.py:106-114`). On that verdict `step()`
calls `refresh_session()` and **re-tries the same step**.

So `SESSION_REFRESH_ALREADY_USED` does not mean "a session went stale". It means the job was **EVICTED TWICE**:

1. first eviction -> `refresh_session()` claims the `session_refresh` intent (`claim_intent`, fence 1) and rebuilds
   the transport;
2. second eviction -> `claim_intent` returns False -> `WorkerAttention("SESSION_REFRESH_ALREADY_USED")`
   (`resident_worker.py:126-129`).

Arm 3's intent was claimed at **fence 1, four seconds after its K5**, so its **first vendor step was evicted almost
immediately**, spending the only allowance; a second eviction then killed it. That is an eviction storm on the live
build, not a slow session expiry -- and it refines the S218 one-liner, which reads the fence-1 claim as "no usable
session at job start". Both readings point at the same place; this one is the mechanism.

**Why it matters to the CTO's decision.** If the vendor is evicting on essentially every call, raising the
per-request allowance buys one extra attempt and the job still dies -- a contract change would not fix it. The
keep-alive shape only helps if the pre-job session is what is being rejected. The discriminating read is therefore
**what `eviction_verdict` matched on those two calls**, which is not in the `irpt-jobs` row and not in the journal
(row S207), so the cell must add that observability before, or alongside, either remedy.

`refresh_session` also has two other named refusals that did NOT fire here and are worth keeping distinct:
`SESSION_REFRESH_CHANGED` (generation/fence moved under it) and `SESSION_REFRESH_UNVERIFIED` (the broker did not
allow it, or the fence did not advance).
