# NFRA_MCPINDEX -- surprise channel, REMEDIATION v8 -- THE ROUND-10 SLUG

Author: 3.0.0_SA_CVO~Z. Round: v8 (round 10). Fabric: site-z. Recorded: 2026-10-14 ~00:3xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 10: 2 of 2 orders complete, MAY-CLOSE (re-run by this seat), all checks mechanical, served on `7eff14b2e6`. L8 is
at `adjudications/ADJUDICATION_v9.md`.
- **FWD-21: REALIZED.** This seat's own discover reads on the served host returned 5, 1 and 8 catalogued matches, the
  last with 3 servable.
- **FWD-20: the partition is REALIZED; the depth is NOT REALIZED** (Z-W33-S1 graduated by Z-C-S49, below). The 67-tool partition was read
  live, and its classification holds on this seat's sample. "absent" depth on all 11 tools is wrong for at least one:
  the served AUA timeseries carries `as_of_first = 2024-11-01` beside the `as_of_last` the catalog already reads.
- **11 rows dismissed.** The deploy-recipe recurrence (Z-S108/S109/S111) folds into OPEN Z-S92.
- **Two older rows cleared, both caught by the slug gate.**
  - Z-S82 (BLOCKING, from round 6): its guarded act, MX-s-17's repoint, is cancelled (Z-C-S51).
  - Z-S96: this seat's round-9 Z-C-S47 had dismissed it in its text but filed it under GRADUATED. Corrected by Z-C-S52.
- **Out of round, ARMED:** Z-S101 and Z-S102 (MX-s-19, owner `2.0.0_SA_COO~MI`, read on 10-19/20). Z-S102 is a BD
  silver partition re-written at 1.3% of its bytes.

**For the analysis:**
1. **FWD-20 depth** (Z-W33-S1): read depth from the body at answer time, the same rule as freshness. No producer change
   is needed where the object already carries a first date.
2. **v0.10:** FWD-21 re-pins to list v4. Round 11 cuts the 13 added prefixes (CTO msg 33748).
3. **The deploy cone** (Z-S92, recurred three times): it must carry `infra/logic/registry`.
4. **Suite re-baseline** (Z-S107) and **a durable tool_index link key** (Z-S106).

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-W33-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "FWD-20's history_depth reads 'absent' on 11 of 11 (a) tools because MX-c-8's bound 4 forbade reading a served object's body. At least one object carries its first date as a body field: platinum/mdpf/global/aggregate-aua-timeseries.json as_of_first = 2024-11-01, read by this seat. 'absent' is therefore a wrong claim, not a measured absence, and r11.AC3's depth comparison compared absent with absent",
    "evidence": [
      "3.0.0_SA_CVO~Z read of the served AUA timeseries, ~00:2xZ 2026-10-14 (as_of_first 2024-11-01, as_of_last 2026-10-12)",
      "members.yaml mdpf_get_aggregate_aua history_depth: claim absent, 'how far back its data goes is inside the body'",
      "NFRA_MCPINDEX-Z-W33-S1 (0.9.0_WK_NFRA_MCPINDEX~33)"
    ],
    "remedy": "Read each (a) index's depth at answer time from the served artifact, as freshness is read (FWD-13): a first-date field or the dated series' first element. A snapshot object's depth is its one as-of, claim measured. A live-queried row's depth is its served window, claim inferred where it is not read. 'absent' is kept only where no artifact carries any date. FWD-20's PROOF compares one MEASURED depth with the artifact by a second instrument. Closes when that comparison passes on the served host.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v8",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v8"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~Z
