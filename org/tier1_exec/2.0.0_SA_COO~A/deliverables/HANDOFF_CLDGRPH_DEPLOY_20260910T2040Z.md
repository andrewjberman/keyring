# HANDOFF — NFRA_CLDGRPH DEPLOY — for `0.8.0_AE_CloudComp`

**From:** `2.0.0_SA_COO~A` · **Written:** 2026-09-10 ~20:40Z · **Handed by Andrew directly.**
**This document is the whole context. Everything it asserts was measured at this seat this evening and
says which instrument said so. Where it says HELD or UNMEASURED, treat it as unproven and measure it.**

---

## 1. AUTHORITY, AND ITS EXACT EDGES

**Andrew-direct 2026-09-10 ~20:2xZ, verbatim, at the `2.0.0_SA_COO~A` terminal**, answering a card that
asked *"Does the graph work get DEPLOYED, knowing every run texts your phone?"* whose option (a) was
*"deploy tonight and take the pages"*:

> Rec (a) for call 1.

Full record: `org/tier1_exec/2.0.0_SA_COO~A/deliverables/ANDREW_DIRECT_20260910_202xZ_CLDGRPH_DEPLOY_AUTHORIZED_PORTAL_PAT_SET.md` @`cdc768c997`.

⛔ **WHAT IT AUTHORIZES:** the acts below, on `NFRA_CLDGRPH`, **including the SNS publishes they cause and
the SMS that reaches his personal mobile.** That page is expected and accepted.

⛔ **WHAT IT DOES NOT AUTHORIZE, and no reader may stretch it:** it is **NOT** a general lift of the
estate-wide exclusion of egress from agent autonomy; it is **NOT** a push word (every commit stays LOCAL
until he says otherwise); it is **NOT** a change to the SMS subscription, which is a separate card still
his; and it reaches **no other project**.

## 2. YOUR LANE — MEASURED, so you do not have to find out by refusal

`check_agent()` from `.tools/owned-paths-validate.py`, against `.owned-paths.yaml` **pulled at HEAD with
`git show`** (204,508 bytes) rather than read by path, because on a tree this dirty the worktree copy is a
different object.

| path | `0.8.0_AE_CloudComp` |
|---|---|
| `infra/aws/lambda/globgrph/incremental_updater/incremental_updater.zip` | **PERMIT** |
| `infra/aws/lambda/globgrph/incremental_updater/lambda_function.py` | **PERMIT** |
| `infra/aws/globgrph/derive_stitch.py` | **PERMIT** |
| `infra/aws/terraform/globgrph/item2b.tf` | **PERMIT** |
| `org/critical_paths/change_management/` | **PERMIT** |

Its `~A` lane reads the same. **`2.0.0_SA_COO~A`, `1.0.0_SA_CTO` and `0.0.0_AB_MSTR` are REFUSED on all
four** — which is why this is a handoff and not a dispatch. Controls that discriminate were run beside it
(my own drive log PERMITs me and REFUSEs you; the project's task-order path PERMITs all three), because my
first run of this checker was mis-called and returned `REFUSE` for everything, including paths I had
committed to six times the same evening. **A detector that cannot return PERMIT is not a measurement.**

### 2.1 Your SEATING is clear too — a different plane, measured separately

⛔ **A CLEAN `PERMIT` IS EXACTLY WHAT AN ENCUMBERED LANE LOOKS LIKE.** `check_agent` answers *"may this
serial write this path"*. It does **not** answer *"does this serial already owe work somewhere else"*, and
Rule 27's **one project per Tier-2 seat instance** is enforced on that second plane by
`.tools/to-decomp-ref-lint.py`, which refuses a new order addressed to an instance holding open orders on
another project. `2.0.0_SA_COO` surfaced this at 95582 about a different seat, and it was right to.

**Measured this turn, over every task-order face in the estate:** 210 faces scanned, 210 carry an
`<issued_to>`; **non-terminal orders addressed to any `0.8.0_AE_CloudComp` serial: 0.**
**Positive control on the same sweep:** `0.7.0_AE_CloudOps~W` returns **2** (`NFRA_OUTSET` `TO-OS-s-22`
and `TO-OS-s-23`, both `pending`), which matches what that seat's own issuer reported independently.

**So the seat Andrew chose is permitted AND unencumbered.** The `~W` collision that the other COO warned
about does not reach you.

## 3. NEVER-2 — BEFORE YOU TOUCH ANYTHING

Open a ledger entry at `org/critical_paths/change_management/` **at the start** and close it **at
completion**. ⛔ **I deliberately did NOT open one for you**: an entry opened by a seat that will not
perform the act creates exactly the artifact the law warns about — an OPEN entry that proves only that one
device saw no completion. **The performer opens and closes its own.**

Never leave either act half-landed. Finish in session or roll back and escalate loudly.

---

## 4. ACT A — THE KEY-COLLISION FIX ONTO THE UPDATER LAMBDA

**Do this one FIRST and on its own.** It stops a live record being destroyed on every S3 write, and on the
evidence below it pages nobody by itself.

### 4.1 The trap that makes this act look done when it is not

`infra/aws/terraform/globgrph/item2b.tf` defines `aws_lambda_function.globgrph_incremental_updater` with:

```
s3_bucket        = "opal-313476888478-lambda-artifacts"
s3_key           = "globgrph/incremental_updater.zip"
source_code_hash = filebase64sha256("${path.module}/../../lambda/globgrph/incremental_updater/incremental_updater.zip")
```

⛔ **THE HASH IS COMPUTED FROM THE TRACKED REPO ZIP, AND THAT ZIP STILL CONTAINS THE PRE-FIX CODE.**
Measured this turn by opening it:

```
incremental_updater.zip   21,323 bytes   sha256 2e4693a373c5ff78
  lambda_function.py   35,213 bytes   2026-07-15 15:12
  _provenance.py       27,072 bytes   2026-07-10 01:26
```

The **zipped** `lambda_function.py` still declares `def _match_filter(arns: list[str], ids: list[str]):`
and still writes `"id": bucket, "arn": bucket_arn, "type": "S3_BUCKET",` — the collision itself.
The **worktree** source declares `def _match_filter(keys: list[tuple]):`. They are not equal.

**So: apply without rebuilding the zip and `source_code_hash` does not move. Terraform reports no change,
the deploy reads clean, and production keeps the bug.** This is surprise row `NFRA_CLDGRPH-W1-S51`,
ARMED, and it is step 1 of this act rather than a follow-up.

⚠ `infra/aws/lambda/globgrph/incremental_updater/__pycache__/lambda_function.cpython-312.pyc` is **also
tracked and also stale**. It is not read by Lambda; decide whether it belongs in the repo at all, but do
not let it into the zip.

### 4.2 The sequence

1. **Rebuild the zip from the current source**, containing exactly the two members the existing zip has and
   nothing else: `lambda_function.py` and `_provenance.py`, both at the repository root of the zip (no
   directory prefix). Both live in `infra/aws/lambda/globgrph/incremental_updater/`.
2. **Verify by reading the rebuilt bytes back**: open the new zip, confirm two members, and confirm the
   zipped `lambda_function.py` is byte-identical to the worktree file. Do not trust the zip command's exit
   code — read the member back.
3. **Commit the rebuilt zip** (`safe-commit.sh`, your own author line). This is what makes
   `source_code_hash` move, so it happens before the apply.
4. **Upload to `s3://opal-313476888478-lambda-artifacts/globgrph/incremental_updater.zip`.** This is the S3
   write Andrew's word authorizes.
5. **`safe-apply`** on `infra/aws/terraform/globgrph`. Never bare `terraform apply`; never
   `aws lambda update-function-code` (Terraform-only for Lambda).

### 4.3 How to prove it landed — against the SERVED artifact, not the plan

- `aws lambda get-function --function-name opal-globgrph-incremental-updater` and compare
  `Configuration.CodeSha256` to the base64 SHA-256 of the zip you built. **A plan that says "1 changed" is
  a DESIRED state, not an APPLIED one.**
- Then the real acceptance, and the instrument already exists: round 9's settle harness at
  `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/i1_settle.py` reads the warehouse
  table directly from this estate through the producer's own S3 metadata pointer — no Trino, no Athena.
  Its pre-fix reading was `DESTROYED_BEFORE=2`. **After the deploy and after at least one S3 write has
  flowed through the updater, that count should stop growing.**
- ⚠ **The collision is FIVE class pairs, not one** (row `W1-S49`): bucket/policy 12, role/lambda 8,
  rule/lambda 8, project/role 1, rule/document 1, over 30 of 27,632 two-claimed strings. The fix closes all
  five. If your reading shows only the bucket pair moving, something is partial — say so rather than
  rounding it to success.

### 4.4 Rollback

The pre-fix zip is the object currently in git and currently in S3. If the apply misbehaves: re-upload the
pre-fix bytes to the same key and `safe-apply` again. Nothing here is destructive to data; the risk is a
function that fails to import, which the CodeSha256 read plus one invocation log will show immediately.

---

## 5. ACT B — THE STITCH PRODUCER FIXES. ⛔ READ 5.1 FIRST; ITS MECHANISM IS NOT WHAT I TOLD ANDREW.

`infra/aws/globgrph/derive_stitch.py` now carries three landed changes: round 8's prior-cycle drop-on-read,
round 9's rebuild of the dangling-check key set after the collapse, and round 9's moved fold licence
(`SOLE_WRITTEN_EDGE_TYPES` + `SOLE_WRITERSHIP_EVIDENCE` + `drop_prior_cycle_edges`, which refuses to
type-delete a term that is not sole-written).

### 5.1 ⛔ CORRECTION, MEASURED AFTER I HAD ALREADY DESCRIBED THIS ACT

I told Andrew and the CTO that act B was *"CodeBuild build, image push, derive run."* **The image-push half
is wrong and I am correcting it here rather than letting you discover it.**

`infra/aws/terraform/globgrph/stitch-produce.tf` defines `aws_codebuild_project.stitch_produce` with:

```
source { type = "S3"  location = "${local.stitch_globgrph_bucket}/${local.stitch_source_key}" }
```

on a **stock `aws/codebuild/amazonlinux2-x86_64-standard:5.0` image**, whose buildspec runs
`python3 infra/aws/globgrph/derive_stitch.py --out /tmp/stitch_graph.json`. **There is no Opal image to
build or push for this producer.** It executes whatever `derive_stitch.py` is inside the **source zip in
S3**. The nightly Fargate derive-runner is repo-less, so the stitch cannot ride it — the workflow file says
so in its own header.

⛔ **THEREFORE: THE FIXES REACH PRODUCTION ONLY WHEN THE S3 SOURCE ZIP IS REFRESHED. Nothing else moves
them.** Committing to `CLOUD` does not.

### 5.2 And the committed route to refresh it has never worked

`.github/workflows/stitch-source-push.yml` is LEG-1, the publisher of that source zip. Round 9 measured it
(row `NFRA_CLDGRPH-W4-S10`): **855 runs, 8 successes — all inside one 103-minute window on 2026-07-07, all
BEFORE the step that packs `portal/src` landed, so all eight published archives with zero portal files.
Since that step: 847 runs, 0 successes**, dying every time at `Checkout portal` on an unprovisioned
`secrets.PORTAL_REPO_PAT`. **Correct publishes by the committed route, ever: 0 of 855.** All five zips that
have actually served came from a hand route.

**Andrew has said the credential gets set** (same message, *"for Call 3, we need this credential set"*): a
fine-grained token scoped READ-ONLY on the private `Opal-Capital/portal` repo, added as repo secret
`PORTAL_REPO_PAT`. It is needed because `portal/` is a bare gitlink rather than a registered submodule, so
the default `GITHUB_TOKEN` cannot read a separate private repo.

### 5.3 So act B has two routes, and the choice is yours to make and state

- **B-1, the committed route.** Wait for the secret, then `workflow_dispatch` the workflow on `CLOUD`. The
  zip is then published by the mechanism the estate intends, WITH portal files, and the nightly CodeBuild
  consumes it. **Slower, and correct.**
- **B-2, the hand route.** Publish the source zip to the S3 key yourself. **Faster, and it re-does by hand
  the thing this project spent rounds retiring**, and a zip packed by hand may miss `portal/src` exactly as
  the 8 "successful" runs did — which is the defect that started this.

⚠ **UNMEASURED BY ME AND YOURS TO MEASURE BEFORE ACTING:** whether either route's build publishes to the
SNS topic carrying the SMS subscription. Andrew's word covers the page either way, but your ledger entry
should say what you expect and what happened.

**MY RECOMMENDATION, and it is only that:** take **B-1**. Act A is the one that stops active damage and it
does not depend on any of this. Act B's fixes are a producer that has not run correctly since July; one
more night on the correct route is cheap, and the hand route is how the portal layer went empty for two
months without anyone noticing.

### 5.4 If you take B-1, one thing to check that nobody has

The workflow's `push:` trigger fires on `CLOUD` across five path globs including
`infra/aws/globgrph/derive_stitch.py`. **The day the secret works, a production input that has moved about
five times in 65 days starts moving on every qualifying push.** That is a NEVER-2-class cadence change
arriving disguised as a credential. Andrew has been asked whether he wants the trigger restricted to
`workflow_dispatch` only, and **had not answered when this was written.** Do not decide it for him; if he
has not answered by the time you act, say so in the ledger entry.

---

## 6. WHAT NOT TO DO

- **Do not perform the `STORED_IN` retirement.** Round 9 made it *available* and explicitly did not take
  it. Row `W2-S80` found it was always a **two-edit** act: `derive_runner.py:2276`'s `STITCH_EDGE_TYPES`
  allow-list does not contain `OWNED_BY`, and no cell in any round has ever named that second edit.
- **Do not add a type to `SOLE_WRITTEN_EDGE_TYPES`** without re-running the writer census. That table is a
  licence to type-delete, and its own comment states its expiry: sole-writership is a fact about today, not
  a property of a term.
- **Do not build, propose or wire any alert, alarm, monitor or notification.** Standing moratorium.
- **Do not push.** Every commit stays local until Andrew's word.
- **Do not read this document as authority on any project other than `NFRA_CLDGRPH`.**

## 7. IF YOU FIND SOMETHING ODD

Append ONE row to
`org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md`
(`spec_asserts` + `world_is`, a real `surfaced_at` minute, your own row id) and **keep working**. Do not
halt to investigate, and do not send a broker message as the carrier. The file is append-only: never edit an
existing row, and restate the denominator by parsing every fenced JSON block. It stood at **291 rows** when
this was written.

**Questions about scope go to `1.0.0_SA_CTO`; anything about this handoff comes back to `2.0.0_SA_COO~A`.**

**Push state, measured at this write:** every hash named here is LOCAL. Andrew holds the push.
