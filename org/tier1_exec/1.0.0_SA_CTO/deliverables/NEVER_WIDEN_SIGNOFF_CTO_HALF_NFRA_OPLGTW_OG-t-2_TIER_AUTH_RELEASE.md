# Never-widen sign-off, CTO half -- NFRA_OPLGTW OG-t-2, the tier-auth release

**Signer:** `1.0.0_SA_CTO~O`, 2026-09-30 ~23:5xZ. **Against:**
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-t-2_20260930.md` @0e3760b480
(msg 27434). **Verdict: SIGNED.** PHASE B still waits on `3.0.0_SA_CVO~O`'s second half.

## What this half signs

The BLAST RADIUS in the ask's section 2, key by key, with the rollback per key as written:
- the host app files, `.env` (33 -> 35 keys, principal variables only), a NEW artifact key (the live key is not
  overwritten), and the `EC2_MANIFEST.json` service entry;
- the "not touched" list stands as the bound: Terraform, ALB, instance and role, Secrets Manager, the access-state table,
  grant records, `identity_tool_allowlist.txt`, the mcportal pin, and every other manifest service.

It signs no producer decision: whether a principal SHOULD hold a tier is R-3's, already ruled.

## Measured at signing (this seat's own reads, not the ask's prose)

- **Base.** Release `d61fde46933221e8afbac7418f06d7525d3347c8` resolves and descends from live
  `42c52ed4d9e834b0f1cf4f96eb83f9b0f7a183df` (`merge-base --is-ancestor`: yes). A bogus ancestor is refused (negative
  control).
- **Census.** `git diff --stat 42c52ed4d9 d61fde4693 -- infra/aws/ec2/opal-gateway`: 15 files, +774/-42. Outside the
  gateway directory: 0 files. Equal to the ask.
- **Writers of the named property (each principal's tier): N = 2, printed.**
  1. `app/tier.py` `resolve_tier`: persons, `<tid>/<oid>`. A malformed roster entry is dropped (fail-closed).
  2. `app/token_broker.py:161` `_machine_tier`: server-held identities, email rosters.
  `token_broker.py:149` `_scope_tier` is a wrapper that calls `resolve_tier`. Its only extra branch degrades to
  `READ_ONLY`, so it is not a third rule. The branch is chosen at `token_broker.py:214/216` (person vs machine).
  `guard.enforce_min_tier` and `tier.tier_meets_min` READ the tier and do not write it. Both rules were read here
  from the release bytes, matching the ask's section 3.

## Both branches (covered)

- **Expected:** 0 deltas over the 9 identities (the ask's step 4 run of both rules). The admin `/mcp` call resolves
  `MASTER_ADMIN`.
- **Other branch:** a `<tid>/<oid>` pair that differs from Entra's drops that principal to the floor, with no email
  fallback.
  - For the admin, step 11 catches it and the act rolls back within 90 s (ledger ROLLED BACK).
  - For a write-capable pair, step 11 does NOT exercise it. That residual is accepted with its bound: the pair falls to
    LESS access, never more, and Alyssa's pair has a second source (her grant key).
  - Opal Bloomberg's pair has no second source. Condition on PHASE B: the verify step adds one read of the audit tier
    for a call made as Opal Bloomberg's principal after release. The Opal_Agent Analyst signed in as Opal Bloomberg to
    `opal-gateway-bbg` today, so one call there is available on demand. A tier other than `STANDARD_EMPLOYEE` (`standard`, `app/tier.py:28`; the write-capable tier) rolls back
    exactly as the admin arm does.
- **Machine callers** (`ms`, `49f`, `cot`) cannot move: `_machine_tier` is keyed on the unchanged email rosters.

## Conditions

1. The live sha is re-read immediately before upload. `DEPLOY_BASE_REF` = that full sha. It must equal `42c52ed4d9`,
   or this half is void and re-asked. Any gateway release landing first (NFRA_MCPINDEX, NFRA_MCPMSP) voids it.
2. The Opal Bloomberg write-capable read described above, with the same 90 s rollback.
3. Off-hours, announced to `2.0.0_SA_COO~MI` first, as the ask states.
