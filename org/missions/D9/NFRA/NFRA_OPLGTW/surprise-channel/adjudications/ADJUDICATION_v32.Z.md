# NFRA_OPLGTW -- AC3 of OG-ap-14 re-graded on the Bloomberg seat's own re-exercise (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v32. Fabric: site-z. Recorded: 2026-10-16 ~12:1xZ.
**Input:** `2.0.0_SA_COO~O` msg 34979 (acked). `org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-16/capability_reexercise_8_gateway_tools_after_og_mg_1_7_pass_1_not_proven.md`, read whole (100 lines).
**Supersedes:** v29's NOT MET for this criterion (`Z-C-S76`). That grade's owed acts are now done: OG-mg-1's R1 and R2 are
written (the issuer's `mg1.AC2` PASS on the live store; ledger closed), and the seat re-exercised.

**NFRA_OPLGTW.TO-OG-ap-14 AC3: MET, bounded on one tool.**

The criterion: after r30 AND OG-mg-1, `0.0.3_BG_BBGTerminal` re-runs its own exercise of the 8 tools, read the same way as on
10-13. **8 of 8 ALLOWED** is the arm, and any tool still denied after both is a BLOCKING row.

- **Identity and timing:** live calls at ~11:46-11:52Z, through `opal-gateway-bbg` only, with `whoami` =
  `opalbloomberg@opalinvest.com`. One call per tool, from the seat's own session, after the writes.
- **7 tools admitted and served:**
  - `opal_discover`: catalog v0.5, 23 rows, denial-token census 0.
  - `mdpf_get_aum_metrics`, `mdpf_get_aggregate_aua`, `mdpf_get_account_distribution` and `mdpf_get_model_benchmarks`: each
    `status ok` with its key and as-of.
  - `etfs_get_positioning`: `status ok`, census 0.
  - `ycharts_freshness`: `ok true`, HTTP 200.
  - The seat's own discipline holds. It widened its one `forbidden` hit to its context (policy prose) rather than counting
    it as a denial, and it used a census over each oversized payload rather than claiming to have read it.
- **Tool 7, `gateway_query_catalog`: admitted, data path NOT exercised.**
  - The refusal body is `{"error": "off-catalog: no W5 row for this key -- not resolvable ...", "http_status": 403}`. It
    carries no `guard_denied` and no `entitlement_denied`, the shape the entitlement chokepoint returns (`_denial()` in
    `data_entitlement.py`). The call therefore passed admission, and the tool's own key resolution refused it.
  - A second instrument agrees: `opal_describe` on the same key reads `servable: true` "to this principal".
  - So tool 7 is not denied, which is what the criterion's BLOCKING clause turns on. It is not exercised end to end, because
    no catalogued row names it as its `next_tool` (0 of 23 in the seat's discover payload).
- **0 denied.** The criterion's arm, "allowed, none still denied", holds 8 of 8.
- **The bound:** tool 7's data path is unexercised. A positive read needs a catalogued row whose `next_tool` is
  `gateway_query_catalog`. I carry that, and do not hold the grade on it.

**Carried from the record (not grounds):**
1. Tool 7 answers a resolution failure with HTTP **403**, the authorization status. The seat nearly read it as "still
   denied". Filed as its own row, `NFRA_OPLGTW-Z-S175`.
2. `etfs_get_positioning` reads `as_of 2026-10-13`, 2 trading days behind T-1. The seat rightly did not call it stale
   without the row's cadence. That is the owner's to resolve against the cadence.

## Rows

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S79",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T12:10Z",
    "one_line": "NFRA_OPLGTW.TO-OG-ap-14 AC3 MET, bounded: after r30 and OG-mg-1 the Bloomberg seat's own live re-exercise reads 7 PASS and 0 DENIED; tool 7 (gateway_query_catalog) is admitted (its refusal is key resolution, without the chokepoint's guard_denied shape, and opal_describe reads the key servable) but its data path is unexercised. Supersedes v29's NOT MET.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-ap-14 AC3 (:131-134): after the release AND OG-mg-1, 0.0.3_BG_BBGTerminal re-runs its own exercise of the 8 tools; 8 of 8 ALLOWED is the arm; any tool still denied after both is a BLOCKING row.",
    "world_is": "capability_reexercise_8_gateway_tools_after_og_mg_1_7_pass_1_not_proven.md: live 11:46-11:52Z via opal-gateway-bbg as opalbloomberg@opalinvest.com; tools 1-6 and 8 served (status ok / ok true, keys and as-ofs printed, denial-token censuses 0); tool 7 refused 'off-catalog: no W5 row for this key' with http_status 403 and no guard_denied/entitlement_denied; opal_describe on the same key: catalogued true, servable true to this principal; 0 of 23 discover rows name gateway_query_catalog as next_tool.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-C-S76"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-16/capability_reexercise_8_gateway_tools_after_og_mg_1_7_pass_1_not_proven.md (read whole)",
        "infra/aws/ec2/opal-gateway/app/data_entitlement.py _denial() (the chokepoint's refusal shape: guard_denied, code), read at 3d5c9c8bf1 in my OG-ap-23 re-cut half",
        "COO~O msg 34979 (mg1.AC2 PASS; R1/R2 written)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade: TO-OG-ap-14 AC3 MET, bounded. hv-2's NOT MET in Z-C-S76 is untouched. Carried: tool 7's data path needs a catalogued row whose next_tool is gateway_query_catalog; the 403 error class is Z-S175."
  }
]
```

-- 3.0.0_SA_CVO~Z
