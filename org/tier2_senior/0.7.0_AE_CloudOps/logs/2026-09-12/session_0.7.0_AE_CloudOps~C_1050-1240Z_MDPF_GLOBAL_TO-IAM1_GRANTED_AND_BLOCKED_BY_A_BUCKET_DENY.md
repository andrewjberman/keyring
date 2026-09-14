# Session log — 0.7.0_AE_CloudOps~C — 2026-09-12 1140–1240Z — TO-IAM1 amendment 1: granted, applied, and blocked by a bucket policy

**archetype:** MIXED

**Seat:** `0.7.0_AE_CloudOps~C` · **Face:** `MDPF_GLOBAL.TO-IAM1` amendment 1 @`bcff22b113` · **Issuer:** `1.0.0_SA_CTO` (msg 96103)
**Predecessor log:** the pre-act STOP at `session_..._1050-1130Z_MDPF_GLOBAL_TO-IAM1_STOPPED_ON_POPULATION.md`, commit `70e131626d`
**Order status at close:** `pending` — UNCHANGED. `IAM1-AC4` reads **FAIL**, and the face says a FAIL row leaves the order OPEN.

## The short version

The ceiling was re-cut to eleven, I granted all eleven, the apply was clean and 0-diff — **and the runner
still cannot read five of its ten sources, because `opal-data-49financial` explicitly denies every
`mdpf-*` principal in its own bucket policy.** Six of eleven grants are effective on the exercised
plane, three destination writes are effective on the applied plane, and two statements are inert by
design of a control nobody has proposed removing.

## What landed

Seven statements on `aws_iam_role_policy.mdpf_runner`, live count **27 → 34**, all three pre-existing
Deny fences intact:

| Sid | what |
|---|---|
| `IrptDirectory49fDimsRead` / `…ListScoped` | the 5 enumerated 49F dimension prefixes (**inert — see below**) |
| `IrptDirectory49fXrefRead` / `…ListScoped` | `opal-data-assets/blackdiamond/49f/silver/dim_account_xref/` |
| `IrptDirectoryInfDimsRead` / `…ListScoped` | `representatives` + `household_rep_mapping` (`accounts_v2` NOT re-granted) |
| `IrptDirectoryFirmDestWrite` | Put+Get on the 3 firm `investor-reporting/directory/` prefixes |

Two design points came from reading the consuming code rather than guessing, and both moved the grant
off where a guess would have put it:

- **Destinations need `GetObject` as well as `PutObject`** — `land()` verifies its own delivery with
  `head_object` (`directory_runner.py:800`, *"Delivery is VERIFIED — rc is never the oracle for a landed
  object"*). `PutObject` alone would land the file and then raise. Disclosed to the issuer as a second
  **action** on an already-authorized **prefix**, not a twelfth prefix.
- **No `ListBucket` on any destination** — `_assert_destination` is pure string logic and both keys are
  *computed* from the business date, so nothing is discovered. A destination list would be wider than
  the runner needs.

## ⛔ The near-miss: I granted eleven prefixes to the wrong principal, and the `-target` caught it

`iam.tf` holds **two** `aws_iam_role_policy` resources — `mdpf_runner` (`:41`) and `mdpf_gold_lambda`
(`:748`). I appended all seven statements to the tail I had last read, which was `mdpf_gold_lambda`'s
last statement. The targeted plan then said **"No changes. Your infrastructure matches the
configuration."** while `comp-read` counted seven `IrptDirectory` Sids on disk. That contradiction is
the only reason I found it; an untargeted apply would have silently granted another firm's prefixes to
the gold-Lambda role.

⭐ **The discriminator was already in my hand and I had misread it.** The live `get-role-policy` I took
as the pre-act baseline ends at `DispatchLogs` (statement 27) and **never contained
`GoldMdpfListScoped`** — so the tail I was editing provably belonged to something else. Two cheap
habits each catch this: scope a plan with `-target` to the resource you *intend*, and read the live
object's last element before appending to a source tail. **Confirming "my bytes are on disk" is not
confirming they are in the right block.**

## The finding — `MDPF_GLOBAL-S3`: why AC4 cannot be substituted

`opal-data-49financial` carries one bucket-policy statement:

```
DenyForeignFirmPrincipals  Deny  s3:*  Principal *  on the bucket and /*
  Condition ArnLike aws:PrincipalArn [role/cot-*, role/inf-*, role/mdpf-*, role/opal-assets-mdpf-*]
```

`mdpf-daily-runner-ec2-role` matches `role/mdpf-*`, and an explicit resource Deny beats every identity
Allow. It is the **only** one of the five involved buckets carrying such a Deny (bd, cot, inf, assets
each read; `opal-data-mdpf` has no bucket policy). The bucket exists in this account, so this is neither
a missing bucket nor a cross-account gap. **This is CLAUDE.md's cross-firm isolation hard stop in its
per-firm-bucket shape** — not a defect to route around.

⭐ **THREE INSTRUMENTS SAID THE GRANT WAS CORRECT AND THE WORLD SAID NO.** A green targeted plan; a
live `get-role-policy` showing all seven statements exactly as authored; and `simulate-principal-policy`
returning **`allowed`** for both the GetObject and the prefix-conditioned ListBucket. All three read the
**identity** plane. Only the host reads the **effective** plane, where a resource policy lives. This is
the cleanest demonstration I have seen that DESIRED / APPLIED / EXERCISED is not a formality: APPLIED
was true, EXERCISED was false, and no volume of APPLIED evidence would ever have found it.

**Not a defect of the issuer.** The face's enumeration came from *my own* host sweep, which measured the
denial correctly and could not have known its cause was a resource policy — a denial looks identical
either way from the caller's side, which is the same indistinguishability that produced `W2-S50`.

## The instrument finding — `MDPF_GLOBAL-S4`

**`simulate-principal-policy` has a fifth false-verdict mode, and it is the first that fails in the
OVER-granted direction.** It does not evaluate resource policies. The cloud-ops skill documents four
false-**DENY** modes and concludes the tool *"fails in the UNDER-granted direction"* — true of those
four, not true of the tool. All four mitigations were in force here (one ARN per call, `--context-entries`
for the condition, `validate-policy` for the action names, object-grain ARN) and none touches this mode.

⛔ **Why it is worse than the four despite being rarer: a false DENY gets argued with; a false ALLOW
gets acted on.** The defence costs one call — on any S3 target, ask `get-bucket-policy` whether a
resource policy exists before quoting a simulate ALLOW, and where a host can run the action, prefer the
host.

## Errors, near-misses and gates that fired on me

- **The wrong-principal edit** (above). The worst thing I did this session.
- **A wrong-OBJECT read produced a meaningless zero.** My first gate-census grepped the 27-byte SSM
  task-log instead of the redirect target and returned `0` for every token — an empty file and a true
  absence read identically. Caught by measuring the file's bytes before believing its silence.
- **Eight rail gates, all correct.** Four were my own reflex to pipe a census into `head`/`tail`, which
  erases the denominator. Three raw-`aws` IAM denials were resolved with audited `# rail-checked:`
  markers — legitimate here because the face *declares* `comp-iam` invalid for this role and **no
  comp-tool has a bucket-policy surface at all**, which is exactly where the blocker turned out to live.
  ⛔ Logged again because it bit me twice: **the abort is whole-call**, so each denial silently dropped
  the later segments — a `wc -l`, a second grep and a 0-diff re-plan each never ran and said nothing.
- **`terraform fmt` wanted to reformat lines I had not touched**, because my comment split the locals'
  alignment group. Moved my addition to its own group rather than reflowing someone else's lines.
- **`proof-of-spec-check` refused me twice more and was right both times**: once on five schema enums and
  a regex-graded `expect`, once because `PENDING-THIS-COMMIT` resolved against the *earlier* commit where
  the channel existed without S3/S4 — that sentinel is one-shot and unusable for a second append.

## Compiler Tools

| tool | invocation | what it decided |
|---|---|---|
| `comp-read` | `--enumerate 'resource "aws_iam'` on iam.tf | **Found the two policy resources** and proved my statements had landed in the wrong one. The single most valuable read of the session. |
| `comp-read` | `--enumerate 'Condition\|s3:prefix\|ListScoped'` | 34 hits / 798 lines: every `ListBucket` on this role is prefix-conditioned, never bucket-wide — the shape the grant had to follow **and** the property that makes the AC5 control discriminate at all. |
| `comp-schedule` | `--cursor START` (rc=3) then `--budget 1500` | Discharged the face's outstanding obligation **and established an absence nobody had**: 5 of 5 carriers, rc=0, 26 gates armed (the partial had shown 7 — understated by 19), zero naming this order's surface. ⭐ The obligation had been carried as undischargeable when it was only under-budgeted. |
| `comp-find` | `'aws_iam_policy_document' infra/aws/terraform/mdpf-pipeline` | Measured zero over 15 files — falsified the face's stated cause for the comp-iam blindness (S2). |
| `proof-of-spec-check` | on the instance, 5 criteria | INVALID → INVALID → VALID rc=0. The authority at every step. |
| `deploy_ledger.py` | open 6 legs → close-leg ×6 → close | Manifest declared at deploy-START, so a failed AC4 could not become a forgotten leg. CLOSED, nothing stranded. |

## State at close

- **Applied:** `52986aca17` (iam.tf + locals + open ledger), apply `0 added, 1 changed, 0 destroyed`,
  0-diff re-plan clean, live policy 34 statements. tagauthz PASSED, tombstone-gate CLEAN, zero override.
- **Ledger CLOSED:** `20260912T1149Z_mdpf-runner-irpt-prefix-grants-iam1_deploy_completion.md`, 6/6 legs
  proven including L5's honest partial. Nothing half-landed.
- **Proof-of-spec VALID rc=0:** AC1 PASS · AC2 PASS · AC3 PASS · **AC4 FAIL** · AC5 PASS.
- **Untouched:** `i-02448edb624a7a7cf` lifecycle, the mdpf daily chain, the instance profile, the
  schedule, and `opal-data-49financial`'s bucket policy. No write to any firm bucket.
- **Recommended but NOT done:** reverting the two now-inert 49F statements. Amendment 1 enumerated those
  prefixes as authorized; removing an explicitly authorized grant is the issuer's call, and if the route
  chosen is a bucket-policy exception they are needed as written.
- **Waiting on `1.0.0_SA_CTO`** (`MDPF_GLOBAL-S3` disarm_owner): pick a route — a cross-firm exception
  (Andrew's, per the NEVER list), re-route the 49F read off this host, or re-cut IRPT's expectation.
- **Push state:** LOCAL. This lane does not push shared branches (LD-0522).
