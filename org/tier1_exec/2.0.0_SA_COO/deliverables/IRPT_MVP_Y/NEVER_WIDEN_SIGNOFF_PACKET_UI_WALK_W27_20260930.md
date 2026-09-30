# Never-widen sign-off packet -- WINDOW 27: the three-variant proof under the CANONICAL identity, with the endpoint recording built in

Author `2.0.0_SA_COO~Y`, 2026-09-30 ~07:2xZ. **Supersedes W26** (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W26_20260930.md`,
blob `a4ba10a9d4`, both halves signed, never opened). **Halves owed: `1.0.0_SA_CTO` and `4.0.0_SA_CRO`.**

## Authority, verbatim

**Andrew-direct 2026-09-30 ~06:5xZ** (record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260930_065xZ_NO_DAYPASS_PROVE_3_VARIANTS_RECORD_HAR_THEN_ENDPOINT_REPLAY.md`
@51edcd3ee6): *"go do the walk anyway and prove the generation through the method i described which is canonical in
our cloud, not this fucking daypass bullshit, and while you do it (svc account or otherwise), record HAR and identify
the endpoints that appear in that recording"* ... *"we need to prove that really bad that we can actually do it
properly for the 3 variants"* ... *"go tighten up (aka slash the bullshit) in the IRPT login flow ... make sure it
actually works"*.

**CTO 103196** ruled the service identity for job submission; **CTO 103196's "no interactive login" is measured
unimplementable as built** (this seat's 103213: the auth-handler has no service-token path), so W27 names the V1 form
and asks the CTO half to rule it explicitly.

## W27-1 -- what changed from W26, and each change is a NARROWING or a REMOVAL

| W26 had | W27 has | why |
|---|---|---|
| a `uiwalk` principal minted at open, deleted after the jobs | **`svc-irpt-analysis`, created ONCE under its own ledger, never deleted** | Andrew: *"not this fucking daypass bullshit"*; S231 (deleting the principal strands the job) |
| K1-CRED minted at open, credoff by `0.0.0_AB_MSTR` on the login line | **no per-window credential at all** -- the password lives in Secrets Manager permanently | nothing to mint, nothing to credoff, no second seat on the critical path |
| a two-party property protected by the credoff | **the property is replaced by the credential never being on the walker's disk**: `live_upload.py` reads it by name into memory only, as today | same guarantee, no ceremony |
| one HAR nowhere | **two recordings**: (a) the resident's `tx.evidence` ledger persisted into `receipt.json` per job, (b) a Playwright `recordHar` of the login/session capture | Andrew: *"record HAR and identify the endpoints"* |

**Nothing widened.** Same three bodies, same firm, same serialization, same solo gate, same cap arithmetic, same
per-arm independence. One login, three K4/K5 pairs, no retry.

## W27-2 -- the identity: V1 form, measured against the code that will judge it

`svc-irpt-analysis@opalinvest.com` in `opal-users-v2`:

| attribute | value | the line that judges it |
|---|---|---|
| `firmId` | **`opal-capital`** | `current_authority.py:88` firm match, `:117` -> `OPAL_GLOBAL` scope. **A ticket_center-style `firmId: "null"` FAILS both** (measured 103213) |
| `userType` | `service` | carries no scope by itself (`GLOBAL_USER_TYPE` is `"Dev"`, :24); it is the MARKER the estate's own `service` class uses |
| `role` | **`admin`** | **CTO 103221 limit (1), measured:** `current_authority.decide()` never reads `role` (0 occurrences) so `user` is least THERE -- but the API's `classify_principal` (`_scope/resolve.py:228-262`) resolves a role-`user` service account to **UNKNOWN**: branch 2 (OPAL_GLOBAL) needs an explicit roster that **no deployed Entry populates** (`opal_principal_ids=` appears in none of the installers; default `frozenset()` at `served.py:576`), and branch 4 needs `admin`. So `admin` is the least role that yields a non-empty grant at the API, and it is what every walk principal since 2026-09-26 was. Stated with the reason, not chosen by habit |
| `status` | `active` | `:92` |
| `allowedFirmIds` | `cottonwood` | **RECORDED, NOT ENFORCED** (CTO 103221's own words). Neither `decide()` nor `classify_principal` reads it. Enforcement is cell **`IB-yr-293`, cut in the SAME round, and it must land before this principal touches any firm but cottonwood** -- limit (3) |
| `createdBy` | `2.0.0_SA_COO~Y svc-irpt-analysis-20260930 (Andrew-direct @51edcd3ee6)` | provenance; the census marker |
| password | 32 random bytes, bcrypt 12 in the row; plaintext ONLY in Secrets Manager `irpt/svc-irpt-analysis/password` | never printed, logged or committed |

**Precedent:** `svc-bbgtml@opalinvest.com` -- `opal-capital`, `user`, `active` since 2026-07-15. Same shape, 2.5 months
of history.

**Limit (2) -- what this principal can reach, enumerated from the code, not inferred:**

- **At the API (`_scope/resolve.py`):** class **FIRM_OPERATIONS** (branch 4). Its permitted set is `firm_population(directory,
  firm_id)` for **the ONE selected firm** (`:445-449`: *"never a cross-firm union: bound 3 forbids a new all-firm
  aggregate, and this function is handed ONE directory"*). **OPAL_GLOBAL is unreachable as deployed** -- the roster is
  empty everywhere -- so *"global in reach"* is FALSE at the API and TRUE only inside the resident.
- **Inside the resident (`current_authority.decide()`):** `firmId == opal-capital` -> `OPAL_GLOBAL` scope (`:117`),
  which passes for ANY `data_firm`. **This is the global reach CTO 103221 names, and it is why `IB-yr-293` is in the
  same round**: until it lands, the only thing keeping this principal off inflection or 49financial data is that no
  job for those firms is submitted under it.
- **The operations it can call:** exactly the routes `classify_principal` grants FIRM_OPERATIONS on the selected
  firm -- the Analysis upload (`K4`), submit (`K5`), status and report reads. It carries no advisor id, so
  `FIRM_ADVISOR`'s ownership-map path is never taken.
- **Who may read its secret** (`irpt/svc-irpt-analysis/password`), by explicit ARN as `ycharts/iam.tf:96-99` does for
  the session secrets: **the walker's principal only** (this laptop, Andrew's own credentials, which `live_upload.py`
  already runs under). **The resident does NOT read it** -- it resolves the recorded owner by profile row and never
  logs in as it. No function role is granted it.


**Its creation is its own act** (CTO 103196): ledger `irpt-svc-analysis-principal-20260930`, blast radius = one
`opal-users-v2` row + one secret, rollback = delete both. **It happens ONCE.** Every later window uses it. **Retirement is DISABLE, never delete** (CTO 103221): a disabled row still resolves for `decide()`'s `ACTOR_INACTIVE` refusal, which names the cause; a deleted row is S231's `ACTOR_NOT_FOUND`, which does not.

## W27-3 -- the three bodies (unchanged from W26)

| # | variant | body | firm | comparisons | template |
|---|---|---|---|---|---|
| Y1 | OVERVIEW | `aapl-vnq-12.03.csv` | cottonwood | none | 14141822 |
| Y2 | COMPARISON | same | cottonwood | `opal_long_term` | 14141824 |
| Y3 | MULTI | same | cottonwood | `opal_short_term,opal_intermediate_term` | 14141847 |

Counts are `templates.json`'s own bounds; template ids match Andrew's 2026-08-21 HAR one-to-one (census @2aaf618ff3).
Serialized on the `irpt-jobs` terminal (S206). Solo gate per W26-5/W26-6 -- the 8 derived non-terminal states, the two
stranded ids excluded by exact id, 17/17 single page. A failing arm does NOT stop the others.

## W27-4 -- the recordings, which is what makes this window V2's input

**(a) The endpoint ledger, per job.** `transport.py:474-481` already records every vendor request as
`{method, path, status, content_type, bytes, set_cookie_count, waf_action, login_destination, final_url_path}` --
**shapes, never values** -- into `tx.evidence`. Production then keeps only `len(tx.evidence)` (`job.py:334`).
**Cell `IB-yr-291` persists the list itself into the job's `record` so it lands in `receipt.json`.** That is the
HAR-equivalent for generation, values-free by construction, and it is what Andrew's *"call those in order"* needs.
It is cut and drained BEFORE the window; if it is not on the running resident by open, the window still runs and the
ledger is read from the offline suite's replay instead -- stated so the window does not wait on it.

**(b) A real HAR of the session capture.** `ycharts_session.js` is Playwright/chromium and records no HAR today.
Playwright's `recordHar` on the context is a one-option change; **cell `IB-yr-292`** adds it behind `YC_RECORD_HAR=1`,
writing to a host path with the packet's ROE (cookie NAMES only -- the HAR is post-processed to strip `Cookie`,
`Set-Cookie` and `Authorization` values before it leaves the host). This captures LOGIN and WAF, which the resident's
ledger cannot. Same non-blocking clause as (a).

**Cell `IB-yr-293` (limit 3):** `decide()` and the authorizer read `allowedFirmIds` and refuse a `data_firm` outside it. Same round as 291/292; **must land before the principal is used on any firm but cottonwood.**

**The census to diff against already exists:** `YCHARTS_GENERATION_ENDPOINT_CENSUS_20260930.md` @2aaf618ff3, from
Andrew's own three-route HAR. Tonight's ledgers are DIFFED against it, not censused from scratch.

## W27-5 -- interval and cap

Opens once both halves are at HEAD **and** `svc-irpt-analysis` exists (its ledger CLOSED with the row and secret read
back). **Cap 150 min**, W26's arithmetic unchanged. No principal deletion at close -- there is nothing to delete. Both
censuses before and after; DLQ growth over baseline 1 is a BLOCKING row the same tick.

## W27-6 -- blast radius, both branches

- Every arm is a write `svc-irpt-analysis` owns plus reads. **Nothing served for any other user moves.** No code
  change inside the window (`IB-yr-291`/`292` land BEFORE it or not at all). No IAM, no schedule, no resident restart.
- If an arm FAILS: its REQ stays as evidence, a BLOCKING row same tick, no retry, the remaining arms still run.
- If the resident misbehaves: the window closes; rollback to st4 stays under the st5 ledger's rollback root.
- **The two stranded jobs are neither revived nor deleted.**
- **Reachable:** one login, one vendor session, three jobs for cottonwood under one durable principal.

## What the halves sign against

This file's committed blob; Andrew's direct @51edcd3ee6; CTO 103196 and this seat's 103213 (the two measured limits);
rows S230, S231, S232, S233 at their committed ids; the census @2aaf618ff3; W26's text as superseded here; the V1
identity form in W27-2 **with the CTO half explicitly ruling it**; the three bodies in W27-3; the two recordings in
W27-4 and their non-blocking clause; the interval in W27-5.

**Not asked for:** a fourth arm, any retry, a resident restart, any code change inside the window, any new vendor
account, or the day pass.
