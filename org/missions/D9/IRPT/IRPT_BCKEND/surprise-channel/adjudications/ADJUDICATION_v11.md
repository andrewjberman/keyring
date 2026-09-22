# IRPT_BCKEND Round 14 — targeted capture-tool judgment

Author: `3.0.0_SA_CVO~B`. R114-AC3 only; not a round-drain or publication claim.

```json
[
  {
    "id": "IRPT_BCKEND-C-S195",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T10:03:00Z",
    "one_line": "R114-AC3 PASS: type-only timeout repair splits same-text errors; publication and capture holds are separate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IB-rtn-1 R114-AC3 requires no message-based classifier, a genuine typed/deadline fixture, the unmodified CVO typed-pair split, and no regressions except two named historical mock cases.",
    "world_is": "R114-AC3(i)-(iv) PASS at repaired blob 17aff45ed837a3a6e62fb2ce0410075b62a499dd (sha256 ea437510ee96fdf7fd106ff36dff3dead1aaf8ada94458a62556bae210cdc25a). capture-session.cjs:148-155 and :487 @b99067c3bc classify solely by instanceof/name, never message text. New versioned fixture uses real asynchronous timers and a genuine instance of the injected TimeoutError class; both typed and untyped timer cases were run. Own fresh unmodified R13 before/after companion splits all six cases as required. Fresh R11 and R12 each change only the explicitly authorized historical untyped-timeout case to terminal; R10/R9/R8 and R12 cleanup are unchanged. This grades local implementation/test evidence, not publication, host delivery, or authorization to capture.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R14_R114_AC3_REVIEW_20260922.md (co-committed)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R14_REVIEW_PROBE.cjs (co-committed)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtn-1.the-capture-tool-timeout-by-type-or-deadline-state-only.proof_of_spec.json@32bfd035dee24662c1e9b6910704cb081cfdaeac"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only; no new finding or remediation clock. No full Round 14 drain, publish, or capture-release assertion.",
    "grades": [
      {
        "criterion": "R114-AC3",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtn-1.the-capture-tool-timeout-by-type-or-deadline-state-only.proof_of_spec.json@32bfd035dee24662c1e9b6910704cb081cfdaeac",
        "verdict": "PASS",
        "reason": "R114-AC3(i)-(iv) PASS at repaired blob 17aff45ed837a3a6e62fb2ce0410075b62a499dd (sha256 ea437510ee96fdf7fd106ff36dff3dead1aaf8ada94458a62556bae210cdc25a). capture-session.cjs:148-155 and :487 @b99067c3bc classify solely by instanceof/name, never message text. New versioned fixture uses real asynchronous timers and a genuine instance of the injected TimeoutError class; both typed and untyped timer cases were run. Own fresh unmodified R13 before/after companion splits all six cases as required. Fresh R11 and R12 each change only the explicitly authorized historical untyped-timeout case to terminal; R10/R9/R8 and R12 cleanup are unchanged. This grades local implementation/test evidence, not publication, host delivery, or authorization to capture."
      }
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S196",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T10:32:20Z",
    "one_line": "R14 final reconciliation: C-S195 PASS carried unchanged; three clocks close; C-S174's shared wrong full-hash oracle remains open.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Formal L8/L10 receives the final bound proof and closes only individually verified remedies; a full-length comparison must not be mistaken for independently established hash truth.",
    "world_is": "Final proof blob7e3486032ab312a5c29eadb7721163510da659f7 has the identical acceptance array, source and fixture as C-S195's graded vintage. Bound receiving and explicit-ID proof checks pass; all11 artifact blobs resolve and match current paths. Signed S3 publication closes C-S179 at source/delivery grain, not host/browser grain. The prospective typed-only cut and fixture close W13-S6; actual final R113 result pin closes C-S194. C-S174 remains OPEN: reconstructed CRLF bytes and saved diagnostic hash contain ...03bfb20..., whereas proof and battery expected constant both contain ...03fbb20.... Proof still incorrectly attributes git-LF hash to the worktree diagnostic. Full-length comparison alone passes that shared wrong oracle. No new worker items; own terminal census0/98, channel0/343 undispositioned.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v7.md (co-committed), Round 14 addendum: per-clock event pins and outcome boundaries",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R14_FINAL_RECORD_PROBE.cjs (co-committed): read-only 11/11 pin and hash reconstruction assertions",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v11.md@d2e855e299#IRPT_BCKEND-C-S195: unchanged grade",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/battery_ib_rtm_1.py@188a483e37:69,218-219; full comparison against wrong CRLF_VALUE",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json@bfd088d173:254; erroneous hash and diagnostic attribution"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Reconciliation record, not a duplicate remedy or second judgment grade. Residual belongs to existing C-S174 in REMEDIATION_v5, kept OPEN/INERT with its existing owner. Only C-S179/W13-S6/C-S194 clocks advance in their original rows; no source repair or capture hold follows from the metadata residual. CTO alone receives formal slug."
  },
  {
    "id": "IRPT_BCKEND-C-S197",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T11:41:58Z",
    "one_line": "R15 metadata hash repair verified by three control arms; C-S174 stays open only for an unqualified S3 exclusion in the published proof.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "R115-AC1/2 are mechanical metadata criteria. C-S174's broader existing remedy requires truthful final proof text with historical exclusions scoped to the pass they describe.",
    "world_is": "Both R115 criteria pass their invocations; bound receiving and explicit two-ID check pass; all six artifact blobs resolve and equal HEAD. Hashes are recomputed from historical bytes and match the stored diagnostic, not a copied oracle. Own runs of the actual committed battery accept corrected text and refuse in-memory wrong-CRLF and wrong-LF text separately (3/3 expected arms, both mutants leave disk scan0/90 and omit success token). The R107 proof now correctly attributes both hashes, but line23 records completed S3 publication while lines269-270 still exclude any real host/SSM/S3 action with an unqualified all-stubs/static reason. No source or README changed. R114-AC3 remains C-S195 PASS; no new judgment criterion. Own terminal census0/99, channel0/343 undispositioned.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v7.md (co-committed), Round15 addendum: full measurements and bounded carry",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R15_METADATA_REVIEW_PROBE.cjs (co-committed): actual three-arm control and independent byte reconstruction",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json@6b8139682d:23,254,269-270 (blob f8253e60cba7b531c9fe5f92f2f3ed5da89467a5)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/battery_ib_rtm_1.py@6b8139682d:124-162,304-367 (blob967f45ea8a7e9ba1acf80b0b0f5098a29bd8dc63)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No new remedy minted: remaining text conflict belongs to existing C-S174 in REMEDIATION_v5, whose OPEN/INERT clock and owner are preserved. CVO owns late disclosure of the exclusion residual. Scope it to the earlier diagnostic pass or actual remaining exclusions; no code repair, publish replay, changed R115 verdict, new capture hold or PRD addendum is implied. Formal slug to CTO only."
  }
]
```
