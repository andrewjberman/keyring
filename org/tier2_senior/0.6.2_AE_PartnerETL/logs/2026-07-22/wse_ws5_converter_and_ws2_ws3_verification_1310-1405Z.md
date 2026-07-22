# WSE_COTMDL -- WS-2/WS-3 verification, the 06:00Z alarm clear, and WS-5's converter half

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, IMPLEMENT, COORDINATE

**Agent:** 0.6.2_AE_PartnerETL~A · **Window:** 2026-07-22 ~13:10Z -> ~14:05Z · **TO:** WSE_COTMDL WS-5 (converter half)

## Summary

Spawned on Andrew's 1259Z ONE-FLIP directive to "get DE the real Rebalancer shape." **DE already had it** (WS-2 @bcd5ab971, WS-3 @449ef54aa, both landed on real bytes minutes before I loaded), so re-sending a shape doc would have been theatre. Verified his build instead, then took WS-5's converter half on CTO's ranking. Landed it, then found and fixed a live defect in my own landed commit.

## What I did

**1. Verified WS-2/WS-3 by exercise, not by reading.** Pulled the real 25 model_detail + roster JSONs from the 07-22 bronze pull and ran DE's own gold script dry-run against landed silver. **Dollar conservation exact: 126,381,228.84 (the 296 accounts' own holdings) vs 126,381,228.86 (dim sum) -- $0.02, pure per-row rounding.** DE's blend math creates and destroys nothing. Three findings the reconcile gate structurally cannot see:
- **F1** -- the entire Opal Satellite family (10 models, **288 of 296** assigned accounts) produces **ZERO** served dim rows; they decompose 100% into 5 building blocks. Spec-correct per Andrew's own count-vs-dollar rule, but the page will show "Opal Intermediate-Term 223 accts / $74.8M" and nothing for "Opal Satellite 50 / 82 accts" -- the name Cottonwood advisors use. **Surfaced, not adjudicated** (XXX.md). CTO carrying to Andrew.
- **F2** -- 3 `Sleeve - *` rows ($763,213.84, `is_opal=False`) reach the dimension. Mechanism I grounded and DE did not have: "Blended Opal / Satellite 50" carries FIVE children -- 2 primary Opal models AND 3 asset sleeves -- **all typed `rebalanceModelType='Model'`**, so the vendor's own type field cannot discriminate. DE accepted it as BINDING on WS-4 and will exercise the filter.
- **F3** -- count axis 1.51x (447 vs 296); correct by design, but any FE total summing the column double-counts.

**2. Corrected my own discovery deliverable @8fd4d2a94.** My sec-4 presented three hierarchy patterns as mutually exclusive. They are not, and `rebalanceModelType` does not discriminate a primary model from a sleeve. That error is what F2 grew out of -- DE built faithfully to a document that was wrong.

**3. Cleared a live alarm that had already reached Andrew.** 0.7.0 reported today's bronze carrying 02:00:4xZ mtimes against `cron(0 6)`, implying the producer never fired and that MSTR's unattended-fire citation was wrong. **It was `aws s3 ls` rendering LOCAL time with no timezone marker** (Eastern/DST, UTC-4), landing coincidentally on a real `cot-bd-session-daily = cron(0 2)`. Resolved on two instruments in different bases: ListObjectsV2 ISO8601 `2026-07-22T06:00:45.000Z` + CloudWatch (exactly one 07-22 stream, last event 06:00:49Z). MSTR had already relayed a retraction to Andrew; un-retracted. Now doctrine @18147abf0.
   Consequent sequencing correction, adopted verbatim by CTO and COO: 07-21 was my MANUAL deploy test, **07-22 was the first UNATTENDED fire and it PASSED** -- so the bronze leg is already proven and tomorrow's run re-proves the only green leg while staying silent on the two that are not wired.

**4. Retired the feed-liveness UNDETERMINED (COO Assignment 2), zero egress.** The vendor exposes `lastUpdate`, populated 60/60. Newest edit anywhere in the roster = `2026-07-20T19:17:49.973Z`, **before both pulls** -- so the 07-21/07-22 byte-identity is *explained by vendor content*, not merely unrefuted. The field demonstrably varies (spans 05-29..07-20), so it can fail, which is what makes the unchanged reading meaningful. Did not over-claim: a wholly frozen vendor would freeze this too; `accountCount`/`rebalanceAssignmentCount` are the sharper post-flip watch.

**5. Built WS-5's converter half** @228182599 -- whole-day completion-keyed convert + the sweep backstop, to CTO's ruling. Then **fixed a live defect in it** @7aa7e645f (below).

## The defect I shipped and self-reported

`manifest_body` asserts AC-6 parity on every `action=="converted"` result (`output == vendor + 5 riders`). My adapter emitted `converted` with the column census at its 0 defaults -> `0 == 0 + 5` -> **VendorDriftError on the first real conversion**, in both `run_event` and `run_sweep`, **after** the parquet landed. Live shape: correct data, failed run, retry, skip-idempotent, raise, **DLQ**. We would have shipped the remedy for a silent-failure gap and produced a loud failure on top of correct data.

**Why 30 green tests said nothing: every one called `convert_rebalancer_date` DIRECTLY.** Production runs `on_success -> lambda_entry -> run_event -> convert_rebalancer_day -> manifest_body -> write_manifest`. **I mutation-tested every gate inside the converter and proved each had teeth -- and the thing that broke was not a gate, it was the JOIN. I tested both ends of a seam and not the seam.**

Surfaced by grounding a claim I had *already sent* to 0.7.0 (that his exercise must assert `mode=="event"`). I had inferred that field from a call signature. Reading `manifest_body` to verify -- the claim held -- is what exposed the defect. Rule 22 paid for itself on a claim I was confident about.

Fix is an **explicit exemption, not a silent skip**: `parity_basis` defaults to the AC-6 law so every other family is bit-identical; rebalancer declares `declared_shape_equality`; the manifest **records** the basis. I rejected "skip when cols are 0" -- that fixes my bug by disarming AC-6 for orion/eclipse/etf.

## Two catches worth keeping

- **A shared vendored module's blast radius is invisible from the source file.** I first wrote a top-level `import rebalancer_conversion`. `mirror_conversion.py` is vendored FLAT into **four** Lambda packages -- that import would have raised `Runtime.ImportModuleError` in all four for a feed only blackdiamond converts, and the identical vendor-closure failure is already in the opal-assets CHANGELOG (etf leg-1). Lazy inside `_rbc()`: **blast 4 -> 1**, the other three structurally unable to break. Now doctrine 7c; gate candidate accepted.
- **`assertRaises` cannot tell you WHICH gate raised.** I mutated each gate in the source; `_reconcile_attested` disabled *entirely* left both its tests GREEN, because the mutations tripped *other* gates. Two tests named set-identity in their titles and tested something else. Rebuilt for isolation, all four mutants now caught. CTO merged it with DS's `ModuleNotFoundError` false-pass as one law: **a failure signal is not a reason.**

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-which` | Routed the S3 key-enumeration question; near-tie (comp-assets / comp-whoread), neither fit key enumeration -- used the native Grep tool rather than force a raw gated grep. |
| `comp-grep "_BD_RE" data/` | 2 matches / 1 file, scanned 1825 -- located `mirror_conversion.py` with systems context. |
| `comp-blast classify_key` | **NOT-FOUND over a stated 1442-node denominator. Did NOT read as a clear** -- the tool says so itself; re-ran against the Lambda node. |
| `comp-blast opal-assets-silver-blackdiamond` | 4 sibling Lambdas + opal-data-assets -- independently corroborated the BUILD_MANIFEST coupling that drove the lazy-import decision. |
| `commit-gate.sh` | Clean 4/4 then 2/2 (py_compile + ds-precommit + ruff). |
| `vendor-manifest.sh` + `--check` | Materialized closure; **parity 7/7** both before and after the fix. |
| `safe-commit` surface-check / risk-reflex | CLEAN; risk-reflex HOLD on `lambda-source-map.json` read (untracked-production-source-file citation) -- my change *adds* tracked files to it, which is the side that citation wants. |
| pytest | 261 -> **267 passed / 10 skipped** (full silver suite, all families). |
| Live primitives | ListObjectsV2 (ISO8601 UTC), CloudWatch `describe-log-streams`, `s3 cp` -- the two-instrument basis for the alarm clear. |

**What worked:** exercising rather than reading, every time -- DE's gold script dry-run, the mutation passes, the old-vs-new classifier census over 5,841 live keys. **What failed:** my own test suite's scope (both ends, not the seam), and a cwd that drifted into `data/assets/scripts/silver` and made relative paths resolve one level deep -- I nearly filed a false "file deleted" finding off it before checking `pwd`. **Gap:** none open on my side.

## Current state

- **@228182599** WS-5 converter half; **@7aa7e645f** the AC-6 fix. Both pushed. **NOT DEPLOYED and no deployed claim made.**
- Blast denominator measured: **62 of 5,841** live bronze keys changed, all rebalancer; controls (outside `/rebalancer_`, orion|eclipse, `.xlsx`) each **0**; 30 legacy markers still `legacy_marker`. 897 `.json` live under those prefixes vs 62 rebalancer -- the justification for structural rather than suffix exclusion.

## Next Steps

- **[0.7.0_AE_CloudOps]** owns the `on_success` TF + the `lambda:InvokeFunction` grant on `cot-rebalancer-runner-role` (implicitDeny, verified isolated) + the exercise. **Both in one apply in the opal-assets root** -- destination-without-grant fails SILENTLY. **Exercise must assert the manifest's `mode=="event"`**: my sweep backstop can otherwise mask a broken destination, since the parquet lands either way.
- **[1.0.0_SA_CTO]** F1 carried to Andrew -- cheap today, expensive once the page renders.
- **[0.4.0_DE_ClientPlatform]** F2 binding on WS-4's fold; conservation adopted as a standing gate.
- **[self]** reachable; converter half complete pending 0.7.0's exercise.
