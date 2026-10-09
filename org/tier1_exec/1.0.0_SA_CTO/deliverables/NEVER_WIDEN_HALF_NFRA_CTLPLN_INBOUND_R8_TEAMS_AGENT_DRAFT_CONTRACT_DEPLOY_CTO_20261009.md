# CTO never-widen half -- NFRA_CTLPLN workstream INBOUND, round 8: the drafting contract (targeted apply of `module.ldo_001`)

**Author:** `1.0.0_SA_CTO`, 2026-10-09 ~22:4xZ. **Counterpart:** the COO half
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_INBOUND_R8_TEAMS_AGENT_DRAFT_CONTRACT_DEPLOY_COO_C_20261009.md`
@082e0d865a (msg 108143). **Authority:** the Andrew-direct and rulings A and B in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_21xxZ_TEAMS_TEXT_OPS_AGENT_TALK_LEAKED_INTO_EOD_POST.md` @74fc19c25f.

## What I read myself

- `git diff --stat 2ad98c2e3a bde0c0fc90` over `data/transcripts/scripts/teams_chat`, `daily_reports/eod` and
  `infra/aws/terraform/transcripts`: 3 files, +297/-36 (`post_format.py`, `assist.py`, `tenant.py`); no `.tf` in the root.
  Matches the COO half.
- `bde0c0fc90` is an ancestor of laptop HEAD.
- `assist.py:574` `_draft_fields`: strips one code fence, then the whole text must be one JSON object with a string `post`;
  no slicing between braces, so prose around the JSON is refused, never posted. `parse_draft` (`:619`) logs counts only.

## Blast radius

The act may touch only `module.ldo_001.aws_lambda_function.handler` and `.ingress[0]`, and only `source_code_hash` /
`last_modified`, through one targeted `safe-apply` by `0.7.0_AE_CloudOps~CTL`. Nothing outside the module, no policy, no
environment variable, no schedule. Rollback per key: the saved live package (hash `op92gM7r...`) restored to
`dist/teams-chat-assist.zip` and the same targeted apply; `st["dialog"]` is ignored by the old code.

## Both branches

I adopt the COO half's Branch A (apply on exactly `0 add / 2 change / 0 destroy`, hash-only) and Branch B (apply nothing and
report on anything else, including a live `CodeSha256` drift, the 20:00Z-21:45Z End of Day window, or an event in flight)
without change.

## The named risk

If the live model does not answer in the contract, every draft is refused and Andrew gets one line instead of a draft: a
lost draft, never a leak. I accept that risk, with the COO's first-hour read of `draft_contract` outcomes and a same-hour
rollback if refusals dominate. Status after the apply is APPLIED; EXERCISED only on the first real drafting call.

**SIGNED** -- `1.0.0_SA_CTO`
