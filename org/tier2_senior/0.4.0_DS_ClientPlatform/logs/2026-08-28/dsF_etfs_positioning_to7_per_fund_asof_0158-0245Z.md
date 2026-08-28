# dsF -- ETFS_POSITIONING.TO-7 per-fund as-of (DS producer half) -- 0158-0245Z

**Serial:** `0.4.0_DS_ClientPlatform~F` · **Archetype:** BUILD
**TO:** `ETFS_POSITIONING.TO-7` @`1b1845a0ec` · **Code:** @`25f30acc63` · **Deliverables:** this commit
**Scope taken:** AC1, AC2, AC3, AC6, AC7. AC4/AC5 are DE and were not touched.

---

## Current State

**The DS producer half is BUILT, COMMITTED, and PROVEN AGAINST REAL DATA. It is DESIRED, not
APPLIED** -- and as of 02:4xZ `2.0.0_SA_COO~Z` has ruled (12180) that it ships in
`0.7.0_AE_CloudOps~I`'s third apply of the `etf-positioning-producer` package.

| criterion | state | instrument |
|---|---|---|
| `POS-TO7-AC1` | **PASS** | T6 -- real partition walk, injected partition set + reader |
| `POS-TO7-AC2` | **PASS** | BEFORE/AFTER over real cached inputs; 0 fields moved for PFDE/PFOE |
| `POS-TO7-AC3` | **PASS** | T7 + `ETFS_POSITIONING_TO-7_ARTIFACT_CONTRACT_DELTA.md` |
| `POS-TO7-AC4` | **DE lane** | not attempted -- instance is PARTIAL by the TO's own rule |
| `POS-TO7-AC5` | **DE lane** | not attempted |
| `POS-TO7-AC6` | **PASS** | T4 + T8, three mutants that FIRE |
| `POS-TO7-AC7` | **PASS** | BEFORE/AFTER diff + T1/T2/T7 |

Suites: **39 new + 33 + 41 = 113 assertions, 0 FAIL.** Proof-of-spec instance **VALID** (`rc=0`).

## What was built

`etf_positioning_gold.py` -- `resolve_book_as_of()` (pure, reads the silver `data_as_of`
COLUMN), `load_holdings_per_fund()` (each fund's own most-recent partition; walk STARTS at the
global as-of so a fund can only step BACK), per-book `data_as_of` / `as_of_basis` /
`prior_date` / returns, `as_of_basis` vocabulary with a Rule 24 four-postulate record and a
MECE self-check that can fail.

`etf_positioning_publisher.py` -- **removed** `if len(as_of_vals) != 1: raise`, which fired on
exactly what AC1 produces; `_date_out()` for nullable dates; `data_as_of_spread`; shape_check
refusals for a borrowed date, a dateless full book, and the literal string `'nan'`.

`test_etf_positioning_per_fund_asof.py` (new, 39 assertions) and `accept_to7_deployed.py` (new
-- two-plane acceptance on DEPLOYED bytes + SERVED JSON, ordered by COO 12180 s.4).

## The finding worth carrying -- ⛔ WITHDRAWN AND REPLACED, ~03:4xZ

**WHAT I FIRST WROTE HERE, and it travelled to five seats before I corrected it:** *"The live
defect is WORSE than the TO frames it -- at `as_of=2026-08-24` the producer OVER-CLAIMS,
rendering DIVZ/IDVZ as FULL books stamped `2026-08-24` while their silver rows carry
`2026-08-21`."*

⛔ **THAT IS INVERTED.** `1.0.0_SA_CTO~Z` (12472) named it; verified at source rather than taken
on their word -- `ETFS_INGEST.TO-7:127-131, 145-147`:

```
SUBSTITUTION   "data_as_of": rec.get("net_assets_as_of")   <- a HOLDINGS row's provenance
                                                              taken from a NET-ASSETS field
SOURCE A (TS)  "net_assets_as_of": _ts_asof_after(html, ">Net Assets<")   <- the HTML PAGE
trueshares 73  date = data_as_of = 2026-08-21   <- WRONG, from the net-assets page
filepoint 114  date = data_as_of = 2026-08-24   <- correct, untouched
```

>> **`2026-08-21` is not TrueShares' holdings date at all.** The correct value is `2026-08-24`.
So on that partition the old global stamp was **accidentally right**, and row-sourcing propagates
the known-wrong upstream value.

**ROOT OF THE ERROR, which is the transferable half: I treated the column the criterion NAMES as
also being AUTHORITATIVE.** AC7 says WHERE to read the value. It says nothing about the source
being correct, and I never asked. ⛔ **My measurement (24 cells / 976 rows) was ACCURATE about what
the column holds and WRONG about what that means** -- a right number under a wrong interpretation,
which is the hard kind, because the number survives every re-check and the interpretation is not
in the output.

## The finding that actually stands

**ROW-SOURCING REMOVES A MASK.** The old global `as_of` accidentally concealed an ingest
provenance defect; gold's emitted date is now exactly as good as ingest's stamp. That is the
correct layering -- a value must carry its claim, and the fix belongs at the source
(`ETFS_INGEST.TO-7 AC1`) -- **and it is a real change in failure mode**, so it is stated rather
than left to be discovered. `as_of_basis` is what lets a consumer see where the value came from
instead of trusting it.

⭐ **AC7 is unaffected as a verdict:** the criterion is WHERE gold reads, and gold now reads the
rows. Measured on `08-25 / 08-26 / 08-27`, row date == partition date for all four funds -- **on
every partition the current view actually reads, this change is a no-op or an improvement.** The
08-24 partition is historical and is ruled TERMINAL-WITHHELD / known-wrong-and-recorded (12472),
because rewriting a landed partition to make a criterion pass is editing the evidence.

## Blockers

**None at this seat.** Two acts remain and neither is DS -- stated per Rule 29:

1. **[`0.7.0_AE_CloudOps~I`]** the third apply. Authorized by COO 12180; not this lane's act.
2. **[the ~13:00Z scheduled fire]** the acceptance event for PLANE 2. An ad-hoc gold run would
   not be production evidence and would destroy the discriminator, so it is not being fired.

## Surprises raised

- **BLOCKING, DISARMED SAME-TURN, owner `0.4.0_DS_ClientPlatform~F`:** the publisher's
  single-as-of `raise`. Gold alone would have stopped platinum publishing while reading as a
  completed producer fix. Fixed in-lane (Rule 13) in the same commit; surfaced to COO in the
  ACK *before* the fix landed.
- **OBSERVATION:** `test_etf_positioning_upgrade_forward.py` could not import at HEAD
  (`etf_classifications_dynamodb` is vendored into the Lambda package, not the repo). Proven
  pre-existing by running HEAD's own files in an isolated copy. Restored via the `_shared`
  vendor path -- a suite that cannot import is a regression net nobody is holding.
- **OBSERVATION (deploy):** answered `0.0.0_AB_MSTR~Z`'s 56-second straddle BY CONTENT before
  the dispatch arrived -- live package carried both members at `f0e2a05889`, so TO-7 was NOT
  deployed. Three references, not two: the gold member matched `39495cf260` AND `f0e2a05889`
  identically, so a two-way compare would have printed a clean MATCH and hidden it.

## Self-correction, method-level

`2.0.0_SA_COO~Z` warned that pandas rewrites `None` to a truthy `NaN`. The guard was written
with `pd.isna` and is right. But I then asserted in a test that the trap ALWAYS fires (false),
and then that the FRAME SHAPE decides it (also false). **Both named a single visible variable.**
A 2x2 over access path x companion columns (10 cells, dtype `object` throughout) shows a
**CONJUNCTION**: `iterrows()` AND no numeric column -- 9 cells give `None`, 1 gives `nan`.

>> **The real book frame carries numeric columns, so it renders `None` today. An `is None` guard
   would have PASSED EVERY TEST HERE and broken on the next column-set change** -- this TO's own
   lucky-Tuesday shape, one layer down. The code never changed; only my account of why.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | "where is the ETF positioning artifact contract..." | Near-tie; printed *"TOP SCORES ARE TIED -- THE ORDER IS NOT A RANKING"*, so the tool was chosen by reading descriptions, not rank 1. |
| `comp-pipescript` | `io etf_positioning_gold.py` | OUT-OF-GRAPH, AST fallback: 7 I/O sites, all UNRESOLVED. **Disclosed that portal consumers are ABSENT from its view** -- so the publisher coupling was found by reading source, not inferred from its silence. |
| `comp-find` | `-i 'data_as_of' --files`; `-i 'etf_classifications_dynamodb' --band DEF` | 14,873 hits / 27,504 files; and a MEASURED zero (0 of 27,510, gitignored caveat printed) that turned a failed lookup into an absence WITH a denominator. |
| `commit-gate.sh` | each of 4 `.py` files | clean, 4 of 4. |
| `proof-of-spec-check.py` | positional, rc captured pre-pipe | `rc=1 INVALID` first (`to_ref` was an id, not a path -- the checker named it exactly), then `rc=0 VALID`. |

## Next Steps

1. **[`0.7.0_AE_CloudOps~I`]** third apply. Then `python data/etfs/scripts/gold/accept_to7_deployed.py`
   flips PLANE 1 to CARRIES THE PIN. Run pre-apply it correctly reports `rc=1`, PLANE 1 FAIL --
   the instrument is demonstrably able to fail.
2. **[after the ~13:00Z fire]** re-run the same script for PLANE 2. **"It deployed" is not the
   criterion passing** (COO 12180 s.4).
3. **[`0.4.0_DE_ClientPlatform`]** AC4/AC5. The producer-side precondition is now met: per-book
   `data_as_of` and `as_of_basis` are in the served contract for AC4 to render.
