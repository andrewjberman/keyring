# VERIFICATION LAW — the fourteen

**Relocated from `MEMORY.md` 2026-07-31 (Andrew-direct cleanup).** These laws lived in the
always-loaded agent memory index, where a 17,408-byte cap had compressed them into telegraphic
shorthand. They are doctrine — durable principles that bind every agent — so by this directory's own
routing rule they belong here, and they are restored to readable form.

**Relationship to the neighbours.** [`MECHANISM_LAWS.md`](MECHANISM_LAWS.md) is a *taxonomy*: the
fourteen shapes an assertion goes wrong in, with measured frequencies. This file is a *checklist*: the
things to do before you believe a result. They overlap by design — a law here often names a
shape there — but a taxonomy tells you what happened and a checklist tells you what to run.
[`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md) carries the full verification doctrine these compress.

> Citations of the form `memory/<slug>` root at the **agent memory DIRECTORY**
> (`C:\Users\AndrewBerman\.claude\projects\C--Users-AndrewBerman-Desktop-ajb-workspace\memory\`),
> not at the repo.

---

## 1 — DEPLOYED means downloaded AND imported

A green test suite describes a **file**. A deploy is about a **runtime**. The two are different claims
and the first does not establish the second. Verify the artifact was fetched *and* loaded by the thing
that runs it.

## 2 — An injected column is a HYPOTHESIS

Adding a column to prove a theory produces a value shaped like evidence. It is a hypothesis until
something independent of the injection confirms it.

## 3 — A false premise gets answered ON and returns as corroboration

Ask a question containing a wrong assumption and you will get a confident answer built on it — which
then reads as confirmation of the assumption. **Ask for the ARTIFACT, not the number.**

## 4 — A guard nothing invokes is not a guard

Existence is not enforcement. Find the call site or treat the guard as absent.

## 5 — An instrument that cannot fail is not an instrument

If there is no input that would make it report a problem, it reports nothing about the world.
Compounding this: **there is no channel for "I don't know," so not-knowing renders as confidence.**

## 6 — Enumerate what a number is *OF* before explaining why it differs

A rigorous instrument pointed at the wrong axis **survives review**, because the rigor is real and
the axis is unexamined. *Live instance 2026-07-14: W1's 40.7% versus 16.5% — a file-count axis and a
gold-script axis, both computed correctly, describing different populations.*

## 7 — "Well grounded" is not "FRESHLY grounded"

Grounding has a timestamp. A claim that was verified is not a claim that is verified.

## 8 — A stale record says something false WITH AUTHORITY

**A retracted prohibition is only as dead as its last surviving copy.** Retraction must propagate to
every enforcing copy, not just the one you were looking at.
*See `memory/feedback-retraction-propagates-to-every-enforcing-copy`.*

## 9 — Care is not a control

Care is what you have *instead* of one. Knowing a failure mode by name does not immunise you against
writing it — several instruments have been broken by the same agent who landed the rule against them
that same hour.

## 10 — State the coverage DENOMINATOR, and run the positive control SEPARATELY

A hand-chosen control measures **the author**; a generated one measures **the instrument**. A sweep
that cannot find a known-present instance is a broken instrument reporting silence. Run the control in
isolation from the target — a control batched with the target can be corrupted by the target's presence.

## 11 — Host is UTC-4: no `Z` is ambiguous, and a HAND-TYPED `Z` is worse

Ambiguity **prompts** the check; forgery **cancels** it.
- `aws s3 ls` mis-renders timestamps.
- `git log --since "18:00"` reads **local** — it returned **0 for an evening of 55 commits**.
- ⛔ `--date=format:'%H:%M:%SZ'` **discards the date and renders local time**, with the `Z` typed by
  you. That produced a 19-day misread and is **RETRACTED**.

Use **computed**-offset forms (`--date=iso-strict`). Never a typed unit or zone. **A zero from a
time-windowed query needs a positive control.**
*See `memory/feedback_aws_s3_ls_lastmodified_is_local_time_never_a_liveness_oracle`.*

## 12 — Control the RETRIEVAL, not the pattern

`grep` silently enters **binary mode** on a log containing invalid UTF-8 and **truncates its own
output while exiting 0** — this cost review RV-0055 a wrong BLOCK count (reported 9, truth 15). Use
`grep -a`, or do not use grep.

**A wrong number is more dangerous than a zero** — a zero invites suspicion, a plausible count does not.

Also: **print the PREDICATE, not just the denominator.** Two honest predicates sharing one word moved
a measured population by 2x.

> **A silently-lying instrument's lesson must be LOADED-ALWAYS or GATED: auto-recall is query-driven,
> and a silently-wrong instrument generates no query.**

*See `memory/feedback_profile_before_reporting_a_mechanism`.*

## 13 — Harness exit codes were corrupted (FIXED, but not durably)

**Fixed 2026-07-28 by MSTR:** `mount -f C: /c` (additive; `/cygdrive/c` untouched).

⚠ **NOT REBOOT-DURABLE** — MSYS shared memory, no fstab entry. A durable fix requires an elevated
fstab write, which is an **operator** action.

**Self-test:** a trailing `claude-*-cwd` line means the mount is gone — resume capturing TRUE_RC in
stdout (`; echo TRUE_RC=$?`, or `${PIPESTATUS[0]}` when piping). Absent, `$?` is truthful.

**Score controls on OUTPUT, never on rc.**
*See `memory/reference-cygwin-harness-exit-codes-corrupted-capture-true-rc-in-stdout`.*

## 14 — Metadata about a record is not the record. Eventually-consistent surfaces read stale exactly when you are debugging a live fire

**Found 2026-08-01 by `0.7.0_AE_CloudOps` — three instances inside one 25-minute month-end fire**, each
a lagging or adjacent AWS surface returning a right-looking wrong answer about an action that had
already succeeded:

| surface | what it said | truth |
|---|---|---|
| SES `SendQuota.SentLast24Hours` | unchanged `1.0 -> 1.0` — reads as "no send" | the send happened; it is a rolling, eventually-consistent counter |
| a log grep for `ses\|email\|sent` | empty — reads as "it never sent" | the function emits no line for its most consequential step |
| CloudWatch `describe-log-streams` -> `lastEventTimestamp` | `14:00:15.385Z`, the **START** event | the **END** at `14:01:08.135Z` already existed; the field had not caught up (53 s stale) |

**Any one of these, believed, produces a RED ALERT on a pipeline that has already delivered** — a
false outage on a partner-rebate basis. The third one is the sharpest: it manufactured an
"unreconcilable" timeline (a function that ended at 14:00:15Z cannot have sent at 14:01:00Z) and with
it a phantom unmodelled producer.

**The fix was identical every time: go to the authoritative per-timestamp record.**

> **A LAMBDA'S TRUE WINDOW IS ITS `START`/`END` EVENTS, NEVER THE STREAM'S `lastEventTimestamp`.**

The general form, and the reason this is a law and not an AWS trivium:

> **STREAM METADATA IS NOT STREAM CONTENT. A summary field ABOUT a set of records is a different
> object from the records, with its own — usually weaker — consistency guarantee. Query the events.**

**Corollary, and the finder's own words on their own miss:** *"a probe aimed at one question will not
volunteer the answer to a question you did not ask, even when the data is on the screen."* The same
pre-fire listing that proved July's artifacts were ABSENT also showed that May and June carried **no
partner CSVs at all** — a materially useful fact, printed in the operator's own terminal, unread
because the probe was aimed at absence. **Enumerate what your output contains, not only what you went
looking for.**

---

## The through-line

Nine of the thirteen are the same shape: **an instrument produced a clean result and the cleanliness
was manufactured by the failure** — the orphan watcher that reads REACHABLE *because* it ate the mail,
the PATH probe that reads 100% healthy *because* the breakage was total and single-caused, the grep
that exits 0 *because* it stopped reading.

**The cleaner the pass, the harder you should look at what produced it.**
