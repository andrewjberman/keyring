# IRPT public wire adjudication — 2026-09-23

Owner: `1.0.0_SA_CTO`. Authority: Andrew's delegated worker-fork adjudication (`ecf350639a`) and [completion contract](CONTRACT.md), S5 and shared interface ownership. This ruling applies to the P/M/Y completion effort; the old B/F canonical cycles remain on hold.

## Evidence and scope

CVO~P review `a050df00e5` reports R-P11 against backend `7915bc9b2c3d264d6b2560989b01dc57565f556f` and portal `cf77e5db12025899a31340b57dd54327d311f348`: four actual caller refusal families emit `status.internal_correlation_id`, despite its server-only annotation and the public projection's strip requirement. CVO~Y's exact 20260923T011327Z notice independently reports the same conflict as Y-W01, including conflicting error-contract wording. These are one repair obligation with two independent evidence trails, not two competing implementations. This ruling relies on those reviews; CTO has not independently rerun their probes.

CVO~Y additionally reports Y-W02: both exact portal `cf77e5db` and assembled endpoint `42412eb8` accept seven adversarial ordinary-status variants that violate the closed contract: unknown data/operation/source/grant members, null business date, impossible date `2026-02-30`, and an unsafe retry converted to a safe UI action. These are mutated actual-wire cases, not a claim that the backend emitted malformed dates or a retry executed.

## IRPT-PUBLIC-WIRE-01: correlation is server-only

Preserve internal correlation in server diagnostics and internal status consumers. Every caller-visible refusal must use a public projection that excludes `internal_correlation_id`. The public refusal schema must neither require nor permit that field. Rendering it invisibly is insufficient. Do not widen public schemas or reclassify the field as public to obtain a pass.

This explicitly resolves the reported governing conflict: any existing error-contract wording that requires this internal CID on caller-visible wire is superseded for that field by this ruling. COO~P must identify and reconcile the exact conflicting source/schema/documentation row in its interface record. Internal diagnostic requirements remain. No replacement public tracking field is introduced by this ruling.

COO~P integrates the narrow response projection, authoritative schema/reference and generated-artifact repair, retaining all required public status/date fields, refusal reasons and fail-closed behavior. It coordinates any lane-owned function changes with that owner rather than editing concurrently.

## IRPT-PUBLIC-WIRE-02: strict ordinary-status consumer

COO~P repairs the shared parser to enforce the applicable closed ordinary-status contract, including nested unknown-member rejection, required non-null business dates, actual calendar validity, and action safety. A `safe:false` action must never become an enabled or safe UI action; reject the invalid form where the applicable contract requires rejection. Preserve legitimate dated responses, admitted undated/per-section prospect variants under IRPT-Y-DATES-01, and internal consumers. Do not broaden the date extension to unrelated operations or fabricate dates.

## Independent closure

P returns an exact paired source/portal pin, regenerated contracts and actual Entry response captures. CVO~P independently reruns its original four refusal cases and public schema/consumer controls. CVO~Y independently reruns the original Y-W01 and seven Y-W02 cases unchanged, retaining valid ordinary, extension, wrong-lane and malformed controls. Coordinate shared evidence but retain independent verdicts. Verify internal diagnostics retain correlation while public responses do not. Distinguish the exact pair from the assembled endpoint and test the final integration where changed.

R-P11/Y-W01 public-refusal acceptance and Y-W02 parser acceptance remain HOLD until independent closure. Previously bounded date, Y-DT01, owned-reopen and exact-package R-P10 results remain scoped to their tested candidates. No real-browser, runtime, vendor, render, deployment, push or integrated product acceptance is granted. All unrelated operational gates remain.
