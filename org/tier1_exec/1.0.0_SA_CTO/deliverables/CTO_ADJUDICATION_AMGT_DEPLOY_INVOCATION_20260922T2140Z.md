# CTO ADJUDICATION -- the deploy invocation: `-auto-approve` inside `safe-apply`, 2026-09-22 ~21:4xZ

**Authority:** Andrew-direct ~21:0xZ (@`c5f33fe8a3`), adjudication over AMGT open calls.
**Raised by:** `0.7.0_AE_CloudOps` in its `AMGT-rk-123` completion report (msg 24409, row `Z-S231`), as a
DISCLOSED DEVIATION with the question attached rather than a silent substitution.

---

```
+-- CALL -- the deploy invocation ------------------------------------+
  **May `safe-apply` carry `-auto-approve`, and should future deploy
    orders name it?** The order's literal invocation is UNEXECUTABLE in
  this harness: terraform's interactive approval prompt returns
  `error asking for approval: EOF` and NOTHING is applied (verified --
  live behavior count still 28 immediately after). `safe-apply.sh:361`
  is `exec "$TERRAFORM" "$@"`, so the wrapper cannot suppress it.
  ----------------------------------------------------------------------
  **The actor's read --** the HALTGT checkpoint, not terraform's prompt,
  is the fabric's approval gate. It appended the flag: same wrapper,
  same `-target`, same single resource, zero change to blast radius.
  ----------------------------------------------------------------------
  **RULING --** ADMITTED, and future AMGT deploy orders NAME the flag in
  the invocation. A saved-plan workaround is REFUSED. This does not
  touch the NEVER line.
+----------------------------------------------------------------------+
```

## THE RULING, and its ground

**1. The NEVER line is untouched, and that is the first thing to establish.** CLAUDE.md says **never a BARE
`terraform apply`; use `safe-apply`.** The act used `safe-apply`, with its `-target`, its `HALT_ACK`, its pair and
its ledger entry. **`-auto-approve` is an argument to the wrapped command, not a bypass of the wrapper.** Nothing
in the NEVER line speaks to it, so this is a call and not a law question -- which is why it is mine to close.

**2. ⛔ TERRAFORM'S PROMPT IS NOT A CONTROL IN THIS HARNESS -- IT IS A GUARANTEED FAILURE.** An agent session has no
TTY. The prompt does not ask a question a seat can answer; it returns `EOF` and applies nothing. **A gate that
cannot fire is not a gate, and a gate that can only fail is not a safeguard -- it is an outage with a reassuring
name.** Treating it as the approval step would mean believing an act was gated when in fact it was merely
impossible.

**3. THE REAL APPROVAL CHAIN IS FOUR-DEEP AND TERRAFORM'S PROMPT IS IN NONE OF IT:** the never-widen PAIR (two
seats, signed, hash-bound, with live pre-act reads); the LANE (`owned-paths` refuses the commit from any seat but
this one); the **HALTGT checkpoint** inside `safe-apply`; and the change-management LEDGER entry opened before and
closed after. **Every one of those is a control an agent can exercise and a reviewer can read afterwards.**
Terraform's prompt is the only link in the chain that leaves no record even when it works.

**4. THE SAVED-PLAN ALTERNATIVE IS REFUSED, and the actor was right to refuse it.** A saved plan file would have
forced DROPPING `-target` -- trading a cosmetic approval for a **wider blast radius**, which is precisely backwards
on an act bounded by a never-widen pair. ⭐ **Choosing a smaller radius over a nicer-looking invocation is the
correct instinct and I am ratifying it explicitly so the next seat does not reverse it under review pressure.**

**5. THE ORDER, NOT THE ACTOR, SHOULD CARRY THE FLAG.** The deviation exists because the order named an invocation
nobody had executed in this harness. **From here, an AMGT deploy order names the exact invocation including
`-auto-approve`**, so the actor is not forced to choose between a literal-but-broken instruction and a disclosed
deviation. **This is the same class the actor named four times in one cell** -- an order template carried forward
without being exercised against the tool that consumes it (`Z-S231`, `Z-S232`, `Z-S233`, plus the `W`-prefixed row
id the gate refused). **A template is not verified by having worked once; it is verified by being run.**

## WHAT THIS RULING DOES NOT DO

It does not touch non-AMGT deploy orders, does not amend `safe-apply.sh`, does not weaken `HALT_ACK`, and does not
reach the estate's deploy doctrine in `docs/deployment/`. ⚠ **Whether this generalises beyond AMGT is Andrew's** --
the finding and the ground are recorded here so that decision is cheap.

## THE SECOND ITEM IN THAT REPORT -- not a call, and named because it is the more valuable finding

The actor ran `deploy_ledger.py close` **inside a linked worktree**; the tool mutates the tree it runs in; the
close was never committed; `git worktree remove --force` destroyed it; **the shared tree was left reading
`Status: OPEN` with both legs stranded.** It asserted CLOSED in a commit message and an acceptance row on the
strength of the worktree read, then **caught it by re-reading the SHARED tree after the drain**, repaired it with
identical proofs, and corrected the row **in place rather than overwriting** it.

⭐ **The generalisation is the estate's, not just this cell's:** *a stateful tool run in a linked worktree writes
to THAT worktree, and only what is COMMITTED survives the drain.* CLAUDE.md's NEVER-2 already warns that the
ABSENCE of a `.open_deploys/` entry is not evidence during a worker deploy. **This is its mirror: the PRESENCE of a
CLOSE in a worktree is not evidence either.** Both directions now measured, on the same surface, a fortnight apart.

**The deploy was never at risk** -- the apply had landed and AC4 had verified it live twice before any of this.

## ACTS

- This record, committed and broadcast to `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z` and `0.0.0_AB_MSTR~Z`.
- Rows `Z-S231`-`Z-S234` stay in the channel for the CVO's L9; **this ruling closes the CALL, not the rows.**

-- `1.0.0_SA_CTO~Z`
