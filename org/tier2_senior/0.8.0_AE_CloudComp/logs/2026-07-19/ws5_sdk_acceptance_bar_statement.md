# NFRA_SYSPARITY.WS-5 -- SDK cloud-acceptance-bar statement

**archetype:** SCRIBE (a durable STATEMENT/label task, not a build -- CTO pre-ruled)

**Session:** `0.8.0_AE_CloudComp~Z` | **Date:** 2026-07-19 | **TO:** NFRA_SYSPARITY.WS-5 @bd698aebf
(COO context-reallocation of the ~Z docs/comp-tools lane, Andrew-direct idle-reallocation). Spec:
`docs/architecture/NFRA_SYSPARITY_PRD.md` S3 (WS-5, CTO-pre-ruled local-only) + brief §3 Infrastructure.

## What WS-5 asked

Make the SDK's cloud-acceptance bar EXPLICIT, not silent. The SDK terraform is faithful-by-construction but
UNEXERCISED (Rule 22a: DESIRED, never `terraform apply`'d). CTO PRE-RULED: do NOT apply a new tenant to AWS
now (consolidation phase + new-territory discipline) -- DECLARE local loop-closure as the accepted v1 bar,
with the Rule-22a caveat LABELED in the SDK header. The label must MATCH reality (CVO fire-2: tier=local), no
overclaim.

## What landed

Added `## Cloud-tier acceptance bar -- EXPLICIT (Rule 22a; NFRA_SYSPARITY WS-5)` to `infra/system/sdk/README.md`
(line 102), a durable statement:
- **v1 bar = LOCAL** (a stated choice): `genesis verify --local` loop-closure + the `--sandbox` storage-substrate
  proof + `up --dry-run`.
- **Rule-22a caveat, LABELED:** the parameterized TF module (P1) is FAITHFUL-BY-CONSTRUCTION but CLOUD-UNEXERCISED
  -- DESIRED, never `terraform apply`'d to a real tenant on AWS (validate-clean + literal-free + version-pin-synced,
  but no tenant provisioned to cloud). Deferral is DELIBERATE (consolidation + new-territory), not oversight.
- **Post-consolidation proof = a one-tenant `terraform apply` smoke** (out of v1 scope; gates to safe-apply + CTO).
- **Label matches reality:** `tenants/*/verify-report.json` reports `"tier": "local"` (both acme + demo; CVO
  fire-2 confirmed) -- explicit "do not read the local PASS as cloud-exercised."

The distinction I was careful to preserve (accuracy, not overclaim in EITHER direction): the loop LOGIC closes and
the STORAGE substrate (`--sandbox`) was exercised on real cloud S3/Iceberg; it is the full tenant PROVISION (the TF
module) that is DESIRED-not-APPLIED. "Faithful by construction, never by exercise" -- stated exactly.

## Cross-lane coordination (WS-5 x ~C's WS-4 Part-B, both touch infra/system/sdk/)

Per the TO's coordination directive: my WS-5 surface = `sdk/README.md` (the Acceptance section) ONLY. ~C's WS-4
Part-B = the SDK vocabulary-bound schema (recognizer_sdk adapter / ontology_ref / schema.json), COMPLETE + held at
CTO. Surfaces are DISJOINT (a doc header vs the recognizer schema) -- no file collision. Pinged ~C @215109Z to
confirm before commit; COO brokers if we collide (we do not).

## Compiler Tools (AC4 -- mandate <run> reproduced, observed vs <expect>)

| Phase | run | observed | vs expect |
|---|---|---|---|
| 1 before-write | read SDK header (`sdk/README.md`) + confirm tier=local (`tenants/*/verify-report.json`) | README already documents local/sandbox acceptance + "cloud up apply OUT of this pass"; both verify-reports `"tier":"local"` | PASS -- the Rule-22a framing was present-but-scattered/implicit; tier=local confirmed (matches CVO fire-2). Made it an EXPLICIT labeled statement. |
| 3 after-commit | grep the SDK header for the acceptance-bar statement + Rule-22a caveat | 4 hits (Cloud-tier acceptance bar / DESIRED-never-apply / tier=local / post-consolidation proof) + the `## Cloud-tier acceptance bar` header @102 | PASS -- the SDK now STATES the bar + caveat durably (not silent). |

No comp-* query tool applied: WS-5 is a docs statement over a self-contained SDK header; the grounding is the
verify-report tier (live artifact) + the SDK's own P-status, not a graph/pipeline query.

## LD-0318 CVO gate

Per AC3 + LD-0318: CVO verifies the stated bar MATCHES reality (its fire-2 already confirmed tier=local, so this is
a light confirm the LABEL matches -- no overclaim of cloud-exercise). Pinging CVO on land.

## Outcome

WS-5 COMPLETE: the SDK's cloud-acceptance bar is now an EXPLICIT, reality-matched statement (local v1 bar + the
Rule-22a DESIRED-not-APPLIED caveat + the post-consolidation apply-smoke proof), closing the un-declared Rule-22a
gap the brief flagged. No overclaim (tier=local, verified). Coordinated disjoint with ~C's WS-4 Part-B.
