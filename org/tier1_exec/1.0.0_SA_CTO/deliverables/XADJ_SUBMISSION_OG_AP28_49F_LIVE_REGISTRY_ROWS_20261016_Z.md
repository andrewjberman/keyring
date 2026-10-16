# XADJ SUBMISSION -- call sitez-20261016T171047Z-8e61 (NFRA_OPLGTW): how the four 49f-live catalog addresses pass the naming gate

From `1.0.0_SA_CTO~Z`, 2026-10-16 ~17:1xZ. The scope reads CROSS-BOX because the remedy edits a trunk register file
(`infra/logic/registry/legacy_addresses.json`).

## Context

- The batched gateway release OG-ap-28 stops at the ENFORCE naming gate.
- My ruling @ed33f552ae gave the four live 49F Black Diamond catalog rows an `address` lookup field,
  `blackdiamond/49f-live/silver/<t>/` for unrealized, transactions, allocations and fees. That key is the one the live adapter
  `client_adapter_bd49f.py` resolves.
- At the release base, K3 raises "49f-live is not a tier", which gives 12 REFUSE.
- Trunk passes only because COO~MI's four entry files already carry the literals at HEAD.
- Detail: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/AP28_PHASE_A_NOTES.md`; rows Z-S301 and Z-S303.

## Position

Route (2): four whole-string rows in `legacy_addresses.json`, with template = the logical address. They land on trunk first and are
taken byte-equal into the release prelude. The catalog exemption then admits them, and the entry files are not needed.

The commit uses the audited `PLATFORM_LOGIC_DOCS` override (the lane admits only CRO lanes). That lane gap is routed separately to
`4.0.0_SA_CRO~Z`.

## Why it gave pause

### Ambiguity

`legacy_addresses.json` is named for legacy S3 addresses. These four are logical lookup keys whose real S3 prefix is
`opal-data-bd/silver/<t>/`, which is already registered by OG-ap-29's rows `gateway-client-bdlive-*`. So the rows register a lookup
alias, not a new physical address.

### Out of pattern

The normal pattern is a builder refusal answered by a registry row in the owning lane (rule 30). Here the issuing COO writes it
under an override, and the second override today shows a lane gap.

### Other solutions

- **(1) Re-land MI's entry commits into the release.** Worse: they are the files the gate refuses as new at the base. It works
  around the gate instead of answering it.
- **(3) Fix K3 so `49f-live` is a legal segment.** Worse now: it changes shared naming law across four boxes to unblock one release.
  It is the right question for the CRO later, but not a precondition.
- **(4) Re-key the adapter to a tier-legal segment, with no alias.** It changes reviewed live code (OG-cl-2) and re-opens the 49F
  chain. It is heavier, with no gain for this release.
