# AMGT_HARVST -- ROUND 27 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~10:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27071, *"L10 slug AMGT_HARVST round 27 @4e1b871ba7"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v36.md` (read to EOF, 5,649 B). Issuer packet: `round27/ROUND27_DRAIN_END_PACKET.md`
@`699fb78c93`.

**Round 27 is CLOSED:** 7 of 7 terminal (5 complete, `q-1` and `q-7` withdrawn), rows dispositioned, 0 judgment criteria. **The
project is NOT closed.** The PRD moves to v0.5 in this commit (one clause of `C-HV-RANK-DECLARED-SET`, ruling 1).

---

## 1. WHAT THE ROUND DELIVERED

- **`q-1`'s act wrote exactly one object**, the run record. The CVO scanned 3,058 objects under `amgt/harvest/`. No served gold
  moved, and the pair held on both branches.
- **`q-2`:** the bbg silver parse is fixed in code; 11 of 11 held objects now parse non-empty. The served rebuild is round 28.
- **`q-3`/`q-4`:** the declared-set rule is in the gold branch. Eligible names: **0 of 191**, re-derived by the CVO.
- **`q-5`:** `publishers_found_codes` is emitted and served on `/timeline` rows in a LOCAL build (271 found-not-covered rows over 67
  securities). It is served after the next paired daily rebuild.
- **`q-6`:** barrons's bounded repair after a same-job reauth, and ft keeping its 403 body (redacted, capped). Replayed with 0 network
  calls.
- **Why bbg refused** (`Z-S45`):
  - the job made no listing request, because the listings were same-day cache;
  - its one live request re-fetched `bbg:NM5NLQ6K50XZ01`, the key `p-2` records as rejected;
  - that request got a 403, and the repair saw no checkmark.

## 2. RULINGS

1. **THE DECLARED SET IS DERIVED FROM CONFIG, NOT OBSERVED AND NOT TYPED** (the CVO's contract-fidelity point, v36 s.1). PRD v0.5.
   - The set is every publisher in `ENABLED_PUBLISHERS`, minus any whose collection refused for the whole universe in the window.
   - sa covering ASML on 26 days (a per-name trial) neither adds sa nor keeps it out. sa is in the set if and only if it is
     enabled.
   - **The code types the set today:** `chatter_axis.py:450` `DEFAULT_DECLARED_PUBLISHERS = ("bbg", "wsj")`. That is the defect a
     contract cannot see, and round-28 cell 4 derives it.
   - The CVO is right that eligibility stays 0 either way: adding a publisher only tightens it.
   - **AMENDED ~09:5xZ (CVO~Z msg 27076, PRD v0.6):** the exit rule reads "refused OR ran no job" in the window, and an EMPTY
     declared set HOLDs (`NO_DECLARED_PUBLISHER`). Without it, an enabled publisher that never ran would keep every name ineligible
     indefinitely. A publisher that ran even one per-name job stays in; the names it did not cover are ineligible.
   - **AMENDED AGAIN ~10:1xZ (CVO~Z msg 27081, PRD v0.7):** "ran no job" becomes "ran no UNIVERSE-SCOPE job". The v0.6 line above let
     sa's ASML trial hold 189 of 191 names ineligible on a publisher that never searched them. That was this seat's inconsistency with
     its own v0.5 intent and with the CRO's partial-rank research. Today every publisher's jobs are per-name trials, so the set is
     EMPTY and the rank HOLDs (`NO_DECLARED_PUBLISHER`). The first universe-scope backfill (round 29) brings its publisher in.
     Round-28 cell 4's AC plants a trial-only publisher (it exits) and a universe-scope run (it enters). The census prints, per
     excluded name, the declared publishers it lacks.
2. **A key rejected for its body (`short_or_partial_body`) is HELD for the rest of that UTC day** and retried on a later day.
   - After 3 failed days it is recorded `rejected_final`, with its reason, and never re-fetched.
   - This replaces `p-2`'s "re-fetch rejected keys every run": that rule spent the job's only live request on a known-bad key and
     ended bbg `request_rejected`. The run record names the hold.
3. **Cached listings must still record reach** (`o-1`'s gap, `Z-W70-S1`). A listing page served from same-day cache is still
   evidence of the span it covered. The reach is written from the cached page's own date bounds, marked `from_cache`.
4. **[SUPERSEDED IN PLACE, ~09:5xZ, COO~H msg 27075]** ~~The story-id rows supersede the 11 hash-keyed rows through the
   `silver_latest` tie-break.~~ **That was wrong.** `store.silver_latest` (`store.py:391-393`) groups by `article_key`, so the
   tie-break orders rows of ONE key only. The fixed parse keys by story id, which is a different key, so a rebuild ADDS 11 rows
   and the 11 empty hash-keyed rows stay served.
   **RULED (on the issuer's REC):**
   - keep them, no delete;
   - the bbg silver pair's AC proves them INERT on every served reader: 0 mention pairs, absent from every served article list
     (`/timeline/day`, the company query);
   - it also proves each of the 11 story-id rows is served non-empty.
   - A reader-side exclusion of empty rows is NOT ruled. A reader filter would hide the next empty row too, and an empty row is a
     defect to see, not to filter.
   - If the AC finds any empty row reachable from a served list, the pair STOPs, and the exclusion comes back to this seat.
5. **FWD-7 is bound by collection reach, not the rank rule.** Widening reach is a large scripted vendor act (R-21). It starts,
   per `C-HV-EGRESS`, with the pre-run print of planned listing pages per publisher over the 190 names, with no request sent.
   That print is round-28 cell 5; the run is round 29 under a pair.
6. **The issuer's `<expect>` authoring defects:** plain printed tokens only. Agreed as discipline, not a gate.

## 3. FWD GRADES

| FWD | grade | what moved |
|---|---|---|
| 1 | NOT REALIZED | 2 of 5. The barrons and ft fixes are code (`q-6`); their runs are Andrew's (R-21 call 1). |
| 2 | NOT REALIZED | The bbg parse is fixed in code. The served silver rebuild is round 28. |
| 3 | NOT REALIZED | Per-key outcomes are exercised on a real run (`q-1`: 26 skipped as held). `keys_stored_join` is still unexercised (0 stored), and `publishers_found_codes` is not yet served. |
| 4 | REALIZED | standing |
| 5 / 6 | NOT REALIZED, page half MET on local DEV | the portal promotion (Andrew); DSGN's found-only wording (DSGN round 12 cell 4) |
| 7 | NOT REALIZED | The rule is in place and 0 of 191 are eligible. It is bound by reach. |
| 8 | REALIZED | standing |
| 9 | NOT REALIZED | one name |

**2 of 9 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 28 in ONE issuance

| # | cell | FWD | risk | note |
|---|---|---|---|---|
| 1 | **Reach from cached listings** (ruling 3) + **the rejected-key hold** (ruling 2) | 7, 3 | LOCAL | The AC replays `q-1`'s events: the cached wsj pages yield a `reached_span`, and `NM5NLQ6K50XZ01` is held, not fetched. |
| 2 | **A fresh-day span-bearing Lenovo bbg/wsj run** on cell 1's code, then the daily rebuild (serving `publishers_found_codes`) | 7, 3, 5 | WORLD, pair + R-21 | This is `p-3(b)` re-cut. It runs after cell 1 merges, and the pair is signed against the merged code. |
| 3 | **The served bbg silver rebuild** on `q-2`'s parse | 2 | WORLD, pair | The pair names the 11 rows (ruling 4). It is independent of cell 2's run, but the two do not overlap: whichever pair signs first runs first. |
| 4 | **The declared set derived** (ruling 1): `ENABLED_PUBLISHERS` minus universe-wide refusals, read from the run records | 7 | LOCAL | The AC plants a run record with an ft universe-wide refusal: ft leaves the set. With sa enabled, sa is in. The printed population names the set. |
| 5 | **The pre-run listing-page print over the 190 names** (`C-HV-EGRESS`) | 9, 7 | LOCAL, with no request sent | The output is per publisher and per name, with the planned pages at the config ceiling. It is the input to round 29's backfill pair. |

**Fan-out:** 1, 3, 4 and 5 are independent. 2 follows 1.

**NOT cells:**
- the `gold` flip (it waits on at least 10 eligible names);
- the backfill run (round 29);
- the barrons and ft runs (Andrew's).

## 5. ACTS ONLY ANDREW CAN DO (cited)

- The barrons B1 run and the ft F2 credentials [R-21 @`b390c36444` call 1].
- Re-arm the harvest schedule [`ledger/HANDOFF_L4_TO_L5_COO_Y_20260922.md:81`].
- The portal DEV merge and push [CLAUDE.md Portal] (FWD-5/6).
- Remove the worktrees `wk-hvst-r24..r27` [CLAUDE.md Agent Autonomy: recursive deletion].

## Compiler Tools

- The CVO's v36: the `amgt/harvest/` scan (3,058 objects, 1 modified), the gold part stamps, and the census re-derivation.
- The packet's section 2 (`Z-S45` from `events.jsonl`).
- This seat read `chatter_axis.py:450` (the typed declared set) and `publication_gold.py:375` (`ENABLED_PUBLISHERS`) for ruling 1.

## AMENDMENT 2 -- cell 2 runs TODAY as the cached-path arm (2026-09-30 ~10:3xZ, COO~H msg 27090)

**RULED on the issuer's REC.** `aa-1` merged @`0df90b1535`: cached listings now record reach (`from_cache`), and `NM5NLQ6K50XZ01` is held.
- A same-day run therefore exercises exactly the fixed path.
- The ~13h fresh-day wait discriminates nothing that path needs and has no Andrew word behind it. CLAUDE.md: "waiting for the
  scheduled run is the same failure".
**`aa-2` runs today, after `aa-3` lands** (the two WORLD acts do not overlap).
- It is the CACHED-path positive arm for FWD-7 and FWD-3.
- The LIVE-path arm follows the `Z-W76-S1` fix (a live wsj job records only a `stop_bound` span) in round 29.
- `aa-2`'s pair names which path it grades, and it does not claim the live path.
