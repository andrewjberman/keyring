# NFRA_FIRMSEP -- Firm-Separation Belt-Consistency Standard (3-layer)

**Author:** 1.0.0_SA_CTO  |  **Date:** 2026-07-09  |  **Status:** DRAFT (arch-gate; implementation owners named below)
**Gate:** this standard is HOW NEVER#1 (firm-sep bd<->cot<->inf, IAM-Deny-enforced at runtime) is made UNIFORM across the estate.

## Why this exists

Firm-separation belts were landing incident-by-incident, producing a **patchwork** rather than a program:
- The **29-role INF cross-firm-deny** (`INF-PARITY`, landed as NFRA_TERRAFORM P2) is a PER-FIRM preventive belt.
- Tonight's **data-plane firm-sep incident #9** belts (market-update + lambda-execution write-Deny; opal-news read-Deny) are PER-FIRMLESS-ROLE belts.
These are **different grains, complementary, not redundant** -- but uncoordinated they leave silent gaps (0.7.0~B's reconcile question, 2026-07-09). This standard unifies them.

## The master-principle framing

A Terraform **declaration** (an IAM grant, an SNS subscription) is a PROXY for the **effective live state** (the grant a `simulate` returns; a subscription that actually delivers). *The estate is not what Terraform says it is.*

> **CORRECTION 2026-07-09 (0.5.0 source-confirmed; CTO independently re-verified live). This paragraph previously
> conflated two different invisibilities, and the loose half propagated into five dispatches, a Tier-0 concurrence,
> and a committed brief. The error originated here, in my document.**
>
> There are **two distinct failure modes**, and only one of them is a Terraform-coverage problem:
>
> 1. **UNMANAGED grant -- invisible to Terraform itself.** The inline `S3Access` on `lambda-execution-role`: absent
>    from all 44 pulled states, `terraform plan` clean TODAY while a firmless role held `PutObject` on
>    `opal-data-bd`. TF genuinely cannot see it. *This is a coverage defect.*
> 2. **AWS-MANAGED policy -- fully Terraform-managed, but its CONTENT is opaque to a grant-shape LINT over our own
>    TF.** `AmazonS3ReadOnlyAccess` on `opal-news-lambda-role` is **declared** (`news-pipeline/iam.tf:171-174`),
>    **in state**, and **live-attached** -- desired == applied == live, **zero drift**. `plan` was clean because TF
>    was managing it *correctly*, not because it was blind. *This is NOT a coverage defect.* (Same for
>    `AmazonDynamoDBFullAccess`, `iam.tf:179`.)
>
> **"Invisible to a lint" is not "invisible to Terraform."** The consequence is load-bearing and must not be lost:
> **100% Terraform coverage would NOT have prevented the PII exposure.** `AmazonS3ReadOnlyAccess` was already at
> 100% coverage and reached `03_mappings/` the entire time. And the belt missed `opal-data-schwab` because
> `cross-firm-bucket-read-deny.tf:58-62` **enumerates bd/cot/inf literally** -- causally independent of TF coverage.
>
> **Therefore: NFRA_TERRAFORM's close MUST NOT be recorded as closing the PII / grant-reach class.** They are
> **orthogonal controls and neither substitutes for the other**: Terraform coverage bounds *drift, review, and
> audit*; only the standing **live-simulate DETECT** (Layer 3, `s3api list-buckets`-derived bucket axis) bounds what
> a grant **reaches**. Reading the TERRAFORM close as closing the reach class is false comfort on a PII
> re-identification asset -- the same error, one level up. (CTO arch-gate, standing.)

What survives, and is independently verified: an **unmanaged grant** is invisible to every lint/plan/drift over our
own TF, and an **AWS-managed policy's content** is invisible to a grant-shape lint over our own TF. Both were found
**ONLY by a live simulate**. See `memory/feedback_firm_sep_detect_must_live_simulate_not_tf_lint.md`.

## The 3-layer standard

### Layer 1 -- PER-FIRM PREVENTIVE belt (the INF 29-role template, extended to ALL firms)
Deny an entire firm's role population from reaching another firm's buckets. Its power: it **auto-covers a future new role** in that firm -- future-proof, not point-in-time.
- **INF: DONE** (29-role cross-firm-deny).
- **bd: GAP.  cot: GAP.**  <- the coverage asymmetry to close. Today bd-firm + cot-firm roles reaching cross-firm are covered ONLY by Layer 3's point-in-time sweep, not a future-proof belt. **Extend INF's template to bd + cot role populations, uniformly.**

### Layer 2 -- PER-FIRMLESS-ROLE adjudication (the shared roles Layer 1 structurally can't cover)
Firmless/shared roles (market-update serves the estate; partners is multi-tenant; lambda-execution is shared behind 13 Lambdas) belong to no single firm, so no per-firm belt covers them. Each is adjudicated through **three gates** -- ALL must clear before belting OR before declaring sanctioned:
1. **Relation** -- is it cross-firm at the IAM layer?
2. **Semantic** -- what is the consumer's actual purpose? (config-as-data resolvers read as "0 code paths" to a literal grep -- ground the mechanism, don't pattern-match.)
3. **Sanction** -- is it TF-declared with an explicit authorization model?
Tonight's outcome (180-role owner-free universe): **write-foreign = exactly 1** (lambda-execution -> belted); **read-foreign = 4** -> 1 belted (opal-news) + 3 SANCTIONED (lambda-execution layer3-read; opal-portal MonitorDataFreshnessRead; partners multi-tenant API). *Three of four "foreign readers" were correct grants -- the gates were the difference between a belt and an outage four times.*

### Layer 3 -- STANDING live-simulate DETECT
`comp-firmsep-sweep` over the 180-role x **N-bucket** x 3-action universe, where **N = every `opal-data-*` bucket enumerated FROM THE ACCOUNT** (`aws s3api list-buckets`), NOT the firm names you happen to know. Run on a cadence + on HEAD-advance. Catches what neither a per-firm belt nor a one-time adjudication covers: **new** firmless/shared roles, drift, and **unmanaged / AWS-managed grants a TF grant-shape lint is structurally blind to** (DETECT leg 2 -- simulate the universe; leg 1, lint-what-we-author, cannot see an unmanaged grant). Sibling: the standing **SNS-email-sub-CONFIRMED** check (bind to a delivering subscription, not the TF declaration; INTENT-AWARE -- a governed-decommissioned sub is not a gap) -- same live-verify-not-config-lint principle.
> **META (2026-07-09, 0.5.0's retraction):** *prove-the-universe is only as good as the universe you ENUMERATE.* Tonight's 180/180 sweep was proven over **3 firm buckets** -- correct for NEVER#1 -- but the account holds **17 `opal-data-*` buckets, 14 never swept**, one (`opal-data-schwab`) holding a client PII re-identification table with 2 unsanctioned readers found only by accident. The enumeration is itself a proxy for the real universe; ground it against the account, not memory. The firm-bucket universe is proven; the estate data-bucket universe is NOT until all N are swept.

## Belt mechanism (applies to Layers 1 + 2)
- **Deny-ADD**, not allow-removal: an unmanaged Allow has no TF line to remove, and a Deny **survives a future accidental Allow** (NEVER#1's control property). `comp-denytest --from-plan` derives `explicitDeny` (a Deny-add), never declared by hand.
- **Scope to the exposed action**, decided by CHECKING the specific role -- **never** by pattern-matching the prior belt: **write-scoped** where a sanctioned read must be preserved (lambda-execution carries `layer3-bd-securities-read` -> a blanket `s3:*` Deny would have silently killed it); **read-scoped** where the role carries no sanctioned read (opal-news). *Same change-class, opposite correct answer, one hour apart -- decided by checking, not pattern-matching.*
- **Verify BOTH sides on LIVE**: the exposure -> `explicitDeny` (vs a proven-allowed baseline) AND a **DISCRIMINATOR** (a legitimately-allowed role stays ALLOWED on the same resource -> the verdict is attributable to the belt, not to default-deny) AND the sanctioned path stays intact. Ledger each.
- **Prefer a ROOT-scope over an enumerate-Deny where a role reads one bucket.** An enumerate-by-name Deny (`opal-data-{bd,cot,inf}`) covers only the resources you thought of -- it MISSED `opal-data-schwab` within an hour of applying (opal-news read the PII re-id table through the gap). Detaching an over-broad grant (`AmazonS3ReadOnlyAccess`) or narrowing an over-broad Allow's `Resource` (partners' `opal-data-*` -> the 5 enumerated firm buckets) closes that reach AND every other, permanently. Belt when you must (unmanaged Allow you cannot remove, genuine multi-bucket need); root when you can.

## Coverage matrix (current)
| Layer | bd | cot | inf | firmless/shared |
|---|---|---|---|---|
| 1 per-firm preventive | **GAP** | **GAP** | DONE (29-role) | n/a |
| 2 per-firmless adjudication | -- | -- | -- | DONE tonight (1 write-belt, 1 read-belt, 3 sanctioned) |
| 3 standing live-simulate DETECT | TO BUILD -- comp-firmsep-sweep on cadence + HEAD-advance; **bucket axis = ALL `opal-data-*` from the account (3/17 swept, 14 pending -> estate sweep GO'd 2026-07-09)** |

## Owners / next steps
- **CTO (me):** author + arch-gate this standard; gate the bd+cot belt diffs on live (both-sides + discriminator).
- **0.7.0 / 0.5.0:** implement the **bd + cot per-firm belt** (Layer 1, INF template) + the **standing comp-firmsep-sweep** (Layer 3). Infra, multi-firm -> AE lane (Rule 13).
- **COO:** coordinate off the incident-#9 tracker; the durable close = this standard fully landed.

## Named governance tail (from incident #9, post-NFRA)
- **14 unmanaged inline policies** on lambda-execution-role -> bring-into-TF-or-remove (the estate-is-not-what-TF-says structural find).
- **Root fixes:** detach `AmazonS3ReadOnlyAccess` (scope to `opal-data-news-v2`); remove the unmanaged `S3Access` (its justification expired when bd Lambdas moved to dedicated roles, per `bd-pipeline/iam.tf:664`).
- **partners-api defense-in-depth:** cross-firm isolation is APP-LAYER ONLY (`is_authorized` + authorizer `allowedFirmIds`) with NO IAM backstop -- one bug = cross-firm partner-data exposure. Durable fix = per-request scoped credentials (assume-role-per-firm). NOT a violation (sanctioned, TF-declared); a real single-layer systemic-shape.
- **behavior-on-next-scheduled-run:** opal-news-layer3-curation + the 4 Phase A narrowed readers (capability verified; behavior verifies on their natural runs).
