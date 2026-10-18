# NEVER-WIDEN -- CTO HALF: `HVST-cf-5`, the version-2 fund forms (holding reports only, Mexico reports out) for PFOE and IDVZ (round 92)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~02:2xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round92/NEVER_WIDEN_HALF_COO_CF5_FUND_FORM_V2.md` as committed at
87eb5b095d, sha256 `a7c7f05e961dc30f778d7cb3e9b9444ae4ef54bf4b53f3dded854c46ffad8b6f`. Any edit to that file voids this half.

## Basis

- cg-3 landed at 02:06Z: release 4257a2aa42, ledger closed, ref pushed. W1's gateway read shows MNST and CLX candidate, ML_FP template, UNH
  holding, and gold unchanged. Silver and its serving are therefore in place.
- **cf-3's rule** (holding reports only, the two Mexico reports dropped) gives:
  - IDVZ 82 reports and PFOE 33;
  - DIVZ 0;
  - 139 reports before and 115 after: 22 non-holding reports dropped and 2 misfiled.
- **N = 1 writer:** `fund_form.write` (`gold_put`).
- **W1's correction is accepted.** With no matching stored form, `substrate._pick_stored` falls back to the stale version-1 form with
  `current` False (`substrate.py:121-159`); it does not return nothing.

## Blast radius

- **Writes:** two NEW gold `research-fund-form` objects, PFOE (33) and IDVZ (82), at method_version 2. Nothing is overwritten or deleted.
- **Served move: NONE.** No gateway tool reads a fund form, and stored dossiers keep citing version-1 forms until they are rebuilt, which
  this act does not do.

## Both branches

As the COO half states them:
- Branch A: each object read back equals the build.
- Branch B: any difference is a STOP. A repair is a still newer object.

## Rollback

The act is ADD-ONLY. Removing the two keys restores the stale resolution; that is an S3 delete, Andrew's act, not pre-approved here.

## Conditions of this signature

1. **C-1 to C-8 of the COO half bind as written,** including C-6: no dossier or continuation `write_one` until this ledger closes. Also no
   `fund_form --compare`.
2. **DIVZ is a hazard this act does not close, so it gets its own rule.**
   - After cf-5, DIVZ still resolves to the stale version-1 form, which counts candidate and misfiled reports.
   - So C-6 stays in force for every dossier or continuation build that reads DIVZ's form, even after this ledger closes.
   - The round-93 cell: DIVZ resolves to a version-2 form with 0 reports and an absent reason, or the substrate stops falling back to a
     stale form. Then no reader can pick up the version-1 count.
3. **D1-S50 (INERT), a round-93 row:** with `fund_relation` added, the response-size cap drops one `research_reports` entry (CPA shows 9 of
   37 where it showed 10). Raise the cap, or state the truncation in the response, so an entry is never silently dropped.
4. **The S44 rule** applies, and the ledger close is COMMITTED with the manifest.

## VERDICT: SIGNED (CTO).
