# ANDREW-DIRECT 2026-08-20 ~02:4xZ — the 07:00 fallback runs UNTOUCHED: the device self-heals or the failure is the finding

**Channel:** Andrew at the MSTR~Z console, ruling the Terminal-signed-out fork. **VERBATIM:**

> "b, let the fallback try it, the whole point is that the device needs to be able to figure
> this out and get it done on its own accord. me signing in to help it out is pointless."

**Effect — the no-assist discipline, binding tonight:**
1. **NOBODY signs the Terminal in before 07:00** — not Andrew, not BG, not any seat. The
   state (wintrv dead, port 8194 dark, bbcomm freshly restarted) is left EXACTLY as found:
   it is the natural test condition for the first fully-unattended self-heal exercise.
2. **The 07:00 fire now carries a THREE-LEG read, attributed per-leg** (the chain's log
   discriminates them): (i) the DAPI precheck + AUTOMATED SIGN-IN FALLBACK — its first
   natural live fire; (ii) the WDAC/kernel leg (the remediated-env acceptance) — exercised
   only if (i) restores DAPI; (iii) publish + served verify.
3. **Branch outcomes, named in advance:** CLEAN = double acceptance (self-heal + WDAC) in
   one natural fire — the strongest possible read. FALLBACK-LEG FAILURE = the self-heal
   exercise's honest result and the day's headline finding; the WDAC read is then
   UNEXERCISED (not failed) and the acceptance-gated morning acts hold; the repair decision
   routes to Andrew FRESH on the measured failure — his ruling killed pre-emptive assist,
   it did not pre-authorize post-failure repair.
4. BG's duty: the 07:00 read with per-leg attribution, runbook HELD (capable, not
   authorized); MSTR~Z reads the served object independently. No alarm/monitor machinery
   (moratorium; BG already refused to propose one).

**FOLLOW-UP, same exchange, VERBATIM:** *"if we dont think the fabric is set up to do it,
then we need to figure out how 0.0.3 gets buzzed to do it with the login function"*
**GROUNDED ANSWER:** the fabric IS set up — OPAL_BGFALLBACK WS-1 closed 2026-08-18 with the
full unattended cycle VALIDATED LIVE (@480da: "the fill always worked — the VERIFIER was
mis-aimed"), and the login function lives IN the 07:00 chain itself (agentless: the
scheduled task is the trigger; no buzz needed; BG's runbook is the manual backstop).
Tonight = its first NATURAL fire. **The residual design gap is BETWEEN fires** (tonight's
22:15 death sat until 07:00): the moratorium-clean remedy is SCHEDULING the agentless
precheck+fill leg every few hours (a schedule, never a monitor) — proposed to fold into the
ruling-2 DAPI-precondition implementation at 0.5.0~Z, pending Andrew's word.

**SECOND FOLLOW-UP — THE DESIGN RULING, VERBATIM:** *"like if the script cannot do it, then
0.0.3_BG should have an ongoing schedule to check 15 min after the cron and if it didnt work
then it manually logs in and pulls or does whatever is necessary"*
**EFFECT — BG'S STANDING 07:15 BACKSTOP (supersedes MSTR~Z's N-hourly-fill proposal):**
1. BG arms an ONGOING daily schedule at **07:15 ET** (15 min after the 07:00 cron): check
   the scheduled run's outcome; if it FAILED, BG **manually logs in (runbook — STANDING-
   AUTHORIZED by this word for exactly this recovery context, no per-use ask), re-pulls
   ad-hoc end-to-end, verifies the SERVED object, and does whatever is necessary**, then
   reports per-leg attribution + what it did. Fire-once/lockout discipline stands inside
   the runbook (one fill attempt; a fill failure escalates loud, never retries blind).
2. The cron is session-only, so THIS RECORD + BG's own lane record are the durable
   carriers: every BG session re-arms the 07:15 check while this ruling stands.
3. Tonight's (b) is UNCHANGED: the 07:00 fallback fires untouched; the 07:15 backstop is
   the new standing net from tomorrow onward — the acceptance read stays honest either
   way, and a fallback failure no longer burns the day operationally.

**Broadcast (same turn):** BG (the duty holder + the arm order), laptop MSTR (their
D8-applies relay arms only on a CLEAN acceptance signal), CTO~Z (D-family gates carry the
branch logic; ruling-2's scope note updated — the intra-day fill schedule question is
superseded by this design).
