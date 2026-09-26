# Hops 5-7 pre-flighted offline -- the deployed resident runs window 3's real composition to READY

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~19:1xZ.

**Order:** Andrew at the ~Y terminal, "do 1 3 and 4 in order" (option 1 of ~Y's /next-steps); the CTO frame is 101442 (no
hop-3 window until the pre-flights of hops 5-10 land).

## Result

With the lane fix (`submission.py`, in `P_HOP3_SUBMISSION_FIXES_20260926.patch`), the DEPLOYED resident package
`f624e8a72f` runs the analysis_generate job produced by the deployed generate code (plus the fix patch) to **READY**:
- one delivery, `handled=1`, and one REPORT# row published;
- the job row is READY, the message is deleted, and 0 refusals.

As deployed, without the fix, the same world is **refused at admission** (`EXACT_PROSPECT_OWNER_REQUIRED`), with 0 vendor
calls and the job left RECEIVED. So the resident must ship the fix.

## Instrument (in `live_walk/`)

- `readthrough.py`: one typed DynamoDB store behind both the client and the Table resource, plus S3, SQS and write
  capture. Reads are live; writes never leave the process.
- `offline_submit_proof.py`: phase 1, generate. It dumps the captured world (rows, objects, the queue message) to
  `--out`.
- `resident_job_preflight.py`: phase 2, the resident, in a separate process on the package's own code.
  - Started as the host starts: package root, resident_main's paths, `resident_installed.build_resident_runtime`,
    `poll_once`.
  - Stated departures:
    - the clients are the phase-1 world;
    - the vendor is the connected harness's recorded HAR script, run from the package's own fixtures, with the upload
      echo seeded from the frozen holdings;
    - the synthetic PDF and its synthetic census are generated in an isolated process from the tree's
      test_publication; the pinned production census describes a real vendor PDF that only a vendor call can produce;
    - the session secret is the replay bundle.

## What the resident did (59 stages; the vendor was replayed, and nothing left the process)

1. `poll_once` -> `execute` -> `current_authority.decide` (ALLOWED for the Opal actor, graded again at every phase) ->
   `durable_job.claim` (lease plus fence) -> `frozen_worker.prepare` -> `composition_admission.validate` (the lane fix
   admits) -> `recipe_inputs`.
2. Vendor, replayed:
   - `GET /custom_pdf_reports/generate/14141822` (the OVERVIEW template);
   - **the holdings upload: the resident SENDS a CSV file part `Symbol,Dollars` carrying AAPL 10.01 / VNQ 2.02** (from
     the v2 template input);
   - `POST /model_portfolios/fixed/` (create), the status, `validate_report_securities`, `POST /custom_pdf_reports/14141822`
     (generate), then the download.
   - Intents and checkpoints are recorded along the way (SUBMITTING, checkpoint_*).
3. Retain, certify, publish:
   - the ORIGINAL_VENDOR_PDF in `opal-data-irpt/irpt/cottonwood/state/vendor_documents/`;
   - the EXTRACTION_EVIDENCE in `state/extraction_evidence/`;
   - retention promotions;
   - `publisher.publish` -> `extract` -> `certify` -> the ANALYSIS report in
     `platinum/analysis_reports/RPT-.../<sha>.json` (4192 bytes);
   - `report_index.publish`: one transaction, ConditionCheck (lease, fence, CERTIFYING) plus Put
     `REPORT#RPT-...#<revision>`;
   - the job goes READY, the lease is released, and the message is deleted.

114 captured writes, all in memory.

## Limits (what this does not prove)

- **The vendor is replayed.** The recorded responses are the package's own fixtures; a live YCharts answer can differ.
- **Certification ran on a synthetic PDF and census**, not the pinned production census. That census was scraped from a
  COMPARISON report (`YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909`), while the default Generate is an OVERVIEW. The
  extractor's own docstring says it is built against the three retained real vendor PDFs; how an Overview certifies
  against that census is first seen live.
- **Conditions:** attribute_not_exists and the NormalizationStates conditional put are evaluated. Every other
  ConditionExpression is recorded, not evaluated: a single-writer run is not a race test, and the unit suites own it.
- Hops 8-10 (the sections GET, reload/history, export) are option 3, next.
