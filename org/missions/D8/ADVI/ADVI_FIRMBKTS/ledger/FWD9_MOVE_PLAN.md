# ADVI_FIRMBKTS -- FWD-9(a): THE MOVE PLAN (one document, two firms) -- `2.0.0_SA_COO~B1`, 2026-10-14 ~13:2xZ

This is the ONE plan document the PRD names (FWD-9, DONE WHEN (a)). It is an index and a reading guide: the plans themselves are the two per-firm records below, each move carrying its
order, its dependencies, its rollback, its proof and its claim. **Writing the plan starts no move.** The grade is the CTO's.

| firm | record (JSON, graded by `r8_checks.py plan`) | prose | moves | retire | open questions | merged |
|---|---|---|---|---|---|---|
| Inflection | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json` | `PLAN_INFLECTION.md` | 44 | 13 | 30 | 5118743acd (`FB-l-1`) |
| Cottonwood | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/PLAN_COTTONWOOD.json` | `PLAN_COTTONWOOD.md` | 30 | 6 | 14 | f90ecab714 (`FB-l-2`) |

Inputs: the round-7 inventories (`~76` to `~80`), `ledger/ROUND8_PLAN_INPUTS_20261013.md`, the CTO's round-7 analysis (`ledger/ROUND_ANALYSIS.round7.md`). The retirement census (`FB-l-3`, `~83`, merged 9977d91265)
feeds the retire lists; its first retirement, `inf-gold-full-on-bronze-complete` (Inflection retire R2), is `FB-l-4`.

## Inflection -- the order in which it moves (from the record)

1. `M01` bring the live `exec-summary-trigger` rule under Terraform (an import; no AWS change). 2. `M02` the destination bucket policy and EventBridge delivery on `opal-data-inflection`.
3. `M03` give `inf-portal-publisher` a new trigger in the 49 Financial shape: a Scheduler floor, created DISABLED. 4. `M04` after M03 is proven: enable the floor, remove the `gold/meta/` S3
notification entry, then disable-and-delete `mdpf-feeder-accelerator` and the Door 6 marker and deny (Andrew's DEC-13 retirement, ordered AFTER the publisher has a trigger). 5. `M05` the bulk
copy of all layers (copy-only), then the Lambda families `M06` to `M39` in dependency order (writers before readers, the silver aggregator after its nine inputs, the gold trigger and runner
after the aggregator), the CloudFront and bucket-policy cutover `M41` and `M42`, and last `M43` and `M44`: `opal-data-inf` reduces to the B2 credential `orion/jwt/current.json`, which stays by Andrew's
word and is out of the 45-day set.

## Cottonwood -- the order in which it moves (from the record)

1. `M1` to `M5` are repairs and prerequisites with no cutover (`cot-etf-ownership-daily`'s stale `SRC_BUCKET`, the `router_iam.tf` comment that cites a destroyed rule, the characteristics-producer Terraform,
the organization trail selector for the 45-day window, the registry rows). 2. `M6` to `M9` copy the served tier, the investor-reporting directory, the satellites JSON and the raw ingest into
`opal-data-cottonwood`. 3. `M10` to `M12` grants, the foreign-firm deny and the event notification there. 4. `M13` the CUTOVER (registry routed-alias flip), then `M14` to `M24` the edge, IRPT and portal
readers and the pipeline writers, 5. `M25` to `M29` the residue and the three-step decommission of `opal-data-cot` (grants and notification, the CloudFront origin, the objects and bucket) after the 45-day window.
The plan RECOMMENDS `opal-data-cottonwood` as the canonical home (the registry grades `opal-data-cot` an alias of it): the CTO's ratification is open question Q1.

## What the CTO is asked to read, and decide (FWD-5's first move; the plan's questions)

- **The first moved trigger (`FB-l-5`).** The plans' first row, Inflection `M01`, is a Terraform import and moves no trigger. The first row that MOVES a trigger is Inflection `M03` then `M04`
  (the publisher's trigger from the S3 notification to a Scheduler floor), which also unblocks `D1-W80-S1` (its successor is `M03`). Recommended `FB-l-5` = `M01`, `M03`, then `M04` steps (1) and (2) only
  (enable the floor, remove the `gold/meta/` entry), exercised once and read; the Door 6 deletion (`M04` step 3) is a separate change after that read. Cottonwood's trigger moves (`M12`, the new bucket's event notification, and `M17`, the
  `cot-bronze-complete` and `cot-silver-complete` rules) depend on the copies and grants before the cutover, so they are not first.
- **Open questions** are carried in each record's `open_questions` (Inflection 30, Cottonwood 14). The ones that gate a first move: Cottonwood Q1 (canonical home), Inflection's cutover date for the 45-day window (Q2), and
  the claims the plan holds as `held` rather than `measured` (Inflection `M04` and `M05` are `held`: they rest on the 49 Financial shape being mirrorable, which `M03`'s exercise reads).
- **Conditions carried, not cells** (unchanged): all six exec-summary slots stay OFF until `D1-W75-S2`, `D1-S50`/`D1-S53` and `D1-W70-S1` each disarm.

-- 2.0.0_SA_COO~B1
