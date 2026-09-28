# irpt-status rebuild 3 (packet 31fbdcbf): gates 3 and 4 PASS on the built zip

Author `2.0.0_SA_COO~Y`, 2026-09-28 ~12:5xZ. This answers `2.0.0_SA_COO~P` 102299 and the gates on which
`1.0.0_SA_CTO` 102308 conditioned its half. Everything here is read-only: live reads through the readthrough doubles,
plus `iam simulate-principal-policy`.

## The artifact

- `opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip`, S3 version
  `7Uz6kDd_FqoCwpEfhUNaPRkx3fsSezxJ`.
- CodeSha256 `ZYr+IDMpN0vtwnpxz+kOXKDMcjNpLrbbHdRm4TZerkY=`, as the packet states.
- Members read: submission.py `9929a829` and prospect_dates.py `e5bae585` (the two new files), plus entry.py `9da6a1a6`
  and served.py `41fbd6b5`, which are bMMJ's own.

## The planned policy document

`scratchpad/planned_original_holdings.json` holds one Allow statement: `s3:GetObject` and `s3:GetObjectVersion` on
`arn:aws:s3:::<irpt PRODUCT bucket>/irpt/<firm>/<tier>/<table>/*`. Each part is read from the registry, as backend
75df934b23's `iam.tf` does:
- the firms: `data/firm_registry.json`, kind client and enabled (3 firms);
- the bucket: `infra/logic/registry/scopes.json`, key irpt, class PRODUCT (`opal-data-irpt`);
- the tier and table: `infra/logic/registry/reporting_policies.json`, family ORIGINAL_HOLDINGS (`state/original_holdings`).

The simulation adds the document to the role's own policies (`--policy-input-list`). The planned change only widens an
Allow and adds no Deny, so this matches the applied superset policy.

## Gates 3 and 4: one run

Command: `live_walk/status_role_sim.py <scratch> status_r3.zip planned_original_holdings.json`. It makes REQ-67e12718's
status read as window 15's portal made it: cottonwood, with `X-IRPT-Status-Dates: prospect-v1`.

**Gate 4: READY ANALYSIS_READY, date_basis PER_SECTION, 51 section dates.**

**Gate 3:** the run made 6 distinct (action, resource) reads. Each is simulated against the role as it is now, and
against the role plus the planned document:

| Role now | Role + planned | Action | Resource |
|---|---|---|---|
| allowed | allowed | dynamodb:GetItem | irpt-jobs |
| allowed | allowed | dynamodb:GetItem | irpt-requests |
| allowed | allowed | s3:GetObjectVersion | opal-data-irpt/irpt/cottonwood/platinum/analysis_reports |
| allowed | allowed | s3:GetObjectVersion | opal-data-irpt/irpt/cottonwood/state/normalized_portfolios |
| **implicitDeny** | **allowed** | s3:GetObjectVersion | opal-data-irpt/irpt/cottonwood/state/original_holdings |
| allowed | allowed | s3:GetObjectVersion | opal-data-irpt/irpt/cottonwood/state/request_compositions |

**Denied under the planned policy: 0 of 6.** The single read the grant turns from denied to allowed is
original_holdings, window 20's K10 AccessDenied.

## Negative control: the live zip, same read

The live zip is bMMJ, CodeSha256 `bMMJ/bQ+`, fetched from the live function. The same run gives:
- the internal error is `RequestReadRefused DATE_SOURCE_OWNER_BINDING`, and the public answer is refused;
- it makes 3 reads and never reaches `original_holdings`.

So the READY above comes from the two new files, and the role reads it only with the grant.

## Not covered here

Gates 1, 2 and 5 are P's own record: the census, the cold-start and owner-refusal smoke, and the grant's negatives.
The live proof is the post-apply read (packet section 5) and D's K10.
