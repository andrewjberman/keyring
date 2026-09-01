# ADVI_PERFRP Peak-Priority Triage - 49F Portal Non-Population

**Seat:** 1.0.0_SA_CTO
**Date:** 2026-08-31
**Source:** 2.0.0_SA_COO Msg-ID 90070
**Status:** ACTIVE

## Finding

COO measured that 49F performance-reporting data is not served to the portal plane at all:

- `portal/gold/` under `opal-data-assets` exposes `etfs/` and `mdpf/` only.
- No `advi/` prefix and no `perfrp/` prefix are served there.
- `opal-data-49financial` exposes `_campaign/`, `_code/`, and `gold/`, with no portal/serve prefix.
- Positive control: `portal/gold/mdpf/49financial/account-distribution/...` exists, so 49F data can reach the portal plane through a served path.

CTO accepts the measured distinction: 49F model-portfolio data reaches the portal; 49F performance-reporting data reaches no served portal prefix. This is sufficient to explain frontend non-population for performance-reporting views, while not proving the frontend render path is otherwise defect-free.

The portal code path is not the first suspect for this specific symptom. COO reports the portal submodule at `local HEAD == origin/DEV == be39451b`, with TO-R1-DE's six portal commits published to DEV and zero pending commits.

## Gate Read

The current non-population is consistent with the registered `ADVI_PERFRP` project row:

- the project remains under a build-only / DEV-only cap;
- the P4I-3 publish activation sits behind Andrew's 2026-08-21T19:18Z 49F-flip hold;
- serve/flip remains the arm-(a) sovereign gate shared with `ADVI_INSURE`;
- the served-data precondition is real and engineering-owned: every served PERFRP leaf must remove client display labels and custodian account identifiers from label/identity/key fields, with server-side pseudonymisation and book-scoping equivalent to the platinum `summary.json` posture.

Conclusion: the frontend is empty because the PERFRP publish is held and no served PERFRP prefix exists. If Andrew is looking at PROD, this is the primary explanation. If Andrew is looking at DEV and expects DEV data to be present, the missing served prefix still explains the empty state but may mask an additional render-path defect.

## Immediate CTO Action

CTO treats D2 `ADVI_PERFRP` as the peak-priority workstream, above `ADVI_INSURE` and above D8 standardization unless D8 protects the D2 path.

CTO authorizes COO to shape and seat the publisher-lane work package for the engineering precondition, without waiting for the sovereign flip:

1. define the served PERFRP leaf set that would be published;
2. remove raw client display label fields from served rows;
3. ensure no custodian account identifier appears in label, identity, or key fields, including the UNMAPPED sentinel class;
4. apply book-scoped, server-side pseudonymisation consistent with the existing portal serving posture;
5. emit a census over every served row proving zero name fields and zero custodian account identifiers, with denominators and positive controls;
6. keep the publish/flip itself gated behind Andrew's explicit word.

This work is not a production flip and does not consume the sovereign publish decision. It makes the flip grantable and gives Andrew a concrete answer for why performance reporting is not currently populating.

## Open Question to Carry

Andrew should answer one routing question so the next diagnostic branch is not guessed:

**Is the observed non-population on DEV, on PROD, or both?**

- PROD-only: current finding is likely complete; publish remains held by design until the sovereign gate is released.
- DEV too: after the served-data work package is shaped, assign a frontend fixture/render validation to prove the Books / Book toggle views render correctly when PERFRP payloads are present.

## Boundary

No vendor egress, deploy, production flip, schedule change, or `ADVI_INSURE` dispatch is authorized by this record. W2 remains autonomous on the Black Diamond mint watch. `ADVI_INSURE` remains parked to its scheduled S1e fire and must not draw focus from core D2 performance reporting.

## Andrew All-Capacity Addendum

0.0.0_AB_MSTR Msg-ID 90077 carried Andrew's 22:1xZ direct word:

> Yes set up a seat for whoever is nedeed on ADVI_PERFRP, the fabric is relatively quiet right now, that should be pushed forward with all available capacity

MSTR reports two lanes reseated under their existing serials so the live task-order addresses still resolve:

- `0.4.0_DE_ClientPlatform~D` for `TO-R1-DE`, portal AdvisorIntelligence pages on DEV.
- `0.7.0_AE_CloudOps~G` for `TO-R1-AE`, publisher wiring, IAM, EventBridge/Scheduler, and Terraform.

CTO accepts the capacity authorization but not as a serve-flip lift. The 2026-08-21 49F-flip hold and the build-only / DEV-only cap still stand unless Andrew explicitly releases them.

CTO capacity ruling sent to MSTR at 2026-08-31T22:20:44Z:

- seat `0.4.0_DS_ClientPlatform~G` for the DS producer/start-condition lane;
- do not retask `0.4.0_DS_ClientPlatform~Y` away from W2;
- do not consume `0.4.0_DS_ClientPlatform~W` from the Tuesday `ADVI_49F` V-4 wait unless COO later rebalances;
- sequencing remains owned by `2.0.0_SA_COO`.

Channel note: the outbound ACK to MSTR delivered by filesystem but again returned `sender unverified`; this is a channel/registration hygiene issue, not a failed delivery.
