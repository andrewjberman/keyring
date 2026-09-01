# Session log — `0.7.0_AE_CloudOps~Z` — 2026-08-31 23:33Z → 2026-09-01 00:45Z

**Archetype:** BUILD (single-project, Rule 27) · **Project:** `PLATFORM_OPS_USERMGMT` and nothing else
**TO:** `D12_PLATFORM_OPS.W1-SITEZ.identity-record-and-email-otp` (read @`49c5c1fdc3`, amended twice
under me: @`9ab786b706`, @`1521e356d4`)

---

## Current State

**W1 is CLOSED 10 of 10.** `2.0.0_SA_COO~Z` validation verdict **PASS** (17257); acceptance sits with
`1.0.0_SA_CTO~Z`. Cells **1.1 / 1.2 / 2.1 / 2.6 BUILT, APPLIED, EXERCISED** on the deployed handler.
Cell **2.5 deliberately NOT BUILT** — §5 invited that answer and the reasoning is in
`declared_exclusions`: 1.1's per-user `mfaChannel`/`mfaEnabled` **is** per-account enablement, and 1.2
leaves every account OFF, so Andrew's staged-rollout ordering holds with nothing exposed to clients.

Proof instance `D12_PLATFORM_OPS.W1_PROOF_OF_SPEC.json` — `VALID (rc=0)`, violations 0, 10 acceptance
rows, 13 of 13 artifacts resolved at pin. Deploy ledger `20260901T0003Z` **CLOSED — COMPLETE**.

Commits (all **LOCAL**; `git ls-remote origin SITEZ` read `272b94c5bf` — push on SITEZ is the
integrator's, so LOCAL is the correct terminal state):
`30676928e4` source · `ffbd814605` untrack fix · `c34d765106` artifact map · `272b94c5bf` Andrew-direct
· `d3226b3d7d` proof + ledger · `b31fd28226` retraction.

Live effects: `opal-portal-auth-mfa` table; 4 Route53 records + SES custom MAIL FROM
(`MailFromDomainStatus = SUCCESS`); auth-handler running `T0Lf6MSrKtr4OKEuoEelpFaFMZwipkPFomVveCtqywc=`;
49 of 49 user profiles carrying a DEFINED `mfaChannel`; `andrew@opalinvest.com` at `email`/enabled.

## What I Got Wrong, and What Caught It

**I reported that `ses:SendEmail` from `support@opalinvest.dev` was IAM-denied and that the two
existing mailers would fail on first use. The conclusion was FALSE.** `1.0.0_SA_CTO~Z` falsified it
against the world — Andrew received a password reset from `support@`. I then measured the cause that
seat correctly refused to guess at: **I passed `--resource-arns "*"`.** The role carries two SES
grants; the literal `"*"` matches the conditioned statement's `Resource` and does **not** match
`identity/*`, so the simulator only ever evaluated the conditioned grant. Re-run against the real
identity ARN: `allowed`, matched by `ses-send-email`.

⭐ **The keeper, and `2.0.0_SA_COO~Z` banked it:** my positive control was *sound* — separate
invocation, exactly as the rule requires — and the conclusion was still wrong, because **both calls
carried the same wrong resource ARN**. A separate invocation buys independence only on the axis you
actually varied. I varied `FromAddress` and held the wrong ARN constant, so the pair could not
discriminate. That is Rule 22's ordering clause (DISCRIMINATION passing inside a wrong GRAIN) and I
walked into it *while quoting the rule in the same report*.

⭐ **Second half, which generalises further:** `APPLIED, NOT EXERCISED` was not a caveat decorating the
finding — it was the finding announcing that nothing had tested it. **An unexercised negative is
exactly what one real observation destroys.** When a claim carries that label, touch the referent
(send the mail, read the mailbox) rather than refining the model of it.

The two bounds I *did* state correctly are what made the correction land cleanly instead of
contradicting a claimed pass: labelling the finding `APPLIED, NOT EXERCISED`, and scoring W1-10
`UNVERIFIABLE-BY-INSTRUMENT` rather than PASS when I could prove delivery but not the folder. The
guess would have been right; it still would not have been knowledge.

**The real defect stands and is sharper than mine was:** an intended restriction that restricts
nothing. Repointing `support@` would have buried it. **No IAM policy widened or narrowed; no repoint
made.**

## My Own Defect, Caught Pre-Apply

`30676928e4` committed `src/lib/partner` — a build-time mirror whose canonical home is
`infra/aws/lambda/lib`. Two carriers of one file, no named primary. Untracked at `ffbd814605` with an
ignore rule added. `build-nodejs-lambda.sh:132` *claims* that mirror "is gitignored"; `git check-ignore`
returned rc=1 — no rule existed. Fixed for this Lambda only; other Lambdas may share the latent gap,
**surfaced not swept** (LD-0405).

## Blockers

**NONE at this seat.** One item is genuinely at Andrew and is not a block on my work: he authorised
`support@ → noreply@` on the premise the mailer was broken. `2.0.0_SA_COO~Z` clarified (17251) that the
hold is *pending his re-confirmation on corrected facts*, **not a refusal of his word and not an
agent-made gate**. I have put the corrected picture to him with the ask. **If his re-confirmation
reaches me first, I execute and report after.**

## Next Steps

1. **[Andrew]** Re-confirm or drop the `support@ → noreply@` repoint, now knowing `support@` works.
2. **[Andrew]** Whether MFA stays on for `andrew@opalinvest.com` or goes back to `none`.
3. **[`1.0.0_SA_CTO~Z`]** W1 acceptance on the proof instance.
4. **[unassigned]** The two-Allow IAM structure — a finding, not a task. Nothing is failing today.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | greenfield census, word-boundary `(mfa\|totp\|otp)` over auth-handler src + control `password` | 0 hits / control 69. Re-derived the TO's claim on my own instrument. Repeated against the **deployed bundle**: 0 / control 29. |
| `comp-find` | SMS send-path census + `SendEmailCommand` control | 1 hit and it is a **comment, not a call** → zero send paths; control 4. W1-7. |
| `comp-find` | remembered-device / 30-day sweep + `CHALLENGE_TTL_SEC` control | 2 hits, both my own comments; control 4. W1-9. |
| `comp-find --name` | `*PROOF_OF_SPEC*.json` | 275 instances; found the schema and authored against the **contract** rather than by imitating a sibling. |
| `commit-gate.sh` | on the migration `.py` | All checks passed (py_compile + ds-precommit + ruff py39). |
| `safe-commit.sh` | 6 commits, `-F`, every message file written by a **non-shell writer** | msg-verify MATCH on each. One `printf`-built draft discarded unused per Rule 14a. |
| `safe-apply.sh` | portal-auth apply | HALT-GATE fired on a 10-day-old message → **read in full** (withdrawal notice, not STOP-class) → `HALT_ACK=1`. 6 added, 2 changed, 0 destroyed. |
| `terraform validate / fmt / plan` | before + after | validate Success; my 3 files fmt-clean (the one diff is a pre-existing file I did not touch); post-apply **"No changes."** |
| `tsc --noEmit` | with shared libs synced as the build does | rc=0, zero errors. |
| `aws iam simulate-principal-policy` | SES FromAddress condition, isolated control | **Produced my one wrong conclusion** — see above. Re-run with the correct ARN corrected it. |
| `aws logs filter-log-events` | AccessDenied + forgot-password sweeps, each with a control | Both zeros real; an early empty result was `--limit` returning oldest-first, **caught by the control**. |
| `nslookup @8.8.8.8` | all 4 new records on a **public** resolver | SPF, DMARC, MX, MAIL FROM SPF all resolve with correct values — verified off our own API. |
| `proof-of-spec-check.py` | the instance | First draft **INVALID, 13 violations** (3 rows named paths git refutes). Corrected → `VALID (rc=0)`. |


---

# DELTA — 00:45Z → 01:15Z (appended, nothing above rewritten)

⛔ **THE "Blockers" AND "Next Steps" SECTIONS ABOVE WENT STALE WITHIN MINUTES AND THIS
APPENDS RATHER THAN REWRITES THEM.** Above, item 1 of Next Steps reads "Andrew re-confirm or
drop the repoint" and Blockers says it is pending him. **He ruled ~00:5xZ and it is DONE.** A
log is a snapshot, but a snapshot nobody marks as superseded is read as current by whoever
finds it next — so the delta is here, and the original text is left intact so the sequence of
what was known when is still legible.

## Andrew ruled both open calls (~00:5xZ, VERBATIM)

> "All of these functions should be noreply, there is nobody responding to these so noreply is
> the coreect point. on call 2, i want to test it with a few people first, including myself. I
> want to try logging in and seeing that MFA actually works."

⭐ **Call 1 shipped on HIS reason, not my retracted one.** His basis is SEMANTIC — nobody reads
replies to auth mail. He had originally been told the mailer was broken, by me, and that was
false; he re-affirmed on corrected facts with a better reason. That distinction is why the
`2.0.0_SA_COO~Z` hold (17251) was correctly a pending-re-confirmation and never a gate.

**Call 2 is a NAMED PILOT, not a rollout and not a wait.** His account is enabled and ready.
**The cohort is unnamed and I did not invent it** — no account beyond his is touched.
⚠ His login will be the **FIRST real exercise on a real account**: W1-3 was exercised on the
test account, so his result must be read as a first exercise, not a re-confirmation.

## What landed (ledger `20260901T0058Z`, CLOSED — COMPLETE)

1. **All auth mail → `noreply@`.** "All of these functions" treated as a census instruction:
   exactly **three** `Source:` sites exist in the whole auth stack, no fourth sender anywhere.
   Two constants collapsed into one (I had created the second myself hours earlier — two
   carriers of one value with no named primary).
2. **`getUserPKByEmail` fails closed on a duplicate email.** `1.0.0_SA_CTO~Z` ruling 1.
   Deny-capable, so the bad state was measured **first**: 48 emails, 48 distinct, 0 duplicates.

Verified in the **running bytes**, not by a live send — firing `/auth/forgot-password` is the
exact probe whose side effect mailed Andrew tonight, and re-running it to check my own work
would have repeated the fault while verifying the fix for it. `2.0.0_SA_COO~Z` W2 verdict:
**PASS** (17268), re-derived at source including the residual `Limit: 1` (a comment, not code).

⭐ **The catch worth carrying:** the warned-about carrier was the commit message. The worse one
was **my own retracted claim sitting in `email.ts` as a source comment** — *"a send from
FROM_EMAIL above is DENIED by IAM"* — in the file every future reader opens. A commit message is
read once by whoever is watching; a source comment is read by everyone who ever opens the file.

## Accepted without qualification: `1.0.0_SA_CTO~Z` ruling 2

**No test account may use a live human email address.** Mine used Andrew's own address via
plus-addressing and sent him two production-shaped emails whose only tell was the greeting.
He reasonably concluded a feature was broken; ~40 minutes of three seats went to a bug that did
not exist. I chose that address because it was the only mailbox I could read, and did not weigh
what it would look like arriving in a human inbox. Account deleted (48 profiles, verified).

## Blockers (superseding the section above)

**NONE.** The two remaining items are Andrew's own acts: try the login, and name the pilot cohort.


---

# DELTA 2 — 01:15Z → 03:40Z (W3 ACT A). Appended; nothing above rewritten.

⛔ **THIS IS THE SECOND TIME THIS LOG WENT STALE WITHIN AN HOUR OF BEING COMMITTED**, and the
pattern is worth more than the content: a session log is written at the moment a seat believes
it is finishing, and this seat has believed that three times tonight. **The fix is the append,
not a resolution to stop being wrong about when work ends.**

## What landed

**W3 ACT A — `POST /auth/mfa/send`** (`e96de00837`, deployed sha
`pyKEMVBmUsw8utCs3dw2tImzy63e0XG+pL5AJqqRIN0=`, 0-diff clean). Purely additive; `login()`
unchanged. Proof instance `d525b48dbe`, **VALID rc=0**: W3-2/3/4 PASS, **W3-1
UNCOMPUTABLE-BY-CONSTRUCTION** because it is ACT B in one sentence.

⭐ **THE DESIGN DECISION: it takes a `challengeId` and NO email address.** The TO required it not
become an open mail relay and not reveal account existence. An email-keyed endpoint would have
needed enumeration defences bolted on; **this one has nothing to defend** — the caller cannot name
a recipient, and no account identifier is an input. Removing the attack surface beat guarding it.

## Three errors of mine, all caught, all recorded

1. **A false security claim in my own docstring** (`1e5e7d4983`). `hashCode` said a table or
   backup reader "cannot replay a live challenge." **False** — the code is 6 digits, so a reader
   with `(salt, codeHash)` recovers it in ~1s, and **that is exactly how I exercised W3-3.** The
   run that proved the feature works refuted the comment above it. Retracted with the false
   sentence QUOTED inside the correction rather than substituted away. **Second false claim I left
   in this codebase tonight** (the first: an IAM deny that did not exist).
2. **A false zero, nearly shipped.** Whole-bundle census for `login#acct#` → 0, which looked like
   proof the new route bypasses no throttle. **Minification artifact** — built at runtime from a
   template. Control proved the throttle IS in the bundle. Replaced with a SCOPED census plus
   in-region controls. **Same class as the wrong-resource-ARN error six hours earlier: a zero from
   the wrong scope, wearing the authority of a measurement. Twice tonight, two instruments.**
3. **An over-stated blocker I corrected in my own favour.** I told COO the split "alters the API
   contract" — true of only ONE of two acts. Decomposing it shipped ACT A immediately and
   unblocked a waiting lane. **I had made myself more blocked than the work was.**

## The finding that outranks the build

Running ACT B's precondition (enumerate `/auth/login` consumers) surfaced a **non-human** one:
`svc-bbgtml@opalinvest.com`, the Opal Gateway's service credential, which fires **the daily
Bloomberg PKL refresh — Andrew's dashboard.** Enrolling it in MFA mails a code to a mailbox nobody
reads and the pipeline gets no session. **True today, with or without ACT B.**
⛔ **AND MY OWN W1 MIGRATION MADE IT MFA-ELIGIBLE** — the 1.2 backfill wrote `mfaChannel` to all 48
rows, including two service accounts. The migration's declared domain was "users" and was not MECE
either; that is the same uncovered-member error one layer below the one CVO caught.
`1.0.0_SA_CTO~Z` ruled the cohort must be an **allowlist of named humans** (an enumerated exclusion
lapses silently — the cross-firm-ban-list trap). `3.0.0_SA_CVO~Z` corrected the safety invariant to
three buckets; **its first use found a SECOND service account** (`cot-verify-internal@`) that had
been counted as human all night. Corrected census: **HUMAN 0/45 | SERVICE 0/2 | FIXTURE 1/2 = 49,
exhaustive** — with the bound that my bucketing is a NAME heuristic, not an attribute.

## Blockers

**NONE at this seat.** ACT B is deferred by ruling and its precondition is now reframed (blast
radius = enrolled accounts, not callers, so it strands nobody today). The gated fixture is **HELD**
for `0.4.0_DE_ClientPlatform~Z`'s DE3 — credential and code-recovery hop handed over; the delete
waits until both lanes report done.
