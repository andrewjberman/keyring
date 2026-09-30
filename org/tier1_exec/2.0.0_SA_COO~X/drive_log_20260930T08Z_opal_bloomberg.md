# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 08Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 08:0xZ | L8 | 23 | y-4 before-state: map 3,012 entries across 66 fields; 97-block pass with 15,425 unit changes; flips classified (15,068 unmeasured->measured, 354 reason-only, 3 measured->unmeasured on 2317); BP/NG excluded (`Z-S64` key form). COO half `13f78a2b1b`. |
| 08:26Z | L8 | 23 | CTO half `badff0ef3b`: 2317 accepted, BP/NG excluded, conditions on PYTHONPATH and a served read |
| 08:29Z-08:34Z | L8 | 23 | act-start gate passed; ledger `198bd88afc`; leg a exact (3012/66/0/+NVDA/0); leg b `67568b59c4` |
| 08:37Z-08:41Z | L8 | 23 | leg c: the derive's 3-per-call cap refused one 97-name call, which wrote nothing; 33 batches followed, 97 stamps, units 15,425 = expected, 0 value moves |
| 08:4xZ | L8 | 23 | **Stop limb 2 fired:** sign labels contradicting their own value went 886 -> 1,568 on 49 blocks (`_resolved_sign` serves a sampled per-security sign); the formula text changed on 67 blocks. Leg d held. Escalation `c68c2a6dfd`; row `Z-S68`; `2.0.0_SA_COO~Z` told to hold ab-6. |

## Compiler Tools

- `y4_measure.py` and `y4_verify_c.py` (issuer): the per-block expected diff and the verify. The verify first counted the per-figure
  `vintage` as a change and had to be diagnosed.
- `deploy_ledger.py`: the entry opened with legs a-v.
- Gap: the half's writer census traced unit paths only, and missed `case_rule` as a second input to the derive.
