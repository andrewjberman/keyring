# Three more applies, and both of the session's stops turned into signed work -- 0.7.0_AE_CloudOps~E

**archetype:** DEPLOY

**Date:** 2026-10-07
**Task Orders:** `NFRA_CTLPLN.TO-APPLY-6` @aa7da845bb, `TO-APPLY-5` @ce2f42661d + AMENDMENT 1 @cbe30ace42,
`TO-APPLY-7` @3fd57f4133 (all GOs acked)
**Status:** ALL THREE COMPLETE
**Workspace CLOUD commits:** `3e9fdb455a` -> `3ebf741843` (TO-APPLY-6); `1dea8357e8` -> `7a5f1c5f66` (TO-APPLY-5);
`a8e3498eaf` -> `2f43f492d1` (TO-APPLY-7)
**Push state:** `7a5f1c5f66` and `3ebf741843` ON ORIGIN; `a8e3498eaf` and `2f43f492d1` LOCAL. Origin CLOUD read
`94ad9fa086` by `git ls-remote`. `CLOUD` is pushed only by `0.0.0_AB_MSTR` on Andrew's word.

---

## What this log covers

The delta since `session_ctlpln_apply5_step0_1143-1156Z.md`, which recorded only TO-APPLY-5's **stop** at step 0.
Three applies landed since. Their full records are the ledger entries and the three genre-DEPLOY proof instances,
all committed and all **VALID rc=0**; this log carries the Compiler Tools section and the decisions, and does not
restate them.

| order | act | entry | proof |
|---|---|---|---|
| TO-APPLY-6 | 8 IAM objects created (3 Denies narrow the Dells, 1 grant widens dell2) | CLOSED 6/6 | VALID, 7/7 controls discriminate |
| TO-APPLY-5 | the cottonwood fence, 1 bucket policy, 2 projects in one update | CLOSED 5/5 | VALID, 9/9 controls discriminate |
| TO-APPLY-7 | `sqs:SetQueueAttributes` added to the Deny, 74 -> 75 | CLOSED 4/4 | VALID, 7/7 controls discriminate |

---

## The shape of the session, which is the part worth keeping

**Two of these five applies exist because this seat stopped instead of applying.**

1. Under **TO-APPLY-4** the plan gate caught a cross-project rider: the cottonwood policy also carried three
   unapplied `ADVI_COTBKF` statements from `8e58736597`, a commit whose own subject ends *"nothing applied"* and
   which was an ancestor of the very trunk the COO half cited. Both signed halves had bound on a plan shape nobody
   had ever measured. Applied nothing; reported.
2. **TO-APPLY-5** then stopped at step 0 because the rider's own project pair disagreed with **itself** about whether
   the break-glass role was in its scope -- its CTO half disclaimed what its COO half signed. Applied nothing;
   reported both that conflict and a second one the order had not named.

Neither was adjudicated here. Both were resolved by the parties who owned them -- `2.0.0_SA_COO~C2` amended its own
half to STATEMENTS ONLY @e297665fdb, citing this seat's step-0 record by path and hash -- and the work then landed
under halves that actually covered it. **`1.0.0_SA_CTO` and `2.0.0_SA_COO~C` both wrote the same sentence into their
amendments: "The stop was the half working."**

**And TO-APPLY-7 exists because of one arm beyond what an order asked for.** Under TO-APPLY-6 this seat added a third
resource-policy arm on its own initiative; `sqs:SetQueueAttributes` read ALLOWED. Rather than report a defect, the
policy was checked first: the action was absent from the Deny's 74, and that absence is an already-ruled class (rows
W4-S1, W4-S2, NFRA_CTLPLN-S6, bound by reading only). So it was reported as a CONFIRMATION and not re-filed -- with
one precision point, that the COO half's prose listed "a queue policy" among what a Dell is refused while
`SetQueueAttributes`, the call Terraform actually uses, was not denied. The issuer corrected that prose and cut
TO-APPLY-7, which closed the gap.

---

## Compiler Tools

| Tool | Where | Result | Note |
|------|-------|--------|------|
| `derive_reached_roles.py --check-fresh` | TO-APPLY-6 | PASS `fresh=True` | The perishable gate of that act: 175/175 roles, 0 verdict changes, **510 s**. Run read-only, unbounded, and deliberately ALONE -- no concurrent AWS reads, because the order warns it retries on throttling. |
| the roots' evaluator checks (6, then 3) | all three | PASS, every `ok=True` | `POLICY-SIM` moved `respol_ok=11/11 -> 13/13` across TO-APPLY-7; `SSM-DOCS` independently confirmed the halves' most consequential claim (`resident_free_text=2 resident_fixed=0`) rather than this seat inheriting it. |
| `check_restricted_prefix.py` | TO-APPLY-5 | PASS on its POLICY limb | Amendment 1(a)'s exact requirement. Its PLAN fields read `plan_add=2` from the check's OWN untargeted plan -- the role -- not from the targeted apply. Whole output recorded; the amendment reserves to others which limb matters, so it was not interpreted. |
| `dell_fence_census.py --live` | TO-APPLY-5 | PASS | `dell2_admitted=24/24`, `gap_dell2=0` -- the figure the whole three-fence sequence existed to produce. 24 of 24 read, denominator printed. |
| `terraform show -json` | TO-APPLY-6 | PASS and load-bearing | The ONLY source for the rendered form of the two module-built routes documents, which have no on-disk artifact. Without it, "the live documents equal the rendered ones" was unverifiable for half the policies. |
| `comp-find` | TO-APPLY-7 | PASS, and instructive | First run proved no relay record existed (10 hits, denominator 14339) -- which is why this seat asked rather than assumed. Second run returned a **MEASURED ZERO over 481 files while the record existed**, because the record writes the English and not the API name. See the trap below. |
| `comp-iam` | all three | SKIPPED WITH REASON | Each order's preflight routes it to the cell's own evaluator arms, re-run before each plan and repeated against the LIVE attached policies at read-back. It models `(action)` not `(action, resource)`, is the DESIRED plane, and exposes no bucket-policy document at all. Running it would have produced a repo-wide report with nothing in any of these blast radii. |
| `deploy_ledger.py` | all three | PASS | 15 legs across three entries, each closed with proof; all three entries CLOSED, all sentinels removed. |

**What worked:** the plan gates, which are the whole story -- a shape rule caught a cross-project rider two signed
halves had missed, and a conflict read caught a pair contradicting itself. `proof-of-spec-check` earned its keep
twice, refusing an `introduces` claim pinned to a commit that did not introduce the token.

**What failed:** nothing returned a wrong answer. Two self-inflicted defects, both caught by measuring my own
output: a channel append that rewrote 798 CRLF endings (fixed at `a162b02c50`), and a bogus-hash control that read
exit 0 because `head -1` swallowed git's exit code (re-run without the pipe: 128).

**Gap found -- now five orders old and unchanged:** no comp-tool exposes an IAM managed policy's default version,
its version list, its document, an S3 **bucket-policy** document, or an IAM group/user attachment set. **Every
never-widen half in this project that binds on "the live document equals the repo/rendered bytes" has had to leave
the rail under an audited `# rail-checked:` marker.** Raised for the tool's owner across TO-APPLY-3, -4, -5, -6
and -7. A `comp-iam policy <name>` verb returning the live default version, the document and a repo-equality
verdict would put the whole class back on the rail.

**A search trap worth keeping:** `comp-find 'SetQueueAttributes' org/tier0_exec` returned a measured zero over 481
files **while the relay record proving condition 5 existed**, because the record correctly writes "a queue's policy
or its other attributes" rather than the API name. The FILENAME was the signal. A token census is not a census of
the claim -- and the tool's own caveat ("a MEASURED zero ... not a claim the term is absent from the estate", plus
12 unsearched binaries) is what stopped the zero being treated as the answer and a premature STOP being filed.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Took TO-APPLY-6 before TO-APPLY-5 when the issuer left sequencing to this seat | TO-APPLY-6's 510-second freshness read is a perishable gate that ages; TO-APPLY-5's restricted-prefix check must be taken immediately before its own apply regardless, so nothing was lost by deferring it. |
| Checked whether the integrator's trunk sync had invalidated an in-flight gate, twice | The sync landed DURING TO-APPLY-6's 510 s freshness read, and again mid-step in TO-APPLY-7. Both times the root and the census blob were verified untouched (`34f037a55e4f` at both HEADs) before the result was trusted. A gate verified against a HEAD that then moves is a gate verified against bytes that may not be the ones applied. |
| Did NOT sync the trunk myself to unblock TO-APPLY-5's precondition | It exited 1, and the finding was that the commit was ALREADY on `origin/CLOUD` -- so the blocker was a local sync, not the dell2 merge. Pulling 78 commits of other seats' work into the tree this seat would then apply from is an integrator act and would have carried this seat's own commits onto the trunk. Measured, reported, left to the integrator, who performed it. |
| Matched plan address sets programmatically rather than reading the tail | TO-APPLY-6's plan is 409 lines; eyeballing it is how a ninth address gets through. Extracted by regex and compared as a SET: 0 extra, 0 missing. Same discipline on TO-APPLY-5's 47 added lines, classified rather than skimmed. |
| Added a resource-policy arm no order asked for, then checked the policy before calling it anything | It read ALLOWED. Had it been reported as a defect it would have been wrong -- the action was absent by design and the absence is an owned, ruled class. Reported as a confirmation, nothing re-filed, and the one genuinely new thing (the half's prose overstating coverage) named separately. That is what produced TO-APPLY-7. |
| Supplied an `s3:prefix` context entry on every list arm | `DenyRestrictedListExceptReaders` is conditioned on both `aws:PrincipalArn` and `s3:prefix`. Without the context the conditioned statement returns `implicitDeny` byte-identical to a real deny, so a list arm run without it is worthless evidence in either direction. |
| Stated plainly where attribution was NOT available, instead of implying it | On the cottonwood fence `MatchedStatements` names `ResourcePolicy` but not the Sid, so Sid-level attribution came from the ARM DESIGN -- the same principal allowed outside the prefix and denied inside it. On TO-APPLY-7 the policy holds exactly one statement, which was CHECKED, so there naming the policy does name the Sid. The difference is recorded rather than smoothed. |
| Used two ADMIN identities as the sharpest discriminator | `Andrew_Berman` denied ON the restricted prefix while `Andrew_Berman_Console` is allowed -- both admins, so the `ArnNotLike` exception is the only difference, and it demonstrates an explicit resource-policy Deny overriding `AdministratorAccess`. |
| Reported `gap_dell1=1` as a divergence with proof it pre-existed, rather than quoting only the figures that matched | AMENDMENT 1's report clause expects 0. The pre-apply census **the halves themselves cite** already recorded `MDPF_SECCLASS` on dell1 citing that bucket. Quoting only the three matching figures would have been true and misleading. |
| Asked `0.0.0_AB_MSTR` once for condition 5 rather than stopping or proceeding | The order allows either reading the record or asking once, and makes an unshowable condition a STOP. No record existed when first searched. Asking was the sanctioned middle path; the record then arrived with both managers' acks BY MessageId. |
| Did not copy the CTO on the peer lane's fence finding | Rule 31 routes corroborations to the record, not an inbox. `0.7.0_AE_CloudOps~I` is carrying the ask; this seat gave it the denominator that sizes it and the one composition point only this seat could supply. See below. |

---

## The peer lane's fence finding, and what this seat's measurements do and do not establish

`0.7.0_AE_CloudOps~I` (msg 106347, acked) reports that `cloudops-dell-agent-deploy-policy`'s
`S3ObjectsOnOpalBuckets` allows `s3:GetObject` on `arn:aws:s3:::opal-*` with NO condition, so the fence does not
fence READS, and that `opal-data-cot` carries no Deny at all.

**That does not contradict anything reported here, and the two together are sharper than either alone:**

- **Where a fence EXISTS it DOES refuse reads.** This seat's committed arms: `cloudops-dell1-agent-user`
  `s3:GetObject` **explicitDeny on all three** of `opal-data-49financial`, `-inflection` and `-cottonwood`, each
  matched to the Resource Policy; the same for an unlisted role whose existence was separately proven. The mechanism
  works.
- **It exists on almost nothing.** The census this seat ran: `buckets=24 fenced=3 no_policy=11 no_fence=10`. **21 of
  24 carry no fence at all.** That denominator is the size of the peer's finding.
- **One composition point only this seat can supply, because these applies caused it:** dell2 is now
  `dell2_admitted=24/24`, `gap_dell2=0`, by design under four signed halves. Combined with an unconditioned
  `S3ObjectsOnOpalBuckets`, **dell2's read reach is now every `opal-data` bucket**, not only the three its placed
  projects need. The halves anticipated that dell2's own policies would apply once the fence stopped refusing; the
  peer's finding is what makes the width worth stating plainly.

A read-Deny is **not** adjudicated here; the peer has taken the ask to `1.0.0_SA_CTO` and now carries the
denominator with it.

---

## Blockers

**None.** Nothing is owed by this seat. All three `<status>` flips are the issuer's act.

---

## Current State

All five NFRA_CTLPLN applies this seat was handed are complete, proven and recorded: the Dell identity policy
(TO-APPLY-3), the two-bucket dell2 fence join (TO-APPLY-4), the cottonwood fence carrying two projects in one update
(TO-APPLY-5), eight IAM objects of Denies plus the dell2 command grant (TO-APPLY-6), and the queue-attribute Deny
(TO-APPLY-7). Five NEVER-2 entries CLOSED with 25 legs proven in total, five proof-of-spec instances **VALID rc=0**,
`deploy_ledger.py check` lists **0** `nfra-ctlpln` entries open, and no sentinel remains. dell2 now reaches all 24
`opal-data` buckets (`gap_dell2=0`); the Dells are refused resource-policy writes including queue attributes, the
routes to ten census-YES roles, and ten access-deciding Lambda functions; dell2 may send two free-text documents to
one host as `irpt-ycharts-runner-role`; and the Cottonwood CRM prefix is closed to every agent identity and to the
laptop's own user.

**Nothing in any of the five was EXERCISED by this seat and none is claimed.** No object was read in any firm bucket,
no command was sent to any host, no queue was created or changed, and no Dell identity was acted as. Every refusal
and every grant is proven at the policy plane against live or attached policies.

---

## Next Steps

1. **[`2.0.0_SA_COO~C`] Three `<status>` flips** -- TO-APPLY-5, -6 and -7. All proof instances are VALID rc=0 beside
   their orders.
2. **[`2.0.0_SA_COO~C`, OWED AND NAMED BY THE CTO HALF] The queue-policy root mapping.** Whether a Dell-placed
   project owns `globgrph`, `inf-pipeline`, `opal-gateway` or `partner-etl-ops-alerts`. Those four declare a separate
   `aws_sqs_queue_policy` resource and can no longer be applied from a Dell -- **on a CREATE as well as a change**.
   Until read, a Dell seat could meet a refused create and not know why. This is the item with live blast radius.
3. **[`1.0.0_SA_CTO`] The peer lane's read-Deny question**, now carrying the denominator: 21 of 24 buckets have no
   fence, and dell2's read reach is account-wide across `opal-data`.
4. **[`1.0.0_SA_CTO~DELL2` / `2.0.0_SA_COO~C2`] The break-glass role is still owed** and is the only thing between
   the restricted CRM prefix and its intended readers. Verified for them: the statements' derived ARN
   (`role/<builder name>`, no path) WILL match the role once created, so no statement change is needed.
5. **[the owner of `irpt-ycharts-runner-role`'s Terraform] CTO condition 7 binds you:** any later change to that role
   is a never-widen act that must name dell2's command route in its blast radius, because the grant is exactly as
   wide as the role and both granted documents take a free-text parameter.
6. **[a tool owner] The five-order rail gap** -- `comp-iam policy <name>` returning a live default version, document
   and repo-equality verdict.
7. **[`0.0.0_AB_MSTR`] Push CLOUD on Andrew's word** -- `a8e3498eaf` and `2f43f492d1` are LOCAL.
