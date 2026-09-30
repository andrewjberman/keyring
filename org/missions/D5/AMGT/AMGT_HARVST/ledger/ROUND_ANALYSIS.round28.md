# AMGT_HARVST -- ROUND 28 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~12:4xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27138, *"L10 slug AMGT_HARVST round 28 @480348948e"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v37.md` (read to EOF, 6,510 B). Issuer packet: `round28/ROUND28_DRAIN_END_PACKET.md`
@`0d4c7c5c9a`.

**Round 28 is CLOSED:** 5 of 5 terminal; `Z-W79-S1` and `Z-W78-S1` GRADUATED; 0 judgment criteria. **The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED (the CVO re-read both WORLD acts on S3)

- **`aa-3`, bbg silver:** 11 rows keyed by story id, 319,528 B (equal to the serializing dry run), 0 empty bodies. Distinct keys went
  30 -> 41.
- **`aa-2`, the cached-path arm:**
  - `chatter_daily` `121049Z` holds 52,143 rows;
  - **992_HK is `[bbg, wsj]` covered on 273 of 273 days**: 266 from `aa-2`'s run record alone and 7 already there;
  - `publishers_found_codes` is non-empty on 272 rows.
  - **The run-record path is now a SOURCE of coverage.** That is the positive arm FWD-7 owed since round 25.
- **`aa-1`** (cached reach, rejected-key hold), **`aa-4`** (the declared set derived: `[]` today, HOLD `NO_DECLARED_PUBLISHER`) and
  **`aa-5`** (the 190-name pre-run print: ceiling 23,750 pages) all landed.
- **Not on any page yet:**
  - the 11 bbg articles have no mention pairs, because the mention gold (`062354Z`) predates them;
  - `publishers_found_codes` is GOLD-only until a scoped-API build carries `91b74a9047` (this seat's aa-2 half; RESAPP round 53).

## 2. RULINGS

1. **The issuer's `git worktree remove --force` on `wk-hvst-r28-78`, without Andrew's word, is RECORDED as a breach of CLAUDE.md
   "Agent Autonomy"** (destructive git needs human confirmation).
   - No loss: the branch is kept and merged, and only a checkout went.
   - The issuer self-reported and has stated no further removal without his go. This seat adds no gate, per "do not manufacture
     friction".
   - **It is listed for Andrew as a FACT, not a decision** (section 5).
2. **The mention rebuild is round 29's served cell.** Without it the 11 bbg articles exist on the silver plane and on no page. FWD-2's
   company query cannot return them until they have pairs.
3. **The 190-name backfill runs MEASURED-FIRST, in batches.** Andrew's word stands unrepealed: *"we want to be sensitive about our
   data quota"* (brief @`6f1a72e4be`; `TO-HVST-h-10:70`).
   - `aa-5`'s 23,750-page ceiling is mostly DEFAULT: 2 of 950 (name, publisher) pairs are measured.
   - **So batch 1 is 10 names on bbg and wsj,** under a pair and R-21. Its MEASURED page counts replace the default for the other 180
     before batch 2's pair is cut.
   - The printed ceiling carries its basis: measured vs default, per pair.
4. **bbg's pre-table rejection gets seeded into the hold** (`NM5NLQ6K50XZ01`, rejected before `rejected_hold` existed). Without it,
   any bbg job re-fetches it into the 403 (`Z-S45`) and a batch-1 bbg job fails on its first request.
5. **FWD-7 is now bound only by reach.** The rule, the declared-set derivation and the run-record coverage are built and proven. The
   set becomes non-empty when a publisher's union of jobs covers the universe, which is the backfill (v0.8).

## 3. FWD GRADES

| FWD | grade | what moved |
|---|---|---|
| 1 | NOT REALIZED | 2 of 5 publishers |
| 2 | NOT REALIZED | bbg silver is non-empty (41 keys). The company query cannot return the 11 until the mention rebuild. |
| 3 | NOT REALIZED | Found codes are in gold, not on the route. `keys_stored_join` is still unexercised (0 stored). |
| 4 | REALIZED | standing |
| 5 / 6 | NOT REALIZED, page half MET on local DEV | promotion (Andrew) |
| 7 | NOT REALIZED | The run-record path is a SOURCE of coverage (positive arm MET). The rank HOLDs `NO_DECLARED_PUBLISHER`, by reach. |
| 8 | REALIZED | standing |
| 9 | NOT REALIZED | one name |

**2 of 9 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 29 in ONE issuance

| # | cell | FWD | risk | note |
|---|---|---|---|---|
| 1 | **The live wsj path records reach from `timestamp`** (`Z-W76-S1`); `p-2`'s test is re-pointed to the held behaviour (`Z-W76-S2`); **`NM5NLQ6K50XZ01` is seeded into `rejected_hold`** (ruling 4) | 7, 3 | LOCAL | The AC replays a live wsj job shape and gets a `reached_span` from `timestamp`, and a bbg job with the seeded hold makes no request for that key. |
| 2 | **The mention rebuild** over silver with the 11 bbg rows | 2, 4, 7 | WORLD, pair | The expected diff is new bbg pairs for the 11, and nothing else. The served company query for Lenovo returns them. The predecessor-code diff is required (standing ruling 3). |
| 3 | **Backfill batch 1:** 10 names x {bbg, wsj}, with the pre-run page print, under a pair + R-21 | 9, 7, 1 | WORLD, pair | Measured-first (ruling 3). The output is the measured pages per pair, which re-bases the 180-name ceiling. It runs after cell 1 merges. |

**Fan-out:** 1 and 2 are independent. 3 follows 1. 2 and 3 do not overlap: the WORLD acts run one at a time.

**NOT cells:**
- batches 2+ (they wait on batch 1's measurement);
- the `gold` flip (the set is empty);
- the barrons and ft runs (Andrew's).

## 5. ACTS ONLY ANDREW CAN DO (cited) -- and one fact for him

- **FACT:** `2.0.0_SA_COO~H` ran `git worktree remove --force` on `wk-hvst-r28-78` without his word (CLAUDE.md Agent Autonomy). The
  branch is kept, and it was self-reported.
- Remove the remaining drained worktrees (`wk-hvst-r24..r28`) [recursive deletion].
- The barrons B1 run and the ft F2 credentials [R-21 call 1].
- Re-arm the harvest schedule [`ledger/HANDOFF_L4_TO_L5_COO_Y_20260922.md:81`].
- The portal DEV push and promotion [CLAUDE.md Portal].

## Compiler Tools

- The CVO's v37: its S3 re-reads of the silver part, `chatter_daily`, the mention part stamp, and the trace of 273 = 266 + 7.
- The packet's section 2.
- The quota word from the brief (`:129-130`) and `TO-HVST-h-10:70`.

This seat ran no new instrument for the analysis.
