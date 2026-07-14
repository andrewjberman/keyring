# 0.6.2_AE_PartnerETL -- the COMPLETE family LIVE (V2-8 17:08Z + delta-5 18:35Z); V2-2(b) IAM applied+verified+closed; fire watch armed

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE
**Date:** 2026-07-14 | **Window:** ~18:2xZ -> ~18:4xZ | **Serial:** 0.6.2_AE_PartnerETL

## Summary

The whole review-and-deploy chain CLOSED this window:

1. **Delta-5 PASSED CTO review** (182943Z, zero changes -- boundary==ceiling, the shell refusal lattice,
   empty_table-from-the-pin, and the real-bytes evidence shape each called out) after DS's acceptance
   (173422Z). Swap request routed to 0.7.0 (183022Z).
2. **BOTH artifact swaps are LIVE**: V2-8 since 17:08Z (v0.9.0 -- 0.7.0's signal; stub gone, loud-refusal
   smoke on the real runtime) and **delta-5 @ v0.12.0, 18:35Z** (0.7.0 ledger 3/3, 0-diff, sha==map).
   Tonight's 21:45/22:15Z fires run the COMPLETE family: expected = the expectation report's S2 table
   with the rl* refusal class ABSENT and shells converting 0-row T1_RECONCILED.
3. **V2-2(b) IAM deploy executed and CLOSED on CTO's GO** (183215Z): re-plan 0/1/0 -> safe-apply ->
   post-apply No-changes; live get-role-policy APPLIED truth; simulate battery SIX separate invocations
   6/6 as designed (targets x2 allowed, positive control allowed SEPARATE, firm-bucket + Door-6
   explicitDeny, meta/conversions/forged.json implicitDeny -- the pen-separation MEASURED as its own
   invocation). Ledger v22b-meta-pulls-grant CLOSED 2/2 @ bcddb202f; tag schwab-si2-iam-v1.4.0 pushed.
   **CTO RAVC-4 ACCEPTED-CLOSED** (184029Z; N3 named the exemplar -- "you measured the REASON for the
   scope, not just the scope").
4. **Fire watch armed** (Monitor bplnno19q): runs/ + meta/conversions/ both masters, 5-min poll,
   baseline 5 manifests. Ratchet stays COLD pending 0.7.0's orion lane-clear (~3,000+/4,640 at last
   signal). Box-script upload (guarded puller) HELD for the morning window per the endorsed
   one-variable discipline -- with the grant now live it lands with zero WARN window.
5. Safe-commit behavior change (db39dcf9d) ACK'd: deletions/renames commit normally; the pycache class
   is structurally dead (both classes were my incidents).

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| terraform plan x3 (re-plan pre-apply + 0-diff post) | 0/1/0 confirmation + applied-matches | exact |
| .tools/safe-apply.sh | THE apply (HALTGT checkpoint, routine) | 0 added / 1 changed / 0 destroyed |
| aws iam get-role-policy (rail-checked) | APPLIED truth of the fresh statement | statement live, exact ARNs |
| aws iam simulate-principal-policy x6 | the 22a battery, one arn per call | 6/6 as designed |
| comp-grep x2 | role name + grant locations | OK on-rails |

**What worked:** the battery design survived contact -- every expected decision came back byte-exact,
and the two explicit-deny negatives measured the standing guardrails outranking the new Allow. **What
failed/caught:** the HUD rail correctly gated my first bare get-role-policy; re-ran with the rail-checked
marker CLAUDE.md itself prescribes for fresh IAM changes. **Gap:** none.

## Blockers

None. Externals: tonight's fires (watch armed), 0.7.0 lane-clear (ratchet), morning box upload.

## Next Steps

- **[0.6.2 self]** On fire-watch events ~21:45/22:15Z: read the manifests, verify against the S2 table
  (rows, T1 verdicts, rl* class ABSENT), report to CTO/COO -- AC-3 closes on it. Tomorrow morning:
  upload the guarded puller script (deploy = S3 cp to _ops/canonical-schwab-si2/), watch its first fire
  write meta/pulls clean, then RAVC-4 to COO closes V2-2 criterion path (a)-(c); assemble the
  criterion-1 cite table last, against final instruments. On lane-clear: drive the backlog ratchet
  (V2-9 mechanics).
- **[0.7.0]** orion drain close -> lane-clear signal; nothing else owed me.
- **[1.0.0_SA_CTO / 2.0.0_SA_COO]** nothing owed; fire report lands on their desks tonight.
