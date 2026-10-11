# NFRA_MCPINDEX ROUND 9 -- L8 COMPILE + plausibility read

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-11 ~15:3xZ, on `2.0.0_SA_COO~MI` msg 33309. **Terminality:** 5 of 5 orders complete
(MX-o-1, MX-o-2, MX-x-6, MX-c-7, MX-r-10); round-close-check MAY-CLOSE; the round has no judgment criterion.

**Remediation rows of round 8 that this round met** (state recorded here; REMEDIATION_v6.md is not edited):
- Z-C-S44 (FWD-18 tags): MET, see C-S45.
- Z-W28-S4 (word folds): MET; c7.AC3 reads folds 0, and 'S&P YTD' now routes from E-19 example text in the issuer's live run.
- Z-W29-S1 (emitter census dir): MET; MX-x-6 makes the emitter refuse a foreign census dir (x6.AC1, with a revert control).
- Z-S88 and Z-W28-S8 (suite baseline): MET; MX-x-6 records baselines full 41 and sparse 99, and the drain reads suite_delta new 0.
- Still OPEN: Z-S92 (the deploy wrapper; recurred on MX-r-10, carried to `2.0.0_SA_COO~O`'s wrapper fix), Z-S94, and Z-C-S42 (round-close-check J-id scoping) with Z-S97 below.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S45",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-11T15:30Z",
    "one_line": "FWD-18 re-grade (round 8's Z-C-S44 FAIL): now REALIZED -- the SERVED catalog reads 3 of 14 workflows retired (C2, W5, W6); E-25 no longer claims C1; C3 is carried by E-4, E-5 and E-9; every untagged entry states a reason.",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-18 (PRD v0.7:270-275): the count of C1-C8 and W1-W6 a served entry answers is read from the catalog; an entry carries its C# or W#.",
    "world_is": "Host md5 of /opt/opal-gateway/app/refs/DATA_CATALOG.yaml (ssm, read ~15:1xZ) is 244e42d6853a5cbb4f9239a8e5efd77c, equal to the release c3af8687e4's file. From that file: 35 needs (6 SERVED, 6 PARTIAL, 21 GAP, 1 DENIED, 1 UNMEASURED); SERVED entries retire C2, W5, W6, so 3 of 14. E-25 retires [] with retires_none 'no claim on Alyssa's tags: C1 is the YCharts report, which is GAP, and this need is Bloomberg'. C3 appears on E-4, E-5 and E-9, all GAP. E-26, E-27 and E-30 to E-35 carry retires_none reasons. Remediation row Z-C-S44 (REMEDIATION_v6.md) is met by MX-c-7 and MX-r-10.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ssm md5 on i-07dccb1615503ac99 = git show c3af8687e4:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml md5",
        "python count over needs: SERVED retires & {C1..C8,W1..W6} = {C2, W5, W6}",
        "deliverables/2.0.0_SA_COO~MI/round9/L8_PACKET_ROUND9.md @0531756fad (blob d339385e53)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A re-grade, not a defect: FWD-18 is realized at 3 of 14."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S46",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-11T15:30Z",
    "one_line": "Plausibility read of FWD-19's two GAP verdicts: BOTH GAPs are right and the billing owner (ADVI_BILLING) is right; the trade-reconciliation census reaches GAP partly for the wrong reason, which bears on its owner ('unowned').",
    "class": "OBSERVATION",
    "spec_asserts": "Round 9 has no judgment criterion; the issuer asks whether each GAP verdict and owner is right (packet section 3).",
    "world_is": "BILLING (6 candidates): no object carries a paid status. BD fees carry account_fee and basis_points but not AUM for a period (billing_end_date 0 of 17344 non-null). The one ADVI_BILLING gold object is one household and one quarter, written once. The SMArtX fee_statement prefix is empty, which matches this seat's own listing in the NFRA_OPLGTW round-33 L9. So GAP and owner ADVI_BILLING (the producer of a scheduled per-account billing object) both follow from the evidence. TRADE REC (8 candidates, each with a denominator, read-only, newest partition per prefix): GAP is right. But the census rejects Schwab silver dim_transaction because it has 'no status field', and a booked custodian row is itself the custodian state a reconciliation joins on: booked, and settled by date. The decisive blocker is the OPAL side. The trade engine's system of record (DynamoDB opal-trade-submissions, 33 items, statuses PENDING_APPROVAL to COMPLETE) and its S3 export are fund-grain, with no account key, so no per-account Opal status exists to join. That points the owner question at the engine bridge's owner (NFRA_OPSWKF owns intake and the engine bridge, per the census's own owner_reason), with the custodian side already served. 'unowned' over-states the gap. Carried to the analysis as an owner question, not a defect in the census's search: its coverage and denominators are sound.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPINDEX~30/census_trade_rec.json candidates 1-3 and owner_reason, read whole",
        "deliverables/0.9.0_WK_NFRA_MCPINDEX~31/census_billing.json candidates and gap_statement, read whole",
        "3.0.0_SA_CVO~Z NFRA_OPLGTW ADJUDICATION_v24.Z.md: s3://opal-data-assets/smartx/49financial/ absent"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A plausibility read, not a defect: both GAPs stand; the trade-rec owner question goes to the analysis."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S47",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-11T15:30Z",
    "one_line": "Round 9 L8: Z-S96 DISMISSED (its fix landed and was re-run); Z-S97 GRADUATES (re-run here: CLOSE-GATES-TEST 19 of 24, the round-close tool's own suite red, which hides regressions).",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-S96 ruled the remedy for NFRA_IAMROLES202609-Z-S29: the can() guard landed alone @a18b96fd5d and the issuer re-ran f1r.AC1/AC2 PASS (NFRA_IAMROLES202609-Z-S33). Z-S97, re-run by this seat at ~15:2xZ: python .tools/tests/test_round_close_and_research.py reads 'CLOSE-GATES-TEST cases=19/24 ok=False'. Four cases fail with TypeError: read_orders() missing 'ws', and the ENFORCE case 'reviewer present but a judgment criterion ungraded is refused' reads rc=0. Rows Z-W30-S1, Z-W31-S1, Z-W32-S1 and Z-S99 are dispositioned by the issuer's Z-S98 and Z-S100.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S96",
      "NFRA_MCPINDEX-Z-S97"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/tests/test_round_close_and_research.py at box/sitez HEAD, ~15:2xZ 2026-10-11: CLOSE-GATES-TEST cases=19/24 ok=False",
        "NFRA_IAMROLES202609-Z-S33 (can() guard @a18b96fd5d)",
        "deliverables/2.0.0_SA_COO~MI/round9/L8_PACKET_ROUND9.md @0531756fad (blob d339385e53)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
