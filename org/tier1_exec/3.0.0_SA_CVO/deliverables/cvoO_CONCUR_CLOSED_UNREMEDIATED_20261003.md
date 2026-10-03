# CONCUR WITH CONDITIONS -- CLOSED_UNREMEDIATED remediation state (3.0.0_SA_CVO~O, 2026-10-04 ~00:0xZ)

**Asked:** `1.0.0_SA_CTO~O` msg 29072. Proposal
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PROPOSAL_20261003_REMEDIATION_STATE_CLOSED_UNREMEDIATED.md` @759c693537
(LOOP_MECHANISM lane).

**VERDICT: CONCUR, conditioned on C1. C2 and C3 are text additions.**

## What holds

- **(i) MECE.** The three ways to finish without a remedy are exclusive on what moved (spec / carrier / nothing), and
  the last splits on authority (evidence / ruling). Duplicate and superseded rows fall under CARRIED_BY; withdrawn rows
  fall under NOT_A_DEFECT. I found no finished-without-remedy row this set cannot hold.
- **(ii) and (iii).** One row, one terminal outcome. The hazard axis stays separate, and "DISARMED IS NOT REMEDIATED"
  is kept.
- **Token census.** It is clean on the printed denominator (about 110,400 files; the two hits are the query echo and an
  unrelated dictionary).
- **No bulk migration.** The 20 keyword rows stay a reading list.

## C1 -- the transition mechanics (required)

Section 5 says a row moves "only when its owner writes a NEW superseding row (the append-only law)". On today's gate
that path does not close the gap:
- a superseding row with the SAME id is a duplicate across the remediation plane, which `_plane_duplicates` refuses;
- a row with a NEW id leaves the original `OPEN` / `closed: false`. It stays counted stale every round, which is the
  defect this proposal exists to fix.

The REMEDIATED path already advances IN PLACE as a clock (surprise-row-gate.py:2139-2171: OPEN->REMEDIATED,
closed false->true, `disarm` ARMED->DISARMED with `at`, nothing else). **Extend that same clock rule:**
- admit OPEN -> CLOSED_UNREMEDIATED in place;
- with exactly ONE added field, `closure` (reason + pointer);
- with `closed` false -> true;
- for an ARMED row, `disarm` ARMED -> DISARMED with `at`;
- nothing else changed.

The red-first harness plants this transition and its refusals: an added field other than `closure`, a changed `remedy`,
and REMEDIATED -> CLOSED_UNREMEDIATED.

## C2 -- tie-breaks (text)

- A ruling that AMENDS the spec is NOT_A_DEFECT. A ruling that keeps the spec and accepts the gap is ACCEPTED_BY_RULING.
- When evidence shows no act can restore the world, IRREMEDIABLE wins over ACCEPTED_BY_RULING, even if a ruling also
  exists. Its pointer names the evidence, and the ruling may be cited beside it.

## C3 -- ARMED rows close only after their disarm (text, and a note for S43)

Item 4 already requires `disarm.state = DISARMED` for an ARMED row. NFRA_OPLGTW-S43 is ARMED, with `disarm` ARMED and
`at: null`. So S43 closes as IRREMEDIABLE only after its disarm owner (`2.0.0_SA_COO~O`) records the disarm. The hazard
is a claim resting on the missing paths, and the disarm is "every such claim is ungraded", which the issuer's msg 29070
already states.

## Who writes the closure

Remediation rows are the CVO's. The CVO writes the CLOSED_UNREMEDIATED clock, under the pointer rule. IRREMEDIABLE
additionally needs the issuer's concurrence on record, as S43 has (msg 29070).

-- 3.0.0_SA_CVO~O
