# AMGT_HARVST -- ROUND 25 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~06:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26934, subject *"L10 slug AMGT_HARVST round 25 @190101cb31"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v34.md`. Issuer packet: `round25/ROUND25_DRAIN_END_PACKET.md` @`b635dadc66`.

**Round 25 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED -- the first SERVED writes since round 22

- **The CVO reconciled the served plane on S3** (every object since 04:39Z, per root):
  - `o-5` wrote **57 objects under `bloomberg/` and `wsj/` only** (bronze 27, silver 30), and 0 under ft, barrons or sa bronze;
  - `o-4` wrote exactly 3 sa silver parts;
  - no HARVST object landed outside the two named acts' roots.
  **Both pairs held on the output.**
- **`o-1`:** `chatter_daily` coverage from run records. It is built, and moves 0 of 5,730 name-days, because no span-bearing run
  record exists yet (`o-5` ran on pre-`o-1` code).
- **`o-2`:** `--harvest-grammar` in `run-local.ps1`. The task is confirmed Disabled with an empty `<Triggers>` by the XML.
  The CVO notes `@($_.Triggers).Count` reads 1 on an empty collection.
- **`o-3`:** the `silver_latest` tie-break.
- **`o-5` closed after two amendments.** Both cut-time misses (`jobs_per_run: 1`; the outbox in front of `upload-harvest`)
  graduated.

## 2. RULINGS

1. **THE ISSUER'S PROCESS FIX IS AGREED, AND IT BINDS THIS SEAT'S HALVES TOO.**
   - Both `o-5` misses passed this seat's CTO half as well: it re-measured the roots and never traced argv to the config
     defaults or the actual put call.
   - **From now on, a CTO half on a producer's WORLD act names the command that reaches the put, reads the config defaults the
     argv leaves unset, and cites a stub-client put-count dry run.** One read catches both classes.
   - This is recorded here as this seat's own discipline. It is not a new gate on any other seat.
2. **The check template: the base commit is pinned at cut, never derived from HEAD** (CVO v34 section 2). A check whose base is
   `merge-base HEAD CLOUD` cannot pass after its own drain. This goes to 2.0.0_SA_COO~H's check template.
3. **FWD-3's two owed rows** (the `o-5` CTO half, AMENDMENT 2) become round 26 cell 2:
   - `bbg:NM5NLQ6K50XZ01`, fetched and never stored;
   - the wsj URL/UUID key split.
4. **FWD-9's reach is one name and two publishers.** bbg reaches the 2026-01-01 floor for Lenovo (273 of 273 days); wsj spans
   8 days. ft was `request_rejected`, barrons was challenged, and sa waits on the renewal.
   - **Before widening past Lenovo, round 26 reads WHY ft and barrons refuse**, a LOCAL read of the collector's request path and
     its challenge handling, with no request sent.
   - Widening to 190 names on two working publishers would be a large vendor act for half an outcome.

## 3. FWD GRADES

| FWD | grade | what moved |
|---|---|---|
| 1 | NOT REALIZED | Received bytes are stored for bbg and wsj (the Lenovo run). ft and barrons refused, and sa is pending: "each of the five publishers" is 2 of 5. |
| 2 | NOT REALIZED | sa silver is rebuilt (3 parts). The company query needs the mention rebuild (round 26). |
| 3 | NOT REALIZED | Rank, page and run records are live for bbg/wsj, and the repeat fetched no held article. Two rows are owed (ruling 3). |
| 4 | REALIZED | standing |
| 5 / 6 | NOT REALIZED, page half MET on local DEV | the portal promotion (Andrew) |
| 7 | NOT REALIZED | coverage is built, 0 of 5,730 moved; it needs a span-bearing run record |
| 8 | REALIZED | standing |
| 9 | NOT REALIZED | one name, one publisher at the floor |

**2 of 9 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 26 in ONE issuance

| # | cell | FWD | risk | note |
|---|---|---|---|---|
| 1 | **The mention rebuild** over the rebuilt sa silver and the Lenovo rows | 2, then 4 and 7 inputs | WORLD, under a pair | It gives the new rows `mention_count` and backs the company query by the mention join. `Z-W53-S3`/`S4` graduate on it. Per ruling 1, the half names the command that reaches the put, the config defaults, and a stub put-count. |
| 2 | **FWD-3's two rows answered** (the never-stored fetch; the wsj key split) | 3 | LOCAL | Each is a cause plus a fix or an accepted limit. A silent loss on the collection path is fixed, not accepted. |
| 3 | **A span-bearing run record:** one Lenovo bbg/wsj collection run on current (post-`o-1`) code, then the `chatter_daily` coverage rebuild | 7 | WORLD, under a pair plus R-21 scripted egress | The expected diff is the coverage marks for Lenovo's searched days moving from DENIED to SEARCHED, and the gold branch's RESOLVED count leaving 0 for Lenovo. It is the positive arm for FWD-7's gradable pair. |
| 4 | **Why ft and barrons refuse:** a LOCAL read of the collector's request path, headers and challenge handling, and of the signed-in browser session path (R-21 call 1) | 1, 9 | LOCAL, with no request sent | The output is the cause and the smallest route to a clean fetch, or a stated limit. |

**Fan-out:** 4, independent. Cell 3's gold step follows its own run.

**NOT cells:**
- the backfill of the other 190 names (ruling 4);
- the gold flip (it waits on cell 3's evidence);
- the schedule (Andrew's).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Re-arm the harvest schedule [`ledger/HANDOFF_L4_TO_L5_COO_Y_20260922.md:81`].
- Renew Seeking Alpha [spend]. His word is given.
- The portal DEV merge and push [CLAUDE.md Portal] (FWD-5/6).

## Compiler Tools

- The CVO's v34: its per-root S3 listing since 04:39Z, and its `Export-ScheduledTask` XML read.
- The packet's section 3 (the FWD notes).
- This seat's own `o-5` CTO half and its two amendments (the misses it did not catch).
