# ANDREW-DIRECT 2026-09-10 ~20:2xZ — CLDGRPH DEPLOY AUTHORIZED (call 1, rec a) · THE PORTAL PAT IS TO BE SET (call 3) · CALL 2 IS NOT ANSWERED, HE ASKED WHAT IT IS FOR

**Terminal:** `2.0.0_SA_COO~A`, this lane's own. **Recorded by:** `2.0.0_SA_COO~A`, same turn as receipt.
**Carrier class:** answers to a `/open-calls` run at this lane at ~20:2xZ.

---

## VERBATIM AND ENTIRE

> Rec (a) for call 1. What exactly do you need to do the second machine session on the other machine what
> exactly is the purpose for that? THen for Call 3, we need this credential set.

---

## CALL 1 — **DEPLOY AUTHORIZED. THIS IS THE WORD THE EGRESS HOLD REQUIRED.**

*"Rec (a) for call 1."* The card's (a) was, verbatim from the card: **"deploy tonight and take the pages"**,
against a call whose own text was *"Does the graph work get DEPLOYED, knowing every run texts your phone?"*

⛔ **SO THE SCOPE OF THIS GRANT IS EXACTLY THAT AND NOTHING WIDER.** It authorizes the acts that put
`NFRA_CLDGRPH`'s committed fixes onto the served plane, accepting that the derive pages his personal mobile.
**It is NOT a general lift of the estate-wide egress exclusion, NOT a push word, and NOT an answer on the SMS
subscription itself** (that card stays his and untouched). Any seat reading this record for authority to
egress on another project is reading it wrong.

### What the deploy actually consists of — MEASURED at this seat, not recalled

Two acts with different blast radii. **They are separable and the first is the one that stops active damage.**

**ACT A — the key-collision fix onto the updater Lambda.** `infra/aws/terraform/globgrph/item2b.tf` defines
`aws_lambda_function.globgrph_incremental_updater` with `s3_bucket = "opal-313476888478-lambda-artifacts"`,
`s3_key = "globgrph/incremental_updater.zip"`, and — this is the load-bearing line —
`source_code_hash = filebase64sha256(".../lambda/globgrph/incremental_updater/incremental_updater.zip")`,
the **TRACKED REPO ZIP**. Sequence: rebuild the repo zip from the fixed `lambda_function.py` → upload it to
that S3 key → `safe-apply`.

⛔ **AND ROW `W1-S51` IS NOW LOAD-BEARING RATHER THAN CARRIED.** That tracked zip **still contains the
PRE-FIX code**. A deploy that skips the rebuild ships the collision while the source reads clean, and
`source_code_hash` would not even move. **The row I filed as "carry to round 10" is step 1 of this deploy.**

**ACT B — the stitch producer fixes onto the derive image.** `derive_stitch.py` carries round 9's moved
licence and round 8's drop-on-read. It rides the derive-runner image: CodeBuild build → image push → a
derive run. **This is the act that pages him**, and under NEVER-2 its ledger entry must name EVERY task
family that pulls the tag it moves (`NFRA_CLDGRPH-S31`: two builds re-pointed **seven** families in one
night and five were counted).

### Lane, stated plainly

⚠ **NEITHER ACT IS THIS LANE'S TO EXECUTE.** `safe-apply`, an S3 write, a CodeBuild start and an
`ecs run-task` are infra-lane acts (`0.7.0_AE_CloudOps`, `0.8.0_AE_CloudComp`), and a Tier-2 seat hears an
act **only as a task order from its issuer**. This lane holds `NFRA_CLDGRPH`'s L5/L6 and does not hold
those seats. **Andrew's word removes the HOLD; it does not move the LANE, and inventing a route around
that is the shape the LD-0529 send guard exists to refuse.** Routed, with the sequence above, to
`1.0.0_SA_CTO` (to place the acts) and `0.0.0_AB_MSTR` (which holds the estate), copy to `2.0.0_SA_COO`
(CloudOps' issuer). **NEVER-2 obliges a `org/critical_paths/change_management/` entry opened at start and
closed at completion, by whoever performs it.**

## CALL 2 — **NOT ANSWERED. HE ASKED WHAT IT IS FOR, AND THAT IS A QUESTION, NOT A DECISION.**

*"What exactly do you need to do the second machine session on the other machine what exactly is the purpose
for that?"* ⛔ **This is NOT (a) and NOT (b), and it must not be recorded as either.** The card stays OPEN.
The answer given back to him, from the PRD read this turn rather than from memory:

**FWD-7, verbatim from `prd/NFRA_CLDGRPH_PRD.md`:** *"The estate keeps one graph story, and the per-machine
copy is retired rather than kept alongside."* **DONE WHEN:** *"EXERCISED -- two people on different machines
have asked the same question at the same moment and received the same answer, after the local copy was
switched off."* **ACCEPT:** *"turning off every developer machine does not change what the graph says; two
people asking the same question at the same moment get the same answer; and there is no second, older copy
anyone could still be reading from."*

**Why the existing evidence does not satisfy it (row `S22`, `absent`):** the earlier exercise drove **two
machines from ONE worker**. One process talking to itself twice cannot discriminate *"two machines agree"*
from *"one caller got its own answer back"* — which is the whole content of the outcome. **The person half
is the discriminator, not a formality.**

**What it costs him:** the other machine powered on, an agent session started on it the way this one runs,
registered under its own serial, then one question asked from each machine inside the same window. Minutes,
not an evening. **Everything else on FWD-7 is done:** the local hook pair is gone from both clones, the
cloud producer is the sole writer of the stitch key, and the laptop half is exercised and recorded.

## CALL 3 — **THE CREDENTIAL IS TO BE SET. THE CADENCE HALF IS NOT ANSWERED AND I SAY SO.**

*"we need this credential set."* **The credential gets set — that is decided.** ⚠ **He did not pick (a) or
(b), and the difference between them is the trigger restriction, not the credential.** Recorded as: the
credential is authorized; the cadence question stays open and is put back to him in one line rather than
resolved by inference in either direction.

**Exactly what it is, measured from `.github/workflows/stitch-source-push.yml` this turn:** secret name
**`PORTAL_REPO_PAT`**, provisioned as a **repo secret on the workspace repository**, holding a
**fine-grained PAT (or deploy-key-backed token) scoped READ-ONLY on `Opal-Capital/portal`**. The reason it
is needed is in the workflow's own comment: `portal/` is a **bare gitlink, not a registered submodule**, so
the default checkout leaves it empty and the default `GITHUB_TOKEN` **cannot read a separate private repo**.
**That one missing secret is what has failed 847 consecutive runs.**

**The cadence consequence, restated because it rides in with the fix:** the workflow triggers on
`push: branches: [CLOUD]` across `portal/src/**`, `data/**/scripts/**`, `org/modules/graph/**` and two
producer files. **The day the secret works, that S3 input starts republishing on every qualifying push**,
where today it moves about five times in 65 days. The restriction, if he wants it, is to drop the `push:`
trigger and keep `workflow_dispatch` only — a one-line change to a file this lane does not own.

---

**Push state, measured at this write:** this record is LOCAL. Andrew holds the push.
