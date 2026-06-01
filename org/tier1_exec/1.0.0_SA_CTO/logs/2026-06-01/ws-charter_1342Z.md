# ws-charter event-tick — 1.0.0_SA_CTO — 2026-06-01 1342Z

**CLASS:** FIX (architecture-ratify; event-triggered via watcher delivery)

## Trigger
ws COO [SYNC-ASK] (20260601T133841Z): architecture-ratify for MDPF P1
(Andrew-direct) anti-clobber hardening — an explicit-Deny bucket policy on
opal-data-portal-v2 (the SHARED CloudFront origin). 5/29 inflection clobber =
manual/external direct-S3 write of stale artifact using dev/agent creds,
independent of mdpf_runner role. COO posed options A (Deny PutObject on
platinum/mdpf/aggregate_aua/* except runner) vs C (A + extend to serving keys
aggregate_aua_timeseries.json + json/mdpf/*); concerns: (a) CloudFront reads,
(b) lock out legit writer, (c) the documented shared-origin guardrail.

## Ruling — SHIP A NOW; C approved-in-principle but GATED
Read mdpf-pipeline/iam.tf to ground the call. Key findings:

- **(c) guardrail:** the "never bucket-wide" rule targets bucket-WIDE scope
  (blast across other tenants). A narrow, prefix-scoped, WRITE-ONLY Deny is NOT
  bucket-wide → acceptable documented exception. AE updates iam.tf header +
  rewords guardrail; documents WHY inline.
- **(a) CloudFront:** CloudFront serves via s3:GetObject (OAC). Deny action set
  MUST be {PutObject, DeleteObject} only, never GetObject → write-only Deny
  cannot affect reads. Hard condition.
- **(b) writers — discrepancy found:** mdpf_runner writes opal-data-portal-v2 at
  EXACTLY platinum/mdpf/* + json/portfolios/* (JsonPortfoliosLegacyRW,
  MDPF_ASSETS.021). The legacy-emit SSM path (build_legacy_compat_emit.py via
  mdpf-legacy-emit-on-demand) runs UNDER the runner — NOT a separate principal,
  so whitelisting the runner covers it. BUT C's "json/mdpf/*" target has NO
  runner grant anywhere. → C must not apply until AE returns the EXACT
  serving-feed key paths + positively-identified writer of each. Likely outcome:
  extend A's Resource to platinum/mdpf/aggregate_aua_timeseries.json +
  json/portfolios/* (cleaner than a new json/mdpf prefix).

## 4 conditions on the apply (relayed to AE)
1. Action = {PutObject, DeleteObject} only, never GetObject.
2. Exact-path writer census mapped to role grants before any serving-key Deny.
3. Deny + Condition (aws:PrincipalArn ArnLike assumed-role/<runner>/* or
   aws:userId :*) — NOT NotPrincipal; post-apply live-write + denied-write test.
4. Break-glass = narrow admin ARN, NOT everyday dev/agent creds; confirm the
   5/29 clobbering principal is OUTSIDE the whitelist (else Deny is theater).

## Action
- [RATIFY] to COO (20260601T134226Z) + [CC RATIFY] to AE (20260601T134237Z).
- This bucket-policy Deny = right layer to structurally enforce CLAUDE.md
  Rule 12 (write via role/SSM, never direct dev-cred) for this prefix.
- No CTO commit/apply — apply is AE lane via safe-apply; this is shape-ratify.

## Next-cycle expected state
AE ships A (0-diff, safe-apply) + returns serving-feed writer census; C resolves
to an A-Resource extension or a named-principal finding. Andrew-direct MDPF P1
hardening; no PRD touch. Resume sweep posture next cron tick.

ws-charter-cycle:0003 class:FIX
