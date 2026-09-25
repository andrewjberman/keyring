# NFRA_MCPINDEX -- ROUND 1 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-09-25 ~06:4xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 25880, `REMEDIATION_v1.md` @df601037cc, `ADJUDICATION_v1.md` same commit),
and on `2.0.0_SA_COO~O`'s drain-end read (msg 25875). Round 1 was issued on the laptop by `2.0.0_SA_COO~M`. It was
wound down there on 2026-09-21, re-seated to the ~O fabric (@23bbeff325), and closed here. Grade tokens are
`REALIZED | NOT_REALIZED | DEFERRED | HELD`. The recut is `2.0.0_SA_COO~O`'s, in ONE issuance.

---

## 1. L7, L8 and L9 accepted

- **L7:** 38 of 38 orders are terminal. 9 are complete: MX-a-1..a-7, MX-c-1 and MX-c-2. 29 are superseded: 28 at the
  close, and MX-c-4 under ruling D-3. The CVO re-ran 9 of 9 instances VALID.
- **L8:** 11 of 11 items are dispositioned (7 graduated, 4 dismissed). The CVO also lifted two findings out of the
  issuer's prose (C-S12, C-S13), which is a row made from a sentence nobody had filed.
- **L9:** 8 judgment criteria were graded, all PASS with stated limits (C-S14, C-S15).
- **Adopted as the round's most useful act:** C-S13. The Black Diamond asset-to-cusip bridge is built by a script no
  scheduler runs, frozen since 2026-04-14, so every asset first seen since then joins to a null cusip. The round was
  about tools and found a live data defect underneath them.

## 2. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-1 (discover routes a cold question) | NOT_REALIZED | The catalog is written (MX-c-1) and its silver schema is in (MX-c-2). No discover tool exists yet. |
| FWD-2 (portal figures equal the portal's) | NOT_REALIZED | The analysis is done (MX-a-1). No portal tool is built. |
| FWD-3 (Schwab positions and transactions) | HELD | The Schwab tools sit behind G-Q and G-OPLGTW, Andrew's OPLGTW stop. Analysis done (MX-a-2). |
| FWD-4 (custodian and platform tools) | DEFERRED | Black Diamond waits on C-S13's read, Eclipse on C-S12's read, and Orion and SmartX follow the thread. Analyses done (MX-a-3..a-6). |
| FWD-5 (ETF tools) | DEFERRED | The TrueShares funds wait on W3-S2, which is parked. The other issuers follow the thread. Analysis done (MX-a-7). |
| FWD-6 (typed query) | DEFERRED | It follows the purpose-built tools, which are the routing ladder's first rung. |
| FWD-7 (entity resolution) | DEFERRED | It is still gated on D3's residual enum. |
| FWD-8 (on-demand paths) | DEFERRED | YCharts stays on Andrew's per-use word. Bloomberg is the NFRA_OPALAI S15 view. |
| FWD-9 (beta roster) | DEFERRED | G-B: Andrew admits the first beta person. |
| FWD-10 (next property = entry + tool) | DEFERRED | It needs one tool shipped first. |

## 3. Rulings on the open rows

**R-2, on C-S13 (ARMED, the Black Diamond cusip bridge).** The CVO's remedy is split by owner.
- (1) **The read is round 2's:** the null-cusip rate in silver transactions since 2026-04-14, and in any served figure
  that joins on cusip. It is read-only.
- (2) **Scheduling the builder is Black Diamond's pipeline, a DS act** under CLAUDE.md rule 13. It is PARKED with the
  owner of the Black Diamond pipeline, with the un-park condition "that seat live". It is a production schedule, not
  an alarm.
- (3) **No Black Diamond tool that answers by cusip is cut** until (1) reads.

**R-3, on C-S12 (ARMED, Eclipse firm scope).** Round 2 carries the one read: distinct firm or rep identifiers across
live Eclipse silver rows, checked against the Inflection allowlist. No Eclipse tool is cut in round 2 either way. If
any row falls outside the allowlist, the converter gains the filter first, and that is a DS act, parked like R-2 (2).

**R-4, on W3-S2 (ARMED, TrueShares holdings never reach silver).** It stays PARKED with `0.4.0_DS_ClientPlatform`,
which is NOT REGISTERED, last seen 2026-08-30. The un-park condition in its row stands. Routed from here: one line to
`0.0.0_AB_MSTR~Z`, because a DS seat is its to seat. Until it un-parks, the ETF tools exclude the TrueShares funds and
SAY so in their answer, never presenting an absent fund as zero.

**R-5, on W1-S5:** as ruling D-3 R-1. The re-cut cell classifies the 9 non-Schwab tools on MX-c-4's base, drains the
held branch and releases NARROW. AC11 is 49, graded 44 classified + 5 HELD. The CVO grades MX-c-4's AC8 before the
branch drains.

**R-6, carried as standing rules on every round-2 face:**
- W1-S6: a device-neutral interpreter, never `py -3.12`.
- W4-S1: every tool and read fence works by exact key prefix, never by bucket, with a negative control that reads a
  sibling property's prefix and is refused.
- W1-S1: a criterion that exercises a served file names that file in `<paths>` at the cut.
- W1-S3: the issuer picks, at the cut, gitignoring `catalog_v02/validation_report.json` or naming it.

**R-7, on C-S14:** the portal tool cell carries "model composition and weights" or names it unanswerable. The rest of
C-S14's gaps ride the tool cells they belong to, in later rounds.

**R-8, where round 2 builds.** The gateway has not moved into `opal_ai`: G-MOVE waits on Andrew's OPLGTW word. Round 2
is cut on the gateway's CURRENT path, and the move carries it, as NFRA_MCPORTAL's handoff rules. Every gateway release
is NARROW, cut at the deployed commit plus this project's own changes. Today's deployed commit is `f1f0fc6780`, and a
cell re-reads the manifest at its own cut.

## 4. THE ENRICHMENT LIST ROUND 2 CUTS -- the thread first

FWD-1 is the thread, and round 2 builds it end to end:

1. **E1, the discover family (S2).** A small set of always-loaded tools that answer from the ONE catalog: which property
   and dataset hold a fact, its freshness, its firm scope, its caveats, and the next tool to call. A question about an
   uncatalogued property says so and names nothing.
2. **E2, the portal purpose-built tools (S3, FWD-2).** The first rung of the ladder. They read the SAME precomputed
   tables the portal points at. They carry R-7's question. The side-by-side against the portal's page is the proof.
3. **E3, the classification cell** (R-5), with its narrow release.
4. **E4, the routing harness plus a question set from REAL asks.** It uses the Analyst's thread memory and the CRO's
   question lists, never the catalog's own descriptions (RCN-0014 finding 13). Its live cold run needs a non-author
   asker, which is G-B, Andrew's.
5. **E5, the two reads:** C-S13 (1) and C-S12. Both are read-only.
6. **E6, the batch cell:** C-S15's docstring line, and W1-S3's choice.
7. **Close run:** E1 plus E2 exercised live through the gateway. One question per portal surface, answered by the
   purpose-built tool, with the figure and date equal to the portal's. If G-B has been given, the FWD-1 cold run.

**Subtracted from round 2, with the reason for each:**
- Schwab (HELD, G-Q and G-OPLGTW);
- Black Diamond, Eclipse, Orion and SmartX tools (after the thread, and after E5's reads for Black Diamond and
  Eclipse);
- ETF tools (after the thread, with TrueShares on R-4);
- the typed query, entity resolution, on-demand paths and the roster (DEFERRED as graded).

## 5. What this analysis does not do

- It does not read the null-cusip rate or the Eclipse tenancy. E5 does.
- It does not seat a DS lane. R-2 (2) and R-4 are parked with owners and conditions.
- It does not touch the Schwab integration, NFRA_OPLGTW's contract or its store.
