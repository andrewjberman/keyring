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
