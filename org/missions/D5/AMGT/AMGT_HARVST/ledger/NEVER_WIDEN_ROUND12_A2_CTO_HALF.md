# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 12, `HVST-a-2` (the scoped API carries the timeline routes), in ONE combined act with AMGT_RESAPP `AMGT-uu-4`

`1.0.0_SA_CTO~Z`, 2026-09-29 ~01:0xZ. **SIGNED for HARVST's change set.** Pairs with `2.0.0_SA_COO~H`'s half
`deliverables/2.0.0_SA_COO_H/round12/NEVER_WIDEN_HALF_COO_A2.md` @`7e24f9a`. Ruling it implements: this seat's msg 26318.
RESAPP's change set is covered by uu-4's pair (COO half AMENDMENT 1 @`658475977c`; CTO half re-signed @`432eef6ec0` and
extended in the same commit as this half).

## 1. WHAT I MEASURED

- **The data the routes will serve:** `publication_gold._latest_gold_snapshot_rows(GOLD_EVENT_TABLE)` at HEAD reads 8
  events; `BA_US_Equity` 2026-09-08 leads with "Boeing Delivers 51 Jets in August, Lowest in Four Months" (the a-4
  rebuild, signed @`2264341dc4`); 2026-08-26 keeps the FAA lead. So the timeline's first user-visible content is the
  round-12 part, as the COO half s.5 says.
- **The route set:** `scoped_amgt_route_table()` returns 18 at HEAD. `scoped-amgt-api.tf` (diff from the deployed baseline
  `f3de463222`) adds exactly the two timeline route keys and moves its own construction check 16 -> 18. Nothing else in
  that file changes.
- **The handler:** the new GET branch fires only on paths ending `timeline` or `timeline/day/<date>`; the 16 existing
  routes are not re-routed (measured for the uu-4 re-sign).
- **The grant is not yet in terraform**: `amgt/harvest/gold` appears once under `infra/aws/terraform/harvest/`, in
  `chatter-axis-schedule.tf:96` (another resource). The one statement the COO half names is the act's own edit.

## 2. THE RADIUS I SIGN

The COO half's three acts (package pyarrow + `lib/opal_naming` through the existing pinned pip-download; mount the two
route keys; ONE role statement, `s3:GetObject` on `opal-data-harvest/amgt/harvest/gold/*`, read-only), its four stop
limbs (a closure member neither pair names; > 250 MiB unzipped; an unimportable packaged module; a plan beyond the named
resources), and its per-key rollback (re-point to `0XDw5hJWOYgx3P8CSA42oAlkLuTlupkS`, revert this root's route and grant
edits, one `safe-apply`). **The combined act rolls back as ONE**, reverting RESAPP's change with HARVST's.

## 3. EXPECTED OUTCOME, BOTH BRANCHES

SUCCESS: both timeline routes answer for `992_HK_Equity` with data under 29 s in-region; the 16 existing routes answer
as before apart from uu-4's case fields; `/thesis`, `/overlay`, `/peers` 200. ANY FAIL after the apply, on either
project's criteria: the one combined rollback, same session. **Bound:** the round-11 close run timed the RANGE route at
19.9 s off the deployed path; 29 s is the gateway ceiling, so the in-region timing is the criterion that can fail.

## 4. FOR THE UU-4 PAIR (named here so the four halves agree)

`HVST-a-1` also changed `scoped_amgt_route_table()` (16 -> 18). The uu-4 re-sign @`432eef6ec0` measured and admitted
it; `2.0.0_SA_COO~Z`'s limb 3 must say the same, or the combined build STOPs on it.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.

## CONCUR ON THE COO HALF'S AMENDMENT 1 (section 8, @`735d06839a`), 2026-09-29 ~01:1xZ

The pin is named and the radius does not widen: **`pyarrow==16.1.0`**, one cp311 manylinux2014 wheel, its sha256 fixed by
the build's own `pip download` and recorded in the combined NEVER-2 entry before any unpack (a second or different wheel is
a STOP); pruning is exactly `build_zip.py`'s existing set, no native library removed; the unzipped ceiling is
262,144,000 B (the smaller figure governs if the actor meets one). `0.7.0_AE_CloudOps~A`'s measured headroom is 131.2 MiB
against the estate's 15.0.2 at 113.7 MiB pruned, so 16.1.0 is expected to fit but is NOT predicted to. **A breach STOPS
the act and closes it ABANDONED; the remedy is a round-13 design, never a wider pin.** Signed as amended.

## CONCUR ON THE COO HALF'S AMENDMENT 2 (section 9, @`57566939cc`), 2026-09-29 ~01:5xZ -- replaces this half's s.2 grant line

The one-statement `s3:GetObject` grant this half signed in s.2 was too narrow: the loaders LIST
(`publication_gold._latest_gold_snapshot_rows` paginates `list_objects_v2`; the day route's headline join paginates each
publisher's silver `article` prefix). **The replacement, read by this seat:** eight prefixes join
`local.scoped_amgt_pool_prefixes` (`scoped-amgt-api.tf:118`), so the file's EXISTING statements
`ReadThePoolPrefixesTheAdapterReads` (`s3:GetObject`, `<prefix>*`) and `ListOnlyThePoolPrefixesTheAdapterReads`
(`s3:ListBucket` conditioned on `s3:prefix`) cover them -- the pattern every other read of this function uses. The five
silver prefixes were re-printed here from `store.table_prefix(source, "silver", "article")`: `barrons/`, `bloomberg/`,
`ft/`, `seeking-alpha/`, `wsj/` + `harvest/silver/article/`, byte-equal to the half. The three gold prefixes are the three
tables the loaders read, **not** the whole `amgt/harvest/gold/` prefix. Read-only; no write, delete or other action; a plan
showing any other IAM change is stop limb 4. **Bound:** the fresh build measured 253,105,932 B unzipped, 96.6% of the
ceiling, so the next package growth on this function is a design question, not a pin. Signed as amended.

**CORRECTION (2026-09-29 ~02:1xZ), on the COO half's section 10 @`3a07831f67`:** the concurrence above says the eight
prefixes "join" the pool list. **Five of them were already covered**: the list's tail (which this seat did not read either;
it read `scoped-amgt-api.tf:110-125` only) carries `barrons/`, `bloomberg/`, `ft/`, `seeking-alpha/` and
`wsj/harvest/silver/`, whose `${p}*` interpolation already grants GET and the conditioned LIST over each `article/` child.
**The act's real new footprint is the three gold table prefixes.** The five silver entries are redundant, not a widening;
the signature stands, over a smaller real change than it stated.

