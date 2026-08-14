# 4.0.0_SA_CRO — recs executed: re-land + three passes to a filled served surface (16:55–17:20Z)

**archetype:** DEPLOY (with two DIAGNOSE interludes)

## Arc
Andrew "recs approved" (@9b816615f1) → Deploy_State confirmed (v2.2 @a72cf0ce99, W-03 closed) →
three /mdpf-refresh passes, each one honest instrument teaching the next step, ending with the 7
holes FILLED AND LABELED on the served surface, all scopes verified.

## The three passes (each green; two were green-about-the-wrong-thing)
- **Pass 1 (16:56Z):** green, "conflicts=0", holes unchanged → the lambda executes its PACKAGE
  (env pin bf74d031c1), not the loose script channel my comp-pipescript MATCH had verified — the
  sweep's own DECLARED-UNSWEPT rows named the gap (22a staged-vs-executing). Remedy: package
  rebuilt FROM PIN 5b00923c11 per the TF header protocol; first upload shipped the OLD zip wearing
  the new sha in metadata (caught on ContentLength ~90s, corrected, verified by download-and-hash);
  TF re-pinned @1dbf54a9fd; **apply via AE under CTO gate** (charter symmetry both directions) —
  applied 17:05:30Z, executing bytes byte-exact.
- **Pass 2 (17:07Z):** green, "conflicts=0", holes unchanged AGAIN → TWO defects measured:
  (1) my driver's conflict parse read `objects`/`rows`; the A6 manifest keeps rows under
  **`writes`** — a clean false zero while the guard held **12 keys** both passes (fix committed);
  (2) the lambda role lacked s3:GetObject on `reconstructed/*` — simulate implicitDeny beside an
  allowed positive control (separate single-ARN calls); in-lambda the EVR read AccessDenied and my
  fail-toward-gap catch served honest holes. Grant authored into GoldInputSilverRead @a1e73f080b;
  **applied via AE under CTO gate #2** with a full three-way simulate battery.
- **Pass 3 (17:16Z):** `--reland` listed the 12 (fixed parse) → `--reland --confirm` deleted them
  under Andrew's word → gold re-landed everything → publisher 14/14 (run 20260814T171628Z-43902a75)
  → **VERIFY: all four scopes as_of 2026-08-13 behind=1 fresh; inflection reconstructed dates
  served = the exact 7; fully-empty = []**.

## (d) evidence (sent to CTO 17:18Z)
Gold==platinum value-equality 7/7; platinum _provenance.source_keys names the re-landed gold key
(gold 17:16:26Z ETag 1dc6ddde → platinum 17:16:33Z ETag 1b4dc0a2); reconstructed(evr-1.0.0) labels
in cohort_provenance BOTH layers on exactly the 7; meta.reconstructed.dates identical across
layers; GLOBAL point_class 'reconstructed' only on 05-20 + 08-05, the other five correctly
interpolated_estimate by the weakest-component law (cottonwood band outranks), zero leakage.

## Instrument corrections (mine, both false-green shaped, both committed with mechanisms named)
1. manifest_conflicts read the wrong field → clean false zero over 12 held keys (the
   denominator-frame class, in my own tool, caught by reading the artifact).
2. _find_ssm_ref missed the accrual's `runner` key → pass 3 published ~1.4s before the accrual
   SSM's Success (17:16:31.599Z — harmless this run, measured; awaited from now on).

## Compiler Tools
comp-iam gaps (post iam.tf edit, per mandate) · simulate-principal-policy per 22a (single-ARN,
controls as separate invocations, both directions) · commit-gate ×3 · comp-pipescript deployed
(whose DECLARED-UNSWEPT rows named the pass-1 gap) · live primitives (lambda invoke ×6, ssm ×2,
s3 reads throughout) · lib/trading_calendar (serve-bar math).

## Open
- CTO serve-conformance close on the (d) pack (their word, expected same-turn).
- COO: RP-W7 TO disposition (supersede-with-pointer) + card close.
- Tags mdpf-pipeline-v2.1.2/v2.1.3 local at AE; push rides MSTR's integrator window.
