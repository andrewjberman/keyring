# NFRA_CTLPLN: CVO adjudication, L9 of three judgment criteria (2026-10-09)

On 2.0.0_SA_COO~C msg 107759: `round-close-check.py --project NFRA_CTLPLN` read orders=45, judgment=4, graded=1, ungraded=3.
This document grades CT4d8-AC2, CTi6-AC3 and CTi8-AC2, all MET.

<sweep_watermark>2026-10-09T05:50Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S10",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T05:50Z",
    "one_line": "L9: CT4d8-AC2, CTi6-AC3 and CTi8-AC2 MET; S36, S9102 and S9104 DISMISSED as records.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT4d8-AC2: the missing-row proposal can be acted on without a question (measured behaviour, refusal, place, cost, non-application). CTi6-AC3: DEPLOY_PLAN_MEASURED.md explains every targeted-plan line by the workstream's merged work, or names the line it cannot. CTi8-AC2: PACKAGE_LINE_ENDINGS_MEASURED.md names the differing files and their cause from reads, and states what the change does to the next deploy's hash.",
    "world_is": "CT4d8-AC2 MET: the proposal states the probe's three measured results (B, a well-formed unregistered name, admitted), the refusal and its line, its place (naming-apply-gate.py run_plan lines 366-373), its cost and its non-application. Its one open question (section 7: resources.json holds no conformant row and validate() refuses one) is a measured defect in the PRD's premise, not a gap in the proposal, and the owner acted on it: PRD v0.14 withdrew the refusal and replaced C-NAMING clause 3 (NFRA_CTLPLN_PRD.md:610-619). CTi6-AC3 MET: the targeted plan's three lines (aws_iam_policy.exec, handler, ingress[0]) are each explained, and the file names the source_code_hash line it can explain only in part (other projects' registry inputs copied into the zip, split not measured); its new hash wa8/4zVW... decodes to the stated zip SHA-256 c1af3fe3... (checked by this seat). CTi8-AC2 MET: it names remediations.json and scopes.json (i/lf, w/crlf in the shared tree; this seat reads the same today), their cause from reads (no attribute, core.autocrlf false in effect, a working-copy write inferred), and the next deploy's hash change with its honest limit (the live hash not read); this seat's re-run of test_build_reproducible.py reads PACKAGE-REPRODUCIBLE ok=True crlf_sha=lf_sha=worktree_sha=f9360727a66c files=32. Dismissed: S36 is a handoff record whose effect is on W36-S2's remediation row (owner 2.0.0_SA_COO~T2, @59ec92f15d); S9102 and S9104 record how TO-CT-k-2's worker ran its criteria (an --init-only readback; --all-roots over 40 lock files).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~11/PROPOSAL_MISSING_ROW_REFUSAL_FOR_LGIC_ENFORCE.md",
        "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~34/DEPLOY_PLAN_MEASURED.md and PLAN_TARGETED_module_ldo_001.txt (lines 43, 92, 109, 126)",
        "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~36/PACKAGE_LINE_ENDINGS_MEASURED.md",
        "org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md:610-619 (v0.14: the missing-row refusal WITHDRAWN, clause 3 replaced)",
        "run by this seat at box/laptop ccbe8b8be1: base64 of wa8/4zVW6JXsl8vwrWvRkVWW9NruXCWdH8pVppfR2jI= -> c1af3fe33556...; git ls-files --eol on the two registry files -> i/lf w/crlf; python infra/aws/lambda/teams-chat-assist/tests/test_build_reproducible.py -> PACKAGE-REPRODUCIBLE ok=True ... files=32",
        "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows S36, S9102, S9104"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-S36",
      "NFRA_CTLPLN-S9102",
      "NFRA_CTLPLN-S9104"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S36, S9102 and S9104 are records (a handoff already carried on W36-S2's remediation row; two notes of how a worker ran its criteria). No remedy is owed."
  }
]
```
