# IRPT M -- status

Seat `2.0.0_SA_COO~M` (CODEX). IRPT contract v1.3:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
at `f0fcc4516c`. Reviewer: `1.0.0_SA_CTO`, per Andrew's direct assignment.
Current sequencing: CTO ruling batch `5edf991c06`, message `20260923T165545Z`.
Controlling access correction: `IRPT-OPAL-FULL-ACCESS-20260923` at `5ad99c7d30`.
Verified Opal users may use every IRPT function across firms, including prospect
uploads, other-owner reports, history and exports. Global/firm selection filters
inputs and views; it is not an Opal permission ceiling. Preserve actor identity,
exact selection, per-input firm/account/source attribution and audit history.
Ordinary firm-user restrictions and forged-Opal refusals remain. Missing workflow
capability must not be presented as a valid Opal user's permission denial.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m` |
| Source candidate | `200ba442f5`, docstring correction on runtime `3539ad2ae5` |
| Publication review | CTO `bb43292167`: bounded source PASS; unchanged 99 tests in isolated candidate archive |
| COT local validator | `b3e63a795e0b8c7399619dbc545745786add4eb7`; CTO `1ada74ee5c`, 114 offline tests |
| Paired field review | M `ae99df9169`, Y `605449f4cc`; P retained-selection draft `75bbe9cc2d` |
| Portal / deployed candidate | P-owned; no M deployment or new live measurement |
| Push state | LOCAL; no push by M |

## Live thread

State: NOT LIVE according to the current sequencing ruling; M has no new live
trace. P owns the next active proof at current localhost5174: real login ->
auth/scope/bootstrap -> real firm/investor data -> screen. P must record the exact
served revisions and sanitized first failing boundary. M does not infer that
boundary from offline custody tests or take over P's shared surfaces.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| S1-S7 | No product acceptance claimed by M | Offline passes close no acceptance ID before the live thread |
| Publication-history seam | Bounded offline PASS, not live acceptance | Runtime `3539ad2ae5`, wording `200ba442f5`, CTO review `bb43292167` |
| Local COT source controls | Bounded offline PASS, not custody admission | `b3e63a795e`, CTO `1ada74ee5c` |

## Write claims

No implementation is active. Completed publication/snapshot work is confined to
`infra/aws/lambda/investor-reporting/holdings/publication.py`, `snapshot.py`,
`tests/test_publication.py` and `tests/test_snapshot.py` under CTO `999998e448`.
Earlier source-validator scope remains preserved. This status update does not
acquire auth/scope/bootstrap, browser, shared schema, package or binding-store
ownership from P. No running atomic work remains to checkpoint.

## Next proof

Support only a concrete first-hop dependency identified by P's live trace.
Once one names an M-owned boundary, use its exact failing input/revision to prove
and repair that boundary within the admitted scope. Until then, deeper custody
source/package implementation and review remain parked; do not rerun passed
suites or circulate field-name drafts.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Exact first-hop dependency, if M is needed | COO~P | Current live trace and served revisions under `5edf991c06` | AWAITED |
| Exact dependent M data/selection change for full Opal access | COO~P shared authorization/UI/API owner | `5ad99c7d30`; no specific M implementation delta supplied yet | AWAITED; no takeover of shared ownership |
| Private publication integration | COO~P | `capture` / `load_pinned`, `3539ad2ae5` plus `200ba442f5` correction | HANDED OFF; deeper review PARKED |
| Direct review | CTO | `bb43292167` bounded publication PASS | CONSUMED; no new CVO wait |

## Parked

| Question / work | Owner | Un-parks when |
|---|---|---|
| Deeper custody source/package review, including candidate `155213fedf` named in CTO ruling (not independently reviewed by M) | P integration; CTO reviewer; M/Y owned support | First hop is live, or a trace names this as a necessary first-hop dependency |
| Missing source currency/sign/unit/cash/accrual, canonical mapping and numeric receipts; complete empty-account census | M source capability, P binding, Y consumer, CTO interpretation rulings | Same sequencing condition plus exact admitted source scope/evidence |

## Limits

Capture/replay proves exact publication history, not actual custody. The receipt
pins historical index VersionId/length/hash and exact date row/manifest; replay
has no current-date fallback. Original full snapshot revision stays distinct
from selected/decorated bytes. A failed index readback can follow a successful
conditional write: reconcile the exact version before retry; no rollback is
implied. Tests are synthetic offline evidence, not fresh source receipts.

Current authority, source economics, integrated admission and live journey remain
unproved by M's pins. No cloud read/write, producer invocation, new IAM, vendor
call, activation, promotion or deployment follows from the hold lift. Existing
gates remain. CRO message `20260923T165608Z` changes backend-only thread guidance
and explicitly does not change frontend-bearing IRPT.
The Opal access correction authorizes the coordinated implementation, not deployed
behavior or cross-firm economic aggregation by inference. Per-firm publication
receipt identity remains a data-attribution check, not an actor-home permission
rule. CLOUD push remains held under MSTR's `8a5c01207d` relay.
