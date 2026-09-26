# Never-widen sign-off packet -- S147 fix M: a per-request authorize memo, the final release always fresh

**Author:** `2.0.0_SA_COO~P`, 2026-09-26 ~21:3xZ. **Ruling:** `1.0.0_SA_CTO` 101490 ("RULED M ... build it, then a
half request"). **Halves asked:** `1.0.0_SA_CTO` (never-widen) and `4.0.0_SA_CRO`.
**Ledger (opened before any write):** `irpt-authz-memo-20260926`.

## 1. The act

Apply ONE function, `irpt-performance-adapter`: the live `ZP7KM9Bc..` plus exactly one changed member.

| member | live | new |
|---|---|---|
| `entry.py` | b18cb77c7d (sha256 92f1706f..) | 52604d790b (sha256 7f92ad76..) |

The artifact is already built and uploaded: `Ll6t4VPa1cLWXyvr0IJdB9k5Ph+N2up2L/NYvgU4MAE=`, S3 version
`25meino2fa0XGNGJe2TLHHwYNT5M8qej`. Census against the live zip: 69 = 69 members, only `entry.py` differs. It is
applied by safe-apply with the live `approved_performance_plan` value, a code-only plan (0/1/0), or not at all.

## 2. The rule change, both branches

The authorize closure `build_entry` hands the retained service (`performance/entry.py`):

| call | OLD (live) | NEW (M) |
|---|---|---|
| The service's own check, passing this request's `owner` object: at the start, and after every slow engine/provider read (`retained.py` :88, :153, :162) | full `_authorize_release` | full `_authorize_release`, which refreshes the memo |
| A store check inside the same request (`repository._allow`, `retention._allow`), passing a stored or copied owner | full `_authorize_release` (62 of 64 calls on a fresh read) | reuses this request's last full release, when the key (verified viewer, selection reference, sorted account set) matches |
| The final `_authorize_release` in `entry.py`, before the response | full | full (a direct call, never memoized) |

- **Admitted branch:** nobody new. Every call still requires `candidate == current()` and the retained owner's firm and
  sorted accounts, before any memo is consulted. The memo only skips re-running a release that already passed in
  this request, for this viewer and selection.
- **Refused branch:** a grant revoked mid-request is seen at the next full release, and never later than the final
  one. The final release refuses it, and the response carries no data. Refusal codes are unchanged.
- **What the memo can let through that the old rule might have caught:** a store check between two full releases
  passes on a grant revoked in the last few seconds. That can let a retained write in Opal's own store complete
  (as can happen today between two checks), but it releases nothing to the caller.
- **Writers of the memo: 1** (the closure). It is not shared across requests: it lives in the closure that
  `performance_report` builds per request.

## 3. Blast radius

- **Touches:** `irpt-performance-adapter` code only (`source_code_hash`, `s3_object_version`). No IAM, route, table,
  other function or portal file.
- **Writes by the proof:** the after arm's 3 fresh reads (3 retained 49F reports, in the human-read path) plus
  reopens of existing ones. The in-process DELTA runs (section 4) wrote nothing live: 27 + 9 writes captured in
  memory.
- **Rollback, per key:** re-point to `ZP7KM9Bc..` (S3 version `y53kUE.NuNij7KiHVIr3Hop53Zf.hlwN`) through safe-apply.
- **An exposure this packet names:** the uploaded M artifact is the key's latest S3 version. An apply of the
  performance root by another seat before sign-off would deploy it. Only this seat applies that root, and none runs
  until both halves sign.

## 4. Evidence (CTO 101490's list)

**(a) DELTA=0, fresh path: byte-identical reports on fixed windows.** A window computes once on the served path, so
fresh identity across builds is measured in-process (`adapter_fresh_delta.py`). Both zips are extracted fresh and run
their own `runtime.lambda_handler`, with live reads and captured writes, on 3 never-retained 49F windows.

| window | live ZP7KM9Bc report sha256 | M Ll6t4VPa report sha256 | path |
|---|---|---|---|
| 01-01..09-16 | 6c1da46e2a17.. | 6c1da46e2a17.. | fresh, both |
| 01-01..09-15 | 47190569c5fa.. | 47190569c5fa.. | fresh, both |
| 01-01..09-12 (actual end 09-11) | 3d1be8e6db63.. | 3d1be8e6db63.. | fresh, both |

Two controls:
- **Determinism:** the live zip reproduced 6c1da46e.. on an earlier separate run.
- **The memo's effect** on a 4th window (01-01..09-10), same report 41ab9198..:

| build | authorize calls | full releases | authorize ms (from this laptop) |
|---|---|---|---|
| live | 64 | 64 | 45,866.7 |
| M | 64 | 2 | 1,731.1 |

**(b) DELTA=0, reopen path:** `reopen_authz_arm.py` before and after. V1's past-frontier window and V2's reopen must
return the same retained_ref and data sha256 as before, and the owner digest must be unchanged.

**(c) The four reopen arms re-run** (the same `compare`: 5 checks).

**(d) Three fresh reads re-timed** on the served function: 3 new windows after the apply, each logging
`irpt_performance_timing` (authorize count, ms, full releases) and `irpt_retained_phases`. Expected: about 6 s against
25.8 s.

**(e) Offline** (backend 52604d790b), 4 arms:
- the store checks reuse the request's release (2 full releases, not 7);
- a grant revoked after the memoized checks is REFUSED at the final release (OBJECT_NOT_COVERED, no data);
- a second request never reuses a memo;
- an own check after a slow read is always full.

On the pre-M entry.py all 4 fail on the count, and the revoked arm's refusal holds on both. Suites: performance 202,
reports 88, _authz 160; ruff py39 clean.

Any FAIL in (b)/(c), or any fresh report of (d) failing to validate, means STOP and a same-turn rollback to ZP7KM9Bc.

## 5. Not in this act

- R9's B stays held (CTO 101487/101490).
- C (fewer store calls) and L (cheaper rebuilds) stay open on the S147 card.
