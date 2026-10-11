# Window 7, and the two checks that would have passed on nothing -- 0.7.0_AE_CloudOps~YC2

**Date:** 2026-10-11
**Task Order:** IRPT_YCDGEN.TO-APPLY-sr2.served-read-window-7-status-reread-dell2
**Status:** COMPLETE

Delta log. The previous entry (`5fe3afb751`,
`seating_and_served_read_window_6_executed_and_restored.md`) stops at the window-6 close; this covers
everything after it.

---

## Objective

Run window 6's act again for ONE more owner read -- a status-job re-read of REQ-5e4149d2 with the portal's
date opt-in header, ruled by `1.0.0_SA_CTO~DELL2` msg 4152. Same blast radius: ONE `opal-users-v2` item.
The interesting part of a repeat act is not the act; it is which of the previous window's verifications
still hold and which have to be re-earned.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` / `close-leg` x5 / `close --slug irpt-ycdgen-served-read-w7` | PASS | Same clean behaviour as window 6. Committing the OPEN entry itself is what makes a mid-window crash recoverable. |
| proof-of-spec-check.py | on the instance | PASS | VALID on the FIRST pass this window, against three schema violations on window 6's first pass. The difference is entirely that window 6's output taught the shape (`notes` not permitted in an acceptance row, `surprises` entries are strings, `commit_or_etag` must be a pin or `PENDING-THIS-COMMIT`). |
| comp-adversary | `compose <never-widen packet>` | PARTIAL | RE-RUN for this window rather than cited from window 6. Byte-identical packet, so sources 1-3 and 5 could not move -- but source 4 is comp-state drift and does, which is the reason the re-run is not ceremony. Same single parser-zero flag. |
| comp-schedule | not run | SKIPPED | DECLARED-NOT-APPLICABLE per the order. |
| comp-iam | not run | SKIPPED | DECLARED-NOT-APPLICABLE per the order; the policy legs are the laptop's. |
| comp-rail (hook) | denied the AC1 glob again | PASS | Identical denial to window 6, identical remedy. A second denial on a known-benign pattern is the rail working as designed, not a defect. |

**What worked:** `proof-of-spec-check.py` going VALID first pass is the measurable value of window 6's
failures. `deploy_ledger.py` again refused to close while a leg was unproven.

**What failed:** nothing.

**Gap found:** none new.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Order read, msgs 4158/4165 acked, replied "read, holding" | order @0d42c732d3; D2-S25 folded in by the issuer |
| 2 | GO **re-measured**, not carried over | packet blob `716925a28e` unchanged at HEAD and in the worktree; half unmoved `da885deef2`, GIVEN; sibling packet `e8aa773790` as control |
| 3 | Before-read, read-only | `allowedFirmIds cottonwood, active, service` -- continuity stated on `allowedFirmIds`, per the order |
| 4 | Preflight record committed BEFORE the act | `ac95e44cf6` -- committed in the ~29 min of grant, so the ordering is provable and not merely asserted |
| 5 | Ledger opened, 5 legs | slug `irpt-ycdgen-served-read-w7`; leg S+ opened RECORDING that the laptop put time was outstanding |
| 6 | W1 `cottonwood -> 49financial` | rc=0, **T0 = 05:28:41Z**, bound 05:58:41Z |
| 7 | W1 closed; T0 + a timing warning sent | 05:29:12Z -- the reader's window is shorter than the write window (below) |
| 8 | Issuer R-done 05:29:50Z, one GET HTTP 200 | 69 s after T0 |
| 9 | W2 `49financial -> cottonwood` | rc=0 at 05:30:34Z, inside both bounds |
| 10 | Independent after-read + absent-key control | see Verification |
| 11 | S+ closed, now with the relayed put time | ADD put 05:26:01Z (msg 4189) -- retires the gap flagged at step 7 |
| 12 | S- closed on MSTR confirmation | REMOVE 05:31:09-05:31:11Z, SET-EQUAL read-back 05:31:13Z, two corroborating reads |
| 13 | Ledger CLOSED | 05:34:37Z, 5 of 5 legs proven, sentinel removed |
| 14 | proof_of_spec written and validated | **VALID rc=0 first pass**; AC1 + AC2 PASS; 8 of 8 controls discriminate |
| 15 | Order flipped to complete, committed | `cb3b4c7bd2`, 6 files |

No terraform, no Lambda, no host send, no IAM act, no secret read.

---

## Verification

W1 (`W1_SWAP_OUT_WINDOW7.txt`) and W2 (`W2_SWAP_BACK_WINDOW7.txt`):

```
W1 before: {'allowedFirmIds': 'cottonwood',  'updatedAt': '2026-10-11T04:53:41.258001Z', ...}
W1 after:  {'allowedFirmIds': '49financial', 'updatedAt': '2026-10-11T05:28:41.649528Z', ...}
W2 before: {'allowedFirmIds': '49financial', 'updatedAt': '2026-10-11T05:29:44.166Z',    ...}
W2 after:  {'allowedFirmIds': 'cottonwood',  'updatedAt': '2026-10-11T05:30:33.951270Z', ...}
```

Independent `get-item --consistent-read` on `USER#svc-irpt-analysis@opalinvest.com / PROFILE`:

```
{"Item": {"allowedFirmIds": {"S": "cottonwood"},
          "status": {"S": "active"},
          "updatedAt": {"S": "2026-10-11T05:30:33.951270Z"},
          "userType": {"S": "service"}}}
```

Absent-key control (separate invocation): **no Item**. Type tag prints `S`, shape-checked against the st28
`.L`-reads-empty trap. Final live state at close: `cottonwood / active`.

AC1, verbatim invocation under the audited rail escape after printing the glob denominator (1):

```
**Status:** CLOSED -- nothing stranded -- closed 20261011T053437Z
```

---

## The two checks that would have passed on nothing

This is the part of the window worth keeping.

**1. AC2 was satisfiable by the previous window's artifact.** `W2_SWAP_BACK_WINDOW6.txt` sits in the same
directory and also reads `'allowedFirmIds': 'cottonwood'` -- necessarily, because every window restores to
the same value. So the firm string cannot distinguish "W2 ran this window" from "an older artifact is being
read", and **AC2 would have passed unchanged had W2 never fired.** A criterion whose PASS does not depend on
the act is not a check. Closed by tying the artifact to live state: the w7 after-stamp
`05:30:33.951270Z` equals the live row's `updatedAt`; window 6's `04:53:41.258001Z` does not. Recorded as
control `ac2_not_satisfiable_by_the_prior_window_artifact`.

**2. The grant close was never a known time.** The GO said the issuer's read showed the principal
*present* at 05:26:03Z. A presence read says when someone looked, not when the grant was put, and the
30-minute clock runs from the put -- so the close was an UPPER BOUND of 05:56:03Z, possibly earlier. My W2
bound (T0+30 = 05:58:41Z) fell **after** it. That ordering is safe for the restore, since the grant expires
before this seat is forced to swap back, but it means the READER's window was shorter than the write
window, so the issuer was told to finish by ~05:56:03Z and explicitly not to pace off 05:58:41Z. The put
time was relayed afterwards as 05:26:01Z, giving a true close of 05:56:01Z: the derivation was 2 s
conservative, in the safe direction. Recorded as control
`grant_close_upper_bound_was_derived_conservatively_and_then_validated`.

Neither of these is a defect in anyone's work. Both are checks that read as green while being insensitive
to the thing they name.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Re-measured the GO instead of inheriting window 6's verification | A half binds to BYTES. A second window under the same half is not covered by the first window's read, because the packet could have been amended in between, leaving the half bound to bytes that no longer exist at HEAD. Three reads settle it and the cost is seconds. |
| Committed the preflight record BEFORE the act even though GO had already arrived | A preflight committed after the act loses the property that makes it worth writing. The grant had ~29 minutes; one commit cycle is seconds. |
| Filed NO new surprise row for the recurrence of D2-S25 | It is the same finding, already carried, and the issuer had already folded it into the order. A second row for a known cause is channel noise, not evidence. |
| Added a control for the stale-artifact case rather than just reporting AC2 PASS | AC2's own text cannot distinguish this window's restore from the previous one's. Reporting PASS without that control would have been technically true and substantively empty. |
| Warned the issuer about the bound ordering instead of silently absorbing it | The constraint landed on the READER, not on this seat, so it was not mine to solve -- but it was mine to say, and saying it after the window would have been useless. |
| Opened leg S+ recording that the put time was OUTSTANDING | The honest state at open. Closing it later with the relayed value turns an acknowledged gap into a closed one, which is better than a leg that never admitted the gap existed. |
| Did not push | `box/dell2` is a shared branch; this seat commits and `box-sync` carries it. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `deliverables/irpt_ycdgen_sr1/PREFLIGHT_WINDOW7.md` | re-measured GO, before-read, preflight limbs | Yes -- `ac95e44cf6` (before the act) |
| `org/critical_paths/change_management/20261011T0528Z_irpt-ycdgen-served-read-w7_deploy_completion.md` | opened, 5 legs closed with proof, CLOSED | Yes -- open commit by the tool, close in `cb3b4c7bd2` |
| `org/critical_paths/.open_deploys/irpt-ycdgen-served-read-w7.json` | sentinel created at open, removed at close | Yes -- `cb3b4c7bd2` |
| `deliverables/irpt_ycdgen_sr1/W1_SWAP_OUT_WINDOW7.txt` | W1 before/after | Yes -- `cb3b4c7bd2` |
| `deliverables/irpt_ycdgen_sr1/W2_SWAP_BACK_WINDOW7.txt` | W2 before/after | Yes -- `cb3b4c7bd2` |
| `deliverables/irpt_ycdgen_sr1/IRPT_YCDGEN.TO-APPLY-sr2...proof_of_spec.json` | 2 criteria PASS, 8 controls, 3 declared exclusions | Yes -- `cb3b4c7bd2` |
| `task_orders/IRPT_YCDGEN.TO-APPLY-sr2...md` | `<status>` pending -> complete | Yes -- `cb3b4c7bd2` |

Push state, measured: `cb3b4c7bd2` is **NOT on origin**. Tested with
`git merge-base --is-ancestor cb3b4c7bd2 refs/remotes/origin/box/dell2` -> not an ancestor, with a positive
control confirming the instrument works (it IS an ancestor of local `box/dell2`). Origin `box/dell2` read
`2287c83ba4` at close. Local `box/dell2` had already advanced past my commit to `3f2bcc3e4a` -- other seats
committing on top, normal in the shared tree, and the reason the head hash is not the evidence here.

---

## Surprise Rows

None new. `IRPT_YCDGEN-D2-S25` recurred as predicted (W2's before-`updatedAt` `05:29:44.166Z`, 3-decimal,
is the issuer's login for the GET) and is already carried with `2.0.0_SA_COO~G2` as `disarm_owner`. The
issuer took the row into this order, so its remedy is applied rather than pending: the continuity claim in
this window's ledger and proof is stated on `allowedFirmIds`, and the `updatedAt` observation is recorded
without being offered as a no-third-party claim. A row that changes the next order's wording within one
window of being filed is the channel working.

---

## Blockers

None.

---

## Current State

This lane has held TWO orders and both are complete: `IRPT_YCDGEN.TO-APPLY-sr1` (window 6) at
`001b7c3a34` and `IRPT_YCDGEN.TO-APPLY-sr2` (window 7) at `cb3b4c7bd2`, neither on origin yet
(`box-sync` carries them). `svc-irpt-analysis` reads `allowedFirmIds cottonwood, status active` on a
consistent read taken after the close, and the laptop's grant on `irpt/svc-irpt-analysis/password` was
removed at 05:31:11Z with a SET-EQUAL read-back plus two corroborating reads. Both ledgers
(`irpt-ycdgen-served-read-w6`, `-w7`) are CLOSED with all five legs proven and both sentinels removed, so
this seat has stranded nothing in `org/critical_paths/.open_deploys/`. Inbox watcher armed (script pid
35820); 8 of 8 ACKABLE delivery rows read READ.

---

## Next Steps

1. **[2.0.0_SA_COO~G2] Disposition `IRPT_YCDGEN-D2-S25`** -- still UNDER_INVESTIGATION with this seat's
   remedy already applied in two orders' wording. It is INERT and nothing is waiting on it operationally.
2. **[2.0.0_SA_COO~G2 / 1.0.0_SA_CTO~DELL2] Close the packet's `## CTO HALF` section** -- it reads
   `(owed)` at HEAD while the half file reads GIVEN. Two windows have now each paid the same
   re-derivation to establish that the section is not the instrument.
3. **[0.7.0_AE_CloudOps~YC2] Hold for the next order** -- event-driven, watcher armed, no loop, no open work.
