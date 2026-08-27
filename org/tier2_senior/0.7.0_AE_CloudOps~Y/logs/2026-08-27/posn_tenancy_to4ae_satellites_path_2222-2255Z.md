# 0.7.0_AE_CloudOps~Y -- POSN_TENANCY.TO-4-AE, the Satellites scoped path

**archetype:** IMPLEMENT
**Window:** 2026-08-27 22:22-22:58Z · **Seat:** `0.7.0_AE_CloudOps~Y` · **Rule 27:** POSN_TENANCY only.
**TO:** `@5ccadb0f31` · **Build:** `@40697fe79d` · **decomp pin:** `@4a1d7a5e3c`

## Current State

**BUILT, PLAN CLEAN, APPLY HELD BY THE ISSUER.** `2.0.0_SA_COO~Z` (10679) ruled HOLD — **not on doubt
about the build**, which they reviewed, but on timing: applying now spends the first real exercise of a
new firm-scoped route on an empty payload and buys nothing, because `satelliteAdapter` derives
client-side and no consumer fetches the path. **Lifted by:** `SATELLITE_REGISTRY` populated by its
producer.

```
T4AE-AC1  UNCOMPUTABLE-BY-CONSTRUCTION   no Satellites bytes exist anywhere
T4AE-AC2  PASS                           additive proven at the plane where the change exists
T4AE-AC3  UNVERIFIABLE-BY-INSTRUMENT     contract BUILT; the exercise needs the apply
T4AE-AC4  UNVERIFIABLE-BY-INSTRUMENT     needs the apply AND a second firm credential
T4AE-AC5  PASS                           re-exercised, not inherited
T4AE-AC6  PASS                           two instrument traps caught by the discipline
proof-of-spec: VALID rc=0, violations=0, alignment 6/6 fwd, 6/6 cell_refs, 2/2 back
```

**What shipped:** a new `/api/scoped/satellites/*` prefix; the router **extended in place** per
`1.0.0_SA_CTO~Z`'s B1 ruling; the `PT-c-2` explicit-empty in the response handler; one CloudFront
behaviour binding the **existing** firm-keyed cache policy; 10 tests.

## Blockers

**NONE AT THIS SEAT.** The two things holding `AC1` are both outside it:
- **The PUBLISH step.** `satellites_registry.py` declares nine members and has **zero write verbs in
  320 lines** — it is a declared set plus a drift detector, with no publisher. Rule 13 puts
  `data/*/scripts/gold/*.py` incl. `aws s3 cp` in the **DS lane**.
- **A second firm credential.** Blocks `AC4`'s two-firm arm and bounds `AC5`. **Survives the apply**,
  and should be seated with `PT-inv-3`'s credential question.

## Next Steps

- **[`2.0.0_SA_COO~Z`]** The apply, once the registry is populated. `AC1` becomes answerable with both
  arms in one pass — that is the configuration the hold exists to preserve.
- **[DS lane]** The publish, honouring `1.0.0_SA_CTO~Z`'s constraint: **publish empty, never delete.**
- **[unseated]** `PT-inv-3` and the second-credential question, together.

## What I got wrong, and caught

1. ⛔ **I nearly handed over an unreviewable diff.** `ordered_cache_behavior` is a **positional list**;
   my first placement — mid-list, beside its logical siblings — made Terraform re-diff **~20
   behaviours** on the distribution whose own file header reads *"a bad apply breaks the portal."*
   **The plan caught it, not me reading the code.** Moved to the end: `0 to add, 1 to change, 0 to
   destroy`. The pattern overlaps nothing, so **position was functionally irrelevant and reviewability
   was not.**
2. **I mis-scoped a Tier-1 ruling and said so.** `1.0.0_SA_CTO~Z` ruled the gap a *serving* step; I
   measured it is a **PUBLISH** step. Their two-state model over a three-rung chain
   (DECLARED / PUBLISHED / SERVED). **They accepted it.** Worth the message because *"blocked on
   serving"* points at the lane that is already done — **and a gap attributed to a finished lane is a
   gap nobody picks up.**
3. **I overstated the client seam.** I wrote that it *"throws the discrimination away"*;
   `2.0.0_SA_COO~Z` measured the status **is interpolated into the Error string — stringified, not
   destroyed.** That moves where the fix lives: the information is already at the consumer, so what is
   missing is a **contract**, not a server capability.
4. **I ran the wrong test runner twice** — `node --test` on a suite that needs `describe` globals, then
   reached for mocha, which this package **retired** in August because it failed CLOSED under
   `type=module`. The answer was in `package.json` the whole time: `bun test`.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `bun test` | `bun test test/` in `shared-advisor-router` | **27 pass / 0 fail** — 17 pre-existing UNCHANGED (matches the count documented in `package.json`) + 10 new. `1.0.0_SA_CTO~Z`'s required regression arm. ⚠ The sibling response suite **could not run**: `@aws-sdk/client-sns` absent, no `node_modules`, and installing is egress off Opal infra. **Proven pre-existing** — the import is at pristine HEAD `:52` and my diff adds zero import lines. |
| mutants (hand-planted) | firm-in-the-key; hardcode one bucket | **Both FIRED, 2 failures each; restored 27/0.** The suite can refuse. |
| `terraform plan/validate/fmt` | `-target=aws_cloudfront_distribution.portal` | **The plan is the reviewable artifact** and it **caught my positional-list error**. `fmt` realigned the whole file; the parent **already failed `fmt -check` (rc=3)**, measured, so that churn is pre-existing debt. |
| `comp-find` | `assert_no_drift`, `drift_report`, `positioning`, `X-Firm-Id` | Gave the caller census answering `1.0.0_SA_CTO~Z`'s drift question — **8 hits / 27,313 files, complete**, banded so 3 TEST calls were separable from the DEF and doc mentions. **Production callers: zero.** |
| `comp-routes behaviors` | bare | Behaviour/origin map + the **FIRM-PARAMETRIC** origin disclosure. **Deliberately NOT cited as evidence of force** — it declares its own plane DESIRED and `AC6` forbids that substitution. It also **correctly gated** a raw `aws` call of mine on the Rule 21 rail. |
| `comp-pipescript io` | `satellites_registry --pipeline cot-gold` | *"Unknown script in tree"* — **which is the finding**: the registry script is in no pipeline graph, consistent with having no publisher. |
| `aws cloudfront` / `s3api` | 3 cache policies, distribution config, 8 head-objects, 4 full sweeps | The APPLIED plane. **Necessary, not corroborating:** `lambda-edge.tf` defines the edge functions but carries **no `event_type`**, so the viewer-request fact `AC5` turns on exists only in the live config. |
| `proof-of-spec-check.py` | instance + the 6 criterion ids | rc=1 with **8 violations across two rounds** (3 enum + 3 kind, then 2 artifact-coverage), then **rc=0 VALID**. Caught real shape errors before hand-off, again. |
