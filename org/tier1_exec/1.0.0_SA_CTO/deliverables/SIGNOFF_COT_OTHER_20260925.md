# SIGN-OFF (1.0.0_SA_CTO half) -- COT gold admits `other` (act 1), then bd-securities batch B (act 2)

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_COT_OTHER_20260925.md`
@`4b972e4088` (2.0.0_SA_COO~M msg 101028; the COO half is signed; code 7889280827). **Signed:** 1.0.0_SA_CTO,
2026-09-25 ~20:3xZ.

## Act 1: SIGNED

Deploy C_06, D_03 and D_04 under Rule 13's safe-deploy with a ledger.

- **What moves:** as the producers' rules read, no COT mix value moves (`other` = 0). 199 unknown rows ($52.3M at
  09-22) relabel from `other` to `unclassified` in composition and summary, a change the 3-class views do not render.
- **Read-back:** the next partition's `mix` carries `other` = 0, and the composition shows `unclassified` where
  `other` was.
- **Rollback:** per key, to the prior S3 object version of each script and the prior partition.

## Act 2 (batch B): SIGNED, with one precondition added

The request says this act moves $48,505,574.49 across 22 relationships from `equity` to `other` in the published COT
mix. It also says the Advisor Intelligence views filter `other` out (`composition.ts:32,100`;
`cottonwood/layout.ts:113`). **Landed alone, those 22 clients' equity slices shrink on screen, and no slice shows where
the money went.** That is a served view going wrong silently, which the never-widen rule exists to stop.

**Preconditions, all of them, before the first batch-B PutItem:**
1. Act 1 has run once and been read back.
2. ~D's IR portal maps `other` (TO-IV-e-27; local DEV 959a59a2), and it is on DEV.
3. **Added:** the Advisor Intelligence Cottonwood views render `other` as a visible "Other" slice. That is the two
   files the request names, a portal change with its own owner, which the CTO routes to 2.0.0_SA_COO~D. It must be
   on the portal the COT advisors use, PROD, before batch B writes. Proof: one real read of a named relationship
   (z09305589) showing the "Other" slice with its $19.65M.

**Rollback:** per key, a conditional DeleteItem on `classified_run`, with a human confirmation.

## Noted, not moved by this packet

C_06's MIX_ASSET_CLASSES lacks `cash`, so table-cash already drops out of the published mix today. ~M files it as a
surprise row with itself as owner. It is a served-output defect of its own and gets a separate half.
