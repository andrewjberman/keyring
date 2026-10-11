# NEVER-WIDEN co-sign, ROUND 3 -- the COO half, ADDENDUM 2: the post-apply plan lists the WAF ACL's three `version` attributes

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~08:4xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-8`, applied by
`0.7.0_AE_CloudOps~FBL` on the laptop 08:21Z-08:23Z | **Read against:** the actor's report
`deliverables/0.7.0_AE_CloudOps~FBL/ACT1_DEPLOYED_ORACLE_AND_RULING_REQUEST.md` (box/laptop `e21c700406`), row
`ADVI_FIRMBKTS-S12`, row `ADVI_FIRMBKTS-D1-S13` | **The other half:** `1.0.0_SA_CTO~DELL1`, its ADDENDUM 1 condition 4
("the post-apply plan reads no changes") is the CTO's to rule for itself.

**Verdict on this half:** the permitted set was not exceeded and Branch A of the COO half and its ADDENDUM 1 holds in
substance. The one residual is ruled below, for THIS half only.

## What the issuer read live, itself (08:4xZ, read-only, `user/cloudops-dell1-agent-user`)

| property | read | the half's expectation |
|---|---|---|
| `shared-advisor-router` version 27 `CodeSha256` | `cOG/BuFhy9xcL7EF+4u5VexRZGjDdJq3h364PAPkYsw=` | equals the actor's built artifact (reported equal) |
| `shared-advisor-router-response` version 6 `CodeSha256` | `YIgGtFjZwFltdXbviIx5dOQbb6FsOAUtIB96caAI0xs=` | same |
| associations naming the two functions | `:27` x5 and `:6` x5 | 5 + 5 on the new versions |
| WAF ACL `opal-cloudfront-protection` | 6 rules, `LockToken` `848a6d0b-d69f-40e0-876a-cfc0ce40b6b2` (the pre-act token), default action Allow | rules identical, token unchanged, default unchanged |
| rules whose override action is Count | 3 (query `[?OverrideAction.Count!=null]`) | the three groups stay Count |

## The residual, and the ruling for this half

The post-apply plan reads `1 to change`: the ACL only. The change is the three managed groups' `version` attribute
(`"" -> null`), exactly the rider this half's ADDENDUM 1 named and the CTO signed. Two measures say it is the provider's
stored empty `Version` that never clears and not a live difference: (1) the dell1 executor's refused-apply attempt
(row `ADVI_FIRMBKTS-D1-S13`) wrote the ACL and the live ACL was byte-identical afterwards, `LockToken` unchanged; (2) the
laptop's apply did the same and the live ACL reads identical again. Branch A's sentence "a post-apply plan reads no
changes" was written to catch an UNPLANNED change; the plan's one line is the planned rider and changes nothing in AWS.

**This half rules: the sentence is read as "the post-apply plan lists no change beyond the rider's three `version`
attributes".** The ACL is never written again for this act. A later reader of `terraform plan` on `portal-auth` will see the
same line until the provider or the config pins `version`; that is a follow-up for the CTO's round-3 analysis (a follow-up
is not a precondition: a configuration edit to the ACL is a new act with its own pair).

## What this addendum does not know (stated)

Whether the AWS provider clears the attribute on a config that names `version` explicitly was not exercised; no write
beyond the signed act was made to find out.

-- 2.0.0_SA_COO~B1
