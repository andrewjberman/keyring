# CTO-Y-KIMI-DEADLINE-01: bounded source closure

Direct reviewer: 1.0.0_SA_CTO, 2026-09-23.
Source5609c2e46a2d36716743f21a8e6a5eec6876e5d8, parent6cfe01c3e238e9a90e88d3a501b25ac0eaf41540. Y handoffc0867388b4. Reviewed both-file diff: resolution_kimi.py and its focused tests.

PASS/CLOSED at this source pin for the reported total-budget reset and late-success defect. One monotonic deadline now starts at call entry and is checked across preparation, pre/post telemetry, attempts and parsing; transport receives remaining time immediately before send. Exhaustion prevents send/retry and late acceptance.

Fresh archived source replay: focused43 passed; full intake190 passed+18subtests, no skips. Focused43 is included in intake190, not additive. Prior fixture-pinned paired dependencies and exact CRO lookup fixtures reused from the7c8484466c review. Generation/session code unchanged; no new replay or aggregate claim for those suites.

Independent CTO retest reused the prior committed ctoreview_deadline_probe.py fake-clock scenario unchanged (119s HTTP503 followed by119s valid response), replacing only its expected-defect assertion with closure assertions and pointing it to the new archived source. The retry timeout arguments are[120,1], overall result null with KIMI_TIMEOUT, original finding_reproduced false. Saved cto-retest.json identifies the actual repaired source pin; the reused probe initially printed its old embedded source label, corrected before evidence persistence. No network calls.

The deliberately noncompliant fake transport still consumes238 simulated seconds. This demonstrates refusal of late success and correct remaining-time argument, not interruption of blocked callbacks. Installed send must enforce actual remaining wall time; telemetry/callback blocking and operation-level final status remain runtime concerns. AFTER_CALL may record an OK attempt before slow telemetry causes overall timeout; consumers must use the overall result.

Existing local integration may consume this exact repair. No live QA/deploy/session/login authority or full upload-resolution acceptance follows. W1 legacy status-only eviction fallback, durable runtime wiring, canonical dated-price facade and user workflow remain open under existing assignments. CTO is the reviewer.
