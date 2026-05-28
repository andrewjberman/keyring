# ws-charter cycle 1326Z — Phase 2A ACTIVATION (ANDREW_DIRECTION)

**Author:** 1.0.0_SA_CTO (ws CTO, respawn session)
**Class:** ANDREW_DIRECTION → Phase 2A activation-sequencing (NOT NOVEL PRD authoring — PRD v0.7.2 already covers Phase 2 scope)
**Cron tick:** first post-respawn /ws-charter cycle (a22eb079)

## Inbox classification

- **CVO 132518Z [ANDREW-DIRECT GREENLIGHT]** → ANDREW_DIRECTION. Andrew (via ws CVO session): "ready to start exploring LinkedIn Phase 2 now... proceed to Phase 2." Phase 1 web-scrape CLOSED (d2033738c) so subset-informing scores exist.
- (Earlier this session: MSTR respawn-directive → co-ratify rendered d2033738c; COO ACK 131232Z → close confirmed + JSON flipped + .037 GO'd; all handled.)

## CTO disposition

Phase 2A is architecturally GO. PRD v0.7.2 (shipped ff27f57ef) already scopes Phase 2 Part A: FULL 99-IMO org-chart-only, Lusha narrowed (/v3/companies/search + enrich + /v3/contacts/prospecting; contact-reveal deferred v0.7.3+; 20-call/IMO cap). No new PRD authoring required — this is activation, not scope expansion.

## Sequencing decision (the CTO value-add)

Two tracks; only ONE gates TO authoring:

**TRACK 1 — SUBSET-CUT (Q1) GATES TO AUTHORING.** Andrew's pick (explicit Phase 1→2 review gate, PRD §4). COO's 4-option framework `5a00ced3b` drafted ready-for-Andrew. CVO Mode A#2 candidate-pool framing to attach: 24 IMOs nonzero am_prominence (7 present amp≥0.50 + 17 adjacent) vs 23 absent + 52 blocked-upstream. → COO routes framework + candidate pool to Andrew for his cut while he's engaged. Hold Phase 2A TO authoring until cut lands.

**TRACK 2 — PRE-LIVE TECHNICAL PREREQS (un-gated; parallel NOW).** Does NOT depend on the subset-cut, so start to compress critical path:
- (a) Verify Lusha key `find-insure/lusha-ai/api-key` live in Secrets Manager (PRD §4 Andrew [SYNC]-provisioned).
- (b) Land KMS CMK `find-insure-data-key` — LinkedIn bronze/silver are PII-bearing SSE-KMS scope (PRD §3.1/§57 v0.4 absorption); must exist pre-first-live-call. AE verifies-then-lands via v0.4 TF kms.tf.
- Both AE 0.7 lane; AE~A off-roster pending respawn (COO 1312Z) — flagged COO to surface to MSTR if a live AE lane is needed.

**Gate logic:** Phase 2A TO authoring fires once (Andrew subset-cut lands) AND (Lusha + KMS prereqs verified GREEN). Tracks run in parallel; neither blocks the other until the join.

## Routed

- COO 132652Z (dispatch owner): both tracks.
- CVO 132701Z: ack greenlight + sequencing.
- CC MSTR (goal-advance awareness, via COO/CVO threads).

## Next-cycle expected state

COO routes subset-cut to Andrew + dispatches AE prereq track. Next tick: check for Andrew's Q1 cut + AE prereq-verification results; if both GREEN, Phase 2A TO authoring is unblocked (COO-dispatched per lane). CVO verifies at LinkedIn Series-detect / org-chart meaning-probe high-leverage moments.
