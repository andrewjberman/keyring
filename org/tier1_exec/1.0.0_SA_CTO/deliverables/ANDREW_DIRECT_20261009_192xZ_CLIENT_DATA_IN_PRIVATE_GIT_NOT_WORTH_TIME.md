# Andrew-direct 2026-10-09 ~19:2xZ -- client data in the private git: not worth more time

**Where:** 1.0.0_SA_CTO terminal (laptop). **Verbatim:**

> I don't care about the client data getting committed to Git. Git is a private Git and there's only one user. So that's that spending time
> messing around with that is I don't think is really worth it.

## What this seat does with it (scope: his words, nothing wider)

1. **No history purge.** The "purge yes/no" item comes off his list; nothing is rewritten.
2. **The containment sweep stops** (dell2 containment ruling @0e8209c33c items 1-5): no further moving, redacting or renaming of tracked files
   for account ids. What already landed stays; nothing is reverted.
3. **`client-data-check.py` (8c1d8a1966) stays wired and WARN-only.** The hashed id list it needs is NOT built (dell2's builder ask is
   withdrawn), so it never refuses a commit. Removing it is not needed; it costs one warning line per commit.
4. **The to-pipeline-gate redaction and rename support stays** (9caacb0f35, 24bdcd2690, 8fff05ca26). It is harmless and already landed.
5. Relayed to dell2's CTO and the managers via `0.0.0_AB_MSTR`.
