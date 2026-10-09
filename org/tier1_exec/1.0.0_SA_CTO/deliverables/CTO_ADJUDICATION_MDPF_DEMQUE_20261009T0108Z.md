# CTO adjudication -- MDPF_DEMQUE, L10 round 1, FWD-1's consumer (2026-10-09 ~01:0xZ)

**Seat:** `1.0.0_SA_CTO~DELL1`. **Authority:** Andrew-direct 2026-09-03 ~05:2xZ ("if upon receipt it is in question ... the CTO can run
/open-calls on the subject and then CTO adjudicates on the recs and it picks up from there via a new (or adjusted) PRD"; record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_052xZ_WHO_DECIDES_DONE_COO_COMPLETION_REPORT_CTO_GRADES_TWO_READS.md`).
Scope measured with `open-calls.py`: `verdict=OWN-BOX` (row `dell1-20261009T010722Z-e8d1`). The card was put to Andrew at ~00:0xZ;
no answer arrived in ~1 h. This ruling keeps the loop moving, and Andrew may override it.

**Evidence:** CVO slug `ADJUDICATION_v1.md` @94d0ca79a6; row `MDPF_DEMQUE-D1-W4-S2` (REMEDIATION_v1): "No Cottonwood page reads
canonical_prices.parquet ... no page shows a client's per-security daily prices. FWD-1's 'shows its daily prices on that client's pages'
has no consumer." COO real-run `FWD1_REAL_RUN_R1.md` @246e601ef2.

```
+-- CALL 1 of 1 -----------------------------------------------------+
  **What does a backfilled price feed on the client's pages?**
  (a) the client's historical holding values and performance for dates
      Black Diamond does not cover, built by ADVI_COTBKF from these
      prices; (b) a new page or column showing each security's daily price.
  --------------------------------------------------------------------
  **REC --** (a). That is what the prices are for (Andrew's Yahoo record:
  ADVI_COTBKF "consumes the prices"), it needs no new frontend, and FWD-1
  stays checkable by a person: the backfilled values match trade prices.
  --------------------------------------------------------------------
  RULING -- (a), because the outcome's purpose is valuing the client's
  history, a price page nobody asked for would be frontend work outside
  the brief, and (a) keeps FWD-1's id and its trade-price test intact.
+---------------------------------------------------------------------+
```

## Acts

1. PRD v0.3: FWD-1's ACCEPT amended in place, id unchanged, narrowed to its real consumer.
2. Round 2 (COO `2.0.0_SA_COO~Q1`) carries the seam: the hop-6 consumer is ADVI_COTBKF's valuation read of the queue's price store,
   which is a cross-box file contract with dell2 (path and key namespace). It also carries hop 5 (CUSIP absent from the lander's
   transactions object) and S_00's schedule (D1-W4-S1, now dell1's own SSM/EventBridge change).
3. Row `dell1-20261009T010722Z-e8d1` closed ruled_by=cto.
