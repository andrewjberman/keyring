# dell1 is admitted to the three firm fences IN FULL -- the confinement this seat added nine hours ago, removed -- `0.7.0_AE_CloudOps~E`

**Date:** 2026-10-08
**Task Order:** NFRA_CTLPLN.TO-APPLY-10.dell1-full-fence-admission-apply-laptop (@351dd873af, GO msg 106728)
**Status:** COMPLETE
**archetype:** DEPLOY

**Preceding log:** `session_ctlpln_applies_8_9_1700-2115Z.md` (2026-10-07). **Issuer:** `2.0.0_SA_COO~C`.
**Box:** the laptop. **Risk:** WORLD. **Genre:** DEPLOY. Two signed never-widen halves, both read in full before acting.

---

## Objective

ONE targeted `safe-apply` of `infra/aws/terraform/shared-infra/` at exactly three bucket policies, removing the three
`DenyScopedExemption1*` statements from each so `cloudops-dell1-agent-user` is admitted to the 49 Financial, Cottonwood
and Inflection fences IN FULL, as `cloudops-dell2-agent-user` is. **This act removes the confinement this same seat
ADDED under TO-APPLY-8 about nine hours earlier.**

**The width, stated as both halves state it:** dell1's identity policy allows `s3:PutObject` on the estate bucket
pattern, so with the confinement gone dell1 can read **and write** any object in the three firm data buckets, not only
the holdings prefix it read before. Deletes stay denied by that identity policy. Andrew's word was phrased as a READ
limit; the act is wider, both halves say so, and this log says so.

## Deployment Sequence

| step | act | result |
|---|---|---|
| 0 | HEAD contains the merge the GO names | `756acb9c3c` contains `225390daf6` (`merge-base --is-ancestor`, positive read) |
| 0 | the three dell1 registry rows carry no `actions` and no `prefix` | 3 of 3, printed per row from `infra/logic/registry/exemptions.json` |
| 0 | the two fence `.tf` files and `modules/opal_name/main.tf` unmodified | clean; the only untracked path under the root is a pre-existing `.tf.proposed` |
| 1 | `check_dell_fence_join.py` | rc=0 `cross_firm_leaks=0 evaluator_allowed=6/6 negative_arm=denied ok=True` |
| 1 | `check_fence_scoped_rows.py` | rc=0 `scoped_rendered=9/9 sim_ok=31/31 refusals_ok=7/7 ok=True` |
| 2 | three LIVE policy documents saved with SHA-256 | 3599 B / 2793 B / 1581 B, 7 / 7 / 4 statements |
| 2 | live fence census BEFORE | `dell1_admitted=24/24 dell1_scoped=0 disagree=3 gap_dell1=1 ok=False` |
| 3 | targeted read-only plan | exit=2 `0 to add, 3 to change, 0 to destroy`; **126 removed / 0 added** |
| 4 | NEVER-2 entry opened with its sentinel | `a443beb622`, six legs |
| 5 | ONE `safe-apply`, same three targets | `Apply complete! Resources: 0 added, 3 changed, 0 destroyed` |
| 6 | read-back LIVE, 27 arms | V1 3/3 + mutant controls; V2 9/9; V3 3/3; V4 6/6 |
| 6 | re-plan (AC3) | `No changes.` exit=0 |
| 6 | live fence census AFTER (AC2) | `dell1_admitted=24/24 dell1_scoped=0 disagree=0 gap_dell1=0 ok=True` |
| 6 | entry CLOSED | all six legs proven |

**THE APPLIED TIME: `2026-10-08T05:17:17Z`** -- all three `PutBucketPolicy` calls in the SAME SECOND, read from
CloudTrail `lookup-events`, three events in the 05:10-05:25Z window. The wrapper's own window on the local clock was
05:15:07Z to 05:17:16Z, **one second before** the AWS-plane stamp; that is local-vs-AWS clock and the AWS plane is the
authority for the time the CTO passes to dell1. CloudTrail's `Username` reads the laptop's IAM identity
(`Andrew_Berman`), not a seat serial.

## Verification

- **V1, the document is what was signed and nothing more.** Per bucket the live document equals the saved pre-apply
  document MINUS exactly the three `DenyScopedExemption1` statements, by parsed comparison of the Statement list and
  every other key: 49financial `7 -> 4` (`ec0f269b...` -> `536f9bcb...`), cottonwood `7 -> 4` (`7d3a66f0...` ->
  `c8bcfff6...`), inflection `4 -> 1` (`4404d190...` -> `a14b7106...`). **A planted Sid rename on a surviving
  statement reads False through the same comparator in all three**, so the True is discriminating.
- **V2, the widening measured at its FULL width, 9/9.** `s3:GetObject` outside the old prefix, `s3:PutObject` outside
  the old prefix, and `s3:ListBucket` with NO prefix -- all `allowed` in all three buckets, each matching
  `cloudops-dell-agent-deploy-policy` on the identity side with no resource-policy deny left. **The PUT arm is the one
  that makes this wider than the read limit Andrew's words named**, and it is reported as a write reach.
- **V3, the cross-project arm, 3/3 -- the one that could have gone wrong.** On cottonwood dell1 is STILL
  `explicitDeny` on `commonwealth/cottonwood/bronze/crm/` for get, put and list, each attributed **by name**:
  `DenyRestrictedReadExceptReaders`, `DenyRestrictedWriteExceptBreakglass`, `DenyRestrictedListExceptReaders`
  respectively. ADVI_COTBKF's statements bind a principal admitted after them and then widened in full.
- **V4, the fence itself was not widened, 6/6.** dell2 unchanged (`allowed` in all three). The unlisted, previously
  refused `opal-gateway-role` still `explicitDeny` in all three, attributed to `DenyForeignFirmPrincipals`.
- **Attribution instrument:** LEAVE-ONE-OUT throughout -- drop each Sid, see which removal lifts the refusal. No
  offset arithmetic, which was measured wrong on TO-APPLY-8 and discarded there.

## Decisions Made

1. **The two checks were run THREE more times than the order asks, because step 2 breaks step 1.** See S24 below.
   The pre-plan pass is the one on the restored fixture, and it was re-exercised after the census to prove the
   bounds-clean form leaves it intact.
2. **The census's `--out` was redirected out of `tests/`.** The order's literal invocation edits a tracked test file,
   which its own bounds forbid. The redirect changes nothing the census measures. Stated in AC2's denominator, not
   silently.
3. **AC2's PASS is reported with the fields that actually MOVED**, because the two the expect names read the same
   before and after this act.
4. **The seat-gate `verdict=STOP` was read, not skimmed.** Under ENFORCE this apply would have been stopped; the basis
   is an overlap on a different file in the same root that this targeted apply never touched.

## Files Modified

- `org/critical_paths/change_management/20261008T0508Z_nfra-ctlpln-dell1-full-fence-admission-laptop-20261008_deploy_completion.md`
  (+ its sentinel, opened `a443beb622`, closed in this session's second commit)
- `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` -- two rows appended
- `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/` -- 14 evidence artifacts + the proof-of-spec instance
- **No `.tf`, module, registry or test file was edited.** Measured at the close: `git status --porcelain` on the two
  fence files, `modules/opal_name`, `infra/logic/registry` and `shared-infra/tests/` is empty but for one pre-existing
  untracked `.tf.proposed`.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `check_dell_fence_join.py` | AC1 | ok=True pre-plan and post-apply; ok=False in between, caused by this seat's own census run (S24) |
| `check_fence_scoped_rows.py` | step 1 | ok=True twice; carries the second unlisted-principal arm (C4 CONTROL inside `sim_ok=31/31`) |
| `dell_fence_census.py --live --out <deliverables>` | AC2 | BEFORE `disagree=3 ok=False`; AFTER `disagree=0 ok=True` |
| `iam:SimulatePrincipalPolicy` | 27 arms + leave-one-out sweeps | one action and one resource ARN per call; `s3:prefix` context entry supplied for the conditioned cottonwood listing arm |
| `comp-read` | `check_dell_fence_join.py --for "what exactly does the NEGATIVE arm strip and evaluate"` | **how S24 was found** -- it surfaced the fixture-as-base-document dependency |
| `comp-find` | `'DenyForeignFirmPrincipals' --name '*.tf' --files` | MEASURED ZERO over 1218 files: the fence Sid is never typed in Terraform, corroborating the check's `typed_in_tf=0` from a second instrument |
| `deploy_ledger.py` | open / close-leg x6 / close | entry CLOSED, sentinel removed |
| `proof-of-spec-check.py` | with AC1,AC2,AC3 and `--governing-order` | **VALID rc=0**, 8 of 8 controls discriminate, 0 violations |
| `comp-pipescript` / `comp-iam` | not run | **correctly not run**: no script deployed, no gold run, no `iam.tf` edit -- and `comp-iam` models `(action)` only, so it is structurally blind to a resource-policy change |

**What worked:** `comp-read`'s qualifier ledger pointed straight at the two arms whose base document is a fixture;
that is the whole of S24. `comp-find`'s measured zero over a printed denominator turned "the Sid is not typed in
Terraform" from the check's own self-report into a second, independent reading.
**What failed:** nothing in the tools. One instrument error of this seat's own: the leave-one-out sweep threw
`InvalidInput: ResourceNames are not in a valid ARN format: *` on inflection, because removing that policy's only
statement leaves an empty Statement list and the API's error names the resource rather than the cause. Fixed with a
neutral non-matching statement injected into the trimmed copy only; the traceback is kept beside the corrected run.
**Gap found:** an acceptance check (`check_dell_fence_join.py`) whose verdict depends on a tracked fixture being
STALE, where refreshing that fixture is a step of the same order. Filed as S24.

## Blockers

**None.** Nothing is owed by this seat on this order.

## Current State

**The grant is APPLIED, NOT EXERCISED, in those words.** This seat read no object, listed no firm bucket and made no
call against firm data. All three acceptance criteria PASS at their stated expects; the NEVER-2 entry is CLOSED with
six legs proven; the proof-of-spec instance is VALID; the re-plan is 0-diff. Two surprise rows are filed and neither
held the act:

- **`NFRA_CTLPLN-S23`** -- the order's parenthetical expected BEFORE census line (`dell1_admitted=21/24
  dell1_scoped=3 disagree=0 ok=True`) is stale against the registry the same order names: with the three dell1 rows
  already FULL rows `@173f98f24b`, the census read `24/24`, `scoped=0`, `disagree=3`, `gap_dell1=1`, `ok=False` before
  the apply. **So AC2's two printed fields do not discriminate this act** -- `disagree` 3 -> 0 and `gap_dell1` 1 -> 0
  are what moved. A later applier grading AC2 on its printed fields alone would read PASS on an apply that never
  landed.
- **`NFRA_CTLPLN-S24`** -- `dell_fence_census.py --live`, the invocation step 2 and AC2 both name, defaults `--out`
  to the TRACKED fixture `tests/dell_fence_census.json`. The bare form (a) edits a test file this order's bounds
  forbid and (b) flips step 1's join check from `ok=True` to `ok=False` (`evaluator_allowed` 6/6 -> 3/6, the NEGATIVE
  arm 0 -> 2 stripped), because that check reads the fixture as its base document. **Step 1, then step 2, then the
  plan cannot be run as written.** Measured, restored by `git checkout`, re-exercised.

**The seat-gate lines, reported because the order asks and because one of them matters:** APPLY-WHO
`verdict=ADMITTED`; `STOP: 3 hit(s) in OVERLAP -- first: OVERLAP: project NFRA_REPORT is placed on sitez ... and its
write set names infra/aws/terraform/shared-infra/infra-monitor.tf`; CROSSBOX-DEPLOY `device=laptop root=shared-infra
open_call=clear overlap=hit upset=clear open_deploy=clear verdict=STOP`; `WARN ... would stop under ENFORCE
( crossbox-deploy ); WARN mode proceeds.` **Under ENFORCE this apply would have been STOPPED** on an overlap naming
`infra-monitor.tf` -- a different file in this same root, which the plan never named and the apply never touched. Only
the first of the 3 OVERLAP hits is printed, so the other two are UNREAD here and are not claimed either way. Also
`open_deploy=clear` while THIS entry was open on the shared index, which is a reading about the gate, not the ledger.

## Next Steps

1. **[a Dell, by another route]** COO condition 7's exercise: dell1 reads 49 Financial's code prefix and lists the
   Cottonwood bucket. Until then: APPLIED, not EXERCISED.
2. **[`2.0.0_SA_COO~C`]** The `<status>` flip on TO-APPLY-10, and the dispositions of S23 and S24.
3. **[`2.0.0_SA_COO~C`]** S24's cheap fix before the next order quotes the same invocation: `--out` outside `tests/`
   in step 2 and AC2, or a `--no-save` flag on the census.
4. **[`1.0.0_SA_CTO`]** The applied time for dell1: `2026-10-08T05:17:17Z`.
5. **[whoever owns the seat gates]** CROSSBOX-DEPLOY would stop a correctly signed, correctly scoped apply under
   ENFORCE because another project's write set names a different file in the same root. Worth reading before the mode
   flips.
6. **[this seat]** Two GOs for TO-APPLY-11 arrived during this order (msg from `2.0.0_SA_COO~C` 05:36:10Z and from
   `2.0.0_SA_COO~R` 05:46:24Z, different subjects). Both read next.

## Pending answer owed

`1.0.0_SA_CTO` msg 106590 (acked 2026-10-08 ~04:5xZ) asks two read-only questions about 49 Financial's nightly gold
chain. Not answered in this session: the apply held the turn. It is this seat's next item after TO-APPLY-11's two GOs
are triaged.
