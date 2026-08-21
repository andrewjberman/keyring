# 0.4.0_DS_ClientPlatform — ETFS_POSITIONING TO-1: the projection producer (a MINT, two stages) + the `sub_asset_class` vocabulary act (2026-08-21 20:05–21:05Z)

**Serial:** `0.4.0_DS_ClientPlatform` (base, PID 1624) | **Archetype:** BUILD
**TO:** `ETFS_POSITIONING.TO-1` — cells `ETFS-d-1` (producer) + `ETFS-d-2` (vocabulary)
**Priority:** P1 SESSION PRIORITY, Andrew-direct: *"I want ETFS_POSITIONING DONE RIGHT NOW"*
**Scope:** Andrew's four DS clauses bind — TO-1 is the qualification, everything else at this seat held.

---

## What happened (ordered)

1. **Startup.** `/watcher`: not registered (fresh seat, no live peer, no orphan — `ps` found nothing),
   registered LIVE, persistent inbox Monitor armed (task `bl33zxoin`). It immediately drained 5
   queued messages plus 4 more during the session; all read and acted on.

2. **SPEC-AT-PICKUP first, before any build** — the TO's required first act. All four oracles run
   live, **4/4 premises hold**; COO accepted (65717).
   - O-1 producer is a MINT: `find data/etfs/scripts -name "*position*"` **EMPTY** over 9 py files.
   - O-2 weights are ours: `silver/holdings/` through 2026-08-20.
   - O-3 **the one that could have moved AC5**: `bbg/` carries **ONE** date prefix. AC5 stays pending
     its observed anchor. I declined to quote `s3 ls` local timestamps as UTC.
   - O-4 universe runtime-read, confirmed at source (the config's own description says so).

3. **Data plane profiled before designing anything.** 114 holdings rows (PFDE 90 / PFOE 24, DIVZ 0 /
   IDVZ 0), 4 netassets rows covering all four books, 109 characteristics rows = 105 constituents + 4
   fund rows. **The 4x105 `field_exceptions` are a GRAIN SPLIT** — 105 constituents correctly lacking
   FUND-level fields — exactly as I warned pre-pickup; counting them as defects manufactures a phantom.

4. **`ETFS-d-2` — the vocabulary act, and it changed shape mid-cell.** I came expecting to MINT an
   enum. **Build-ladder rung 2 fired and the answer became ADOPTION: 12/12 values already exist
   in-estate.** The 11 GICS sectors are already spelled in `portal/src/lib/dataLoader.ts:236`
   `SECTOR_INDICES` **byte-identically to Bloomberg's `GICS_SECTOR_NAME`** (so the producer needs no
   mapping table at all) and byte-identically to the existing `SECTOR_COLORS` map (so a misspelling
   would render colorless — a live, checkable consequence). `Cash & Cash Equivalents` is named in
   **this project's own PRD s.2.5:147**. Full four-postulate record + `-i` census + `comp-estate
   --definitions` check in the deliverable.

5. **`ETFS-d-1` — the producer, built as TWO STAGES** per Amendment A / Rule 17b as amended.
   `etf_positioning_gold.py` ((a) plane → gold parquet) and `etf_positioning_publisher.py` (gold
   parquet → platinum JSON). The publisher holds no grant to any input; the gold stage holds no grant
   to the serve. **One-producer-per-served-key therefore holds by construction, not by discipline.**
   The legacy `json/`-landing single-script shape was deliberately not built.

6. **Exercised, not merely coded.** 23/23 assertions PASS. AC3's sharpest test binds: **ONE
   UNMODIFIED `build_tables`** yields shells from rows-absent and full books from rows-present — no
   ticker is named anywhere in the producer, so there is no edit to make when TrueShares rows land.

7. **Committed** @`71265d372e` (4 files, 1,548 insertions), commit-gate clean, risk-reflex CLEAN over
   1,813 danger nodes. **Push state READ, not predicted: 0 remote branches contain it — LOCAL, rides
   MSTR's integration push.**

8. **Proof-of-spec instance VALID, rc=0** (checked the rc, never the output string — the usage banner
   contains both verdicts' vocabulary).

---

## Two things I got wrong in-session, and what caught them

**(1) A census that could not have said otherwise.** My first token-census pass piped `comp-find`
through `grep -c "^"` and returned **7 for all twelve tokens**. I was counting the tool's own frame
lines, not its hits. **Identical counts across twelve different tokens is an instrument that could not
have said otherwise** — the tell was in the output, not in the method. Fixed by reading `comp-find`'s
own `DENOMINATOR:` line, which is the frame it prints for exactly this reason. Recorded in the
deliverable rather than quietly corrected.

**(2) An empty diff that was empty by construction.** Checking whether the spec had moved under me, I
ran `git diff HEAD origin/CLOUD` on the TO/contract paths and got nothing — but `rev-list
HEAD..origin/CLOUD` was **0**, meaning origin was an *ancestor*, so that diff was empty **by
construction** and carried no information. The informative question was `cc7eca2da3..HEAD`. Re-ran it:
the contract HAD moved (v1.1 @`f93b4571d1`), and v1.1's own changelog says the change is the
edge-version pin and is "nothing a consumer builds against" — key, B-form shape, `holdings_status` and
the vocabulary hand-off all unchanged. **I re-read rather than assumed, as I told COO I would.**

## The MECE hunt found a real uncovered member

`2602335D` (TPG Inc) — 1 of 106 unique non-cash tickers, no characteristics row, no GICS sector. It
emits `sub_asset_class: null` and is **COUNTED** into the manifest (`sub_asset_class_unmapped: 1`)
rather than bucketed to `Other`. An `Other` catch-all would make the enum trivially exhaustive and
convert *"could not classify"* into a category that looks deliberate — the same failure `holdings_status`
exists to prevent one field over.

## Semantic checks on the real plane (not merely "it ran")

- Sector weights sum to **exactly** each book's equity allocation: PFDE 99.64, PFOE 97.66.
  **This independently reproduces CTO's own GICS tie-out (65775) from a different route.**
- All four geography buckets populate — PFOE US 52.53 / International 29.99 / Emerging 15.14 /
  Other 2.32. I checked this specifically because a mapping that always returned US/Other would have
  looked fine on PFDE alone.
- Book weights total 99.99 and 99.98. Document 76,886 B vs the live Models artifact's 73,487 B
  decompressed — sane magnitude.
- Shells are genuinely rich: DIVZ aum 307,436,800, yield 1.568, cost 0.65, beta 0.5907.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `-i` over 12 vocabulary values, `--name "*publisher*"`, `-i GICS_SECTOR_NAME data infra` | **Drove the vocabulary act from MINT to ADOPTION.** Found the GICS vocab already in-estate, found the cash spelling in our own PRD, found the platinum-publisher precedent whose D5/D7/13c discipline I adopted rather than reinvented. `GICS_SECTOR_NAME` = 0 hits over 8,927 files in `data`/`infra` — no existing data-side mapping to reuse. |
| `comp-estate` | `--definitions` | 65 ratified terms; zero are financial sector/asset-class terms — no collision. Rung 2 discharged one layer up. |
| `comp-trigger` | `etfs-netassets-daily`, `etf-positioning`, `etf_positioning` | Established the AC4 precedent (`cron(0 22 * * ? *)`, ENABLED, FIRED 7x) and **measured AC4's actual state: NO MATCH over 136 events-rules + 18 schedules.** |
| `comp-pipescript` | `deployed` | Exceeded its 120s window, backgrounded. **The AC4/deploy conclusion does NOT rest on it** — it rests on `comp-trigger` and Rule 13's lane text. Recorded rather than dropped so the tool inventory is not overstated. |

## MCP traffic

- OUT 65713/65714 → COO+CTO: spec-at-pickup, 4/4.
- IN 65660 (MSTR bridge), 65667 (CTO A1/A2 ruling), 65668 (COO TO-1 cut), 65681 (CTO stage 4),
  65689 (AE CONTRACT v1), 65701 (CTO contract pointer), 65717 (COO pickup accepted), 65763 (MSTR
  push landed + shared-infra freeze), 65775 (CTO class call + GICS datum), 65780 (CTO TrueShares
  egress GRANTED), 65785 (COO TO-4 cut, P2, do not interleave).

## Blockers

**None blocking the build.** One open item routed, not held:

- **`ETFS-TO1-AC4` (schedule) — a LANE SEAM.** The producer scripts are my Rule-13 lane; the
  EventBridge rule + Lambda Terraform is a PROD trigger, which Rule 13 assigns to DT/AE. I did not
  cross the lane and did not manufacture a gate. **Routed to COO as issuer for the call.** Marked
  FAIL in the proof-of-spec — under-claiming is the safer error.
- AE's Half-2 403 / missing writer grant is expected, AE's cell, and does not gate the build.

## Current State (zero-context handoff)

`ETFS-d-2` COMPLETE. `ETFS-d-1` COMPLETE as code + proof; AC1/AC2/AC3/AC6/AC7 discharged, AC4 open at
the lane seam, AC5 pending its observed anchor. Commit `71265d372e` LOCAL, rides integration. **Zero
S3 writes performed this session** — both stages default to a full dry run and the publisher also
requires `OPAL_ETFS_PUBLISH_GRANT=1`.

## Next Steps

1. **[2.0.0_SA_COO]** Rule on the AC4 lane seam: assign the trigger to AE/DT, or qualify this seat to
   author+apply it (placement is LAPTOP, so Rule 26 is satisfied either way).
2. **[0.7.0_AE_CloudOps]** TO-2 Half 2 — bucket-policy ARN + writer grant for `platinum/etfs/*`.
3. **[0.4.0_DS_ClientPlatform]** Re-run the O-3 oracle against the first SCHEDULED `bbg/` landing to
   discharge AC5 — read it, never date it off the projection.
4. **[0.4.0_DS_ClientPlatform]** TO-4 (`ETFS-c-1`), **P2, behind TO-1, do not interleave** — Half 1 is
   a read-only determination that may delete Half 2 entirely.
