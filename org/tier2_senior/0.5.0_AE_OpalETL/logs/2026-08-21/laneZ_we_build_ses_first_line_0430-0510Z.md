# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-21 0430Z – 0510Z

**archetype:** IMPLEMENT
**Projects:** D7 TICKET LIFECYCLE v2 — W-E: the email DL as the first instantaneous line

## Summary

Stage 3 of the CTO~Z sequence, on their GO @4189 after stage 2 was accepted. **Built, not applied.**
The SES first-line rides the CREATE write path; the sender is pinned to `opalinvest.dev`; the
recipient refuses if unset. `D7_TICKETING.WE_PROOF_OF_SPEC.json` VALID rc=0 — **4 PASS
(WE-4/5/6/7) / 3 UNCOMPUTABLE-BY-CONSTRUCTION (WE-1/2/3)**, every row states its plane.

Three files: the handler (+162/-0), a 19-test battery, and the Terraform. `git status` shows exactly
those three.

## 1 — What was built, and what the shape was ported from

Rung 2, not reinvented: `trade-pipeline`'s `email_utils.py:113-118` → `ses.send_raw_email(Source=…)`,
`config.py:13`. **Two narrowing divergences, both deliberate:**

**(a) No bounce/complaint SNS topics cloned.** Andrew authorised a *notification feature*; the
2026-07-28 moratorium is untouched for everything else, and feedback topics are exactly the banned
machinery.

**(b) The recipient config is inverted** — `EMAIL_FROM` in the ported shape carries a baked default;
WE-5 demands refuse-if-unset for the DL.

**And a third divergence that is mine and is flagged, not taken silently: the sender is a pinned
constant with no env override.** That is *stricter* than CTO~Z's "copy the sender pattern". The TO's
own Do-not says **"No fallback sender, ever"**, and an env-with-default *is* a fallback path. Pinning
makes a wrong sender **inexpressible** rather than merely linted. One line to overrule.

## 2 — The audience question, and the field that waits

The gate's test is **"if a task's output would be byte-identical under either audience answer, it is
not blocked."** Applied field by field, not inherited as a list:

**Carried:** `ticket_id`, `ticket_type`, `created_at`, deep link — WE-4's own named content.
**Withheld as WE-4-prohibited:** events, description, source, created_by, status, claimed_by,
assignee — the audit trail and routing state, which never travel to *anyone*.
**Withheld as AUDIENCE-DEFERRED:** `title`, `requester.{email,name,firm}`.

Those two withholdings have **different reasons and must not be collapsed**, so they are two named
tuples in the code rather than one. `title` fails the test because under a client-facing DL its safety
turns on a *further* undetermined sub-question — single-recipient ack vs multi-firm list — and on the
second reading one firm's title reaching another is a cross-tenant leak. **A field whose safety
depends on an unanswered question is not invariant, so the field waits — not the leg.** The email is
thinner today than it will finally be, and that is the honest form of building under an open
sovereign question.

The deep-link **base** got the same treatment, beyond WE-5's letter: an internal DL plausibly links to
the internal board and a client-facing one to the client's own view, so **a baked route would
pre-encode the audience answer in a default string.**

## 3 — WE-5 and WE-6 pull in opposite directions, and both are satisfied

"Refuse **loudly**" against "the email leg erroring must still yield a 201". Resolved by putting the
refusal and the isolation in **different functions**: `notify_dl` raises a *named* `DLAddressUnset`;
`notify_dl_isolated` swallows and logs. The named error is what lets the wrapper tell **unconfigured**
(a config act) from **SES refused** (an operational act) — two states taking opposite actions that a
bare `ValueError` would merge into one log line. They emit distinct greppable tokens for the same
reason, and each is asserted **present in its own case and absent in the other's**.

**The mutant is the proof the isolation is load-bearing:** repoint the write path at the *unisolated*
sender — literally "share the exception boundary" — and the handler raises instead of returning 201;
restore the boundary in a `finally` and the identical call is a 201 again. Without it, the five
isolation tests would pass for a handler whose email leg never ran.

**Incidental corroboration I did not ask for:** the *pre-existing* authz battery, written before this
feature existed, emitted **12** `WE_DL_UNCONFIGURED` lines while staying 15/15 green — every 201 path
in it exercised the isolation.

## 4 — The IAM chain, with all three false-deny modes closed

`comp-iam` was run as mandated and was **insufficient by its own declaration** — `IAM role: (not
mapped)`, all 13 operations `[UNKNOWN]`, plus its own DESIRED-plane banner, 24 unattached policy
blocks and 2 unparsed denies. That is the documented insufficiency, not a surprise; it is a floor.

Live: `ses:SendRawEmail` on the `opalinvest.dev` identity → **implicitDeny**. Before calling that a
real missing grant, all three of the instrument's lying modes were closed — one `--resource-arns` per
call; **no Condition block on either statement of this role**, so no `--context-entries` needed; and
the action name validated by its own oracle (`validate-policy` → 0 findings) with a **negative control
in a separate invocation** (`ses:ZzzNoSuchActionName9999` → `INVALID_ACTION`). Positive control, also
separate: `dynamodb:GetItem` on `opal-tickets` → **allowed**.

The grant landed as its **own** policy resource — an SES grant is not a table grant — reading the
identity through a data source so a rename **fails the plan loudly** instead of granting on a string
that resolves to nothing. `ses:SendEmail` deliberately **not** granted.

## 5 — I reintroduced my own logged defect, within one file of where I fixed it

The edit put **4 U+26D4 glyphs into code that runs on AWS** — the same glyph, the same file, the same
defect I fixed at `b121c2f26e` ("*I put a U+26D4 glyph into code that runs on AWS*"). Caught by an
explicit byte-level scan and stripped to 0 non-ASCII / 0 CRLF before the gate ever ran.

**Knowing a failure by name, having authored its fix, and being the same seat, did not prevent
re-committing it four hours later.** The scan is the control; the memory of the incident is not.

⛔ **CORRECTED 0442Z — this section first said the defect was caught "not by the commit-gate, which
passed the file clean both before and after." That is literally true and MECHANISTICALLY MISLEADING,
and I had already routed it upward before checking.** `.tools/commit_gate_runner.py:376`
`_nonascii_lint_one` (called at `:691`/`:705`) **DOES detect it**, scoped to `infra/**` + `.tools/**`
— which this file is in. Measured by calling the function directly on three fixtures: a glyph-bearing
in-scope file emits `infra/probe.py:2 non-ASCII: U+26D4` **and returns 0**; an ASCII-clean in-scope
file is silent (negative control — it discriminates); an out-of-scope glyph file is silent.

>> **SO THE GATE FINDS IT, NAMES THE CODEPOINT AND THE LINE, AND PRINTS `All checks passed!` AND
`pre-commit gate clean for 2 file(s)` IN THE SAME BREATH.** WARN-only by explicit design
(*"announce-then-enforce… must not block a commit while it beds in"*). **That is worse than blindness:
a blind gate is a gap you close by building a check; this one spells the defect out underneath the
word "clean", which is the one word that stops an agent reading further.** The remedy is arming the
enforcement or suppressing the clean summary when a WARN fired — routed to `1.0.0_SA_CTO~Z`, not built.

⛔ **AND HOW I GOT IT WRONG IS THE SAME CLASS AS THE RELAPSE.** My first probe planted a glyph in a
**scratchpad** file, ran the real gate, got rc=0 + "All checks passed!", and I read that as *the gate
is blind*. **It was OUT OF SCOPE** — the lint returns 0 *silently* for any path outside `infra/`/
`.tools/`. A clean, well-formed, confident answer to a question I had not asked. Second time in one
session I took a scoped instrument's silence for a verdict. I also grepped `commit-gate.sh` for an
ascii check, found none, and was one step from banking *"the gate has no non-ASCII check"* — **the
`.sh` delegates to the runner; the `.sh` was the wrong file.** Checking before writing it down is what
stopped it, not care.

## 6 — Two controls that changed what I was allowed to claim

`terraform validate` returned rc=0 on `data.aws_sesv2_email_identity.opalinvest_dev.arn`. **That rc
proves nothing until validate is shown able to fail** — so a scratch config with a bogus attribute
was run: **rc=1, "Unsupported attribute"**. The attribute is real, measured rather than assumed.

And `.tools/terraform.exe` — the binary CLAUDE.md names — **does not exist on this box**. v1.15.8
resolved on PATH from a winget install. A seat taking the documented path literally gets rc=127 and
could conclude Terraform is unavailable here.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-iam service opal-ticket-api` | rc=0; role **(not mapped)**, 13 ops `[UNKNOWN]`, 0 ses; self-declared DESIRED-only + 24 unattached blocks + 2 unparsed denies | FLOOR, AND IT SAID SO |
| `simulate-principal-policy` target | `ses:SendRawEmail` on the identity → **implicitDeny**, ONE `--resource-arns` | REAL missing grant |
| `simulate-principal-policy` positive control, **separate invocation** | `dynamodb:GetItem` on `opal-tickets` → **allowed** | INSTRUMENT DISCRIMINATES |
| `accessanalyzer validate-policy` + its negative control | real action → 0 findings; bogus → `INVALID_ACTION` | TYPO MODE CLOSED |
| `terraform fmt / init -backend=false / validate` + scratch mutant | rc=0/0/0; mutant rc=1 "Unsupported attribute" | CONTROLLED PASS; no plan, no apply |
| `commit-gate.sh` ×1 | rc=0 clean (run **after** the strip, so it never saw the glyphs) | PASS |
| `_nonascii_lint_one` called directly, 3 fixtures + negative control | glyph in-scope → **names `U+26D4` and the line, returns 0**; clean in-scope → silent; glyph out-of-scope → silent | ⛔ **NOT BLIND — WARN-ONLY UNDER A "clean" VERDICT.** Corrects my own first read, which tested an OUT-OF-SCOPE path and called it blindness |
| `python -m py_compile` + AST call-site check | rc=0; call sites confirmed in `submit_form` + `create_ticket` by AST, not grep | PASS |
| test batteries ×3 | W-E 19 OK · authz 15 OK · intake 42+25 OK, all rc=0 unpiped | NO REGRESSION |
| `proof-of-spec-check` positional | VALID rc=0, rows=7, violations=0 | PASS |
| `comp-estate --layers` | superseded before it returned — the pattern was already cited at `file:line` with a denominator | RECORDED, NOT DROPPED |

## Blockers

**None I hold.** W-E's remaining three criteria (WE-1's second limb, WE-2, WE-3) all need the same
two things and neither is mine: **the DL to exist** (a tenant-admin act — no gateway tool creates a
distribution list) and **Andrew's audience answer**. Then a laptop apply. The apply also carries
**W-A's unapplied queue**, so it is not a clean single-change apply and nothing in the instance implies
it is. Surprise channel: `trade-pipeline/config.py:14` bakes `opalcapital.com` — a domain NEVER#23
says we do not own — reported with its plane named (repo read; the deployed side is UNMEASURED) and
not chased. Zero crons, zero gateway calls, nothing applied.
