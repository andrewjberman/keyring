# R-P09: independently closed at the browser response boundary

Reviewer: `3.0.0_SA_CVO~P`, 2026-09-22.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Original finding: review `fb0f801529`, portal `cb62721c6095c0d51e1e4ec52be9c44a88002a48`.
Replacement portal: `c86a5eb53df6e48906def496df2d4dcdc0f47404`.
Unchanged backend: `5add22ca9fb36545d4ed0b857e17217644d10c98`.

The shared upload adapter now requires `input_id === 'portfolio_' + input_ref.content_sha256` in addition to the existing paired-ID and artifact receipt checks. The original negative control, which changes both input IDs together while retaining the actual content and receipt hashes, now throws `EnvelopeMismatch`. R-P09 is closed for this precise consumer validation defect.

The independently regenerated actual guarded producer NORMALIZED and NEEDS_CORRECTION responses pass the pinned schemas and browser parser. Canonical-byte hashing again confirms the input ID, content hash and artifact hash agree. All 35 tests pass: 8 supplied producer schema tests, 16 supplied browser tests, and all 11 unchanged independent assertions. The original finding changed from 10 PASS / 1 FAIL to 11 PASS / 0 FAIL. The supplied regression adds an assertion within an existing test, not an additional test count.

The remaining receipt-refusal controls, correction-state constraints, complete route denominator parity, repeat-request serialization and explicit superseding lineage still pass. Repeated LiveClient requests to the unavailable route make zero transport calls. No fixture expectation or independent test was changed to obtain closure.

`upload_contract_retest_c86a.py` executes the original runner from commit `fb0f801529`, replacing only the portal pin and output capture filename. It asserts the unchanged independent test file SHA-256 `13ef33af34b8d20e806c0d8c25194a5158055d44a74f6ca20f2355bea543f5ea`. The original evidence remains intact. `upload_contract_retest_c86a.json` records all commands/results and pinned source hashes; `upload_actual_retest_c86a.json` records the fresh producer capture. Its SHA-256 `a06685ee8b910028ec794ffa18dd1498cdaf66c4aa19ea51b6b545b077bcd0a0` is identical to the original independently generated capture. Replacement envelope SHA-256: `774f1a72745ead7c9124809500ec14952495418a49dfa9577eb16316e3e5c586`. Ruff passes for the retest wrapper.

This closes the cross-field content-address binding gap, not general document authenticity or the full upload workflow. The producer uses supplied owner/storage doubles and the older bare artifact repository setup. The route remains `NO-HANDLER-AT-HEAD`. No authenticated HTTP, mounted upload UI, retained runtime, queue, provider, server-clock, deployed IAM, layer or full S7 proof is added. Project typecheck remains producer-reported. Broader P1-P8/S1-S7 gates remain NOT_EVALUATED. R-P07 and R-P08 retain their prior bounded closures.

Separate peer evidence: CVO~Y review `b43fba4bd38bd8e89239e1f2c2be6be629271c9b` reports local canonical security identity checks on `d99a072742`; actual M resolver, vendor upload/readback and maintained browser/runtime integration remain pending. No peer counts are included in this retest.
