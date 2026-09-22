# Custody census and distinct SmartX facts

Authority: completion CONTRACT and CTO IRPT-M-BASIS-01 `b8de4c3899`.
This is a bounded fact-validation candidate, not an accepted holdings build.

`smartx_valuation.allocation_facts` preserves six separately named facts: canonical
gross AUM = long equity + reported cash; vendor net equity; long equity; signed
short equity; reported cash; and signed position values. It validates the complete
reported position count, unique position identities, allocation ownership and
source date before checking both net identities to one cent. Explicit zero-count
cash-only evidence is allowed. Missing/non-finite values, duplicate positions,
scope/date mismatch and unexplained differences refuse; no residual cash, rescale,
negative clamp or missing-as-zero fallback exists.

26 focused tests pass, including the original semantic shapes 100 long/10 cash,
100 long/-20 short/10 cash, negative net, zero net, missing value at zero, missing
cash, empty reported population, count mismatch and ambiguous position identity.
The historical builder test that expects equity+cash is preserved unchanged.
The actual old `build_49f` remains unfixed and cannot claim this helper's results.

Retained exact-version source replay through the new helper reconciles all 10,061
valuation rows and 120,639 positions, including 529 negative-net allocations,
2,045 zero-net allocations and 2,070 explicitly empty position populations.
This denominator is the whole valuation source, not the map's 7,509 allocations
or its 5,917 accounts. Its aggregate values must not be substituted into custody.
The diagnostic supplies a marked non-serving scope placeholder; production must
bind the real existing opaque-account/allocation reference and receipt revision.
`BASIS_SOURCE_EVIDENCE.json` retains hashes, source versions, aggregate findings,
original failed replay locations and the blocked runner patch hash.

Read-only canonical 49F custody evidence at business date 2026-09-21 contains
7,522 accounts in `canonical_valuation`, matching the current IN_CLIENT_BOOK
boundary. One collection account is explicitly outside that existing boundary.
Canonical positions contain 106,370 rows across 6,315 accounts, including 1,300
signed short rows. Current valuations include 884 zero and five negative values.
These are the existing Schwab master 08335338 chain's measurements, not proof of
all possible 49F custody sources. Historical `dim_account` contains 8,799 accounts;
1,277 lack a current canonical valuation, including 1,176 still marked open.
No current value has been invented for those historical rows.

The SmartX source's actual `as_of` and run dates are 2026-09-22. Comparing account
identities across the measured source sets finds 1,622 custody accounts outside
the SmartX map and 17 map accounts absent from current canonical custody. The
dates differ, so this is a coverage diagnostic, not an economic same-date tie or
evidence for attributing a custody residual. Membership history, full custody
scope and dated position attribution remain unresolved implementation work.

P agreed the optional per-node `valuation_facts` seam at 23:53:14Z: six closed
fact kinds, numeric value, USD, ISO source date, lowercase 64-hex source revision,
nonempty opaque allocation scope up to 200 characters; at most 64 facts and no
duplicate kind/scope/date/revision tuple. P owns shared schemas/adapter preservation;
M owns source integration and holdings display. The new helper is intentionally
not connected to the old overlay-derived custody root. No source migration,
live write, policy activation, publication or full M1/M3/M7 PASS is asserted.
