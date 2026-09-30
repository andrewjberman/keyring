# AMGT_HARVST -- ROUND 26 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~08:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27027, *"L10 slug AMGT_HARVST round 26 @8183d770e8"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v35.md` (read to EOF, 5,551 B). Issuer packet: `round26/ROUND26_DRAIN_END_PACKET.md`
@`f48aa8fe6e`.

**Round 26 is CLOSED:** 4 of 4 orders terminal, every BLOCKING or ARMED row dispositioned, 0 judgment criteria. **The project is
NOT closed.** The PRD moves to v0.4 in this commit: two CONTRACTS are added, `C-HV-RANK-DECLARED-SET` and `C-HV-COVERED-VS-FOUND`.

---

## 1. WHAT THE ROUND DELIVERED (the CVO re-read both WORLD acts on S3 and on the deployed route)

- **`p-1`, the mention rebuild:**
  - 358 rows; 304 of 304 prior rows are byte-identical and 54 are new (sa 6, wsj 48);
  - `mention_count` is null on 0 of 358;
  - Lenovo goes from 32 to 43 pairs;
  - the deployed `/timeline/day` serves a new wsj article with its `mention_count`.
  - **bbg adds 0**, because `o-5`'s 11 bbg rows are empty in silver (`Z-S44`).
- **`p-2`:** FWD-3's two owed rows are answered in code (12 tests, 5 mutants).
  - The run record now names each fetched key's outcome: stored, rejected or not stored.
  - It also carries `keys_stored_join` for the wsj URL/UUID split.
- **`p-3(a)`, the `chatter_daily` rebuild:**
  - 52,143 rows, at the signed digest;
  - Lenovo is 273 of 273 days PARTIAL (previously DENIED);
  - 43 `articles_total` rows moved.
  - This seat's condition 3 was the served-route read, and it held.
- **`p-4`:** why ft and barrons refuse, with no request sent.
  - **barrons:** the session was logged out, reauth met a DataDome 401, and `worker.py:393` refuses the repair after a same-job
    reauth.
  - **ft:** a 403 whose body is never kept, so its cause cannot be separated.

## 2. RULINGS

1. **THE CVO'S QUALIFIER STANDS, AND IT CORRECTS THE PACKET'S SENTENCE.**
   - The packet reads *"serves `[bbg, wsj]`"*. The CVO measured `[bbg, wsj]` on **8 of 273 days** and `[bbg]` on the other 265.
     The packet's sentence was true of the set's union, never of the series.
   - This seat's `p-3(a)` half predicted "PARTIAL with its publisher codes" and did not predict which codes. So the half is
     unaffected, and the grade below uses the CVO's count.
2. **WHAT `publishers_covered_codes` MEANS** (the CVO's section 3 item 3) is now a contract, `C-HV-COVERED-VS-FOUND` (PRD v0.4).
   - **COVERED = the publisher's listing for that name ran over that day. FOUND = the publisher's articles are served that day,
     by any path.**
   - On 2026-02-12, covered=`[bbg]` with sa and wsj articles is coherent under that meaning. What is missing is the FOUND set,
     so the page cannot tell "found, listing not run" from "not searched".
   - **Coverage marks and FWD-7 eligibility read COVERED only; a found-only article is served and never scored.** Otherwise one
     incidental wsj hit would make a day SEARCHED and a name eligible.
   - DSGN_AMGTV1 round-11 order `n-3` (a not-searched day says how its articles were found) renders the page half. This project
     serves the field.
3. **FWD-7's denominator is now a contract, `C-HV-RANK-DECLARED-SET`** (PRD v0.4), from the ruling @`ddcc71fd2d`.
   - One line is ADDED at the landing: **the score counts only the declared set's articles.** It follows from rulings 2 and 3
     together.
   - This is a CONTRACTS change, so the ratified half re-opens to `3.0.0_SA_CVO~Z`. Under R-10 it is reviewed, not held.
4. **`Z-S44` (bbg silver empty) is repaired BEFORE any further bbg silver read is graded.** It explains why FWD-2 shows bbg
   adding 0.
   - The repair is a LOCAL build graded on the 11 held bbg bronze objects, read-only.
   - The silver rebuild from bronze is a WORLD act. It goes to round 28 under its own pair, after the round-27 run adds more bbg
     bronze, so one rebuild covers both.
5. **barrons B2 (the `worker.py:393` guard edit) and ft F1 (keep the 403 body) are LOCAL code cells.** Their runs need a
   signed-in session (barrons) or credentials (ft F2), and both are Andrew's under R-21 call 1. The egress itself is granted by
   R-21. The cell is the code. (Corrected same day; see section 5.)
6. **`p-3(b)`'s CTO half is signed at the cut, not now.**
   - Its COO half @`dadba8badd` was signed on the round-26 code.
   - This seat re-measures the snapshot and checks that the code at the act equals the code at signing. Round-27 cells 4 and 5
     change `chatter_axis`, `generation_writer.py` and the daily builder.
   - **So cell 1 runs and drains BEFORE cells 4, 5 and 7 merge.** That is dependency order, as in the CORPUS round-22 ruling 1.

## 3. FWD GRADES

| FWD | grade | what moved |
|---|---|---|
| 1 | NOT REALIZED | 2 of 5 publishers. The ft and barrons causes are read (`p-4`); both fixes are round-27 code, and both runs are Andrew's. |
| 2 | NOT REALIZED | sa and wsj mention rows, and the company query by the mention join, are served. bbg is empty in silver (`Z-S44`), so "every field ... rebuilt from the stored original" fails for bbg. |
| 3 | NOT REALIZED | Both owed rows are answered in CODE. The per-key outcome and `keys_stored_join` are exercised only by a run on the new code: round-27 cell 1. |
| 4 | REALIZED | standing |
| 5 / 6 | NOT REALIZED, page half MET on local DEV | the portal promotion (Andrew) |
| 7 | NOT REALIZED | Coverage moved DENIED -> PARTIAL on 271 Lenovo days, and 8 of 273 days are covered by two publishers. The rank rule is now contract. Its code and flip are in round 27. |
| 8 | REALIZED | standing |
| 9 | NOT REALIZED | one name at the floor for bbg, 8 days for wsj |

**2 of 9 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 27 in ONE issuance

| # | cell | FWD | risk | note |
|---|---|---|---|---|
| 1 | **`p-3(b)`**: the span-bearing Lenovo bbg/wsj run, its upload, and the `chatter_daily` rebuild over the persisted run record | 7, 3 | WORLD, pair (COO half @`dadba8badd`; this seat's half at the cut) + R-21 scripted egress | **Runs and drains FIRST** (ruling 6). It also exercises FWD-3's per-key outcomes and `keys_stored_join` on a real run. |
| 2 | **`Z-S44`**: bbg as-received parses into silver | 2 | LOCAL | The AC reads the 11 held bbg bronze objects and parses each one non-empty, read-only. No silver write this round (ruling 4). |
| 3 | **FWD-7 eligibility census** under the declared set (bbg, wsj) | 7 | LOCAL read | It prints eligible of 191 over the window, with the excluded names by reason, **COVERED set only**. Run it after cell 1 drains, so it counts the new coverage. |
| 4 | **`C-HV-RANK-DECLARED-SET` in code**: `chatter_axis` eligibility before no-signal, the declared set, declared-set-only scoring, the floor HOLD, and the population through `generation_writer.py` | 7 | LOCAL build | The AC plants an unsearched name and shows it EXCLUDED, not quiet. A second plant, a found-only article, is served and not scored. |
| 5 | **`C-HV-COVERED-VS-FOUND` in code**: the daily builder emits `publishers_found_codes`, and the timeline route serves it | 3, 5 | LOCAL build | The AC reads 2026-02-12 from a local build over the current gold inputs: covered `[bbg]`, found `[sa, wsj]`. The rebuild that serves it rides cell 7's pair or round 28's. |
| 6 | **barrons B2 + ft F1**: the guard edit at `worker.py:393`; the 403 body kept | 1, 9 | LOCAL, with no request sent | Tests only. The runs are Andrew's. |
| 7 | **The `gold` flip** (`CHATTER_AXIS_SOURCE`), re-cut on cells 3-4 | 7 | WORLD, under a pair | The expected diff comes from cell 3's population. **If cell 3 prints fewer than 10 eligible names, the flip's expected outcome is a HOLD with its `empty_reason`**, and the pair says so for both branches. |

**Fan-out:**
- 1 first.
- 2, 4, 5 and 6 are independent, and each merges after 1 drains.
- 3 follows 1.
- 7 follows 3 and 4.

**NOT cells:**
- the 190-name backfill, until FWD-1 reaches more than two publishers;
- the bbg silver rebuild (round 28);
- the schedule (Andrew's).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Re-arm the harvest schedule [`ledger/HANDOFF_L4_TO_L5_COO_Y_20260922.md:81`].
- The barrons run B1 (the `p-4` packet: the saved session is logged out, and B1 is a run on his word) and the ft credential
  re-harvest F2 [R-21 @`b390c36444`
  call 1: *"a signed-in admin+Dev browser, or he runs the readout. NOT credentials."*]. **CORRECTION (same day):** this line first
  cited `C-HV-EGRESS`'s per-use word. That is wrong: R-21 already grants scripted vendor egress. What stays his is the sign-in and
  the credentials, never the call.
- The portal DEV merge and push [CLAUDE.md Portal] (FWD-5/6).
- Remove the drained worktrees `wk-hvst-r24..r26` [CLAUDE.md Agent Autonomy: recursive deletion].

## Compiler Tools

- The CVO's v35: its S3 re-reads, the Lambda invoke of `/timeline` (the 8-of-273 count), and the `Export-ScheduledTask` read.
- The packet's section 2.
- This seat's `p-3(a)` half, section 1.
- The FWD-7 ruling @`ddcc71fd2d`.

This seat ran no new instrument for the analysis: every number above is the CVO's or the packet's, each cited.

## AMENDMENT 1 -- cell 7 (the `gold` flip) WITHDRAWN from round 27 (2026-09-30 ~09:0xZ, msg 27056)

- **Measured by the issuer:** `q-4`'s gold branch (declared bbg+wsj, as-of 09-30) puts **0 of 191** names in the eligible
  population: NOT_SEARCHED 190, PARTIAL 1. The result is HOLD `BELOW_ELIGIBLE_FLOOR`.
- **`q-1` was withdrawn.** bbg refused; wsj's cached listings recorded no span; the reach gap goes to round 28.
- **RULED (driver, on the issuer's REC): WITHDRAW `q-7` this round.**
  - A flip whose only reachable outcome is HOLD changes no served rank.
  - It would stop the legacy rank refreshing, leaving the last generation served behind a HOLD marker. That is a freshness loss
    for no gain.
  - `q-7` is re-cut when an eligibility census reads at least 10 eligible names (`C-HV-RANK-DECLARED-SET`'s floor).
- **What this says about FWD-7:** the binding constraint is now COLLECTION REACH (FWD-1 and FWD-9), not the rank rule.
- **Also carried to the round-27 analysis:** why bbg refused a run that `o-5` completed on the same name.
