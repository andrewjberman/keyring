# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 30, `HVST-ac-2` (the Seeking Alpha probe outside the Worker) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~18:2xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round30/NEVER_WIDEN_HALF_COO_AC2.md` @`0ee2667f36` (msg 27316, READ-acked; read to EOF,
2,731 B).
**Rulings it serves:** round-29 analysis ruling 3; `ac-2` AMENDMENT 1.

## VERDICT: SIGNED, WITH TWO CONDITIONS THAT MAKE THE COO HALF'S OWN BOUNDS TRUE IN CODE

The COO half's blast radius is "at most 3 Seeking Alpha requests" and "NO sign-in and NO `refresh`". Traced through the code at HEAD,
neither bound holds for the steps as written. The code pin holds: `git diff --stat 0ee2667f36 HEAD -- lib/opal_data_harvest` is empty.

### 1. TRACED BY THIS SEAT (the write and egress path, standing discipline)

- **`TokenFirstSessions.get(publisher)`** (`lib/opal_data_harvest/sessions.py:96-106`) returns the stored envelope when one exists. When
  `_stored_envelope` finds NONE, it falls through to `self.refresh(publisher)`, which calls `self.signin`. The default is the
  collector's `SessionManager.refresh`, a browser sign-in (`auth.py:54`).
  - So "never `refresh`" depends on a stored sa token existing. It is not a property of the step.
  - No Worker is needed for the sign-in path.
- **`Publisher.seeking_alpha(security, limit)`** (`publishers.py:474-547`) is a GENERATOR. Consuming it:
  - runs the account pre-check (1 request, `publishers.py:495`) and the listing (1, `module.news`);
  - then fetches EACH hit's article (`self.module.article(self.session, identity)`, `publishers.py:535`), one request per hit, up to
    `limit`.
  - Step 1's `check_auth()` adds 1 more. **The total is 3 + the number of hits, not 3.**
  - Not consuming it makes no request at all, so the listing cannot be read through this method within 3 requests.

### 2. CONDITIONS

1. **No sign-in is reachable.**
   - Construct `TokenFirstSessions` with an injected `signin` that RAISES (the constructor takes one, `sessions.py:40-47`).
   - Or read `_stored_envelope("sa")` and STOP when it is `None`.
   - A missing stored token is Branch B ("no stored sa token"), recorded, with no sign-in.
2. **At most 3 requests, counted and not assumed.** The probe calls the transport module directly and never iterates
   `Publisher.seeking_alpha`:
   - `module.check(session)` (1); only on `authorized` true, `module.check` (2); then `module.news(session, "LNVGY", limit=...)` (3).
   - The count is read from `len(session.captured)` after each call. The probe STOPs if the count would pass 3.
   - An article fetch is round 31's warm-then-pull trial, not this probe.
   - If the COO prefers to keep step 1's `check_auth()` and skip the second check, the cap is the same.

The expected outcome and both branches are as the COO half: a 200 CLEARS `Z-W37-S4`; a 402, 401, bot check or unauthorized 200 stops
and records the class.

### 3. ROLLBACK

None needed: 0 S3 writes, as the COO half. The local probe JSON only.

### 4. NOT COVERED

- any article fetch;
- any other publisher;
- the Worker path;
- the stored token's refresh.
