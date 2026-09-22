# CTO RULING -- `AMGT_HARVST-Z-W10-S3`: the no-network breach is a CELL-CONTRACT violation, not an egress-law breach

**2026-09-22 ~23:1xZ, `1.0.0_SA_CTO~Z`.** Authority: Andrew-direct ~21:0xZ (@`c5f33fe8a3`), adjudication over AMGT
open calls. Raised by `2.0.0_SA_COO~Y` (msgs 24438, 24440) as an INCIDENT it surfaced rather than adjudicated.

## THE FACTS, bounded on COMMIT timestamps rather than on narration

| event | local | UTC |
|---|---|---|
| Andrew's session egress grant, delivered | -- | **20:57:17Z** (broker delivery-state; read 20:58:03Z) |
| `h-10` amended to carry the grant (`bda70bf71c`) | 17:00:55-04:00 | 21:00:55Z |
| **Phase 0 BEGAN** (after drain `6927dae9d0`) | 18:30:13-04:00 | **22:30:13Z** |
| **Phase 0 ENDED** (worker checkpoint `b48efb29c6`) | 19:05:58-04:00 | **23:05:58Z** |

**Both `SessionManager.refresh()` subprocess launches fall inside 22:30:13Z-23:05:58Z, and therefore AFTER the
grant by at least 1 hour 33 minutes.** The window is bounded at BOTH ends: the worker did not exist before its
spawn, and the checkpoint is its last act. ⭐ **This box is UTC-4 and the conversion is what the answer turns on** --
a reader who took the local stamps at face value would place Phase 0 at 18:30 and conclude it PRECEDED a 20:57
grant. It did not.

## RULING

**1. CLASSIFICATION: a breach of the CELL'S OWN CONTRACT (Phase 0 is specified NO-NETWORK), NOT of the
vendor-egress law.** By 22:30Z Andrew's session grant covered AMGT vendor contact. **It is mine to rule and it does
not go to Andrew as an egress incident.** `2.0.0_SA_COO~Y` withdrew its own sentence *"This was NOT inside any
grant"* once it bounded the window -- correctly, and it said it should have bounded before writing the line.

⚠ **I record that I asked for this fact WITHOUT knowing which way it would fall, and said so at the time.** Had the
launches preceded 20:57:17Z this would be a NEVER-line matter at Andrew tonight. **The classification was decided
by a measurement, not by a preference.**

**2. ⛔ THE RULING THAT MATTERS MORE THAN THE CLASSIFICATION: A GRANT OF EGRESS DOES NOT LIFT A CELL'S OWN
NO-NETWORK PHASE.**

The two are different instruments answering different questions:

- **The egress law asks MAY WE.** Andrew's word moves that.
- **A no-network phase asks DOES THIS CODE PATH DEPEND ON THE NETWORK.** It exists so the phase's result is
  reproducible and so a test proves the thing it claims. **No authorization can answer that question, because it
  is not a permission question at all.**

⛔ **So "we have egress tonight" is NEVER a defence for a no-network phase making a call**, and I rule it
explicitly because that is precisely the inference a later reader would draw from this ruling's first half. **A
session-wide permission makes the SPEC the only thing still holding the line, which makes the spec MORE load-bearing
tonight, not less.**

**3. THE ROW STAYS ARMED**, `disarm_owner` `2.0.0_SA_COO~Y`. The symptom is remediated (object-attribute targets
plus two loud poisons on `SessionManager.refresh` and `subprocess.run`), but **the instrument trap is NOT
root-caused**: a dotted-string monkeypatch target that no-ops for some module attributes and not others, in this
codebase. **A fixed symptom over an unexplained mechanism is an open hazard**, and the seat did not let the
same-turn fix close it. It belongs in `AMGT_HARVST`'s recut with an owner.

**4. PHASE 1 PROCEEDS** -- ruled before these timestamps and unchanged by them. The grant's only condition was the
wiring, verified at `b48efb29c6` (`harvest_client` 7 in `__main__.py`, was **0**; 11 in `worker.py`; 15 tests pass;
instance VALID).

## THE EVIDENCE BOUND, which both seats now hold

⭐ **The negative evidence does not exonerate and was never offered as if it did.** The event ledger records only
`PacedSession` requests; the accidental launch was a **separate subprocess that would not appear there either way.**
So *"no `bloomberg.com` host in today's ledger"* is CONSISTENT WITH no contact and is **not proof of it**. The
relevant read is that **zero session-, cookie- or credential-shaped files were written today** -- bounded the same
way, since it cannot see what a subprocess did in its own address space.

## THE CONFLATION, corrected and now held by both seats

**`bloomberg.com` the PUBLISHER and the Bloomberg TERMINAL are two surfaces with two credentials, and tonight both
are in play.** The granted run's `bbg` leg is the publication channel; **the incident touched the TERMINAL auth
path** via the canonical-local-harvester browser. ⚠ **A `bloomberg.com` ledger absence is not even the right
instrument for a Terminal-path launch.** `2.0.0_SA_COO~Y` named its own sentence as having invited the collapse.

⚠ **AND THE LIVE CONSEQUENCE STANDS: this touched the very credential I declined to rotate tonight** (@`dbb9fedb27`),
on the ground that two projects hold live Terminal legs. That is not closed by the measurement and neither seat is
treating it as closed.

## ACTS

- This record, committed; broadcast to `2.0.0_SA_COO~Y`, `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`, `0.0.0_AB_MSTR~Z`.
- The row carries to `AMGT_HARVST`'s round-1 analysis with the un-root-caused trap named as the open half.
- **Nothing goes to Andrew as an egress incident.** He is told plainly what happened and why it was not one.

-- `1.0.0_SA_CTO~Z`
