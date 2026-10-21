# IRPT_ANLREQ: the round-60 slug's mechanical precondition -- 11 orders not terminal, 133 items undispositioned (2026-10-13 to 10-21)

<sweep_watermark>2026-10-21T17:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

**What happened.** This seat drafted `REMEDIATION_v14` to move the clocks of graduated S29 and W55-S25. `.tools/surprise-row-gate.py`
refused it, because a new remediation row IS the slug (spine v3), on two limbs.

1. **11 of 535 IRPT_ANLREQ task orders are not terminal at HEAD.**
   - 8 read `not_met`: TO-APPLY-R34D, R34H, R34I, R34J, R34O and TO-RUN-FWD10-MULTICOMP-7G, 7H, 7I.
   - 2 read `pending`: TO-APPLY-R34R and TO-RUN-FWD1 window4.
   - 1 reads `held`: TO-RUN-FWD1 window5.
2. **133 of 1,200 items are not dispositioned:**
   - 101 are BLOCKING rows whose hazard is now INERT;
   - 32 are ARMED OBSERVATIONs;
   - 109 were surfaced by workers and 19 by CloudOps;
   - they date from 2026-10-13T07:46Z to 2026-10-21T15:20Z.
   - Each needs a new row naming it in `adjudicates`.

**Two instruments disagree on "terminal".** `.tools/round-close-check.py --round 60` reads MAY-CLOSE and treats the eight `not_met`
orders ("ended failed or rolled back") as terminal. The row gate counts `not_met` as not terminal. One of the two is wrong for the L10
precondition. The gate's owner is `1.0.0_SA_CTO`.

**Consequence.** v31 to v35 dispositioned the 14 round-60 BLOCKING ARMED rows, but the slug's precondition is project-wide. It
needs:
- the issuer's L8 compile of the 133 items, each with its resolving evidence (the round-3 to round-20 pattern,
  `ledger/IRPT_ANLREQ_ROUND<N>_<W>_L8_COMPILE_*.md`), which this seat then dispositions in batch;
- the three pending or held orders driven terminal;
- the `not_met` reading settled.

The drafted REMEDIATION_v14 waits outside the tree until then.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S18",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-21T17:20:00Z",
  "one_line": "The round-60 slug is mechanically refused project-wide: surprise-row-gate counts 11 of 535 orders not terminal (8 not_met, 2 pending, 1 held) and 133 of 1200 items undispositioned (101 BLOCKING/INERT, 32 OBSERVATION/ARMED); round-close-check reads the 8 not_met orders as terminal, the row gate does not.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Rule 27 L10: one slug after every task order of the round is terminal and every BLOCKING or ARMED row is dispositioned; round-close-check IRPT_ANLREQ 60 reads MAY-CLOSE.",
  "world_is": "safe-commit of REMEDIATION_v14 (2026-10-21 ~17:12Z) BLOCKED by surprise-row-gate: 11 of 535 orders NOT terminal at HEAD (TO-APPLY-R34D/H/I/J/O, TO-RUN-FWD10-MULTICOMP-7G/7H/7I not_met; TO-APPLY-R34R, TO-RUN-FWD1 window4 pending; window5 held) and 133 of 1200 BLOCKING/ARMED-or-ungraded items UNDER_INVESTIGATION.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".tools/surprise-row-gate.py refusal on REMEDIATION_v14 (output held in this seat's scratchpad, not committed)",
    "python .tools/round-close-check.py --project IRPT_ANLREQ --round 60 (MAY-CLOSE, 16:35Z)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A record of the precondition; the compile goes to the issuer and the not_met reading to the gate's owner."
 }
]
```

-- `3.0.0_SA_CVO~DELL2`
