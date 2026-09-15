# POSN_ASTTAX -- ROUND 6 ANALYSIS (L10)

**From** `1.0.0_SA_CTO~Z`, L2/L4 owner, answering `3.0.0_SA_CVO~Z`'s round-6 slug
`surprise-channel/remediations/REMEDIATION_v6.Z.md` @`895a87921f` (L9: `surprise-channel/adjudications/ADJUDICATION_v8.Z.md`).
**2026-09-15 ~10:3xZ.** Portal gitlink `e85f6eb84f`, unmoved. **Round-6 portal head: `refs/drains/posn-6-portal` = `ebbee2e61a`**
(F5 `10a2799c` + F5 re-cut `5ddce2c7` + F4 `16c5d359`, drained `ebbee2e6`) -- the ref `0.0.0_AB_MSTR~Z` publishes to the cross-fabric
merge (msg 23085). No promote, no DEV/PROD push from this seat.

> **VERDICT: ROUND 6 IS CLOSED WITH NO PRD ADDENDUM; ONE ONE-CELL RECUT (`C-S177`, the seeder guard) IS CUT AFTER THE PROMOTE. The Satellites mode presents on today's data.** B6 deployed and was
> driven twice (04:53Z, and 08:10Z on the ad-hoc Bloomberg partition); F4 and F5 are drained; the real ad-hoc pull Andrew asked for
> ran end to end; `2.0.0_SA_COO~Z`'s render read 0 of 512 Holdings Breakdown cells mismatched (Z-S171) and `0.0.0_AB_MSTR~Z`'s independent
> instrument read 0 of 544 (msg 23102). What remains is cosmetic, tooling, or the guard cell; none gates the merge. **FWD-3, FWD-4, FWD-6 and FWD-7 become REALIZED at the promote** --
> the freeze is the only thing between the drained code and a user, and it is Andrew's word (by 13:00Z, msg 23085).

---

## 1. COVERAGE -- the subtraction, measured this tick

```
DENOMINATOR   31 task orders under POSN_ASTTAX (27 complete, 2 superseded, 2 cancelled; 0 open) -- L7 closed @5467a8e804, 10:03Z
DECLARED       7 (FWD-1..FWD-7, PRD v0.11)
COVERED        7
UNCOVERED = declared MINUS covered = { }

  FWD-1 19 orders   FWD-2 7   FWD-3 4   FWD-4 3   FWD-5 5   FWD-6 7   FWD-7 2 (TO-W1-1, TO-W2-1)
```
Instrument: every `task-orders/*.md` read whole, `<status>` parsed, outcome ids matched as whole words; FWD-1..FWD-6 the positive controls.
WARN: naming is not serving -- s.5 grades each outcome on the served plane.

## 2. WHAT ROUND 6 ESTABLISHED

| cell | order | landed | evidence |
|---|---|---|---|
| B6 | `TO-W1-1` | `characteristics.json` gains the `tickers` block (measures + `name`/`management_style` from ETFClassifier); rule `cron(30 12 * * ? *)`; READ grants for the history prefixes and `dynamodb:GetItem` | deploy ledger `posn-round6-b6-characteristics-tickers`; driven runs 04:53Z and 08:10Z (VersionId `PXyBGaqn.0Jk6TwWmXl34FlsDH8Gwd0R`, 25 tickers 23/1/1, names 25/25, GLD 8 windows at the 2026-09-14 frontier; this seat's read-back 08:1xZ) |
| F4 | `TO-W2-1` | the adapter attaches each holding's served measures, name and ACTIVE; ACTIVE's blank third state; the Holdings panels on the mode's own clock; the composition legend per displayed book | `16c5d359`; render compare 0 of 512 (Z-S171) |
| F5 | `TO-W3-1` | one presence set per render over the columns the view DRAWS; the single-bar label at two decimals trimmed; the Satellites footer Black Diamond's; the blend copy retired | `10a2799c` + `5ddce2c7`; Models control unchanged (82.6% / 17.4%) |

Outside the cells, this session: R2 relabel (03:02Z, Z-S135); GLD/VXX return-history backfill (ledger closed @d3d2ffc4a5); the ad-hoc
Bloomberg pull `bbg/2026-09-14` (07:52Z, run_class adhoc, msg 23083); the 07:00Z organic registry fire (Z-S165).

## 3. ROUTING -- the slug's remediations and the round's carried rows

| id | remedy asked | disposition |
|---|---|---|
| `C-S177` (DECOMP_INVALIDATING, ARMED, owner this seat) | V3-AC7 FAIL: the seeder guard's owned fields `YANG_OWNED_FIELDS = ('asset_class', 'sub_asset_class', 'name')` (`data/black_diamond/scripts/classification/seed_canonical_securities.py:210`) do not cover R1's write surface, which also set VNQ's `management_style` (`TO-V8-1` V8-AC4); reconcile before any reseed and prove the corrected set | **ONE-CELL RECUT, round 7, cut by `2.0.0_SA_COO~Z` AFTER the 13:00Z promote -- NO PRD ADDENDUM.** `C-RETAG-SAFETY` and `C-RETAG-SET` already bind the guard to every field the retag writes; the defect is the tuple, not the spec. The cell: add `management_style` to the owned tuple (or state, measured, why a reseed can never write it), and a criterion that runs the guard against a reseed changing ONLY `management_style` on VNQ and reads the refusal. **NOT GATING THE PROMOTE, measured:** no EventBridge rule schedules a seed (`list-rules` on "seed": empty), and VNQ is held by no satellite and no served Yang book, so no served figure moves before the fix. v0.11's `C-HOLDING-IDENTITY` now READS `management_style`, which is why the fix is owed rather than optional. |

**Judgments owed at L9, stated rather than assumed graded:** `ADJUDICATION_v8.Z.md` grades round 5's three carried judgments (V1-AC13 PASS,
V2-AC14 PASS, V3-AC7 FAIL). Round 6's own three -- `W1-AC15`, `W2-AC9`, `W3-AC8` -- appear in no adjudication file (census of
`surprise-channel/`: the investigation file only). They are owed by `3.0.0_SA_CVO~Z`; none is a precondition of the promote, and the
round's L10 does not wait on them.

**Carried, not gating the merge (owner named):**

| row | item | owner / where |
|---|---|---|
| `Z-S146` | the longest Satellites label (90.24%) clipped at the panel edge at 1440 px -- pre-existing, narrowed by F5 | next Positioning frontend cut |
| `Z-S169` | the Holdings header's `DataTimestamp` takes `source` and never renders it; the composition title sits under the chip strip | next Positioning frontend cut |
| `Z-S172` | VGSH's Credit cell renders "-0" (served -0.1467 through `toFixed(0)`) -- a signed zero, not a float | next Positioning frontend cut |
| `Z-S154` | the characteristics handler's docstring still reasons about `cron(20 7)` | next edit of that handler |
| `Z-S163` | `lambda-source-map.json` carries 28 non-ASCII bytes again from the CI recorder's own deploy commits | deployment tooling owner (one recorder fix: encoding + ensure_ascii) |
| `Z-S151` | the artifact's `inputs` triple is not an identity for the input BYTES (same dates, different bytes) | next B6-family edit: add input VersionIds |
| `Z-S143`, `Z-S145` | `ui-smoke.mjs` text dump is a 160-char prefix; the portal does not ignore `.scratch/` | portal tooling owner |
| `Z-S148`, `Z-S150`, `Z-S156`, `Z-S162` | sparse-cone worker worktrees cannot run the commit gates / manufacture CRLF "modified" files | `/dispatch` cone recipe (the COO's) |
| `Z-S158` | the row gate's `class` enum is two values; workers reach for richer ones | surprise-channel doctrine owner |
| `Z-S137` | round 6 passed LIMB 6 on the ~W lanes' v0.10 signatures (the router's alphabetical pick); the ~Z re-signs at the same bytes followed | **OPEN CALL AT ANDREW**: `route_half` prefers the project's fabric letter |
| `Z-S173`, `Z-S174` | F4 took four spawns, three of them on the issuer's invocation defects, and one spawn HUNG 07:35-09:21Z while the harness showed it running (stopped on this seat's file-plane measurement, msg 23110) | the COO's cut discipline: every limb names the base, never the moving ref; a worker liveness read on the files, not the harness |
| W1-AC15 (JUDGMENT) | GLD's returns come from the ETF gold rule beside Yang's windows (start-inclusive, 1Q 91 vs 90 days) -- disclosed in v0.10 | graded at L9: NOT YET GRADED -- owed by `3.0.0_SA_CVO~Z` (see above) |

## 4. STATE -- 0 of 7 REALIZED, and what moves them

- **FWD-1, FWD-2, FWD-5** -- served: both stores carry the thirteen; `holdings.json` 2026-09-15 carries the retagged labels (Z-S165);
  the Yang payloads carry them. REALIZED on the DATA plane at this read; graded REALIZED on the page at the promote with the other four. FWD-5 carries `C-S177`: a reseed today would refuse a change to the class fields but not to `management_style`.
- **FWD-3, FWD-4, FWD-6, FWD-7** -- the drained code at `ebbee2e61a` renders them against the served bytes (Z-S171). They are
  served to no user until the promote; that wait is Andrew's, expressly (the freeze; his ~08:0xZ deadline).
- **Freshness, stated:** at this read the 23 Yang-priced satellite tickers carry `positioning_data_as_of 2026-09-11`. A THIRD driven
  characteristics run is armed on the ~11:05Z models publish being READ at `data_as_of 2026-09-14` (both B6 halves: COO R3 @f083f68e17,
  CTO A3 @4d751e57c1), so all 25 reach T-1 before the merge window; B6's 12:30Z fire stays the organic leg.

## 5. ALSO OPEN AT THIS SEAT

- Card-4 ledger `posn-bbg-etf-pull-gld-vxx` L2: the 11:00Z scheduled pull's manifest (`run_class scheduled`), read and closed by this seat.
- The cross-fabric merge overlap on the Positioning files (laptop `d13`: "Satellite ##" labels, per-asset hover colours, the
  name-keyed palette) is `0.0.0_AB_MSTR~Z`'s `/integrate` resolution; this round's head is named above.

---

**PRD ACTION: NONE.** v0.11 @`ab2ee8052a` stands, both halves SIGNED by the ~Z lanes. **The recut is `2.0.0_SA_COO~Z`'s: ONE issuance of
ONE cell (`C-S177`), after the 13:00Z promote.** The cosmetic and tooling rows ride the next Positioning frontend cut when Andrew calls one.

Push state: LOCAL (this seat never pushes; `0.0.0_AB_MSTR~Z` carries).
