# MANDATE -- `2.0.0_SA_COO~Y` -- AMGT **Lead Panel**, step 2: the H03 chatter gold cutover (B01 · B09 / H1-H4)

**Authority:** Andrew-direct 2026-09-24 ~02:4xZ at the `1.0.0_SA_CTO~Z` terminal: *"I also want the 'Lead
Panel' mandate for COO~Y who I can bring up any time"*, plus *"you have egress for whatever calls you want"*
(R-15). **Contract:** `CONTRACT.md` (this folder). **Trace:**
`org/tier1_exec/4.0.0_SA_CRO/deliverables/LEAD_PANEL_END_TO_END_GAP_BRIEF_20260923.md` + `.evidence.json`.
**Proposal:** `CLOSER_PROPOSE_LEADPANEL_20260924.md` @`d2bbf82b3f`.

## YOUR ONE STEP -- and it is the one the whole surface is waiting on

⭐ **THE READ PATH ALREADY WORKS END TO END. "WHAT IS UNFINISHED IS THE WATER, NOT THE PIPES."** Your step is
the water. Four of the panel's six steps are cosmetic-to-structural adapter work; **yours is the only one that
changes what a user actually sees in the list.**

**Today, measured on deployed bytes:** the chatter producer ranks over **`names_with_links=3` of 250 names**.
Trending x Chatter serves **TWO rows** (BA US, HD US) with **`score 0`** and **`raw_chatter_count 0`**, ranked
on `window_total_count` 1 and 2. **Breakout x Chatter has committed EMPTY for NINE CONSECUTIVE DAYS**
(`NO_SIGNAL_IN_WINDOW`, **189 of 191**). The empty-arm mechanics are CORRECT and disclosed -- **the input is
what is missing.**

**THE CAUSE IS FOUR FACTS, all measured:**
1. **The deployed zip predates the fix.** `amgt-resapp-chatter-axis` CodeSha256
   `I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=`, 669,924 bytes, @2026-09-19T09:49:46Z. Inside it
   `chatter_axis.py` is **37,443** bytes and `pool_reader.py` **24,238**; at HEAD they are **40,666** and
   **30,850**. The delta is commit **`fd9449f246`** (2026-09-22, `0.9.0_WK_AMGT_HARVST~7`, *"chatter axis ranks
   from the graded chatter_daily table"*). ⭐ **The local build artifact
   `infra/aws/terraform/harvest/.build/chatter-axis-producer.zip` has the SAME digest as the deployed function**
   -- so the build input is stale too, not just the deploy.
2. **`DEFAULT_SOURCE = "legacy"`** at `chatter_axis.py:427`. **Even the HEAD bytes rank over legacy unless the
   source is switched.**
3. **The role lacks the gold prefix** (`amgt-resapp-chatter-axis-role`).
4. **The function carries no environment at all** -- so a source env var does not exist to set yet.

## WHAT TO DO

**Rebuild the zip from HEAD** (so `fd9449f246`'s `gold_daily_mention_scores` is in the bytes) · **add the gold
prefix to `amgt-resapp-chatter-axis-role`** · **set the source to `gold`** (an env var the function does not
carry today, or move the default) · **deploy through TERRAFORM** · **let the ENABLED 10:00Z schedule land**
(`amgt-resapp-chatter-axis-daily`, `cron(0 10 * * ? *)`, one invocation and zero errors on each of the last
three days -- **the schedule is healthy; do not touch it**).

**PROOF, and each clause carries its denominator:**
- the next `_CURRENT` pointer for `TRENDING_CHATTER` with **`row_count` on the order of the universe, not 2**;
- rows carrying **non-zero `raw_chatter_count`** (today every one is 0);
- the run line's **`names_with_links` above 3, printed WITH ITS DENOMINATOR (250)** -- ⛔ **a bare
  "names_with_links improved" is not a proof clause; the ratio is the claim**;
- the served list showing those rows **through hop 2 unchanged** -- you change the producer, not the route.

⭐ **AND YOUR STEP SHOULD END THE `BREAKOUT_CHATTER` EMPTY STREAK.** If it does not, that is a finding worth a
blocker message, not a silent pass -- `189 of 191` names having no signal is a claim about the INPUT, and your
step replaces the input.

## ⭐ A DESIGN INPUT THAT DECIDES *WHICH* CUTOVER FORM TO USE (`3.0.0_SA_CVO~Z`, msg 25187, baseline @`0c802d124d`)

⛔ **THE DEPLOYED CHATTER FUNCTION HAS NO DURABLE FIRST-PARTY ARTIFACT.** `get-function` returns
`RepositoryType S3` pointing at a **LAMBDA-MANAGED SNAPSHOT**, not an artifact bucket this estate controls.
Unlike `opal-amgt-scoped-api`, whose artifact of record is the versioned
`research/opal-amgt-scoped-api.zip`, **this function's ONLY stable identity is its `CodeSha256`
(`I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=`, CodeSize 669,924, RevisionId
`e37b6030-cf2e-4ea3-b4d4-ade683745880`) -- the deployed bytes CANNOT BE RE-FETCHED from anywhere we own.**

⭐ **SO THE CUTOVER FORM IS NOT A TIDINESS QUESTION. Moving this function to `yang-lambda` S3-metadata
CLOSES that gap; keeping `filename` / `filebase64sha256` PRESERVES it.** ⛔ **PREFER THE S3-METADATA FORM, and
the reason is durability of the artifact of record, not convention.** It is the same shape as the cutover's
`C2` -- a hash-bound identity with no durable artifact -- except here it is the **PRE-EXISTING** state rather
than something a cutover creates. ⚠ **A cutover that improves the code and preserves the
no-durable-artifact condition has fixed the water and left the record un-refetchable.**

⚠ **That seat did NOT reproduce the snapshot URL anywhere -- it is PRESIGNED and carries a live credential --
and it verified its committed record carries no `X-Amz-Signature` / `Security-Token` / `Credential` before
committing. Do the same: the URL is a secret, not a coordinate.**

## ⛔ THREE GATES ON THIS STEP. NONE IS LIFTED BY THE EGRESS GRANT

1. ⛔ **THE NEVER-WIDEN SIGN-OFF PAIR (CTO + COO halves) IS REQUIRED, because this deploy MOVES SERVED OUTPUT.**
   Name in your half **what the act MAY touch and the rollback for each key**, and read the outcome **from the
   producer's own rule**, not predicted from the input's shape. ⚠ **COUNT THE WRITERS OF EVERY PROPERTY YOU
   NAME** -- a property with N writers needs N rules read, and N is a number your half prints. **Request the
   CTO half from `1.0.0_SA_CTO~Z` when the candidate is ready; do not deploy on one half.**
2. ⛔ **TERRAFORM ONLY.** Never `aws lambda update-function-code`; never a bare `terraform apply` -- use
   `safe-apply`. ⚠ **AND THE ARTIFACT-OF-RECORD TRAP ON THIS FAMILY: `modules/yang-lambda` reads the S3
   object's `content-sha256` METADATA as `source_code_hash`, NOT the bytes. Build and upload FIRST, then
   apply** -- a rebuild from source after upload produces unsigned bytes that still pass a filename check.
3. ⛔ **THE DEPLOY LEDGER** (`org/critical_paths/change_management/`): opened at start, closed at completion.
   **An image/artifact act names EVERY task family that pulls the tag it moves.**

⭐ **EGRESS: R-15 grants the vendor word for the price pull and the Refresh proof ONLY. YOUR STEP NEEDS NO
VENDOR WORD AND MAKES NO VENDOR CALL** -- it reads the **graded `chatter_daily` gold table**, not Bloomberg.
Stated so nobody reasons from a grant that does not apply here. **If your work turns out to need a vendor call,
that is a blocker message, not an inference from R-15.**

## YOUR WRITE SURFACE (already granted -- exercised, not assumed)

`lib/research/metrics/{chatter_axis,generation_writer}.py` · `lib/research/coverage/pool_reader.py` ·
`lib/opal_data_harvest/**` -> `lib/research/harvest/**`, plus the Terraform and role changes this step needs.
**These resolve to lane `BASE_EXEC` and permit `~Y`** (same resolution verified for `~Z` on the peers path at
R-14, with a working negative control). **A refusal at a path this table gives you is a BLOCKER message, never
a workaround.**

## ⚠ TWO THINGS ALREADY ON YOUR PLATE THAT TOUCH THIS

1. **`AMGT_HARVST` clauses 5 and 6 are ratified IN TEXT ONLY.** `pool_reader.py` at HEAD still carries the
   two-key map -- correct under clause 4's ordering, but the ratified behaviour is not in the code. **The zip
   you rebuild contains `pool_reader.py`, so this step and that debt touch the same file.** Land them
   coherently or say which you are deferring.
2. **You are LIVE on IRPT** (`irpt_y_loop_ticks`, PID 27444, branch `irpt-mvp-y-20260922`). ⚠ **This mandate
   makes AMGT a second concurrent project for this lane.** Rule 27's one-project-per-Tier-2-seat-instance exists
   to protect your CONTEXT, not the box. **Andrew asked for this mandate knowing the lane exists; if the two
   commitments collide, say so as a blocker and he sequences them. Do not silently timeshare them.**

## OPERATING RULES

**LIVE FIRST:** you do **not** own the shared first hop. `B00`/`E0` is `2.0.0_SA_COO~Z`'s and is **BLOCKED on
Andrew's browser session endpoint** (its blocker, 02:30Z). **Build against the published interface; an offline
closure counts toward NO acceptance ID until the thread is live.** Your producer work is legitimately
independent of it -- the generation lands in DynamoDB whether or not a browser has rendered it.
**FILES OVER MAIL:** overwrite `STATUS.md` in place (current state, ~5 KB, not a journal). **No ACK messages.**
One of three per message: interface published, blocker, review handoff -- each citing `path@commit`, owner,
requested action, IDs. **NO SIDE-QUESTS:** park off-thread questions as one STATUS line with owner and
un-park condition.
**Commit** via `.tools/safe-commit.sh` with pathspecs, in your own worktree (14b). ⚠ **Working branch is
`CLOUD`** (ONE TRUNK; `SITEZ` no longer exists on origin). ⛔ **COMMIT BUT DO NOT PUSH** -- `0.0.0_AB_MSTR~Z`
pushes as integrator. *(Correcting this seat's own earlier relay, which wrongly told you to pull-merge and
push.)*

**Your reviewing CVO is `3.0.0_SA_CVO~Z`.** It captured a **pre-build baseline** on the Peers surface before
any build landed, on the reasoning that *"a before-state not measured before the change can only be taken on
the BUILDER's word afterward -- the party the grade is about."* ⭐ **Expect the same here: your before-state is
`row_count` 2 and `names_with_links` 3 of 250, and it becomes unrecoverable the moment your deploy lands.**
