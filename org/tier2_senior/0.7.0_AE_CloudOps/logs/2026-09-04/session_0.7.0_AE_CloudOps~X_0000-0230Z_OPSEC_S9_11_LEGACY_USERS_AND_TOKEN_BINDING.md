# Session log -- 0.7.0_AE_CloudOps~X -- 2026-09-04 00:00-02:30Z -- NFRA_OPSEC202609 TO-OP-S-9-11

**archetype:** MIXED

**Seat:** `0.7.0_AE_CloudOps~X` (site-z, spawned by `2.0.0_SA_COO~Z`)
**Task order:** `NFRA_OPSEC202609.TO-OP-S-9-11` -- the legacy user table (`OP-s-9`, FWD-9) and the
refresh-token binding (`OP-s-11`, FWD-11)
**Commits:** `776437a094`, `a7edcf6722`, `dafb3e7147`, `bb09d1db76`, `aa30bd1360` (+ this log)

---

## Current state

**BOTH CELLS ARE AT THEIR TERMINAL STATE FOR THIS FACE.** The proof-of-spec instance is **VALID
(rc=0)** with 8 of 8 criteria filed: seven PASS and one `UNVERIFIABLE-BY-INSTRUMENT` with its
substitutes enumerated.

**`OP-s-9` -- the retirement is BUILT AND STOPPED AT THE DELETE.** Snapshot taken and verified
(12 items / 4,506 bytes, matching the live table on *both* count and size). Both `opal-users` grants
removed from `portal-auth/iam.tf:50-51` and the removal proven differentially on the applied plane
(dynamodb resources 7 -> 5, removing exactly two, adding none). Fixture login identical before and
after. **The table stands at 12 rows, ACTIVE, nothing written and nothing deleted.** Row `Z-S119`
offers the decision; `2.0.0_SA_COO~Z` accepted the gate (20101) and is putting the delete to Andrew
as a card. `OP-s-9` does **not** flip complete -- its closing condition includes a decision that
belongs to a human.

**`OP-s-11` -- shipped and exercised.** The refresh token's `sub` is no longer an email address. It
is a 32-hex SHA-256 binding over the row's PK and `createdAt`, deployed and verified in the running
bytes. A deleted-and-re-created fixture account on the same address does **not** resurrect the old
session, and **nobody was signed out**.

## What was done

**Phase 1 re-grounding produced two premise corrections before any act**, which is the whole reason
the dispatch put it first.

1. **A THIRD live grant exists outside this face's lane** (`Z-S112`). The face models the grant
   population as two ARNs on one role in one root. The live population is **three statements across
   two roles in two roots**: `trade-submission-lambda-role` holds full CRUD on `table/opal-users` at
   `trade-pipeline/iam.tf:63-64` and is the execution role of **seven live lambdas**. Removing
   `:50-51` does not leave the table ungranted. Routed up rather than taken; `2.0.0_SA_COO~Z` ruled
   it a separate cut (`TO-OP-S-9C`) and **amended this face's grant limb** so it no longer claims an
   exclusivity that a portal-root-scoped check cannot see is false.
2. **The us-east-2 table does not exist** (`Z-S113`). us-east-2 holds *zero* DynamoDB tables in this
   account. That discharges by measurement a `status UNKNOWN/deferred` carried since 2026-06-26 and
   falsifies the stated premise of the CTO condition-2 that had preserved `iam.tf:51` for ten weeks.

**Then the work:** the four-plane reader census; the snapshot; the grant removal (targeted apply,
ledger, before/after fixture probes); the retirement gate report; the `sub` re-binding (source, bun
ESM rebuild via the canonical builder, targeted apply); and the delete/re-create probe with its
controls and an exact fixture restore.

## Blockers

**None outstanding at this seat.** One item is *parked with a human by design*, not blocked:
the `opal-users` DELETE. `2.0.0_SA_COO~Z` explicitly declined to route it as a COO decision.

## Next steps

- **[Andrew, via `2.0.0_SA_COO~Z`]** The delete decision. If the word comes, the sequence is **not** a
  bare delete: `opal-users` is still terraform-managed at `portal-auth/dynamodb.tf:151-165`, so a
  console/CLI delete would leave the resource in state and the next plan would propose to **re-create**
  it. Order: `terraform state rm` -> `delete-table` -> remove the block -> plan.
- **[this lane]** `TO-OP-S-9C` (@`0ed206674e`) -- the trade-pipeline residual. **Its runtime oracle
  does not exist and I already measured that**: neither CloudTrail trail carries DynamoDB data
  resources, so no read of any DDB table in this account leaves a trail record. Per `2.0.0_SA_COO~Z`
  (20101) that outcome *passes* `S9C-AC3` as `UNVERIFIABLE-BY-INSTRUMENT` and the grant stays. The
  remaining honest alternative is the deployed-bytes route across the seven functions.
- **[house-keeping]** Four pre-existing non-ASCII characters remain in
  `infra/aws/terraform/portal-auth/iam.tf` at lines 138, 199, 208, 229 -- not mine, not introduced
  here, surfaced rather than silently edited in another seat's blocks.

## Errors and corrections at this seat

- **I misread the portal-auth plan baseline.** I read a pending WAF block as `0.7.0_AE_CloudOps~S`'s
  unapplied work and said so to that seat and to `2.0.0_SA_COO~Z`. It is not: the rule is already
  live at priority 5 in Count, and what I was looking at is the **documented perpetual non-converging
  churn** (rows `Z-S68`/`Z-S75`) -- three minus-rule blocks against three identical plus-rule blocks
  that survived three applies. Corrected by `~S` in 20075. **The correction improved the work**: it
  is why `S911-AC4` files `UNVERIFIABLE-BY-INSTRUMENT` with substitutes instead of chasing a
  convergence that cannot happen.
- **I cited `dist/db.js` as "the BUILT plane".** It is a `tsc` artifact in the repo and is **not what
  runs** -- the deployed artifact is a single bundled `dist/index.mjs`. The conclusion survived and is
  now *better* grounded, because I read the actual bundle: it contains `opal-users-v2` once and the
  exact legacy name **zero** times. Recorded because the citation was the weak kind that reads as
  strong.
- **I built a commit-message file with `printf`**, which CLAUDE.md 14a forbids for exactly the reason
  it forbids `-m`. Caught before the commit and rewritten with a non-shell writer.
- **I piped `comp-find` into `head`/`tail` twice** and the rail refused both. Correct refusals -- that
  is the pattern that erases a denominator.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-iam refresh-census` | `--out <scratchpad>/iam-census-20260904.json` | The APPLIED-plane instrument for the IAM census: 221 roles, 1,173 inline statements, vintage `2026-09-04T00:26:29Z`. **It is what found the third grant** a file-scoped check could not see. Discloses its own blind spot -- 174 UNRESOLVED attached-managed statements across 137 of 221 roles -- which was carried into `S9-AC1` rather than dropped. |
| `comp-find` | `'opal-users'` then `'opal-users($|[^-])'`; scoped runs over the trade + auth-handler trees | Gave the source denominator **and caught the substring trap that would have corrupted it**: the naive pattern returns 2,145 hits by matching `-v2`/`-master`/`-trade`; the whole-value pattern returns **303 across 51,693 files**. The scoped trade run returned 2 hits across 302 files, *both the grant lines themselves*. |
| `comp-read --enumerate` | on `jwt.ts`, `auth.ts`, `db.ts`, `types.ts`, `portal-auth/dynamodb.tf` | Located the claim construction and, more usefully, **every consumer of `payload.sub`** (`auth.ts:435` in `refresh()`, `:473` in `getCurrentUser()`) -- which is what established the OP-s-11 boundary. The `dynamodb.tf` enumerate surfaced that `opal-users` is still terraform-managed at `:151-165`, the detail that makes a bare delete wrong. |
| `comp-read --for` | `jwt.ts --for "how is the refresh token sub claim constructed"` | Put `sub: user.email` (`:119`) in front of me with its qualifier band on the first read. |
| `comp-schedule` | issuer preflight, **not re-run** | Nothing in this face builds a monitor or alarm, and the STOP at the delete is a pre-existing CLAUDE.md human gate rather than an agent-made one, so the moratorium surface is untouched. Stated rather than left blank. |

## Evidence discipline worth carrying

**The positive control is what made two of these findings real rather than plausible.** A 2-role IAM
result from a matcher that excludes three patterns is *indistinguishable from a broken regex* until
the v2 ARN returns 4 on the same census. A refusal after a delete proves nothing until the same token
is shown working before it. And a "the binding is enforced" claim is worthless until a deliberately
**wrong** binding is shown being refused -- which is why that third control was added beyond the two
the face named.

**Two instruments disagreeing in FORM but agreeing in RESULT is worth more than one repeated.**
us-east-2 absence was read twice: `describe-table` *throwing*, and `list-tables` *returning an empty
array on a successful call*. The second is strictly stronger -- it enumerates the region instead of
probing one name -- and only the pair rules out a credential or endpoint artifact reading as absence.
