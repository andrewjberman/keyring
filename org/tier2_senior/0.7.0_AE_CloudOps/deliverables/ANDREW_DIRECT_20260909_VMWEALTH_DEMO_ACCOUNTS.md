# ANDREW-DIRECT 2026-09-09 ~18:2xZ — VM Wealth demo accounts + `opal-partners-demo` firmId

**Received by:** `0.7.0_AE_CloudOps~X`
**Channel:** Claude Code terminal, this seat
**Recorded:** 2026-09-09, same turn as receipt (org/XXX.md "Andrew-direct instructions" clause)
**Broadcast:** MCP to `2.0.0_SA_COO`, `1.0.0_SA_CTO`, `0.0.0_AB_MSTR`, same turn

---

## THE WORD — VERBATIM AND ENTIRE (message 1)

> I need you to check my teams thread with Yang Liu. I need you to create a handful of assets for
> the Portal. Namely, we need to create demo accounts for these two vmwealthpartners users. I think
> in order to do this properly, it means creating a firmID (if there is not one already) for
> opal-partners-demo, which means making an opal-partners-demo DDB that is synced to the "Demo"
> firmID. THis way we can spin up accounts for people to sign in but in Advisor Intelligence they
> just see the demo data set presented.

## THE WORD — VERBATIM AND ENTIRE (message 2, follow-up in the same turn)

> The "demo" firmId is the system we need to plug into here. the mockadv is surely deprecated but
> thats another story.

**SCOPE IS NOT ADJUDICATED HERE.** Surfaced, not interpreted. Two readings of message 1 + 2 remain
live (new `opal-partners-demo` firmId plugged into demo's dataset, vs. seat the users on the
existing `demo` firmId); the fork is put back to Andrew rather than resolved at this seat, because
a standing ruling blocks one of them (below).

---

## UPSTREAM SOURCE — Yang Liu, Teams 1:1, VERBATIM

`19:024dc4e9-febd-45ce-806e-7ec998305149_2e21f8e5-55ca-45c1-91b9-a4607bf28d4f@unq.gbl.spaces`

- 2026-09-09T17:48:35Z — Yang Liu: "need two demo accounts: sarah@vmwealthpartners.com
  dustin@vmwealthpartners.com"
- 2026-09-09T17:48:43Z — Yang Liu: "this is for VM wealth"
- 2026-09-09T17:48:55Z — Yang Liu: "this is another 200m opportunity"
- 2026-09-09T17:48:59Z — Andrew Berman: "Ok great will set these up momentarily."

---

## MEASURED STATE AT RECEIPT (all live reads, 2026-09-09 ~18:3xZ)

| fact | value | instrument |
|---|---|---|
| `vmwealth` anywhere in repo corpus | **0 hits / 152,454 files** (`corpus=all`) | `comp-find` |
| `FIRM#opal-partners-demo` in `opal-users-v2` | **ABSENT** | `dynamodb scan SK=META` |
| `FIRM#demo/META.s3Bucket` | `opal-data-demo` | same scan, Count=6 of 75 scanned |
| users on `firmId=demo` | exactly one real: `demo@demo.test`, `lastLogin 2026-07-09` | `query firmId-index` |
| `opal-data-demo` object count | 22,414, prefix `platinum/` only (**no `gold/`**) | `s3api list-objects-v2` |
| MFA default when fields absent | `mfaEnabled ?? false` -> no challenge | `auth-handler/src/db.ts:161`, `auth.ts:106` |

## THE FIVE CARRIERS A NEW firmId MUST ENTER (measured, not inferred)

1. `opal-users-v2` `FIRM#<id>/SK=META` — `s3Bucket` (data plane; `lambda_function.py:288-312`)
2. `infra/aws/lambda-edge/_shared/firm-config.mjs` `FIRM_CONFIG` — **Lambda@Edge** routing
3. `portal/src/lib/firmAccess.ts` `FIRM_ALLOWED_PATHS` — **deny-by-default** page access
   (+ `FIRM_EMAIL_DOMAINS`)
4. `portal/src/api/endpoints/advisor-intelligence.ts` `ROUTER_FIRM_SUFFIX` — wire protocol
5. `users/scripts/create_user_v2.py` `FIRMS` — provisioning (deny-by-default)

`demo` is present in **all five** today. `opal-partners-demo` is present in **none**.

## THE BLOCKER ON THE LITERAL INSTRUCTION

`infra/aws/lambda-edge/_shared/firm-config.mjs` carries a standing CTO ruling owned by the AE lane:

> **"DO NOT ADD OR EDIT AN ENTRY THAT MAKES TWO firmIds SHARE A `bucket` VALUE."** … "The moment two
> DISTINCT firms share one bucket, that comparison degenerates to always-equal and the cross-firm
> tenancy check SILENTLY PASSES — while its negative control keeps passing too" … "THE REMEDY, ruled
> by CTO and owned by the AE lane: replace bucket-equality with TENANT-GRAIN ENTITLEMENT (`advTenant`)
> … **If you are here to change a `bucket` value, that remedy lands FIRST.**"

Adding `opal-partners-demo -> bucket: opal-data-demo` beside `demo -> bucket: opal-data-demo` is
precisely the prohibited edit. The prerequisite `advTenant` remedy has **not** landed
(record: `.../deliverables/ADVI_P4R3_ADVTENANT_RULE24_RECORD_20260821.md`).

Andrew's own note that "mockadv is surely deprecated" is the SAME hazard's other instance — the file
records mockadv/49financial sharing `opal-data-bd` as MEASURED live 2026-08-21. Surfaced, not chased.

## DISPOSITION

Not adjudicated at this seat. Put back to Andrew as a single call with a recommendation
(seat both users on the existing `demo` firmId — zero deploys, all five carriers already wired,
one bucket / one firm preserved). No user record and no carrier edit made pending his word.
