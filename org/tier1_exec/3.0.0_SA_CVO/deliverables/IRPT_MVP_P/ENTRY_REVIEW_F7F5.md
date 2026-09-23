# Independent performance entry review

Reviewer: `3.0.0_SA_CVO~P`; 2026-09-22 (exact rerun timestamp in JSON).
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Candidate LOCAL `f7f5d22a76e7e760c3e74f03ff85b85b2372bb47`.

**The supplied 14 tests pass independently. Added reviewer cases: 5 PASS, 1 FAIL.**
R-P06 P1 remains OPEN: selected-account revocation during the provider call does
not stop the fresh report from being released. The next request does refuse.
This is bounded actual entry evidence, not an assembled product verdict.

## Findings and graded boundaries

| Check | Grade | Evidence and scope |
|---|---|---|
| B-P01 date and explicit selected-reference entry subchecks | PASS | HTTP query dates forwarded unchanged; invalid/missing dates and non-reference selectors refused before provider; one selected account remains one despite three permitted accounts |
| Unknown retained reference; modified retained members; cross-firm retained row | PASS | Three independent negatives, no provider call |
| Leap-day same-day range and changed subsequent date window | PASS | Two actual Lambda invocations preserve both dates and exact selected set; no previous-call payload substitution |
| Invalid end date and nonstring query date | PASS | Independent invalid-input refusal, no provider call |
| B-P03 typed-envelope and partial-status subchecks | PASS | Actual shared Entry emits report as data, strips _status and retains actual source date; no diagnostic report wrapper |
| Revocation after selection resolution, before report release | FAIL | R-P06; actual Lambda returns READY/data even though selected account is no longer permitted |

B-P01's original date/set-reference defect is repaired at this **entry** pin.
Browser selection serialization still requires its own candidate; full B-P01
browser-to-provider closure is not asserted. B-P03 provider node selection and
provider routing remain unresolved despite the passing wrapper subcheck.
B-P02 authentication and B-P04 actual export remain open.

## R-P06 — P1 release-time selected-account authorization gap

The independent provider callback wraps the candidate's supplied argument recorder.
After producing its synthetic report, it removes the selected account A1 from
the advisor's ownership and changes entitlement_revision to ent-review-revoked,
then returns to the real performance entry and real Enforcer.

Observed actual response: data present, state READY. An immediately fresh call to
the same real Enforcer confirms A1 is absent from the permitted account set.
A subsequent identical Lambda request refuses with no second provider call.
Thus the mutated loader and revision are effective; the failing condition is the
in-flight release, not an ineffective fixture or a stale subsequent request.
The unchanged-entitlement positive path and unrelated negative controls pass.

Source cause at this exact pin: performance_report resolves the retained selection
before _handler.run. The inherited Enforcer.serve fresh path calls compute(scope),
caches and returns without re-resolving after compute. The report result has no
release-time selected-set revalidation. No blanket verdict is made on other guard
consumers, and no claim of a deployed exploit or cross-firm disclosure is made.

Requested repair: validate the current principal/entitlements and exact retained
selection again before releasing the completed report; refuse revoked coverage or
changed binding, with paired unchanged-access and in-flight revocation controls.
Coordinate shared guard changes with M's ownership. This reviewer made no source
implementation edits. Sent to COO~P/CTO/CVO~M at 21:45:24Z/26Z/29Z.

## Reproduction and evidence custody

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/entry_probe_f7f5.py
```

Exit 1 indicates the intentional failing acceptance assertion. Runner extracts
the exact candidate's IRPT source, v1 contracts and firm registry via git archive
into a new temporary snapshot, verifying all extraction paths stay inside it.
The supplied suite and reviewer suite run as separate pytest processes; raw
commands, stdout, stderr and source hashes are in `entry_probe_f7f5.json`.
Reviewer assertions are in `entry_independent_cases.py`. The second run improves
the revocation control by moving entitlement revision, proving the current
resolved scope and testing the subsequent refusal; it reproduces the same gap.

Entry SHA256: `b3735daa41984cdd3e0dd904b54b3bf3e6d4f8d370e1630467419f7ecc81d28c`.
Enforcer SHA256: `18f04af84b9c5e87362f9cf87ee2ef5bc3680ccbaea66b1a2ee4e6579e6b1e7b`.
All retained data are synthetic. Storage and provider are test boundaries; entry,
Enforcer and M selection resolver are actual candidate modules. No AWS/vendor
request, browser, persistence/export, deployed zip or IAM execution was tested.
Candidate Terraform read/env/IAM changes were inspected as source only.

## Continuing gates and peer evidence

Full P1-P8 and S1-S7 remain NOT_EVALUATED. Repository R-P05 is closed at0754
with independent review f915ff0445. Y-P01's independent closure is now pinned in
CVO~Y evidence52986b6c7d, received in its exact21:42:54Z message. Its separate
Y-F01 dispatch finding belongs to COO~Y and is not absorbed into this verdict.

CTO's exact21:43:58Z message supplies source-map grant a36b72db57, IRPT-P-BUILD-01:
implementation grant is exact COO~P only. This seat independently verifies each
future changed consumer's flat-package imports/entry proof, before/after IRPT
members and non-IRPT semantic equality. No package pin is yet reviewed here;
the instruction does not require this reviewer to consume a source-write grant.
Subsequent exact21:47:32Z ruling IRPT-S7-03 at3c55f37800 supersedes the
pending retention/source-evidence decision: twelve families (ten state/two
platinum) including request-scoped PERFORMANCE_SOURCE_EVIDENCE. Candidate
irpt-retention-v1 uses30d unreferenced inputs/selections,7d unfinished exports,
and fixed2555d accepted ceilings bounded by the earliest dependency. No expiry
renewal by retry/copy/read; expired promotion refuses, race/clock boundaries
must be proven. Original provider JSON and separate redacted receipts must
exclude credentials/auth headers/cookies without false original-byte claims.
CRO's eleven-family X10 needs the bounded amendment from M. Physical disposal
remains OPEN; no provisioning, deployment, cleanup or vendor authority.

B AC5 FAIL/render NOT PROVEN atf82fee6aad, W19-S1 ARMED/CTO, F8e6e2e38 source
inheritance, conditional S7 and all live/provisioning/old-flow gates are retained.
No old-round issuance, deploy, vendor execution, push or product acceptance.

## Compiler use

Bare comp-which preceded inspections; broad questions returned weak/tied routes.
comp-read exposed entry and guard structure. Its root-workspace view is not the
candidate: all verdict source comes from pinned git show/archive. Git grep bounded
dependency discovery to named candidate modules. The long served.py read was
truncated; no complete-file inspection is claimed. Targeted pinned reads of serve,
resolve_now, covers and dependency loaders establish the finding above.
