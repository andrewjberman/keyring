# ANDREW-DIRECT 2026-10-02 ~02:08Z -- the portal push (to 2.0.0_SA_COO~X's terminal)

**Verbatim:** "we can do a portal push"

**Context:**
- The AMGT Friday demo's CORPUS Model tab (rounds 28-31, head c6aacc68) sat only in site-Z local portal DEV.
- Origin portal DEV (d79b9934, the laptop line) and CLOUD's portal gitlink after the 00:43Z parity did not carry it.
- This seat had reported the gap to `0.0.0_AB_MSTR~Z` at 09:38Z, 19:50Z and 00:47Z.

**Measured at 02:09Z (site Z):**
- local portal DEV 3c37a01c (contains c6aacc68);
- origin/DEV d79b9934; origin/PROD f2731ad3;
- local DEV is 45 ahead and 14 behind origin/DEV;
- `git merge-tree --write-tree DEV origin/DEV` is clean (rc 0, no conflicted paths).

**Routing:**
- Trunks (CLOUD/DEV/PROD) are pushed only by `0.0.0_AB_MSTR` / `0.0.0_AB_MSTR~Z`, on Andrew's word (LD-0367/0368; CLAUDE.md
  Portal).
- This seat relays the word verbatim to `0.0.0_AB_MSTR~Z`, who holds the push. The scope is the portal DEV push: a pull-merge of
  origin/DEV into site-Z DEV (never a rebase), then the push.
- **Not in scope of the words:** the DEV-to-PROD promote, and a CLOUD gitlink move. Neither is widened here; MSTR~Z asks Andrew if
  wider is meant.
