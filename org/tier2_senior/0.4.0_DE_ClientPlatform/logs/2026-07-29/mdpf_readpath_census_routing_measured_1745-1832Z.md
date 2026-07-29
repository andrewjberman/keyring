# MDPF read-path census: CTO's deploy INVERTED, then the routing MEASURED — 1745–1832Z

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, COORDINATE

Continues `mdpf_blend_revert_shipped_gap3_design_1625-1745Z.md` (@`74228b2bf5`).
**Zero commits this window** — it was measurement, rulings and cross-lane resolution. Deliberate:
CTO froze build, and the one design I would have written was blocked on an unmeasured premise.

## What came in

**CTO explicit dispatch 174131Z** — a read census unowned for 75 minutes, gating a deploy word:
*does ANY live consumer read `json/portfolios/aum-timeseries.json`?* That key's Stage-3.5 write is
IAM-denied, so it is FROZEN since 2026-07-27T15:10Z with its frontier model leg
**~$121,868,077.28 BELOW canonical.** He demanded predicate + denominator, indirect consumers
included, and *"if the honest answer is UNDETERMINABLE, say that — do not manufacture a clean
negative."*

**Andrew-direct, two corrections at my terminal** (~1755Z / ~1800Z), verbatim:
- *"the portal should never be calling from opal-data-assets"*
- *"all the /json paths are deprecated for the mdpf files in question. Other paths for mdpf are only
  relevant if its peers or benchmark data. the aum-metrics, account-distribution, and
  aua-aggregate-timeseries json files are all to be pulled from opal-data-portal-v2/platinum/"*

He was explicit this does **NOT** go in XXX.md — working guidance for those on MDPF now, not law. So
it was passed to DS~A + DT and used, not formalized.

## The census — answered YES, and wider than asked

PREDICATE: **symbol-traced fetcher→callers hop by hop, not string-matched** (this morning's
`getNonModelAssets` lesson: the string was in 10 places and the function had ZERO callers, so a
literal match answers the wrong question in *both* directions). DENOMINATOR: 404 of 404
`portal/src` files, every pass. SCOPE BOUND: `portal/src` only; non-portal consumers not claimed.

```
/api/general/portfolios/aum-timeseries.json   LIVE  portal-proxy.ts:334 getAUMTimeSeries()
                                                    <- endpoints/aum.ts:443 wrapper
                                                    <- endpoints/aum.ts:322 model extraction
                                                    <- ModelPortfolios rawTimeSeriesData
                                                       (RESTORED as graceful-degrade fallback trend
                                                        source + Q-end priorLevels -- NOT orphaned)
/api/general/portfolios/aum-metrics.json      LIVE  getAUMSummary() -- and imported DIRECTLY by
                                                      Attribution/tabs/SelectionTab.tsx:89
                                                      Positioning/tabs/HoldingsTab.tsx:564
                                              LIVE  getAUMMetricsWithCalculations() <- aum.ts:385
/api/general/portfolios/non_model_assets.json DEAD  ZERO call sites (the negative control proving
                                                    the predicate discriminates live from dead)
```

Two client-facing pages outside the MDPF lane's footprint consume the deprecated family directly,
bypassing `endpoints/aum.ts`. **Found while establishing the denominator, not asked for** — the
argument for stating denominators.

## CTO 180504Z — THE DEPLOY INVERTED

He was 30 minutes from wording the retirement pair (32e953198a + ca3739c2fc). Ruling: **retirement
pair STAYS HELD, and for a stronger reason than the hold was placed.** Retiring the writer would
*"convert a stale-but-repairable artifact into a permanently frozen one, with a live consumer still
reading it, and the rc=1 that currently advertises the problem would go silent."*
**RULED SEQUENCE: RE-POINT → VERIFY → THEN RETIRE.** Retirement is last and only safe once nothing
reads the frozen key.

## Then I found a bigger premise problem — and corrected myself

`endpoints/aum.ts:557-560` (dated MDPF_3FIRMS.3F-P3a, 2026-07-23) states
`/api/general/mdpf/{firmId}/aum-metrics.json -> s3 json/mdpf/{firmId}/aum-metrics.json` — **a /json
path**, i.e. the MDPF family everyone treats as modern might *also* be deprecated. Raised a
**mixed-state hypothesis** (aggregate repointed, aum-metrics not) and stopped CTO before he sequenced.

**SELF-CORRECTION, and CTO called it the sharpest self-catch of the day.** I had told DS~A the
cottonwood platinum object was "exactly right" under Andrew's rule. What I had actually done was read
`platinum/mdpf/cottonwood/aum-metrics.json` and find clean current data.

> **That proves the OBJECT EXISTS AND IS POPULATED. It does NOT prove the PORTAL READS IT.**

Object-exists and portal-reads-it are different claims and I collapsed them — on the adjacent family,
in the same hour I correctly flagged the identical URL-vs-KEY confusion for `aum-timeseries`. CTO's
generalization: *"a true measurement of the wrong proposition."* Corrected to both CTO and DS~A before
either built on it. **CTO SUSPENDED his 180504Z sequencing** — the priority order had been a guess on
a possibly-wrong denominator.

## THE MEASUREMENT — hypothesis REFUTED, frozen key CONFIRMED

CTO required two independent instruments and *"do not resolve this from comments, and do not resolve it
from object existence."*

**Router source, `infra/aws/lambda-edge/public-data-router/index.mjs` — order was the entire crux:**
```
if      /api/general/json-tiered/  -> /json-tiered/
else if /api/general/json/         -> /json/
else if /api/general/mdpf/         -> /platinum/mdpf/    <- Special case 3 (WO-3 re-point)
else if /api/general/              -> /json/             <- fallback, evaluated AFTER
```
Had the fallback come first, mdpf would land on `json/mdpf/` exactly as the comment claimed.

**`comp-routes trace`, exact URIs:**
| Portal requests | Resolves to |
|---|---|
| `/api/general/mdpf/cottonwood/aum-metrics.json` | `s3://opal-data-portal-v2/platinum/mdpf/cottonwood/aum-metrics.json` |
| `/api/general/portfolios/aum-timeseries.json` | `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json` |

**ALL FOUR MDPF paths resolve to `platinum/mdpf/`** — `aggregate-aua-timeseries` (global + per-firm),
`account-distribution`, `aum-metrics`. **And the non-model series is NOT a separate fetch** — it is
the `non_model_aua` FIELD inside `aggregate-aua-timeseries`, so it rides the platinum path.

**MY MIXED-STATE HYPOTHESIS IS REFUTED, NOT NARROWED.** The artifacts three agents spent today
root-causing ARE the ones the page reads; the cottonwood arc does not reframe.
**CTO's frozen key is CONFIRMED at the KEY level** — the live 3-hop chain terminates on the exact
frozen path, so re-point-then-retire rests on measurement, not URL-naming inference.

**THREE LOAD-BEARING COMMENTS LIED TODAY, all in one file family:**
| Comment | Claim | Truth |
|---|---|---|
| `ModelPortfolios.tsx:529` | legacy fetch "DELETED (~0340Z)" | true of ONE leg, false in general |
| `ModelPortfolios.tsx:523-525` | "served from opal-data-assets" | Andrew: portal never does — and it invokes HIS name |
| `endpoints/aum.ts:557-560` | `-> s3 json/mdpf/...` | router says `platinum/mdpf/` |
Each would have produced a different, wrong decision.

## Verify — how far the APPLIED gap is closed, honestly

- `comp-routes` is **DESIRED plane** (parsed TF + committed router source), never a live
  `describe-distribution`. Its own disclosed risk: *"a pinned stale Lambda@Edge version reads
  identical here."*
- **I checked that axis:** `comp-routes edge-versions` — all 5 routers incl. `public-data-router`
  bound **DYNAMIC via `qualified_arn`, auto-updating on apply, all [OK]. No pinning**, so the
  specific invalidating failure mode is excluded. **Not a full APPLIED proof and not called one.**
- **Independent runtime corroboration (DS~A's, different plane):** legacy holds 47/47/56 and would
  render a visibly RICHER chart; platinum holds 2/0/0; **Andrew observed the EMPTY band.** Two
  candidates predicting OPPOSITE observable outcomes, only one matching — a genuine discrimination,
  and it reached the right answer before the route trace existed.
- **Three instruments, three planes, one answer.** Residual: a live `describe-distribution` /
  deployed-edge fetch. Offered to CTO; judged low-yield with no pinning, not closed silently.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-routes rewrites` | **PASS — decisive** | the 13-rule URL→S3 table; gave both mappings at once |
| `comp-routes trace` (x2) | **PASS — decisive** | exact S3 URIs for the mdpf and portfolios paths; also auto-caught an MSYS leading-slash mangle and reported the corrected arg |
| `comp-routes edge-versions` | PASS | the pinning axis — 5/5 DYNAMIC, closes the disclosed DESIRED-plane risk |
| `comp-grep` (x6) | PASS | the census: fetchers, callers, re-export/barrel check, `NOT_MEASURED` (1 hit, a comment), mdpf-family paths — denominator printed every call |

**What worked:** `comp-routes` was the right instrument and its **self-disclosed COVERAGE/BLIND
header did real work** — it named the DESIRED-plane limit and pointed at `edge-versions` as the axis
to check, which is how the applied gap got narrowed instead of hand-waved. A raw grep of the router
would have given the same if/else text with none of that framing.
**What failed:** nothing this window.
**Gap found:** none new. Prior window's two `comp-which` gaps stand.

## MCP traffic

10 handled. Significant: CTO 174131Z census dispatch → answered 180316Z; CTO 180504Z **deploy
inversion**; my 180830Z stop-before-you-sequence + self-correction → CTO 181924Z **sequencing
SUSPENDED**; DS~A 181922Z negative-control narrowing; my 182934Z **measurement closing it**;
corrections/closes to DS~A (180858Z, 183003Z) and FYIs to DS~A + DT carrying Andrew's guidance.

## Blockers

None assumption-based. All build work **frozen by CTO** (181924Z: *"Design and measure only. The
wave, the accrual overwrite, and the audit unwedge are ahead of this."*) — an explicit, evidence-cited
hold with a named owner.

## Current State

- **Read paths MEASURED and settled.** MDPF family (4 paths) → `platinum/mdpf/` ✓ (Andrew's rule
  already satisfied). Legacy `/api/general/portfolios/*` → `json/portfolios/*`, and
  `aum-timeseries.json` is CTO's frozen key with a live 3-hop reader.
- **Exposure is the legacy `portfolios` family only** — 3 readers, 2 of them direct imports on
  Attribution + Positioning. NOT the MDPF family. CTO's sequencing can resume on this denominator.
- **Retirement pair (32e953198a + ca3739c2fc) HELD** on CTO's word; sequence is re-point → verify →
  retire.
- Design docs: `MDPF_COTTONWOOD_PROVENANCE_RENDER_DESIGN_20260729.md` @ `298f96dd54` (3 gaps, both
  cross-lane rulings, gap-3 design). **Its pre-addendum citations are @`b0fc1e75`; head is now
  `a969d615` (+45 lines) — re-locate by symbol, never by line.**
- Cross-lane state with DS~A unchanged and confirmed: enum `absent` + sibling field, (A) on the 32
  dates correct-until-my-step-2, they want a ping when steps 1-2 land. Their R5 no-clobber item now
  matters MORE — platinum is the served plane, so 2/450 → 50/450 is a visible client change.
- Nothing built. No re-point design written — writing one against an unmeasured source would have
  baked in the assumption CTO's item 1 exists to prevent. Now measured, so it is unblocked on his word.

## Next Steps

1. **[1.0.0_SA_CTO]** resume sequencing on the corrected denominator (legacy `portfolios` family
   only); then his word on the re-point design + whether to close the residual live-edge fetch.
2. **[0.4.0_DE_ClientPlatform]** on his word: re-point design for the `aum-timeseries` reader
   (platinum-sourced, field-read only) + the two extra readers scoped SEPARATELY with their own
   exposure statement (CTO: do NOT bundle into cottonwood).
3. **[0.4.0_DE_ClientPlatform]** on unfreeze: gap 3 → gap 1 → gap 2, each with a READ headless
   screenshot.
4. **[0.4.0_DE_ClientPlatform]** on next touch of `ModelPortfolios.tsx` / `endpoints/aum.ts`:
   **DELETE** the `NOT_MEASURED` comment (`:304`) and **FIX all three lying comments** above — they
   are load-bearing and each has already misled a decision.
5. **[0.4.0_DE_ClientPlatform]** ping DS~A when steps 1-2 land → flips their (B) from deferred to
   correct.
