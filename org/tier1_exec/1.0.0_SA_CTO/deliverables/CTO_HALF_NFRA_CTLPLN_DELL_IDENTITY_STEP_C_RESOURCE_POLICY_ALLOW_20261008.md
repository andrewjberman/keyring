# CTO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP C of three -- the Allow of 70 resource-policy actions

**Author:** `1.0.0_SA_CTO`, 2026-10-08 ~12:3xZ. **Counterpart read in full, all 117 lines:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_IDENTITY_STEP_C_RESOURCE_POLICY_ALLOW_20261008.md` @71f0dc910c.
**Not read by this seat:** the plan, the simulator's output, the list of 70 actions by name, any live resource policy.
**Authority:** Andrew-direct 2026-10-08 ~00:4xZ, "lets start with lifting 1 2 3 6"; item 3 as put to him: "Change who may reach
a resource: bucket policies, key policies, Lambda permissions, queue policies (an explicit deny of 75 actions)", with the note,
in the same answer, that lifting it reverses his own "laptop should admin". Record @14a030c049.

## What this half signs

The act the counterpart names: one `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/` with `-var apply_respol_allow=true`
on both the plan and the apply; `2 to add, 0 to change, 0 to destroy`; one Allow statement of 70 actions on any resource, and
its attachment to the Dell group.

## What it is, in one sentence

After this, an agent seat on either Dell can change who may reach almost any resource in the account: it can rewrite a
bucket's policy, share a key, let another principal call a function, or open a queue, wherever no explicit Deny stands.

## What this seat held out, and what it did not

Held out, each by this seat's ruling and each told to Andrew as an interim reading narrower than his words: every IAM action
(item 4, not lifted); a secret's own policy (it would undo the 28 withheld platform keys); the ten protected functions; the
audit-trail bucket and the audit trail; the four agentbus queues. All but the first two are explicit Denies live since step A.

NOT held out, because his words name them ("bucket policies, key policies"), and stated here so they are signed with open eyes.
A Dell can, after this step:
1. rewrite the policy of a firm's data bucket (49 Financial, Cottonwood, Inflection): the fence that keeps one firm's
   principals out of another's data;
2. rewrite or delete the policy of the Terraform state bucket, which every box's applies depend on;
3. rewrite any key's policy or grants;
4. widen itself on the transcripts key past the decrypt-only grant of 2026-10-07;
5. change object and bucket ACLs on the shared assets bucket.

## The one rule this seat adds, and why it is the laptop's to add

Each of those five is a resource more than one box depends on. A change to any of them is, in Andrew's own words of
2026-10-07 ~19:0xZ, "a deploy that could upset another device's work", which is the case he left with the laptop. So:
**a Dell that intends to change the policy, grants or ACLs of a firm data bucket, the state bucket, a key another box uses, or
the shared assets bucket tells the laptop BEFORE the act, by bus, naming the resource and the change, and acts when the laptop
has answered.** Every other resource-policy change is a Dell's own, under its own pair, reported after. This is a rule seats
read; no tool enforces it, and the seat gates do not grade a direct command-line call.

## Not examined, by either half

Organization-level policies; the account's public-access block (whether a public bucket policy would take effect at all); the
policies already on the five resources; whether a Dell job in flight changes behaviour once these calls stop being refused.

## Expected outcome, BOTH branches

As the counterpart's, A and B.

## Conditions

1. The counterpart's conditions 1 to 7 stand.
2. Condition 6 is not left as a note: until the variable's default is made true, ANY plan or apply of this root without the
   variable destroys the Allow. The cell that makes it durable is cut the same hour as the apply, and no other seat plans this
   root in between; the applier's report says so in its first line.
3. Both Dell CTOs are told the before-rule above, in those words, before a Dell seat's first resource-policy change.
4. The exercise is a Dell's own first use, reported. Until then: APPLIED, not EXERCISED.
5. Andrew is told the five routes in plain words in the same hour this is signed.

**SIGNED** -- `1.0.0_SA_CTO`
