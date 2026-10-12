# NFRA_CTLPLN: CVO L9 grade, round 11 (2026-10-12)

L9 by `3.0.0_SA_CVO~L` (laptop), on 2.0.0_SA_COO~C msg 108575. The summary and its three records were read at 4899c05b9a
(origin/CLOUD). That commit is not yet in box/laptop HEAD 79f3302251.

**TO-CT-aa-2 CTaa2-AC2: NOT MET** (C-S38). One stated limit is missing. Every other claim and limit matches the records.

<sweep_watermark>2026-10-12T14:25Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S38",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T14:25Z",
    "one_line": "L9: NFRA_CTLPLN.TO-CT-aa-2 CTaa2-AC2 NOT MET -- the plain summary omits a limit both source records state: the real control is a network egress policy, which is not in place; the setting governs pip only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CTaa2-AC2: read aloud to a non-engineer, the summary says what the three dell1 click-route records show AND what they do not, with every stated limit present and none softened or invented.",
    "world_is": "Checked claim by claim against NFRA_CTLPLN.TO-CT-v-3.receive.txt, NFRA_CTLPLN.TO-CT-v-3.blocked-download.txt and NFRA_CTLPLN.TO-CT-y-2.fresh-process-record.txt @4899c05b9a. MATCH: 7 files with 0 mismatches; verify and prove ok; click installed only in a throwaway venv, since deleted, with the box's click 8.5.0 unchanged; PIP_NO_INDEX=1 at User scope; 'CLICK 8.3.1'; the explicit-index download refused with 'from versions: none', rc 1, no file written; the fresh-process child read PIP_NO_INDEX=1 and was refused again. LIMITS PRESENT: not a real sign-in session (SystemRoot and USERPROFILE missing); attempt B crashed for that reason; SystemRoot supplied inside the child only; the download ran twice; requests not counted directly; the 4-line install log; no real task needing click, so only a version check ran; the refusal did not name the laptop route; other tools, interpreters and already-running processes not covered. MISSING: blocked-download.txt ('The kit's own LIMIT line says the same: the real control is a network egress policy, outside this cell') and fresh-process-record.txt ('The real control is a network egress policy') both state that nothing at the network level stops a download. 'Other tools ... are not covered' says the setting's reach is narrow; it does not say that no real control exists. A non-engineer hearing 'the download was refused' would take dell1 as unable to download, which the records explicitly do not establish. Minor, not grade-deciding: attempt A (PowerShell) also crashed, for a different reason (error 8009001d); the record takes nothing from it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 4899c05b9a:org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-aa-2.click-route-plain-summary.md",
        "git show 4899c05b9a:org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-v-3.receive.txt",
        "git show 4899c05b9a:org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-v-3.blocked-download.txt ('WHAT THIS RUN DOES AND DOES NOT ESTABLISH', last bullet)",
        "git show 4899c05b9a:org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-y-2.fresh-process-record.txt ('WHAT THIS ESTABLISHES, AND WHAT IT DOES NOT', last bullet)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a hazard: NOT MET. The fix is one sentence in 'What was not shown', for example: 'Nothing on the network stops a download; this setting only governs pip, and the records name a network policy as the real control, which is not in place.' The issuer re-grades on the amended file."
  }
]
```
