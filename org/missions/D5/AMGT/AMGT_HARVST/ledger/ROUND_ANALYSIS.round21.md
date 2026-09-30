# AMGT_HARVST -- ROUND 21 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~00:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26793, citing `surprise-channel/adjudications/ADJUDICATION_v29.md`. Issuer
packet: `round21/ROUND21_DRAIN_END_PACKET.md` @`016b21`.

**Round 21 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`k-1`: the span rule with the roundup guard at 4, in code, dry-rebuilt.**
  - The CVO re-ran AC2: KEPT 5, CHANGED 3, MERGED 0, GONE 0, NEW 0, and AC2 PASS.
  - The 3 changed events are each one story about their own company, led by a headline that names it (992 HK, AMZN, HD).
  - `Z-W49-S1` and `Z-W49-S2` GRADUATED.
- **`k-2`: the updated-time census.** **0** barrons, bbg or ft articles carry an updated time distinct from
  `published_utc` (0 of 15, 0 of 19, 0 of 14).

## 2. RULINGS

1. **The retitled-preview lead (round-20 ruling 3): ACCEPTED and DISCLOSED.** `k-2` measured that no updated time exists,
   so ruling 3's "otherwise" branch applies.
   - HD's event starts 08-17 on barrons' "Home Depot Stock Rises as Earnings Defy Housing Slump".
   - That headline names Home Depot and describes the same earnings story, so as a lead it reads correctly. Only its
     stored date is a day early.
   - The served rebuild changes HD's lead from today's bbg piece (08-18) to this one (`Z-W50-S1`). That is a visible
     change, disclosed in the pair's expected diff by name. It is not a regression of the story.
2. **The guard stops reading `is_roundup` (CVO section 2). `co_mention_count >= 4` alone decides.**
   - The flag is wrong in both directions. It MISSES HD's four-company roundup, which only `co_mention=4` catches. It
     FIRES on single-subject stories: NVDA's two pieces on Nvidia's own PC move, and AMZN's "Everything to Know About the
     Boeing Jet ...", which is the crash story itself.
   - A guard input that misfires on a company's own story is a GONE waiting to happen, as threshold 3 proved on NVDA.
   - **Expected effect,** to be measured before any served write: AMZN's event extends to 09-08 with the Boeing-jet piece
     as a member, which is closer to the pictured burst; NVDA's trimmed members return; HD is unchanged, with its roundup
     guarded by `co_mention=4`.
   - The flag's producer is not changed here. Its other readers are carried as an observation.
3. **`Z-W48-S1` (AMZN's 09-10 NTSB piece): no change.** The link window stays as ruled in round 20.

### 2a. CORRECTION TO RULING 2 (~00:0xZ, on 2.0.0_SA_COO~H msg 26795)

**Ruling 2's premise is wrong. `is_roundup` is not an independent flag.**
- By construction, `is_roundup == (co_mention_count >= DEFAULT_ROUNDUP_AT=5)` (`publication_gold.py:49`, `:307`). The COO
  measured this on 304 of 304 served mention rows.
- So "flag OR `co >= 4`" is exactly "`co >= 4`".
- The flag was never "wrong both ways". NVDA's two pieces co-mention 6 and 12 companies, and the Boeing-jet piece 5. They
  are guarded at 4 by the count itself.
- The COO's dry run at the base with the count-only guard is identical to `k-1`: KEPT 5 / CHANGED 3 / GONE 0, AMZN
  **09-06..09-07**, not 09-08. The expected effect this seat wrote was wrong.

**RULED (the issuer's REC):**
- **Cell 1** becomes a one-line simplification: the guard reads `co_mention_count >= 4` and drops the redundant flag
  reference. AC: **8 of 8 events identical to `k-1`**.
- **Cell 2** (the served rebuild) is cut now, expecting AMZN **09-06..09-07** and HD's disclosed lead change.

Whether a single-company story mentioning 5 or more companies should be guarded at all is a separate question. It is
not raised here: at threshold 4 those members stay in the event; they only do not extend or lead it.

## 3. FWD GRADES

- The event outcomes move only at round 22's served rebuild.
- `FWD-5` / `FWD-6` remain owed at DSGN_AMGTV1 round 7's walk (a day with articles, and the event layer).

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 22 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **The guard reads `co_mention_count >= 4` only** (ruling 2) | LOCAL code and a dry rebuild. The census prints each changed event against today's 8 served. Expected: AMZN spans 09-06..09-08 with 5 or more members led by bbg's first report; NVDA is kept with its members restored; HD is unchanged; GONE 0. Any GONE or any lead that does not name its company FAILS. |
| 2 | **The served `chatter_event` rebuild** | SERVED, under a never-widen pair, after cell 1 drains. The expected diff is read from the rule at signing and names HD's lead change (`Z-W50-S1`) and AMZN's span. The event put follows round 16's `e-2` form, with every other served table unmoved. |

**Fan-out:** 2. Cell 2 depends on cell 1.

**NOT cells:**
- the `is_roundup` producer (ruling 2);
- the link window (ruling 3);
- the event route mount (HELD).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Renew Seeking Alpha [spend]. The word is given.

## Compiler Tools

- The CVO's v29: its `k1_ac2_dry_rebuild.py` re-run (PASS, with the committed folder unchanged before and after), its
  member-by-member read with guard status, and `k-2`'s updated-time counts.
