# ANDREW-DIRECT -- 2026-10-08 ~18:5xZ -- Alyssa can file on behalf of all partner firms

**Channel:** the `1.0.0_SA_CTO~DELL2` terminal on dell2, in-session. It answers the open act "the real X-1 filer entitlement: which Opal
person may file for which partner firm" (msg 944 (2); self-drive tick 4 act list item 1).

VERBATIM:

> Alyssa can file on behalf of all partner firms

## How it lands (this seat's ruling on the mechanics; his word sets the entitlement)

- **"All partner firms" is written as an explicit list, never as the `"ALL"` token.** `"ALL"` never admits (msg 944 (2);
  `interactive_access.py` drops it). The list is every partner firm in `data/firm_registry.json` today: `49financial`, `inflection` and
  `cottonwood`. `mockadv` and `demo` are test firms and are left out.
- **A future partner firm** joins Alyssa's list as part of that firm's own onboarding. His word covers all partner firms, so each
  addition needs no fresh word, but each is still an explicit edit.
- **The act:** set `allowedFirmIds` on Alyssa's existing `opal-users-v2` profile row (OPAL_GLOBAL, home opal-capital) to that list.
  - It is a data write that widens one principal, so it runs as a never-widen pair (COO half by `2.0.0_SA_COO~Y2`, CTO half by this
    seat).
  - The pair names: her row; its before-read (no value printed beyond the field); the one field changed; and a rollback to the
    before-value.
- **Effect:**
  - Once release 2 (E6) is live, she may create an Analysis upload for a client of any of those three firms.
  - The record names her as the actor, and the owner is a verified advisor of that firm (E5, ruling (c)).
  - TCKT_VNEXT TV-r-1's real run can use her sign-in.
