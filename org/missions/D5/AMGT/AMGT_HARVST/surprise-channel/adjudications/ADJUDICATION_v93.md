# AMGT_HARVST -- disarm compile for D1-W183-S14 and D1-W171-S3 (dell1)

<sweep_watermark>2026-10-18T17:25:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-20T15:05:00Z, on the disarm owner 2.0.0_SA_COO~W1's word (msg 8659; org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round99/DISARM_WORD_D1-W183-S14_AND_D1-W171-S3_20261020.md @c5eda52375). This is a disarm compile for two named rows, not a sweep, so the watermark is unchanged. W171-S3's clock is written in REMEDIATION_v26 (in place, with an appended disposition line).

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S78",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~DELL1",
    "surfaced_at": "2026-10-20T15:05:00Z",
    "one_line": "DISARM of AMGT_HARVST-D1-W183-S14 (BLOCKING): this seat's own no-var plan of infra/aws/terraform/harvest against the real state reads 'No changes.' (detailed exit 0), so a no-var apply destroys nothing. DISARM of AMGT_HARVST-D1-W171-S3 to RECORDED on the CTO's cross-adjudication ruling; its remediation stays OPEN on the ruling's release-test condition (REMEDIATION_v26).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-W183-S14",
      "AMGT_HARVST-D1-W171-S3"
    ],
    "spec_asserts": "W183-S14: with the flag defaults false, a no-var apply of the harvest root planned 5 destroys of applied build-half resources (the ECR repository among them). It disarms when a no-var plan against the real state applies nothing. W171-S3: the CTO rules on the gateway's copy of the slash-key rule (ruling XA-20261018T094750Z-cbaa).",
    "world_is": "READ BY THIS SEAT 2026-10-20 ~15:0xZ on dell1. W183-S14: `sha256sum infra/aws/terraform/harvest/dossier-refresh.tf` reads 3e068c0ee8ed1e8db6b5fe0989826f3ef9ca219a161bd3be82183bcfc41a1dc7, equal to the owner's figure and the HVST-cn-8 drain's plan input. `git status --porcelain` on the root is empty. `terraform plan -input=false -lock=false -detailed-exitcode` with no -var, in the already-initialized root, reads 'No changes. Your infrastructure matches the configuration.', exit 0. The cures are 0bf0e821b4 (flag defaults aligned) and ab70f25bcf / drain 207db2a041 (schedule default ENABLED), with CTO countersigns @2acfe451aa and @68a5e50abd. Not moved: any later change to the root re-opens the question. W171-S3: org/critical_paths/cross_adjudication/20261019T1238Z_XA-20261018T094750Z-cbaa.md (1.0.0_SA_CTO, 2026-10-19T12:38:14Z) ruled option (a), keep the ~20-line copy guarded by arm 7 of tests/test_cj2_slash_key_one_form.py, and states the row disarms to RECORDED on that ruling. Its binding condition, the test in every opal-gateway release's test list, is unread for the live ref 13917ef993 (site Z batch15), so REMEDIATION_v26 keeps the remediation OPEN.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform plan (no -var) in infra/aws/terraform/harvest -> No changes, exit 0 (this seat)",
        "sha256sum infra/aws/terraform/harvest/dossier-refresh.tf -> 3e068c0e... (this seat)",
        "org/critical_paths/cross_adjudication/20261019T1238Z_XA-20261018T094750Z-cbaa.md lines 15, 51",
        "org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round99/DISARM_WORD_D1-W183-S14_AND_D1-W171-S3_20261020.md @c5eda52375"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record. S14's hazard is measured gone by this seat's own no-var plan, and S3 is disarmed to RECORDED by the CTO's ruling, with its remediation clock left open on the ruling's condition."
  }
]
```

-- 3.0.0_SA_CVO~DELL1
