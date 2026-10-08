# NFRA_TRNSPT decomposition -- ROUND 10 (2026-10-08, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on 1.0.0_SA_CTO~DELL2's round-9 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_9_20261008.md`
@9c6c91c505 (msg 1579). FWD-5 ACCEPT: "an analyst who now opens a file to find what was said about one company gets it without opening
the file".

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-q-10` | the company read over Research silver: given a company (name or ticker, with optional aliases), the matching speaker turns across the stored meetings, `held_out=false` rows only | FWD-5 | dell2 worker, then ISSUER (one real query from S3) | LOCAL | worker-light | -- |

**Chains.** A = TR-q-10 (slot ~1). Fan-out 1 of 1, cap 8.

**Issuer rulings.**
1. **Source:** the 29 objects under `s3://opal-data-transcripts/teams/transcripts/silver/research_meeting/` (round 9). The function takes an
   s3 client (tests use a fake); it never reads `research_transcripts/` files, so the caller opens no file.
2. **Matching:** case-insensitive whole-word match of the query and each alias on the stored (wiped) `text`. No alias registry exists in
   the repo for these meetings (`research_transcripts/index/mentions.jsonl` has 4 lines), so aliases are a caller argument. The wiped
   text may have removed some names; the result says so in its reason when nothing matches.
3. **Criterion (1)** is the issuer's close act: one real company chosen at close from the stored rows, counts printed, no text in the
   record.

## Rule 24 record

Domain: analysis s.2 E1, criteria (1)-(3). (2) and (3) = TR10-q10-AC1; (1) = the issuer's close. Remainder: none.

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R10_CHECKS/r10_checks.py`, dry-run at base box/dell2 f62d3f661e: q10-read FAIL (absent).
