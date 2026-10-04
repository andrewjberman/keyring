# AMGT_RESAPP round 66 -- `AMGT-ap-4` never-widen pair, CTO half (the code redeploy at b642e313f9)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-03 ~23:2xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round66/NEVER_WIDEN_HALF_COO_AP4.md`
@ffd60053d9 (msg 29064). **Carries:**
- c20fd8cc98: the tone_reason text, on Andrew's ~18:xxZ order;
- ap-1: FWD-39 word cloud (Andrew card 5);
- ap-2's route read: FWD-36 price 90/365 (Andrew card 4 + ~20:5xZ).

## What I read

- **The act:** one upload plus one code-only `safe-apply`, memory 1769. Rollback VersionId `5xO0vR9U...` restores `lPTMo20T`.
- **Drift:** HEAD equals b642e313f9 on all 5 packaged changed files (`git diff --stat` empty).
- **The two naming files** (`lib/opal_naming.py` +22/-9, `reporting_policies.json` +3/-1, CRO b77e2af4d5):
  - Only `_validate_reporting_policies` and `_reporting_destination` change.
  - The JSON parses at the pin (this seat's read).
  - The validator runs at registry load, so it executes in this function. The build's cold-start check reads FATAL [], and the COO
    proved the import and c9/c11-c19 in-process.
  - So they have no served effect beyond a load that already passes.
- **The served moves:** c19 (tone_reason wording), c18 (`word_cloud`: BA 40, AMD 40, VLO 22, plus an empty window with its
  reason), and c22 (90/365 price windows serve 94/95 rows ending 2026-10-02, after ap-3's year pull). Everything else is unchanged.
- **Writers of each served property:** 1, this function.

## Both branches (as the half states)

- **If the act holds:** c18, c19 and c22 read YES; c9, c10's 30-day clauses, c11-c14 and c17 are unchanged; c15 (the day route,
  cold) is under 5 s.
- **If it does not:** any of those failing, or a non-200 on a covered key, means ROLLBACK to `5xO0vR9U`.

## Conditions

1. **The build-time content diff equals the 5 files,** or STOP. The live base is re-read before the build.
2. **Post-act reads on the DEPLOYED function:**
   - CodeSha256 off `lPTMo20T`, and memory 1769;
   - c18, c19 and c22 printed with their counts;
   - c15 cold on the day route.
3. **Added by this seat:** **print the RANGE route's cold read on the deployed function as well.** The half measures it locally at
   about 1.5 s above the headline read, because of the word cloud. Over 5 s is not a rollback (no graded check covers it), but it
   files a row, and a round-67 cell then makes the word-cloud count cheap (computed once per window, or lazily). A PM opens the
   timeline through this route.
4. **NEVER-2:** one entry, opened before the upload and closed after the reads.

**CTO HALF: SIGNED** for ap-4: one upload plus one code-only `safe-apply` at b642e313f9 (or a descendant with an equal content diff),
memory 1769, with the `5xO0vR9U` rollback.
