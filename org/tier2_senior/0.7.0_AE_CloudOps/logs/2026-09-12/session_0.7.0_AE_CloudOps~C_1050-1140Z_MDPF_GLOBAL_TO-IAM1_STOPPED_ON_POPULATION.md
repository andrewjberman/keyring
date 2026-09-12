# Session log — 0.7.0_AE_CloudOps~C — 2026-09-12 1050–1140Z — MDPF_GLOBAL.TO-IAM1 stopped on its own population tripwire

**archetype:** DIAGNOSE

**Seat:** `0.7.0_AE_CloudOps~C` (fresh lane, seated by `0.0.0_AB_MSTR` on `1.0.0_SA_CTO` msg-id 96082)
**Face:** `MDPF_GLOBAL.TO-IAM1` @`85f58dfd9c` · **Issuer:** `1.0.0_SA_CTO` · **GO:** msg-id 96097
**Order status at close:** `pending` — UNCHANGED. Not flipped, not failed.

## What the order asked, and why it is not done

Grant `mdpf-daily-runner-ec2-role` the prefixes its own runner needs — per the order, "the 5 read
prefixes and the 3 firm destination prefixes", with a hard boundary: **"NOT AUTHORIZED: any grant
beyond the 8 prefixes the measurement names."**

I never reached the grant. The order's own first criterion is a re-run of the pre-act sweep, and it
arms a tripwire on it:

> ⛔ **THE COUNT IS PERISHABLE.** Re-run the sweep before acting; if the live denominator is not 9
> read prefixes and 3 destination prefixes, that is a NEW population — stop and report rather than
> reconcile.

The live denominator is **10** read prefixes, of which **8** are denied. Plus 3 of 3 destinations
denied. A correct grant is **11** prefix grants, against an authorized ceiling of 8. Both of the
order's stop conditions fired, so I stopped. Nothing was applied, nothing was edited, nothing is
half-landed and no rollback is owed.

## The finding — row `MDPF_GLOBAL-S1`

**Three documents carry three different denominators for one population, and the order's number
matches neither of its own sources.**

| document | claim |
|---|---|
| `battery_ib_rt_6.result.md:40` | "AccessDenied on 5 of the 9 prefixes the runner reads" |
| pinned row `IRPT_BCKEND-S50` @`6d7c132f43` | "denominator 6 source prefixes + 3 destinations", 4 denied |
| the task order @`85f58dfd9c` | "5 of 9", boundary fixed at 8 prefixes |
| **this sweep, on the host, by the host** | **10 source prefixes, 8 denied; 3 of 3 destinations denied** |

The 6-prefix sweep was **correct for the subset it probed** and was never offered as a population
census. It probed `dim_relationship` alone for 49financial and never probed `dim_account`,
`dim_identity_crosswalk`, `dim_portfolio_group` or `bridge_group_account` — all four of which
`directory_runner.py` reads (`Firm49F.DIMS` in `load()`, plus the 201-group overlap census).

**What made it catchable was refusing to take the inherited count.** I derived the population by
subtraction from the *consuming code* — `directory_runner.py`'s own read sites plus the three firms'
`runner_common.py` constants — and got 10 before I ran anything. That disagreed with the order's 9,
which is what sent me to the pinned row, which disagreed again. CLAUDE.md Rule 24's warning is the
exact shape: a subtraction over the **wrong domain** arrives with a printed denominator and therefore
**reads as MEASURED**. The 6 was a real number from a real sweep. That is precisely why nobody
re-derived it.

⭐ **The cheap defence, stated as a question rather than a procedure:** for any inherited count you
are about to act on, ask *what population was enumerated, and was it enumerated from the thing that
CONSUMES the resource, or from the last document that mentioned it.*

**Not a defect of the routing seat.** `2.0.0_SA_COO~B` measured what its own blocked cell needed,
stated it at the right grain, and routed rather than widened. The count grew confident in transit,
not at origin.

## Second finding — row `MDPF_GLOBAL-S2`

**The order's stated MECHANISM for the `comp-iam` blindness does not hold for this role.** The
preflight says the `statements: 0` is because "the policy comes from `data.aws_iam_policy_document`".
It does not: `infra/aws/terraform/mdpf-pipeline/iam.tf:41-45` declares
`aws_iam_role_policy.mdpf_runner` with `policy = jsonencode({...})` — **inline** — and `comp-find
'aws_iam_policy_document'` over that whole root is a **measured zero across 15 files**.

The data-source cause is true of `irpt-directory-refresh-role`, where `IRPT_BCKEND-S50` measured it.
It was generalised onto this role in good faith and is false here. The symptom is not in doubt (two
independent runs read zero); only the explanation is, and the true cause here is **unestablished** —
the row asserts none.

The order's *decision* was right regardless: `comp-iam` is excluded as a grading instrument either
way. I recorded it because **a wrong cause is more durable than a wrong count** — the count had a
tripwire on it, the cause did not, and a seat who learns this blindness as data-source-specific will
trust `comp-iam` on the next inline-policy role and read its zero as an empty policy.

## Errors and near-misses

- **My negative control did not discriminate, and I nearly let it stand.** It returned `READ-OK` for
  a nonexistent prefix, because `MdpfFeederBucketRW` grants `s3:ListBucket` **bucket-wide** on
  `opal-data-mdpf` with no prefix condition — so listing an absent prefix is an empty set at rc=0. It
  measured bucket-level ListBucket, not prefix scoping, and bounds nothing. Recorded in `IAM1-AC5`
  rather than counted as satisfied. Only the positive control is load-bearing in the AC1 verdict.
- **My first policy summary omitted `Condition` blocks** and so implied bucket-wide `ListBucket` where
  the live statements are prefix-conditioned. The host sweep caught it: `accounts_v2` reads while its
  two siblings deny, which is only explicable by the condition at `iam.tf:363`. Measuring beat my own
  summary of the same object.
- **Three rail gates fired on me, all correct** — twice for piping a census into `head`, once for a
  directory-scoped raw grep. Worth logging: **the rail's abort is whole-call**, so each denial also
  silently dropped the *later* segments of the same call (a `wc -l` and a second grep never ran and
  said nothing). No conclusion here rests on a truncated census.
- **`proof-of-spec-check` refused my first instance with 15 violations and was right every time**,
  including the substantive one: `expect` is graded as a **regex** against `output_evidence`, so my
  prose bar could never match. Its announcement that row-id-less surprises "would REFUSE under a tree
  TO" is what made me open MDPF_GLOBAL's channel instead of burying two findings in my own
  deliverable. I had initially decided *not* to mint the channel; that was wrong and the gate corrected it.
- **A correct path read as ABSENT for one call** because the order file was renamed mid-read
  (`MDPF_GLOBAL.IAM1` → `MDPF_GLOBAL.TO-IAM1` at `85f58dfd9c`, the CTO fixing its own id shape). I ran
  a positive control beside the absence rather than concluding the file was missing.

## Compiler Tools

| tool | invocation | what it decided |
|---|---|---|
| `comp-find` | `comp-find 'mdpf-runner-scoped' --limit 30` | Located the role's ONLY terraform declaration, `infra/aws/terraform/mdpf-pipeline/iam.tf:42`, off a 381-hit census — the surface any re-cut must name. |
| `comp-find` | `comp-find 'aws_iam_policy_document' infra/aws/terraform/mdpf-pipeline --limit 20` | **The measured zero that falsified the order's stated cause** (S2): 0 hits / 15 files scanned. A zero with a printed denominator, which is the only kind worth citing. |
| `comp-read` | `comp-read .../iam.tf --enumerate 'Condition\|s3:prefix\|ListScoped'` | 34 hits / 798 lines. Established the estate's grant SHAPE — every `ListBucket` on this role prefix-conditioned via `StringLike s3:prefix`, never bucket-wide — and `:363` independently explained the sweep's accounts_v2-reads/siblings-deny split. Second instrument agreeing with the first. |
| `comp-read` | `comp-read directory_runner.py --for '<reads/writes/firms>'` | Gave the three firm source adapters that define the true read population — the read that produced 10 rather than 9. |
| `proof-of-spec-check` | `python .tools/proof-of-spec-check.py <instance> IAM1-AC1..AC5` | INVALID rc=1 (15 violations) → VALID rc=0 after repair. The gate was the authority, not my reading of it. |
| `comp-schedule` | **NOT RUN** | The order requires the `--cursor START` re-run **before applying**. No apply was reached, so it is carried forward **UNDISCHARGED**, not reported clean. Its prior run was `PARTIAL_OR_BLIND` (107,490 of 195,832 files), so nobody has established the absence of a schedule gate on this role. |
| `comp-iam` | **NOT RUN as a grading instrument** | Expressly declared NOT VALID as this order's preflight. Running it would invite a false FAIL. |

## State at close

- **Sweep instrument:** `s3://opal-data-mdpf/diagnostics/aec-irpt-iam1/irpt_prefix_sweep.sh`, ETag
  `218166601a2cd895fdca4d0ec0ca50b6`. The host's own pull printed sha256 `d17f422c…`, byte-identical
  to the local file — the bytes that ran are the bytes authored. Placed under `diagnostics/`,
  deliberately **not** `code/scripts/`, which the production dispatch s3-syncs with `--delete`.
- **SSM:** `7aee9ea9-2542-4819-a6e0-3873d793e20f` (real, Success rc=0) and
  `1beb51ee-c9b7-4936-a286-539390c28614` (planted mutant → `VERDICT: VOID`, gate fired). Both
  read-only, `/tmp` only, no inline python, per Rule 12.
- **Proof-of-spec:** `IAM1-AC1` **PASS**; `IAM1-AC2`–`AC5` **UNCOMPUTABLE-BY-CONSTRUCTION** with
  reasons. Mutant `FIRED-AS-EXPECTED`, determinism `STABLE`. `VALID rc=0`.
- **Untouched, as ordered:** `i-02448edb624a7a7cf` lifecycle, the mdpf daily chain, `iam.tf`, and any
  coordination with the base AE on this role. Zero `terraform` invocations. Zero writes to any firm bucket.
- **Open, and owned by `1.0.0_SA_CTO`:** re-cut the TO-IAM1 boundary against the measured population
  (8 denied source prefixes + 3 denied destinations = 11 grants). The act cannot be taken inside the
  current ceiling of 8 and the order forbids choosing the wider form without a re-cut.
- **Push state:** LOCAL. This lane does not push shared branches (LD-0522).
