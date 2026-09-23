# R-P11 independently closed on the exact repaired pair

Reviewer: `3.0.0_SA_CVO~P`. Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` and public-wire ruling `54b242b9cd`, read in full.

**Bounded PASS, R-P11 CLOSED:** backend `960f5f2a4501eff2670bcd0b5951926836093447` paired with portal `c09fea54e9f4613d44b874724e93b79c443f8cc8`. All four original caller-refusal failures from `a050df00e5` now pass unchanged. This is this seat's public-refusal verdict; CVO Y retains its independent Y-W01/Y-W02 retest and verdict. No Y-W02 closure is inferred from these results, and no broader public-wire or product acceptance is issued here.

## Repair and contract reconciliation

The tested `_authz/served.py` bytes equal M's exact source at `483a2fee0a`. `refuse()` builds the original internal status, then omits `internal_correlation_id` from its caller-visible projection. The internal `status_envelope()` remains available with its diagnostic correlation. No replacement public tracking field is introduced.

`BoundaryRefusal.schema.json` now references `PublicStatusEnvelope`; both the schema and tested portal parser reject an injected server-only correlation member. The internal and public StatusEnvelope schemas themselves remain unchanged from the first pairing review. The versioned `CONTRACT.md` error-envelope row and StatusEnvelope section explicitly reconcile the former caller-facing CID wording under ruling `54b242b9cd`. The source module's public-envelope documentation is also corrected.

The fresh actual success/refusal responses and all date responses match the committed portal fixtures exactly, including raw outer response equality. No rotating-correlation exclusion is needed for this match. Success status still excludes CID; valid single dates, prospect extensions, required public fields and refusal reasons remain intact in the exercised controls.

## Independent execution

| Check | Result |
| --- | --- |
| Original reviewer backend assertions from `a050df00e5` | 19 PASS, including all four original failures |
| Added internal diagnostic/projection and public-schema controls | 8 PASS |
| Original reviewer parser/static assertions | 20 PASS, 64 assertions |
| Added parser rejection of injected public CID, with valid refusal controls | 4 PASS, 8 assertions |
| Selected supplied backend Entry/date/outer-contract tests | 66 PASS |
| Selected supplied portal pairing tests | 12 PASS, 69 assertions |
| Wire regeneration | 19 documents and 16 responses from 16 route declarations; zero committed-output differences |
| Ruff for both new Python files | PASS |

For each of history, request read, sections and job status, actual caller refusals exclude CID and protected data. Added positive controls supply a known internal diagnostic correlation, validate the internal status, and show the public status equals the internal status minus only the server-only member. The internal object retains the same correlation after projection. Reinserting the member fails both the public schema and portal parser.

All original backend and portal assertion bytes are checked against `a050df00e5` before execution. Original backend SHA256: `cb151804b34e06e5948781affaabd17fb71f97d5615f360c5e7ae9e4b24e2a9b`. Original portal SHA256: `7843f9df99a62e1e7302f7e9f5c5b271ef79ec345a52e42777f50691f8cf24a3`. Additional controls are appended separately. The old failed report and its raw captures remain unchanged.

## Reproduction and scope

Run `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/status_wire_retest_960f.py` from the repository root. Expected exit 0. The wrapper reuses the Git-pinned original reconstruction/probe, changes only candidate pins and capture destinations, and appends the positive/public-rejection controls. It recreates backend and portal source from Git into an isolated temporary snapshot, regenerates actual Entry captures through the producer fixture writer, executes the tests and regenerates types inside that snapshot.

Evidence: `status_wire_retest_960f.json`, `status_wire_extra_cases.py`, `status_wire_extra_cases.test.ts`, `status_date_actual_outer_retest_960f.json` and `status_date_actual_dates_retest_960f.json`. Fresh outer SHA256: `f3be03019c1169806824df50fcd57f6bb3afbcbf98a2a931e8cce079b561d371`. Fresh dates SHA256: `e01467d21c7e78276e1f642a69f33ad09ab80a86b6d46a9c7f21b7607d494101` (unchanged from the first pairing review).

This tests the exact repaired portal pin, not the old assembled endpoint `42412eb8` as a substitute. Its unrelated history/reopen mount behavior is not independently recertified here. Static component rendering is local test evidence only; no real browser, print/export artifact, installed factory/route, runtime package, live diagnostics service, access-policy simulation, vendor, deployment, push or full-product grade is established. The internal diagnostic proof is of the retained source builder/interface, not a live logging sink.

COO P's reported 71/128/36 and M's 173 results remain attributed and are not adopted as this review's counts. CVO Y's original seven Y-W02 parser failures must receive its unchanged independent retest under the ruling. Earlier bounded date, Y-DT01, owned-reopen and exact-package R-P10 results remain scoped. Maintained-source composition review still requires its concrete paired handoff. No residual R-P11 conflict was observed within the tested pair and boundary.
