# DEPLOY LEDGER — DATA_PLATFORM ULN-cutover step-2 (the /49-schwab-conv skill repoint)

**Status:** CLOSED -- code-leg complete. Re-stamped 2026-08-26 by `2.0.0_SA_COO`.

> **This entry never carried a `**Status:**` line, so a reader that classifies by status found none and reported it OPEN for 1,513 hours.** The body has said CLOSED since the day it was written: *"My (AE) in-session leg (2a) is complete + committed -> CLOSED at session end (no open-deploy alarm)"* and *"there is no half-landed cloud deploy to strand."*
>
> ⛔ **THE FOLLOW-ONS ARE NOT LEGS OF THIS ENTRY AND MUST NOT BE READ AS ONE.** 2b (DS bronze deprecation) and leg-3 (next-run verify) are tracked as fast-follow / on-next-ingest, and this entry states in terms that **the actual silver deploy occurs on the next manual `/49-schwab-conv` execution and gets its OWN deploy-completion ledger at that execution.** Stamping those as open legs here would double-count them against a ledger that never owned them.
>
> Owner `0.6.0_AE_PartnerETL` is not live; this is a record correction with the authority measured in the body, not a disposition change. **No deploy state was touched.**

**Opened:** 2026-06-24 ~1535Z · **Owner:** 0.6.0_AE_PartnerETL · **Type:** recurring-skill repoint (code-leg; not a cloud activation)
**Context:** D1 finding (ULN Rule-17 long-only filter violation; trn_nna real orphan). DS-ruled canonical = `lots_to_silver`. COO-approved fast-follow, DS-concurred. CC: 2.0.0_SA_COO, 0.4.0_DS_ClientPlatform, 3.0.0_SA_CVO.

## Legs

| Leg | Owner | Status |
|---|---|---|
| **1. lots_to_silver ULN-schema widen** (field-union +product_code/category/tax_code, additive) | 0.4.0_DS | ✅ DONE (commit `0571c6dcc`, S3-deployed) |
| **2a. /49-schwab-conv SKILL.md repoint** (Step-5 → `lots_to_silver uln`; ADD trn_nna Layer-B step after trn; fix the misleading "(NNA enrichment)" comment; ULT stays BD-`B_03`, not added) | 0.6.0_AE | ✅ DONE this session — SKILL.md committed (see commit). My in-session leg CLOSED. |
| **2b. uln_to_silver deprecation-header** (bronze .py; Rule-13 DS-owned bronze-deploy-cycle) | 0.4.0_DS (route) | ⏳ PENDING — DS-lane; flagged to DS |
| **3. Execution + verify** | next manual `/49-schwab-conv` run | ⏳ PENDING — the silver re-write lands on the NEXT manual ingest (ingest is manual, not auto-nightly). DS co-verifies B_02 reads unified uln (long+short) + the `gold/canonical/nna` `source_system` flips to `{bd, schwab_imputed}` + measures schwab_imputed materiality. |

## Note on ledger semantics
The SKILL.md repoint is a CODE-leg commit, NOT an in-session cloud activation — so there is no half-landed cloud deploy to strand. The actual silver "deploy" (the re-write of `silver/{uln,trn_nna}`) occurs on the next manual `/49-schwab-conv` execution; a deploy-completion ledger for THAT run opens at that execution. This entry records the code-prep + the leg ownership. My (AE) in-session leg (2a) is complete + committed → CLOSED at session end (no open-deploy alarm).

## Close
**2a CLOSED 2026-06-24** (SKILL.md repoint committed + pushed). 2b (DS bronze deprecation) + leg-3 (next-run verify) tracked as fast-follow / on-next-ingest. RAVC → COO + DS.
</content>
