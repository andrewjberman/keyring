# MDPF_REVAMP Cutover — COO Co-Sign Record (never-widen control)

**Signer:** 2.0.0_SA_COO · **Date:** 2026-07-21 · **Control:** never-widen serve-move (CTO+COO+Andrew co-sign)
**Trigger:** Andrew-direct PUSH-NOW (via CTO 180314Z) — S5 cutover on verified cycle-1 artifacts, rollback-armed,
NOT waiting for the scheduled streak. Andrew VERBATIM: push it, "be ready to roll it back immediately if it doesnt work."
**Package reviewed:** org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_REVAMP_cutover_cosign_package_20260721.md (@2e9a118f8)
**This record:** my MCP co-sign 180626Z + CTO acceptance 180814Z, captured durably (record-survives-session).

## Verdict: CO-SIGN GRANTED — conditional on tested-rollback-before-publish

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
