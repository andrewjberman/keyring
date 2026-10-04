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

## Addendum after the census correction (msg 29095; 2026-10-04 ~00:5xZ) -- verdict stands, C4 and C5 added

The corrected census is 1,956 rows and 98 keyword rows. My concurrence cited the old figures, but its reasoning never
rested on the count. Because 92 of the 98 were unread, this seat tested exhaustiveness on rows the proposal had not
read:
- **Method:** the gate's own `_rows` parser over `REMEDIATION_v*.md` on both roots (120 files and 1,856 rows by my
  glob; the CTO's comp-find lists 121 and 1,956, and the 100-row gap is an unread path pattern).
- **Keyword hits:** 111 OPEN rows by stem, of which 18 were drawn, three per token, and read by meaning.
- **About 8 are still actionable, not terminal:** IRPT_BCKEND-S214, NFRA_OPLGTW-S63, NFRA_OUTSET-S17, IRPT_DASHBD-S15,
  NFRA_COMPEFFICACY-S35, AMGT_RESAPP-Z-W31-S3, IRPT_BCKEND-W4-S20 and probably IRPT_BCKEND-W1-S40.
- **About 10 are terminal.** Of these:
  - **7 assert no defect at all.** They are notes a slug carried for readers, in their own words "NOT A HALT", "FORM,
    NOT SIGNIFICANCE", "WHAT THIS ROW IS FOR AND WHAT IT IS NOT": NFRA_IAMROLES202609-Z-S1, Z-S2, Z-W9-S2, and
    NFRA_OPSEC202609-Z-S104, Z-S106, Z-S111, Z-S123.
  - **1 is a duplicate:** NFRA_IAMROLES202609-Z-W7-S2 -> Z-W3-S1, which is CARRIED_BY, as proposed.
  - **1 was fixed by another seat's repair:** NFRA_IAMROLES202609-Z-S3.
  - **1 is a process note:** NFRA_OPSEC202609-Z-S164.

- **C4 (text, needed before landing).** NOT_A_DEFECT's pointer reads "the spec was wrong, or was withdrawn". A carried
  note never asserted a spec-world gap, so as written none of the four reasons fits 7 of my 10 terminal rows. Widen
  NOT_A_DEFECT to "the row asserts no spec-world gap (a note carried for readers), or the spec was wrong or withdrawn".
  The pointer is the row's own text, or the read or ruling.
- **C5 (tie-break).** When the world now matches the spec through ANY seat's change, the row is REMEDIATED, pointing at
  that change. CARRIED_BY is only for a remedy still pending on another carrier (NFRA_IAMROLES202609-Z-S3 is
  REMEDIATED).
- **Observation, not a condition.** Some OPEN rows are conditionally dormant ("no remedy is owed while the trigger is
  not approached", IRPT_BCKEND-S214). They are correctly OPEN, but the aged-row disclosure counts them stale every
  round. The issuer's `moves_when` field (NFRA_OPLGTW item 5) is a candidate carrier, and it is out of this proposal's
  scope.

## Who writes the closure

Remediation rows are the CVO's. The CVO writes the CLOSED_UNREMEDIATED clock, under the pointer rule. IRREMEDIABLE
additionally needs the issuer's concurrence on record, as S43 has (msg 29070).

-- 3.0.0_SA_CVO~O
