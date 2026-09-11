# IRPT_BCKEND round 2: CVO adjudication

Partial L9 intake for RT5 at worker tip `8d173559747f875ea751eeaea898de2b241ed8e7`. This document will accumulate CVO review as round-two evidence arrives; it is not an L10 slug. Review details: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_RT5_L9_REVIEW_20260911.md`.

```json
[
  {
    "id": "IRPT_BCKEND-C-S79",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T13:25:15Z",
    "one_line": "RT5-AC2 passes the requested disclosure record; the two-file bundle does not establish an executable host or a scheduled run.",
    "class": "OBSERVATION",
    "spec_asserts": "RT5-AC2 asks for a judgment record of bundle completeness, execution host and its dependencies, and the limits of the served artifact; the worker must leave this criterion ungraded.",
    "world_is": "The pinned instance records two files, zero bundled dependencies, zero identified hosts, unmeasured host dependencies and zero runner execution. It leaves RT5-AC2 UNVERIFIABLE-BY-INSTRUMENT for the named CVO. Independent source and path checks substantiate the limitation, with corrections recorded in the linked review.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.md@8d173559747f875ea751eeaea898de2b241ed8e7 (RT5-AC2; BOUNDS excludes production runner execution)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@8d173559747f875ea751eeaea898de2b241ed8e7",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_RT5_L9_REVIEW_20260911.md (same commit; source hashes, checker result and corrections)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "RT5-AC2",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@8d173559747f875ea751eeaea898de2b241ed8e7",
        "verdict": "PASS",
        "reason": "The issued RT5-AC2 asks the worker to state deployment scope and limits, rather than execute the runners (expressly excluded by BOUNDS). The record clearly states that the bundle contains only two files, that the execution host and its dependency availability are undetermined, and that deployment proves no scheduled run. PASS applies to that disclosure record only. The two-file tarball is not established as a sufficient standalone execution unit: host identity, third-party packages, first-party modules, schemas/configuration and the silver registry remain unverified. Read the path-expression, dynamic-import census, consumer-search and fixed-key qualifications in IRPT_RT5_L9_REVIEW_20260911.md with this grade. No RT5-AC1 truth verdict, whole-order acceptance, CLOUD merge, or runtime readiness follows from this grade."
      }
    ],
    "notes": "Pinned worker-branch review while 8d173559747f875ea751eeaea898de2b241ed8e7 is not an ancestor of observed CLOUD 0ecf25f1ca604fcdb15f7e73241d351966e75505. No worker artifact or frozen task-order face was changed. This partial round-two record is not an L10 slug."
  },
  {
    "id": "IRPT_BCKEND-C-S80",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T13:25:15Z",
    "one_line": "RT5-AC1(a)'s green-test bar is replaced by matching red baseline counts, and the invoked battery omits the 55-file tools suite.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "spec_asserts": "RT5-AC1(a) requires the guard's self-test and .tools/tests/ to pass, with counts printed. BOUNDS also names the self-test as a control and freezes the specification mid-round.",
    "world_is": "At the pinned worker tip the instance labels RT5-AC1 PASS while reporting FAIL 3/18, FAIL 7/14, and 47 PASS / 8 FAIL of 55. battery_ib_rt_5.py:55-56,111-125 accepts equality with the two red failure-count tuples; it neither compares failing-case identities nor invokes the 55-file .tools/tests/ suite. Preserving a red baseline is evidence of a bounded control, not satisfaction of the issued green-test bar.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.md@8d173559747f875ea751eeaea898de2b241ed8e7 (lines 63,75,87-88)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rt_5.py@8d173559747f875ea751eeaea898de2b241ed8e7 (BASELINE and arm (a), lines 55-56 and 111-125; full 220-line source read)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@8d173559747f875ea751eeaea898de2b241ed8e7 (RT5-AC1 output and denominator explicitly disclose the changed bar)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_RT5_L9_REVIEW_20260911.md (same commit; read-only verification and limits)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The issuer owns resolution of the acceptance contradiction through the existing lane. This row neither amends the frozen face nor directs new worker work. Worker S27 at the cited branch pin already records the red baseline; this CVO observation adds the acceptance-predicate and omitted-suite consequences. No adjudicates edge is asserted to an unmerged branch-only row. Do not rerun this battery as a read-only probe: its mint and gate arms write the cloud object."
  }
]
```

