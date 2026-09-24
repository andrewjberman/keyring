# Direct CTO W1 broker review

Source4173322f457aeeb390033b410e85bebadc49a3e3, parent5609c2e46a; Y handoff92fbf25c76. Date2026-09-23. Reviewer1.0.0_SA_CTO.

Fresh git archive direct replay:54 session tests PASS, no skips. Separate run_session_suite.py: c_rotation/d_eviction/controls/netguard_positive_control/all_pass all true. Exact FirmDestinationPolicy extracted from b475b96309c0034b513f19393138984d05716d0e:infra/aws/terraform/investor-reporting/core/firm_destination_policy.json. Network guard rejected its deliberate external connection control; no successful vendor egress. Generation/intake full suites were not rerun. Original generic401 fixture was explicitly changed to recognized signed-out body; negative generic HTML controls remain.

Bounded improvement confirmed: actual broker-owned reply observer, no fabricated status-only reply and no job-reported decision authorizing refresh. Unknown401/403, WAF, entitlement and mutation failures do not admit refresh; one-refresh/real GenerationJob checkpoint regression passes. No raw bodies retained by observer. This does not establish installed caller coverage or full W1 closure.

## CTO-Y-W1-CORRELATION-01 OPEN

Additional synthetic boundary probe uses actual run_with_recovery and ReplayTransport with a small job adapter. The application read returns401 and the recognized SIGNED_OUT body; an unrelated diagnostic probe then returns200 JSON; job still returns APPLICATION_READ_FAILED. Broker returns NOT_AN_EVICTION with no refresh, retaining only the healthy probe classification. This violates existing078349 rule that a healthy probe cannot override a failed application endpoint. It is a source boundary reproduction, not evidence that the deployed GenerationJob currently issues this diagnostic sequence.

The latest-request-only observer loses causal failure evidence. Repair must bind the failure to an actual broker-observed request/attempt, not keep arbitrary old eviction state. Preserve mutation reconciliation, unknown-body refusal, later contract-failure and exception controls; add a negative case where unrelated old eviction cannot authorize refresh for a later failure. No raw body or secret retention. Y received bounded local repair request193152 under existing mandate.

Reproduce: extract exact source and policy into a scratch root; set IRPT_CTO_REVIEW_SOURCE_ROOT to that root and run failure_correlation_probe.py. This evidence probe asserts the original defect; it is not the future acceptance test. Output saved in failure-correlation.json. All fixture replies are offline.

Remaining separate gates: shared account operation lease for all consumers, actual hard-deadline transport, durable D2 interpreter, installed recovery and live proof. Kimi deadline source closure remains separately pinned at5609c2e46a/df23c8e35a. No cloud mutation/login/vendor/host action authorized by this review.
