# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 18: the round-8 walk, K8 on the async export, four identity reads

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W18_20260927.md`
blob `b74de7e4653e3ad703d0963184e58c6a6b266ed6` @`ec6aae3838`. The blob is the same at HEAD and on disk (read
2026-09-27 ~20:2xZ).
**Asked by:** 2.0.0_SA_COO~P msg 102076. This seat is not in the act.

## VERDICT: SIGNED on blob b74de7e4, with one named item

- **A, ~D's round-8 walk,** is window 9's read-only shape on local DEV `3b98939b`, with the byte-proof and no media in
  git. It is the CVO's round-8 artifact.
- **B, K7/K8 on the async export `Ulim/gmf`,** carries the five arms signed on dd91065c and 5f45ed04, plus two
  count-based proofs:
  - one hop: exactly 2 invocations for the ONE POST, read by request id;
  - the pointer's `binding` names this window's principal.

  Any failed arm is a same-turn rollback.
- **C, four read-only `securities_info` GETs,** run on the resident's own session under the `_opal` lease.
  - The stop rule is: a non-200, a login destination or a non-JSON answer stops the act.
  - The write set is 0 vendor writes, the lease row, and ONE evidence file of Opal's own model rows, with no client
    data.
- **Timing:** the window opens only after this seat reports its ui-walker DISARMED, and the user and REPORT#
  censuses are taken after that. This seat's deep walk is running and disarms by about 20:55Z; this seat reports
  DISARMED when it has. The window closes well before MSTR's 03:00Z freeze.

## Named -- part C's authority line cites the wrong scope

W18-5 cites "Andrew's session egress (MSTR 101850 as scoped by CTO 101854)". But CTO 101854 scoped that word to ~P's
**Performance** vendor uses, and these are YCharts reads.

The ruling the act actually rests on is **CTO 102028 (1)**, read here: "They are API calls under Andrew's 'egress is
permitted for API calls'". That is Andrew's 2026-09-26 session word, not the 09-27 "full session" word. This seat
accepts the CTO's reading, which covers four read-only GETs with no writes, and does not rule wider or narrower.

The line should cite 102028 (1) and the 09-26 word, so the record matches the basis. This seat also names it to
Andrew, so that he sees a YCharts read resting on the session egress word.

Not measured by this seat: the pins, the runner script's bytes and the resident queue (the packet's).

## Addendum 1 (2026-09-27 ~20:5xZ) -- part C RE-SIGNED on runner blob `3373f30879b89b8c71b4985989c96d807584d713`

The source is 2.0.0_SA_COO~P msg 102094.
- **`git diff cf3f4c5d 3373f308`, run here, is ONE line:** `UNIT=irpt-resident` becomes
  `UNIT=irpt-analysis-resident.service`. The runner at HEAD and on disk is `3373f308`, and the packet blob is still
  `b74de7e4` (unchanged).
- The old name matched nothing on the host, so the runner would have stopped before any read. The new name resolves
  to the W18-2 pin, `fe64236bbb-lt` (P's read-only SSM check).
- Every part C term carries: four read-only GETs, the stop rule, the write set, and the authority as named above.

## Addendum 2 (2026-09-27 ~21:2xZ) -- the window's outcome, read against this seat's conditions

The source is 2.0.0_SA_COO~P msg 102117 (window CLOSED @`614594fff7`), not re-measured here.
- **Part B's arms 1, 2, 4 and 5 PASS.**
  - QUEUED in 3,140 ms.
  - The pointer was SUBMITTED, with the binding naming the caller.
  - The grant names the caller.
  - The owner is unchanged, with exactly 2 invocations (one hop).
  - The narrative was withheld with the client sentence.
- **Arm 3 ended as "a named FAILED".** That is the branch the async-submit half (dd91065c section 5) admits: the render
  was dispatched and REFUSED at the served print route ("exr_d9ee2b18 is absent").
  - This is **not a rollback trigger** for the async-submit change. The refusal is in the print route, downstream of
    the change, and this was the first real bundle ever to reach it.
  - It is a new defect, routed by the CTO.
- **This seat's K1-CRED condition (window 7, carried) was breached by a tooling defect,** as self-reported (row S172).
  The delete at ~D's login was path-mangled, so the credential lived until 21:12:46Z. Under S149 it was readable by
  any SSM-managed host for that span.
  - The condition's check is a `ParameterNotFound` read taken immediately after the delete. That read would have
    caught it.
  - From the next window, the ledger records that read, with its timestamp, beside the delete. A delete is not done
    until the read confirms it.
