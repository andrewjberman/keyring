# NEVER-WIDEN SIGN-OFF -- **CTO HALF** -- `IRPT_BCKEND.TO-IB-rtf-5`: the two LGIC firm buckets unlocked, re-applied and fenced

**Signed by:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~05:2xZ.
**Pairs with:** the COO half @`ad45bd9691`. **This is step 5** of the remedy at @`9eeb9a70a8` / @`80dada6d8d`;
`IB-rte-3`'s re-hand. **Step 4 (the account root's `delete-bucket-policy`) has NOT landed and is not signed here.**

## BOUND TO CONTENT -- ALL FIVE INPUTS RESOLVED ON THIS SEAT'S OWN INSTRUMENT

| input | blob at HEAD | matches COO half |
|---|---|---|
| `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` | `9ccbe87c01` | yes |
| `infra/logic/registry/scopes.json` | `daa145d6a7` | yes |
| `infra/logic/registry/exemptions.json` | `db823b3d9f` | yes |
| `infra/aws/terraform/modules/opal_name/generated_locals.tf` | `494ac9aa39` | yes |
| `.tools/ds-precommit-check.py` | `38e316c99e` | yes |

⚠ **ONE PATH CORRECTION, SUBSTANCE UNAFFECTED:** `generated_locals.tf` lives at
`infra/aws/terraform/modules/opal_name/`, **not** under `shared-infra/`. My first resolution used the wrong
directory and returned `fatal: path does not exist in HEAD` -- **a wrong-object read, caught because a fatal is
loud.** The blob at the real path is `494ac9aa39` and matches. **The fifth input is NOT a Terraform input** (it is
the commit-time fence); it is bound because my round-5 analysis named the fence generator's output as a thing the
flip already moved.

⛔ **A PLAN READ FROM DIFFERENT BYTES FOR ANY OF THE FIRST FOUR IS NOT WHAT THIS HALF SIGNS.**

## 1. THE COO HALF'S KEYS AND BRANCHES ARE ACCEPTED AS WRITTEN

`K1`-`K7` with blast radius and rollback per key; the three branches (applies / STOPS / **applies-and-the-operator-
is-still-denied**); and the writers counted and PRINTED -- **2 / 1 / 1**, with *both* writers of the policy read:
the root's rule is the declaration at `blob 9ccbe87c01`, the console's rule is **"delete" -- it can only remove,
never author**, so the two cannot write conflicting documents.

⭐ **THREE THINGS EARN THE ACCEPTANCE:** it does **not predict the plan's counts** (arm (b) prints them and a plan
outside the bound is a STOP); it names the **operator-still-denied** branch explicitly *"so it is not discovered by
surprise"*; and it states that the `rte-3`-era policy **is not a rollback target because it IS the lockout** --
which is the distinction that would otherwise get one seat to "roll back" into the incident.

## 2. ⛔ THE CONDITION THIS HALF ADDS: **MEASURE THE APPLYING IDENTITY'S ARN AGAINST THE EXEMPTION SET BEFORE THE APPLY**

The exemption rows I drafted name **three IAM USERS**: `arn:aws:iam::313476888478:user/{Andrew_Berman,
Andrew_Berman_Console, Opal_Terminal}`. The new policy denies `s3:*` to every principal outside that set plus the
firm's own role pattern.

⛔ **NOTHING IN EITHER HALF MEASURES THAT `safe-apply`'s RUNTIME IDENTITY IS ONE OF THOSE THREE.** If the apply runs
under an assumed ROLE, or under any user not in the set, then the moment `K1`/`K2` create the policy **the applying
identity is denied on its own next read** -- and that is **`W3-S43` REPRODUCED EXACTLY**, by an act whose whole
purpose is to end `W3-S43`.

⚠ **The COO half names that outcome as a BRANCH to be discovered after the fact. It is cheaply refusable BEFORE.**

**SO, BINDING: arm (b) prints `sts get-caller-identity`'s ARN and asserts it is one of the three exempted ARNs.
A non-match is a STOP, not a branch.** ⭐ **COST: one call, in the arm that already runs.** **NON-APPLICATION:** an
apply whose identity is itself one of the resources being created, which this is not.

⚠ **AND THE ROOT IS NOT IN THE EXEMPTION SET, DELIBERATELY** -- the rollback path (`delete-bucket-policy` by the
account root) does not depend on an exemption, because the bucket owner's root can remove a policy that denies it.
**That asymmetry is the reason the rollback survives its own fence, and it is worth stating so nobody "fixes" the
exemption list by adding root.**

## 3. ⚠ THE SECOND CONDITION: **"0 KEYS" IS LOAD-BEARING AND PERISHABLE**

`K3`/`K4`'s rollback reasoning rests on *"no object exists to be versioned (`0` keys)"*, and the delete-then-create
window in `K1`/`K2` leaves each bucket **carrying NO policy for the duration**. ⭐ **Both are harmless ONLY while the
buckets are empty** -- an unfenced window over an empty bucket exposes nothing; over a bucket holding one object it
is a different act entirely.

**The buckets are empty today and nothing can write them (every identity reads `AccessDenied`), so the risk is
small -- but the fact is a MEASUREMENT AT SIGNING, and this act happens later, after a human step.**
⛔ **SO: the `0` keys is re-measured in arm (b) AT APPLY TIME, not carried from this signature.** Non-zero is not
automatically a STOP -- it is a fact that changes what the unfenced window means, and it goes to the halves before
the apply proceeds.

## 4. ORDERING, AND THE HUMAN HALF OF IT

The halves require **step 4 BEFORE the apply**, and the COO half is right that this is what stops the console writer
acting on the replaced policy after the fact. ⚠ **The ordering is enforced on the machine side only** -- arm (b)
measures `get-bucket-policy` at hand-off. ⛔ **A root `delete-bucket-policy` run AFTER the apply would strip the new
fence, and no arm can prevent that.** It is named here so that if the buckets ever read unfenced again, the first
question is *when did root last act*, not *did the apply fail*.

## 5. WHAT THIS HALF DOES NOT SIGN

- ⛔ **Step 4 itself.** The account root's act is Andrew's and is signed by nobody here.
- Any **object write** to either bucket; any reader/writer/runner/env change; any legacy prefix; **any resource
  outside the `lgic_firm` family**.
- **Starting host `i-02448edb624a7a7cf`** -- ruled at @`84225daff6`; `R62-AC3` is graded on its own vocabulary and is
  not this act.
- ⚠ **`W3-S47` (the `terraform fmt -check` rc=3) is NOT covered and NOT a blocker on this act:** it is PRE-EXISTING
  at the worktree-cut blob, the generator's HCL renderer has never produced fmt-canonical alignment at any registry
  state, `validate` is clean and the plan is byte-identical. It is a `lib/opal_naming.py` edit, **mine as the
  generator's owner**, and it is carried, not ridden on this sign-off.

---

## VERDICT

**CTO HALF: SIGNED**, bound by content to the five blobs above, subject to s.2 (the applying-identity assertion, a
STOP on non-match) and s.3 (the `0`-keys re-measure at apply time), and the s.5 exclusions.

With the COO half @`ad45bd9691`, **both halves required by CLAUDE.md's never-widen line are on file for
`IB-rtf-5`** -- and **the only remaining gate is Andrew's step 4.**

---

## ADDENDUM 1 -- 2026-09-19 ~06:5xZ: **ANDREW'S ~06:3xZ WORD DOES NOT LIFT s.4's ORDERING, AND THE REASON IS MECHANICAL RATHER THAN DEFERENTIAL**

**Relayed by `2.0.0_SA_COO~B` (msg `98154`), recorded at that seat. VERBATIM:** *"i cant get to the console right
now, i am remote. have an AE deal with it. if they cant for whateve rreason, proceed and note it for later."*
**No ruling was asked of this seat. This addendum is written anyway**, because a later reader holding his word
beside s.4 of this half has a contradiction to resolve alone, and resolving it wrongly authorises an unsigned act.

### THE READING

⛔ **"PROCEED" CANNOT MEAN "APPLY WITHOUT STEP 4", BECAUSE THE APPLY CANNOT RUN WITHOUT STEP 4.** The policy
attached today is the `W3-S43` lockout -- the fence document written with an **EMPTY exemption list** -- and it
denies `s3:*` to every principal. The account's own **ROOT** is the only identity that can remove a bucket policy
that denies the account, and root is **deliberately not** in the exemption set (s.2 of this half says so and gives
the reason). So until root acts, every applying identity is denied on its first read. **There is no branch in
which the apply proceeds and something different happens; there is only a branch in which it fails louder.**

**Therefore his word is read as: the ROUND proceeds, step 4 is PARKED with an owner and an un-park condition.**
That is exactly how `2.0.0_SA_COO~B` executed it -- `IB-rtf-7` cut to the AE lane, every profile tried with
`sts get-caller-identity` printed per attempt, `AccessDenied` recorded truthfully, `IB-rtf-5` left STAGED, and the
item carried on the drain-end packet and slug as parked rather than as a defect. ⭐ **THAT EXECUTION IS CORRECT AND
THIS ADDENDUM RATIFIES IT WITHOUT WIDENING IT.** Nothing in his word authorises starting the stopped host,
changing IAM, adding root to an exemption list, or routing around the fence -- and `2.0.0_SA_COO~B` said so first.

### ⚠ THE PART THAT OUTLIVES THE MEASUREMENT, AND IS THE REASON THIS ADDENDUM EXISTS

⛔ **HIS WORDS ARE SAFE TODAY ONLY BECAUSE OF A MEASUREMENT, AND THE MEASUREMENT IS PERISHABLE.** "Proceed" is
harmless while the apply is *impossible*. **The moment any identity CAN remove that policy -- root acting, an
exemption list edited, a profile turning out to be exempt -- THE SAME SEVEN WORDS WOULD READ AS AUTHORISING AN
APPLY THAT NEITHER NEVER-WIDEN HALF SIGNED.** An instruction whose safety rests on a fact nobody re-checks is an
instruction that changes meaning silently.

**BINDING, AND IT COSTS NOTHING BECAUSE ARM (b) ALREADY RUNS BOTH READS:** his word is NOT a substitute for step 4
and NOT an amendment to this half. **The apply proceeds only when `get-bucket-policy` shows the lockout gone AND
arm (b)'s identity assertion passes** -- s.2 and s.3 stand unmodified. **If step 4 is ever satisfied by some route
other than Andrew at the console, that route is a NEW REACHABLE STATE and returns to BOTH halves before the apply,
not after.**

### ⚠ AND A TRAP FOR ANYONE ANSWERING *"WHO CAN DO STEP 4?"* FROM THE REPO

`infra/logic/registry/exemptions.json` at HEAD lists **three IAM users** -- `Andrew_Berman`,
`Andrew_Berman_Console`, `Opal_Terminal` (root absent; verified at HEAD this tick). ⛔ **THOSE ARE THE EXEMPTIONS
OF THE POLICY THE APPLY WILL CREATE. THEY ARE NOT THE EXEMPTIONS OF THE POLICY ATTACHED RIGHT NOW.** A reader who
opens the registry to find out who can remove today's fence reads **DESIRED state and concludes three identities
can act, when the APPLIED state is the empty-list lockout and none of them can.** ⭐ **Rule 22's STATE axis at its
sharpest: the registry is not wrong, it is answering a different question than the one asked.** The only measured
fact about the applied plane is `2.0.0_SA_COO~B`'s `AccessDenied` on every identity tried -- **read from that
seat's measurement, not re-derived here**, and consistent with the lockout's predicted behaviour.

### TERMINOLOGY, ON ANDREW'S OWN CORRECTION

His first message ~06:3xZ asked why the buckets were being deleted. **They are not; the POLICY is.** Every seat
naming this act to him says **"remove the bucket's access policy"**, never the bare AWS verb. ⭐ **A tool's verb
leaked into a human sentence and read as destruction of the thing it protects** -- the buckets stay exactly as
approved @`af794c77e3`, and this act re-attaches the correct fence.

**s.1, s.2, s.3 and s.5 of this half are UNCHANGED. The five input blobs are unchanged. Step 4 remains the only
gate, now with an AE attempt recorded as tried-and-failed rather than untried.**
