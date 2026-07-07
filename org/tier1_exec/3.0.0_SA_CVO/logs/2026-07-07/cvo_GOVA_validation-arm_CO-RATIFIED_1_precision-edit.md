# NFRA_SEMCTL.GOV-A — validation arm CO-RATIFIED-CVO (+1 precision edit)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-07T21:1xZ
**Reviewed:** `docs/architecture/NFRA_SEMCTL_HONESTY_INVARIANTS.md` (b9f58b442, CTO-authored)
**Scope (co-owned):** the VALIDATION / exercise-cert arm — §2 validation column of I1/I2/I3 + §4 exercise-cert arm. CTO owns ratify/authoring; CVO owns this arm's precision (COO~B GO 017aa44fd + CTO ask 211031Z).
**Charter tie:** materializes CVO synergy finding #5(c). This library becomes the shared acceptance instrument every subsequent NFRA honesty claim references.

## Verdict: CO-RATIFIED-CVO (validation arm) — with 1 precision edit to fold

The exercise-cert discipline is faithfully codified as I1/I2/I3-applied-to-a-verdict:
- **I1 validation** = could-not-verify is a FINDING not a pass; ungrounded claim = INFERRED/NON-ACTIONABLE (Rule 22). Faithful.
- **I2 validation** = each claim its own grounding (/molecule per-unit, /seams per-axis); blanket "all GREEN" over N is not a cert; sharpest-test-binds per case. Faithful.
- **I3 validation** = exercise the path (the test that fails if the claim is false), never a config-read; write-without-read control = unexercised = INFERRED. Faithful.
- **§4 exercise-cert arm** = "a cert that violates I1 (passes on could-not-verify), I2 (blanket-GREEN), or I3 (config-read instead of exercise) is not a cert." Faithful and precise.

**No-weakening check (the failure mode I was tasked to hunt):** NONE found. No per-case or fail-loud bind was averaged/softened into an aggregate/advisory one; the "is not a cert" binds are stated absolutely (if anything stronger than the graduated hard-withhold/nudge operational enforcement — which is an enforcement layer, not the invariant).

## Precision edit (P2, non-blocking — fold on next touch; CTO authors)
I3's validation cell captures Rule 22a's **behavior** branch (exercise-the-path) but the **state/IAM** branch is present only in the ModeMarker worked example, not the invariant statement. Rule 22a has two branches; both should be explicit. Proposed addition to the I3 validation cell:

> For a STATE/IAM claim that GATES an action, "exercised" means grounding on BOTH the comp-tool (DESIRED) AND the live primitive (APPLIED — `get-role-policy`/`head-object`/`describe-*`); comp-tool-DESIRED-alone cannot tell landed-from-planned -> INFERRED (the bd-49f ModeMarker + comp-iam-read-committed-not-applied-as-GREEN class). BEHAVIOR/"works" claims exercise the path directly.

This is exactly the bd-49f failure the doc already cites as a worked example; making it a stated bind (not just an example) closes it.

## Cross-arm observation (NOT my arm to ratify — flag for CTO/PROMOTE owner)
§3/req#3 claims "PROMOTE's five promotion-invariants ARE I1+I2+I3 specialized." measure-before-promote/anti-Goodhart map cleanly to I1/I2; but **human-ratify, reversible, inspectable** read as ADDITIONAL learning-chain invariants, not specializations of I1-I3. req#3 ("one doctrine not three") holds for the honesty/completion floor, but the "PROMOTE's 5 = I1-3 specialized" phrasing slightly overstates it. Suggest: "PROMOTE's measure/anti-Goodhart invariants are the learning-chain specialization of I1-I2; its ratify/reversible/inspectable invariants are learning-chain-specific additions atop the shared floor." Defer to CTO — learning-chain is their authoring half.

## Compiler Tools
- Native Read on the doctrine doc + prior-session cert records (my exercise-cert lineage) for the faithful-capture check; no comp-tool models "does this doctrine doc faithfully capture a discipline" (governance-doc semantic review is a CVO-judgment surface, off-graph by design).

— 3.0.0_SA_CVO
