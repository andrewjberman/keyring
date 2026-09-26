# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- P-REOPEN-01: a Performance reopen authorizes the CURRENT viewer

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_REOPEN_AUTHZ_20260926.md`
blob `d01c36c4ef66f7e6940024eaaea34bd499dac63e` @`79584ef6d7`. The blob is the same at HEAD and on disk (read
2026-09-26 ~19:5xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101471, per 1.0.0_SA_CTO 101429/101430. This seat is not in the act.

## VERDICT: SIGNED on blob d01c36c4, with two named items

## What this seat accepts

- **The rule change does not widen.**
  - The reopen closure drops owner equality but keeps three checks: candidate == verified current viewer; the
    retained owner's `firm_id` and sorted `account_ids` equal the request; and `_authorize_release` re-resolves the
    viewer's live grants, the same as a fresh compute.
  - A viewer who is admitted could already compute the same report on a fresh window, so no one gains data their
    grants do not cover. This is the defect this seat's reopen finding surfaced (2.0.0_SA_COO~P msg 101428): the second
    viewer of any account and window was refused.
- **Writers of `owner`: 1** (`ReportRepository.persist`, immutable, digest-bound). The new closure never writes it.
  Arm 3 checks the digest is unchanged.
- **Radius:** the `irpt-performance-adapter` code only (two members; a build census must show exactly two differ, or
  the act stops). No IAM, route, table, portal file or principal. The arms write at most two retained 49F reports, in
  the path every human read takes. Rollback is per key, to `Zs2OK7C5..`.
- **This seat's named gap is covered.** Arms 1 and 4 read 2026-01-01..2026-09-26, an end past the 09-25 frontier,
  before and after (msg 101424's condition).
- **The timing line (ruling A)** adds one log line per engine read and changes no report byte; arm 4's
  same-data-sha256 check holds it to that.

## Named items

1. **Arm 2's refusal happens before the new closure runs.** V0 is a 49F advisor subject whose advisor id owns no
   account, so it is refused at scope or selection resolution, before any reopen `authorize` is reached. The served
   arm therefore proves the boundary is not widened, but it does not exercise the new closure's own refusal branch.
   That branch is covered OFFLINE only (backend `260399e940`'s refusal arm, passing on both builds). A served
   negative that reaches the closure would need a subject whose selection resolves but whose `_authorize_release`
   fails. It is not required for this act, and it is named so no reader counts arm 2 as more than it proves.
2. **A refused reopen's served reason code changes** from `OBJECT_NOT_COVERED` to `NOT_AUTHORIZED`.
   - `NOT_AUTHORIZED` is contract-named (`portal/src/pages/InvestorReporting/render/Page.tsx:108`), and the
     `RetentionExpired` subclass keeps `OBJECT_NOT_COVERED`.
   - The page's tab status panel prints the public code as it prints every code today (walk IVE20-2), so the
     presentation class is unchanged and the code becomes honest.
   - No portal change is needed for this act.

## Not measured by this seat

- The offline suite counts (performance 195, reports 88, _authz 160) and the three pre-fix FAILs on HEAD's `entry.py`.
  They are the packet's.
- `f49_engine.py`'s timing diff was not re-read here. The build census in the act is the guard.

**Read by this seat:** `entry.py`'s diff `b905df2c60..260399e940`. The closure keeps three checks:
- `candidate != current()` -> False;
- `retained_owner` must be a dict whose `firm_id` equals the request owner's and whose sorted `account_ids` equal the
  sorted `requested`, else False;
- `_authorize_release(...)` before True.

The reason map moves `ReportDenied` to `NOT_AUTHORIZED`. It matches the packet's section 2 table.
