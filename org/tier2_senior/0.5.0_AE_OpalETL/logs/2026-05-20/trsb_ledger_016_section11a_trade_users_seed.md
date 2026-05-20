# TRSB_LEDGER.016 — section 11-A Menachem trade-users seed

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/TRSB_LEDGER.016.ae-section11a-trade-users-seed.md`
**Type:** direct DynamoDB write (no deploy).

---

## Current State

- **TRSB_LEDGER.016 COMPLETE.** `menachem@opalinvest.com`'s `trade-users` row now mirrors
  `andrew@opalinvest.com` exactly — `groups=[approvers,executors]`, `role=dev`. Shipped
  as an **update-in-place**, not a fresh seed (see Premise Deviation).

## Premise deviation — surfaced + COO~B-ruled

The TO modeled section 11-A as a fresh seed (a `put_item` of a new row). A pre-write
`get-item` found menachem@ **already had** a `trade-users` row — executor-only, since
2026-01-06. The .015 probe had not checked menachem@'s own trade-users row (its P1 was
andrew@'s row, P3 was portal-auth), so .016 was authored against an incomplete picture.

I surfaced this to COO~B (2026-05-20 20:15Z) rather than escalating silently — a
`role=dev` SoD-bypass escalation of an *existing* active trade user is more sensitive
than seeding a fresh row. My initial `put_item` used a `attribute_not_exists(email)`
condition, so it correctly **no-op'd** (`ConditionalCheckFailedException`) — no clobber.

COO~B ruling (2026-05-20, recorded in a `coo_disposition` block on the .016 TO, commit
`c7d788148`, CC CTO~B): **ship as update-in-place.** The deviation is mechanism-only —
the end state is verbatim Andrew's section 11.2-A directive ("same authority as andrew@"
= approvers+executors / dev); menachem@ already holding executor-only authority only
reduces the delta. No Andrew re-confirm needed. The executor->dev escalation + SoD-bypass
is exactly section 11.2-A + section 11.3 intent.

## What changed — before / after

`trade-users` row for `menachem@opalinvest.com` (table key: `email` HASH):

| Attribute | BEFORE | AFTER |
|-----------|--------|-------|
| `active` | `true` | `true` (unchanged) |
| `created_at` | `2026-01-06T00:00:00Z` | `2026-01-06T00:00:00Z` (**preserved** — the row genuinely dates to 1/6; no fresh created_at) |
| `email` | `menachem@opalinvest.com` | unchanged |
| `groups` | `["executors"]` | **`["approvers","executors"]`** |
| `name` | `Menachem` | unchanged |
| `role` | `executor` | **`dev`** |

Operation: a single `aws dynamodb update-item` — `SET groups, role` only — with a
`attribute_exists(email)` condition. Only menachem@'s row was touched.

End state = exact `andrew@` mirror (only the identity fields `email`/`name` differ):
`{active:true, created_at:2026-01-06T00:00:00Z, groups:[approvers,executors], role:dev}`.

## Acceptance Criteria

| AC | Status | Evidence |
|----|--------|----------|
| AC1 — menachem@ trade-users row mirrors andrew@ (every attr; groups=[approvers,executors], role=dev) | **PASS** | `update-item ... --return-values ALL_NEW` returned the mirrored row; 6 attributes, andrew@-shape. |
| AC2 — read-back verification transcript | **PASS** | `ALL_NEW` + an independent `get-item` both show `{active:true, created_at:2026-01-06T00:00:00Z, email:menachem@..., groups:[approvers,executors], name:Menachem, role:dev}`. |
| AC3 — andrew@'s row unchanged (no collateral write) | **PASS** | Post-update `get-item` on andrew@ is byte-identical to the .015 P1 capture (`UNCHANGED vs P1 capture: True`). The `update-item` keyed only menachem@. |
| AC4 — no emoji; session log + Compiler Tools; RAVC2 | **PASS** | ASCII-only; this log; RAVC2 to COO~B CC CTO~B. |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `aws dynamodb get-item` (pre-write check) | OK | Surfaced the existing executor-only menachem@ row — the premise deviation. |
| `aws dynamodb put-item` with `attribute_not_exists(email)` | NO-OP (ConditionalCheckFailed) | The conditional guard correctly refused to clobber the existing row. |
| `aws dynamodb update-item` `SET groups, role` with `attribute_exists(email)` + `ALL_NEW` | OK | The escalation write; returned the mirrored row. |
| `aws dynamodb get-item` (andrew@ + menachem@ read-back) | OK | AC2 + AC3 verification. comp-* N/A — a DDB row write (probe/seed TO). |

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 (CC CTO~B) — .016 shipped as update-in-place; before/after
  diff above. On accept, section 11 is fully discharged (.016 + .017 both done);
  TRSB_LEDGER's only remaining item is .012 (Andrew :5175-gated).
