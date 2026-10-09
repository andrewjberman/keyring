# ADVI_COTBKF decomposition -- ROUND 53 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~17:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:**
- `1.0.0_SA_CTO~DELL2` containment AMENDMENT 3 @4b7dcc5929 (msg 3764): "re-sweep COTBKF now, and again with the list. CB2's 4 files go
  by the re-sweep, not by hand." Until the served account-id hash list exists, the shapes are widened, and a 0 from shapes is not
  "clean".
- Row D2-S75 (CB2, msg 3762): the three shapes miss letter+8-digit and 11-digit account ids. Cleartext survives in files the round-51
  sweep rewrote.
- Rows D2-W78-S2 and D2-S73: the residual added-shape census (79 files with added shapes, 14 of them added-only; 2 tracked paths named
  by an account; 2 test files).

**Rule 24.** Domain: every tracked file the round-51 and round-52 tests scan, plus the tracked paths themselves -> one cell. The
re-sweep runs with the widened shapes AND against the project's own account set, which is read from the served Cottonwood account
column and kept outside the repo. The firm-wide list of record is `2.0.0_SA_COO~P2`'s; this cell does not build it.

## Measured constraints (issuer)

1. **Not in scope:**
   - `surprise-channel/` is append-only and the CVO's. Its hits are routed by relay.
   - The 7 completed orders are parked until the redaction gate limb lands (D2-S74). Their redacted texts are held outside the repo.
2. **Valid 9-character security ids can match the widened shapes.** Each such match goes to a named exception with its reason. An
   exception is never an account (the account-set check settles it).
3. **History is not rewritten.** A purge is Andrew's act.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ba-1` | widen both id tests (letter+8 digits, 11 digits, `z0`+9, `cv`+8), add an account-set check read from outside the repo; re-sweep and redact to `acct#<sha8>`; rename the 2 account-named paths; make the 2 test files synthetic; both tests 0 | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~80` |

**Fan-out:** `1 of 1 chains, cap 8`. The CB-al-2 re-cut pair and the CB-ax-2 redeploy pair are issuer acts on this round's drain.
