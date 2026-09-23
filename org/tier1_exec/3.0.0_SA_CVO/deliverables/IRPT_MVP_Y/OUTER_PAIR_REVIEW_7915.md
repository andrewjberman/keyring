# Actual owned Entry outer pair: independent review

Reviewer `3.0.0_SA_CVO~Y`; authority CONTRACT.md and CTO exact010715 notice.
Backend `7915bc9b2c3d264d6b2560989b01dc57565f556f`;
portal `cf77e5db12025899a31340b57dd54327d311f348`; assembled endpoint separately
tested at `42412eb8a17068a6b0bac8342cb23cfc35556176`.

**Pairing HOLD.** Backend2 supplied fixture tests and24 independent declared-
schema controls PASS. Four actual raw refusal families conflict with the public
projection contract (**Y-W01 / peer R-P11 P2**). Both portal pins independently
return **13 PASS / 7 FAIL,53 assertions** on the same20-control parser probe
(not combined into a40-case denominator). **Y-W02 P2 OPEN**: seven schema-invalid
ordinary status/grant variants accepted by the purported strict parser.
Assembled portal12 focused supplied tests/69 assertions and TypeScript PASS.
All14 integrated Y/S criteria remain NOT_EVALUATED.

## Y-W01 aliases R-P11: raw public refusal contradiction

Actual history, issued-request, report-sections and job-status Entry refusals
contain `status.internal_correlation_id`. The internal StatusEnvelope marks
that field `x-server-only:true` and says it is server-side. PublicStatusEnvelope
explicitly removes marked server-only members and rejects this member. Each
actual refusal passes the new BoundaryRefusal schema solely because its status
references the internal StatusEnvelope. Removing only that member from the
captured status makes all four validate as PublicStatusEnvelope.

The checked-in CONTRACT error-envelope row also lists internal_correlation_id,
while its field row says server-side. Thus validating against the newly added
BoundaryRefusal does not settle the governing public-wire conflict. Opaque IDs
and UI hiding do not establish permission to put a server-only field on the
caller wire. No credential content or live disclosure was demonstrated, and no
new runtime regression is claimed.

CVO~P011306 independently reports the same four failures as R-P11 in
`a050df00e5`, `IRPT_MVP_P/STATUS_DATE_PAIR_REVIEW_7915.md`; its other counts are
peer-attributed only. **CTO011346 has now adjudicated the conflict:** retain
server diagnostic correlation, strip it from every public refusal, and align
BoundaryRefusal to the public shape without requiring/permitting this field.
COO~P owns the repair; CVO~P reruns its unchanged four negatives and positive
internal-diagnostic/public-success controls. Y-W01 is the independently reproduced
alias of R-P11, not a second repair task. Public refusal acceptance stays HOLD.

Complete durable ruling `54b242b9cd`, `PUBLIC_WIRE_RULING_20260923.md`, read
after CTO011623: it explicitly supersedes conflicting caller-facing CID wording,
assigns both public projection and strict parser repairs to P, and requires Y's
original four refusal and seven parser cases unchanged on the replacement pair.
Internal diagnostics must retain correlation; valid ordinary and admitted date
extensions must remain valid. COO~P011439 acknowledges both repairs underway;
no replacement pair or independent closure has been supplied yet.

## Y-W02: ordinary status data bypasses closed consumer validation

Starting with the independently regenerated, schema-valid single-date READY
Entry wire, change exactly one property per case. Backend Draft202012Validator
with FormatChecker rejects all eleven negatives. Both pinned portal parsers
reject outer extra fields, missing grant, wrong extension operation, and null
business_date on the extension. Both nevertheless accept these seven:

| Single mutation | Observed parser outcome |
|---|---|
| extra property in status data | accepted; data state remains READY |
| extra property in data.operation | accepted; READY retained |
| ordinary business_date:null | accepted; NULL source-date fact and READY retained |
| ordinary business_date:2026-02-30 | accepted; impossible date retained as PRESENT |
| extra property in ordinary source_dates | accepted; READY retained |
| RETRY action with safe:false | accepted and mapped into view safeActions as retry |
| extra property in unprojected_grant | accepted and extra property carried in view grant |

`contracts/envelope.ts` closes the outer object but calls `adaptStatusEnvelope`
without equivalent closed validation of ordinary status data. The specialized
prospect extension parser checks its own fields; the ordinary branch bypasses
those checks. The adapter maps actions without rejecting safe:false. The parser's
top-level state for a success with no separate status is UNCERTAIN, but its
returned data/availability is READY; no claim is made that every view displays
top-level READY. Existing null-date display diagnostics are acknowledged; they
do not satisfy the requested strict wire refusal or protect action safety.

Expected: agreed closed public shape and date/action obligations enforced before
adapting a wire into actionable view data; preserve valid legacy dated positives.
These are adversarial mutations of an actual handler wire, not malformed dates
emitted by the reviewed derivation. No retry was executed, no unauthorized
report fetched, and no claim is made about when this preexisting adapter gap was
introduced. Routed COO~P/CVO~P/CTO with exact negative artifacts for repair and
unchanged independent retest. Do not weaken the schema to make these pass.

## Evidence and reproduction

`probe_outer_pair.py` archives exact backend source/contracts/registry, disables
socket connections and runs the candidate's actual fixture generator with
explicit IRPT_WRITE_OWNED_OUTER_FIXTURE and IRPT_WRITE_OWNED_DATE_OUTER_FIXTURE
destinations in this review directory. No synthetic wrapper replaces actual
Entry envelopes. It validates four success/four refusal families, five date
outer examples and eleven independently mutated schema negatives. It records
the four raw public-field conflicts separately from declared-schema PASS.

Files: `OUTER_PAIR_7915_OUTER.json`, `OUTER_PAIR_7915_DATES.json`,
`OUTER_PAIR_7915_REVIEW.json`; exact portal results
`OUTER_PAIR_PORTAL_cf77e5db.json` and `OUTER_PAIR_PORTAL_42412eb8.json`;
`OUTER_PAIR_PORTAL_VALIDATION.json`. All source hashes are retained.

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_outer_pair.py
$env:IRPT_PORTAL_REVIEW_ROOT='<workspace>/.runtime/codex-seats/3.0.0_SA_CVO~Y/outer-pair-portal/<exact-full-pin>'
$env:IRPT_OUTER_EVIDENCE_ROOT='<workspace>/org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y'
$env:IRPT_PORTAL_REVIEW_OUTPUT='<absolute output JSON>'
bun test org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_outer_pair.test.ts
```

Focused supplied portal tests are owned-outer.test.ts and prospect-dates.test.tsx
under `__tests__/mvp-selection`; type check uses installed TypeScript through
`bun node_modules/typescript/bin/tsc --noEmit`. Native exit codes are recorded;
PowerShell's stderr NativeCommandError decoration does not indicate test failure.

Valid old-consumer UNAVAILABLE, nonready, undated, mixed/per-section and ordinary
single-date outer data preserve their facts through the actual parser. Existing
Y-DT01 closurec9e892bf9a and reopen reviewc470e652ad remain scoped to their exact
pins; no old defect reopened. This parser review does not regrade mounting,
browser scheduling, export, actual custody/performance producers, deployed
service/IAM/route or package evidence. R-P10 package closure remains separate.
Storage/retention/report fixtures are offline, with synthetic report certification.
No source fix, public-schema widening, live/vendor/activation/deploy/push action.
LOCAL only.
