# ANDREW-DIRECT 2026-09-22 ~12:5xZ -- AMGT_RESAPP keying structure, IEFA global universe, Bloomberg's most stable key

**Where:** the `1.0.0_SA_CTO~Z` terminal (site Z). There were two messages mid-turn, while this seat was building the
backfill scope proposal (`prd/BACKFILL_SCOPE_PROPOSAL_20260922.md` @`51431810dc`). **Extends:** the ~12:2xZ record
@`2a192b6e07` (no backfill until the security list and channel inventory are confirmed).

## VERBATIM

> "Yeah we also need to identify our keying structure, if CIK is the primary, ticker is fallback, etc. That is something
> that needs to be designed into the process based on what has the most coverage. Also the universe that it appears we
> are going to be doing this for is IEFA which is global, so we should be foreign-friendly non-US from the start with
> that in mind."

> "I think keying off of Bloomberg's most stable key is probably the way to go with this in mind"

## WHAT IT RULES (the narrow reading, stated as such)

1. **A third precondition to any backfill: the KEYING STRUCTURE.** It sets the primary identifier and the ordered
   fallbacks, and it is designed into the process on MEASURED coverage.
2. **The universe the backfill is designed for is IEFA** (global, non-US developed markets). The design is
   foreign-friendly from the start. A US-only identifier (CIK) cannot be the primary.
3. **His stated direction for the primary key is Bloomberg's most stable key.** He says "probably"; this seat records
   it as a direction, not a final ruling. Which Bloomberg identifier that is (for example the FIGI / `ID_BB_GLOBAL`
   family versus the ticker-derived key in use today) is the design question. It returns to him with coverage and
   stability measured.
4. **Not ruled:**
   - Whether IEFA replaces the 36-name proposal as the backfill list, or is the target the 36 are a first slice of.
     The proposal @`51431810dc` is re-cut against IEFA once the key design lands.
   - The migration of today's `security_key` (`<ROOT>_<CC>_Equity`, ticker-derived). It is a design output, not
     assumed.

## ACTS

- This record, committed; broadcast to `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`, `4.0.0_SA_CRO~Z` and `0.0.0_AB_MSTR~Z`.
- A DESIGN FORK, so it is routed to `4.0.0_SA_CRO~Z` for research on past patterns under the self-drive call routing.
  The research covers:
  - the estate's existing identifier patterns;
  - Bloomberg identifier stability;
  - identifier coverage measured over IEFA's constituents;
  - the blast radius of re-keying.
- `1.0.0_SA_CTO~Z` decides when the research lands and returns the key design to Andrew with the re-cut list and
  inventory as ONE confirmation card.

-- `1.0.0_SA_CTO~Z`
