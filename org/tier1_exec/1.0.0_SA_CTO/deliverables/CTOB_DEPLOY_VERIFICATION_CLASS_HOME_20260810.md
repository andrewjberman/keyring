# Deploy-verification class — the HOME for mechanism (2) and the generalization sweep

**Seat:** `1.0.0_SA_CTO~B` · **Date:** 2026-08-10 · **Status: BANKED, NOT STAFFED**
**Provenance:** Andrew-direct at the MSTR terminal ~1748Z 2026-08-10, VERBATIM: *"I would recommend
this work to CTO~B rather than CTO Base, they are too busy to deal with this."* Relayed by
`0.0.0_AB_MSTR` 175239Z; base-CTO disposition 175017Z inherited unchanged.

⛔ **Nobody comes off the MDPF repair for anything in this file** (Andrew ruled MDPF repair the main
fabric priority 2026-08-10 ~1620Z). This file exists so the class does not evaporate — all four
members were found INCIDENTALLY while chasing something else.

---

## The class (one line)

**The deploy-verification layer disagreeing with the deployed artifact, in BOTH directions.** Full
mechanism table + the direction asymmetry (false STALE is loud and cheap; false GREEN silently costs
the assumption that deployed code is reviewed code; and the noisy defect degrades the detector that
would catch the silent one):
`memory/feedback_an_atomic_commit_is_not_an_atomic_deploy_config_has_no_leg.md` (auto-memory store).

## Disposition of the four mechanisms — where each one LIVES

| # | mechanism | direction | home | status |
|---|---|---|---|---|
| 1 | `safe-deploy` PIPELINE_MAP resolves scripts-only | FALSE GREEN | gate candidate routed to COO 2026-08-07 (extend deploy leg to declared config paths, or fail push on unresolvable commit member) | NOT built |
| 2 | m365-gateway deploy tar = explicit include list, cannot print its exclusions | FALSE GREEN | **THIS FILE + owner notification** (see below) | FIXED `@2582eb244` (site Z) — see caveat |
| 3 | `comp-pipescript deployed` raw-md5 vs CRLF | FALSE STALE | MDPF register **R-33** (`docs/architecture/MDPF_REMEDIATION_REGISTER.md`), amended `@fb53baf1c6` to measured-on-two-instances | OPEN (register-tracked) |
| 4 | commit-vs-landed never reconciled at all | FALSE GREEN | the generalization sweep (below) — (4) is not a bug in one leg, it is the ABSENCE the sweep enumerates | banked |

## Mechanism (2) — the record, homed here per base's ruling

**Base-CTO ruling inherited (175017Z, not re-adjudicated):** (2) MUST NOT get an MDPF register row.
The m365 gateway is not MDPF; filing it there buries a gateway defect where its owner will never
look, while making the register assert coverage it does not have (Rule 24 scope error).

**The defect:** the gateway deploy tar was built from an EXPLICIT INCLUDE LIST — a file absent from
the list silently did not ship, and the deploy reported success. FALSE GREEN by construction: an
include list that cannot print its own exclusions is the defect, not the list.

**Owner (grounded 2026-08-10):** `infra/aws/ec2/EC2_MANIFEST.json` `/services/m365-mcp-gateway` —
`deployed_by: 0.7.0_AE_CloudOps~Z`, deploy script `infra/aws/ec2/m365-mcp-gateway/deploy-to-ec2.sh`.
**CloudOps holds the gateway.** Owner notified by MCP this date (record act, no work ordered).

⚠ **CAVEAT — the fix citation is RELAYED, not locally verified:** `2582eb244` does not resolve on
this checkout (`git show` → unknown revision at 2026-08-10T18:0xZ). It is a site-Z commit not yet
fetched here, per MSTR's relay. Anyone closing (2) verifies the fix against the DEPLOYED gateway
artifact (manifest `file_checksums` vs live `/opt/m365-mcp-gateway`), not against this citation.

## The generalization sweep — banked at CTO~B

**The question the sweep answers:** for EVERY deploy leg in the estate — `safe-deploy`,
`safe-ec2-deploy.sh`, each `deploy-to-ec2.sh`, the Terraform S3-artifact legs, the portal promote,
any ad-hoc `aws s3 cp` leg — does it (a) compare NORMALISED bytes of what it INTENDED to ship
against what is ACTUALLY at the destination, and (b) ENUMERATE WHAT IT EXCLUDED? Every leg failing
(a) is a member of mechanism (4); every leg failing (b) is a latent mechanism (2).

**The control shape, if ever built (MSTR-relayed, base-adopted, inherited verbatim):** a
**denominator printed by the deploy leg itself** — the deploy-layer instance of CLAUDE.md's "print
the denominator of every retrieval you reason from."

⛔ **FENCE (carried intact):** this is EXPLICITLY NOT an alarm, monitor, freshness checker, or
SNS/SES anything — the 2026-07-28 moratorium stands and none of this routes around it. Printing a
denominator inside the deploy act is a different act from building a detector.

**Activation:** requires an explicit staffing decision (Andrew or CTO-base routing CTO~B onto it
once MDPF repair no longer holds priority). Until then this file is the whole deliverable.
