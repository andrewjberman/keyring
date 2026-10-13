# Disarm evidence: MDPF_DEMQUE-D1-W37-S1 and -S3 (2.0.0_SA_COO~Q1 as disarm owner, 2026-10-13)

**S1 (CFNCASH priced as P1).** Hazard: the P1 slice would have asked Bloomberg to price a 7-character cash identifier (3,326 cells).
Fix merged @1d7ad82723: `card_a_slice.py` marks a name unresolved (`cash_identifier`) when its identifier is not exactly 9 alphanumeric characters or starts with `FDIC`.
Measured at HEAD after the merge (`p1_coverage.py`, `dq_t46_real.py`, rc=0): P1 609 names, **606 priced, 3 unresolved**; the three are FDIC66606, FDIC66853 and CFNCASH. No
draw of the P1 request has been made (the CTO's hold, msg 4904; Andrew's form is open), so nothing was spent on it.

**S3 (check read a key the naming gate refuses).** Hazard: acceptance AC2 read `bd_units_value`; the module prints `blackdiamond_units_value`.
Fix: the check script `R9_CHECKS/dq_t46_real.py` reads `blackdiamond_units_value` and expects priced 606 (issuer amendment @19b2775741). Run at HEAD: `COVER-REAL-OK`.

Both rows are disarmed by a change that is on box/dell1 and by a real run that read it. -- 2.0.0_SA_COO~Q1
