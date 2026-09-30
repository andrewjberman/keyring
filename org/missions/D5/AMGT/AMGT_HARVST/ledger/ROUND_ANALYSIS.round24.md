# AMGT_HARVST -- ROUND 24 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~03:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26875, subject *"L10 slug AMGT_HARVST round 24 @7061f0fd82"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v33.md`. Issuer packet:
`deliverables/2.0.0_SA_COO_H/round24/ROUND24_DRAIN_END_PACKET.md` @`9a86a3c153`.

**Round 24 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED -- BUILT, NOT SERVED (CVO v33 section 2.1, AGREED)

- **`n-1` (FWD-1/3):** the collector keeps received bytes with `received-sha256`, links each article to its listing object,
  records rank and page for all five publishers, and writes a run record. The 126 existing objects are unchanged.
  - It runs only under `--harvest-grammar` (`Z-W56-S2`).
- **`n-2` (FWD-2):**
  - sa's missing fields go from 5 to 0, and the 6 unlabelled sa objects yield rows.
  - Query-by-company is the mention join: Lenovo 32 against 35, with AES, Barrick and Atlantic Power dropping out.
  - It waits on the `silver_latest` tie-break before the paired rebuild.
- **`n-3` (FWD-7):** the served rank holds 2 rows because 188 of 191 names have no legacy pool link. The gold branch resolves 0
  of 191.
- **`n-4` withdrawn** on this seat's ruling 1 (@5998e71f23). The CVO verified the world is unmoved: `CHATTER_AXIS_SOURCE=legacy`,
  LastModified 09-24.
- **`n-5` (FWD-9):** a plan of 23,859 listing pages over 191 names, Lenovo first. **952 of 955 page figures are the config
  default of 25**, and 3 are measured.
- **`n-6` (`/timeline/day`):**
  - Reading silver dominated 9 of 9 reps. The new path reads only the named publishers' columns, concurrently, with an
    ETag-keyed cache.
  - Bodies are byte-equal on 4 of 4 days, at 2.3x cold and 37-46x warm.
  - Not served; it awaits the scoped-API redeploy.

## 2. RULINGS

1. **`n-6` rides AMGT_RESAPP round 51's ONE build (cell 8) as a NAMED, NON-INERT rider**, not a second deploy of the same
   function.
   - `timeline_api.py` is served by `opal-amgt-scoped-api`, and one function takes one build per window.
   - The RESAPP pair's expected diff names `/timeline/day`'s latency moving and its bodies byte-equal. The executor re-runs
     `n-6`'s OLD == NEW body check on the deployed function.
   - Routed to 2.0.0_SA_COO~Z with this analysis.
2. **FWD-9's plan is a CEILING, labelled as one.**
   - A page count that is 952/955 config default is what the run is ALLOWED to ask for, not what it will ask for, because
     listings exhaust early. The plan's figures carry that claim (measured on 3, held on 952), and the run records actual
     pages per publisher per name.
   - The DONE WHEN's "printed before the run" is met by a labelled ceiling. FWD-9 grades on the run.
3. **FWD-9's run starts with Lenovo on the four live publishers (barrons, bbg, ft, wsj), under a never-widen pair:**
   - scripted vendor egress under R-21 (@b390c36444);
   - bronze and silver writes as the served act;
   - the sa leg waits on the renewal.
   The pair's expected diff is the plan's Lenovo rows. The acceptance is "every day from 2026-01-01 has a row" and "running it
   again adds nothing" (a second run, `fetched 0`). The other 190 names follow in the next round, on the Lenovo run's actual
   page counts.
4. **FWD-5 and FWD-6: PAGE HALF MET, not REALIZED.** This is this seat's standing rule from rounds 13-15: the page half counts
   when the page is on portal DEV as served.
   - Walk G (DSGN_AMGTV1 round 8, @2c63f69a09 ruling 4) ran on the 5174 build of site-Z portal DEV `29c8226a`.
   - This seat measured site-Z DEV as **30 commits ahead of and 15 behind `origin/DEV` (5c7eead8)**, so it is unpromoted and
     divergent.
   - Promotion is the integrator's merge and push, on Andrew's word (CLAUDE.md Portal), and is listed below.

## 3. FWD GRADES

| FWD | grade | since round 23 |
|---|---|---|
| 1 | NOT REALIZED | built (n-1). Served when the scheduled run passes the flag (round-24 ruling 2, round 25). |
| 2 | NOT REALIZED | built (n-2). Served at the paired silver rebuild after the tie-break. |
| 3 | NOT REALIZED | built (n-1). The same flag, then the same-day re-run with `fetched 0`. |
| 4 | REALIZED | standing |
| 5 | NOT REALIZED -- page half MET on local DEV, served half MET | promotion of portal DEV (ruling 4) |
| 6 | NOT REALIZED -- page half MET on local DEV (an opened event lists its rows), served half MET | promotion of portal DEV |
| 7 | NOT REALIZED | gold coverage (round-24 ruling 1) |
| 8 | REALIZED | standing |
| 9 | NOT REALIZED | plan printed as a ceiling; the Lenovo run under a pair (ruling 3) |

**2 of 9 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 25 in ONE issuance

| # | cell | FWD | risk | note |
|---|---|---|---|---|
| 1 | **`chatter_daily` coverage from run records** | 7 | LOCAL, then a served rebuild under a pair | Round-24 ruling 1. Prints the before and after coverage distribution and the gold branch's RESOLVED count. |
| 2 | **The scheduled run passes `--harvest-grammar`** | 1, 3 | WORLD, under a pair | Round-24 ruling 2. The flag and the pair land together, because the task runs the working tree. |
| 3 | **`silver_latest` tie-break on `run_stamp`** | 2 | LOCAL | Round-24 ruling 3. Two plants. |
| 4 | **The paired silver rebuild** | 2 | WORLD, under a pair | After cell 3. The expected diff names 5 superseded rows and 6 new ones. |
| 5 | **Lenovo's backfill on the four live publishers** | 9, then 3 | WORLD, under a pair plus R-21 scripted egress | Ruling 3. The second run reads `fetched 0`. |

**Fan-out:** 4 now (1, 2, 3 and 5); cell 4 follows 3.

**Routed, NOT cells:**
- `n-6`'s redeploy, into AMGT_RESAPP r51 cell 8 (ruling 1);
- the portal DEV promotion (below).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- **The portal DEV promotion** [CLAUDE.md Portal: "`0.0.0_AB_MSTR` pushes trunks on Andrew's word"].
  - Site-Z portal DEV `29c8226a` is 30 ahead of and 15 behind `origin/DEV` `5c7eead8`, and needs a merge and a push by the
    integrator.
  - It carries DSGN_AMGTV1 rounds 6-8's page work and HARVST FWD-5/6's page half.
- Renew Seeking Alpha [spend]. His word is given (@d0e74747a9). FWD-9's and FWD-1's sa legs.
- Remove the drained `wk-hvst-*` worktrees [recursive delete, CLAUDE.md Agent Autonomy]. His word to 2.0.0_SA_COO~X ("if all the
  content has been committed, then we do not need them anymore") was acted on for CRPS only, and is not widened here.

## Compiler Tools

- The CVO's v33: its `get-function-configuration` reads on both Lambdas.
- The packet's section-1 table (a close run of 12 of 12 at rc 0).
- This seat: in `portal/`, `git fetch origin DEV`; `git log --oneline origin/DEV..DEV | wc -l` = 30; `DEV..origin/DEV` = 15.
