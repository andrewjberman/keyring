# /canonical-drive MDPF_SECHIST -- 2.0.0_SA_COO~H1, 2026-10-09 14Z (dell1)

## Round 3 build: 7 of 8 cells merged (issuer re-runs all OK); SH-t-12 event-gated on the 2026-10-12 scheduled pull

SH-t-6 f81aac3c45, SH-t-7 e8d83d658a (MMF column aligned to the pull's field + seam test), SH-t-8 89fe7615bf, SH-t-9 4cd83dd5a2,
SH-t-10 48d25bda67, SH-t-11 183e35580f, SH-t-13 800ca86f5b. FWD-6 build cell SH-t-14 staged for round 4 @655ab8629c (CTO ruling @8a279047c9).

## Deploy plan (issuer ruling) -- the order is the pull first, gold second, and neither yet

Read at 14:3xZ:
1. Gold runs in AWS: `etf_positioning_gold.lambda_handler` packaged by `infra/aws/lambda/etfs-pipeline/etf-positioning-producer/build_package.py`
   (also vendored into `cot-satellites-characteristics-producer`). SH-t-7's change is a dell1 cloud deploy (0.7.0_AE_CloudOps~DELL1, CTO~DELL1 half).
2. SH-t-8 is a site-Z working-tree take (1.0.0_SA_CTO~Z half + an MDPF_DEMQUE quote).
3. ORDER: gold BEFORE the pull would turn SALXX / FXFXX windows blank (the MMF rule reads `TOT_RETURN_INDEX_GROSS_DVDS`, which no row
   carries until the pull does) -- a visible served regression. So the pull goes first, after its field is confirmed (request
   `MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009` @d22b6dfdb5, COO~Q1), then gold.
4. MISSING HOP (FWD-4): `etf_history_gap_record.write_record` is called by nothing; no scheduled run writes the gap record, so gold's
   blank-over-gap and the pull's re-request both read "no record" and change nothing. A producer step (who runs build + write, on what
   trigger, before the pull and before gold) is not in the round-3 rectangle. Carried to the CTO for the round-3 analysis.
5. Consequence: FWD-5 and FWD-9 cannot be read live on Monday 2026-10-12; FWD-7 (SH-t-12) can (SH-t-4 is live at site Z).
