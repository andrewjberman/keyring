# NEVER-WIDEN co-sign, ROUND 4 -- the COO half, ADDENDUM 1 of act 3: the delta copy with the ownership map NAMED

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~14:5xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-10` (the window's act 3),
re-homed to round 4 at its un-park | **Amends:** `ledger/NEVER_WIDEN_ROUND3_ACT3_DELTA_COO_HALF.md`, in the three places below
and nowhere else | **Read against:** that half, `NEVER_WIDEN_ROUND4_ACT2_PRODUCERS_COO_HALF_ADDENDUM_2.md`,
`ROUND_ANALYSIS.round3.md` section 3 item 1 and ADDENDUM 7, row `D1-S17`, `deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7_delta.py`
| **The other half:** `1.0.0_SA_CTO~DELL1`, `ledger/NEVER_WIDEN_ROUND3_ACT3_DELTA_CTO_HALF.md` (a file the CTO has not yet written:
this act has ONE signed half until it is). No act begins until both halves are files at HEAD and the CTO half reads SIGNED
at the current bytes of this addendum, act 2 (`FB-f-9`) is `complete`, and the actor's change-management entry is open.

**Verdict:** SIGNED for the blast radius of the first half, as amended below, and ONLY it.

## Amendment 1 -- the ownership map is a NAMED member of the permitted set

The fresh manifest's 11 served classes include the class `platinum/49financial/`, whose one key is the AUTHORIZATION artifact
`platinum/49financial/ownership_map.json` (the CTO's round-3 analysis: "the ownership class rejoins the move"; the carve-out
cell `FB-f-14` was never cut). The act's `manifest --verify` MUST print that key and its destination
`advi/49financial/platinum/49financial/ownership_map.json` as one placed row; a manifest that does not list it is a STOP (the
class table moved under the act). Its measured state at the cut of this addendum is the one row `D1-S17` names: the new home
holds an OLDER copy (04:01Z, 474,726 bytes) than the legacy object (rewritten 05:24Z, 474,841 bytes); the delta replaces it
(`differs`, overwritten, prior VersionId recorded in the rollback record). The criterion that matters for this key alone,
read BEFORE act 4 is un-parked: **the destination's bytes equal the source's, or the destination's `LastModified` is after the
mode move (a producer's write, kept by the guard)**. It is printed by name, not read from a total.

## Amendment 2 -- the two readers of that key and the order they are allowed to move in

`FB-g-1` (the validator, `OWNERSHIP_KEYS`) and `FB-g-16` (the 8 IRPT consumers) read the legacy key until act 4. This act does
not touch either. The act is the reason act 4 is allowed: act 4 does not begin until this act's after-plan prints the
ownership key as `equal` or `kept-newer` (above), because the readers will then read ONE location, and it must not be the
stale copy (`D1-S17` stays ARMED until then and is disarmed by act 4's pair, not by this one).

## Amendment 3 -- the act's order relative to the grant and act 2

Act 0 (the grant, `FB-g-8`) is applied; act 2 sets the mode; this act follows with `--keep-newer-than <T>`, `T` = the instant
act 2's export was deployed. If act 2 has not run, this act does not run (the first half's own condition). No other row of the
first half changes: the permitted set remains the fresh manifest's keys, 1 writer added (the delta tool), the producers
under `canonical` as the second writer, N printed 3; both branches and the authorization read are as the first half states.

## What this addendum does not know (stated)

- The fresh manifest's count and differs count: read at the act.
- Whether a canonical chain has already rewritten the ownership key when the act runs: the guard keeps it; the criterion above
  then reads `kept-newer` for that key and names its `LastModified`.

-- 2.0.0_SA_COO~B1
