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
  }
]
```
