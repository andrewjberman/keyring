# MDPF_TAXSMA v0.2 — L4-R admitted, L5 handoff

Author: `1.0.0_SA_CTO~A`. Recorded: 2026-09-15T08:50:04.057346+00:00.

**Current v0.3 is submitted for both independent L4-R reviews under CTO97152.** The PRD is DRAFT and contract0.3.0 is PROPOSED_L4_REVIEW; v0.2 signatures are historical and do not sign the changed halves. F1 uses gateway, F2 adds S19 complete Silver, and F3 retains the single historical 49financial served home under granted X7; Global retains granted X2. The gateway row is an S02 build prerequisite only and does not hold PRD landing or review. L6 lifts when both current v0.3 halves are signed under97126. The records below preserve prior v0.2 admission; they are not current v0.3 approval.

For v0.2, `python .tools/prd-signoff.py status MDPF_TAXSMA` was read after CRO notice 96992 and returned both halves SIGNED/current. The project stays `dep_stage=PRD` until COO produces the next limb. Its placement is D8 / MDPF / laptop; the D9 business workflow is separate.

## Independent approval

| Half | Reviewer | Review | Signature commit | Current half SHA-256 |
|---|---|---|---|---|
| ratified-text | 3.0.0_SA_CVO | org/tier1_exec/3.0.0_SA_CVO/deliverables/PRD_REVIEW_MDPF_TAXSMA_v0.2_RATIFIED_TEXT_HALF_20260915.md@20504bde03 | 214982df0b | fed0ad5c18f33765a8e3aaf08bb8fcd1018af3a6ee109340b2ec5fa5ca634fd3 |
| brief | 4.0.0_SA_CRO | docs/briefs/sources/MDPF_TAXSMA_L4_BRIEF_REVIEW_v0_2_20260915.md@f5a6d57e4a6377a9195383c7b9e8285da71e4b48 | 905d2df375 | f67f3a541306f2cf09f706e4fbcb5e5529318c4c193a691cd8ad69f614a97a0e |

Both signatures bind to PRD v0.2 at `8ab2dc2bc63fe8699e01fc33772b6f8523d224f0`. The author does not alter or supply a signature. The approved content includes all eight original endpoint bars, explicit dated operator attestation for initial membership, all 18 brief headings, and the current known-value display rounding rule.

Finalization changes only the PRD header status DRAFT→RATIFIED and the data contract's approval-state metadata PROPOSED_L4_REVIEW→RATIFIED, plus their companion receipts. Both signed PRD section hashes are unchanged. Every contract field except `state` is identical to its reviewed v0.2.0 object. PRD and contract versions remain v0.2 / 0.2.0 because this is approval metadata, not a substantive revision. Canonical shape checks returned zero violations.

## Handoff artifact set

- PRD: `prd/MDPF_TAXSMA_PRD.md`, with 18 owned surfaces and eight approved endpoint bars requiring EXERCISED proof.
- Normative data contract: `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` v0.2.0.
- `prd/component_manifest.yaml`: 47 declared primary, companion, dependency and produced-artifact entries; the underlying owned surface and dependency sets remain S01-S18 / D01-D08.
- `prd/AUTHORING_CHECKS.md` and `prd/authoring-checks.json`: checked structure, coverage, endpoint equality, unchanged signed halves and metadata-only finalization.
- Pinned brief/L2 approvals, governing contracts and certified source evidence remain as cited by the signed PRD. Only `rectangle.final.certified.json@4ff8d9bdaa` is the admitted source rectangle; the documentary certificate is not implementation proof.

## Next limb and routing

The next limb is **L5 decomposition, owned by COO**. A scoped `comp-find --name MDPF_TAXSMA_DECOMP.md --under org/missions/D8/MDPF/MDPF_TAXSMA` returned zero matches across seven indexed files; this measures absence of that canonical output, not the owner's activity or unrelated work. No stalled-owner claim is made.

The notifier has released the v0.2 package after both signatures, but its recorded recipient is None and state UNSENT because `project.json` has no `coo_lane`. Source inspection of `.tools/prd-header-notify.py` confirms that this intentionally holds release until the round-holding lane is named. The author sent the concrete admitted package and lane-assignment request to `2.0.0_SA_COO` at 2026-09-15T08:47:33Z. The author will route the final metadata commit and use the canonical notifier once that assignment exists; no arbitrary lane or substitute sender is inferred. Delivery/READ proves transport or intake, not L5 completion.

No runtime implementation, workbook mutation, production activation, task-order issuance, merge or push follows from this signature record. The explicit named-person unattended-content authorization still precedes capability activation. Runtime release checks remain as specified for this project. The separate portal promotion is complete; the scheduled Cottonwood hotfix verification remains a separate assignment.

Routing update after **CTO97073 at2026-09-15T12:55:50Z**: Andrew resolved the competing next-slot claims: **MDPF_TAXSMA takes the next free COO slot, followed by NFRA_OPLGTW**. `org/missions/SEQUENCE.yaml` v4 at`8f0c4fa2bf1538031561ed60993976956e974efa` places both in stage0; current sequence-check reports TAXSMA PLACED/NEEDS-SLOT and first in next-slot order. **The pending-Andrew-ruling hold is released.** MSTR owns naming the actual lane under the three-COO cap; `coo_lane` remains null until assigned. NFRA_OPLGTW keeps COO~O. Once MSTR names the TAXSMA seat, CTO~A records its exact serial and fires the canonical L4 notifier for this unchanged admitted v0.2 package. `L5_ROUTING.md` preserves the full ruling and superseded history; the rejected tail-placement proposal8c70cabc48 remains NOT ADOPTED. L4 remains ADMITTED; no L5 delivery or decomposition is claimed before it occurs.


**Lane reservation update, MSTR97076 / LD-0569 at f0f86cae9a:** MSTR names fresh `2.0.0_SA_COO~T`, to launch after COO~F exits. It explicitly requires waiting for its subsequent live-session line before canonical notification. Because the installed post-commit hook reoffers held releases on every commit, `coo_lane` remains null until that confirmation; this is an operational launch wait, not an unresolved priority decision. `L5_ROUTING.md` carries the exact notice, hook ordering and next action. No canonical delivery has yet occurred.

**Live-lane binding, MSTR97081, 2026-09-15T13:20:53Z:** MSTR confirms fresh COO~T was launched after COO~F exited and directs canonical status verification before binding. The unchanged repository `org/mcp/server.py:get_agent_status("2.0.0_SA_COO~T")` returns **LIVE**, last seen10s ago, PID26332, working on MDPF_TAXSMA startup/L5. `project.json` now binds that exact lane. The launch wait above is satisfied; the installed canonical notifier can reoffer the held v0.2 release. Actual delivery evidence belongs in `L5_ROUTING.md`; L4 stays ADMITTED and the project remains at PRD pending COO~T's L5 artifact.

**Canonical send receipt, 2026-09-15T13:25:23Z:** Binding commit `a245ccd226` triggered the installed notifier, which sent **97083** at13:22:49Z from CTO~A to exact COO~T. The broker reports **SENT**, with no emitted_at or acked_at at the measured time; READ is pending. `L5_ROUTING.md` carries the pinned release, exact receipt, unchanged PRD/contract hashes and fresh sequence-check (stage0, no flags, G/O/T capacity3/3). The requested bind-and-send act is complete; COO~T owns the next L5 artifact.

**Final intake receipt, 2026-09-15T13:30:03Z:** Canonical `delivery_state(97083)` returns **READ**, `acked_by=2.0.0_SA_COO~T`, `acked_at=2026-09-15T13:26:22.594818+00:00`. The notifier retired the outstanding row. This supersedes the SENT-only observation above and completes the L4 handoff to the assigned L5 owner; it does not claim a decomposition or exercised endpoint.
