# ANDREW-DIRECT — the DRIVE PAIR ratified: /self-drive (CTO) + /drive (COO) linked on one target

**Channel + time:** the base `1.0.0_SA_CTO` terminal, 2026-08-27 ~19:2xZ.
**His framing word (same exchange, VERBATIM):** *"I want to identify with you how we can synergistically
design this loop to work in tandem with the coo /drive loop. ... if we engage a self-drive on CTO we
shoudl definitely be also instituting drive on COO tied to the same target."*
**The ratifying word (on the presented design, VERBATIM):** **"DO it get this set up"**

## What was ratified (the design as presented at this terminal, in full)

1. **The pair**: one target, one arming act, two instruments — CTO `/self-drive <scope>` (SENSE +
   ADJUDICATE: open-calls -> pitch w/ rec -> CVO verdict -> own-lane acts) and COO `/drive <scope>`
   (ACTUATE: convert unblocking verdicts + measured in-scope blocks into dispatches).
2. **The link is an ARTIFACT**: a per-scope verdict ledger
   `org/{tier}/{driver_base_serial}/drive_pairs/<scope>/VERDICTS.jsonl` — appended by the self-drive
   driver (producer-owned, own agent folder, zero new grants), READ by /drive with a cursor. The
   message scrolls; the artifact persists.
3. **Offset cadence** (:T CTO / :T+15 COO) — a pipeline, not a barrier; adjudicate-to-dispatch
   latency bounded at 15 minutes.
4. **/drive's dispatch obligation SCOPED in paired mode** to ledger rows + measured in-scope blocks —
   an empty ledger + no blocks is a LEGAL no-op tick. This is the shape that cures the defect that
   keeps /drive off by standing order (a gate that cannot conclude "dispatch nothing" breaks holds
   on a timer, @014de1937).
5. **One carrier clause, one stop-condition** in the driver's XXX.md row, struck once for both; and
   the twice-measured carrier-loss class is closed mechanically: **no tick 1 until the carrier commit
   exists**.
6. **The wire stays primary**: BLOCKING/ARMED items route immediately by MCP as always; the pair is
   the latency floor for unattended windows, not a replacement for live adjudication.

## Landed by this commit

- `.claude/skills/self-drive/SKILL.md`: carrier-gates-tick-1; verdict-ledger emission in §3;
  CVO-dark held-rows to the ledger; PAIRED MODE section (+ default-pair prompt at arm time).
- `.claude/skills/drive/SKILL.md`: PAIRED MODE section (scoped obligation, cursor, legal no-op,
  offset, shared carrier/stop).
- `org/ref/DRIVE_PAIR_PROTOCOL.md`: the ledger row contract + pairing mechanics, single source.

## Explicitly NOT done by this setup

**No pair is ARMED.** Arming stays operator-initiated per the zero-crons law — a pair arms on his
word naming a scope (`/self-drive <scope>` at CTO, which then offers/institutes the COO half per the
ratified default). The D2 drive tonight continues event-driven with all execs live; the pair is the
instrument for the next unattended window.
