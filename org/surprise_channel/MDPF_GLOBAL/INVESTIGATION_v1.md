# MDPF_GLOBAL -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (CLAUDE.md Rule 2 / Rule 27).

**Round opened** 2026-09-12T11:31:51Z by `0.7.0_AE_CloudOps~C` while executing `MDPF_GLOBAL.TO-IAM1`
(issued by `1.0.0_SA_CTO` @`85f58dfd9c`, GO msg-id 96097). **This channel did not exist before this
commit** -- MDPF_GLOBAL had neither a tree channel under `org/missions/` nor a legacy flat one, and
CLAUDE.md Rule 2 names the flat path as a sanctioned carrier with lane ANY, so it is opened here
rather than leaving two findings inside one seat's deliverable where no other reader would meet them.

**The rows below were surfaced by the EXECUTING seat about ITS OWN ORDER**, which is the case Rule 2
contemplates ("the seat that sees it appends its own row"). None is a remediation row; remediation
stays `3.0.0_SA_CVO`'s.

⚠ **NO TALLY IS RECORDED IN THIS HEADER, AND THAT IS EARNED RATHER THAN INHERITED ADVICE** -- this
header said "both rows below" when there were two and was stale inside the hour when S3 and S4 landed,
then again when S5 did. The count, the class split and the ARMED-without-owner check are all DERIVED
from the block below by the protocol's extractor, which prints its own denominator. A hand-maintained
derived figure loses to the record it summarises.

**Round history, because the phases reached different outcomes and the ids alone do not say so:**
S1/S2 were surfaced when the order STOPPED pre-act on its own population tripwire and nothing was
applied. S3/S4 followed amendment 1, after the grant DID apply -- cleanly and 0-diff -- and was still
short of its goal for a reason no identity policy can reach. S5 answers the one READ the issuer then
asked, and closes the remaining engineering route by measurement rather than by attempt.

```json
[
  {
    "id": "MDPF_GLOBAL-S1",
    "project": "MDPF_GLOBAL",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~C",
    "surfaced_at": "2026-09-12T11:31:51Z",
    "one_line": "THREE DOCUMENTS, THREE DIFFERENT DENOMINATORS FOR ONE POPULATION, AND THE TASK ORDER'S NUMBER MATCHES NEITHER OF ITS OWN SOURCES. MDPF_GLOBAL.TO-IAM1 bounds its authorized act at 'the 8 prefixes the measurement names' (5 read + 3 destination) and states 'AccessDenied on 5 of 9 prefixes directory_runner.py reads'. Measured on the host by the host with a firing positive control, the live population is 10 source prefixes of which 8 are denied, plus 3 of 3 destinations denied -- 11 grants, not 8. The order's own pinned source says a THIRD number: row IRPT_BCKEND-S50 @6d7c132f43 records 'denominator 6 source prefixes + 3 destinations' with 4 denied. The battery summary that fed the order says '5 of the 9'. The 6-prefix sweep was CORRECT for the subset it probed and was never a measurement of the population: it probed dim_relationship alone for 49financial and never probed dim_account, dim_identity_crosswalk, dim_portfolio_group or bridge_group_account, all four of which directory_runner.py reads. The order ARMED the tripwire that caught this ('THE COUNT IS PERISHABLE ... stop and report rather than reconcile'), so this is a clean pre-act stop, not a post-apply discovery.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO -- re-cut MDPF_GLOBAL.TO-IAM1's BOUNDARY against the measured population (8 denied source prefixes + 3 denied destinations = 11 grants). The act cannot be taken inside the current ceiling of 8, and the order's own words forbid choosing the wider form without a re-cut. Nothing is applied and no rollback is owed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM command 7aee9ea9-2542-4819-a6e0-3873d793e20f on i-02448edb624a7a7cf, AWS-RunShellScript, read-only, Status Success rc=0 -- caller printed by the run: arn:aws:sts::313476888478:assumed-role/mdpf-daily-runner-ec2-role/i-02448edb624a7a7cf; TOTALS 'SOURCE: READ-OK=2 READ-DENY=8 READ-OTHER=0 denominator 10' and 'DESTINATION: READ-OK=0 READ-DENY=3 READ-OTHER=0 denominator 3'; 'VERDICT: VALID -- positive control fired'",
        "planted mutant SSM command 1beb51ee-c9b7-4936-a286-539390c28614 -- positive control re-pointed to a known-DENY prefix, printed 'positive rc=1' and 'VERDICT: VOID', so the VALID above is a tested pass and not a constant",
        "population derived by subtraction from the consuming code, not from the upstream summary: data/assets/scripts/gold/investor_reporting/directory_runner.py Firm49F.DIMS + the 201-group overlap census (dim_portfolio_group, bridge_group_account), FirmINF.DIMS, FirmCOT.completed_dates",
        "the three firms' own constants: runners_49f/runner_common.py GOLD_BUCKET='opal-data-49financial' OUT_ROOT='gold/advi' SILVER_BUCKET='opal-data-assets'; runners_inf/runner_common.py SILVER_BUCKET='opal-data-inf' API_DIMS_PREFIX='silver/api_dims/'; runners_cot/runner_common.py ASSETS_BUCKET='opal-data-assets' SILVER_PREFIX='blackdiamond/cottonwood/silver/'",
        "aws iam get-role-policy mdpf-daily-runner-ec2-role/mdpf-runner-scoped -- 27 statements; opal-data-49financial in ZERO, opal-data-cot in ZERO, s3:PutObject on NO firm bucket; the policy read agrees with the host's own attempt, which is a second instrument",
        "row IRPT_BCKEND-S50 @6d7c132f43 stating denominator 6 source prefixes + 3 destinations with 4 denied",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_6.result.md:40 stating '5 of the 9 prefixes'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MDPF_GLOBAL.TO-IAM1 @85f58dfd9c: 'mdpf-daily-runner-ec2-role is AccessDenied on 5 of 9 prefixes directory_runner.py reads' and 'NOT AUTHORIZED: any grant beyond the 8 prefixes the measurement names'.",
    "world_is": "The live, host-measured population is 10 source prefixes with 8 denied and 3 of 3 destinations denied. A correct grant therefore needs 11 prefix grants and cannot be expressed within a ceiling of 8.",
    "notes": "THE GENERAL SHAPE IS WORTH MORE THAN THE COUNT, and it is not about this role: A SUBSET MEASUREMENT TRAVELLED AS A POPULATION MEASUREMENT, gaining confidence at each hop while its denominator silently shrank -- worker sweep (6 probed, 4 denied) -> battery summary ('5 of the 9') -> task order ('5 of 9', boundary fixed at 8). Every hop was written in good faith and each cited the one before it. It was catchable only by deriving the population from the CONSUMING CODE rather than from the nearest upstream summary. This is CLAUDE.md Rule 24's subtraction-from-a-printed-denominator, and specifically its warning that a subtraction over the WRONG DOMAIN arrives with a printed denominator and so READS AS MEASURED -- the 6 was a real number from a real sweep, which is exactly why nobody re-derived it. The cheap defence is one question asked of any inherited count before acting on it: what POPULATION was enumerated, and was it enumerated from the thing that consumes the resource or from the last document that mentioned it. NOT A DEFECT OF THE ROUTING SEAT: 2.0.0_SA_COO~B measured what it needed for its own blocked cell, said so at the right grain, and routed rather than widened -- its sweep was never offered as a population census."
  },
  {
    "id": "MDPF_GLOBAL-S2",
    "project": "MDPF_GLOBAL",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~C",
    "surfaced_at": "2026-09-12T11:31:51Z",
    "one_line": "THE TASK ORDER'S STATED MECHANISM FOR THE comp-iam BLINDNESS DOES NOT HOLD FOR THIS ROLE -- THE SYMPTOM IS REAL AND INDEPENDENTLY CONFIRMED, BUT THE CAUSE WAS IMPORTED FROM A DIFFERENT ROLE AND NOT RE-MEASURED HERE. MDPF_GLOBAL.TO-IAM1's preflight block says comp-iam reads 'statements: 0' for mdpf-daily-runner-ec2-role because 'the policy comes from data.aws_iam_policy_document and the parser does not follow that indirection'. It does not: infra/aws/terraform/mdpf-pipeline/iam.tf:41-45 declares aws_iam_role_policy.mdpf_runner with policy = jsonencode({...}), an INLINE document, and comp-find over that whole root returns a MEASURED ZERO for aws_iam_policy_document across 15 scanned files. The data-source finding is true of irpt-directory-refresh-role, where row IRPT_BCKEND-S50 measured it; it was generalised onto this role in good faith and is false here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/mdpf-pipeline/iam.tf:41-45 -- resource aws_iam_role_policy.mdpf_runner, name = 'mdpf-runner-scoped', policy = jsonencode({ Version/Statement ... }) (inline, not a data source)",
        "comp-find 'aws_iam_policy_document' infra/aws/terraform/mdpf-pipeline --limit 20 -> 'NO HITS. This is a MEASURED zero over 15 scanned file(s) in scope'",
        "row IRPT_BCKEND-S50 @6d7c132f43 naming the data source it DID measure: 'data.aws_iam_policy_document.irpt_directory_refresh.json' on irpt-directory-refresh-role",
        "comp-read infra/aws/terraform/mdpf-pipeline/iam.tf --enumerate 'Condition|s3:prefix|ListScoped' -> 34 hits / 798 lines, every ListBucket on this role prefix-conditioned via StringLike s3:prefix, never bucket-wide"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MDPF_GLOBAL.TO-IAM1 @85f58dfd9c preflight: comp-iam reads statements: 0 on this role because its policy comes from data.aws_iam_policy_document and the parser does not follow the indirection.",
    "world_is": "This role's policy is an inline jsonencode document and this terraform root contains no aws_iam_policy_document data source at all, so whatever makes comp-iam read zero here, it is not that indirection. The true cause on THIS role is UNESTABLISHED and this row does not assert one.",
    "notes": "NOTHING IN THE ORDER'S DECISION DEPENDS ON THE CAUSE -- comp-iam is excluded as a grading instrument either way, and that exclusion was the right call. Recorded because A WRONG CAUSE IS MORE DURABLE THAN A WRONG COUNT: the count has a tripwire on it and the cause does not. A later seat reading 'this role uses a data source' will look in the wrong file; worse, a seat that learns the blindness as data-source-specific may TRUST comp-iam on the next inline-policy role and read its zero as an empty policy. Sibling of the estate's standing note that a named enforcement surface is a claim until someone runs it -- the same holds one level down: a named MECHANISM is a claim until someone reads the source. Two independent runs agreed on the zero (2.0.0_SA_COO~B msg 96077, 1.0.0_SA_CTO), so the symptom is not in doubt; only the explanation is."
  },
  {
    "id": "MDPF_GLOBAL-S3",
    "project": "MDPF_GLOBAL",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~C",
    "surfaced_at": "2026-09-12T12:35:00Z",
    "one_line": "THE 49FINANCIAL HALF OF TO-IAM1 IS STRUCTURALLY IMPOSSIBLE AS AN IDENTITY GRANT, AND THE ESTATE ALREADY DECIDED SO ON PURPOSE. The grant applied cleanly (0-diff, 34 live statements, 7 new Sids present) and the host STILL reads AccessDenied on 5 of 5 opal-data-49financial prefixes, because that bucket carries a bucket-policy statement DenyForeignFirmPrincipals -- Deny s3:* on Principal * conditioned ArnLike aws:PrincipalArn [role/cot-*, role/inf-*, role/mdpf-*, role/opal-assets-mdpf-*]. mdpf-daily-runner-ec2-role matches role/mdpf-*, and an explicit resource-policy Deny beats every identity Allow. This is not a defect: it is CLAUDE.md's cross-firm isolation hard stop in its PER-FIRM-BUCKET shape ('per-firm buckets -> bucket-scoped Deny'), and opal-data-49financial is the ONLY one of the five involved buckets carrying it (bd, cot, inf and assets were each read: CloudFront OAC/OAI allows only, no PrincipalArn-conditioned Deny). So 6 of the 11 authorized grants are effective, 3 destination writes are effective on the APPLIED plane, and 2 statements are INERT BY DESIGN OF A CONTROL NOBODY HAS PROPOSED REMOVING.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO -- three mutually exclusive routes and NONE of them is an AE lane's to choose: (a) seek an exception to DenyForeignFirmPrincipals for this one role and prefix set, which is a CROSS-FIRM ISOLATION decision and on CLAUDE.md's NEVER list, so Andrew's; (b) re-route the 49financial dimension read so the mdpf host never touches that bucket (e.g. the three dimensions reach the runner the way its bundle already reaches it, or the build moves to a principal the bucket permits); (c) accept that the 49financial leg cannot run from this host and re-cut IRPT's expectation. \u26d4 AND A FOURTH ITEM THAT IS NOT A ROUTE BUT IS OWED EITHER WAY: two now-INERT statements (IrptDirectory49fDimsRead, IrptDirectory49fDimsListScoped) reference another firm's BUCKET from the mdpf pipeline tree and grant nothing. This lane RECOMMENDS REVERTING THEM if the Deny stands, and did NOT revert them unilaterally because the amended face enumerated those five prefixes as authorized -- removing an explicitly authorized grant is the issuer's call, not the executor's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM b2da11c2-cf22-40d8-8335-14169fd0445a on i-02448edb624a7a7cf, Success rc=0, positive control READ-OK: 'AC4 SOURCE: READ-OK=5 READ-DENY=5 READ-OTHER=0 denominator 10'; the 5 denials are exactly the 5 opal-data-49financial prefixes and nothing else",
        "aws s3api get-bucket-policy --bucket opal-data-49financial -> 1 statement, DenyForeignFirmPrincipals, Deny s3:*, Principal *, Resource [bucket, bucket/*], Condition ArnLike aws:PrincipalArn [role/cot-*, role/inf-*, role/mdpf-*, role/opal-assets-mdpf-*]",
        "the same call on opal-data-bd, opal-data-cot, opal-data-inf, opal-data-assets -> 2 statements each, CloudFront OAC/OAI allows plus one non-PrincipalArn Deny on assets; NONE denies mdpf-*; opal-data-mdpf has NoSuchBucketPolicy",
        "aws s3api head-bucket opal-data-49financial -> exists, us-east-1, same account 313476888478 (so this is neither a missing bucket nor a cross-account gap), and it is 1 of 36 buckets in the account's list",
        "aws iam get-role-policy post-apply -> 34 statements = 27 pre-existing + 7 new, all 7 Irpt* Sids present with the authored shape, so the identity grant is APPLIED and correct",
        "terraform 0-diff re-plan after apply: 'No changes. Your infrastructure matches the configuration.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MDPF_GLOBAL.TO-IAM1 amendment 1 @bcff22b113 authorizes 11 enumerated prefix grants, of which 5 are opal-data-49financial/gold/advi/dimensions/*, and defines IAM1-AC4 as the host-side re-read reading ALLOWED on the previously denied prefixes.",
    "world_is": "Five of those eight denied source prefixes cannot be granted by any identity policy, because the bucket itself explicitly denies every mdpf-* principal. IAM1-AC4 therefore reads 5 of 10 rather than 10 of 10 and the order stays OPEN.",
    "notes": "\u2b50 THIS IS THE CLEANEST AVAILABLE DEMONSTRATION OF WHY THE FACE CALLED IAM1-AC4 NON-SUBSTITUTABLE, AND IT SHOULD BE CITED WHEREVER THAT CLAIM IS DOUBTED. THREE INSTRUMENTS ALL SAID THE GRANT WAS CORRECT: a green targeted plan (0 to add, 1 to change, 0 to destroy, 26 unchanged elements hidden), a live get-role-policy showing all 7 statements exactly as authored, and simulate-principal-policy returning ALLOWED for both the GetObject and the prefix-conditioned ListBucket on 49financial. THE WORLD STILL SAYS AccessDenied. Every one of those three reads the IDENTITY plane; only the host reads the EFFECTIVE plane, where a resource-policy Deny lives. A DESIRED-APPLIED-EXERCISED ladder is not a formality here -- APPLIED was true and EXERCISED was false, and no amount of APPLIED evidence would ever have found it. See MDPF_GLOBAL-S4 for the instrument half of this finding. NOT A DEFECT OF THE ISSUER: the face's enumeration came from this lane's own host sweep, which measured the denial correctly and could not have known its CAUSE was a resource policy rather than a missing grant -- a denial looks identical either way from the caller's side, which is the same indistinguishability that produced W2-S50."
  },
  {
    "id": "MDPF_GLOBAL-S4",
    "project": "MDPF_GLOBAL",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~C",
    "surfaced_at": "2026-09-12T12:35:00Z",
    "one_line": "simulate-principal-policy HAS A FIFTH FALSE-VERDICT MODE AND IT IS THE FIRST ONE THAT FAILS IN THE OVER-GRANTED DIRECTION: it does not evaluate RESOURCE policies, so it returns ALLOWED for an action an explicit bucket-policy Deny refuses. Measured here: the same action, the same principal, the same ARN -- simulate says 'allowed' for s3:GetObject on opal-data-49financial/gold/advi/dimensions/dim_account/... and for the prefix-conditioned s3:ListBucket, while the host's own attempt returns AccessDenied, because opal-data-49financial carries DenyForeignFirmPrincipals. The cloud-ops skill documents FOUR false-DENY modes and states the instrument 'fails in the UNDER-granted direction'; that sentence is true of those four and is NOT true of the instrument as a whole.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/mdpf-daily-runner-ec2-role --action-names s3:GetObject --resource-arns arn:aws:s3:::opal-data-49financial/gold/advi/dimensions/dim_account/date=2026-09-11/data.parquet -> allowed (ONE resource ARN, object grain, no batching)",
        "the same tool, s3:ListBucket on arn:aws:s3:::opal-data-49financial WITH --context-entries s3:prefix=gold/advi/dimensions/dim_account/ (so mode 2 is excluded) -> allowed",
        "the host's own attempt as that exact principal, SSM b2da11c2-cf22-40d8-8335-14169fd0445a: READ-DENY AccessDenied on all five 49financial prefixes, positive control READ-OK in the same sweep",
        "aws s3api get-bucket-policy --bucket opal-data-49financial -> DenyForeignFirmPrincipals, Deny s3:*, ArnLike aws:PrincipalArn role/mdpf-*",
        "accessanalyzer validate-policy on the action set -> 0 findings, so mode 3 (a typo reading as a deny) is excluded"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cloud-ops skill's IAM INSTRUMENT TRAPS section enumerates four independent false-DENY modes for simulate-principal-policy and concludes 'It fails in the UNDER-granted direction and is INVISIBLE against a narrowly scoped principal'.",
    "world_is": "There is a fifth mode and it fails the OTHER way. simulate-principal-policy evaluates identity policies only; a resource-policy Deny is invisible to it, so it returns ALLOWED where the effective decision is DENY. The four documented mitigations (one ARN per call, --context-entries, validate-policy for action names, correct resource grain) were ALL in force here and none of them touches this mode.",
    "notes": "\u26d4 WHY THIS IS WORSE THAN THE FOUR ALREADY DOCUMENTED, EVEN THOUGH IT IS RARER: a false DENY gets argued with, because somebody has to explain why a grant they just wrote does not work. A false ALLOW gets ACTED ON -- it is the green that closes a ticket. The estate's standing note that 'the failure mode is a GREEN' applies exactly. \u2b50 THE CHEAP DEFENCE IS ALREADY IN THE LAW AND COSTS ONE CALL: simulate-principal-policy answers a question about the IDENTITY plane only, so on any S3 target ask get-bucket-policy whether a resource policy exists BEFORE quoting a simulate ALLOW -- and where a host can run the action, prefer the host. SCOPE OF THE CLAIM, STATED NARROWLY: this was measured on S3 with a bucket policy. The same blindness must apply to every resource-policy surface the simulator does not take as input (KMS key policies, SQS/SNS, Secrets Manager, Lambda permissions, S3 Access Points), but this lane measured ONE and is not asserting the others. `simulate-custom-policy` with the resource policy supplied is the documented way to include one, and nothing in the estate currently does that."
  },
  {
    "id": "MDPF_GLOBAL-S5",
    "project": "MDPF_GLOBAL",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~C",
    "surfaced_at": "2026-09-12T13:06:32Z",
    "one_line": "ROUTE (b) IS CLOSED BY MEASUREMENT, AND THE ROUTE ITSELF WOULD COLLIDE WITH A SECOND NEVER. 1.0.0_SA_CTO asked one read under TO-IAM1: are the five 49F dimension tables reachable by KEY-PREFIX in a bucket mdpf-daily-runner-ec2-role may read -- which would satisfy the cross-firm law rather than circumvent it, key-prefix being one of the two shapes the law names. ANSWER: NO, not today. The five tables exist ONLY at opal-data-49financial/gold/advi/dimensions/ (1098 / 1098 / 1098 / 2 / 2 objects), and a census of ALL 23 prefixes this role may read found 0 of 35,538 objects carrying any of the five table names. The legacy shared-bucket root opal-data-assets/portal/gold/advi/ is EMPTY (0 objects). \u26d4 AND THE REASON IT IS EMPTY IS ITSELF THE ANSWER TO WHETHER IT SHOULD BE REFILLED: the GOLDHOME re-point (Andrew-direct 2026-08-18 ~1730Z, 'Ratified, proceed with the re-point before the P2 apply') deliberately moved the ADVI gold root FROM that shared path INTO the per-client bucket. Re-mirroring it back to make it readable would reverse a standing Andrew ruling AND stand up a duplicate output path -- which is its own NEVER carrying Andrew's complete veto ('NEVER stand up a shadow/build-alongside pipeline, duplicate output path').",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3api list-objects-v2 on opal-data-49financial/gold/advi/dimensions/<table>/ with CLIENT-SIDE counting -> dim_account 1098, dim_relationship 1098, dim_identity_crosswalk 1098, dim_portfolio_group 2, bridge_group_account 2",
        "census over all 23 prefixes this role may read post-grant (opal-data-assets x11, opal-data-mdpf, opal-data-portal-v2 x3, opal-data-bd x4, opal-data-inf x3, opal-data-etfs x1) -> DENOMINATOR 35,538 objects, 0 carrying dim_account/ dim_relationship/ dim_identity_crosswalk/ dim_portfolio_group/ or bridge_group_account/",
        "aws s3api list-objects-v2 --bucket opal-data-assets --prefix portal/gold/advi/ -> Contents None, i.e. 0 objects",
        "aws s3api list-objects-v2 --bucket opal-data-49financial --prefix gold/advi/ --delimiter / -> CommonPrefixes _logs/ canonical/ dimensions/ insurance/ reference/, so the canonical root is live and structured",
        "docs/architecture/GOLD_MIGRATION_PHASE_FRAMEWORK.md:37 -- 'ADVI GOLD HOME SUPERSEDED 2026-08-18 ~1730Z (Andrew-direct, RATIFIED)': the ADVI gold root moves out of opal-data-assets",
        "org/critical_paths/change_management/20260819T0106Z_goldhome-repoint-49f-rp-ae-1-bucket-mint_deploy_completion.md -- CLOSED, the re-point ledger; its own pre-act check recorded comp-find 'portal/gold/advi' = 0 hits",
        "CLAUDE.md HARD STOPS: 'NEVER stand up a shadow/build-alongside pipeline, duplicate output path, or standing parity comparator (Andrew complete veto)'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "1.0.0_SA_CTO msg 96105 under MDPF_GLOBAL.TO-IAM1: route (b) is the live engineering route IF the five dimension tables are reachable by key-prefix in a bucket this role may read -- 'whether they exist under a prefix this role may read is a measurement nobody has taken', asked as a READ and explicitly NOT ordered as a build.",
    "world_is": "They are not. One location only, and it is the bucket whose policy refuses this principal. Every readable alternative is empty of them across a 35,538-object denominator. Making route (b) true requires WRITING 49F gold data somewhere new, which is a build, reverses an Andrew-direct supersession, and trips the duplicate-output-path veto.",
    "notes": "\u2b50 THE VALUE HERE IS THAT A ROUTE WAS CLOSED BY ONE READ INSTEAD OF BY A SPRINT. The issuer declined to order the build off an assumption after two wrong counts in one night and asked for the measurement first; the measurement says the build would have been wasted AND would have collided with a second hard stop nobody had connected to this question. \u26d4 NOTE THE SHAPE OF THE NEAR-MISS: route (b) is ATTRACTIVE precisely because it sounds like compliance -- 'use the key-prefix shape the law allows' -- and the law does name key-prefix as a legitimate shape. What makes it wrong is not the shape but the ACT required to reach it: you cannot make data appear under a new key-prefix without writing it there, and for already-published gold that write is a duplicate output path. A law that names two permitted SHAPES does not thereby permit any ACT that produces one of them. THE REMAINING ROUTES ARE (a), which is Andrew's and which 1.0.0_SA_CTO recommends AGAINST, and (c), which is IRPT's expectation to re-cut. This lane has no engineering route left on this order and says so rather than inventing one."
  }
]
```
