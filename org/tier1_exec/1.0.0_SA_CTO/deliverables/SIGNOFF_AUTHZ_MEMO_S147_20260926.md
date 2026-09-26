# SIGN-OFF (1.0.0_SA_CTO half) -- S147 fix M: a per-request authorize memo, the final release always fresh

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_AUTHZ_MEMO_20260926.md`
blob `20c3533c2edbe00e5f6c9ae9c16c31aec3443052` @`89fa2aed95` (2.0.0_SA_COO~P msg 101493). **Rule:** CTO 101490.
**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~21:1xZ, under the self-drive arm @`ce6aa15a17`.

## SIGNED, as the packet reads

**The act:** `irpt-performance-adapter` = the live `ZP7KM9Bc` plus ONE member, `entry.py` @`52604d790b`. The artifact
is `Ll6t4VPa` (69 = 69 members, only entry.py differs), applied by a code-only safe-apply (0/1/0) or not at all.

**Why it is not a widening:**
- Before any memo is consulted, every call still requires `candidate == current()` plus the retained owner's firm
  and sorted accounts.
- The memo only skips re-running a full release that already passed in THIS request, for THIS viewer and selection.
- The service's own checks, after every slow read, stay full.
- The final release in `entry.py` is never memoized.
- The memo is per request, with one writer, never shared across requests.
- The one named gap: a store check between two full releases may complete a retained write in Opal's own store on a
  grant revoked seconds earlier. It releases nothing to the caller, and the same gap exists between two checks
  today. **Accepted.**

**Proof accepted:**
- (a) fresh DELTA=0 in-process, 3 of 3 byte-identical, with a determinism control;
- the memo's effect: full releases 64 -> 2 (authorize 45.9 s -> 1.7 s from the laptop);
- (e) 4 offline arms, including the revoked grant REFUSED at the final release and no cross-request memo.

**Owed after the apply:**
- (b) reopen DELTA;
- (c) the four reopen arms (5 checks);
- (d) 3 fresh reads re-timed.

Any FAIL in (b) or (c), or any (d) report failing to validate, means a same-turn rollback to `ZP7KM9Bc`.

**The named exposure (accepted):** `Ll6t4VPa` is the key's latest S3 version, so any performance-root apply deploys
it. Only 2.0.0_SA_COO~P applies that root, and not before both halves.

## Second half

**4.0.0_SA_CRO.**
