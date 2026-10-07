# MDPF_HEALGAP decomposition -- ROUND 1, the THREAD (issuer 2.0.0_SA_COO~G1, dell1; cut 2026-10-07 ~08:5xZ)

**Status: ISSUED** in one issuance. Seat: `0.0.0_AB_MSTR~DELL1` msg 29 (SPAWN-DIRECT), on laptop `1.0.0_SA_CTO` placement msg 106053;
Andrew-direct ~07:15Z relayed there: "the COOs should be running /canonical-drive on their projects".

**Cut on:** PRD v0.1 @78db344481 (L4-R ADMITTED: ratified-text half SIGNED by `3.0.0_SA_CVO` @53596a3131; brief half admitted because the
CRO wrote the brief). Brief `docs/briefs/mdpf-healgap-midstream-brief-20261007.md` @a8c67a424e.

## The thread (PRD section 2, FWD-1) and its hops, measured at the base 2026-10-07 ~08:3xZ

| hop | what | today | cell |
|---|---|---|---|
| 0 read | why model_detail stopped 2026-09-01..09-10; the guard's state | measured here, no cell (below) | none |
| 1 fail | the 06:00Z pull fails on a lapsed login | `cot-rebalancer-runner-daily` ENABLED `cron(0 6 * * ? *)`; a lapse raises at `mint_rebalancer_bearer` (`lambda_function.py:145-152`), two async retries, no `on_success`. No way to make it fail on purpose without touching the login | `HG-t-1` (the induced lapse) |
| 2 heal | the session chain mints or re-uses a login | `cot-bd-session-daily-et` 07:30 America/New_York; both legs (Lever-A skip and mint) end in `opal-cot-bronze-run`, which writes `s3://opal-data-cot/bronze/<date>/_BRONZE_COMPLETE.json` LAST. Measured 10-01..10-06: one sentinel a day at 11:31-11:32Z, same UTC date as the 06:00Z pull | none: works, relied on (C-SESSION) |
| 3 re-attempt | the runner re-runs for the date only if incomplete | NOTHING re-runs. And the guard is dead: `_already_landed` (`lambda_function.py:211-218`) reads the stamp with `s3:GetObject`, which the role does not hold (`comp-iam service cot-rebalancer-runner`: `s3:GetObject [UNGRANTED]`, 2026-10-07), so it falls open and re-pulls on every invocation | `HG-t-1` (guard), `HG-t-2` (wire) |
| 4 chain | three feeds land; `on_success` carries them to silver, then gold | live: `MaximumRetryAttempts 2`, `MaximumEventAge 21600`, OnSuccess `opal-assets-silver-blackdiamond` (`get-function-event-invoke-config`, 2026-10-07) | none: works |
| 5 page | the reader sees the day's Cottonwood figures | unchanged | none: the COO's one real run at close |

**Hop 0, measured at the base (no vendor call):**
- **Cause of 2026-08-31..09-10:** the count-reconcile self-gate RAISED after `rebalancer_models` and `rebalancer_accounts` landed and before
  `rebalancer_model_detail` (account 26725961 left `/api/accounts/search` while BD kept `accountCount`). Carried at HEAD in the docstring of
  `_reconcile_counts` (`lambda_function.py:334-394`) and fixed by `c53e48f7fb` (committed 2026-09-11T02:17Z); deployed bytes LastModified
  2026-09-11T03:26:00Z. Claim: **held** (the fix commit's own measurement), corroborated by the stamp census: `meta/2026-09-0*-complete.json`
  ABSENT, `meta/2026-10-01..07-complete.json` PRESENT (each ~06:01Z). The runner's own log line for those days is unrecoverable: the log group's
  retention is 14 days (`describe-log-groups`). So the cause is a SECOND cause class (a vendor-counter gate), not session death, and it is closed.
- **Guard:** dead on the DESIRED plane (above). The APPLIED plane is unread: `iam:SimulatePrincipalPolicy` is denied to the dell1 agent user.
- **For FWD-3 (enrichment 2):** the runner sends NO as-of to Black Diamond (`date` only keys the landing, `lambda_function.py:400-458`). Row
  `MDPF_HEALGAP-S2`.

## Rule 24

Domain: the FWD-1 thread, hops 0-5. Hop 0 is measured above; hops 2, 4 and 5 work today. The remainder is two write sets with one intent each:
the runner's own code (`HG-t-1`: the guard that makes a second attempt safe, and the induced lapse that makes hop 1 exercisable, both inside
`ingest()`'s entry), and the wiring that makes the second attempt happen (`HG-t-2`: Terraform in the runner's root). No remainder. Same grain:
each cell is one adapter of the thread. State coherence: neither cell moves the per-feed run result (enrichment 1, FWD-2), the repair of old
dates (FWD-3), the retry/age settings (FWD-4), the 06:00Z fire time (FWD-5) or the class census (FWD-6).

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `HG-t-1` | The runner's guard reads the complete-stamp by LISTING (the role holds `s3:ListBucket` on `blackdiamond/cottonwood/*`), not `GetObject`, so a complete date skips before the session secret is read; and an event key `"induce": "auth-lapse"` raises the same HTTP 401 error a lapsed login raises, after the guard and before the session read, so hop 1 can be made to fail without touching the login | FWD-1 | NOT-EVALUATED | dell1 (code); deployed by the issuer at the drain | WORLD | A, `0.9.0_WK_MDPF_HEALGAP~1` |
| `HG-t-2` | The re-attempt: a second target on the existing `cot-bronze-complete` rule invoking `cot-rebalancer-runner` with `{"mode":"pull"}`, plus the invoke permission scoped to that rule, in a new file in the runner's Terraform root (opal-assets); a step of the existing chain (C-ONE-PIPELINE), no new schedule, rule or output path | FWD-1 | NOT-EVALUATED | dell1 (code); applied by the issuer at the drain | WORLD | B, `0.9.0_WK_MDPF_HEALGAP~2` |

## Write sets (disjoint)

- **HG-t-1:** `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py`,
  `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/test_healgap_guard.py` (new), the surprise channel.
- **HG-t-2:** `infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf` (new), the surprise channel.
- Checks (issuer's, dry-run at the base, all FAIL as expected; the seam instrument's own controls PASS on `cot-bronze-complete` and REFUSE
  `cot-silver-complete`): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/`.

## Edges and fan-out

No data edge: `HG-t-2` declares a target and consumes no output of `HG-t-1`. The ORDER of the two at the drain (guard deployed before the
target is applied, C-IDEMPOTENT) is a drain act, not an edge. `fanout: 2 of 2 chains, cap 8`.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- thread round; no schedule changes (the re-attempt is an event target on an existing rule).
- `comp-iam`: RUN (`comp-iam service cot-rebalancer-runner`, 2026-10-07): 4 call sites; `s3:ListBucket` GRANTED, `s3:GetObject` UNGRANTED,
  2 UNRESOLVABLE-RESOURCE (`PutObject`, `GetSecretValue`). The guard's repair uses the GRANTED call, so the round needs no IAM write. The new
  `aws_lambda_permission` is a resource policy on the runner (principal `events.amazonaws.com`), not a role grant. Blindness, as the tool states
  it: 10 Deny statements unparsed, and DESIRED plane only (simulate is denied to the dell1 user).
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches its surface.
- C-NAMES: the round mints no resource name. `target_id` and `statement_id` are sub-resource ids; `lib/opal_naming.py`'s schema maps neither
  `aws_cloudwatch_event_target` nor `aws_lambda_permission` (`tf_type_map`, `tf_unmapped_own_name`, `not_covered`, read 2026-10-07).

## The issuer's acts at the drain (not cells)

1. **Deploy `HG-t-1` (WORLD):** build-and-upload of the runner zip and `safe-apply` of opal-assets for the code only, under a change-management
   entry. It adds no vendor call (the guard removes calls). Then read the deployed code against the build input.
2. **Before applying `HG-t-2`:** read how `opal-assets-silver-blackdiamond` treats an `on_success` envelope whose `responsePayload.verdict` is
   `SKIP-IDEMPOTENT`, because once the re-attempt exists the runner returns cleanly TWICE on a normal day and the destination fires twice.
3. **Apply `HG-t-2` (WORLD), held on ACT 1:** the target makes a second Rebalancer call on any day the morning failed. That is the standing
   vendor word the PRD's ACT 1 names, so the apply waits for it. A never-widen half (CTO + COO) names the blast radius: bronze keys for that UTC
   date under `blackdiamond/cottonwood/bronze/`, the stamp, and the silver/gold chain the existing `on_success` drives; rollback = remove the
   target.
4. **The one real run of FWD-1, held on ACT 1:** for one morning set the 06:00Z target's input to `{"mode":"pull","induce":"auth-lapse"}`,
   restore it the same day, then read that UTC date's three feeds and the reader's Cottonwood page by end of day. The next natural failure is the
   negative arm.
