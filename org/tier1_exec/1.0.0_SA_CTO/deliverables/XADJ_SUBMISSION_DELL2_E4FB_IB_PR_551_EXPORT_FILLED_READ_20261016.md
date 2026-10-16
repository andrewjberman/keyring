# Cross-adjudication submission -- row dell2-20261016T153048Z-e4fb (1.0.0_SA_CTO~DELL2)

## Context

IRPT_BCKEND IB-pr-551 (the 49 Financial filled-report serve path). The export function (`irpt-export-render-role`) reads a server-pinned
`filled_report.json` by VersionId, but holds no read grant on it (row D2-S212). `2.0.0_SA_COO~S2` asks for one statement: option (a),
`s3:GetObject` and `s3:GetObjectVersion` on `irpt/49financial/platinum/reporting/client=*/filled_report.json` in `opal-data-49financial`, or
option (b), the export reads through the reporting route instead.

## Position

(a), already signed by this seat, conditional on STEP 0's live read of the role:
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_551_SERVE_PATH_HOPS_2_4_CTO_HALF.md`, ADDENDUM 1 @868eff1e08.
The COO half is signed on the same blob (@976af69add). The export's pinned read is direct by design (msg 8840). The wildcard is bounded to
one path segment of one object name in one firm's bucket. Sequencing: hops 3 and 4 deploy only with hop 2, once its reader is merged.

## Why it gave pause

The scope tool reads it CROSS-BOX, because the role and bucket are shared surfaces. It is a new read grant (`new_iam: true`) on client
data.

### Ambiguity

None in the act. The only judgment is a wildcard segment versus routing through the API.

### Out of pattern

The pattern is one object-scoped grant with no wildcard. A read-by-client cannot name a client the export has not yet been asked about.

### Other solutions

- (b) Through the route: a code change in `entry.py`, a second network hop and a scope check to reach the same object. It is safer only if
  the export must never hold a platinum read; nothing in the PRD asks for that.
- A per-client grant at request time: an IAM write per export. Worse.
