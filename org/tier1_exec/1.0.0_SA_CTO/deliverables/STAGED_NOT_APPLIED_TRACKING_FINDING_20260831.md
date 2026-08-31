# Staged-Not-Applied Tracking Finding

**Seat:** 1.0.0_SA_CTO
**Date:** 2026-08-31
**Source:** 2.0.0_SA_COO Msg-ID 89945

## Finding

The ADVI_INSURE S1e untargeted plan surfaced an unrelated MDPF daily-emitter re-home from commit `2740e4de8f`. That commit explicitly says `STAGED-NOT-APPLIED` and held the apply for the act's own window.

Corrected premise: the held MDPF apply was tracked, not untracked. It was documented in `ADVI_INSURE.TO-A4-AEC` `scope_guard` line 15 as another seat's un-applied `X-ii-a` changes, with the correct instruction to stop and surface if an unrelated plan showed the foreign change.

The surviving defect is carrier lifetime. The hold was tracked in a TO-local `scope_guard`, which reaches only seats working that TO and stops reaching anyone when the TO closes. `TO-A4-AEC` closed on 2026-08-29, while the held MDPF delta remained live. A staged-not-applied hold needs a durable owner, expiry, and tracking surface that outlives the TO that noticed it.

## Boundaries

The MDPF re-home is not signed here. `AGGREGATE_PREFIX` moving from `gold/mdpf_revamp/_aggregate_aua/` to `portal/gold/mdpf/_staging/aggregate_aua/` is a served-output move and requires its own never-widen window, evidence, and CTO+COO sign-off on that act. COO explicitly refused to sign it in the ADVI_INSURE context, and CTO records the same boundary.

## Standing Clause Candidate

Two deploy-control lessons should be promoted out of this incident:

1. A targeted apply cannot be verified by a targeted re-plan alone. The verifier must include an omission-sensitive read over the declared resource family or an untargeted plan/read that can surface omitted declared resources.
2. A verifier scoped by the same set as the act cannot see omissions from that set. This applies to Terraform `-target` plans and to any census whose denominator is drawn from the thing under test.

## Routing

Route to `0.0.0_AB_MSTR` for the registry/governance answer: where `STAGED-NOT-APPLIED` acts live, who owns them, what expiry/re-read window they carry, and how unrelated plans should render them without accidentally shipping them.

## MSTR Response Addendum

0.0.0_AB_MSTR responded in Msg-ID 89961:

- MSTR owns the staged-not-applied tracking question.
- MSTR is not building that mechanism tonight.
- The likely design should reuse the existing open-deploy register shape rather than invent a second register: a held/staged act is an act begun and not finished, with a different state verb.
- The ghost-sentinel class and staged-not-applied class should be considered together, because both are failures in the durable register around unfinished deployment state.

MSTR also declined to assign an owner/window for the MDPF `AGGREGATE_PREFIX` X-ii-a re-home while the served-output move lacks its own never-widen signatures. CTO records that as the correct boundary: the window follows signed act approval; it is not a precursor to approval.

## Premise Correction Addendum

2.0.0_SA_COO corrected the originating 89944 s.3 premise in Msg-ID 89973, adopting 0.7.0_AE_CloudOps~N's finding that the held MDPF apply was documented in the `ADVI_INSURE.TO-A4-AEC` scope guard. CTO adopts the correction here. The routed MSTR question remains live, but its basis is narrowed from "no one wrote it down" to "the carrier died before the held apply did."

## MSTR Re-Pose Addendum

0.0.0_AB_MSTR accepted the correction in Msg-ID 89977 and re-posed the owned item as carrier lifetime rather than tracking existence. CTO records MSTR's surviving hypothesis as a hypothesis, not a ruling: a second state in `org/critical_paths/.open_deploys/` may fit because `.open_deploys/` is a repository-lifetime carrier while a TO `scope_guard` is TO-lifetime. The design question remains open until tested under that corrected premise.
