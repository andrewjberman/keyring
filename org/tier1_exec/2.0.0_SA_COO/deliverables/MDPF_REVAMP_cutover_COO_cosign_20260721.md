# MDPF_REVAMP Cutover — COO Co-Sign Record (never-widen control)

**Signer:** 2.0.0_SA_COO · **Date:** 2026-07-21 · **Control:** never-widen serve-move (CTO+COO+Andrew co-sign)
**Trigger:** Andrew-direct PUSH-NOW (via CTO 180314Z) — S5 cutover on verified cycle-1 artifacts, rollback-armed,
NOT waiting for the scheduled streak. Andrew VERBATIM: push it, "be ready to roll it back immediately if it doesnt work."
**Package reviewed:** org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_REVAMP_cutover_cosign_package_20260721.md (@2e9a118f8)
**This record:** my MCP co-sign 180626Z + CTO acceptance 180814Z, captured durably (record-survives-session).

## STATUS UPDATE 2026-07-21 ~18:12Z — CO-SIGN HELD / RE-OPENED (do not read the GRANTED below as live)

PUSH HELD on a MATERIAL finding (CTO 181202Z; AE serving-path grounding). Two changes:
- **Mechanism corrected:** the FE reads `opal-data-portal-v2` via the public-data-router, NOT
  opal-data-assets. Cutover = a router origin-REPOINT (mechanism A), not the publisher copy this record
  originally co-signed. A is BETTER for condition-1 (router revert-to-legacy leaves the legacy artifact
  untouched = cleanest tested-rollback).
- **Potential DEFECT outside this co-sign:** the FE's AUM-Daily source appears to be `platinum/mdpf/`
  (443K/541d); the 3-way parity was against `json/mdpf/` (429d). The revamp global is 165K/427d — a 62% /
  ~114-day gap. If that is MISSING REAL HISTORY (not re-encoding) it is a TRUNCATED CHART = a DEFECT, and
  this co-sign attested "none a defect" — so it does NOT authorize publishing that artifact.

Added pre-push conditions (CTO 4+5, on top of my 1-3): (4) LIVE-trace which artifact the FE reads + why the
gap (Verification-Law-6 axis check: ground the artifact AS THE FE READS IT); (5) /frontend-dev render-check
proving full-depth clean render off the revamp before live. **RE-CONFIRM REQUIRED:** COO GO on publish is
withheld until 4+5 clear clean AND I re-confirm this co-sign against mechanism A + the actual FE-read
artifact. Missing real history -> FIX first, re-co-sign against the fixed artifact. The GRANTED verdict below
applies to the 5 verified items only; it is NOT a live authorization to publish while the artifact question
is open.

## ETAG-PIN 2026-07-21 ~18:43Z (CVO catch) — co-sign covers the SERVING ETags ONLY

CVO grounded (head-object) that the gold/mdpf_revamp/ spine RE-STAGED at 18:21Z with NEW ETags (49F
6e072745->933318c2, infl a9778de4->f3fd7af2, global 7d574a2d->53b732b2, +86..+899B) — AFTER the 3-pass +
this co-sign. This co-sign is PINNED to the PACKAGE ETags (6e072745-era) and does NOT cover the re-staged
bytes. Grounded likely-cause (git 82c4d1ec6): the item-4 account_count-WIRE landing (account_count WIRED,
"other 6 data arrays + model_value byte-IDENTICAL", counts tie) — an EXPECTED co-signed change, but a commit
message is a self-report, not the served bytes. HARD GATE folded into the re-confirm: (1) DS states the
re-stage delta = item-4 only; (2) CTO re-runs the 3-pass on the ACTUAL serving bytes (also discharges
condition-2 seam-continuity); (3) COO RE-PINS this co-sign to the EXACT ETags serving at serve-time. Never
serve an ETag no completed control covers. **Full re-confirm = DE-align + render-check + 3-pass-on-actual-
serving-bytes + ETag-pin.**

## ETAG-PIN RESOLVED + RE-PINNED 2026-07-21 ~18:51Z

Chain-of-custody hard gate DISCHARGED. The full 3-pass now covers the EXACT serving ETags
(933318c2/f3fd7af2/53b732b2): CTO S3 re-verify (6-array anchors match to the cent: 49F model
$1,397,277,094.44 / custody $1,665,338,126.76; inflection model $137,773,262.95 / custody $202,375,944.55;
global model $1,535,050,357.39 — all == prior verified) + DT aggregate 3/3 (@80bf482d5) + CVO from-scratch
byte-diff (data byte-identical). The 18:21Z re-stage was account_count-only among the data arrays,
streak-neutral, INDEPENDENTLY confirmed. **Condition-2 DISCHARGED:** account_count ties served EXACT (49F 7/7,
infl 7/7, global 9/9, 0 non-tie @07-17) — seam-continuity EXERCISED on the actual bytes.

**CO-SIGN RE-PINNED to 933318c2/f3fd7af2/53b732b2.** Data + byte dimension SOLID. Full delta vs the original
signed bytes = account_count wire (item-4, verified) + generated_at (benign) + source_vintage_last
skeleton->'current' (benign metadata, TO-5-deferred field; CTO intent-confirm PENDING — non-blocking, not a
defect). PIN DISCIPLINE: serve ONLY these covered ETags; any re-stage before the repoint -> fresh 3-pass +
re-pin.

**PUBLISH GO STILL HELD on (not the data/byte dimension):** condition-1 rollback tested-armed (AE) +
condition-5 DE FE-alignment + /frontend-dev render-check + post-cutover cycle-1 verify-before-serve (adopted)
+ CTO GO on the CF/L@E/OAC repoint + the TO-5 vintage-block intent-confirm. Condition-3 (TO-2) = my ongoing
post-cutover track.

## SCOPE 7 -> 9 KEYS + CENSUS-GATE 2026-07-21 ~19:25Z (Andrew-direct expansion)

Andrew caught an UNDER-SCOPE (CTO 192509Z, source-confirmed): leaving aum-metrics.json + aum-timeseries.json
on legacy portal-v2 (my item-1's accepted interim) yields a MIXED-BASIS Global enterprise Total
(ModelPortfolios.tsx:745 = legacy-model aum-timeseries + revamp non_model) — concretely WRONG (+$20M D-2
basis), not just stale. So:
- **CUTOVER IS NOW 9 KEYS** (aggregate x3 + account_distribution x3 + non_model + aum-metrics + aum-timeseries).
  My co-sign coverage + the 3-pass extend to all 9.
- **ITEM-1 RESOLVED-BY-INCLUSION:** TO-2 (aum-metrics/aum-timeseries off the revamp aggregate) is PULLED
  FORWARD into this cutover — supersedes my item-1 "interim dual-read accepted" (strictly better; the residual
  I tracked as condition-3 is now fixed BEFORE the flip). Producers: DS builds the 2 new gold shapes
  (field-identical to AUMMetricsResponse + AUMTimeSeriesResponse); AE extends the S4 runner + 9-key route.
- **FLIP NOW HELD ON A COMPREHENSIVE CENSUS** (Andrew-direct "confer with CVO... get to the bottom of what the
  REVAMP still does not cover... be comprehensive"): CVO + CTO jointly produce ONE cross-verified census (every
  FE fetch -> serving source -> revamp-covered? -> disposition), independent + reconciled. No flip until closed.
  Render-check already surfaced more than the 2 aum gaps -> content items A (inflection model_value post-onset
  None gaps, DS/Eclipse) + B (account_count MIDDLE Dec31/Jun30 gaps, all firms — DS GROUNDS real-vs-fill per
  Rule 22 BEFORE ruling). Both routed to DS, feed the census.

**Revised pre-push gate:** comprehensive census CLOSED (CVO+CTO) + 9/9 3-pass (incl. the 2 new producers,
field-identity verified) + content A/B resolved + render-check clean + AE router-revert TESTED-armed + my
re-co-sign on the FINAL 9-key coherent ETags. "Nearly there" is RESET — real producer + census work first.
CTO single tracker-writer records the 9-key scope + census-gate.

## COHERENT-9 RE-PIN — CORRECTED 2026-07-22 ~00:00Z (CTO pin-discipline catch + my live ListObjectsV2 ground)

My earlier staged pin was STALE + INCOMPLETE — the EXACT discipline this record enforces, caught by CTO's live
S3 re-verify. It cited the PRE-cohort_provenance aggregate ETags (8c0f8e45/2fda9d52/1b53f85b @165b84ac4) + the
PRE-decouple A4 (d4802341), and listed only 7 keys (omitted A1/A2). CORRECTED by grounding on the LIVE
ListObjectsV2 ETags (my own read of opal-data-assets/gold/mdpf_revamp/, APPLIED TRUTH — not a manifest
transcription), which match CTO's S3 re-verify + CVO re-derive @233355Z EXACTLY.

**CO-SIGN PINS to the CURRENT coherent-9 (live-verified ETags):**
- aggregate: 49f `a2e87f311fd0` / inflection `7ab6e93e3f3a` / global `1b52211f6443`
- non_model A4 (global/non_model_assets.json): `7ef321124087`
- aum-metrics A1 (portfolios/aum-metrics.json): `d69ac96ab99a`
- aum-timeseries A2 (portfolios/aum-timeseries.json): `38e9e8d46678`
- account_distribution: 49f `865919f2be40` / inflection `afb964c4d67f` / global `b946d8364ca3`
(`non_model_assets_precutover_frozen.json` da2260f6 = the A4 frozen pre-cutover boundary artifact — supporting,
NOT one of the 9 served keys.)

The data-neutral re-stage moved the ETags (cohort_provenance 0->populated + A4 decouple) but not the DATA. The
final re-co-sign confirms the 9/9 3-pass covers THESE exact 9 + render-check clean + AE router-revert tested.
Lesson re-banked (on myself): ground the pin on the LIVE object, never a message/manifest transcription.

## FINAL RE-CO-SIGN -- GRANTED 2026-07-22 ~00:56Z (all held conditions met; CTO gate DECLARED @005544Z)

COO limb of the never-widen CTO+COO co-sign: **GRANTED.** Every condition I held this co-sign on is now
satisfied against LIVE / independently-verified truth -- not a self-report:

1. **SCOPE** -- exactly the coherent-9, NO widening beyond it. Legacy opal-data-portal-v2 untouched
   (byte-identical revert available). account_dist replace-lane drift UNGATED (CTO ruling 1).
2. **PIN** -- the live-verified coherent-9 (my OWN ListObjectsV2 @ opal-data-assets/gold/mdpf_revamp/,
   char-for-char == CTO S3 re-verify + CVO re-derive + DT + DE md5):
   aggregate 49f `a2e87f311fd0` / inflection `7ab6e93e3f3a` / global `1b52211f6443`; A4 `7ef321124087`;
   A1 aum-metrics `d69ac96ab99a`; A2 aum-timeseries `38e9e8d46678`; account_dist `865919f2be40` /
   `afb964c4d67f` / `b946d8364ca3`.
3. **VERIFICATION** -- 3-pass 3/3 CLEAN: CTO S3 re-verify + CVO from-scratch re-derive + DT date-joined
   parity @93382362c (NAMED_DELTA_PASS / 0 unexplained).
4. **RENDER** -- CTO INDEPENDENTLY verified all 6 cells (read the durable screenshots himself, not DE's
   claim): no picket-fence, no frontier drop-to-zero, no mixed-basis Global Total (headline=aggregate-primary
   $1.81B, aum-timeseries priorLevels-only); Inflection pre-onset HONEST; totals tie exact ($1.81B / $1.68B /
   $202M); frontier-count coherence EXACT (7560 / 7026 / 534). Vintage == the coherent-9.
5. **ROLLBACK** -- LOCKED, ARMED + EXERCISED BEFORE PUBLISH (my explicit held condition): router-revert +
   negative control (a legacy /api/general/* key NOT in the 9 stays portal-v2 before/during/after). The
   condition I held the co-sign on is met.

**This co-sign authorizes GO-TO-APPLY** (the AE scope-isolated apply of the Option-C exact-9 CF behaviors).
The IRREVERSIBLE serve-widen -- the repoint -- remains gated by CTO's portal-auth FINAL GO with Andrew
surfaced; this co-sign does NOT skip that gate. Two of three never-widen limbs now signed (CTO declaration +
COO co-sign); Andrew's limb is at CTO's final-GO surface.

## ROLLBACK + STRENGTHENED RE-FLIP GATE (post-flip P0 data bug; 2026-07-22 ~04:00Z)

The FINAL RE-CO-SIGN above was GRANTED and the flip fired -- then HALF-LANDED (data live + FE-unpromoted
picket-fence) and Andrew caught a P0 DATA bug: the Global aggregate EXCLUDES Inflection non_model. CVO's
from-scratch Layer-3 enterprise re-derive (grounded on the co-signed ETag `1b52211f6443`, lastmod
2026-07-21T23:30:25Z) then found the exclusion is SYSTEMATIC: `opal_aggregate_aua != model_aua + non_model_aua`
on **421/421 headline dates** (2024-11-01..2026-07-20), miss == inflection non_model exactly, ~$151M-203M/date.
**The exact artifact I co-signed as "3-pass 3/3 CLEAN" was holed on EVERY date.** The 3-pass passed because it
checked PARITY-to-baseline, not INTERNAL CONSISTENCY (total==components) -- the axis none of CTO-S3 /
CVO-re-derive / DT-parity read. CTO rolled back to known-good; this co-sign's GO-TO-APPLY is SPENT/VOID (the
artifact is defective), and the 0159Z 3-limb co-sign is VOID for any re-flip (data changes -> ETags move ->
FRESH co-sign required).

**RE-FLIP RE-CO-SIGN HARD GATE (strengthened; I will NOT re-co-sign without ALL):**
1. DS Global TOTAL-FIELD (opal_aggregate_aua) COMPOSITION fix, FULL-SERIES (all 421 dates, NOT a spot/window
   fix) -- gated on Andrew's A/B basis call. NOT a firm-sum fix (firm-sums are CORRECT).
2. THREE independent, complementary, EXERCISED consistency layers, each covering the FULL 421-date series
   per-date all-firms with a PRINTED coverage denominator (must read 421/421, so zero-coverage can't pass):
   (1) DS producer-validate (refuse-to-emit-inconsistent + SMA coherence, pre-publish);
   (2) DT harness-gate (mutant-exercised: seeded hole -> RED; sensitivity-floor reported; absent!=zero);
   (3) CVO Layer-3 from-scratch re-derive (demonstrated-RED on the seeded Inflection hole).
3. FE @aa8c0420 promoted FE-FIRST (ordering fixed).
4. FRESH never-widen co-sign (CTO+COO+Andrew) pinned to the CORRECTED data's NEW ETags + Andrew eyeball.

STANDING lesson banked: parity is not consistency; a total must be checked against its own components
(EXERCISED, with a mutant + a printed denominator), not just against a prior vintage. A rigorous instrument on
the wrong axis survives review -- three did, on an artifact holed 421/421.

**CORRECTION (my OWN grounded re-run of DT's gate @3e557741e vs LIVE S3, 2026-07-22 ~04:07Z -- correcting two
briefings I'd propagated without grounding):**
- **(1) The Global inconsistency is PRE-EXISTING, not a revamp regression.** `--consistency --served` (legacy
  live) is holed **429/429 dates** too (back to 2024-11-01, hole $64M-$204M). Rollback clears the FE
  picket-fence and HIDES the inconsistency (the legacy FE doesn't display components beside the total); it does
  NOT fix the data condition. My earlier "rollback clears the Global bug, known-good" was WRONG on the data.
- **(2) The fix is the TOTAL-FIELD COMPOSITION (opal_aggregate_aua), NOT the firm-sum.** CROSSFIRM_PASS:
  global.model_aua & global.non_model_aua each == 49f+inflection at every date. Briefing DS to a "firm-sum fix"
  sends them after a component that never broke.
- The revamp FIXES a legacy 49f defect (legacy 49f holed 2025-12-26 -$43.16M; staged passes). Also-unowned:
  staged inflection has 3 PARTIAL_NULL dates (custody populated, both components None) -> joins gate item 2.
- => the A/B basis call reframes: is the LONG-STANDING exclusion of inflection non_model from opal_aggregate_aua
  INTENTIONAL (a basis choice) or a defect? That is Andrew's decision, and it is NOT a revamp-introduced bug.
- METHOD note to self: I propagated both errors by inheriting a framing instead of grounding it -- the SAME
  transcription failure as the stale pin. Ground the claim on your own run, then state it.

## RE-LAND STAGED CO-SIGN -- DATA-GATE INDEPENDENTLY VERIFIED ON MY OWN RUNS (2026-07-22 ~05:55Z)

CTO: re-land DATA GATE PASSED (B-basis fixed data, frozen c27e1f37 set, 3 battery legs green + CTO HeadObject
same-set). Per the lesson (I transcribed a stale pin + rested on an unverified data gate the first time), I
grounded my OWN limb BEFORE staging -- not CTO's evidence:

**MY OWN GROUNDING:**
- ListObjectsV2 opal-data-assets/gold/mdpf_revamp/ -> the 6 composition-affected keys CHANGED (fixed, lastmod
  05:23Z today), the 3 account_dist keys UNCHANGED (correct -- the composition fix did not touch them). New
  coherent-9 pin:
    aggregate: 49f `aa5c5b85` / inflection `cec5a0d6` / global `c27e1f37` (== CTO's named frozen set; != the
      holed `1b52211f`)
    A4 non_model: `8a195549` | A1 aum-metrics: `529b7c21` | A2 aum-timeseries: `f2c03476`
    account_dist: 49f `865919f2` / inflection `afb964c4` / global `b946d836` (unchanged, composition-independent)
- Ran CVO's mutant-proven Layer-3 gate (@f3c202256) MYSELF vs the live c27e1f37 data: **GATE VERDICT = PASS**
  (B-basis enterprise composition consistent; denominator global_dates=427 checked=421 honest_none_verified=6
  absence_agreement_checks=1281). Self-test first confirmed instrument integrity (clean-B PASS + fold-in / drop /
  unverified-None / partial-row RED). MY OWN run, not transcribed.
- B-basis resolved (Andrew A/B ruling): non_model == 49F-only; inflection cohort-2b EXCLUDED from headline. The
  total now ties its stated components -> internally consistent. The exclusion is an INTENTIONAL BASIS
  (Andrew-ruled), NOT the earlier defect (which was total-vs-displayed-component mismatch).

**CO-SIGN STAGED, pinned to the new coherent-9 above.** FIRES when CTO brings the COMPLETE assembled package:
data-gate evidence (independently verified above) + FE-assembled (DE 2x + content-A/B, DEV-surface-green) +
ROLLBACK-ARMED-BEFORE-PUBLISH + publisher/routing plan + FE-FIRST ordering (the half-landed lesson). Then
CTO+COO co-sign -> Andrew sovereign limb -> verify-before-serve cycle-1. New re-land ledger (per AE); the
mdpf-exact9-cutover ledger closes as rolled-back.

## Verdict (as-of 180626Z, now HELD per above): CO-SIGN GRANTED — conditional on tested-rollback-before-publish

All 5 cutover items independently verified NAMED + CORRECT serve-real, none a defect:

| # | Item | Verify |
|---|---|---|
| 2 | A4 pre-cutover verbatim-passthrough boundary @2025-12-22/23 | Clean by construction (frozen legacy rows not monolith-derivable); post-cutover ties $0.00 all windows (~A-verified). CO-SIGN. |
| 3 | 2026-05-21 legacy-imputed -> honest None (value disappears) | Served value was FABRICATED (eclipse feed never carried 05-21; bronze+silver both lack it). Honest None = serve-real-correct. CO-SIGN. (visible) |
| 5 | inflection 05-15 launch onset (model turns on 3 trading days earlier) | Andrew-ruled (model=0 until 05-15); clean seam 0@05-14 -> $94.5M@05-15; CVO-confirmed. CO-SIGN. (visible) |
| 4 | account_count PRESERVE (None -> wired to real at cutover) | Counts not lost; wire to real (==served exact tie) at cutover. CO-SIGN, cond. seam-continuity EXERCISED. |
| 1 | dual-read + $10-20M Q-end drift | Drift PRE-EXISTS cutover; cutover swaps one source to more-correct revamp; TO-2 kills it. CO-SIGN interim, cond. TO-2 tracked. (visible) |

## Conditions (adopted by CTO 180814Z)

1. **ROLLBACK TESTED-ARMED *BEFORE* PUBLISH** — sequencing catch: CTO's original "publish -> rollback armed" had
   the order wrong. CORRECTED: co-sign complete -> AE EXERCISES the revert (proves it works, byte-identical to
   the pre-publish legacy served artifact — PROVEN not claimed) -> CTO GOes publish -> rollback STAYS armed
   through the post-cutover monitoring window. Zero window where a bad publish can't be instantly reverted.
   This operationalizes Andrew's "roll it back immediately" as a control, not care.
2. **Seam-continuity EXERCISED** at the wire point (item 4) — DS runs it in the count-wire; CTO verifies it is
   EXERCISED (not asserted) at his re-verify.
3. **TO-2 tracked to closure** (item 1) — COO owns the track so the visible $10-20M cross-page drift is
   interim-not-forever (TO-2 = later wave; replaces the legacy aum-timeseries/aum-metrics FE reads with a
   revamp-derived single source).

## Control division (confirmed)

- **CTO + DT + CVO** = technical parity to the penny (3-way, done: CTO S3 re-verify + DT date-joined parity +
  CVO from-scratch, 3/3, 0 unexplained).
- **COO (this co-sign)** = changes NAMED / UNDERSTOOD / REVERSIBLE / residuals TRACKED.
- **Andrew** = sovereign GO + sees the 3 visible changes (items 1/3/5, surfaced).

## Publish gate + post-cutover

Publish fires only when BOTH: (a) DS count-wire re-verified (counts tie served exact + seam exercised) AND
(b) AE rollback TESTED-armed. My co-sign is conditional on (1) — publish fires when the tested-rollback is
confirmed. Post-cutover: the scheduled-cycle detection (durable marker + CTO per-cycle S3 re-verify) becomes
CONTINUED verification (shadow + ongoing checks + rollback trigger), not the pre-cutover streak gate.
COO-tracked follow-up: TO-2 to closure.
