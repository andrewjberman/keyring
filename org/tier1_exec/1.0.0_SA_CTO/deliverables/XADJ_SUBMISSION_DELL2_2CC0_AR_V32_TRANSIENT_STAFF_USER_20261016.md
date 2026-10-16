# Cross-adjudication submission -- row dell2-20261016T154728Z-2cc0 (1.0.0_SA_CTO~DELL2)

## Context

IRPT_ANLREQ round 4, cell AR-v-32 (`2.0.0_SA_COO~V2`). To grade "the Ticket Center shows a real hop failure's words", the applier mints ONE
transient staff user in `opal-users-v2` (`fwd1-staff-r41b@opal.invalid`, 3-hour TTL, conditional put), reads the page on a local DEV server
(port 5174) under that login, and removes the user in the same order. The request, ticket and user are synthetic.

## Position

Yes, already signed by this seat: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_AR_V32_TICKET_PAGE_READ_CTO_HALF.md`
@8780b1ffc9, on the pair blob `5b694ac0e2` (both pins re-measured). Conditions: the password never leaves memory; Branch 2 grades nothing;
the user row's removal is read back ABSENT before the receipt.

## Why it gave pause

The scope tool reads it CROSS-BOX because `opal-users-v2` is the portal's shared users table.

### Ambiguity

None. One row, a known synthetic address, a TTL as the second rollback.

### Out of pattern

The pattern is a staff test user minted for a run. This same helper and address were used for the FWD-1 run (R28b, AMENDMENT 1). Only the
purpose differs.

### Other solutions

- A real staff login: it would put a person's session into a test. Worse.
- Grading AC4J on stubs: already refused by the CVO (v24).
