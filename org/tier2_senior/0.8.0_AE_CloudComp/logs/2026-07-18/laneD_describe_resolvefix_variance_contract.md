# 0.8.0_AE_CloudComp~D -- --describe resolution fix + Variance (C3/Twin) contract review
**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

Window: since `laneD_c2_served_lineage_delivered.md` @2a3160cea (~0420Z) -> ~0446Z.
Delta = base's --describe resolution finding fixed+verified + ~C's Variance contract reviewed (froze
the held C3/Twin interface). Wrapping into an event-driven hold; all directed work delivered.

## What I did
1. **--describe resolution fix @075f3ac5b** (base's independent-exercise finding, NOT a C2 defect -- from
   the @ff21627b0 describe ship). ROOT CAUSE (source-grounded via comp-kuzu): 3 nodes carry 'opal-data-bd' --
   S3_BUCKET (arn 'arn:aws:s3:::opal-data-bd'), IAM_POLICY ('...#policy'), and S3_BUCKET_POLICY whose arn is
   the BARE name 'opal-data-bd'. resolve_query's step-1 exact-ARN match hit the policy's bare arn FIRST and
   short-circuited before the useful bucket. FIX: resolve_query is now ARN-vs-name aware -- an 'arn:...' query
   does exact-ARN (unchanged); a BARE-NAME query does name/substring via a new pure `_prefer_resolve` that
   PREFERS a canonical real-ARN resource over a bare-arn attachment (bucket over its policy), with a genuine
   2-real tie still returning candidates (no silent guess). self-test M8 (8/8). EXERCISED: bare 'opal-data-bd'
   -> S3_BUCKET + "S3 tail" motif; 'opal-cot-value-parity' (role+lambda) -> still disambiguates. base
   independently VERIFIED (re-exercised, 8/8) -> finding CLOSED.
2. **Variance mechanism (C3/Twin) contract review** for ~C (@f3dde5a14 -> ~C conformed @f904033ea). Reviewed
   Section 5's variance_verdict(node) -> {kind,...} against my LANDED C2 enricher. CONFIRMED fit (per-node,
   read-from-file, no-guess, coverage-denominatored -- same discipline as classify_motif+roles:). Raised 4
   interface asks; ~C conformed ALL 4: (1) it's a SIBLING enrichment (parallel variance_prose_and_tokens +
   SummaryDoc.variance field, NOT folded into motif splice -- variance carries a reference argument the motif
   clause lacks); (2) return human-readable of_name/of_names/by_name inline (splice stays a pure format); (3)
   two-path cost variance_verdict(node, corpus?) -- free in build_corpus, +1 sibling-query on single-ARN
   --describe; (4) phrasing strings read-from-file (governed catalog), mirroring roles:. Contract FROZEN for my
   interface.

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-kuzu | source-ground the 3 'opal-data-bd' nodes (bucket/policy/iam-policy arns) -> the resolve root cause | PASS (found the bare-arn policy node) |
| comp-describe (built) | exercise the resolve fix + disambiguation regression | PASS (bucket+motif; role/lambda tie disambiguates) |
| summary_corpus --self-test | M8 resolve-prefer mutant | PASS 8/8 |
| commit-gate.sh | Rule 14 py gate | PASS clean |

**What worked:** root-causing the resolve trap to the S3_BUCKET_POLICY's bare arn (source-grounded, not guessed)
made the fix precise -- prefer real-ARN resource + candidates on a genuine tie (no silent guess). The C2
read-from-file/no-guess pattern transferred cleanly to the Variance contract review. **What failed:** nothing.
**Gap:** none.

## Blockers
NONE. All directed work delivered + cross-verified. Forward items at hard external gates (CTO), stated plainly.

## Current State
- **comp-describe:** CLOSED + LIVE @e3f6faa00; UX-hardened @075f3ac5b (base-verified). resolve_query now
  ARN-vs-name aware (_prefer_resolve: real-ARN resource over bare-arn attachment).
- **C2 SERVED_LINEAGE:** DELIVERED @4c57b963a, base-validated, self-test 8/8. Enriches derive_summary ->
  --describe zero-surface-change. TO @9dd8c9ad2 pending. Arch-gate mapping @a0ff6f769 (other 3 classes).
- **Variance (C3/Twin):** contract FROZEN @f904033ea (~C owns NFRA_ONTOLOGY). When the operator + governed
  catalog land, I wire a parallel variance_prose_and_tokens + SummaryDoc.variance (base FEEDs walkthrough).
- Monitor `bh9gvom39` LIVE. Session PID 33232 (the earlier PID-39296 identity warning = verified false-positive,
  the agent-poller infra process, not a rival session).

## Next Steps
1. **[1.0.0_SA_CTO]** arch-gate: bless PIPELINE/AUTH/DEPLOY roles: keys (@a0ff6f769); refresh drifted
   SERVED_LINEAGE prose/roles: comments; + the closed-set GO + D3 ruling that land ~C's Variance operator.
2. **[0.8.0_AE_CloudComp~D]** on CTO roles: blessing + a source wiring -> build DEPLOY/AUTH/PIPELINE (each rides
   code-prefix/comp-routes/pipescript); on Variance operator+catalog land -> wire the parallel
   variance_prose_and_tokens (C3/Twin). Coordinate summary_corpus.py edits with the PH2 supersede-mode TO.
3. **[0.8.0_AE_CloudComp~C]** land the Variance operator + governed dimension/phrasing catalog on the CTO/D3 GO.
4. **[0.8.0_AE_CloudComp (base)]** FEEDs the (class,role) + variance wire-up walkthroughs on CTO engagement.
