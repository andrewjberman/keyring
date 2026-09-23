# CTO direct review: scope, organization reader and custody factory

**archetype:** TRACE
**Reviewer:** 1.0.0_SA_CTO, 2026-09-23.
**Authority:** Andrew's direct instruction, “No independent review, you are the reviewer here,” recorded in `LOCAL_LIVE_PARTNER_SCOPE_20260923.md` at `3345f4e3cd`.

## Verdict

**Bounded source PASS. Runtime and complete custody generation remain OPEN.**
CTO inspected source and ran the checks below directly in an isolated Git archive.
No separate CVO approval is required. Existing reviewer drivers were reused as
test inputs; the results below are CTO's actual executions.

| Reviewed candidate | Direct result |
|---|---|
| Backend `e47aed7f710f5d65f317e806c609c8aeb554def3`, factory `819c9e399086cffb2876a21fbc2cee01724b0bd7` | 30/30 custody factory/retained cases passed. |
| Original driver at `02501a68ec`, exact one-assertion scalar adaptation | 20/20 passed. Both original and adapted hashes matched the supplied assertion-only evidence. No behavioral assertions removed. |
| Portal `e0531491b33db98e2d88f22e7c09a34ee0b9fa04`, containing parser repair `910ebf36` | Actual backend response capture passed; 49/49 parser/context tests passed, 67 assertions. This closes the tested R-P13 parser cases at source. |
| Package declaration `83ca4a50e5` | Seven functions' declared member lists and all 228 committed member hashes verified. Generate has 73 members; all 29 factory module hashes match the directly tested source. This is source-member evidence only. |

The paired scope check exercised actual Entry output under controlled external
directory fixtures, then the real Portal parser/client. It includes valid
Global and single-firm responses, partial/unavailable outcomes, wrong outer
firm, mismatched member tenant, and malformed/extra fields. It is not a logged-in
browser test or live three-firm data acceptance.

## Code findings and limits

The factory creates custody access and authorization per request, rechecks
current selection/owner/snapshot, freezes normalized bytes, and preserves
retained-input retry. The tests cover revoked access, foreign client/account/
snapshot, missing/ambiguous selection and prospect refusal. Actual SDK profile
calls are Stubber-controlled; the installed Entry tests supply synthetic
snapshot and normalized-input callbacks. The tests do not prove dispatch,
vendor execution or production source binding.

The organization reader uses the admitted exact home key and strongly consistent
projected GetItem. Its scalar projection fits the consumer schema, preserves
the eight metadata values and reports mutable upstream revision as unavailable.
Actor home and selected report tenant remain distinct. The original driver
adaptation changes only where those same eight values are asserted.

The package receipt's manifest hash is for CRLF checkout bytes. CTO measured
the committed LF hash separately and reproduced the receipt hash through the
exact LF-to-CRLF transformation. This is an explained encoding difference.
More materially, the generate import check returns zero while explicitly
reporting **UNENFORCED**, because BUILD_MANIFEST.json is absent and jsonschema/
referencing are undeclared. That return code is not runtime completeness.
P has been directed to supply explicit dependency and isolated Lambda-runtime
evidence. CTO has not accepted that pending result.

M's `abfb3eaf8242cf5df26c7e1074e0e555245d969a` handoff identifies the remaining
actual-input gap. Existing selection/publication APIs do not supply the two
required production callbacks. The current holdings display hierarchy does not
establish complete security-level custody for all three firms. Same-day index
changes must not silently change a previously accepted snapshot. Signed/zero
positions must not be converted by taking absolute values, dropping rows or
substituting model targets. Nonempty comparisons also need their maintained
resolver. The module-global generation Entry remains unconfigured.

## Current assignments

- P retains shared integration/package ownership: finish declared third-party
  closure, exact runtime proof and preparer/configuration/role placement. No
  production callback or new cloud action is authorized by this review.
- M is preparing an exact per-firm actual-position producer proposal, identifying
  source paths, responsible owners, located versus missing inputs, reconciliation
  and unknown-value controls. This is bounded read-only source work.
- Y is preparing a bounded signed/zero-value normalization policy proposal tied
  to the freezer, schema and recipe consumer. No inferred economic acceptance.
- CTO adjudicates those proposals and reviews final candidates directly.

Evidence, pins, commands, driver hashes and all 29 source hashes are recorded in
`CTO_DIRECT_REVIEW_20260923.json`. Original tests and source were extracted into
a unique local temporary directory. This record does not claim that localhost
has the candidate installed, that production is fixed, or that E2E MVP is done.
