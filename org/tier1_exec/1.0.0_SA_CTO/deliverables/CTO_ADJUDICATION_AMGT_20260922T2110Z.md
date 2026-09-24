# CTO ADJUDICATION -- AMGT open calls, 2026-09-22 ~21:1xZ

**Authority:** Andrew-direct ~21:0xZ at this terminal, VERBATIM *"you have adjudication ability for any and all
open calls you encounter for the duration of this session as it pertains to AMGT projects."* Record
`ANDREW_DIRECT_20260922_210xZ_SESSION_EGRESS_AND_AMGT_ADJUDICATION_AUTHORITY.md` @`c5f33fe8a3`.

**Both cards below were standing AT ANDREW before that word. Neither waits now.** Each is written in the
`/open-calls` card form -- the CALL, a divider, this seat's REC as it was put to him, then the RULING as a third
stacked half. **A ruling may reject its own REC; where it does, it says why.**

---

```
+-- CALL 1 of 2 -- the Bloomberg terminal credential ------------------+
  **Rotate the Bloomberg terminal credential, and/or scrub the
    username from the 4 committed artifacts that carry it?**
  The code leak is closed (@ab796d0520, both limbs hashed, 5 controls).
  The password was never exposed by this path. The repo is private.
  But half a credential pair is committed, oldest 2026-08-14.
  ----------------------------------------------------------------------
  **REC --** Rotate at your convenience, not urgently; skip the history
  scrub (destructive git on a private repo, low return).
  ----------------------------------------------------------------------
  **RULING --** (a) NO SCRUB, and it is refused on stronger grounds
  than "low return". (b) ROTATE, but NOT this session and NOT by this
  seat. (c) The row stays ARMED until (b) lands.
+----------------------------------------------------------------------+
```

**(a) NO SCRUB -- the reasoning, because "low return" was the weak half of my own REC.**
A history scrub is a **destructive git act on a shared branch**, which CLAUDE.md reserves to a human word per act
and which this adjudication authority does **not** reach (a NEVER line is law, not a call). So the scrub was never
mine to grant even under tonight's word, and saying "skip it, low return" understated that. **It is refused
because I cannot authorise it, and separately because it would not be worth it if I could:** the value is half a
pair, the repo is private, and rewriting shared history across 33 live worktrees would cost more risk than the
exposure it removes.

**(b) ROTATE, and here is the constraint that decides the timing.** Rotating the Bloomberg TERMINAL login is not a
Secrets Manager edit -- it is a change at Bloomberg followed by a Secrets Manager write, and the two are not
atomic. ⛔ **A rotation fired tonight breaks every live Bloomberg sign-in mid-flight**, and `AMGT_RESAPP` round 30
plus the granted second HARVST run both still have Bloomberg legs. **Rotating now would convert a contained
disclosure into an outage.** So: rotation is OWNED, not open -- it goes to the credential's holder (the
`0.0.3_BG_BBGTerminal` surface, with Andrew as the account identity) **after the AMGT Bloomberg legs are done**,
and it is carried as an item with that owner rather than a card at anyone.

**(c) Row `AMGT_RESAPP-Z-S230` stays ARMED**, `disarm_owner` this seat, and disarms when (b) lands. It does **not**
disarm on the code fix alone -- that was the EXPOSURE limb; the INCIDENT limb is the four committed artifacts, and
they are still there. **Naming that distinction is the whole point of the row.**

**What changes right now: nothing, and that is the correct outcome.** New artifacts cannot carry the value
(@`ab796d0520`). Old ones do and are recorded. Nobody is blocked.

---

```
+-- CALL 2 of 2 -- the lane-blind worker grant ------------------------+
  **A task order's <paths> clause admits its worker by ORDER ALONE and
    prints no lane** -- so an order can grant a worker write access the
  ISSUING seat does not itself hold. Found by 3.0.0_SA_CVO~Z while
  ruling R5 (@af2c1a673e); mechanism read at
  owned-paths-validate.py:209-235 and :330-332. The CVO built no gate
  and carried the second-order item.
  ----------------------------------------------------------------------
  **REC --** Narrow it: admit a <paths> entry only where the ISSUING
  seat's lane admits it. Cost: an order crossing a boundary must be cut
  or co-signed by a seat holding the lane.
  ----------------------------------------------------------------------
  **RULING --** ADOPTED as AMGT CUTTING PRACTICE, binding by reading at
  L6 and verified at the round analysis. **NO GATE IS BUILT.** The
  estate-wide mechanism stays Andrew's.
+----------------------------------------------------------------------+
```

**ADOPTED, and narrower than a gate would be.** From now on, in AMGT projects: **an order's `<paths>` may name only
paths the ISSUING seat's own lane admits.** An act outside the issuer's lane is re-homed to a seat that holds it,
via its own order, exactly as R5 required for the instance.

⛔ **I RULE THE PRACTICE AND I DO NOT BUILD THE GATE.** Two reasons, and the first is the binding one:
1. **CLAUDE.md §2 forbids an agent-made gate absent Andrew's explicit ask.** Tonight's word gives me authority over
   CALLS; a gate is a MECHANISM, and building one on my own initiative is precisely the move that rule names. The
   CVO reached the same conclusion and built none.
2. `owned-paths-validate.py` is estate-wide machinery. A change there binds D0 through D14 and every seat on both
   fabrics -- **far outside "as it pertains to AMGT projects."** Ruling AMGT practice is inside my grant; editing
   the estate's lane validator is not.

⭐ **THE COST IS ALREADY MEASURED, TONIGHT, AND IT IS SMALL.** `rk-122`/`rk-123` is the worked precedent: the
worker produced the patch and stopped; the COO cut a SECOND order (`rk-123`) addressed to `0.7.0_AE_CloudOps`, the
seat whose lane admits `infra/aws/**`. Total cost: **one extra order.** ⚠ And it surfaced a real gap on the way --
LD-0529 refuses every act message to a seat holding no order, so **re-homing an ACT without re-homing an ORDER
leaves it undeliverable.** That is now part of the practice: *when you re-home an act, cut the order that carries
it, in the same turn.*

**NOT RULED, and left to him:** whether the estate-wide validator changes. I am recording the finding and the
worked cost so that decision is cheap when he takes it.

---

## WHAT THIS ADJUDICATION DOES NOT TOUCH

The never-widen pairs, the destructive-act bar, the shadow-pipeline veto, the monitor moratorium, Rule 27's seat
separation, and the CVO's independence at L4-R/L8/L9. **An authority over calls does not reach a NEVER line, and
it does not make this seat a reviewer of its own PRDs.**

## ACTS

- This record, committed, and broadcast the same turn to `2.0.0_SA_COO~Z`, `2.0.0_SA_COO~Y`, `3.0.0_SA_CVO~Z`,
  `0.0.0_AB_MSTR~Z` and `4.0.0_SA_CRO~G`.
- Row `AMGT_RESAPP-Z-S230` stays ARMED; the rotation item is carried with its owner named.
- **Andrew's card queue for AMGT is now EMPTY.** Nothing in AMGT is waiting on his word.

-- `1.0.0_SA_CTO~Z`
