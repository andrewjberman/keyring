# Final paired consumer and access-restriction review

Reviewer: 3.0.0_SA_CVO~P.

Authority: org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md. Exact CTO notices 20260923T043906Z and 20260923T045329Z; latter reports supersession 9ab944db82 and Andrew handling visual smoke. Exact P command handoff 20260923T045434Z. This is the already-requested bounded review, not a separate publication approval gate. MSTR retains publication ownership.

**Bounded PASS on portal `a538217980cdb5d15dc67cdcc98794baeb5e2517` paired with backend `cd8d11825424e45fe82f1e78df0396904c0b9ae0`. No concrete defect reproduced within the focused consumer/access checks.** No visual, live-runtime, full-product or backend render/key acceptance is asserted.

## Executed evidence

`final_consumer_probe_a538.py` creates isolated detached worktrees at the exact commits, materializes the backend contract directory and supplies explicit `IRPT_WORKSPACE_ROOT` and `IRPT_CONTRACTS_DIR`. The backend census reads this detached backend's committed blobs, not a moving workspace HEAD. The portal's gate-test carrier modules are clean before the supplied test and remain clean afterwards. Dependencies use the existing node_modules junction; no installation or network call is needed.

| Focused check supplied by P, independently rerun | Result |
| --- | --- |
| fe-s-49 admin gate, fe-s-88 prior render delegate, mvp-selection, mvp-upload, selectionRequest, submission-request, fe-s-15 composer | 64 PASS, 290 assertions, 13 files |
| Affected analysis tests: owned reopening, prospect submission, recipient | 16 PASS, 87 assertions, 3 files |
| Reviewer Python Ruff | PASS |

Full commands/output and source comparison hashes are retained in `final_consumer_probe_a538.json`. Run `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/final_consumer_probe_a538.py` to reproduce. P's separate full lint/typecheck/build passes and mounted race runs are reported in its handoff; they were not rerun or claimed as independent browser evidence here.

## Access and integration observations

- The actual committed ProtectedRoute component is evaluated through React static rendering, and the committed navigation filter is lifted unchanged by the supplied TypeScript-parser harness. Opal internal Dev admin reaches both page and print routes. Three partner-firm admins refuse on both routes (6/6). Non-admin and internal non-Dev identities refuse (10/10 checks). Navigation shows the entry only to the internal Dev admin (1/9 identities). Both routes and the one navigation entry carry all three human-access limbs.
- The existing `allowRenderClaim` opt-in remains on exactly one route, `/investor-reporting/print`. Its synthetic claim admission and malformed/wrong-role/wrong-audience refusal controls pass. Non-opted-in routes do not gain admission from that claim. This client decoder is explicitly not a signature verifier; preserving it is not approval of backend render/key readiness or evidence of live edge validation.
- Against merged remote DEV parent `b3d5f59b4534eb653105f9bedc9e178384111c9f`, 58 of 59 selected SecurityAnalysis/MFA/auth/firm-access files are byte-identical. The sole difference is ProtectedRoute, which adds the already-sanctioned render delegate from the IRPT parent. ProtectedRoute is byte-identical to IRPT parent `7a5b24e705f79d5df872f9a443b6a552e9de62b9`; direct diff inspection confirms the human-access checks stay intact. The 59-path comparison is an explicit bounded source inventory, not a claim that every merged file is identical.
- Focused consumers preserve issued IDs and original dates, reject public/private-field and upload-receipt mismatches, refuse pending live adapters before transport, retain comparison ordering and recipient values, and check owned reopening without resubmitting. Recipient changes alter custody composition identity; exact retries retain it. Static initial UI checks do not establish actual browser effects or server integration.

## Limits retained

The 16-route backend census is a source inventory. It includes UNKNOWN classifications for unbound/undeclared handlers and does not certify a universal backend admin-only policy. Frontend access restriction is distinct from current backend authorization and deployment configuration; no backend authorization regression was established by these passing tests.

Preview and actual browser work remain stopped per Andrew's superseding instruction. No render/vendor call, deployment, push, publication operation or new approval gate was performed. Existing backend render/key, legacy-read and full-product gates remain separate; all 14 broader completion criteria remain NOT_EVALUATED. No prior exact-pair closure is silently generalized to this head beyond the focused checks recorded here.
