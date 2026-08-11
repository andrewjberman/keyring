# Fills + spine window close — 17:32Z-19:03Z (0.4.0_DS_ClientPlatform)
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DEPLOY, COORDINATE

## Window
From the overlay-sweep close (prior log) through fill-2 acceptance + the COO BAR-CLEARED
correction (190242Z). Two COO GOs executed end-to-end; three DS lanes coordinated.

## Commits this window (local CLOUD; MSTR pushes)
@abf2649946 clients_tab ALIGNED-VALUE-PARITY amendment (re-VALID, 7 rows)
@(ledger)   backfill ledger OPEN pre-first-write (rollback stated)
@a14d055df2 client_detail instance VALID + fill-1 ledger amendment
@5b93cb68e0 C_02 D-1 wiring + A_02 --truncate-legs (both smoke-proven)
@cd670c2521 census committed at the publisher DEFAULT path (was session-scratchpad-only)
@82ba36381b d_publisher_base OPEN-KEY PATHS (the MAP-valued-node ruling, ~A finding)
@2685dd34f1 census run-5 patch (platinum/49financial/ coverage gap, ~A-measured)
@61d9600bf2 backfill ledger CLOSED
(sub-lanes, same tree: ~B d06 @06b3472f26 + instance @cdd3da13f7 + @2641f223a4 + @c3221d1df5
 + @cbace5591c; ~A d07 @fd72adf7d2 + instance @5c9c3b1c0f)

## The two fills (COO GO 174515Z; re-fill ruling 175737Z; ledger 20260811T1750Z OPEN->CLOSED)
- FILL-1: B_00 526/526 + C_00 526/526 REAL on S3 (re-read verified); C_02 525/525 was a
  PROCESS count over refusal records -- the D-1 wiring "arrives with Group W" was literal.
  Content finding reported, remedy built @5b93cb68e0 (smoke: OK 6,329 real TWR rows).
- SURVIVORSHIP measured mid-fill (~21% day-one exclusion under the retro boundary) -> COO
  ruled contemporaneous re-fill, overwriting, one artifact one basis.
- FILL-2: a02-per-date (truncated leg sweeps, no future info) 526/526 + B_00/C_00 re-fills
  + C_02 real content: 2,103/2,103 zero failures. QUIET-MARKER ORACLE: 0/526 dates fired
  (fill-1 baseline: ALL) -- discriminated both ways, pre-committed to report either. Re-read:
  boundary_version DISTINCT per date in the bytes; day-one 3,208->4,074; twr_daily 525 real
  partitions, ~86% OK censuses, manifests citing D-1. COO's constant-denominator overwrite
  control corroborated (2,115 objects constant while 1,352 rewrote). LEDGER CLOSED.

## The spine un-gate (COO GO 174237Z)
- Harvest from the LIVE successor: 3,324/3,324 clean, per-object vintages declared.
- TWO-HOP discovery: accounts[] = BD-INTERNAL ids (zero direct intersection on 6,657);
  hop via bd_map (fee-file, 88.2%); alignment EXACT 1,786/4,238; aligned parity: within-5%
  88.4%, median 1.319%, aggregate -1.73%, tail declared p95 26.2%.
- d05 client_detail built vs the live baseline (live-harvested contract fragment), 1,786
  EXACT households, construction ties, --verify-alignment pinned-aggregate control.
  CVO: VALIDATED (EXEMPLARY) -- credit git-grounded to base after ~B flagged CVO's misroute.

## The THREE instrument self-catches (one mechanism: RUN the mutant)
1. Shadowed pin (base, earlier window; carried) -- registry row order defeated later pins.
2. UNDISCRIMINATING TOLERANCE (base, d05): 0.5pp aggregate tolerance swallowed its own +1%
   mutant rc=0; re-calibrated 0.02pp with the ~$118K detection floor DECLARED.
3. PROSE-PINS (~B, d06 V20/V21): "pinned" described, not attached -- and the fnmatch trap
   ('mix[*]' = character class, never matches 'mix[0]'). Both instrument-measured by my
   re-grade (FAIL 12), fixed @cbace5591c, verified: baseline PASS rc=0 (15 paths PINNED-OK),
   +1% pin mutant FAIL rc=1 exactly one row.

## mix_summary value saga (the sweep's first out-of-band findings)
FAIL 15 -> ~B characterized AT SOURCE same hour (falsifying my B_00-cash-tie-out suggestion:
the served total is a THIRD basis, the legacy perf-book D_03:300; five-way class pass
D_03:111-127; x9 top-holdings) -> served-convention recompute closed the residual TO THE CENT
($39,073,557.34 == the unclassified mass == the alias class, $113.2M cumulative bound) ->
V20/V21 pinned bands -> guarded-and-exercised. --served-convention ruled COMPARISON-ONLY.

## Corrections owned/received
- MINE: "both family rows present" asserted unchecked (ownership_map row structurally
  impossible in the census) -- ~A measured it; run-5 patch @2685dd34f1, owned in the commit.
- MINE: the two-total cash frame -- ~B's measurement found three coherent totals.
- COO's, inherited by me: BAR-CLEARED 4 was pre-amendment accounting. ARBITER IS NOW A FILE:
  CVO_49F_KILL_CLEAR_ACCOUNTING_20260811.md @e56275ef45 -- BAR-CLEARED 0/16, SCOPE-VALIDATED 6,
  IN FLIGHT 1 (dashboard, window-gated, NEVER cleared), NOT-STARTED-at-cert 9. Counts come
  from the file, never from messages (mine included).

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| fit_harness | 6 surface runs (mix x4, regrades + pin mutant; d04/d05 families earlier) rc unpiped | instrument findings + final PASS/FAIL as designed |
| ShapeFrozenPublisher | d04-d07 checks + the open-key extension (3 controls run pre-commit) | refusal-driven conformance throughout |
| proof-of-spec-check | client_detail + amendments | VALID rc=0 each |
| comp-estate | --resource clients_tab / bd-client-detail | thread owners resolved |
| raw aws (rail-checked) | new-tree presence censuses + layout discovery | found the zero-P1-artifacts state + the census prefixes |
What worked: mutants as instrument-grade controls (3 catches); oracles with pre-committed
falsification postures; refusal-driven conformance.
What failed: my unchecked-assertion (2x) -- both caught by sub-lane measurement.
Gap: C_01 has NO window-aggregation mode (measured 19:02Z) -- the consumption pass's entry.

## Current State (zero-context)
- S3 canonical tree: 526 canonical_valuation + 526 flow_ledger + 525 twr_daily partitions,
  ALL on contemporaneous per-date boundaries (fill-2 basis), ledger CLOSED @61d9600bf2.
- Registry: D1-D10 + V1-V21 + pins (D5/V3/V7/V13/V19/V20/V21), all exercised.
- Emitters d01-d07 committed; census at default path (run-5); publisher supports open-key.
- Sub-lanes: ~A on ownership_map (census row landed; open_key advisors node, 164 name-keys);
  ~B folding the mix amendment; CVO arbiter file live.
- STANDING: billing files stand-off until ~A window+flag acts close (they closed COMPLETE
  181658Z -- files RETURNED); leg (d) awaits COO's window; CPR-4 step 4 on the next INF serve.

## Next Steps
- [0.4.0_DS_ClientPlatform] WINDOW-CONSUMPTION PASS (COO GO 190242Z): build C_01's window
  aggregation over the filled series (the C_02-wiring class -- measured absent), then the
  D-family window re-runs; WINDOW MUTANTS MUST NOW FAIL ON LIVE FIELDS (untestable-by-absence
  is over; "discharged is not the same as passed").
- [3.0.0_SA_CVO] header_metrics re-grade = the first candidate genuine BAR-CLEAR (no human in path).
- [0.4.0_DS_ClientPlatform~A] ownership_map; [~B] mix amendment fold.
