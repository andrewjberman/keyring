# AMGT_HARVST round 3: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T04:0xZ at HEAD after `26cea6fac3`, LOCAL on SITEZ.
**Inputs:** the packet @`26cea6fac3` (7,360 bytes), the two orders, the channel's 33 rows, and this seat's own
instruments: a source read of the new `finally` guard, and **a metadata census of every bronze object in the
store, by publisher and label.**

## Round state

**2 of 2 terminal.** Sweep **PASS 10 / FAIL 0 / UNVERIFIABLE 0 of 10** over 2 orders. **No judgment criterion.**
**ZERO vendor calls, zero S3 writes.**

## ASK 1 -- the round, graded, and the guard verified at the bytes

`HVST-t-1` moved the listing persist into a `finally` wrapping the per-article loop, so a mid-loop raise no longer
discards pages already captured. **That is FWD-1's third cause fixed** — the one that was ours rather than the
publishers'. The pages round 1 discarded are NOT recovered, and the worker says so.

**The amendment matters more than the fix, and I read it rather than took it.** `worker.py`, the only `exc_info`
in the file:

```
already_propagating = sys.exc_info()[0] is not None
try:    self._write_harvest_listings(client.listings)
except Exception as persist_exc:
        self.record({"event": "harvest_listing_persist_failed", ...})
        if not already_propagating: raise
```

**Evaluated BEFORE the persist; the persist in its own try; a distinct event on failure; a re-raise ONLY when
nothing was already propagating.** ⭐ **The second arm is what stops the guard becoming a silent swallow**, and the
issuer's own framing is the durable part: **a correct fix created a new reachable state on the failure path**,
because in Python an exception raised in a `finally` REPLACES the propagating one. A disk-full would have surfaced
instead of the 502 that actually stopped the job. **The old placement could not do this, since it ran only on the
success path.**

## ASK 2 -- does `Z-S1` close? **THE FORWARD HALF CLOSES. THE BACKWARD HALF DOES NOT, AND IT IS SMALLER AND
SHARPER THAN ANY OF US STATED.**

**Forward: CLOSED.** `t-2` exercises 5 of 5 paths, `byte_equal 5 of 5`, `vendor_calls 0` from a counter, all three
poison sites raising, **a negative control that REPORTS FAILURE on a re-serialised body** (so the instrument can
detect the defect it denies), an undrivable path reporting UNEXERCISED rather than assumed, and the counter
snapshotted BEFORE the positive control so a deliberate trip cannot inflate it. **On the current code the writer
stores what the transport returned.**

**Backward: measured here, and nobody had this number.** Every bronze object in the store, by publisher and
`received-form`:

| publisher | objects | `as_received` | `bbg-client-json` | `normalised_record` | **NO LABEL** |
|---|---|---|---|---|---|
| seeking-alpha | 41 | 3 | -- | 20 | **18** |
| bloomberg | 134 | -- | 115 | 19 | 0 |
| wsj | 28 | 13 | -- | 15 | 0 |
| ft | 14 | -- | -- | 14 | 0 |
| barrons | 15 | -- | -- | 15 | 0 |
| **total** | **232** | 16 | 115 | 83 | **18** |

⭐ **83 objects labelled `normalised_record` are NOT a defect — they are a DISCLOSED STATE.** The store says what
it holds, which is what `C-HV-BRONZE-AS-RECEIVED`'s metadata rule exists for. A re-serialised object cannot be
un-re-serialised; only a re-fetch produces received bytes, and that is vendor egress.

⛔ **THE REAL REMAINDER IS 18 UNLABELLED SEEKING-ALPHA OBJECTS OF 232.** An unlabelled object asserts nothing: a
consumer cannot tell whether it is as-received or normalised, and the contract requires every object to record the
form. **That is the whole backward half, it is bounded at 18, and it needs no vendor call** — the label is
derivable from the writer that produced them, or the objects are re-fetched under a future granted act.

**So `Z-S1` is GRADUATED, not closed**, with its scope reduced from "SA and Bloomberg raw_bytes" to **"18 unlabelled
objects."**

## The round's two defects, both the issuer's own, both found by reading past a PASS

- **`Z-S10`** — the `finally` guard, above. Found by reading the diff after five criteria passed.
- **`Z-S11`** — ⛔ **the gate finding, and it is the durable one:** invocation-alignment compares the INSTANCE
  against the ORDER, so **when both carry the same unrunnable text it PASSES. It certifies AGREEMENT, never
  RUNNABILITY**, and nothing in the chain asks whether a shell could run the string. **A worker who meets a
  mis-escaped invocation is REWARDED for mirroring it; only one who mirrors AND DISCLOSES surfaces it.** Both are
  GRADUATED; `Z-S11`'s checker half is the gate owner's, as the issuer states.

## `Z-S4`'s remedy is measured, and one number in it was corrected

Four rows this round, **all the issuer's, and NO worker filed one — because both workers' baselines matched the
full-tree counts EXACTLY.** `Z-S9` disarms `Z-S4` with both controls run BEFORE either spawn: 0 tree violations
where there were 24 false orphans, 7 passed where there was 1 failed and 6 passed. ⭐ **And the issuer corrected
its own justification: `org/missions` is 5,649 tracked paths, not the 26,278 it assumed, so the memory risk that
justified the narrow cone never applied to the path that needed widening.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S11",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T04:05Z",
    "one_line": "L9 GRADE RECORD for round 3: 2 of 2 terminal, 10/0/0, no judgment criterion, zero vendor calls and zero S3 writes; FWD-1's third cause is fixed and its finally-guard verified at the bytes (exc_info before the persist, re-raise only when nothing was already propagating).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_HARVST --round 3: PASS 10 / FAIL 0 / UNVERIFIABLE 0 of 10 over 2 orders.",
        "worker.py, the file's only exc_info: already_propagating = sys.exc_info()[0] is not None evaluated BEFORE the persist; the persist in its own try/except; a distinct harvest_listing_persist_failed event; re-raise only if not already_propagating.",
        "t-2: paths_exercised 5 of 5, byte_equal 5 of 5, vendor_calls 0 from a counter snapshotted before the positive control, all three poison sites raising, and a negative control that REPORTS FAILURE on a re-serialised body."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "Both cells meet their orders, the fix holds on the failure path as well as the success path, and no vendor budget was spent.",
    "notes": "Grade carrier. The pages round 1 discarded are NOT recovered and the cell says so. A correct fix created a new reachable state on the failure path -- the issuer's own framing, and the reason the amendment matters more than the fix.",
    "dismissal_reason": "Grade record: this row carries the round-3 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_HARVST-Z-C-S12",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T04:05Z",
    "one_line": "RULING on ask 2: Z-S1's FORWARD half CLOSES on t-2's 5-of-5 byte-equal exercise with a working negative control; the BACKWARD half does NOT, and a metadata census of all 232 bronze objects reduces it to 18 UNLABELLED seeking-alpha objects -- the 83 labelled normalised_record are a DISCLOSED STATE, not a defect.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Metadata census by this seat over every bronze object: seeking-alpha 41 (3 as_received, 20 normalised_record, 18 NO LABEL), bloomberg 134 (115 bbg-client-json, 19 normalised_record), wsj 28 (13 as_received, 15 normalised_record), ft 14 (14 normalised_record), barrons 15 (15 normalised_record). Total 232.",
        "C-HV-BRONZE-AS-RECEIVED requires every object to record received-form in its S3 metadata.",
        "A re-serialised object cannot be un-re-serialised; only a re-fetch produces received bytes, and that is vendor egress."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Bronze is the bytes as received, and every object records its received form.",
    "world_is": "The writer now stores received bytes on all five exercised paths; 83 historical objects honestly declare they are normalised; 18 declare nothing.",
    "notes": "SCOPE REDUCED from 'SA and Bloomberg raw_bytes' to '18 unlabelled seeking-alpha objects'. The remedy needs NO vendor call: derive the label from the writer that produced them, or re-fetch under a future granted act. Remediation row owed at L10.",
    "adjudicates": [
      "AMGT_HARVST-Z-S1"
    ]
  },
  {
    "id": "AMGT_HARVST-Z-C-S13",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T04:05Z",
    "one_line": "GRADUATED: Z-S10 (a correct fix created a new reachable state on the failure path, guarded by amendment) and Z-S11 (invocation-alignment certifies AGREEMENT, never RUNNABILITY -- when order and instance carry the same unrunnable text the gate PASSES, and nothing in the chain asks whether a shell could run it).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S10: an exception raised in a finally REPLACES the propagating one, so an unguarded persist would have surfaced a disk-full instead of the upstream 502; the old placement ran on the success path only.",
        "Z-S11: an HTML-escaped AC5 invocation passed the alignment check because the instance mirrored the order; the worker mirrored AND DISCLOSED, which is the only path that surfaces it."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A guard does not replace the error it guards; a recorded invocation is one a shell could run.",
    "world_is": "The first is fixed and guarded in this round; the second is a gate property nobody had named.",
    "notes": "Z-S11's checker half is 1.0.0_SA_CTO~Z's as the gate's owner -- a limb that PARSES a recorded invocation (shlex or bash -n would refuse instantly), stated as a candidate and not built. The cheap half the issuer already adopted: every order through one writer. Remediation rows owed at L10.",
    "adjudicates": [
      "AMGT_HARVST-Z-S10",
      "AMGT_HARVST-Z-S11"
    ]
  }
]
```
