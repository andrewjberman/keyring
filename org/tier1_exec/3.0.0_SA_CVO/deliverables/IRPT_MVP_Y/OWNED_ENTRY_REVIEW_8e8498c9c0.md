# Owned Entry factory: bounded independent review

Reviewer: `3.0.0_SA_CVO~Y`, September 22, 2026 evening.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact candidate: `8e8498c9c08a37fb162656496d7bc8d98f00cfb6`.
Exact COO~Y notice: `20260923T003050Z_2.0.0_SA_COO_Y_IRPT_Y__owned_Entry_factory8e8498c9c0_re.md`.

**Bounded PASS: 28 supplied tests and 42 independent controls.** This is the
actual factory/event/Entry with actual owned request, report and status readers,
actual retained repositories, and offline storage/clock/policy fixtures. It is
not acceptance of the public generated contracts or runtime installation.
All 14 integrated Y1-Y7/S1-S7 criteria remain **NOT_EVALUATED**.

## Evidence and reproduction

`probe_owned_entry.py` archives the exact source, contract and fixture files into
the ignored exact-seat runtime directory, hashes every file, disables Python
socket connections, runs independent controls and the candidate's
`ops/tests/test_owned_entry.py`. `OWNED_ENTRY_8e8498c9c0.json` preserves results,
responses, hashes and supplied test output. Run from repository root:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_owned_entry.py --pin 8e8498c9c0 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/OWNED_ENTRY_8e8498c9c0.json
```

No implementation file was edited. The synthetic schema-valid report carries
fixture certification fields; this does not establish actual extraction,
certification, vendor publication or released-report provenance.

## Independently measured boundaries

- Four actual events return the expected bounded data. History and issued
  request project immutable identity/time; sections match the exact closed
  analysis-report **data** schema and exclude vendor artifact/disclosures/release.
  The outer firm is opaque. This is not a complete outer response schema PASS.
- All eleven durable phases map as expected: RECEIVED to QUEUED; six active
  phases to RUNNING; FAILED to FAILED; UNCERTAIN, ATTENTION and READY to
  UNAVAILABLE. Only queued/running offer safe WAIT. No business/source date is
  invented; source_dates is empty; public status data excludes internal CID.
- READY invokes the actual accepted-report reader once, then returns
  ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE. Other phases do not invoke it. Unknown
  and empty states refuse. This neither emits nor accepts the new date basis.
- Sections and status refuse numeric READY receipt corruption before report
  fetch, composition expiry after report bytes, and current authorization loss
  after report bytes. These exercise Y-R01's repair through the factory.
- All four operations refuse when the actual Entry request claims change after
  compute. Issued request/sections also refuse full retained-owner change after
  the service returns. Their record authorizer, and status's, also refuse a
  separately changed authorization fixture.
- Unexpected queries on the three issued-ID routes refuse before job/blob
  reads. Unsupported contract version on all four routes refuses before query,
  job or blob work. Another principal receives an empty history page.
- Legacy status-summary retains its existing operation/guard; module ENTRY and
  lambda_handler remain the old assembly. Calling build_owned_entry does not
  install routes or activate a new runtime handler.

## Preserved limits and integration obligations

The initial independent run recorded 38 PASS / 1 FAIL. Its history assertion
changed `case.headers` after the history service returned and expected Entry to
refuse. The test helper had copied those headers into the event; Entry's actual
request claims were unchanged. History Entry deliberately has no single
retained-record authorization callback; history's service owns filtering and
per-item final checks. Thus that assertion did not establish a principal-change
defect. The initial JSON is preserved as `OWNED_ENTRY_8e8498c9c0_INITIAL.json`.
The final probe retains the returned-data observation separately and adds four
actual Entry-claim mutations, all refused. It does **not** claim atomic checks,
an extra post-service history authorization pass, or server revocation beyond
the supplied authorization port. Earlier service checks remain bounded by
`OWNED_REQUESTS_REVIEW_e93300e34b.md` and its evidence.

Raw checked-in response schema observations remain unresolved for integration:
both actual sections and status outer responses contain `unprojected_grant`,
which those closed schemas reject. The raw StatusEnvelope additionally requires
`internal_correlation_id`, correctly absent from this public status data.
The probe substitutes only the local data schema and the already-valid firm
property to avoid remote reference retrieval. These are concrete mismatches
against those source schemas, **not** a validation of a generated public schema
or an instruction to expose the server-only correlation ID. P must pair the
actual factory response with its agreed public schema/type/parser and exercise
positive and refusal wires. New history/read routes also need their published
contracts and factory installation. No claim of a newly introduced schema
regression is made against this explicitly uninstalled factory.

Date derivation/compatibility remains subject to IRPT-Y-DATES-01 @dea338a397 and
the paired review plan. No real HTTP, flat package import, Terraform/IAM,
browser/reload, live retained service, vendor session, policy activation or
deployment was exercised. There is no integrated acceptance lift.

Compiler routing was used before inspection. One broad comp-which fallback
timed out at its 90-second budget; exact pinned files were then read directly.
Main-tree zero hits were not treated as absence from this alternate source pin.
Push state LOCAL; no push by this seat.
