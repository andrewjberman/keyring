# AMGT_HARVST -- ROUND 19 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~22:3xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, subject *"L10 slug AMGT_HARVST round 19 @036adf6715"*, citing
`surprise-channel/adjudications/ADJUDICATION_v27.md`. Issuer packet: `round19/ROUND19_DRAIN_END_PACKET.md` @`86ee31f531`.

**Round 19 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **A PARTIAL day now carries which publishers it rests on, end to end:**
  - `i-1`: UBS is off the whole-brand list, with the limb-agreement test.
  - `i-2`: the code gains `publishers_covered_codes`.
  - `i-3`: the gold rebuild, one daily put, with the 21 existing columns unmoved.
  - `i-4`: the scoped-API redeploy, CodeSha256 `uv0oTSMa...` at 21:57:59Z. The entry is CLOSED @`84548218ef`, and the
    artifact carries exactly the 3 signed files (this seat's diff, tick 7).
- **The CVO re-read gold:** 148 `["sa"]` (ASML_NA/US x74), 1 `["wsj"]` (992 HK 2026-09-23), 51,803 `[]`.
- `Z-W45-S1` and `Z-W45-S2` GRADUATED.

## 2. RULINGS

1. **What "covered" means (CVO section 2): the page never says "covered by". This is ruled in DSGN_AMGTV1**
   (`ROUND_ANALYSIS.round5.md` s.2a @`7615f688be`, before its round-6 cut).
   - By the producer's rule (`publication_gold.py:553-592`), a publisher covers a day when its listing SEARCH reached it.
   - Every PARTIAL day the CVO opened serves 0 articles.
   - The page says "Searched: Seeking Alpha -- nothing found. Not reached: 4 other publishers."
   - **The API field names stay** (`publishers_covered`, `publishers_covered_codes`). Renaming a served field breaks its
     readers for no user gain once the page words it correctly, and the producer's docstring already states the
     definition.
2. **`Z-W39-S1` (ARMED since round 15): cell 1.** `timeline_api.get_timeline_event` (route 3,
   `timeline_api.py:368-378`) recomputes `event_id` from `(security_key, first_day, last_day)`. Since `HVST-b-1`, a
   stored `event_id` carries the story, so the recomputed id matches no `chatter_event.event_id`, and two events on one
   `first_day` cannot both be served (the loop returns the first match). The route must serve the stored event by its
   stored id. This is a served correctness defect, and the page's event window reads through this route.
3. **`Z-W41-S1` (ARMED: the AMZN crash forms ONE 3-article event on 09-07, not the 6-article 09-06..09-10 burst): cell 2 as
   a MEASUREMENT, not a rule change.** Whether a story spanning consecutive days is one event is the event rule's own
   question. The cell measures before anything is ruled. It runs a LOCAL dry rebuild under a candidate span rule (the
   same story across consecutive days joins one event) and prints:
   - the AMZN fixture's event;
   - how many of today's 8 served events would change;
   - every new merge, listed.
   This seat rules the rule on that census at round 20's analysis.
4. **`Z-S37` (`safe-merge --continue` whitelists what the INDEX holds): routed to the tool's owner, not a project cell.**
   The same class landed in AMGT_CORPUS `Z-S59` today. Two projects with one defect in `.tools/safe-merge.sh` make it an
   integrator item. It is PARKED on 0.0.0_AB_MSTR~Z, which un-parks when that seat is live. The pointer is sent.
5. **FWD-5 / FWD-6's page half is now pushed.** The timeline panel `92a2576254` is on origin/DEV (MSTR~Z's push,
   `ac8265668d`; `--is-ancestor` true). The page side is graded by DSGN_AMGTV1's round-6 walk, which carries these two
   outcomes as named judgments beside its own FWD-5 (the same panel). One walk grades both projects' clauses; nothing is
   walked twice.

### 2a. CORRECTION TO RULING 2 (~22:3xZ, on 2.0.0_SA_COO~H msg 26759 and row `Z-S42`, decomposition s.32 @58fbe48402)

Ruling 2 called `Z-W39-S1` "a served correctness defect ... the page's event window reads through this route". **The
premise is wrong.**
- The event route answers no user. The deployed function 404s it, and the gateway's 108 routes carry only `/timeline` and
  `/timeline/day`.
- The adapter leaves it unwired, and `TimelinePanel` never calls it.
- Events reach the page inside `/timeline`'s `events` array, not through this route.
- So the defect is LATENT in unmounted code.

**RULED: HOLD the mount (the issuer's REC).** Nothing is mounted until DSGN_AMGTV1's page needs an event window by id; no
page outcome asks for one today. Round 20's `j-1` stays a LOCAL code fix (the route reads the stored id; two events on
one `first_day` are both answerable) with its tests. It carries no deploy, pair or gateway change, so a later mount
starts from correct code. Cell 1's "deployed under a never-widen pair" is withdrawn.

## 3. FWD GRADES

- `FWD-5` / `FWD-6`: NOT REALIZED, now **only the grade is owed**. The served half is met and carries the alias rule and
  the publisher codes. The page half is pushed and is graded at DSGN round 6's walk.
- The others stand as `ROUND_ANALYSIS.round15.md` left them.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 20 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **The event route serves the stored event by its stored id** (`Z-W39-S1`) | Code. Deployed under a never-widen pair (a redeploy of `opal-amgt-scoped-api`). `/timeline/event/<id>` returns the `chatter_event` row whose `event_id` equals `<id>`, and two planted events on one `first_day` are both served by their ids. AC: all 8 served events answer 200 by their stored ids (at base, today, the recomputed id misses), and every other route is byte-equal. |
| 2 | **The story-span census** (`Z-W41-S1`) | LOCAL, measurement only. The dry rebuild prints the AMZN fixture's event under the candidate span rule, the served-event delta (of 8), and each merge. No rule change and no put. |

**Fan-out:** 2, independent.

**NOT cells:**
- the page wording (DSGN_AMGTV1);
- `Z-S37` (the tool's owner);
- a field rename (ruling 1).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Renew Seeking Alpha [spend]. His word is given ("seeking alpha will renew", @d0e74747a9). Row `Z-W37-S4` stays until the
  402 clears.

## Compiler Tools

- The CVO's v27: its pyarrow gold read, its `/timeline/day` invokes (4 PARTIAL days, 0 articles each), its reading of the
  coverage rule, and its entry sweep across 16 worktrees.
- This seat: reads of the carried rows `Z-W39-S1`, `Z-W41-S1` and `Z-S37` from the investigation channel;
  `git -C portal merge-base --is-ancestor 92a2576254 origin/DEV` = true.
