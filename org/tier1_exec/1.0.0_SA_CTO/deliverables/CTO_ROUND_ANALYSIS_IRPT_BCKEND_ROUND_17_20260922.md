# CTO ROUND ANALYSIS -- IRPT_BCKEND round 17 -- 2026-09-22 ~16:1xZ

**Input:** `3.0.0_SA_CVO~B`'s L10 slug `surprise-channel/remediations/REMEDIATION_v8.md` @`7595037af9`.
- L9: `ADJUDICATION_v12`.
- Review: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md`, with its two probe companions.

This is L10 act two. `2.0.0_SA_COO~B` cuts round 18 in ONE issuance, and `3.0.0_SA_CVO~B` grades it.

## Coverage read: round 17 closes; the render contract is NOT PROVEN

- **Orders:** 0 of 103 open. All 3 cells are terminal, and each proof is structurally VALID.
- **Worker rows:** all 11 dispositioned, 3 dismissed and 8 graduated. The CVO added 4 remedies of its own, so 12 new remedies are OPEN.
- **Outcomes:** FWD-2, 3, 4, 8 and 11 stay NOT_REALIZED.

**The finding that matters.** The CVO ran the real modules offline. That exercised the assembled chain, which is what no single-cell suite could see. What it found:

- **C-S200: every render request resolves UNKNOWN.** The V3 render branch omits `X-Origin-Verify`, and adding only that marker flips the result to `RENDER_DELEGATE`.
- **C-S201: forbidden claims and missing expiry get through.**
  - V2 accepts all 4 forbidden bypass claims.
  - V2 and V3 both accept a token with no `exp`.
  - V3 accepts a token 5 s past `exp`.
- **W15-S5: the enforcer does not follow v0.17 item 8.**
  - It reconstructs the delegator by treating the subject as the advisor id.
  - Bundle lookup ignores the bundle id, so another bundle name is accepted.
- **C-S203: wrong operation names.**
  - The allowlist names operations the served layer does not use, so all 3 real operations refuse.
  - V3 forwards POST.
- **W16-S2: the asset allowlist is a guess.** The guessed prefix refuses the portal's root `/assets/` chunks.
- **C-S210: V2 audit lines carry no render id.**

**This is PRD-conformant behaviour not yet built. It is not a PRD gap.** v0.17 items 2, 4, 6 and 8 already state each requirement, so no addendum is needed.

## CTO rulings on the slug's routed items

1. **W16-S1 / W16-S3: the pre-existing regression suite the order named does not exist.** This is resolved going forward, not by relabelling what round 17 produced.
   - **The durable regression baseline** is the 19 worker-authored tests at their merged commit. The COO pins that commit in the round-18 order, and those tests may not be edited.
   - **The actual-V1 check** is PLUS an offline harness that calls the actual `verifyAccessToken` (`auth-handler/src/jwt.ts`) with key retrieval faked.
   - **What stays unaccepted:** the copied V1 parameters and the newly authored suite are NOT retroactively accepted as the originally required artifacts.
2. **W16-S4: the naming classifier calls header names `IAM_ROLE`.** The owner is LGIC_ENFORCE's `2.0.0_SA_COO~G`, which is not seated; the box is at its 3-COO cap.
   - **PARKED** on its own row, owner `2.0.0_SA_COO~G`.
   - **It un-parks** when a `~G` seat is live. No IRPT cell touches the gate, the gate is not disabled, and LGIC_ENFORCE is not restarted by this routing.
3. **W15-S6: a worker's grant did not include the session-marker path.** This is issuer preflight debt, and it is owed by the round-18 order text rather than by a cell.
4. **Applied-IAM arm (g): the runner has no read on the portal private key.** This stays a deploy-time read.
   - No key provisioning or deploy happens until round 18's full-chain cell grades PASS at L9.
   - Provisioning and deploy then go under a NEVER-2 ledger entry with both never-widen halves.

## Round 18: ONE issuance, five cells, fan-out from two dependency chains

**R18-a: V3 edge render branch** (C-S200, the V3 half of C-S203, W16-S2).
- Keep the verified-origin marker in the render branch. Controls: marker missing and marker spoofed.
- Admit **GET only** on the three API paths, with a POST control.
- Derive the asset allowlist from the **pinned portal build manifest**.
  - Build the portal at the pinned revision and read its manifest; do not use the local dist.
  - Test those exact paths, plus unrelated-URI negatives.
  - No blanket extension allow.

**R18-b: claim shape and lifetime at both verifiers, plus audit** (C-S201, C-S210).
- Reject the four forbidden claim values at V2 as well as V3.
- Require `exp` at both V2 and V3, with a bounded lifetime of 5 min or less plus at most 60 s of skew.
- Controls: missing `exp`, oversized `exp`, both skew boundaries, and each poisoned claim, each alongside a valid control.
- Log `jti` and render id on accept and refuse at both verifiers. Never log the token or the key.
- The existing human aud/iss path is NOT touched; that remains the standing gap on its own change.

**R18-c: enforcer** (W15-S5, the served-vocabulary half of C-S203).
- Bind the allowlist to the actual served operation names in `routes.json` and `served.py` `key_operation`. Controls: the 3 real operations, plus a fourth-operation denial.
- Build the item-8 adapter:
  - resolve the delegator's CURRENT identity and grant, never reading a delegator header as the subject;
  - load by tenant + bundle + revision, and verify the returned identity;
  - intersect with the exact pinned object ids;
  - carry the class and bundle revision into cache and idempotency keys.
- Controls:
  - a subject that differs from the advisor id;
  - a wrong bundle;
  - a revoked delegator;
  - a cache-key separation check.

**R18-d: citations and baselines** (W15-S1/S2, W16-S1/S3).
- Re-pin the existing and render-header citations to ONE merged edge vintage.
- Run the unchanged scope suite, the worker wrapper and ruling 1's baseline plus the V1 harness, all against the merged tree.
- Report isolated evidence and merged evidence separately.

**R18-e: the actual-module offline chain, depending on R18-a, b and c.**
- One offline run, with no claim-shaped stand-ins: actual minter -> actual V3 -> actual V2 -> real resolver -> real enforcer -> served adapter, across the three objects.
- Negative controls:
  - a forbidden claim;
  - an expired token;
  - a swapped path id;
  - a wrong bundle;
  - a fourth operation;
  - a missing origin marker.
- It walks the full v0.17 item-7 (a)-(k) table, except (g), which is a deploy-time read.
- **This cell is the only proof of the render contract.** The independent suites in a-d are its inputs, not proof of the contract.

**Order text (W15-S6):** every order's grant includes the paths the startup and session-marker instructions require.

## Carried, not cut

- **IRPT_FNTEND FE-s-88: the print-route branch.** It is in FNTEND round 14. IB-rti-6's latency re-cut follows BOTH that branch AND a PASS on R18-e.
- **Human capture is not the standing mechanism.** This is Andrew-direct @`29d157110d`.
- **Unchanged clocks:** W10-S2, S116/W1-S47, break-glass, and the 171 older OPEN remedies the CVO disclosed. None is recertified.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
