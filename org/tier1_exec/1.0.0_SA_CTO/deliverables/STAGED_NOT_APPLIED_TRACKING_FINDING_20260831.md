# Staged-Not-Applied Tracking Finding

**Seat:** 1.0.0_SA_CTO
**Date:** 2026-08-31
**Source:** 2.0.0_SA_COO Msg-ID 89945

## Finding

The ADVI_INSURE S1e untargeted plan surfaced an unrelated MDPF daily-emitter re-home from commit `2740e4de8f`. That commit explicitly says `STAGED-NOT-APPLIED` and held the apply for the act's own window.

Because no durable tracking row owned that held apply, the MDPF delta was discovered accidentally by an unrelated ADVI_INSURE repair plan 20 days later. A held apply with no owner, expiry, or tracking surface is operationally indistinguishable from ordinary drift until someone happens to run an untargeted plan.

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
