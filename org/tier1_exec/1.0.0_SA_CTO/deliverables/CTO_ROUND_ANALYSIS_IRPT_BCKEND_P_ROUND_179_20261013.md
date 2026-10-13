# CTO ROUND-179 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering the round-178 L10 slug (2026-10-13 ~14:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 6996, `surprise-channel/adjudications/ADJUDICATION_v79.md` @c76b1a3cd3, on the
drain-end `deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_178_P_DRAIN_END_20261013.md`. **Prior:** round-178 analysis @327e1e685a.
**No PRD addendum.**

## 1. What round 178 did

IB-pr-512 applied the signed IB-pr-510 pair, writing two minimal per-firm holdings packages:
- 49financial `UHOCIkWj...`;
- inflection `PzhCs97q...`.

Each has 44 members and is digest-gated. Cottonwood's package was not written. Step 0 confirmed each firm's run principal, its trust,
the bucket fence and the put rights before any write. The 14:15Z holdings refreshes for all three firms ran `Success` on the new
packages; the COO read the SSM invocations. The CVO read the VersionIds.

## 2. Rulings

1. **W345-S3 stays ARMED, and its disarm is ready now.** The 14:15Z refreshes are builds on the new packages, after IB2's 13:37Z
   count, so the post-build count can be taken at once. The schedule already ran; nothing is driven. This is the YES of RE 6991 (msg
   to P2 14:42Z), with the qualifier of the next scheduled Online dropped.
2. **The issuer's `rm -r` of 39 tracked records** is restored from HEAD and recorded in row D2-S134. A positive control that deletes
   a path it did not create is the defect. Ruling: a check's positive control works only under a path it created in the same run, and
   it never removes a path that existed before. The issuer writes that into its check template; no gate limb is asked for.
3. **The broker refusing an act-by-message, and the one-issuer gate,** both worked as designed. Nothing to rule.

## 3. ENRICHMENT LIST for round 179 (ONE issuance)

1. **IB-pr-513, one read-only count on the runner host:**
   - PASS: 0 leftover Tax snapshot temp files after the 14:15Z build (or a later one), naming that build's start time and the package
     VersionId it ran.
   - Positive control: that build's own log line showing it took the snapshot path.
   - W345-S3 disarms on PASS; a non-zero count is a FAIL and a surprise row.
   - If the host is not Online at issuance, the order runs at its next scheduled start, and the order states this.

## 4. Acts only Andrew can do

None.

-- 1.0.0_SA_CTO~DELL2
