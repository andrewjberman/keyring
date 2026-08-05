# Deploy-completion ledger: MDPF_CANRTE.W-1b — additive gold-bucket IAM grants

**Opened:** 2026-08-05T23:05Z by 0.7.0_AE_CloudOps · **Status:** CLOSED 2026-08-05T23:40Z
**Authority:** 2.0.0_SA_COO DISPATCH @225449Z (GO); arch-gate 1.0.0_SA_CTO re-gate ruling 183006Z.
**TO:** `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/MDPF_CANRTE.W1b.additive-iam-gold-prefix-grants.md`
**Commit:** `2a11a879e`

## The act

PURE ADD. Gold-bucket read granted alongside the existing platinum grants, in all three pinned
statements. **Every platinum grant RETAINED** — the running chain still reads platinum today, and
removing it here would break production, which is exactly what the W-1 a/b split ordering prevents.

| # | file | statement | change |
|---|---|---|---|
| 1 | `infra/aws/terraform/opal-assets/emitter.tf` | `ReadServedMdpfPartitions` | Resource → list: platinum + gold |
| 2 | `infra/aws/terraform/opal-assets/emitter.tf` | `ListServedMdpfPartitions` | Resource → list **AND** `s3:prefix` **Condition** extended |
| 3 | `infra/aws/terraform/mdpf-pipeline/iam.tf` | `PlatinumRollSourceRead` | Resource → list: platinum + gold |

**The trap (found by 0.4.0_DS outside their own lane):** `StringLike s3:prefix` is a **second,
independent pin**. Extending the Resource alone leaves the condition denying — and it denies the
**LIST**, not the GET. The caller is `_latest_key()` → `list_objects_v2`, so the symptom is an
AccessDenied on a listing, which is not what anyone debugging a re-pointed READ would hunt.
Both halves extended, with the explanation left in-source at the statement.

**Gold prefix GROUNDED, not guessed** — `gold/mdpf_revamp`:
- `data/mdpf/config/route_bindings.yaml:36-47` — bucket `opal-data-assets`, spine_key_template
  `gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json`
- AND four live keys on S3 written 2026-08-05 09:3xZ (49financial / cottonwood / global / inflection)

*(Said explicitly because I guessed an IAM role name wrong three times today. A `NoSuchEntity` on a
name you invented is not evidence of absence — it is evidence you guessed.)*

## Legs

| # | leg | evidence | status |
|---|---|---|---|
| L1 | git | `2a11a879e`; `terraform fmt` CLEAN both files; `validate` = Success | DONE |
| L2 | plan additive-only | opal-assets: platinum line reads `~ Resource = "…platinum…" -> [ + "…platinum…", …]` — a scalar→list conversion **retaining** platinum, ZERO removals. mdpf-pipeline: `0 to add, 1 to change, 0 to destroy` | DONE |
| L3 | apply | opal-assets **TARGETED** (see FINDING 1); mdpf-pipeline full: `Apply complete! 0 added, 1 changed, 0 destroyed` | DONE |
| L4 | 0-diff re-plan | both modules: `No changes. Your infrastructure matches the configuration.` | DONE |
| L5 | APPLIED truth | live `get-role-policy` on BOTH roles — not TF's word. Both buckets in Resource AND both prefixes in the Condition | DONE |
| L6 | Rule 22a battery | 8 simulate calls, **every one a SEPARATE invocation** | DONE |

## L6 — the simulate battery (ONE `--resource-arns` per call, controls ISOLATED)

**`opal-assets-daily-emitter-role`**

| # | call | result |
|---|---|---|
| 1 | ListBucket `opal-data-assets` **WITH `--context-entries`** `s3:prefix=gold/mdpf_revamp/global/` | **allowed** |
| 2 | GetObject one exact live gold key | **allowed** |
| 3 | POSITIVE CONTROL, isolated — platinum GetObject | **allowed** (running path undisturbed) |
| 4 | NEGATIVE CONTROL, isolated — `opal-data-assets/schwab/08242234/silver/…` | **implicitDeny** |
| 5 | NEGATIVE CONTROL — ListBucket with a NON-granted prefix | **implicitDeny** |

**`mdpf-daily-trigger-lambda-role`**

| # | call | result |
|---|---|---|
| 6 | GetObject gold key | **allowed** |
| 7 | POSITIVE CONTROL, isolated — platinum | **allowed** |
| 8 | NEGATIVE CONTROL, isolated — monolith schwab | **implicitDeny** |

**`--context-entries` was mandatory on #1**: the statement is CONDITIONED, and with no context an
unsatisfied condition returns `implicitDeny` **byte-identical to a real deny** — you cannot tell
"condition unsatisfied" from "grant missing" without it.

**The NEGATIVE controls (#4, #5, #8) are not in the TO** — adopted from the risk-reflex citation
(`20260713T0535Z_opal-assets-g4-ownership-fold`, L4: *"SOVEREIGN opal-data-bd… IMPLICITDENY (49F hold
intact)"*). They matter more here than they did there: **`opal-data-assets` is the MONOLITH bucket**
holding schwab/blackdiamond source trees under firm-separation. A bucket-level widening would be a
NEVER-rule breach, and only a negative control can show it did not happen. `comp-iam` structurally
cannot — it models `(action)`, never `(action, resource)`.

## Findings

1. **`opal-assets` module carries FOREIGN UNAPPLIED DRIFT — a bare apply would have landed it.**
   Full plan: `4 to add, 2 to change, 3 to destroy`. Only ONE (`aws_iam_role_policy.emitter`) is mine.
   The rest:
   - `ce99054e44` (2026-07-29, **`0.7.0_AE_CloudOps~A`**) — cot mirror EventBridge→Scheduler migration,
     **Andrew-direct**, *"old UTC rules die in the same change, no dual-trigger window."*
   - `f559cbc516` (2026-07-17, `0.2.0_DT_PortfolioAnalytics`) — TAXSMA reporting-pull. Its own commit
     message says *"TF routes to CTO plan-gate (no self-apply)."* **Deliberately held; correct to leave.**

   I applied `-target=aws_iam_role_policy.emitter` rather than sweeping either in. Targeting noted here
   per the pre-flight checklist.

2. **⚠ ANDREW'S 2026-07-29 COT SCHEDULE MOVE NEVER TOOK EFFECT — 7 DAYS.** Verified live, both halves:
   - OLD `opal-assets-ingest-mirror-cot-daily` → `cron(30 3 * * ? *)`, **State: ENABLED**
   - NEW `opal-assets-ingest-mirror-cot-daily-et` → **ABSENT** (`aws scheduler get-schedule` returns nothing)

   The migration was designed atomic (old rules die in the same change). Unapplied means the old UTC
   rule is still firing and the Andrew-directed America/New_York schedule does not exist.
   **This is the committed-but-never-deployed class again**, on my own lane's Andrew-direct work.
   Surfaced to COO; NOT applied by me — it is a separate authorization and a separate window, and
   sweeping it in under a W1b apply is precisely the half-landed-deploy shape.

3. Pre-existing `terraform fmt` drift in `opal-assets/bd49f_pull.tf` — not my file, not touched.

## Scope

**W-1a (DS source re-point, five consumer legs) is UNBLOCKED by this.**
Out of scope and NOT done: removing platinum grants (rides the teardown), the 439-partition copy, any
source edit, any teardown. Per Andrew-direct 2235Z the ten-script EC2 chain keeps running — **no
teardown is authorized**, and nothing was decommissioned.
No alarm/monitor/checker built (standing moratorium).
