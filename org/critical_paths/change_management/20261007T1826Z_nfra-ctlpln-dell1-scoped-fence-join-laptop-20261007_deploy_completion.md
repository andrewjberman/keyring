# Deploy Completion Record
**Date opened:** 2026-10-07T18:26:09.644450+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN CT-d-2 as amended -- BOX: THE LAPTOP. ONE targeted safe-apply of THREE firm bucket policies (opal_data_49financial, lgic_firm[cottonwood], lgic_firm[inflection]) admitting cloudops-dell1-agent-user to each fence AND confining it in the SAME apply by three DenyScopedExemption1 statements per bucket, so the join is READ-ONLY and PREFIX-BOUND to that bucket's own irpt/<firm>/platinum/holdings/. Admission WITHOUT confinement would be whole-bucket read AND write on three firms' data, because dell1's identity policy allows get, put and list on the estate pattern. Both halves SIGNED: COO @ca90fc5303 (six conditions), CTO @f4643f1530 (plus condition 7). Plan measured 0 to add, 3 to change, 0 to destroy; 129 added lines, 0 removed.
**Authored by:** 0.7.0_AE_CloudOps~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | one targeted safe-apply of the three firm bucket policies at the laptop | the four fence inputs byte-identical at 17b61b4124 and HEAD (blob hashes, with a working control); both checks ok=True immediately before the plan; plan reads EXACTLY 0 to add / 3 to change / 0 to destroy on the three named addresses; per bucket 43 added lines classified to the one dell1 ARN plus exactly the three signed Sids with that bucket's OWN firm prefix and no other firm's token; 129 added / 0 removed in total; ZERO changed-value lines; no role resource; safe-apply completes 0 added 3 changed 0 destroyed |  | OPEN |
| V1 | verify | per bucket, the live document equals the saved one plus the planned additions | parsed comparison against the three PRIOR8_* documents (49financial sha256 a3edb171..., cottonwood e73fc892..., inflection a405f60f...) plus exactly the dell1 ARN and the three DenyScopedExemption1 statements; planted-mutant control through the same comparator; statement counts 4 -> 7, 4 -> 7 and 1 -> 4 |  | OPEN |
| V2 | verify | the ALLOWED arms per bucket, each with its matched statement | dell1 s3:GetObject UNDER irpt/<firm>/platinum/holdings/ allowed; s3:GetBucketLocation allowed; s3:ListBucket with the prefix supplied allowed -- in all three buckets, by the simulator against the LIVE policy with dell1's live attached policies as the identity side |  | OPEN |
| V3 | verify | the CONFINING arms per bucket -- each refusal attributed to a DenyScopedExemption1 statement BY NAME | dell1 s3:GetObject OUTSIDE the prefix, s3:PutObject UNDER the prefix, s3:ListBucket with NO prefix, and s3:GetObjectVersion under the prefix -- each explicitDeny, and each matched statement named so the refusal is attributed to the confinement and not to the fence. This is the leg that distinguishes a scoped read grant from whole-bucket read and write |  | OPEN |
| V4 | verify | the other-principal arms and the cross-project arm | dell2 s3:GetObject outside the prefix STILL allowed (unchanged by this act); one unlisted previously-refused principal STILL refused; and on cottonwood dell1 refused on the restricted prefix commonwealth/cottonwood/bronze/crm/, which proves another project's three statements applied earlier today still bind the newly admitted principal |  | OPEN |
| V5 | verify | AC1 + AC2 + AC3 and the census reported with its scope | check_dell_fence_join.py reads cross_firm_leaks=0 scoped_rows=3 scoped_confined=3/3 ok=True; check_fence_scoped_rows.py reads unchanged_today=True scoped_rendered=9/9 sim_ok=30/30 refusals_ok=7/7 ok=True; the re-plan of the three targets reads exit=0; and the live census dell1_admitted moving 21/24 -> 24/24 is reported with the words 'scoped, 3 of 24' per COO condition 5 |  | OPEN |

## Log

- 20261007T182609Z OPENED by 0.7.0_AE_CloudOps~E with 6 leg(s)

---

## BOX

**THE LAPTOP.** Executor `0.7.0_AE_CloudOps~E`, seated by `2.0.0_SA_COO~C` under
`NFRA_CTLPLN.TO-APPLY-8.dell1-scoped-fence-join-apply-laptop` @c6037a3f5e (GO msg 106487, acked). Applying identity
`arn:aws:iam::313476888478:user/Andrew_Berman`. Terraform v1.15.8 on PATH.

## WHAT MAKES THIS DIFFERENT FROM THE DELL2 JOINS, and why the confinement is the whole act

Under TO-APPLY-4 and TO-APPLY-5 this seat applied these same three resources to admit **dell2**, and admission was
the whole change. **Here admission alone would be a write grant.** `cloudops-dell1-agent-user`'s own identity policy
allows get, PUT and list on the estate's bucket pattern, and a principal admitted through a fence is outside that
fence's Deny. So plain admission would give dell1 **whole-bucket read AND write on three firms' data**.

What keeps it narrow is that the same apply adds, for that principal only and per bucket, three statements:

| Sid | what it refuses |
|---|---|
| `DenyScopedExemption1AnyOtherAction` | every action except the three named |
| `DenyScopedExemption1ObjectsOutsidePrefix` | any object read outside `irpt/<firm>/platinum/holdings/` |
| `DenyScopedExemption1ListingOutsidePrefix` | any listing whose prefix is not under that path (absent or empty included) |

The CTO half rests its signature on the ORDER the work landed in: the reader that refuses an unknown registry key
came first (@3b6c321227), the rows second (@d5516cb074), the checks third (@17b61b4124) -- so the state *"dell1
admitted to a whole bucket with its own put allowed"* **was never plannable**. That is why a plan admitting dell1
without the three statements is a STOP rather than a smaller version of the same act.

## BLAST RADIUS

Three S3 bucket policies. It changes what **one** principal may do in three buckets and nothing for any other
principal. No IAM object, no role, no other bucket of the 24, no object, no served output.

| bucket | prior | after |
|---|---|---|
| `opal-data-49financial` | 4 statements, fence admits 20 | 7 statements, fence admits 21 |
| `opal-data-cottonwood` | 4 statements, fence admits 6 | 7 statements, fence admits 7 |
| `opal-data-inflection` | 1 statement, fence admits 6 | 4 statements, fence admits 7 |

**What dell1 GAINS:** `s3:GetObject` under that bucket's own `irpt/<firm>/platinum/holdings/`, `s3:ListBucket` when
the request's prefix is under that path, and `s3:GetBucketLocation` -- in each of the three. Before this act dell1
was refused everything in all three (`dell1_admitted=21/24`, `gap_dell1=1`).

**Named so it is not read as covered:** `s3:GetObjectVersion` is REFUSED by ruling. After this act dell1 reads the
served holdings of **all three firms** -- that is the placement Andrew set (the securities layer on dell1,
classifying what every firm holds), read-only, one prefix per bucket. A fourth firm bucket is a new row and a new
half.

**THE CENSUS WILL READ 24/24 FOR dell1 AND THAT NUMBER IS MISLEADING ALONE.** The census counts ADMISSION, not
SCOPE. COO condition 5 and CTO point 2 require it always be reported with the words **"scoped, 3 of 24"**. A cell to
make the census print scope beside admission is on NFRA_CTLPLN's list; until then nobody quotes that count alone.

## ROLLBACK PER BUCKET -- independent

S3 keeps **no prior version** of a bucket policy, so the three saved documents ARE the rollback:

| bucket | saved document | sha256 | bytes |
|---|---|---|---|
| `opal-data-49financial` | `deliverables/PRIOR8_bucket_policy_opal-data-49financial_20261007.json` | `a3edb171b9ab187337af1aa30cd2560c6aca0b49ba8bc227974c92f227417766` | 2572 |
| `opal-data-cottonwood` | `deliverables/PRIOR8_bucket_policy_opal-data-cottonwood_20261007.json` | `e73fc8922b0f2f32dac33a9100dfe856d5167d1e40892dc9a6935ed805ab03b4` | 1772 |
| `opal-data-inflection` | `deliverables/PRIOR8_bucket_policy_opal-data-inflection_20261007.json` | `a405f60f5f7622ec50abe9d2352179964d1dd18ea036df8ba8d2a5e13624f866` | 560 |

Per bucket, independently: `4.0.0_SA_CRO` removes that bucket's scoped row and the same targeted apply runs for that
bucket; **or**, same window, `s3api put-bucket-policy --policy file://<the saved document>`, whose bytes are the
exact string S3 returned.

**TRIGGERS, and one of them is sharper than usual --- CTO condition 7:** if dell1's exercised read shows **a put
succeeding, or a get outside the prefix succeeding**, in any of the three buckets, that bucket's saved policy goes
back **in the same window** and `1.0.0_SA_CTO` is told. That branch is a write grant on a firm's data and is not left
standing while it is investigated. Also triggering: AC1/AC2 failing, an AC3 regression, or any live document ceasing
to equal saved-plus-additions.

## PRE-APPLY EVIDENCE IN HAND

- **THE FOUR FENCE INPUTS ARE UNCHANGED SINCE SIGNING.** `s3-49financial.tf` `ae957bccea05`,
  `s3-lgic-firm-buckets.tf` `b65e1ef4cd61`, `modules/opal_name/main.tf` `ff1859d31c6f`, `exemptions.json`
  `4b391ffd96c0` -- each blob EQUAL at `17b61b4124` and HEAD, and the working tree clean. Proven POSITIVELY by blob
  hash, because the order's `git diff` form is uncontrolled here: `17b61b4124` is a TRUNK PIN that did not itself
  touch these files, so its diff is trivially empty. **A working control was found instead:** the same four-file
  pathspec across `d5516cb074^..HEAD` prints 36 insertions, so the instrument discriminates and the empty gate is a
  real absence.
- **BOTH CHECKS, run 18:07:43Z immediately before the plan:**
  `FENCE-JOIN pairs=3 rows=3/3 typed_in_tf=0 cross_firm_leaks=0 evaluator_allowed=3/3 negative_arm=denied
  other_rows_changed=0 validator=ok scoped_rows=3 scoped_confined=3/3 ok=True`; and
  `FENCE-SCOPED rows_today=32 unchanged_today=True scoped_rendered=9/9 sim_ok=30/30 refusals_ok=7/7
  unknown_key_refused_by=validator+module ok=True`. The `scoped_confined=3/3` is the check's own statement that each
  scoped row carries its confinement.
- **CENSUS BEFORE:** `dell1_admitted=21/24 gap_dell1=1`, matching the half's expectation exactly;
  dell1 evaluator decisions `explicitDeny 3 / allowed 21`.
- **THE THREE PRIOR DOCUMENTS** saved with SHA-256 above; in each, **dell1 absent from the fence** and **zero
  `DenyScopedExemption1*` statements** before the act.
- **THE PLAN, classified per bucket rather than skimmed** -- `Plan: 0 to add, 3 to change, 0 to destroy`; 3 resource
  blocks; **129 added lines and 0 removed in total**, matching the COO half's own measurement; and per bucket: 43
  added lines, exactly the three signed Sids, the dell1 ARN on 4 added lines, and **one holdings prefix naming that
  bucket's OWN firm with no other firm's token present** (`cottonwood` -> cottonwood, `inflection` -> inflection,
  `49financial` -> 49financial). **ZERO changed-value lines** (`~ ... -> ...`): every `~` in the plan is a container
  marker showing the nesting path down to an addition, so no existing statement's value is replaced.
- **ANOTHER PROJECT'S WORK IS UNTOUCHED:** the cottonwood policy's three `DenyRestricted*` statements, applied by
  this seat earlier today under TO-APPLY-5, appear on **0** added or removed lines.
- **NO ROLE.** The plan's two `aws_iam_role` occurrences are `data.aws_iam_role.irpt_performance_adapter`
  **data-source reads** (`Reading...` / `Read complete`) -- how Terraform looks up the existing adapter role's ARN
  for the 49financial fence. Neither is a resource block and neither is on a changed line. Checked, not assumed.
- The three targeted argv strings were ECHOED BACK before use and arrive intact through MSYS, brackets and quotes
  preserved.

## INSTRUMENT NOTES carried into the verify legs

The decisive leg is V3, and it needs more than a refusal: on these buckets `DenyForeignFirmPrincipals` and the three
new statements can refuse the same principal for different reasons, so **each refusal must be attributed to a
`DenyScopedExemption1...` statement BY NAME** or it does not distinguish a scoped grant from the fence still
refusing. Every list arm supplies an `s3:prefix` CONTEXT ENTRY, because the listing statements are conditioned on it
and an unevaluated condition returns `implicitDeny` byte-identical to a real deny. One resource ARN per call. An
`allowed` is read as "the policy admits an ARN of that shape", never as proof an object exists.

## NOT EXERCISED, and the limits of this evidence

**This seat reads NO object and lists NO firm bucket.** The simulator's `s3:prefix` value is SUPPLIED, not taken
from a real list request, and organization policies are not evaluated -- both named by the COO half as what its
evidence is not. The exercised read is dell1's own, from dell1, by another route, and is owed after this apply (one
get under the prefix, one get outside refused, one put refused). **Until it runs the join is APPLIED, NOT
EXERCISED.**
