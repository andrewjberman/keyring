# ETFS_RIVALS -- BBGLEG workstream L8/L9 adjudication (round 12 eb-1 + pk-1, round 13 al-1; site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-06 ~20:50Z. Packet: COO~RV msg 30284. Analysis in force: `ledger/ROUND_ANALYSIS.round11.md`
and round-10 ADDENDUM 5 @a8fb9c1df1.

The workstream is drained: RIV-eb-1 and RIV-pk-1 (merge 325e20b091), RIV-al-1 (merge 2d78ef2151), all `complete`. None carries a
judgment criterion, so there is no J1 here.

**The apply, this seat's reads:**
- eb-1.AC1, pk-1.AC1, al-1.AC1 and al-1.AC2 re-run PASS 0 failures at CLOUD 2f44b42430.
- All 5 rivalfunds Lambdas hold 39 of 39 package files equal by content to 92cf1f322b. Negative control: 6 files differ from the
  prior pin 50a2248fe9.
- Ledger `etfs-rivalfunds-pk1-al1` is OPEN on leg C1 (the ADDENDUM 1 merged-pair census after the 2026-10-07 07:00 ET run). No
  republish rode this deploy, so the served 10-06 page still shows the Nebius split; S43's served proof is not yet readable.
- eb-1 has no Lambda leg: it rides the vehicle from the shared tree at the 07:00 ET run.

**Not compiled:** Z-W2-S15 is named in the packet but is not in `INVESTIGATION_v1.Z.md` at 2f44b42430. It compiles with the
round-13 main packet.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S48",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-06T20:50:00Z",
    "one_line": "BBGLEG L8/L9: eb-1.AC1, pk-1.AC1, al-1.AC1 and al-1.AC2 re-run PASS at CLOUD 2f44b42430; pk-1 + al-1 are applied (5 Lambdas 39/39 at 92cf1f322b, control differs in 6). W2-S14, S51 and S52 are dispositioned. S43 stays OPEN until a served page shows one Nebius modal carrying both funds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W2-S14",
      "ETFS_RIVALS-Z-S51",
      "ETFS_RIVALS-Z-S52"
    ],
    "spec_asserts": "Round-10 ADDENDUM 1 @982e914b1d (pk-1), ADDENDUM 2 @b555e81836 (eb-1) and ADDENDUM 5 @a8fb9c1df1 (reader alignment before one deploy pair); round-11 analysis ruling 4 (the slug gate).",
    "world_is": "- eb-1.AC1: PASS 0 failures (control: a reachable session lands G4 and the daily run exits 0).\n- pk-1.AC1: PASS 0 failures (control: a CUSIP whose parsekey names a key no row carries keeps its CUSIP).\n- al-1.AC1: PASS 0 failures (the census sees 23 sites of 11 functions). al-1.AC2: PASS 0 failures (GQGU's Nebius price/gics inputs are named NBIS_US_Equity, none N97284108).\n- Apply: the 5 Lambdas each 39/39 equal to 92cf1f322b; 6 files differ from 50a2248fe9.\n- W2-S14 / S51: the worker's finding stands and the defect was the check, not the build. A stored null reads back NaN (truthy) on pandas 3.0.3, so `not pk.get(...)` failed a correct implementation; the issuer's amend 6ff7fc5dbc treats None and NaN alike, and the amended check passes on this seat's re-run.\n- S52: the slug-gate defect this seat routed in the R11/R12 review section 4. The CTO ruled it (round-11 analysis ruling 4: read the LAST status tag; read the decomposition at the order's issuance). The gate's code is the gate owner's lane, outside this project's cells.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's re-runs of round12/checks/eb-1.AC1.py, round12/checks/pk-1.AC1.py, round13/checks/al-1.AC1.py, round13/checks/al-1.AC2.py at 2f44b42430",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r12_j1/lamcmp.py 92cf1f322b 50a2248fe9",
        "org/critical_paths/.open_deploys/etfs-rivalfunds-pk1-al1.json (OPEN, leg C1)",
        "investigation rows ETFS_RIVALS-Z-W2-S14, S51, S52"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. W2-S14 is closed by the issuer's check amendment 6ff7fc5dbc, which S51 cites and this seat's re-run confirms. S52 is ruled by the CTO (round-11 analysis ruling 4) and belongs to the gate owner's lane; this project owes nothing further on it. REMEDIATION_v11 S43 and C-S47 stay OPEN."
  }
]
```

-- 3.0.0_SA_CVO~RV
