# MANDATE -- `3.0.0_SA_CVO~Z` -- grade the AMGT **Lead Panel** (B01 · L1-L4, W1, F1)

**Authority:** Andrew-direct 2026-09-24 ~02:5xZ: *"make sure they get their contracts and/or mandates, in
keeping with /closer logic"* -- and the `/closer` logic is what produced this file. **Step 3 requires one
MANDATE per implementing seat AND ONE PER MATCHING CVO.** Five COO mandates existed and only one CVO mandate
did. ⛔ **`COO~Y` was coming up on Lead Panel step 2 with NOTHING to grade it against. That gap is this file.**

**Contract:** `CONTRACT.md` (this folder). **Trace:** `LEAD_PANEL_END_TO_END_GAP_BRIEF_20260923.md` +
`.evidence.json`. **Proposal:** `CLOSER_PROPOSE_LEADPANEL_20260924.md` @`d2bbf82b3f`.
**Implementing seats:** `2.0.0_SA_COO~Y` (step 2, `COO_Y_LEADPANEL.md`) · `2.0.0_SA_COO~Z` (steps 1, 3, 5, 6).

## THE GRADING CONTRACT -- named up front, because you told this seat the last mandate lacked one

**INTERFACE `G-1`**: every partition is an **immutable GENERATION plus a `_CURRENT` pointer**, with the
`C-RANKING-GENERATION` contract governing republication (`AMGT-rk-20` re-published the bare price partitions
through it). Grade against:
- `lib/research/api/scoped_amgt.py` -- `resolve_axis` `:312-357`, pointer/generation reads `:413-556`,
  `_find_latest_served_pointer` `:558-582`, `read_rankings` `:584-653`, **`read_point_record` `:656-690`**,
  `read_rank_series` `:825-955`.
- `lib/research/metrics/chatter_axis.py` -- `:30-60` input, **`:424-427` source map and `DEFAULT_SOURCE`**.
- `lib/research/price/generation.py` · `portal/src/pages/SecurityAnalysis/types.ts:26-290` (`RankingSet`
  `:181-204`).
⚠ **`dated` and `requested_as_of` are NOT in `RankingSet` today** -- that absence IS step 3's defect, so grade
their ARRIVAL, not their presence.

## ⭐ CAPTURE THE BEFORE-STATE FIRST. YOUR OWN REASONING, AND IT APPLIES HARDER HERE

On Peers you captured a pre-build baseline before grading anything, because *"a before-state not measured
before the change can only be taken on the BUILDER's word afterward -- the party the grade is about."*
⛔ **STEP 2 DESTROYS ITS OWN BEFORE-STATE THE MOMENT IT DEPLOYS.** The numbers that vanish:

| property | today, deployed | denominator |
|---|---|---|
| `names_with_links` | **3** | **of 250** |
| `TRENDING_CHATTER` `row_count` | **2** | universe 191 |
| row `score` / `raw_chatter_count` | **0 / 0** | both rows |
| `BREAKOUT_CHATTER` | **EMPTY 9 consecutive days** | `NO_SIGNAL_IN_WINDOW` **189 of 191** |
| chatter Lambda digest | `I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=` | `chatter_axis.py` **37,443** vs **40,666** at HEAD |
| price `_CURRENT` | `TRENDING_PRICE#2026-09-15`, `BREAKOUT_PRICE#2026-09-15` | **32 rows each** |

⚠ **AND THE PRICE FALLBACK EXPIRES 2026-09-29.** After that both Price crosses read ABSENT with no rows. **A
baseline captured after 09-29 cannot distinguish "the producer never ran" from "the fallback aged out."**

## ACCEPTANCE -- the brief's matrix, unchanged. ONE RECONCILED TRACE PER CASE

A case reconciles when one control selection is followed through: the route's **resolution record** -> the
**pointer it followed** (`generation_id`, `state`, `row_count`, `as_of_date`, `dated`) -> the **rows served** ->
the **rendered resolution line, caption, rows and row states**.

**CROSSES (4):** Trending x Chatter · Trending x Price · Breakout x Chatter · Breakout x Price
**x VIEWS (3):** list · chart · starred-only
**x HOURS (2): before 10:00Z · after 10:00Z**

⛔ **THE HOUR AXIS IS LOAD-BEARING AND IS THE ONE A GRADER WILL COLLAPSE.** `read_rankings` computes "today" as
`_today()` in **UTC** and the chatter producer runs at **10:00Z**, so **every read between 00:00Z and 10:00Z
serves the previous day with `dated: true`.** And for an axis that is EMPTY every day, `_find_latest_served_pointer`
walks back only to a **COMPLETE** pointer -- so before 10:00Z it reads **ABSENT** ("no committed ranking exists
for this date") and after 10:00Z it flips to **EMPTY** with the `189 of 191` reason. ⭐ **TWO DIFFERENT SCREENS
FOR ONE UNCHANGED FACT, SELECTED BY THE CLOCK. A case graded at one hour only is HALF-GRADED.**

**plus SECURITY MODE (3):** `BA_US_Equity` (resolved, on the chatter list) · `PBR_US_Equity` (resolved, price
rank 1) · ⛔ **a row with `security_key` null (`SLB`, 1 of 32) that MUST NOT NAVIGATE** -- `RankedList.tsx:251`
renders UNRESOLVED without navigating; **this is a render-level refusal no route measurement can see.**
**plus ACTIONS (2):** star then unstar one name (**W1**) -- confirm the list filter moves **and that NO
rankings key was invalidated** · Refresh one name to **LANDED** (**F1**).
**plus FAILURE CASES (4):** expired session (401 -> refresh -> retry) · a **SHORT_READ** refusal (render the
refusal, **no rows**) · a series with `read_completeness.complete false` (**the chart must REFUSE**) · the
**no-firm 401** (measured: *"missing edge-injected X-Firm-Id"*).

## THE SIX STEPS AND WHAT EACH OWES YOU

1. **Live thread** (`~Z`) -- served stack, real login. **BLOCKED on Andrew's browser session endpoint** (`~Z`'s
   blocker, 02:30Z). Until it passes, **no offline closure counts toward any acceptance ID.**
2. **Chatter gold cutover** (`~Y`) -- proof: next `_CURRENT` with `row_count` on the order of the universe, rows
   with **non-zero `raw_chatter_count`**, and `names_with_links` above 3 **printed with its denominator**.
   ⛔ **A bare "improved" is not a proof clause; the RATIO is the claim.**
3. **`dated` on screen + the overlay's point-read fallback** (`~Z`) -- ⭐ **the discriminator is that the LIST
   and the OVERLAY must AGREE about the same name.** Today BA is rank 1 on the list (served 09-23) while its
   overlay says `point_status ABSENT` on every axis, because `read_point_record` has no dated fallback and
   `read_rankings` does. **Grade the agreement, not either read alone.**
4. **Price producer owner + run** -- ⛔ **UNOWNED; at Andrew.** Needs his **per-use vendor word (granted, R-15)**
   AND the **deploy ledger** for the first scheduled fire.
5. **Refresh wired to its carrier** (`~Z`) -- four field-level facts to confirm closed: the client calls the
   **pull route** not `/refresh`; the response type matches what the enqueue Lambda **actually returns** (today
   the client reads `queued`, which is `undefined`); the **outcome is rendered** (today only `isPending`); and
   the **consumer's trigger is named**. Vendor word granted (R-15).
6. **ABSENT beside EMPTY** (`~Z`) -- becomes the **negative control** once step 2 lands.

## LIMITS TO CARRY, AND ONE THAT BOUNDS YOUR OWN INSTRUMENT

⛔ **DIRECT LAMBDA INVOKE BYPASSES CLOUDFRONT AND `auth-validator-edge`, SO A `/market` REDIRECT -- WHICH THE
LIVE-THREAD CASE MAKES A FAIL -- CANNOT BE DETECTED BY THAT INSTRUMENT AT ALL.** You named this yourself on
Peers; it binds every case whose expectation is a rendered screen.
⛔ **ROUTE-PROOF IS NOT RENDER-PROOF.** Four routes measured credits no render, no column state, no caption, no
count.
- The edge header injection is **cited** from this seat's C4 measurement, not re-derived.
- `AMGT_MODEL_BLOCK_ROOT` / `AMGT_POOL_ROOT` are **unset** on the deployed function.
- The scanner universe is `asOf` **2026-08-06**; a stale-universe result is not a Lead Panel defect.
- `SLB` (1 unresolved row of 32), `description` ABSENT for BA, and `bloomberg_session_state` are **PARKED** --
  ⚠ though `bloomberg_health` now reads **`ok: true`, `127.0.0.1:8194`, `//blp/refdata`** (R-15), which is a
  **MOMENT, not a property**: it does not establish the session is up when a scheduled task fires.

**You do NOT sign the never-widen pair** -- that is CTO + COO halves on step 2's deploy. **You grade whether
the deployed bytes match the signed candidate.** Write surface: **your evidence folder only.** One
review-handoff message to the implementing seat and `1.0.0_SA_CTO~Z`. **Never fix what you grade.**
⚠ Working branch **`CLOUD`**; **commit, do not push.**
