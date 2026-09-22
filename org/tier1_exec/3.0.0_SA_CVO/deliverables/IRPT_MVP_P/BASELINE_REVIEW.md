# Performance baseline: four confirmed connection gaps

**archetype:** VALIDATE

Reviewer `3.0.0_SA_CVO~P`, September 22, 2026, 4:51 PM Eastern.
Source baseline and scope are in ACCEPTANCE_MATRIX.md. These findings corroborate parts
of CRO's brief against source; they are not new deployment observations or a verdict on
the COO's future candidate. No implementation edited.

| Finding / priority / owner | Observed evidence | Required candidate correction |
|---|---|---|
| B-P01 / P1 / COO~P with COO~M selection seam | Exact performance entry functions discard browser query dates, treat SET-EXAMPLE as one account ID, and default absent selection to all permitted accounts. `baseline_probe.json` records three cases and a passing internal-carrier positive control. | Parse the actual browser event and resolve the selected-set reference server-side. Refuse missing/ambiguous selection rather than broadening silently. Repeat through the full guarded HTTP boundary. |
| B-P02 / P1 / COO~P | `performance/transport.py:LiveTransport.request` performs POST with JSON and timeout only, no authentication/session acquisition. `handler.py:run` gates every mode on RECORDED_LABELS. | Authenticated provider-specific requests with explicit live routing independent of fixture labels, dated scope/body and bounded refresh; verify deployed imports. |
| B-P03 / P1 / COO~P | `handler.py:run` chooses `result.nodes[0]`, sends every non-BD route to Orion and returns a diagnostic wrapper containing `report`. The guarded entry returns that result unchanged. | Explicit SmartX dispatch; identity-selected primary; declared HTTP report/availability shape paired with actual frontend adapter. |
| B-P04 / P1 / COO~P | `export/entry.py:submit_export` unconditionally raises `_ExportNotWiredHere`, reason NOT_READY, and never calls controller. | Connect the real controller after reconciling B/F source claims and R18-e prerequisite, then prove the same-revision artifact/receipt/download chain. |

Grounding: SOURCE-CONFIRMED for B-P02 through B-P04 by the named executable functions.
B-P01 is additionally EXERCISED at the two-function boundary: AST extracts the unchanged
functions; the downstream runner is an argument recorder. The test does not import or
execute the full authorization wrapper, HTTP server or provider. It establishes argument
translation behavior, not a live access leak or a complete browser journey.

Frontend source corroboration: `portal/src/api/endpoints/investor-reporting.ts`,
`LiveClient.getPerformanceReport`, sends `accountSetId=req.scopeFingerprint` and query
`start/end`. Its optional accountIds field is not sent by that method. Probe inputs use
synthetic account IDs only. Probe rc=0 means the regression signatures and positive
control reproduced; it does NOT mean product PASS.

## Exact source hashes (SHA256)

| File | Hash |
|---|---|
| performance/entry.py | f1db39ce6f44e5de92348e97020fbd93fe4b90276ee9c46bfe8eca156a7db2b4 |
| performance/handler.py | 9d6098dcc13471954b2e695e7ee7e6c745450f3e48c1c5b807fb85d49cc01f38 |
| performance/transport.py | 52abf66933e29747000611c41b02a3a1fb9ecfaa78c483c7a1c89620fae048ec |
| export/entry.py | 457f5d3faa1c2640d242d5e2779f8f1db34af7446ce28d2725e9d629bbd37814 |
| portal/src/api/endpoints/investor-reporting.ts | 31c57c9c94cf77192121458951f21b176fc2c696be7c5c3248fa5b08993271e1 |

Backend paths above are relative to `infra/aws/lambda/investor-reporting/`.
Reproduce: `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/baseline_probe.py`.
Candidate fixes receive independent retests at their own pinned bytes.

## What you should have asked but did not

An internal fixture can pass precisely because it supplies top-level dates and account
IDs that the browser never sends. Keep that internal case as a positive control, but
grade the actual browser serialization and deployed event shape separately.

-- 3.0.0_SA_CVO~P
