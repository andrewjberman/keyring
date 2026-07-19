# Session Close 2200-2350Z -- WS-8 SDK-fidelity fixes + IAM-fidelity sweep [lane ~B]
**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Summary
Final window of the ~B respawn (Andrew-direct sanctioned wind-down @235036Z: "let them wrap up and log their
sessions"). Continued from the WS-8 build (@d78cd53a1): hardened the cross-walk to fail-closed, then executed
the SDK-fidelity fixes it surfaced + a one-time IAM-fidelity security sweep. All CTO/CVO-verified + accepted.

## Work
1. **WS-8 cross-walk hardening** (@b721ce89d, CVO rec): advisory -> FAIL-CLOSED via a declared-exclusions
   config (sdk_crosswalk_scope.json). Turned "7 advisory flags" into "1 real question" (fedobs). self-test
   discriminates both directions (declared-excluded=OK vs undeclared=fires). CVO HARDENED CLEAR.
2. **SDK-fidelity fixes** (@a619805de + @fa5069549). My Rule-22 grounding FLIPPED CTO's FEDOBS ruling
   (OMIT->FIX) -- the SDK provisions the fedobs producer (required loop_producer) but on the shared
   derive_runner role = **fail-OPEN** (tenant could write semantic truth). CTO: "declaring OMIT would have
   MASKED a security-relevant gap."
   - **fedobs.tf FIX**: parameterized the scoped read-only-on-truth emitter role into the SDK + wired the
     producer to it. Rule-22a on the applied real role: PutObject truth-prefix=explicitDeny / findings=allowed.
   - **intraday.tf FIX -> EXTENDED** (CTO ruled mirror-the-real-role over minimal): full BoundedDeriveReadOnly
     (~28 read-only Describe/Get/List) -- CVO's DescribeTable was the tip of a whole-policy omission.
   - **fedobs_glue.tf** declared-excluded (Trino query-layer). Cross-walk -> PARITY. CVO CLEAR.
3. **One-time IAM-fidelity sweep** (@145fccb7f, CTO security-ruled): 9 SDK globgrph roles vs real applied
   counterparts. VERDICT CLEAN -- no 3rd fail-open/under-grant beyond the 2 fixed. Deny-boundary census (only
   fedobs had one) + Rule-22a sims (trino read-only confirmed: PutObject-on-truth=implicitDeny). CTO-accepted
   as "a COMPLETE negative, denominator-printed."

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| aws simulate-principal-policy | Rule-22a (rail-checked): intraday DescribeTable=allowed; fedobs truth=explicitDeny/findings=allowed; trino truth=implicitDeny/read=allowed -- isolated controls, separate invocations | PASS (grounded) |
| aws iam get-role-policy / list-role-policies | Deny-boundary census on 3 real task roles (applied truth) | PASS (only fedobs Deny) |
| comp-iam | `comp-iam roles` (real globgrph role enumeration) | PASS |
| terraform fmt | HCL format on the SDK module edits | PASS |
| commit-gate | on sdk_crosswalk.py (E402/E702 caught+fixed) | PASS |

**Why raw aws over comp-iam here:** Rule 22a MANDATES simulate-principal-policy for (action,resource) +
resource-scoped Deny boundaries; comp-iam models action-only + fails-green on resource (explicitly insufficient
per CLAUDE.md 22a) -- so the raw primitive is correct, marked `# rail-checked`. **Gap:** none.

## Blockers
None. server.py Stage-B is event-gated (below), not a blocker.

## Current State (handoffs -- correctly PERSISTING, do not force)
- **server.py Stage-B** -- production-confirm the commit-worker auto-comes-up under 7a264bb1f on the next
  NATURAL broker restart (Stage-A fixed + worker revived pid 402317; the running broker still holds old code).
  Flag 2.0.0_SA_COO + 1.0.0_SA_CTO on the restart. Do NOT force a disruptive restart (non-lossy).
- **Standing IAM-fidelity cross-walk tool** -- blessed-DEFERRED post-consolidation (design+warrant banked in
  IAM_FIDELITY_SWEEP_20260719.md + the boundary-naming). Build when Andrew signals the consolidation phase changed.

## Next Steps
- **[0.7.0_AE_CloudOps~B / successor]** hold for the natural broker restart (Stage-B) + Andrew's next phase-steer.
- **[2.0.0_SA_COO / 1.0.0_SA_CTO]** flagged on Stage-B when the restart fires.
