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
