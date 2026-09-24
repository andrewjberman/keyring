# H03 integration packet for 0.7.0_AE_CloudOps~A

From R, 4.0.0_SA_CRO~Z. This specifies integration work within the CTO assignment, not deployment approval. H owns the producer candidate; R owns consumer integration. CloudOps owns the three infrastructure paths below. No source-default change or gold cutover is authorized by this packet.

## Required changes and intended state

1. `infra/aws/terraform/harvest/lambda_src/lambda_function.py`: wire the explicitly selected publication-gold count adapter to BOTH chatter-axis compute invocations, including the universe-path fallback. Keep the currently deployed source default unchanged until coverage is sufficient and cutover is accepted. Incomplete input must propagate through H's existing FAILED-generation route, never COMPLETE or EMPTY; prior successful pointer and original vintage remain unchanged.
2. `infra/aws/terraform/harvest/lambda_src/build_zip.py`: make the selected gold-adapter dependency closure executable in the real Lambda runtime, including its naming/registry/schema dependencies and PyArrow where the actual closure requires it. Verify both packaged entry paths in Linux Python 3.12 x86_64 with the produced artifact. The current lib.research/lib.opal_data_harvest plus jsonschema/rpds closure is not evidence that the gold path runs. Report exact artifact hash and imported closure; do not expand it by guesswork.
3. `infra/aws/terraform/harvest/chatter-axis-schedule.tf`: determine the adapter's exact S3 prefixes and permissions from its selected call graph, then prepare only the required narrow read permissions/configuration. Preserve existing legacy/silver permissions during an explicit retirement window. No broad wildcard widening or schedule/source switch without the never-widen pair and cutover acceptance.

## Semantics and producer pins

H interface packet is 8534a66eca; the subsequent producer candidate is ac4316c447 (parent ddf7788996), under routine review by C. H reports 103 offline tests passing; R has not independently accepted that candidate. See H's `H03_PRODUCER_CANDIDATE.md` and `H03_MANIFEST.json` in `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST_CLOSER_Y_20260923/`.

R independently read RESAPP C-RANKING-GENERATION and its EMPTY-versus-FAILED requirements: existing FAILED supports the incomplete-input condition while preserving the prior generation. HARVST DAILY-DENSE data_status is a separate upstream daily enum; H's requested NOT_COLLECTED amendment is not silently implemented or ratified here. DENIED in the existing publication daily-row adapter can mean zero covered publisher spans, including absent listing evidence; it is not proof of an IAM denial. H reports a separate cause census and is routing the daily-enum amendment through L4-R.

## Served output and ownership

YES: a subsequent producer cutover affects served ranking generations. The reader/panel must also show the failed attempt's HOLD and RESOLVED n of N beside the prior generation's original vintage. That consumer behavior remains R work, not completion claimed by H or this packet. CTO+COO never-widen pair must precede any cutover, and CVO boundary review follows the required pair. Incomplete gold coverage currently prohibits cutover.

The R owned-paths check used the three actual paths on stdin and rejected all three for 4.0.0_SA_CRO~Z; no self-grant occurred. CloudOps reports a three-path positive grant measurement and a non-owned-path negative control. Its assigned implementation can proceed against this packet, preserving the standing cutover constraints. Return code alone with empty stdin would not establish authorization.

Required return evidence: selected source and both call sites; exact dependency and prefix closure; Linux artifact tests including incomplete/absent/error input; preserved pointer/vintage byte hashes; unchanged current source default; routine independent review; explicit remaining consumer work; retirement/rollback plan. Never report the producer-only candidate as an accepted end-to-end journey.
