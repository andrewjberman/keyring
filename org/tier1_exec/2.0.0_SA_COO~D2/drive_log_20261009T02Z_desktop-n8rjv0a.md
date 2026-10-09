# drive log -- 2.0.0_SA_COO~D2 -- 2026-10-09 02Z -- desktop-n8rjv0a (dell2)

## ticks 220-228 -- round 34 issued, executed, drained, MAY-CLOSE

| project | limb | round | TOs | act |
|---|---|---|---|---|
| IRPT_DASHBD | L10 -> L6 -> L7 -> L8 | 34 | 3/3 complete | issuance @8a02a14a90; kit path @7aea38af1e; drains @9782652f3d, @668b3ec286, @2bc194b282; round-close-check MAY-CLOSE |

- Input: CVO ADJUDICATION_v18 @73fda8626e and the CTO's round-33 ADDENDUM 2 @47c849d75b (msg 2116).
- Checks `deliverables/2.0.0_SA_COO~D2/checks/r34/p34_round34.py`: 6 FAIL at base 5baf94294f (~39's test 1/3 failing, the shim detected);
  planted 5/5 PASS.

### Results

- **DB-b-66 (E1), worker ~43, @668b3ec286.**
  - `~35/crossover_e1.py` and `~39/large_flow_e3.py` import the reader's fee base. Tests: 3/3 each, with new "caller" tests for ~35.
  - The shim is removed from `~42/near_zero_e3.py`. The shim-free re-run gives fixed_within **79 of 79**.
  - The tie-out total is **8,433 of 9,078**: the reader grades 8,385, 31 of the near-zero rows are already counted there, and +48.
  - No record changed on re-run. Row W43-S1.
- **DB-b-67 (E2), worker ~44, @2bc194b282.** The kit (C:/opal-inbound/kit-py312-dashbd/kit-py312-dashbd-20261009.zip, sha256
  c76af678..., verified by the issuer) ran offline in a separate venv: Python 3.12.10, pandas 2.2.3, numpy 1.26.4, pyarrow 14.0.2.
  - Lots peak: **1,500.7 MB, FITS** 2,048 (the 3.0.6 reference was 1,763.4).
  - 7,604 accounts at batch 1000, total 447 s.
  - Row W44-S1: boto3 and psutil were side-loaded from dell2's site-packages, offline; the measured libraries are the kit's.
- **DB-b-68 (E3), worker ~45, @9782652f3d.** FLOW_TIMING_AFTER_FEE_BASE 116: **114 within now** under the reader (flow-start 108, guard 3,
  first-day 3); 2 named (a guard day at 0.40 pp; a flow 3.08x the balance at 0.92 pp, which needs BD's flow date and is out of bounds).

### For the CTO

- The activity-and-lot release's peak on the served pandas reads **FITS**, measured. The release's remaining gates (S31-S33, the COO and
  CTO halves) are the CTO's to rule.
- Tie-out state: **8,433 of 9,078** within 0.35 pp.

### Messages

Acked: CTO 2116, MSTR 2139 (/keep-driving ON), MSTR 2178 (kit landed).
