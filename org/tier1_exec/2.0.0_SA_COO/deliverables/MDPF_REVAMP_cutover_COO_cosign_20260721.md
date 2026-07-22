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

## RE-LAND CO-SIGN -- FIRED 2026-07-22 ~06:43Z (COO limb GRANTED; 2 of 3 never-widen limbs signed)

CTO assembled the COMPLETE package + gave the CTO never-widen co-sign. Every condition my co-sign was staged
on is met; my COO limb FIRES:
- **PIN re-verified AT FIRE-TIME** (my own ListObjectsV2, all 9 ETags UNCHANGED from the staged set, no
  re-stage since grounding): aggregate `aa5c5b85`/`cec5a0d6`/`c27e1f37`, non_model `8a195549`, A1 `529b7c21`,
  A2 `f2c03476`, account_dist `865919f2`/`afb964c4`/`b946d836`. CTO same-set + HeadObject-all-9-live confirmed.
- **DATA:** I independently ran CVO's mutant-proven Layer-3 gate MYSELF = PASS (B-basis consistent, 421/421);
  3 battery legs green same-object + CVO adversarial 7/7 on DT. My limb is INDEPENDENT (not CTO's evidence) --
  the first flip's chain shared a false premise; this one does not.
- **RENDER:** CTO visual-confirmed BEFORE/AFTER pixels (sha 6287847c: Global continuous, 6 gaps bridged, 2x
  axis, flat-grey intact, no false-dip); DEV surface-check + CI GREEN + SURFACE_ACK present.
- **ROLLBACK:** ARMED + exercised BEFORE publish (--target, 409-avoided) -- my held condition MET.
- **FE-FIRST** + window characterized GRACEFUL (DE) + minimized (publisher pre-populated) + CTO accept-window
  call made.
- **Verify-before-serve = HARD post-promote gate** (DE live-render + Andrew hover + CVO cycle-1; rollback
  armed until CTO disarm).

** COO NEVER-WIDEN CO-SIGN: GRANTED (re-land). ** 2 of 3 limbs signed (CTO + COO). Andrew's sovereign limb =
the 3rd + the GO (CTO surfaces). The co-sign is NOT "ISSUED" (for DT's promote gate) until all 3 limbs; I
signal DT PLAINLY only AFTER Andrew's sovereign limb.

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

---

# 2026-07-22 SESSION 2 -- ANDREW RE-SCOPE, PIN RE-VERIFY, ITEM-1 ENUMERATION, CUSTODY DISCHARGE+RE-ARM

## A. ANDREW-DIRECT 2026-07-22 ~1205Z (relayed via 0.0.0_AB_MSTR, who holds the primary record)

VERBATIM (Andrew -> MSTR session, ~1205Z UTC / ~0805 ET):

> "Yes I think we must have crashed sometime this morning, or the device updated/restarted. I want you to
> assess current position, and inform CTO and COO who I have also spawned. The thing I need them to figure
> out, is the finalization of MDPF_REVAMP. The remaining items that need to be completed are figuring out
> why Inflection's model numbers are jumping around july 6 july 7 with some other odd spikes in the daily
> trend timeseries. THe other item is the integration of the Cottonwood data into MDPF on the Portal via
> the Select Partner dropdown and aggregating it into the GLobal view."

**HE DID NOT GIVE THE 3RD LIMB.** He re-scoped instead of signing. MDPF_REVAMP finalization = TWO NAMED
ITEMS. **Whether the held exact-9 flip sits INSIDE or OUTSIDE that gate is UNSTATED -- surfaced to Andrew
via CTO, deliberately NOT inferred by COO, CTO, or MSTR.**

## B. PIN RE-VERIFIED 2026-07-22 ~1205Z -- 9/9 UNCHANGED, CO-SIGN VALID

My own `list-objects-v2` on `opal-data-assets/gold/mdpf_revamp/` (APPLIED truth, not a manifest):
aggregate `aa5c5b85`/`cec5a0d6`/`c27e1f37` - non_model `8a195549` - A1 `529b7c21` - A2 `f2c03476` -
account_dist `865919f2`/`afb964c4`/`b946d836`. **All 9 unchanged from the 0645Z fire-time set.**
COVERAGE DENOMINATOR: 10 objects live under the prefix; 9 = the pinned set (9/9 covered); the 10th is
`global/non_model_assets_precutover_frozen.json` (`da2260f6`), a reference artifact NOT in the publish map.
Newest write across the prefix = 05:23:12Z, BEFORE the 0645Z fire. No re-stage. **CTO independently
verified the same 9 with the same 10-object denominator and the same 10th-object exclusion -- two limbs.**
Both overnight deploy ledgers CLOSED (mdpf-exact9 040519Z as rolled-back; portal-2x 0515Z 8/8). NEVER#5 satisfied.

## C. CUSTODY RULING (mine, binding on my own limb) -- MADE, then DISCHARGED for item 1, RE-ARMED for item 2

**RULING:** my 0645Z limb is pinned to the coherent-9. **If any investigation changes ANY of the 9, the COO
limb VOIDS and re-fires fresh on a new pin with a fresh 3-pass. It does not carry forward.** Same rule I
used to void the 0159Z co-sign at 034410Z; it binds me identically or it was never a rule.

- **DISCHARGED vs ITEM 1** (CTO grounded item 1 with NO change to any of the 9; MSTR concurred). Limb stands.
- **RE-ARMED vs ITEM 2 -- STRUCTURAL, NOT A RISK (MSTR's catch, which I had not made).** Item 2 is
  *"aggregating it into the Global view."* Adding Cottonwood to Global **necessarily rewrites
  `global/aggregate_aua_timeseries.json` = `c27e1f37`, the anchor of the pinned 9.** The 2-of-3 co-sign is
  not "at risk from" item 2 -- it is **structurally doomed by it.**
- **THE ITEM-1 DISCHARGE IS NOT A GENERAL RELEASE.** Recording that explicitly so no post-Cottonwood flip can
  cite a co-sign that Cottonwood itself invalidated -- that is the stale-record-with-authority shape.

## D. ITEM-1 ENUMERATION -- COO INDEPENDENT LIMB (read-only on the frozen-9)

Method: own pull of all three pinned aggregate artifacts; day-over-day pct on `model_aua` and
`non_model_aua`, honest-None-skipping, plus composition signature (dModel / dNonModel / dTotal) and
`by_model` band drivers. Script + raw output in session scratchpad.

**D.1 -- CONVERGENCE WITH CTO (two independent limbs, agreeing).** `136,859,722` appears in BOTH artifacts,
dated **07-06 in legacy** and **07-10 in revamp** -- same value, different date. Legacy posts a real 07-10
move onto 07-06 => jump-and-revert = Andrew's "jumping around july 6 july 7." **The revamp already fixes it.**
Confirms CVO @88851665d ON THE VALUES rather than on say-so. Andrew is necessarily on LEGACY (CTO grounded:
live CF EVTSA9VEHNZVH = 24 behaviors / no assets origin / revamp FE 6287847c on DEV, never promoted).

**D.2 -- 06-03: MEASURED RECLASS, NOT FUNDING; and the mechanism RECURS.**

    06-02 -> 06-03: dModel +16,961,432 / dNonModel -16,894,373 / dTotal   +67,059
    07-09 -> 07-10: dModel +11,765,853 / dNonModel  -9,831,133 / dTotal +1,934,720

`by_model` at BOTH: **all seven bands rise simultaneously**, summing exactly to the model delta (06-03:
intermediate +6,648,251 / ltc +4,501,249 / blend_int_ltc +4,032,709 / blend_st_int +939,853 / st +686,661 /
lta +152,685 / ust +24). A funding event moves the TOTAL; these swap. A single-model onboarding lifts ONE
band. **=> batch account reclassification, and CVO's "ONE-TIME" does not survive -- 06-03 is the same class
five weeks earlier.**

**GROUNDING LABEL (Rule 22): the SIGNATURE is MEASURED. "It is a modelId reclassification" is INFERRED --
artifact-level, no producer source read. It cannot authorize a fix or a cert.**

**D.3 -- I CONCEDED 06-03 TO CTO ON NEW EMPIRICAL EVIDENCE.** CTO produced `accounts +44` at 06-03 against a
flat ~$200-206M `partner_custody_total` -- evidence I did not have. Per my own standing discipline
(reversal requires NEW empirical evidence, never a re-read) I updated: **a real 44-account mix shift, the
chart is honest, it must not be "fixed."** Recorded as a concession, not a hedge.

**RESIDUAL I STILL HOLD (narrow):** `accounts +44` comes from the SAME producer on the SAME axis as the
dollars, so a mis-assigned batch moves BOTH fields to the same wrong date and the artifact stays perfectly
self-consistent -- **which is exactly what legacy did.** It establishes THE EVENT, not THE DATE. Closing it
needs a source OUTSIDE the producer axis (eclipse/silver as-of, or modelId assignment timestamps). Routed to DS.

**D.4 -- SURFACE NEITHER CTO PASS COVERED (both were inflection-only + model-only).** non_model, >=5% DoD:

| artifact | model hits | non_model hits | total hits |
|---|---|---|---|
| INFLECTION | 2 | **4** | **0** |
| GLOBAL | 3 | **15** | **0** |
| 49FINANCIAL | 2 | **15** | **0** |

Every firm TOTAL is smooth -- all motion is compositional. **The trend chart is STACKED, so 15 non_model
moves in the Global view are VISIBLE to Andrew and none are explained.** Largest untouched population of
his "other odd spikes." Mostly offsetting-reclass class; some genuine NET-MOVEs (2025-09-30->10-01 +$49.5M;
2026-07-10->07-16 +$19.6M).

**D.5 -- HONEST-NONE INVENTORY:** `2026-05-21, 06-01, 07-01, 07-13, 07-14, 07-15` (6, matching DE's "6 gaps
bridged"). **49F has ZERO -- every gap is inflection-origin and propagates to global.** 05-21 is co-signed
item 3. **07-13/14/15 is a THREE-CONSECUTIVE-TRADING-DAY hole (Mon/Tue/Wed) immediately after the 07-10
event, inside Andrew's window, covered by NO co-signed item and explained by nobody.**

## E. POSITION CARRIED TO CTO FOR ANDREW

- Item 1 headline **ANSWERED** (legacy date-mislabel + 3 further legacy defects CTO found; revamp fixes them).
- **Flip proceeds on the EXISTING pin** -- COO recommendation stands; nothing found indicates a wrong number
  served, and the revamp beats legacy on every dimension either exec measured.
- **DO NOT say "Item 1 CLOSED" / "no unfixed defect."** Three threads remain open (D.3 date-independence,
  D.4 fifteen unexplained Global non_model moves, D.5 the 3-trading-day hole). MSTR concurs and is holding
  item 1 open for 3-limb convergence (COO + CTO + CVO). **An overclaim in our own favor is the one error
  this gate cannot absorb.**
- **SEQUENCING (Andrew's, unstated, surfaced not inferred) NOW CARRIES A PRICE (MSTR):** item 2 inside the
  gate = **ONE flip later**; item 2 outside = **TWO flips, TWO never-widen co-signs, TWO user-visible
  windows.** My "item 2 does not gate the flip" rec must be argued with that price attached.
- **Item 2 is NOT new scope** -- `MDPF_COTMDL.json` is complete/COMPLETE-AS-SUPERSEDED (07-21) by
  **WSE_COTMDL WS-2/3/4/5**, which COO already carries, with a grounded design (Rebalancer
  `accountRebalStrategyID` === `model.id`; 60 Cottonwood models / 17 Opal in-scope). Andrew has now placed
  it INSIDE finalization, so it is no longer "staged behind the cutover." Flagged to CTO so the stale
  staging order does not reach Andrew.

## F. STAFFING (COO position, MSTR executing)

Item workers UP (MSTR provisioned, COO concurs): `0.4.0_DS_ClientPlatform` (producer side of item 1),
`3.0.0_SA_CVO` (whether its own verdict generalizes), `0.4.0_DE_ClientPlatform` (item 2 portal surface).
Flip-custody set HELD at COO request, CTO concurring and accepting the lead-time deliberately:
`0.7.0_AE_CloudOps`, `0.2.0_DT_PortfolioAnalytics`, `0.6.2_AE_PartnerETL~A` -- ~40s to spawn, CTO calls it
the moment Andrew's limb lands, **AE + DT first (critical path).**

---

# G. COO NEVER-WIDEN LIMB **WITHDRAWN** 2026-07-22 ~1234Z -- RE-LAND IS 0 OF 3

**SUPERSEDES SECTIONS C, D AND E ABOVE WHERE THEY READ AS A CLEARANCE.** The item-1 discharge in section C
is **REVOKED** -- the premise it rested on (CTO: "no defect in the frozen-9") is falsified.

## G.1 -- THE DEFECT, INSIDE THE CO-SIGNED FROZEN-9

Found by `0.4.0_DS_ClientPlatform` at source (122838Z), independently reproduced by `1.0.0_SA_CTO` on his own
instruments with a **separately-run positive control** (123328Z).

`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` imports `account_count` **from the LEGACY
SERVED artifact by date-join** (`:476-500`, wired `:812`) and **discards the correct count it already
computes at `:427`.** Legacy's date axis is the one CTO proved broken. **Therefore one artifact reads its two
axes from two different days:** the VALUE axis comes straight from eclipse (`_source_as_of` == partition,
54/54) and is correct; the **COUNT axis inherits legacy's mis-stamps.**

Frozen-9 `inflection/aggregate_aua_timeseries.json` (`cec5a0d6`), COUNT axis:

    07-02  474  ->  07-06  540  ->  07-07  474  ->  07-08  475      = +66 then revert

while VALUE at 07-06 is correctly `122,866,034`. True 07-06 count = 474; 540 is eclipse's **07-10** roster.
CTO's positive control, run SEPARATELY: revamp count == legacy count at 07-02/07-07/07-08 (474/474/475), so
the test is not vacuous.

> **ANDREW'S SENTENCE -- "Inflection's model numbers jumping around july 6 july 7" -- IS REPRODUCED BY THE
> ARTIFACT TWO EXECS HAD ALREADY CO-SIGNED, on the count view, on his exact dates.**

DS sweep denominator: **38 of 427** revamp dates have an eclipse partition (eclipse starts at the 05-15
launch) -- 26 agree, 7 honest-None, **5 disagree**: 4 genuine misalignments (05-27, 05-28, 06-24, **07-06**)
+ 07-20, which is the **declared** account_dist FUNDED-frontier basis, not a defect.
**UNMEASURED AND EXPLICITLY NOT CLEAN: 49F + global use the same import path (`:628`).** Structurally
present, not swept. *Unmeasured is not clean.*

## G.2 -- WHY MY LIMB WITHDREW: FALSIFIED PREMISE, **NOT** ETAG MOVEMENT

**No ETag moved.** DS wrote nothing; the pin is byte-intact; my 1205Z 9/9 verification is still true.
**I did not auto-void on movement -- I WITHDREW on falsified premise, which is a custodial act, not a
mechanical one.** My limb was granted citing:

> *"DATA: I independently ran CVO's mutant-proven Layer-3 gate MYSELF = PASS."*

**That gate runs the VALUE axis. My evidence never covered the axis carrying the defect.**

> **A CO-SIGN IS WORTH EXACTLY THE AXIS ITS EVIDENCE RAN ON.**
> **AN INSTRUMENT THAT PASSES ON A DEFECTIVE ARTIFACT HAS TOLD YOU ABOUT THE INSTRUMENT, NOT THE ARTIFACT.**

CTO reversed his own "pin intact" ruling on the same grounds within ~40 seconds, independently. **Both limbs
withdrawn. Re-land = 0 of 3. Nothing is servable and nothing should be.**

## G.3 -- THREE DENOMINATOR FAILURES IN A ROW; THE PATTERN IS THE FINDING

| pass | ran | denominator | blind to |
|---|---|---|---|
| CTO | `model_aua`, inflection only | 429/37 legacy, 427/33 revamp | non_model; other firms; COUNT |
| COO (mine) | `non_model` + `model`, 3 firms | 427 dates, 420-426 transitions/firm | **COUNT** |
| DS | COUNT axis vs eclipse source | 38 of 427 eclipse-covered | (found it) |

**Each pass printed its denominator honestly. Each denominator was of a NARROWER POPULATION than Andrew's
words described.** Three rigorous instruments, three correct denominators, one defect outside all three.
It was found only because each limb pushed the next one wider -- DS states my Q3 push (below 5%, below the
firm total) is what sent him to the count axis. **A rigorous instrument on the wrong axis survives review.**

## G.4 -- WHAT SURVIVES, AND WHAT I SUPERSEDED OF MY OWN

**SURVIVES (value axis, legacy vs revamp, same field/threshold/firms):** legacy **90** large non_model steps
vs revamp **34** -- GLOBAL 29->15, 49F 55->15, INFLECTION 6->4. Denominators: legacy 429 dates/428
transitions per firm; revamp 427/420-426. **The revamp IS materially better on the value axis.**
Methodological caveat retained: the date-keyed set-diff (BOTH 7 / REVAMP-ONLY 27 / LEGACY-ONLY 83) is **NOT
quotable as event counts** -- the two artifacts sit on different date axes, so one event keys twice
(inflection `05-14->05-15 -46.18%` revamp == `05-15->05-18 -47.94%` legacy). **The COUNT comparison is
axis-independent; the set-diff is not.**

**SUPERSEDED -- MY OWN 123050Z CLEARANCE TO MSTR.** I used 90-vs-34 to clear CTO's Andrew-carry on the
premise *"the flip removes what Andrew is looking at."* **On the COUNT axis that premise is FALSE.**
Whichever view he is on, he sees a Jul6/7 jump -- in different modes. Corrected 20 minutes later, before it
reached Andrew as a clean bill.

## G.5 -- SEQUENCE (CTO gates, COO holds custody -- agreed between us)

1. DS sweeps the **49F + global residual FIRST** (same import path `:628`; unmeasured is not clean).
2. Fix the count-axis import (the correct count already exists at `:427`).
3. Rebuild **re-produces inflection + global** -> **FRESH PIN**.
4. **FRESH 3-PASS COVERING BOTH AXES.** The old Layer-3 gate passed on this artifact -- it may NOT be the
   sole data evidence, and the re-verify needs a clause that would have caught THIS.
5. Fresh CTO + COO limbs -> Andrew's sovereign limb.
- Binding (CTO): print the 38-of-427 eclipse-coverage denominator so nobody reads the sweep as covering 427;
  keep the 07-20 FUNDED-frontier seam **DECLARED, not "fixed."**
- **AE / DT / PartnerETL~A stay HELD** -- there is no GO, and now a rebuild in front of it.

## G.6 -- COO SERIALIZATION ORDER (write-collision on `global/aggregate_aua_timeseries.json`)

**TWO WRITERS, ONE OBJECT, BOTH IN FLIGHT:** DS's rebuild re-produces `gold/mdpf_revamp/global/
aggregate_aua_timeseries.json`; WSE_COTMDL **WS-4** folds Cottonwood into that same object.

**ORDERED: (1) DS rebuild + fresh pin -> (2) fresh 3-pass + fresh limbs + flip -> (3) Cottonwood Global fold
as its own co-signed change. WS-4 HELD BY COO until (2) completes.** A Cottonwood write landing mid-rebuild
would corrupt the pin DS is establishing, invisibly, until a co-sign cited an ETag that had moved underneath it.
**WS-2 / WS-3 / per-firm `json/mdpf/cottonwood/` + the `ModelPortfolios.tsx:236` dropdown PROCEED NOW** --
new territory, zero collision. DE endorsed and building.
Carried into WS-3/WS-4: **cot gold push AUTO-DEPLOYS** (bypasses a co-sign gate by construction);
**FIRM SEPARATION (NEVER#2 / Rule 13)** -- the Global fold is where the firm-boundary architecture call
actually lands, and it is **CTO's**; **the composition gate does NOT generalize 3->4 firms by assumption** --
`total == bands + non_model` must be re-exercised at four (the class that caused the 07-22 P0).

## G.7 -- CUSTODY STATE OF RECORD

| | state |
|---|---|
| COO never-widen limb | **WITHDRAWN** (falsified premise) |
| CTO never-widen limb | **WITHDRAWN** (self-reversed, same grounds) |
| Re-land co-sign | **0 of 3** |
| Item-1 discharge (section C) | **REVOKED** |
| Item-2 re-arm (section C) | **STANDS** -- Cottonwood-into-Global structurally rewrites `c27e1f37` |
| Pin `9/9` byte-state | still intact; **intactness is now irrelevant** -- the bytes are known-defective |

**THE GATE WORKED.** A never-widen co-sign held a defect off the served surface, on the exact dates the
sovereign asked about, caught by us before him. That is the whole case for the gate, demonstrated on itself.

---

# H. ANDREW-DIRECT 2026-07-22 ~1259Z — **ONE FLIP, COTTONWOOD INSIDE THE GATE**

**AMENDS SECTION G.5.** G's sequence ("fresh pin -> fresh 3-pass -> fresh limbs" on the rebuilt 2-object
set) is **SUPERSEDED**. Leaving G.5 unamended would be a stale record with authority — the exact hazard
this file has been guarding all session.

## H.1 — THE RULING

VERBATIM (Andrew -> CTO terminal, 2026-07-22 ~1259Z UTC / ~0859 ET):

> **"Let's push everything with Cottonwood"**

**ITEM 2 IS INSIDE THE GATE. ONE FLIP, ONE CO-SIGN, ONE WINDOW.**
The joint CTO+COO **two-flips recommendation is OVERRULED** — and it was made **with our reasoning and
MSTR's cost framing in front of him**, so it is *decided, not un-considered*. **No re-litigating, from me
least of all.** My own rec (flip now, Cottonwood behind) is withdrawn.

## H.2 — THE CUSTODY CONSEQUENCE: **NO BINDING PIN UNTIL THE END**

DS staged the rebuilt objects at 12:54Z. **I verified them on my own ListObjectsV2 — not transcribed:**

| key | ETag | size | state |
|---|---|---|---|
| `inflection/aggregate_aua_timeseries.json` | `5e7b684dbc141eeffb6de9ffabc9e893` | 145,039 | **REBUILT** |
| `global/aggregate_aua_timeseries.json` | `08f9720ef2056fd07a457a77c158b567` | 175,195 | **REBUILT** |
| `49financial/aggregate_aua_timeseries.json` | `aa5c5b85066109c9bdb557e51b0d8ffd` | 178,414 | unchanged |
| `portfolios/aum-timeseries.json` (A2) | `f2c034760b44c4bd7338be0fd6c75c58` | 277,699 | **unchanged — STILL DEFECTIVE** |
| A1, A4, account_dist x3, precutover_frozen | unchanged | | |

DS's diff vs frozen: 49F **0 differences**; inflection **2,747** and global **802**, **all in `account_count`
— no value moved anywhere.** 07-06: inflection 540 -> 474, global 7620 -> 7554.

> **THESE ARE A CHECKPOINT, NOT A PIN. I DO NOT SPEND A LIMB ON AN INTERMEDIATE.**
> Cottonwood-into-Global **rewrites `global/aggregate_aua_timeseries.json` again**, so any pin taken today
> is **void by construction before it is ever served.** The binding pin is taken **ONCE, at the end, on the
> complete Cottonwood-inclusive set.** The COO limb fires **once**, on that set.

This also **retires the "you are buying a second co-sign either way" framing** — under one flip there is
exactly one, and it comes last.

## H.3 — SERIALIZATION **INVERTS**; MY WS-4 HOLD IS **LIFTED**

**OLD (mine, G.6):** DS rebuild -> pin -> flip -> *then* Cottonwood fold.
**NEW:** DS's fix lands -> **Cottonwood folds ON TOP** -> **then the whole set is pinned once and co-signed
once.** WS-4 is **IN** the single pinned set, not behind it.
**WS-4 HOLD LIFTED 2026-07-22 ~1301Z** and re-issued to DE, who was holding on my authority.
CTO likewise corrected his own DE ruling: the Global fold is **not a second co-sign — it is THE co-sign.**

## H.4 — THE CLASS GREW: **A THIRD PATH, AND IT IS A PATTERN**

DS found A2 `portfolios/aum-timeseries.json` carries the same defect via a **third code path**
(`build_legacy_compat_emit.py:598`, `ac = legacy_pt.get("account_count")`): count 7291 -> **7353** (07-06)
-> 7302, a **+51 excursion that reverts**, reconciling to inflection's share of the foreign-day roster
(+52 predicted vs +51 measured). **Not written** — DS reported scope growth before writing, per the rule.

> **CTO RULING: this is a PATTERN, not a bug — *everywhere the revamp was built to TIE TO SERVED, it
> inherited served's broken date axis. Three paths, three inheritances.*** A2 is fixed in this wave, plus a
> **full sweep of the tie-to-served class** rather than fixing three and hoping. **Andrew's one-flip ruling
> is what buys the room to do that properly** — an unintended benefit of being overruled.

**COO CONDITION ON THAT SWEEP: it must print its DENOMINATOR.** Three paths are *known*; the population is
**not yet bounded**. My own `comp-grep` over `data/mdpf` shows `opal-data-portal-v2` referenced across the
backfill tree and in at least one further live gold producer
(`build_mdpf_etf_ownership_timeseries.py`, reading `platinum/mdpf/...`). **Whether those are in-class is
exactly what the sweep must answer.** *"Three found" is not "three exist."*

## H.5 — GLOBAL WAS NOT AUTOMATIC (DS, and it belongs in the custody record)

CTO and DS both assumed global would recompose from the corrected inflection leg. **It did not** — the first
rebuild left global **byte-identical**, because global had its **own** served import. Caught only by diffing
the rebuild against the frozen artifact.

> **Why it hid is the sharpest instrument lesson of the day: because the legacy global count WAS
> 49F + inflection, the identity `global == 49F + inflection` held EXACTLY 7/7 *while the entire sum sat on
> the wrong day.* A coherence check PASSED and still shipped a foreign-day roster.**
> **IDENTITY-HOLDS IS NOT DAY-CORRECT.** A cross-sectional invariant cannot detect a whole-series date shift.

DS also caught a **false pass in his own mutant test** (first run exited 1 on a `ModuleNotFoundError`, not on
the gate) and re-ran it properly before recording — *an exit code is not a reason*, the same class as
`grep -c` counting zero matches in an error message.

## H.6 — THE GATE I REQUIRED IS BUILT AND MUTANT-PROVEN

DS's cross-axis coherence clause is **fail-closed**: reverting to the old import makes the build **RAISE and
refuse to emit**, naming `2026-07-06: 474 -> 540 -> 474 (+66, reverts EXACTLY)`. **It would have caught THIS
defect** — which was my requirement (*the old Layer-3 gate could not have failed on this class*).
**Clause (vi) is deliberately THRESHOLD-FREE, because a percentage floor is precisely what hid the defect on
global** (+66 on 7544 = 0.87%, under DS's own 5% floor).

## H.7 — CRITICAL PATH MOVED OFF DS AND ONTO DE

The flip now waits on **WS-4 fold -> Select-Partner FE -> the 4-firm composition gate**, plus A2 + the
tie-to-served sweep. Status: **WS-1 LIVE; WS-2 COMPLETE @bcd5ab971; WS-3 COMPLETE @449ef54aa** (9 dim rows,
447 counts over 296 accounts, 0 orphans, 16 tests + 3 mutants proven to bite).
**Date risk, named not buried:** (a) the tie-to-served sweep's **denominator is unknown** — scope unbounded
until it prints; (b) the **4-firm composition identity is untested** and is the P0 class; (c) **WS-5's
`.xlsx`-vs-`.json` trigger gap** means Cottonwood silver+gold **do not self-refresh** — *we cannot flip a
nightly-fed surface whose feed is manual*, so AE must come up before the flip regardless.
**COO position: give Andrew the sequence and the three risk items, and a date once the sweep denominator
lands. He bought this knowingly; he can price an honest unknown.**
