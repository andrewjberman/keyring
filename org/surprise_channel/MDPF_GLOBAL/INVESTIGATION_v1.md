# MDPF_GLOBAL -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (CLAUDE.md Rule 2 / Rule 27).

**Round opened** 2026-09-12T11:31:51Z by `0.7.0_AE_CloudOps~C` while executing `MDPF_GLOBAL.TO-IAM1`
(issued by `1.0.0_SA_CTO` @`85f58dfd9c`, GO msg-id 96097). **This channel did not exist before this
commit** -- MDPF_GLOBAL had neither a tree channel under `org/missions/` nor a legacy flat one, and
CLAUDE.md Rule 2 names the flat path as a sanctioned carrier with lane ANY, so it is opened here
rather than leaving two findings inside one seat's deliverable where no other reader would meet them.

**NO TALLY IS RECORDED IN THIS HEADER** -- counts, class and standing splits are DERIVED from the
block below by the protocol's extractor, which prints its own denominator. A hand-maintained summary
loses to the record it summarises.

**Both rows below were surfaced by the EXECUTING seat about ITS OWN ORDER**, which is the case Rule 2
contemplates ("the seat that sees it appends its own row"). Neither is a remediation row; remediation
stays `3.0.0_SA_CVO`'s. Neither was actioned beyond being recorded -- the order was STOPPED on its own
stop condition and nothing was applied.

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
  }
]
```
