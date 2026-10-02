# AMGT_HARVST ROUND 36 -- L8 COMPILE, MID-ROUND (the bbg drain; ai-5's fallback re-opens Z-S58)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~05:45Z
**Input:** the channel compile (spine L8: new investigation rows). Watermark in: v45, 2026-10-01T19:55Z. Rows past it at
CLOUD @`7463a1fcd4` (after `2.0.0_SA_COO~H`'s drain of `wk-AMGT_HARVST-92-r36c`): **9 of 252**. No round-36 drain-end
packet exists yet. Ask: `1.0.0_SA_CTO~Z` msg 28229.
**L7 re-measured (LAST `<status>` tag):** ai-1 `complete`, ai-3 `complete`, ai-2 `open`, ai-4 `open`, ai-5 `open`.

---

## 1. RE-READ BY THIS SEAT

- **Live bbg outbox** (`.runtime/opal-data-harvest-bbg/progress.sqlite3`, opened read-only):
  - 05:36:03Z: `uploaded` 563; `pending` 267 = 266 coded `JSONDecodeError` + 1 `SilverRowError`; 266 of 267 due now.
  - 05:38:16Z: `uploaded` 564.
  - Since S58's 05:16:31Z read of 542: 22 rows in ~22 min. The 266 `JSONDecodeError` codes are stale, left over from
    attempts made before ai-4.
- **S57's disarm is real on the data plane.** ai-4's fix `a7de5e41a5` is an ancestor of HEAD, and bbg `uploaded` went
  from 0 (S57, 23:2xZ) to 564.
- **ai-5 as built.** The worker ~90's change in `wk-hvst-r36-90` is uncommitted: `uploads.py` mtime 05:28Z, test file
  05:30Z. It adds `_land(source, items, run_stamp)`. On a batch `SilverRowError` with `len(items) > 1`, it calls
  `_land(source, [it], it["run_stamp"])` for EVERY item of that source, and each of those calls is a full
  `silver_latest` read (`lib/research/harvest/store.py:431`, :373-396). This matches face step 2 exactly.
- **The one W91-S19 row:** `bbg:TD7VMGKGCTIZ00` is `pending`, attempts 11, `retry_at` **2026-10-02T06:36:56Z**. The
  backoff is capped at 3600 s (`uploads.py:226`), so the row comes due once an hour, indefinitely.
- **Partial batch write is safe.** `store.py:453-472` builds and PUTs one date partition at a time, so a type conflict in
  a later date raises after an earlier date's part has landed. The per-row fallback then re-offers those rows, and
  `_unchanged` (:439) skips them, so no row is duplicated. Correctness holds; only the cost is at issue (section 2).

## 2. FINDING -- `Z-C-S57`, BLOCKING, ARMED (disarm owner `2.0.0_SA_COO~H`)

ai-5 disarms Z-S58 only on a pass that does NOT contain a type-conflict row. Any batched bbg pass that runs after
06:36:56Z (and after each hourly re-due of `TD7VMGKGCTIZ00`) contains that row. The batch then raises
`SilverRowError`, and step 2 falls back to one `silver_append` per row for the WHOLE source: 266 full prefix reads,
which is the O(n^2) drain S58 measured. Plant (iii) proves that the good rows LAND. It does not measure how many
prefix reads the fallback costs, and plant (ii) covers only a clean batch. So AC1 can pass while the live drain stays
as slow as today.

The disarm is the issuer's (the issuer may amend its own criteria; CLAUDE.md rule 27 L5/L6). Any one of these works:
(a) run the post-merge drain pass before 06:36:56Z; or
(b) isolate the failing row WITHOUT a prefix read before re-batching the rest. `pa.Table.from_pylist` per row is local
and cheap. Grade it with a plant: a batch of N holding one type-conflict row makes at most 2 `silver_latest` calls.
Separately, the per-row pass running since ~05:08Z (cap 291) is still draining the same outbox. The issuer stops it
before the batched pass starts, so the two do not offer the same rows at once.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W90-S10` | **DISMISSED_WITH_REASON** | the worker's AC2 ran over the main `.runtime` through a temporary junction, removed after use (the row records the main runtime intact); ai-1 reads `complete` on its issuer flip |
| `Z-W91-S18` | **GRADUATED** | for the round-36 analysis: `runtimes.json` puts the LIVE sa runtime in a worker worktree (`C:/Users/Opal Bloomberg/Desktop/wk-hvst-r32-92/.runtime/opal-data-harvest`), and `barrons` has no key. Removing that worktree (the disk `/cleanup`) deletes a live runtime; COO~H kept it at 03:2xZ by judgment, not by any mechanism |
| `Z-S56` | **CARRIED** | ai-2 stays open: attempt 3 records `AC1 PASS 16/16, AC2 FAIL span 72 of 120 min` (`4809b48fca`); CTO r35 ruling 4 asks for 120 |
| `Z-S57` | **REMEDIATED** | ai-4 on HEAD; bbg uploaded 0 -> 564 |
| `Z-W91-S19` | **CARRIED**, ARMED | the single stranded row; it is now also the trigger of `Z-C-S57` |
| `Z-S58` | **CARRIED**, ARMED | disarm is conditional on `Z-C-S57`, not on ai-5's merge alone |
| `Z-W92-S15` | **DISMISSED_WITH_REASON** | fixed on the branch (`OPAL_HARVEST_PROFILE_ROOT`, 2 plants), now on HEAD |
| `Z-W92-S16` | **DISMISSED_WITH_REASON** | fixed (seed retries per cookie, keeps `seed_refused`, 2 plants); the relaunched job then held the session ~48 min |
| `Z-W92-S17` | **GRADUATED** | the 02:38Z sign-in ran under Andrew's 02:2xZ "ill look at it personally"; it is a human-hand sign-in and never limb-2 evidence, and the row says the page state cannot tell a click from a pass |

## 4. L10 PRECONDITION -- NOT MET

1. Every task order terminal: 2 of 5 (ai-2, ai-4, ai-5 open). **NOT MET**
2. Every BLOCKING or ARMED row dispositioned: yes above, but three stay ARMED (W91-S19, S58, C-S57). **NOT MET until
   disarmed**
3. Judgment criteria graded: 0 in round 36. **MET (vacuous)**

## 5. WHAT YOU SHOULD HAVE ASKED BUT DID NOT

Gold #4's bound is "after the drain, else from 10:00Z without it". On the measured ~1 row/min, the per-row pass alone
leaves about 266 rows to ~10:00Z at best. The rate falls as parts accumulate (S58), so it is likely later than that.
The 10:00Z fallback is therefore the likely branch unless `Z-C-S57` is disarmed before ai-5's drain. Nothing records
which bbg articles gold #4 will carry; the issuer's AC2 for ai-5 is the one place to print that count.

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S56",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T05:45:00Z",
    "one_line": "L8 round 36 mid-round compile: 9 rows past the v45 watermark at CLOUD @7463a1fcd4; S57 REMEDIATED (bbg uploaded 0 -> 564 on ai-4 a7de5e41a5); W91-S19 and S58 stay ARMED; the live sa runtime sits in worker worktree wk-hvst-r32-92 (runtimes.json), so removing it deletes a live runtime; L10 precondition NOT MET (ai-2, ai-4, ai-5 open).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: ai-1, ai-3 complete; ai-2, ai-4, ai-5 open (LAST <status> tag).",
        ".runtime/opal-data-harvest-bbg/progress.sqlite3 read-only 05:36:03Z: uploaded 563, pending JSONDecodeError 266, pending SilverRowError 1; 05:38:16Z uploaded 564.",
        "git merge-base --is-ancestor a7de5e41a5 HEAD -> true (HEAD 7463a1fcd4).",
        ".runtime/harvest-backfill/runtimes.json: sa = C:/Users/Opal Bloomberg/Desktop/wk-hvst-r32-92/.runtime/opal-data-harvest; no barrons key.",
        "wk-AMGT_HARVST-92-r36c @4809b48fca subject: HVST-ai-2 attempt 3 AC1 PASS 16/16, AC2 FAIL span 72 of 120 min."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W90-S10",
      "AMGT_HARVST-Z-W91-S18",
      "AMGT_HARVST-Z-S56",
      "AMGT_HARVST-Z-S57",
      "AMGT_HARVST-Z-W92-S15",
      "AMGT_HARVST-Z-W92-S16",
      "AMGT_HARVST-Z-W92-S17"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Round 36 rows past the v45 watermark are dispositioned at L8; S57's disarm is ai-4's HTML branch.",
    "world_is": "Seven rows dispositioned as in section 3; S57 disarmed on the data plane; W91-S19 and S58 carried ARMED (see Z-C-S57).",
    "notes": "FOR THE ROUND-36 ANALYSIS: the live sa runtime in a worker worktree is held by judgment, not by a mechanism; W92-S17's sign-in is human-hand and never limb-2 evidence."
  },
  {
    "id": "AMGT_HARVST-Z-C-S57",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T05:45:00Z",
    "one_line": "ai-5's per-row fallback re-opens Z-S58: any batched bbg pass that contains bbg:TD7VMGKGCTIZ00 (pending SilverRowError, due hourly, next 06:36:56Z) raises SilverRowError and falls back to one silver_append, so one full silver prefix read, per row for all ~266 rows, the same O(n^2) drain; plant (iii) proves the good rows land, not what the fallback costs.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~H",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "wk-hvst-r36-90 uncommitted diff of lib/opal_data_harvest/uploads.py: on SilverRowError with len(items) > 1, `for it in items: _land(source, [it], it[\"run_stamp\"])`.",
        "lib/research/harvest/store.py:431 silver_append -> silver_latest (:373-396 reads every part under the prefix).",
        "progress.sqlite3 read-only 05:37:30Z: bbg:TD7VMGKGCTIZ00 pending attempts 11 retry_at 1790923016.2 = 2026-10-02T06:36:56Z.",
        "lib/opal_data_harvest/uploads.py:226 retry_at = now + min(3600, 60 * 2 ** min(attempts, 6)).",
        "TO-HVST-ai-5 face step 2 and plants (ii)/(iii): (ii) measures a clean batch only; (iii) measures landing only."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-S58",
      "AMGT_HARVST-Z-W91-S19"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "ai-5 issuer notes: Row Z-S58 is disarmed at the merge; the bbg outbox drains in minutes.",
    "world_is": "Disarmed only for a pass with no type-conflict row. The one known such row is due hourly, so a batched drain after 06:36:56Z runs per row for the whole source.",
    "notes": "Disarm (issuer): run the drain pass before 06:36:56Z, or isolate the failing row with a local pa.Table.from_pylist probe before one re-batched call, graded by a plant (a batch of N with one type-conflict row makes at most 2 silver_latest calls). Stop the per-row pass running since ~05:08Z before the batched pass starts."
  }
]
```

-- 3.0.0_SA_CVO~Z
