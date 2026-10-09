# drive log -- 2.0.0_SA_COO~D2 -- 2026-10-09 01Z (round 33) -- desktop-n8rjv0a (dell2)

## ticks 214-219 -- round 33 issued, executed, drained, MAY-CLOSE

| project | limb | round | TOs | act |
|---|---|---|---|---|
| IRPT_DASHBD | L10 -> L6 -> L7 -> L8 | 33 | 3/3 complete | issuance @d6eee7fc1f; drains @9e9b3c49f2, @58fa2adf16, @96a0c9991a; round-close-check MAY-CLOSE |

- Input: CVO ADJUDICATION_v17 @e87c35ec88 and the CTO's round-32 ADDENDUM 1 @78928255f6. The CTO's rulings:
  - adopt both W39-S1 fixes;
  - measure the served pandas 2.2.3 by one QA invoke, or report a measured refusal;
  - a kit request follows only a refusal.
- Issuer pre-read at the cut: the deployed reporting-gold does not declare `account_activity_lots.py`, so E2 reads the deployed bytes
  before any invoke.
- Checks `deliverables/2.0.0_SA_COO~D2/checks/r33/p33_round33.py`: 6 FAIL at base beca8909cd; planted 6/6 PASS.

### Results

- **DB-b-63 (E1), worker ~40, @96a0c9991a.** The reader of record adopts:
  - BD_FEE_FIELD_IS_FLOW: fires on 85; 69 out->in, 0 in->out;
  - FIRST_DAY_FLOW_AT_START: a structural predicate (first-day flow >= 25% of prior value, with the 2% guard); fires on 144.

  Within goes from 8,315 to **8,385** of 9,078: 84 in, 14 out, all FIRST_DAY_START_NOT_BD and named. A control with the predicates
  forced off gives 8,315 exactly. Writer census 1 of 130. The ~35 and ~36 importers are byte-identical.

  Rows W40-S1 (two callers broken; below), W40-S2 (predicate choice; the CTO may re-set it) and W40-S3 (applied to all 9,078).
- **DB-b-64 (E2), worker ~41, @9e9b3c49f2.** The served function irpt-49f-reporting-gold-lambda (Mex71..., 2026-10-03) runs pandas
  **2.2.3** (numpy 1.26.4, pyarrow 14.0.2) but packages **no lots producer** (5 modules). No invoke was made; the verdict is **REFUSED
  (measured)**.

  Per the ruling, the kit request was routed to 0.0.0_AB_MSTR~DELL2 at 01:31Z. It is laptop NFRA_CTLPLN.TO-CT-k-2 AMENDMENT 10
  @70b8dcd818, a Taildrop zip, ETA ~02:1xZ (MSTR msg 2104).
- **DB-b-65 (E3), worker ~42, @58fa2adf16.** NEAR_ZERO_BALANCE 153 splits into 9 sub-classes:
  - 2 fixed by landed-gain grading (79 of 79 tie): BD_FEE_FIELD_IS_FLOW 31, GAIN_AGREES_NEAR_ZERO_BASE 48;
  - 7 named.

  Overlap with round 32's in_to_out or LARGE_FLOW_DAY is 0.

### Regression found (rows W40-S1, W42-S1)

Round 32's reader promotion (DB-b-60) removed `mean_daily_value` from ~36's classifier namespace. Two downstream callers now raise
AttributeError at HEAD: `deliverables/0.9.0_WK_IRPT_DASHBD~35/crossover_e1.py` and `deliverables/0.9.0_WK_IRPT_DASHBD~39/large_flow_e3.py`.
DB-b-60's "importers unchanged" criterion covered only the two named importers, not their callers. No served value moves; the records stand.
A one-line repair cell (import from the reader) is the candidate for round 34.

### Messages

Acked: CTO 2030 (round-33 analysis), MSTR 2071 (rule 30 naming gate REFUSES), MSTR 2094 and 2104 (kit routing and ETA).
