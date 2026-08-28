# Reading a file twice did not find the site; rendering it found the site in one shot

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-08-28
**Project:** ETFS_INGEST -- condition (ii) render rung (Rule 27: this instance's only project, seated by `2.0.0_SA_COO~Z` msg 11648)
**Window:** 2026-08-28T00:49Z -> 02:15Z

**Portal commits (DEV, LOCAL):** `09f9078b`
**Push state, MEASURED:** LOCAL @`09f9078b` -- `git ls-remote origin DEV` reads `f1180aad`; 1 ahead, 0 behind. Integrator pushes (LD-0367).

---

## Objective

Seated on Andrew's promote-condition (ii): *"it displays properly on DEV build with GICS replaced
for sub-categories on frontend."* `1.0.0_SA_CTO~Z`'s 11382 measured rungs 1-6 and left **rung 7
(frontend) explicitly UNMEASURED** -- "I did not open the portal." That rung is this seat's.

---

## Compiler Tools

| tool | run | result | note |
|---|---|---|---|
| (none) | -- | -- | see below |

**No comp-tool was run this session, and that is a finding about my own conduct rather than an
exemption.** Searches went through raw `grep` and native Read. Rule 21 makes a comp-tool the DEFAULT
for search and inspection and raw grep the EXCEPTION; my searches were file-scoped rather than
estate-scoped, so no rail DENIED -- but "no gate fired" is not "complied."
**Andrew-direct ~02:0xZ landed mid-session** (relayed 11841): *"Make sure everyone is using
comp-find ... this would probably help a lot."* Acknowledged as a fair hit in msg 11891 s.6.
**What worked anyway:** every census printed its denominator and carried a POSITIVE CONTROL, which is
the substance the rail exists to enforce -- e.g. industry-group tokens 0 of 13 files with
`sub_asset_class` firing at 4 of 13; fetch-path 0 hits across six patterns with
`positioning_data.json` firing at 8 files.
**Gap found:** the spirit held and the instrument did not. Complying from here; raw commands get the
`# rail-checked: <why>` marker.

---

## Work Completed

**1. Rung 7 measured** (msg 11405). Condition (ii) needs FOUR frontend edit sites, not one, and the
type contract lives in TWO homes. Named the silent-drop property: `toCurrentHolding` is an ENUMERATED
allowlist, so a producer/consumer key-name mismatch renders nothing and ships green. Established that
**no served key name had ever been ruled** -- the DS lane had searched twice on two days and found none.

**2. The page rendered** -- the act both CTO gates declined (msgs 11423, 11509). Six captures. Corrected
11412's *"nothing renders at all until TO-5-DS lands"*: Satellites mode renders a COMPLETE, correct page
with mode-aware copy, capability gating, and a declared empty state. Colour law clean throughout.

**3. `ETFS_POSITIONING-Z-S9` filed** (CVO~Z). `satelliteAdapter.ts:105` joins two causes with `||` into
one `data: null`; `Positioning.tsx:316` names only one. Filed source-confirmed with the bound that I had
NOT separated the limbs; later separated them by single-variable ablation and the record moved to
EXERCISED. A third cause was then found (registry non-empty, all members dropped by validation) in which
**two on-screen notices contradict each other**.

**4. The PERFORMANCE grain split** (msg 11458, adopted by CTO~Z 11464). The panel needs per-TICKER
returns, not per-MODEL; the satellite adapter already spreads them onto blended rows. Andrew's
sufficiency clause corrected from 2-of-3 to 3-of-3. Only the BOOK-grain return is genuinely unbuilt.

**5. The published registry rejected 9 of 9** (msg 11539). Constituent weights were FRACTIONS; the
contract declares `PERCENTAGE (0-100)`. Ruled: the producer converts. Re-mint independently verified
from the served bytes -- 9 of 9 passing, 0 fractional.

**6. The credentialed read nobody had done** (msg 11569). `returns` populated **110 of 110** holding
rows. `as_of_date` NULL on **5 of 5** books -- so the as_of assert ruled 20 minutes earlier **could
never fire** -- while `prior_date` skews 2-across-5, so skew is real on a different field.

**7. Condition (ii) render BUILT and committed** @`09f9078b`, five sites, verified by render.

---

## Decisions Made

- **Geometry remedy (b) shipped without a ruling, flagged as such.** `whitespace-normal` on the
  recessive span. Shipping the untouched 165px cell would have shipped a measured collision; (a) widen
  and (c) truncate remain a one-property change. Not treating my own recommendation as a ruling.
- **Declined to build while the key name was unruled**, then re-asked once with an explicit
  deprioritise option. Ratified by CTO~Z 11831 s.3.
- **Used an isolated git worktree** rather than editing a checkout six agents share.

---

## Blockers

**None.** Condition (ii)'s render half is committed and INERT by design -- no such field is served
today (rungs 3-6 absent). The producer half lands at the 11:00Z pull + 13:00Z gold fire and is not
this lane's. Andrew's smoke test remains the completion bar.

---

## Current State (zero-context handoff)

- `portal` @`09f9078b` on DEV, **LOCAL**, 1 ahead of `origin/DEV` = `f1180aad`.
- `industry_group` + `industry_group_basis`, both `?: string`, at five sites:
  `src/api/portal-proxy.ts` (EtfHolding, CurrentHolding) ·
  `src/pages/Positioning/shared/etfAdapter.ts` (toCurrentHolding) ·
  `src/pages/Positioning/tabs/HoldingsTab.tsx` (AttributionHolding, the Current-period mapper, the
  Sub-Asset cell).
- `industry_group_basis` is RECEIVED and deliberately NOT displayed (CTO 11831 s.2).
- **The fifth site is the load-bearing one:** `HoldingsTab.tsx` Current-period mapper is an ENUMERATED
  object literal with no spread. Its SIBLING mapper ~50 lines below DOES spread. The enumerating one is
  the live path because `selectedPeriod` is hardcoded `'Current'`. Any future holding-row field hits
  this same drop.
- Shared-tree note: `0.4.0_DE_ClientPlatform~S` has uncommitted work in this checkout
  (`Positioning.tsx`, `satelliteSet.ts`, `CategoryViewTree.tsx`, `src/api/endpoints/satelliteRegistry.ts`).
  My pathspec was exactly my three files; theirs verified untouched after committing.

---

## Next Steps

- [`1.0.0_SA_CTO~Z`] Geometry remedy (a)/(b)/(c) -- (b) is shipped; overruling is a one-property change.
- [`2.0.0_SA_COO~Z`] Wants a `bun run build` typecheck before this rides a push? Not run.
- [`0.4.0_DS_ClientPlatform~Q`] CTO 11831 s.2 asks that the publisher carry BOTH keys; `industry_group`
  was measured reaching it, `industry_group_basis` was not seen in that count.

---

## Postmortem -- I nearly reported a defect I manufactured myself

The Model Portfolios page hit its error boundary with `TypeError: Cannot read properties of null
(reading 'useRef')`, on a page named in a sovereign instruction. **The cause was mine:** I had
junctioned the shared `node_modules` into a worktree, and a junction brings `node_modules/.vite` with
it, so a second vite server re-optimised deps under the first.

⛔ **The obvious control did not clear it.** Re-rendering a DIFFERENT route came back clean, because
only the crashing route's lazy chunks held the bad entry. **A passing sibling route is not evidence the
cache is healthy.** What settled it: stop every server, `rm -rf node_modules/.vite`, start ONE, re-render
-- clean. The `deps/` mtime matching my second server's start was the tell.

**What made it catchable at all was asking what *I* had changed about the serving environment before
believing the page.** Banked as `two-vite-servers-share-one-dep-cache`, and the shared cache was cleared
so the next seat does not inherit it.

⭐ **And the session's own headline is the same shape, inverted:** I named four edit sites by READING
the code, twice. I made two of them, rendered, and NOTHING APPEARED -- a fifth site was silently
swallowing the field between a populated payload and a correct renderer. **Reading found four; building
found the fifth in one shot, and the fifth was the one that mattered.**
