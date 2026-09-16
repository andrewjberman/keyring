# Menachem Schwab access specification -- 0.7.0_AE_CloudOps

**archetype:** DESIGN
**Date:** 2026-09-14
**Task Order:** Andrew-direct investigation/specification; verbatim record in deliverable.
**Status:** SPECIFICATION COMPLETE; implementation not started.
**Window:** After startup log ending ~17:34Z, through 18:27:33Z.
**Push state:** LOCAL. Measured origin/CLOUD: 6a5b276f8b382edca90673d1f425320a251ca0e5 (git ls-remote, 18:27Z).

## Objective and result

Specify easy Claude application access for menachem@opalinvest.com to read/query/download selected Schwab data from opal-data-assets. Andrew confirmed an Opal Team/Enterprise workspace, both masters kept separate, the existing opal-gateway as the entry point and filtered CSVs initially with originals later. The complete spec, disabled proposed entitlement, source-reader policy and measured evidence are in deliverables/MENACHEM_SCHWAB_CLAUDE_ACCESS_20260914/.

The design extends gateway authentication and authorization, adds a Schwab catalog/query/export integration, and uses a per-user/purpose assumed role. Current write-class entitlements are insufficient for data scope. The source callback logic allows loopback only; hosted Claude login needs the exact HTTPS callback. The Terraform per-employee role pattern exists and its gateway STS policy is live; no aws_entitlements or assume_role dispatch was found in the searched gateway app source. The proposed exact Menachem role name does not exist.

## Compiler Tools

| Tool | Command/scope | Result | Note |
| --- | --- | --- | --- |
| comp-which | Questions before source, bucket, IAM, inbox and specification inspections | PARTIAL | Bare shims execute. Several fuzzy rankings were unrelated; scoped comp-find fallback used. |
| comp-blast | opal-data-assets | PARTIAL | Served graph 27982 nodes / 60133 edges, vintage 2026-09-14T12:13:53.330672Z. No extracted downstream edges is a lower bound, not no consumers. |
| comp-find | Scoped shared-infra, gateway, source, own-home and artifact queries | PASS/PARTIAL | Useful with explicit paths. Filename mode matches names, not directory paths. |
| comp-find | Router fallback CloudOps | TIMEOUT | Unscoped fallback exceeded 90 seconds; not evidence of absence. |
| comp-find | Filename query with pipe alternation | FAIL | Windows shim exposed pipe to cmd parsing. Retried using simple scoped terms; no shim edited. |
| comp-iam | service opal-gateway | PARTIAL | DESIRED only; 3 unresolved resources. Does not validate proposed standalone policy or prove live grants. |
| comp-diff | Current shared worktree | PASS/PARTIAL | Exit 0; 6 unrelated existing changes and large portal blast. New local specification files require explicit pathspec validation. |

**What worked:** scoped compiler searches, source inspection after compiler limits, account-guarded boto3 metadata reads, footer-only Parquet inspection and IAM custom-policy simulation.
**What failed:** broad router fallback timeouts; pipe escaping through cmd shims; AWS CLI v1 rejected --no-cli-pager, then succeeded without that flag. One inbox inspection mistakenly targeted an agent-home subdirectory; corrected from the canonical contract to org/mcp/inbox/0.7.0_AE_CloudOps, with no unread root Markdown messages and no message consumed.
**Gap found:** current app source has no Schwab dataset entitlement/query dispatch and cannot accept the hosted Claude callback. The IAM compiler cannot establish deny completeness or deployed behavior.
No production code, infrastructure definition or compiler source changed.

## Deployment Sequence

| Step | Action | Result |
| --- | --- | --- |
| 1 | Establish authority | Andrew-direct spec request and clarification answers quoted verbatim in ANDREW_DIRECT.md. |
| 2 | Inspect repository and canonical root inbox | Scoped source findings; no additional unread Markdown message or GO. Startup already complete. |
| 3 | Read live AWS metadata | Account 313476888478; S3 layout, policy, protection, encryption, versioning and file metadata. No rows, secrets or token values loaded. |
| 4 | Inspect Parquet footers | Six latest objects, both masters; version-pinned Range reads of metadata only. |
| 5 | Verify integration evidence | Gateway discovery 200; exact live employee STS policy read; proposed Menachem role absent. No OAuth POST or user login performed. |
| 6 | Model proposed IAM policy | 41/41 SimulateCustomPolicy cases pass; no permissions attached, no write/delete calls attempted. |
| 7 | Review package consistency | Proposed source columns exist in both master schemas; six IAM prefixes match profile; original download false; JSON/syntax/local links pass. |
| 8 | Record locally | Explicit-path safe-commit of eight deliverables plus this log; no push or deployment. |

## Verification and evidence limits

Latest observed position snapshots: 2026-09-11, 102421 rows (08242234) and 105074 (08335338), approximately 2.45 and 2.58 MB. Data dates are independent of modification dates. Account schema includes tax identifiers and mailing fields; balance dimension includes account titles. No source rows were read.

The IAM test is MODEL ONLY. Live authorization, role trust after provisioning, production source parity, application filters and Claude login must be exercised during implementation. No data access has been enabled by this task.

Source inspection checkpoint: HEAD 6ef8aa8a84a6e0e93ec5bbd0db0d7a13988b429a at 18:25Z.
Relevant working-file blob IDs:
- oauth_as.py: e5459e639678d9948af714814802ce9ec572414a
- context.py: e87e1733c45b7625cc4d6a7bf137560df6ba4611
- tools.py: bcbd8e56e690133f2814ab4daf7a0a44b6507365
- entitlements.py: e5e14865814bef03012ff6c72bae18b2d8af0dca
- identity_scope.py: 3779128dc60e9738b071f5d985588c413ce4a9b1
- query_v0.py: 52b42a24b1eb159be5f433d130ad0bbd42c942a2
- taxsma_gateway_iam.tf: 2c9b16543141759a6c40b1483d3e1deaea8753d3
- schwab_schemas.py: 49d85f2fc21a4dd78b9165ba97c8e1c70849f15b
- schwab_projections.py: 726afb057b88c19bd0f66da8585b3f6baa35878a
- monolith.tf: c8cf052e01b153154013a88231ca9f231d23481f

## Decisions

| Decision | Basis |
| --- | --- |
| Extend existing opal-gateway | Andrew's architectural steering; existing identity/audit/IAM foundations. |
| Application entitlement plus restricted AWS role | User customization needs row/column/date scope; AWS denies source mutation. |
| Both masters kept separate | Explicit user answer and source pipeline invariant. |
| CSV first; original-file permission later | Explicit user answer; original files bypass partial-object projections. |
| Initial fields/dates/account coverage remain proposals | User confirmed masters/functions, not those finer dimensions. |
| Record instruction locally; no outbound broadcast in this task | Repository asks for peer broadcasts, but higher-priority developer instruction forbids messaging others without explicit authorization. No separate outbound authorization was supplied for this specification task. |

## Files Modified

Eight new files in the owned deliverable directory: SPEC.md, ANDREW_DIRECT.md, menachem-entitlement.proposed.json, reader-role-policy.proposed.json, observed-metadata.json, gateway-role-readback.json, iam-simulation-results.json, validate_proposed_policy.py. This session log is the ninth committed path. No unrelated shared-worktree changes are included.

## Blockers and current state

None on specification completion. Remaining rollout inputs are Menachem's verified immutable identity, exact initial fields/date/account scope and measured workspace/gateway readiness. These do not block the delivered spec. Original-file format choice is resolved: CSVs first.

## Next Steps

Provide the reviewable specification to Andrew. Implement/provision only under subsequent authorization and the normal gateway security/release workflow. No new monitoring loop or peer dispatch started.

