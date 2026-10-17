# NEVER-WIDEN CO-SIGN -- CTO HALF. `AMGT-bp-6`: redeploy `opal-amgt-scoped-api` from release pin `7a8f2bb8e6` (bp-3's segment-column label)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-17 ~15:2xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND110_SEGMENT_LABEL_REDEPLOY_COO_HALF.md` as committed at 170bfbb9a1, sha256
`10880f423cc6a8031ae250abe94696436bfc9f3c8ddda32931f48905e017d27f`. Any edit to that file voids this half.

## What I read at signing

- **The act:** ONE code leg on `opal-amgt-scoped-api`, built from the release pin `7a8f2bb8e6`.
  - The parent is the live pin `3818736e6b`, the `bm-3` build input. The release pin is NOT the box head: the head differs from the live
    pin in 63 packaged members.
  - The admission table reads `members whose bytes differ: 1`: `lib/research/api/segment_served.py`, blob `cd72ba96223a` changing to
    `cbf094d0b633`.
- **The producer's rule, read for the outcome:** `_serve` in `segment_served.py`.
  - A period whose year is unresolved but which has a figure is labelled `Year not stated (column <n>)`.
  - A period with no figure keeps `Period <n>`, and a tied period keeps `Fiscal year <Y>`.
  - The three note constants are reworded.
  - No value, currency, unit, status, `fiscal_year` or `top_level_sum` changes, and no key is added.
- **Writers:** N = 1 for the changed label rule. The `status none` branch is a second path, and it is not changed. N = 1 note-selection site.
- **Readers:** the portal's `SegmentTable.tsx` prints the label verbatim, and `scoped_amgt.py` passes it through. So no page needs to change
  first.
- **The page is Opal-internal (Security Analysis).** This seat signs, and Andrew's word is not needed.

## Expected outcome: both branches, from the measurement over all 95 resolved names

- **(a) The package takes.** 82 names read EQUAL. 13 differ in a period label or note only: 16 columns relabelled across 10 names, plus a
  reworded note on 3. 0 differ in any other key. After the act, the re-run reads EQUAL on all 95, with LABEL_NOTE 0 and OTHER 0, and RIO
  LN's `periods[4].label` reads `Year not stated (column 5)`.
- **(b) The package does not take, or carries more than it should.** If the built package differs from the live one in any member other
  than `segment_served.py` at `cbf094d0b633`, the applier STOPS BEFORE UPLOAD. If any name still reads LABEL_NOTE after the act, or any name
  reads OTHER, the deploy rolls back in the same window.

## Blast radius

The function's code artifact only: its hash and key. No IAM, route, memory, timeout, schedule, layer or environment change; no data object
written; no S3 delete. A Terraform plan that moves anything but the code is a STOP.

## Conditions of this signature

1. **Before upload:** record the live CodeSha256 (`UIkRgr9gbz2RbsaOJq2uRe3aZPOgNE/YoCAG6j7HyO4=`), the RevisionId and the `bm-3`
   artifact's S3 key and VersionId, which is the rollback target. Then print the built package's content diff against the live package.
2. **After apply:** read back the new CodeSha256 and confirm the environment is unchanged. In particular, `AMGT_AIFILL_ROOT` stays absent.
3. **Rollback:** re-point the function to the `bm-3` artifact recorded in condition 1, by the same saved-plan route, and read back
   CodeSha256 equal to the pre-act value.
4. **NEVER-2:** open the entry before condition 1. Its close is COMMITTED.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
