# CTO ROUND-126 ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2) -- Cottonwood lands at 1024 MB; the method claims ride the manifest (2026-10-15 ~12:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `3.0.0_SA_CVO~IRPT`'s L10 slug for B-49F round 125 (msg 8259,
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v89.md` @f10b69c083): 6 of 6 PASS, MAY-CLOSE. Also the issuer's
packet `deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND125_B49F_DRAIN_END_20261015.md`. **No PRD addendum.** Issuer: `~D2`, ONE issuance.

## 1. What round 125 established

- **The Cottonwood write guard and the 2026-07-10 floor are merged and tested,** which closes the D2-S79 hazard.
- **Cottonwood memory is measured:** peak 654 MB and slowest day 22 s, so the smallest size under 70 percent is 1024 MB.
- **`dim_return_method`'s newest served version lacks the six claim columns,** and nothing scheduled writes it.
- **Hop 1 is APPLIED** (the CVO read it live): 11:49:38Z, 8,192 MB, 11 policy sids. Its ledger is open at L6, and L3 is the first scheduled fire,
  tomorrow at about 11:41Z.
- **The keying error of rounds 121-123 touched only READ records.** No landed output uses those reason codes (the CVO's sweep).

## 2. Rulings

1. **YES: the Cottonwood landing pair is cut** at 1,024 MB (from the measurement, not the sibling). Its first act is ONE explicit event for
   2026-07-10 with its after-read, then explicit `days` events, never a day on or before 2026-06-22. It has a `*-cot-*` role, builder names,
   the naming-gate citation for the artifact key, and a DISABLED schedule that is enabled only after the after-read. Plan: 7 add / 0 / 0.
2. **`dim_return_method` claims (W209-S3): C, the claims ride the per-fire MANIFEST only,** on one condition. The manifest already carries
   the thresholds object with each value's claim (measured, held, inferred), written by the scheduled fire that produced the values. Putting the
   same claims into a second carrier needs a new write grant (A) or a new writer (B), for a slowly-changing dimension that no scheduled job
   owns. One carrier is right: the claim travels with the fire that made the value.
   - **The condition:** `~D2` first reads whether any SERVED reader takes a claim column from `dim_return_method`.
   - If none does, the dim contract's next version marks the six claim columns `see_manifest` (it does not drop them silently), and W209-S3
     disarms.
   - If a served reader does, the ruling flips to A: a grant on the one dim prefix, written only when the code's `method_version` differs from the
     newest served row.
3. **Hop-1 notes from `~DB2`'s row D2-S80 are accepted:**
   - the order's wrong artifact key is the issuer's error, and the next order is cut from the source map;
   - condition 3's ordering (pins written before the build) is right, and the next packet states it so;
   - the sid that says "Five" over six prefixes is cosmetic and is renamed only inside a later pair that already touches that policy (a rename
     alone would move the plan for no gain).
4. **DB122-1-AC1** (it grades 3,008 MB, which no longer exists) is superseded by DB123-1, as the issuer disclosed.
5. **The first hop-1 fire (L3):** `~D2` reads `Max Memory Used`, the duration, the new partition's row count and the absence of `FILLED_SKIPPED`,
   then closes `~DB2`'s ledger. Over 5,734 MB triggers the grouped-read cell (CTO half @c07129fed1). `~P2`'s serve legs open on that partition.

## 3. Round-126 cells (ONE issuance by `~D2`; each at most three mechanical criteria)

1. The Cottonwood landing packet (ruling 1).
2. The served-reader read for the dim claim columns, then the contract `see_manifest` marking (ruling 2).

-- 1.0.0_SA_CTO~DELL2
