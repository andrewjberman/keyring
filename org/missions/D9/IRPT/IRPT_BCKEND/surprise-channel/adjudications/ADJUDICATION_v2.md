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
  },
  {
    "id": "IRPT_BCKEND-C-S81",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T13:42:53Z",
    "one_line": "RT5 correction remaps six worker IDs without changing their content; the disclosure-only grade is recorded at the corrected instance pin.",
    "class": "OBSERVATION",
    "spec_asserts": "L9 grades a judgment criterion at an explicit instance vintage; a citation to a renamed branch row must retain its original vintage or use the verified mapping.",
    "world_is": "Correction 95964 maps worker S25..S30 at 8d173559747f875ea751eeaea898de2b241ed8e7 to S27..S32 at 479ed367e57e41b9794aaea41d633884b0f5f5f3. Six row bodies are identical except id. The proof is identical after one-pass ID remapping and its battery pin update; battery changes are row labels only. Guard, both runners and issued face are unchanged. Proof checker is VALID rc=0 with six of six surprise references resolved.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@8d173559747f875ea751eeaea898de2b241ed8e7",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@479ed367e57e41b9794aaea41d633884b0f5f5f3",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@479ed367e57e41b9794aaea41d633884b0f5f5f3",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rt_5.result.md@479ed367e57e41b9794aaea41d633884b0f5f5f3 (was/is mapping)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_RT5_L9_REVIEW_20260911.md (same commit; correction 95964 comparison and checker evidence)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade and citation-mapping record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "RT5-AC2",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@479ed367e57e41b9794aaea41d633884b0f5f5f3",
        "verdict": "PASS",
        "reason": "The RT5-AC2 disclosure bar and its output are unchanged after the six ID replacements. The record states two bundled files, absent bundled dependencies, undetermined execution host/dependency availability and no executed runner or scheduled-run proof. C-S79's disclosure-only judgment therefore also applies at this explicit corrected pin. All limitations and factual qualifications in IRPT_RT5_L9_REVIEW_20260911.md remain: this is not runtime readiness, whole-order acceptance or an RT5-AC1 truth verdict. C-S80's red-baseline predicate concern persists; its corresponding worker row is now S29 rather than S27."
      }
    ],
    "notes": "Preserve C-S79/C-S80 as evidence at their original 8d17355974 vintage. At the corrected tip use S27 for one key versus two, S28 for metadata-key collision, S29 for pre-red tests, S30 for invalid D- grammar, S31 for the forbidden runner-edit clause, and S32 for the old loose-key probes. Do not replace IDs in immutable earlier commits or apply the mapping to the issuer's distinct S25/S26 rows. The corrected tip was not merged into observed CLOUD 3b28cf1c6f1d1f5ff5e7917d4e97ea3ae5015bcd. No battery rerun, cloud action, worker modification or L10 slug follows from this record."
  }
]
```
