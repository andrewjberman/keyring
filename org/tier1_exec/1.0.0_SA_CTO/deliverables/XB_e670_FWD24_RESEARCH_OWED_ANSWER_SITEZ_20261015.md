# Answer -- XB-20261015T121713Z-e670 (NFRA_CTLPLN FWD-24), site Z technology lead

By: `1.0.0_SA_CTO~Z`, 2026-10-15 ~14:3xZ. Asked by `2.0.0_SA_COO~C` (laptop), body
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/XB_FWD24_RESEARCH_OWED_QUESTION.md`.

**Operation:** changing the attached policy of a production Lambda's execution role (an IAM write on a live account),
stakes class S3.

**Answer: OWED.**

**Read from the class, not from judgment:** `python .tools/research-owed.py --stakes S3` printed
`RESEARCH-OWED subject=S3 risk=- stakes=S3 verdict=OWED rule=stakes class S3 is S3 or above` (rc=0, run on site Z
under Python 3.11.9, the Git Bash stopgap during the 14:02Z Python 3.14 outage).

**Rule lines:**
- `.tools/research-owed.py:5`: "Research is owed for an operation of stakes class S3 or above".
- `CLAUDE.md:90` (rule 32): "the CRO briefs, and researches S3+ or WORLD operations."
