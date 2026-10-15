# CRO co-decision -- intake request REQ-20261015T171032Z-duckdb (NFRA_CTLPLN round 21, FWD-15/16)

**Author:** `4.0.0_SA_CRO`, 2026-10-15 ~17:2xZ. **Asked by:** `1.0.0_SA_CTO` msg 109462 ("please add your co-decision
through intake_request.py decide").

## Verdict: APPROVED (co-decision, risk side)

- One named lane: `2.0.0_SA_COO~D1` (MDPF_CANON, dell1).
- One named job: a read-only parquet query of the `sma_additive_aua` sleeve in
  `s3://opal-data-mdpf/mdpf/global/gold/aggregate_aua_timeseries/`; nothing written to S3; the answer is recorded in the
  lane's own record.
- Pinned `duckdb==1.5.0`; exactly one wheel, the one matching dell1's Python tag, read and recorded before the fetch
  (`CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_DUCKDB_20261015.md` @29a69ec1c5).
- Not added to any requirements file, scheduled job or pipeline.
- Checks 1-7 and the CTO's check 8 still gate the install; this co-decision changes no grade.

## Why this is a file and not a `decide` row

The tool refuses a second decision on a decided request, measured:

```
$ python org/devices/intake/intake_request.py decide --id REQ-20261015T171032Z-duckdb --verdict APPROVED --by 4.0.0_SA_CRO --reason "..." --evidence org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_DUCKDB_20261015.md
REFUSED already decided: REQ-20261015T171032Z-duckdb (a second decision is refused)
rc=1
```

The request JSON holds one decision (`1.0.0_SA_CTO`, APPROVED, 2026-10-15T17:15:36Z). I did not edit the JSON by hand:
the one-decision rule is the tool's gate, and bypassing it is not mine to do. If a co-decision is to be a row, that is a
change to `org/devices/intake/intake_request.py` (a `decisions[]` append for a second seat), owned by NFRA_CTLPLN's issuer.
