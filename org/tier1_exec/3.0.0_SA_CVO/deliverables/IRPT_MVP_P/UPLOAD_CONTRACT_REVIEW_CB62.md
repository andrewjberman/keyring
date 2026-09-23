# Upload contract review: R-P09 open

Reviewer: `3.0.0_SA_CVO~P`, 2026-09-22. Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.

Backend pin: `5add22ca9fb36545d4ed0b857e17217644d10c98`.
Portal pin: `cb62721c6095c0d51e1e4ec52be9c44a88002a48`.

## R-P09 — P2: normalized input identity is not bound to the receipt hash

The browser `adaptAnalysisUpload` parser accepts a NORMALIZED response when both `input_id` and `input_ref.input_id` are changed together to `portfolio_` followed by 64 zeroes, while the actual portfolio document, `input_ref.content_sha256`, and immutable artifact receipt remain unchanged. The paired IDs agree with each other but identify different content from the receipt. `parseIrEnvelope('analysis-input-upload', body)` returns the mutated data without `EnvelopeMismatch`.

This is a concrete consumer validation gap. The actual pinned producer generates content-addressed portfolio IDs. The independent capture recomputed SHA-256 from `portfolio.canonical_bytes(document)` and verified all three producer invariants: `input_id == 'portfolio_' + sha`, `input_ref.content_sha256 == sha`, and `artifact_ref.sha256 == sha`. The captured hash is `2ec1ad0a9eea0141396d4350380e9c71ba892427dff991e93dc421307cee3fd3`. The negative control then changes only the two input IDs. Matching those IDs and separately matching the two hash fields does not bind identity to content.

Requested repair: enforce the producer's input-ID/content-hash invariant at the upload response boundary and retain the existing receipt checks. Rerun the unchanged independent case with both IDs altered together; require refusal while the regenerated valid producer response still parses. This review does not require browser-side canonical serialization or claim that this single comparison authenticates the whole document.

The route remains `NO-HANDLER-AT-HEAD`, and repeated LiveClient attempts refuse before transport. This is not evidence of an authenticated HTTP exploit, unauthorized blob read, deployed exposure, or a server-side ownership bypass. No implementation files were changed by this review.

## Reproduced evidence

| Check | Result |
| --- | --- |
| Supplied actual guarded producer schema tests | 8 PASS |
| Independent regeneration of NORMALIZED and NEEDS_CORRECTION responses, schema validation and canonical content hash assertions | PASS |
| Supplied browser upload, selection, coverage and resolver tests | 16 PASS |
| Independent browser controls | 10 PASS, 1 FAIL (R-P09) |

Passing independent controls cover regenerated producer/parser parity; complete route verb/path/status denominator parity; wrong artifact family, mutable receipt, null version, fractional length and source-upload mismatch refusal; correction responses refusing accepted references/documents; exact repeated request serialization with explicit superseding lineage; and unavailable-route refusal with zero transport calls. No standalone typecheck was rerun; the candidate's typecheck remains producer-reported.

`upload_contract_probe_cb62.py` creates separate exact-pin backend and portal snapshots and uses the existing local browser dependencies. `upload_receipt_cases.test.ts` contains the unchanged independent assertions. `upload_contract_probe_cb62.json` retains commands, outputs, source hashes and pin metadata. `upload_actual_5add.json` retains the independently regenerated producer responses and requests.

- Independent assertions SHA-256: `13ef33af34b8d20e806c0d8c25194a5158055d44a74f6ca20f2355bea543f5ea`.
- Regenerated capture SHA-256: `a06685ee8b910028ec794ffa18dd1498cdaf66c4aa19ea51b6b545b077bcd0a0`.
- Browser envelope source SHA-256: `89ff6b92f0fdfaed46d3546b1a9bdd814ed5bbbe77e84317ada687a9257a3c69`.
- Producer portfolio source SHA-256: `aa23e204e6641e00d66595ecf17ed256cbf85d4bbbe348c39db997fee0e1e2ac`.

Two initial reviewer snapshot attempts omitted `_keys`, then `data/firm_registry.json`. Both were corrected using the same backend pin before this result. Neither harness omission is a product finding. The final runner exits 1 solely because the R-P09 negative control is accepted.

## Boundaries and retained gates

The producer uses actual guarded upload code with supplied identity/storage doubles and the older bare artifact repository setup. It is not the retained upload runtime reviewed separately by Y. Browser checks exercise the parser/client boundary, not the mounted upload UI or an authenticated route. No queue, AWS/IAM, real provider, server-clock concurrency, deployment or full S7 proof is added. R-P08 remains boundedly closed at review `452f8d589f`; R-P07 remains closed within its prior scope. Broad P1-P8/S1-S7 acceptance remains NOT_EVALUATED.

Peer evidence is retained separately, with no counts added to this review: CVO~M reports publication review `c462d8b4df` on `62139c3a1a9792b41e02a8b66b612ad4571c6ab8`, explicitly excluding rollback guarantees after persisted final-index timeouts and suspended-versioning writes. CVO~Y reports Y-S01 closure `10b5b7f25c` on `b258b1696c` using acceptance mocks, with no real queue/recovery claim. Y's separate composition candidate `601e1c7bf1` and its test counts remain producer-attributed; integrated server-clock/Dynamo proof is still outstanding.
