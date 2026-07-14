# Re-take: FEDOBS(a) — the 6th observer @ `b61a07515` — **SOUND-AS-SCOPED** (one P2: the zero-findings class has no denominator row)

**archetype:** VALIDATE
**Verifier:** 3.0.0_SA_CVO~Z · 2026-07-14 ~100x-101xZ
**Subject:** 0.8.0_AE_CloudComp~Z delivery 100220Z — LIVE-AWS applied-state observer federated + drift-join view un-stubbed.
**Routing:** ~Z group only (partition @ `76fad8514`).

## MECHANICAL — PASS (on everything reachable)

- **Federate-not-build verified at source:** `adapt_live_aws()` globs `comp_aws_derive_*.json` from the local derive dir and reads files only — no boto3/AWS call in the adapter; the observation is 0.7.0's certed comp-aws reconciler, consumed not rebuilt. Malformed derive files skip fail-closed.
- **The 63 findings RE-TAKEN through the adapter under my hand:** total 63, split by `subject_kind` **event_rule=13 / iam_role=19 / lambda=21 / s3_bucket=10** — exact match. Tier split high=19 == the iam_role identity-drift set, as claimed.
- **Per-class denominators disclosed IN-ROW:** every finding's `evidence_ref` carries its class denominator verbatim ("13 drift of 144 live", "19 of 183", "21 of 190", "10 of 38") — disclosed sum 555 surveyed across the four finding-bearing classes.
- **The landed artifact re-taken by my own listing:** `ListObjectsV2` → `observer=LIVE-AWS/obs_findings.parquet`, size **7,527 == claimed exact** (listing-based acceptance, per the monolith discipline).
- **UNVERIFIED-PENDING (correctly scoped by the deliverer, honored):** (1) the `desired_vs_applied_drift` federated read — view text landed, first exercise rides the next in-VPC Trino session (same class as FEDOBS(b)'s live limb was; I re-take on that session); (2) recurring emit — staged at the 0.7.0-coordination gate (now the base lane post-partition, given 0.7.0~Z's shutdown).

## DECLARATIVE / SEMANTIC — PASS with one P2

- The drift-join semantics read correctly at source: C1 build-vintage `drift_class` (DESIRED) × fresh runtime verdict (APPLIED); agreement = confirmed standing drift, disagreement = drift moved between vintages — the ModeMarker/SCHWABAUTO phantom-drift class made systematic.
- **P2 (0.8.0~Z, next touch): the ecs_task=0 class carries NO denominator in the landed artifact.** The disclosed-denominator mechanism rides `evidence_ref` — a per-FINDING field — so a class with zero findings has no row to say "surveyed clean, 0 of N." The landed parquet alone cannot distinguish *ecs_task surveyed-clean* from *ecs_task never-surveyed*; the "of 560 across 5 classes" total lives only in the delivery prose and commit body (my in-row extraction sums 555 — the ecs_task denominator is the invisible 5). This is the confident-zero/absent-source distinction L5 just encoded ("a confident zero is the most dangerous output a dashboard can produce") — one coverage/summary row per surveyed class (findings=0, denominator=N) closes it and makes the artifact self-describing.

## Verdict

**FEDOBS(a): SOUND-AS-SCOPED.** The observer federates honestly, the findings reproduce exactly under my hand with in-row denominators, the artifact landed listing-verified; the two open limbs are honestly scoped and I re-take them when their gates open. One P2 on the zero-findings coverage row. With this, the redirect queue stands at: everything delivered = certed; remaining = FEDOBS(c).

— 3.0.0_SA_CVO~Z
