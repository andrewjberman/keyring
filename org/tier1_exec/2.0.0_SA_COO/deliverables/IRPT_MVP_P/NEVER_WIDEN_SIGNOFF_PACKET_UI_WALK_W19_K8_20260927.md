# Never-widen sign-off packet -- WINDOW 19: K8 again on the render-grant decrypt fix and the page's receipt poll, plus K10

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~23:0xZ.
**Walker:** `2.0.0_SA_COO~D` only. **Ledger (opened before any write):** `irpt-ui-walk-principal-w19-20260927`. It also
closes the A1 of `irpt-adapter-render-grant-kms-20260927`, the arm-3 re-run of `irpt-export-async-submit-20260927`, and the
A1 of `irpt-status-dates-rebuild-20260927` (K10).

This packet is window 18's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W18_20260927.md`, blob b74de7e4, both halves) PART B
ONLY, plus K10 (window 15 amendment 1's read-only page read), with the deltas below. There is no part A (no design walk)
and no part C (no vendor read). Every unnamed section
reads as window 18's part B, including K7/K8, the route classes, the byte-proof, the /download body out of the HAR, and
the %PDF audit on the SERVED object.

## W19-1 -- why a re-run (CTO 102119, 102135, 102137)

Window 18's arms 1, 2, 4 and 5 PASSED on the served async export. Arm 3 failed at the render:
- the adapter could not `kms:Decrypt` the render grant under the evidence bucket's S3 Bucket Key (corr-6c1a41bcf09a);
  fixed by packet f7aa7b3c;
- the page did not start its receipt poll on the data-less QUEUED answer (S26); ~D's direct act on local portal DEV.

## W19-2 -- the pins, re-read at create

- irpt-performance-adapter role policy `irpt-performance-render-grant-read-policy` = backend c8572cb1bd, read live
  (bucket-ARN context, core key only), with the adapter code `bOefL9nx..` and NO plan;
- irpt-export-render `Ulim/gmf..`, `IRPT_EXPORT_RENDER=on`, retries 0; the SSM document irpt-export-render-run v5;
- irpt-status **`HyEyoJ67..`** (the template status dates, ledger irpt-status-dates-rebuild-20260927 D1 23:00:34Z);
  irpt-directory-search `o1TXq5PH..`;
- the page: local portal DEV **`8808eeb6`** (~D 102191: TO-IV-e-67 merged, the S26 poll fix; tsc 0, lint 0, suite
  924/27/5), 0 tracked changes.

If any differs, the window does not open.

## W19-3 -- the arms

0. **K10 (read-only, before K7):** the history lists window 15's REQ-67e12718. Its status read on the portal (the
   X-IRPT-Status-Dates prospect-v1 read) answers READY ANALYSIS_READY, and the report RPT-5288c06d opens. There is no
   submit and no upload. This is ledger irpt-status-dates-rebuild A1; it decides DSGN_IRPTV1-S25 (CTO 102187).

1. ONE POST answers QUEUED with an `exr_` revision in under 29 s (HAR).
2. The page polls the receipt on that `exr_` id without a reload (S26), NOT_READY until the render ends.
3. **The render's Performance read as RENDER_DELEGATE answers without AccessDenied** (adapter log for the render's
   window: 0 `irpt_internal` AccessDenied). The receipt reaches **READY with a %PDF** on the served object, or a named
   FAILED that is not the W18 cause. ONE download.
4. The grant and the receipt name THIS window's principal; the owner row is unchanged; exactly 2 irpt-export-render
   invocations for the ONE POST.

**K1-CRED** (CRO 102121, row S172): deleted through `walk_principal.py`/boto3 when ~D reports logged in. It counts as
done only after a ParameterNotFound read, with its timestamp in the ledger beside the delete.

**On an export-code arm failing:** roll back per dd91065c section 3 in the same turn. On the adapter arm failing:
roll back per f7aa7b3c section 3.

## What the halves sign against

This file's committed blob; window 18's part B text (b74de7e4) as amended here; the pins in W19-2 with ~D's pin named;
the arms in W19-3; and the K1-CRED rule.
