# NFRA_SCHWABBF -- ROUND-1 ANALYSIS (1.0.0_SA_CTO, 2026-10-20 ~15:0xZ)

**On:** the issuer's L10 slug `deliverables/2.0.0_SA_COO~SB/ROUND1_L10_SLUG_TO_CTO.md` @7e6e18ee43 (laptop msg 109903). Round 1 is terminal: 6 of
6 orders, proofs 6 of 6 valid, `round-close-check` MAY-CLOSE. Nothing was deployed, moved or written to AWS. **PRD:** v0.5 @99555e0048
(C-KEYFORM is firm scope since v0.3, on Andrew-direct ~14:3xZ).

## 1. Coverage

- **FWD-1 is NOT exercised.** The cells were built on the MASTER form before C-KEYFORM moved to the FIRM form, so the cutover acts did not
  run. That was correct: running them would have written the wrong form.
- **Built and reusable as is:** BF-e-1, the one-shot equality tool, which reads silver by master.
- **Built and needing rework to the firm form:** BF-k-1 (key function pair, parsers, listers), BF-m-1 (move tool), BF-r-1 (readers),
  BF-w-1 (puller), BF-t-1 (trace oracle).
- **Measured by the issuer, outside the round-1 rectangle:** IAM (`monolith-iam.tf:60-81`, `iam.tf`), the silver event rules
  (`silver.tf:242-244`), and the converter reading the master from path segment 1 (`schwab_conversion.py:133-143`, plus its deployed twin).
  The issuer's list is accepted whole.

## 2. Rulings

1. **Round 2 is as slugged, on the BRONZE side:**
   - firm-form rework of BF-k-1, BF-m-1, BF-r-1, BF-w-1 and BF-t-1, with every lister filtering by master inside the shared firm folder;
   - new cells: the converter takes the master from the vendor file name (code, deployed twin and test); the IAM statements for
     `schwab/49financial/bronze/` and `schwab/cottonwood/bronze/`, enumerated per master by file-name prefix (PRD v0.5 C-ALONGSIDE); and
     the event rules for the new prefixes;
   - then the release acts on the firm form.

   Chains as the issuer proposed: the key function first; the Terraform cell runs independently of the Python chain. The fan-out choice (row
   S1: event rule first, or copy first then an explicit conversion run) is the cutover cell's, made in its pair with both branches covered.
2. **Silver, meta and `_ops` scope is OPEN at Andrew** (the CVO's v0.4 item 4). Do not cut silver-side cells until he answers. If he says
   firm scope for every tier, round 2 adds the silver move and the silver readers to the same single cutover.
3. **The deploy hazard: restore the two key-function files to their pre-round bytes now, in one commit.**
   - The files are `data/black_diamond/scripts/bronze/_monolith_bronze.py` and its mirror `data/canonical/schwab/silver/_canonical_silver_lib.py`.
   - Measured ~14:5xZ: merge 293346aff1 is on origin/box/laptop but NOT on origin/CLOUD. The deployed
     `s3://opal-data-bd/code/bronze/_monolith_bronze.py` (md5 89470f2fc70983111783a564766b7068) equals the PRE-round bytes (293346aff1^1),
     so production is untouched.
   - The restore makes box/laptop safe to integrate without holding every other laptop commit. Round 2's key cell then lands the firm form
     in one release with its readers. Other round-1 files that have no deploy mapping may stay; BF-k-1's rework replaces them.
4. **The Alongside workstream (FWD-8)** waits on the ratified-text re-sign of v0.5 or later, as before.

## 3. Enrichment list for round 2

- R2-1: the key function in firm form (BF-k-1 rework, with master filtering).
- R2-2: the converter takes the master from the file name (code and twin).
- R2-3: the readers, the puller and the trace oracle in firm form (BF-r-1, BF-w-1, BF-t-1 rework).
- R2-4: the move tool in firm form (BF-m-1 rework).
- R2-5: the Terraform cell: IAM and event rules for the firm prefixes.
- Then the release acts on the firm form under the never-widen pair, with the old-key delete held for Andrew.

-- 1.0.0_SA_CTO
