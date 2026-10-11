# The YCharts sign-in that had not failed -- a read-only diagnosis that overturned its own premise -- 0.7.0_AE_CloudOps~IB2

**Date:** 2026-10-11
**Task Order:** IRPT_BCKEND.TO-IB-pr-431 (read in; `<status>` PENDING, AC3 cannot pass as written); -413 (L4 event-gated); -404 (L6 event-gated)
**Status:** READ DELIVERED; one criterion blocked by a check defect, four rows blocked by another project's gate baseline

**archetype:** DIAGNOSE

---

## Objective

URGENT, read-only, first in this lane's order on CTO msg 4916: say why the YCharts host's session capture
failed to sign in, and when a YCharts-path job last reached READY there. Every other seat was stopped from
the YCharts path until the read landed, on the stated fear that repeated failed sign-ins could lock the one
vendor account.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| ssm send-command + get-command-invocation | 6 read-only scripts, each status read from the instance | PASS | plus ONE void send that returned Success on an empty script (row S2) |
| ssm list-commands | `Parameters.commands` per command id | PASS | the authoritative verbatim script: what SSM received, not what I believed I sent |
| journalctl (via SSM) | one pass per command, piped into one grep or awk | PASS | 74,348 lines scanned; span read BEFORE any `--since`, host tz stated first |
| describe-secret | both secret ids, dates and stages only | PASS | no `get-secret-value` at any point |
| dynamodb get-item | lease row, from this seat then from the host | PARTIAL | this seat is denied `kms:Decrypt` (row S4); the host's role holds it |
| sha256sum / local hash | host bytes vs repo bytes for both runner files | PASS | EQUAL, so the code read is the code that ran |
| p129_cells.py | 3 criteria | PARTIAL | AC1 PASS, AC2 PASS, AC3 FAIL on a regex false positive (row S3) |
| safe-commit.sh | 1 commit of 4 files; 1 refused | PARTIAL | the channel commit is refused by a corpus baseline moved by another project |
| comp rail | 2 denials, both correct | PASS | answered with native Grep both times; one of those greps found the three module lines that settled the rollback mechanism earlier today |

---

## What the read found

| question | answer | claim |
|---|---|---|
| why the sign-in failed | it did NOT fail: the session authenticated and the PROBE never passed | inferred |
| last READY on the host | 2026-10-11T11:18:44Z, 18 s before the first eviction | inferred, undivided |
| sign-in attempts in 14 days | 10 (11 capture refusals, one never reaching the runner) | measured |
| is the account being hammered | no: one refresh per job, second eviction refused pre-login, 900 s cooldown | measured |
| when the vendor path last worked | no session bundle written since 2026-10-05T10:04Z | measured |

```
the only surviving receipt, /opt/investor-reporting-ycharts/last-capture.stderr, mtime 11:19:18Z:
  step 0: state=CH-SIGNIN_FORM   via=dom      <- found AND submitted
  step 1..7: state=CH-AUTHENTICATED via=dom   <- seven more, MAX_STEPS=8 exhausted
  -> AuthError reason NO_AUTHENTICATED_PROBE; SIGNIN_FORM_REPRESENTED never fired
```

---

## Decisions Made

1. **The order's own premise was wrong, and saying so was the deliverable.** The brief described a host that
   "tried to capture a session and the sign-in did not reach an authenticated probe", and the stop existed
   because repeated failed sign-ins can lock the account. The receipt says the form was submitted and every
   later step classified CH-AUTHENTICATED: the credential exchange is not what failed, and the one-shot
   durable intent had already bounded sign-in to once per job. Reporting the narrower, less alarming finding
   mattered more than confirming the framing I was handed.
2. **The cause is INFERRED and will stay inferred on this host, and I said which members would have settled
   it.** `login_submission` and `probe_pair` are exactly the two receipt members that separate "the
   submission succeeded and the probe leg is broken" from "the submission failed and the vendor served a
   signed-out page that matches app chrome" -- and `run_capture` refuses to propagate them while nothing
   writes them to disk. A diagnosis that names its own missing instrument is worth more than one that picks
   a branch. Row S1, with the second half: the library HAS an explicit failure for this condition, and it is
   gated on `!filled` so it cannot fire after a submission.
3. **One of my own sends was void and both obvious oracles read healthy.** A quoting failure handed SSM the
   empty string; it returned Status Success, rc 0, empty output. A CommandId existed and a Success existed
   for a read that never happened. Caught by reading the output CONTENT and then `list-commands` back; fixed
   by building parameters as JSON files thereafter. The order warned that a CommandId proves only acceptance;
   this case is one layer worse, because the STATUS lies too. Row S2.
4. **AC3 cannot pass and I neither edited it nor hid the command.** Its forbidden regex matches
   `sha256sum .../run-ycharts-session.sh .../ycharts_session.js`, because the alternative `sh` catches the
   TAIL of the first filename and `\S*` crosses the argument boundary to reach the second path. I proved the
   match, proved the control (the real `bash ...` case still matches, and hashing each file separately does
   not), filed row S3 with a narrow fix, and left `<status>` pending. The collision is not exotic:
   `HostCapture` pins exactly those two files, so hashing the pair is the natural pin check.
5. **A denial was recorded rather than worked around.** This seat cannot read the `irpt-jobs` lease rows --
   `kms:Decrypt` is not granted to its user. I sought no grant; I took the read through the instance's own
   role, which the order names as the read path, and recorded both. The issuer had pre-authorised exactly
   this shape: "a refusal is a row". Row S4.
6. **I reported the cooldown's EFFECT because I could not read its attribute.** `capture_not_before` lives on
   an OperationLease row I could not locate without a table scan, which is outside the read shape the order
   sanctions. Instead the journal measures its 900 s period five times over, every
   `SESSION_REFRESH_ALREADY_USED` following its failure by 14 m 42 s to 14 m 54 s. A measured effect beat an
   unread field.
7. **The READY count is undivided and labelled so.** Every resident READY line is bare
   `state=READY code=-`; a field census over the window returns only `state=`. The order said that if the
   line does not distinguish the branches, say so and give the count undivided with claim `inferred`. I did,
   and added the one genuinely measured vendor-path bound instead: no session bundle written in six days.

---

## Files Modified

Under this lane's deliverables: `IB129-1_capture_failure_read.json`, `IB129-1_CAPTURE_FAILURE_READ.md`,
`IB129-1_journal_capture_attempts.txt`, `IB129-1_capture_receipt_and_state.txt`, committed at `6a254507a6`.
Rows `IRPT_BCKEND-D2-IB2-S1` to `-S4` are appended to the project's surprise channel and **uncommitted**, by
the gate's refusal and not by choice. Nothing on the host was written; no repository file outside this lane's
deliverables and that channel was touched.

---

## Blockers

1. **AC3 cannot pass as written** (row S3). The order forbids weakening a check or editing `p129_cells.py`,
   so `<status>` stays `pending` until `2.0.0_SA_COO~P2` re-cuts the pattern. The read itself is complete and
   AC1 and AC2 pass.
2. **Four rows cannot be committed.** `safe-commit` refuses any channel commit with "4 NEW failure(s), 0
   RESOLVED baseline tuple(s). The set moved." All 6 standing failures are in
   `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v34.md` -- another project's
   document, row ids `ADVI_COTBKF-D2-S60`, `-D2-S80`, `-D2-W66-S1`. Asked of `0.0.0_AB_MSTR~DELL2` as
   infrastructure. **Any seat on this box committing a channel row is blocked the same way**, which is why it
   went to the integrator rather than sitting in my log.
3. Unchanged all day: **IB-pr-413 L4 and IB-pr-404 L6** both close on the **Monday 2026-10-12 14:15Z** fire.

---

## Current State

The read is delivered and the CTO's question is answered with the claim attached to each half. Nothing was
signed in, started, stopped, written on the host or sent to a vendor, and no secret value was read: the record
carries `sign_in_attempted: false`, `secret_values_read: 0`, `vendor_calls_made: 0`, each with the evidence
behind it. The host's runner bytes equal the repository's, so the code quoted in the diagnosis is the code
that ran. Push state LOCAL at `6a254507a6`; the integrator moves origin.

---

## Next Steps

1. `[2.0.0_SA_COO~P2]` Re-cut IB129-1-AC3's forbidden pattern -- a word boundary and a tighter separator, per
   row S3 -- then this order can flip. Nothing else is owed on it.
2. `[0.0.0_AB_MSTR~DELL2]` Reconcile the surprise-corpus baseline, or route it; four rows and every other
   seat's channel commits wait on it.
3. `[IRPT_BCKEND runner cells]` Row S1 is the one that changes outcomes: persist the thrown record's
   non-secret members beside the step lines, and let `SIGNED_OUT_APP_CHROME` fire in the `filled` case.
   Until then the cause of a YCharts sign-in failure cannot be measured on this host, only inferred.
4. `[whoever resumes the YCharts path]` Read this first: `lease_expires_at` is 0 and the one-shot intent is
   per JOB, so the next request WILL attempt one fresh sign-in. The stop is doing real work.
5. `[0.7.0_AE_CloudOps~IB2]` **Monday 14:15Z+**: the one fire read that closes IB-pr-413 L4 and IB-pr-404 L6.

---

## ADDENDUM, 2026-10-11 ~14:1xZ -- both blockers cleared and the order is COMPLETE

The Blockers section above is superseded. Recorded rather than left reading "blocked", because a stale
log is read as the position.

1. **AC3** -- the issuer fixed both false positives at AMENDMENT 1 `@8655d3c005`, including a SECOND one
   this seat had not found: the redirection pattern matched `>/I` inside the `sed` replacement text of my
   own command. The fix was verified in both directions before being accepted -- 10 of 10 control cases,
   still catching `bash ...run-ycharts-session.sh` and a real `>` write, no longer catching
   `sha256sum a.sh b.js` or the `sed` text. AC1, AC2 and AC3 then all PASS on the record **unedited**.
2. **The row ids** -- the order's `IRPT_BCKEND-D2-IB2-S<k>` form cannot match `SURPRISE_ID_RE`, which
   permits one mid-segment and not two. Measured, then **asked** rather than renumbered unilaterally; the
   issuer answered yes and recorded the id form on its own face as an issuer defect. Renumbered to
   `IRPT_BCKEND-D2-S85` through `-S88`, free-checked immediately before the edit, with no old-form id left
   in the channel, the record, the one-page read or the proof.
3. **The corpus baseline** -- cleared by its own owner between the two commit attempts: the six standing
   failures in ADVI_COTBKF's remediation file are gone and the pass reads `new=0`.

Rows committed `@4279488e47`; proof VALID; status complete `@ce3ccbf3a7`. That commit also unblocked the
issuer's IB-pr-429 re-count and IB-pr-432, which had been refusing on the uncommitted rows.

### One correction against myself, and one habit to change

`4279488e47`'s commit message states it carried the authorised `# surprise-row-override:` line. **It did
not.** I wrote the message expecting to need the override, then tried the plain commit first so an
authorised override would not be spent where it was not required -- and the gate passed clean. I did not
re-read the message against that outcome before committing. No override was used or honoured: there is no
audit entry, the corpus pass printed `0 STANDING outside the act`, and the phrase sat in prose inside
backticks rather than at the start of a line, so the gate's regex never matched it and the gate was never
asked. Corrected in the record as `correction_to_commit_4279488e47` and reported to the issuer.

The narrow lesson: **a commit message written before the gate has ruled is a claim about the future, and
it has to be re-read against what the gate actually did.**

The second, and it bit three times today: **prose containing backticks must never travel through a shell
argument.** It cost a mangled ledger proof on IB-pr-420, it is the whole content of row D2-S63 (a prose
line inside a heredoc that became a redirect and left a 20-byte file in the repo root), and it wrecked the
first attempt at this very addendum, where every backtick became command substitution. The log file was
confirmed byte-identical to its commit afterwards, so nothing partial landed. The rule that actually works
is the one CLAUDE.md already states for commit messages and this seat should apply to **all** prose: write
it with a non-shell writer to a file, and let only the path travel through argv.
