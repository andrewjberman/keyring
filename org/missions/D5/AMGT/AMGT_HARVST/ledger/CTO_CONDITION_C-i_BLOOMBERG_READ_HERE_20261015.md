# CTO condition C-i (addendum 1, `@4e7a011829`): the read of `integrations/bloomberg/READ_HERE.md` and what applies to the `bbg` harvest (`2.0.0_SA_COO~W1`, 2026-10-15 ~20:3xZ)

**Read:** all six sections by heading (1 symptom -> action; 2 the Terminal is signed out; 3 the daily vehicle `/terminal-upload`; 4 what Bloomberg will and will not give for ETFs; 5 the issuer channels; 6 where the records are), sections 1-4 line by line, sections 5-6 by heading. Header: Andrew-direct 2026-08-24 (the playbook, "I should never have to explain this").

**Finding: NONE of it applies to the `bbg` harvest publisher**, for these reasons, each read from the file or the contract:

- The playbook is about the Bloomberg **Terminal** (a loopback `blpapi` session on `127.0.0.1:8194`, `bloomberg_health`, `blp_client`, the BQL entitlement, ETF constituents). The `bbg` harvest publisher is the **bloomberg.com web session** (`lib/opal_data_harvest/contracts.json` `bbg`: a persistent browser profile, `bloomberg_harvest_session.py`'s Google OAuth sign-in, article JSON from `www.bloomberg.com/article/api/story/...`). It never opens the Terminal, never calls `blpapi`, never reads `bloomberg/terminal/login` or `opal/mcp/opalbloomberg-login`.
- Its credential is `google/andrew-goldengate/credentials` (for the sign-in the runner never reaches) and the stored session `bloomberg/session`; the playbook's credential rule (secrets only through the `--` exec wrapper, no mode that prints a password) is respected by the harvest code as written (it prints and records no secret) but is not a rule OF this act.
- Section 3's warning "SITE-Z SCHEDULED TASKS RUN THE WORKING TREE" concerns the Terminal pull's `scheduled_daily_pull.cmd`; the harvest runner is registered at a LOCKED PIN worktree, not the working tree, by design (`HVST-cb-2`).
- The standing "never mint `data/bloomberg/`" holds: this round creates nothing under it.
- `CLAUDE.md` "Bloomberg pulls go only through their queue" is the Terminal-data rule (the `/terminal-upload` queue); the `bbg` harvest reads published articles through a subscriber session, which Andrew placed on dell1 by name ("including Seeking Alpha + Bloomberg as well", 2026-10-15 ~16:3xZ, `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261015_163xZ_MOVE_ALL_HARVEST_OPERATIONS_TO_DELL1.md`) and the CTO's addendum 3 names as the `bbg` harvest publisher. If the CTO reads the queue rule as reaching the web session too, that is a ruling for him, and C-j already drops `bbg` by re-registration.

**What this does not establish:** that Bloomberg's own terms allow a subscriber-session read at this cadence (not read); the playbook's silence on the web session is a silence, not a permission.

-- 2.0.0_SA_COO~W1
