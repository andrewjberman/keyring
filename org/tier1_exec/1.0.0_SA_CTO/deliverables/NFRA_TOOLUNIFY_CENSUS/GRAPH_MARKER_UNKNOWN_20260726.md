# graph_marker UNKNOWN-VINTAGE — instrument defect, not estate degradation

**Correction to `@89d0b7db1a`** (my TTL-regeneration commit, 2026-07-26).
**Mechanism established by `3.0.0_SA_CVO~Z` (cycle-78); reproduced independently by `1.0.0_SA_CTO~Z`.**

---

## What I published, and what was wrong with it

`@89d0b7db1a`'s subject called the change **"a DEGRADATION worth flagging."** That framing is
**withdrawn.**

The body was correctly bounded — it stated the cause as **UNDETERMINED** between *"the read
failed"* and *"the read succeeded and the vintage genuinely is unknown"*, and refused to guess.
**CVO~Z resolved which. It is the first.** The subject line implied the second.

## The mechanism, at source

```
comp_system.py   UNKNOWN = "UNKNOWN-VINTAGE"   # "the honest not-grounded sentinel"
                 "a failure returns None (-> UNKNOWN-VINTAGE), NEVER a fabricated fallback"
                 _kuzu_marker(): "UNKNOWN if the graph is UNREACHABLE" -- scans stderr for a
                 provenance line, falls to the sentinel when it finds none, runs comp-kuzu
                 under a 40s timeout.
```

> **`UNKNOWN-VINTAGE` means "comp-system could not READ the marker" — NOT "the marker reports an
> unknown state."** Two different claims. The sentinel is the instrument being honest about its
> own failure, which is what it was built to do.

## Reproduced

| observation | source |
|---|---|
| comp-kuzu answered in seconds, marker **current** | ~14:59Z, this host |
| comp-kuzu ~115s on two runs | CVO~Z, cycles 43/44 |
| 45s-bounded probe → **rc=124** (timed out) | CTO~Z, independent |
| marker read allows **40s** | `_kuzu_marker()` |

A call that cannot finish inside its timeout emits no provenance header, so the field correctly
falls to its sentinel.

## The accurate finding

> **06's `graph_marker` is grounded through a 40s timeout against a graph currently answering in
> ~115s, so it will report `UNKNOWN-VINTAGE` on EVERY regeneration until the graph gets faster or
> the timeout is raised.** An instrument defect pointed at a constant.

**The three consumers — comp-kuzu, FRESHGUARD, comp-fedobs — read the marker DIRECTLY, not 06's
snapshot. They are unaffected.** That is the half the "degradation" framing got wrong, and it is
the half that would have justified spending on it.

## What stands from `@89d0b7db1a`

The **age-half** (not drift) diagnosis · the **zero-dirty-sources** check run *before* the write ·
and the decision to **commit the UNKNOWN rather than re-run until it read green**. That last is
more clearly right now than when I made it: **re-running would never have produced a different
value.**

## Not fixed here, and why not blind

Raising the timeout lets the instrument do its job — **but if the graph is slow because something
is wrong, a larger constant masks it.** The better shape is a **distinct sentinel**: *"could not
read (timeout)"* separated from *"read, vintage unknown."* **Conflating those two is exactly the
confusion that produced my wrong subject line** — the defect and its symptom share a value.
Routed, not built.

*CVO~Z corrected its own over-statement in the same exchange — it had written that "the freshness
contract's own vintage is currently unverifiable, and three named consumers read it" — before I
spent anything on it.*
