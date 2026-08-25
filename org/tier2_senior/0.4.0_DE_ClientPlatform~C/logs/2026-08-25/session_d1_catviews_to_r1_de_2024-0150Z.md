# The MDPF L0/L1/L2 view tree — built against a contract that moved three times — 0.4.0_DE_ClientPlatform~C

**Date:** 2026-08-25
**Task Order:** D1_CATVIEWS.TO-R1-DE
**Status:** COMPLETE (delivered; awaiting CVO cert)
**Portal DEV commits:** `760504f0` → `4034239c` → `d1f8f38a` → `cd2f059c` → `7def244d`
**Workspace CLOUD commit:** `d708b02a2f`

---

## Objective

Render Andrew's 2026-08-24 ~18:5xZ view tree on the MDPF page: L0 present-subset tiles, L1
drilldown, L2 Custom enumeration, and the not-available states — consuming the DS lane's
`category_views` block rather than computing membership in the renderer. Eight cells
(`D1-h-v1..v4`, `h-p1`, `c-1`, `c-2`, `inv-4`), nine acceptance criteria.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-transform | `schema-check ModelPortfolios` | **FAIL (silent)** | rc=1, one WARN, its own `SCHEMA CHECK:` header never printed — the check ABORTS at types-resolution. `MISSING 0` is a NON-RESULT that reads as a pass. |
| comp-transform | `schema-check Correlation` / `FactorTilts` | PASS | Positive controls. rc=0 with real verdicts, FactorTilts naming a genuine gap — this is what established the tool discriminates and simply has no domain on a flat single-file page. |
| comp-cache | `comp-cache collisions` | PASS | Found the pre-existing `['model-portfolio-benchmarks']` collision (ModelPortfolios.tsx:533 / ModelPortfolioModal.tsx:114). Bare `comp-cache` prints usage — it needs a subcommand. |
| comp-find | `comp-find -i 'drilldown' portal/src/pages/ModelPortfolios.tsx` | PASS | Printed `DENOMINATOR: 0 hit(s) across 1 file(s)` — the framed zero did its job. |
| comp-which | `comp-which "how do I grep the repo"` | PASS | A.3 exercise limb; forwarder produced its own banner. |
| proof-of-spec-check | positional, 9 criterion ids | PASS | VALID rc=0; prints its own alignment frame (9/9, 8/8, 8/8). Caught one real schema violation first: `spec_ref/group` takes an enum, not prose. |
| ui-smoke.mjs (/frontend-dev) | `portfolios <out>.png --select <firm> --fixtures <ref> --click <name> --fail <url>` | PASS | 7 screenshots produced and READ. Its existing `--select` / `--fail` flags covered the partner-scoped and forced-failure cases, so no bespoke script was written. |

**What worked:** `comp-find`'s denominator line and `proof-of-spec-check`'s printed alignment frame
both answer *what is this a count of*, which is the whole reason they are trustworthy. `ui-smoke.mjs`
already had every flag I needed — reading it saved writing one.

**What failed:** `comp-transform schema-check` on this page. Not a crash — an abort that returns a
clean-looking zero. It is the instrument-that-could-not-have-said-otherwise class, and it sat on an
acceptance criterion.

**Gap found:** two, both usage-shaped rather than tool defects. (1) `ui-smoke.mjs`'s click-failure
diagnostic prints `textContent` (`Models$1.47B`) while `--click` matches the ACCESSIBLE NAME
(`Models $1.47B`), so the printed names are not copy-pasteable as arguments — cost one failed run.
(2) `tsc --noEmit -p tsconfig.json` returns rc=0 in 0.5s because that config is `"files": []` plus
references — it checks ZERO files. Portal's own CLAUDE.md already records this; I hit it
independently and my handling matched the recorded law.

---

## Work Completed

### 1. SPEC-AT-PICKUP and the AC1 defect

Ran the TO's four oracles first. O-1 confirmed with positive controls on the same file
(`ModelPortfolios` 8, `total_aua` 4) so the zero was measured, not a pattern that could not match.

`D1R1DE-AC1` named `comp-transform schema-check` as its oracle. That oracle cannot fire on this
page. Routed BLOCKING × INERT to the issuer (66518); ruled same turn (66521): declare the response
types in `@/api/endpoints/aum` and let `bun run typecheck` be the exercised discriminator, proven
once with a mutant. The `comp-transform` call stays on record run-with-its-domain-disclosed.

### 2. Types + a three-state accessor (`760504f0`, `4034239c`)

`MdpfCategoryViews` and its node/member/child/held-axis types, shape taken from a real invocation of
`build_category_views()` — driven both ways — never read off prose. `getCategoryViewsByFirm()`
returns `{absent_by_scope | unavailable | ok}` rather than the file's usual `T | null`, because AC6
requires the consumed and no-block cases to be distinguishable and a bare null conflates *global
carries no object by ruling* with *the fetch failed*.

`4034239c` corrected a defect I had introduced: the contract moved and `nodes.SMA.aum` became
nullable. I had typed it `number`. A renderer trusting that formats null as `$0` — rendering "this
firm has no SMA" for a firm holding $22.9M.

### 3. The tree component and page consumption (`d1f8f38a`)

`CategoryViewTree.tsx` + wiring, own query key `['mdpf-category-views', effectiveFirmId]`. Built
around three rules, each a measured near-miss on this project: membership is never computed in the
renderer; absent / unavailable / zero are three distinct renderings; an unavailable predicate is
never `Unsupervised = 0`. `D1-inv-4` is computed from what is **on screen** and printed beside
`total_aua − Insurance`.

### 4. The SMA reversal (`cd2f059c`)

Andrew ruled only 49 Financial has SMAs. The `not-separable` marker therefore asserted hidden
dollars for firms with none — a false frame in the opposite direction from the one it prevented.
Path DELETED, not left defensive: a render path nothing can reach is how a false frame survives its
own correction.

### 5. Naming the plane (`7def244d`)

Reading the render showed Custom `$43,484,499.68` inches from three bare "not served" rows (0 of 3
served). Both halves true; the adjacency lying. Issuer-approved fix names the plane on screen and
keeps every member visible.

### 6. Proof instance + cell_status flip (`d708b02a2f`)

VALID rc=0. Two cells flipped deliberately narrow: `D1-c-1` is COMPLETE **at the contract plane**,
not from a served artifact (`D1-inv-5`: a commit is not execution); `D1-h-v2`'s Alternatives limb is
NOT-YET-EVALUABLE and declared rather than counted.

---

## Decisions Made

- **Three-state union over `T | null`** — deviating from house idiom, flagged to the issuer rather
  than left to be found, because AC6's discriminator depends on it.
- **`aum` typed `number | null` deliberately wider than the contract** — the field changed shape
  three times in one session; a null formatted as `$0` states a measurement nobody took.
- **Deleted rather than retained** the superseded not-separable path.
- **Did not invent field names** for `sma_separable` when COO named it but the registry had not
  minted it. Waited for the committed hash.

---

## Files Modified

| File | Commit |
|---|---|
| `portal/src/api/endpoints/aum.ts` | `760504f0`, `4034239c`, `cd2f059c` |
| `portal/src/components/CategoryViewTree.tsx` | `d1f8f38a`, `cd2f059c`, `7def244d` |
| `portal/src/pages/ModelPortfolios.tsx` | `d1f8f38a` |
| `.../deliverables/D1_CATVIEWS.TO-R1-DE_PROOF_OF_SPEC.json` | `d708b02a2f` |
| `.../task_orders/D1_CATVIEWS.TO-R1-DE.*.md` (cell_status) | `d708b02a2f` |

---

## Blockers

**None.** What remains before anyone but me can close this TO is a served-artifact read, which is
not mine and not this round.

---

## Current State

All 8 cells flipped, proof instance VALID rc=0, 7 screenshots read, `bun run typecheck` rc=0 at
`cd2f059c`. Portal `760504f0`/`4034239c`/`d1f8f38a`/`cd2f059c` on `origin/DEV`; `7def244d` and
workspace `d708b02a2f` LOCAL, riding integration. Awaiting CVO certification.

---

## Next Steps

1. CVO cert on the delivered proof instance.
2. If the Moderate Income ruling lands, cottonwood's `Models > Custom` moves off 0.00 and my L2
   gains rows with no render change — re-read the screenshot rather than assume it.
3. Two TO self-scan instances reported to the issuer (67764), not fixed: the stale "(Inflection
   today)" in the `D1-h-v4` cell description contradicting its own AC5, and the SMA row's four
   strategy-ids reading as render labels.

---

## Postmortem — one defect of mine, and one instrument I nearly trusted

**Defect:** I typed `aum: number` while the contract emitted `null`, caught only because I re-checked
at the ref after MSTR warned every seat that contracts were moving under them. Root cause: I
exercised the builder once and treated the shape as settled while the producing lane was still
working. Resolution: a field census across three variants, diffed against my declared types, now
part of how I retrack a contract.

**Nearly trusted:** I built a fixture by importing the registry from the shared working tree and got
a `render_state` value that existed at no commit — a peer had 33 uncommitted insertions in flight.
Checking the file's own state rather than its output stopped it. That became COO's standing rule
(evidence at a named ref), later widened to triggers — and under the widened form I disclosed that
my own start-condition detector had a working-tree-keyed `grep` limb, re-armed on committed state.
The generalisation failure is the part worth keeping: I applied the ref rule rigorously to fixtures
within the hour and did not carry it to my own detector, because *evidence* does not sound like
*trigger*.
