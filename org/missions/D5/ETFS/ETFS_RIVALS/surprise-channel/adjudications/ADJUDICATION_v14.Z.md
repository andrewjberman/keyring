# ETFS_RIVALS -- round 13 L8/L9 adjudication (gw-1, fe-1, lk-1; site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~02:50Z. Packet: COO~RV msg 30520. Earlier round-13 records: C-S48 (al-1, ADJUDICATION_v12)
and C-S49 (fe-1 J1 limbs 1-2, ADJUDICATION_v13).

Round 13 is drained: al-1, fe-1, gw-1 and lk-1 are `complete`. All mechanical checks re-run PASS. fe-1's J1 stands at limbs 1 and 2
MET on the 02:33Z page; limb 3 waits for the 2026-10-07 names run. Two things are owed and named, not graded here: the signed-in
GET of the audit route (CTO condition 4), and limb 3.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S50",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T02:50:00Z",
    "one_line": "Round 13 L8/L9 (gw-1, fe-1, lk-1; al-1 compiled in C-S48): gw-1.AC1, lk-1.AC1 and fe-1.AC1-AC3 re-run PASS at CLOUD e0aafbad8b; 5 Lambdas 39/39 at f3b3055a5e; the served 02:33Z page carries exactly one audit link, 0 citation lines, and still 0 of 2,076 buttons without their fund's section. NOT EXERCISED by any seat: a signed-in GET of /rivalfunds/2026-10-06/audit (CTO condition 4). fe-1 J1 limb 3 still waits for the 10-07 names run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W2-S15",
      "ETFS_RIVALS-Z-S53"
    ],
    "spec_asserts": "ROUND_ANALYSIS.round11.md section 3 (round 13: fe-1, lk-1, gw-1) and ruling 3 (the citation lines move to the audit page with ADDENDUM 4 step 3); Andrew's order step 3: 'Make an audit gateway after 2.) is done'.",
    "world_is": "This seat's reads (S3 bytes, sha256 in served_sha256.txt; batch rv-publish-1006r13c, 02:33:06Z):\n- index.html 1,276,544 B: 2,076 buttons, 0 unresolved, 0 without section[data-fund=F]; 234 of 234 real clicks open the right modal; 13 of 13 panels whole; exactly 1 href, '/rivalfunds/2026-10-06/audit' ('one step away'); 0 'Cited rows:' and 0 machine keys in citation paragraphs (148 on the 17:33Z page). The plain-ticker census leaves 62 hits, all 'AI', 'MTD' or 'MSCI EAFE Dec26'.\n- audit.html 1,381,244 B: 26 'Cited rows:' blocks holding the 148 machine keys; 392 popover targets, 0 unresolved; 221 security buttons; no script; manifest audit_holding_dialogs 'on'.\n- Manifest fund_sections 2076 / 2076 / 0, holding_dialogs 'on'.\n- Apply: 5 Lambdas 39/39 equal to f3b3055a5e (control: 1 file differs from 42b4e258d1). gw-1's gateway release (NFRA_OPLGTW r23 @7d65a28db0) is NOT read by this seat on the applied plane: it sits in another project's lane.\n- The route: an unauthenticated GET of /rivalfunds/2026-10-06/audit answers 302 to the login, and so does a bogus sibling path, so this probe cannot tell a served route from a missing one. The signed-in GET through the balancer is the FWD proof and no seat has taken it.\n- W2-S15: au-1.AC1 arm (a) and au-1.AC2 arm (a) assert NO audit link; lk-1 adds that one link by order, so both arms fail by design while lk-1.AC1 passes. The round-12 checks are superseded on that arm, not regressed.\n- S53: to-check.py shares the slug gate's first-status-tag read (S52's class).\n- fe-1 J1 limb 3: 4 securities still ticker-form, 14 mentions, unchanged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r13_lk1/j1_result.json, census2.json, served_sha256.txt",
        "this seat's re-runs of round13/checks/gw-1.AC1.py, lk-1.AC1.py, fe-1.AC1.py, AC2.py, AC3.py at e0aafbad8b",
        "lamcmp.py f3b3055a5e 42b4e258d1",
        "curl of the audit route and a bogus sibling, both 302",
        "investigation rows ETFS_RIVALS-Z-W2-S15, S53"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. W2-S15 is a superseded check arm, expected under lk-1's order; the issuer retires or amends au-1's arm (a) at the next cut. S53 joins S52 in the gate owner's lane under round-11 analysis ruling 4. Nothing graduates. Still OPEN: S24, C-S36, S43, W6-S2. Owed and named: the signed-in audit GET (CTO condition 4) and fe-1 J1 limb 3 after the 10-07 names run."
  }
]
```

-- 3.0.0_SA_CVO~RV
