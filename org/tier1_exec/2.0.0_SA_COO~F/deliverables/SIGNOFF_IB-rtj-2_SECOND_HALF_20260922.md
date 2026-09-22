# NEVER-WIDEN SIGN-OFF -- IB-rtj-2, SECOND HALF -- signed by `2.0.0_SA_COO~F` IN `4.0.0_SA_CRO`'S STEAD

**Standing authority for the substitution:** Andrew-direct 2026-09-11 ~05:3xZ, verbatim: *"If CRO is not online, can
do COO in their stead."* Invoked here because Andrew reported at the `1.0.0_SA_CTO` terminal ~2026-09-22 01:3xZ that
`4.0.0_SA_CRO` is failing with 529 timeouts (down, not deaf). `1.0.0_SA_CTO` named this seat as the live COO lane
not holding the IRPT_BCKEND round, per the packet's own clause (msg 99357). This is a relayed instruction executed
under Andrew's own prior word, not an inference of scope: if the read below finds anything the packet does not
cover, it is named, not silently signed.

**Signing against:** packet blob `e2f521e5b55e236da0ae83f80254a10a1cbe84a8` (`git hash-object`, matches the CTO's
citation in msg 99357 exactly; committed at `a33a2ca4b71b23de817a39129d815e07fab877e3`), the two policies quoted in
it verbatim, and the role name `irpt-fence-probe-l4-role`.

**My own read, not a restatement of the CTO's or the packet author's:**
- `infra/aws/terraform/investor-reporting/l4-fence-probe/role.tf` read in full at HEAD `5b82db7a31`. The trust policy
  has exactly one principal (`user/Andrew_Berman`), `sts:AssumeRole` only. The inline policy grants exactly
  `s3:ListBucket`, no object action, no wildcard, on `local.probe_buckets` = the registry-derived fenced-firm list
  plus one hardcoded control bucket. A `precondition` refuses the plan if the registry selector yields a count other
  than 2, so a registry edit cannot silently widen this grant after the fact.
- `infra/logic/registry/scopes.json` read directly and evaluated by hand (not by trusting the packet's stated
  result): the selector `class == "FIRM" and bucket_managed_by == "s3-lgic-firm-buckets.tf"` yields exactly
  `["opal-data-inflection", "opal-data-cottonwood"]` today -- 2 buckets, matching both the packet and the
  precondition's expected count.
- The Terraform's rendered grant (role name, trust policy, both bucket ARNs plus the control bucket ARN, the
  precondition) matches the packet's Section 1 claims exactly; nothing in the `.tf` file exceeds what the packet
  describes.

## BLAST RADIUS -- both branches the producer's own rule can take, both covered

**Property named, writer count first.** The property this act touches is IAM role/policy existence for
`irpt-fence-probe-l4-role` in this one AWS account. Writers of that property within this act's own session: exactly
one, the Terraform apply/destroy pair in section 3 of the packet. No other producer in this project writes that
role name (checked: `role.tf` is the only Terraform resource block naming it, one writer).

- **What exists, and for how long:** one IAM role plus one inline policy, for the minutes between the packet's
  step 2 (apply) and step 7 (destroy, same session). Assumable only by `user/Andrew_Berman`, who already holds far
  broader access; no new principal or service gains anything. The grant itself is `ListBucket` only, on three named
  buckets, no object-level access.
- **BRANCH EXPECTED (the fence holds):** the positive control (control bucket) succeeds, both fenced buckets deny
  with the resource-based ("explicit deny") wording, the attribution control (an ungranted, unfenced bucket) denies
  with the identity-based ("no identity-based policy allows") wording. This discriminates the fence and closes leg
  L4 of the `IB-rte-3` deploy-completion ledger, owned by `2.0.0_SA_COO~B`. Covered: nothing served, no bucket
  policy, no exemption list, and no other principal is touched by this branch.
- **BRANCH THE FENCE LEAKS:** a fenced bucket lists successfully for this role. Both buckets hold 0 keys today
  (measured by the packet's own author, not re-derived by me here), so the exposure in that branch is an empty
  listing, never object contents. Covered: the role is destroyed the same way regardless of which branch fires (the
  packet's step 7 runs unconditionally on the sequence, not contingent on arms 4-6 passing); a leak is filed as a
  BLOCKING row, not silently absorbed, and nothing is re-tried or widened to compensate.
- **BRANCH THE POSITIVE ARM FAILS (instrument, assumption or grant broken):** the negative arms are not read as
  meaningful evidence in that case. Covered: destroy and verify still run, a row is filed, and the order stays open
  rather than being graded on an uninformative negative.
- **Rollback, either branch:** packet steps 7-9 -- a destroy plan that must show exactly the 2 deletions this
  create added, `.tools/safe-apply.sh apply` on that plan, then `aws iam get-role` must return `NoSuchEntity`
  (printed verbatim), then the `.tf` declarations themselves are deleted in the same session and committed, per the
  packet's own citation of `safe-apply.sh`'s tombstone note (an undeleted declaration would recreate the resource on
  the next apply). If the apply lands only the role and not the policy, the same destroy plan removes whatever
  state exists, and `get-role` is still the verification. **Rule 27 NEVER-2 applies and is named here explicitly:**
  nothing is left half-landed at session end; if the destroy step cannot complete in the same session, the ledger
  stays OPEN and is escalated, not left silent.

**Not covered by this act, confirmed against the packet's own Section 5:** any other principal, any bucket-policy
or exemption edit (this act reads the fence and never changes it), any grant surviving past this one session.

## SIGNATURE

Signed `2.0.0_SA_COO~F`, 2026-09-22, in `4.0.0_SA_CRO`'s stead, under Andrew's standing word quoted above. Blast
radius and rollback as stated. If `4.0.0_SA_CRO` recovers before this act executes, either signature suffices per
the packet's own terms; this one does not withdraw on that recovery.

Push state: LOCAL; `0.0.0_AB_MSTR` pushes.
