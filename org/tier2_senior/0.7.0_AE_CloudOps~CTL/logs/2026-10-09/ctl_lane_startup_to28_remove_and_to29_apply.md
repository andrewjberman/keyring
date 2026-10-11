# 0.7.0_AE_CloudOps~CTL -- lane startup, TO-APPLY-28 LEG REMOVE, TO-APPLY-29 apply

**Date:** 2026-10-09 | **Seat:** 0.7.0_AE_CloudOps~CTL | **Device:** laptop | **Branch:** box/laptop

## Startup

**archetype:** COORDINATE

Lane registered (PID 10108); `get_agent_status` read NOT REGISTERED for `~CTL` before that. `/watcher`:
census 0 script rows -> armed one Monitor, pid 27840 (task `byhp0186d`), re-armed twice on
`[WATCHER-EXPIRED]` in the same turn each time (`bin0x9lps`, then `brdeoqtjm`). Inbox: 4 messages read and
acked across the session (107946, 107956 to this lane; 107927/107939/107942 read on the base seat's inbox,
which is read-only for this lane and not drained).

`org/XXX.md` steps A.1-E run: session serial file written, audit-archive invoker (1 INTEGRITY finding on
`org/mcp/agent-spawn-audit.log`, an OWNED class the invoker says an exec startup will archive -- not
re-filed), owned-paths hook already wired, `.comp-graph/.agent_context` set, PATH 102 of 102 comp-tools
resolve bare and a forwarder exercised live. `/cloud-ops` loaded before any AWS call.

**Held:** exactly 2 task orders, by `<issued_to>` read from the files themselves --
`NFRA_CTLPLN.TO-APPLY-28` and `-29`, both re-addressed from the base seat, deaf since 09:29Z.
`sequence-check --project NFRA_CTLPLN`: not PARKED, first in the next-COO-slot order.

## NFRA_CTLPLN.TO-APPLY-29 -- ses plan read + svc-custody-statement ARN

**archetype:** DEPLOY

Applied `2026-10-09T12:21:00Z`. Plan 0/2/0 on exactly the two addresses, 18 diff-marked lines and 0
removals; default versions v2 -> v3 and v3 -> v4; ONE `safe-apply`; 8 of 8 simulation arms; AC1 re-plan
`exit=0`. Full evidence:
`org/tier2_senior/0.7.0_AE_CloudOps~CTL/deliverables/NFRA_CTLPLN_TO-APPLY-29_REPORT.md`. Commit
`a9bbbd20ea`, on origin.

Worth the next seat's attention: `safe-apply`'s seat-gates limb printed `CROSSBOX-DEPLOY verdict=STOP` in
WARN mode on an OPEN crossbox call plus an open-deploy hit. Read, both resolved benign -- the crossbox call
is an ORDER to `~CT1` to commit surprise rows, and the open-deploy was this seat's own entry opened two
minutes earlier. The decisive concurrency control was that the plan reproduced the issuer's ~11:0xZ
measurement exactly.

## NFRA_CTLPLN.TO-APPLY-28 -- LEG REMOVE

**archetype:** DEPLOY

dell2 called X1 at 12:03Z; BEFORE put `12:46:15-12:46:19Z`, 23 minutes inside the 13:09:10Z hard deadline.
Start SET-EQUAL to ADD, read-back SET-EQUAL to BEFORE, each graded with a negative control in the opposite
direction; dell2 explicitDeny, dell1 explicitDeny, walker allowed; zero `GetSecretValue` calls. Ledger and
sentinel CLOSED 12:53:00Z. Full evidence: `.../NFRA_CTLPLN_TO-APPLY-28_REMOVE_REPORT.md`. Commit
`b3d0b610d4`, LOCAL (origin/box/laptop `@4586920aca`, `ls-remote` read).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-to` | `comp-to NFRA_CTLPLN.TO-APPLY-29...` then `...-28...` | session TO_ID set race-free per seat+session, once per order |
| `comp-iam` | `comp-iam gaps` | AE minimum after the `iam.tf` change in @`97fb0b2abf`. 886 calls verdicted across 105 mapped roles; 38 missing / 302 deny-present / 1 coverage-unknown / 3 resource-mismatch across 34 services. **Zero** rows name either graded policy. The 3 resource-mismatch rows (`etfs-reports-reporter`, `opal-gateway` x2) are a standing census owned elsewhere -- surfaced here, not re-filed |
| `comp-find` | the rail's `RUN NEXT` after one denied directory-scoped grep | **worked as designed, and the denial was right**: the question did not need a repo sweep. Resolved with a named-dir `ls` plus `terraform state show`, which gave the ARNs the grep was only going to approximate |
| `proof-of-spec-check` | twice, once per order | VALID rc=0 both. **Gap worth recording:** the flag form `--expected-criterion-ids AC1` is a *usage error* (rc=2) that prints the full doctrine block -- the ids are POSITIONAL (`<instance.json> AC1`). rc=2 is a read error, not a refuted proof; a caller reading only "non-zero" would mis-report it |
| `deploy_ledger.py` | `open` / `close-leg` / `close` / `check` | both entries CLOSED with proof, sentinels removed. `check` scanned 22 of 22 sentinels; neither of this seat's slugs remains |

**comp-iam's blind spot, named:** it models identity policy, so it is BLIND to the TO-28 secret *resource*
policy by construction. The instrument that can see that grant is
`iam simulate-principal-policy --resource-policy <live document>`, and that is the one cited.

## Blockers

None. Both held orders are terminal and reported to `2.0.0_SA_COO~C`; the two times are relayed to dell2
via `0.0.0_AB_MSTR`. Status flips are the issuer's.

One item surfaced, not this lane's to take: the Y75 proof-instance ask (msg 107927) is addressed to the
deaf BASE seat and its target path sits outside this lane's `<paths>`. Routed back to the issuer as the one
ask on the TO-29 report rather than written out of lane.

## Next

Event-driven hold. Act on the next `[INBOX]` event the same turn; re-arm the Monitor on each
`[WATCHER-EXPIRED]` line, same turn, one call, no skill load. Zero crons armed.

---

## NFRA_CTLPLN.TO-APPLY-30 -- the served-read window, both pairs

**archetype:** DEPLOY

Four legs on one secret's resource policy, two NEVER-2 entries, both CLOSED.

| pair | ADD put | REMOVE put | open | closed by |
|---|---|---|---|---|
| 1 (original) | 13:37:36Z | 13:45:41Z | 8 min 5 s | G2's REMOVE NOW |
| 2 (AMENDMENT 1 retry, REQ-5e4149d2) | 14:19:50Z | 14:35:09Z | 15 min 19 s | G2's R DONE 14:26:19Z |

Pair 1 produced no read -- G2's own window had run 13:05:57Z-13:35:57Z and closed before the ADD landed.
The issuer dispositioned that by reopening the order for one retry, which is pair 2, where G2's in-memory
read landed at ~14:26:12Z inside the window. No surprise row was filed for a condition the issuer had
already dispositioned in writing.

Evidence: `.../deliverables/NFRA_CTLPLN_TO-APPLY-30_REPORT.md`, commits `d7e3566b1d` (pair 1) and
`045091bab0` (pair 2), both on origin. One proof instance covers both pairs, VALID rc=0.

**Two method notes worth keeping.**

1. **Every start read and read-back was graded in BOTH directions** -- set-equal to the document it should
   match, NOT set-equal to the other signed document. Eight such controls across the four legs. A
   comparator that agreed with everything would print SET-EQUAL on both sides of a pair, so the
   opposite-direction read is what makes each agreement mean something. The same shape applies to the
   simulations: the walker `allowed` arm is the isolated positive control beside the two denies, and
   `explicitDeny` rather than `implicitDeny` distinguishes the Deny statement firing from a merely absent
   grant.
2. **The clock was carried independently of the message.** An ADD+27m background alarm was armed at the
   moment of each ADD, so each hard close (14:07:36Z, 14:49:50Z) would have been met with no GO and no
   inbox event. Both were stopped unused because G2 called first -- which is the outcome you want from a
   backstop, not evidence it was unnecessary. Pair 2's start read doubles as the live confirmation that
   pair 1's REMOVE had landed.

**Delivery note:** pair 2's REMOVE-NOW message did not appear in either broker probe -- `check_inbox` read
empty right after the `[INBOX]` event fired, because the watcher had already moved the file. Read it from
the lane's own `read/` dir at the exact filename the event named, per `org/XXX.md` step B. An agent that
treated the empty probe as "no mail" would have sat on an open window.

## Session total

Three orders held, three terminal, four ledger entries opened and closed, zero sentinels left. Zero
`GetSecretValue` calls by this seat across every leg. Scratch deleted at each close.

---

## TO-APPLY-30 AMENDMENT 2 -- window 3

**archetype:** DEPLOY

| window | ADD put | REMOVE put | open | closed by | hard close met by |
|---|---|---|---|---|---|
| 1 | 13:37:36Z | 13:45:41Z | 8 min 5 s | G2's REMOVE NOW | 21 min 55 s |
| 2 (AMENDMENT 1) | 14:19:50Z | 14:35:09Z | 15 min 19 s | G2's R DONE 14:26:19Z | 14 min 41 s |
| 3 (AMENDMENT 2) | 16:08:46Z | 16:33:06Z | 24 min 20 s | G2's R DONE 16:22:49Z | 5 min 40 s |

AMENDMENT 2 arrived STAGED with an explicit "do not add on this text" and the ADD waited for the issuer's
GO after G2's "ADD now" (dell2 R2 MET @`4a611a8e5f`). The staged turn did one cheap thing and no more: read
the live policy to confirm the `live == BEFORE` start condition would hold, so the GO turn had no surprise
at step 1.

Six legs total, twelve negative controls, eighteen simulated decisions, 47 min 44 s of open window, three
NEVER-2 entries all CLOSED, zero sentinels left. Zero `GetSecretValue` calls by this seat on any leg; the
three dell2 reads are G2's acts under its own ledger. Commit `e857979309`, on origin. One proof instance
covers all three windows, VALID rc=0.

**The pattern worth carrying forward:** every window closed on G2's call *before* its own alarm fired, yet
an ADD+27m alarm was armed at the moment of each ADD regardless. A backstop that only runs when the message
it is backing up arrives is not a backstop. Each window-N start read also served as the live confirmation
that window N-1's REMOVE had stayed landed -- measured on the document rather than inferred from the
previous read-back.

## Session total (final)

Three orders held, three terminal. **Five** ledger entries opened and closed, zero sentinels left. Live
`svc-irpt` policy narrow (dell2 occurrences 0) and the two Dell IAM policies carrying exactly the one action
and one ARN TO-APPLY-29 authorised. Zero `GetSecretValue` calls by this seat all session. Scratch deleted at
each close.

---

## TO-APPLY-30 AMENDMENT 3 -- window 5, and a FAIL control of this seat's own

**archetype:** DEPLOY

Window 5 (the issuer numbers by ledger history, not by this lane's count; this lane ran 1, 2, 3, 5) under a
FRESH laptop CTO consent msg 108068 @`91d0d7982c` -- a service-secret window is consented per use, so
windows 1-3's 107976 consent did not cover it. ADD put 17:57:43Z, REMOVE 18:05:37Z on G2's R DONE 17:59:20Z,
open 7 min 54 s, 22 min 6 s inside the hard close. Both legs graded as before. Commit `00b5317a75`.

**THE DEFECT, recorded because it is this seat's own.** The order says send the ADD put time AT ONCE. It
went at 18:01:39Z -- 236 s after the put, 139 s after G2 had already finished and called R DONE -- because
this seat ran the read-back, the three simulations and the alarm, and composed the relay afterwards. The
issuer reported the time "never reached MSTR or dell2".

Measured rather than accepted: the message WAS written and sits in `0.0.0_AB_MSTR`'s `read/` at 1,134 bytes.
Delivery did not fail; ORDERING did. G2 was unblocked only because it polled the live grant and acted 97 s
after the put -- luck, not design. Had it been waiting on the message it would have lost four minutes of a
thirty-minute window.

**Remedy adopted and carried in the proof instance as `put_time_relay` status FAIL:** the put time goes out
IMMEDIATELY after the put returns, before read-back, simulations, alarm or ledger work. The ADD's proof can
be assembled a minute later; a consumer waiting on the time cannot. Correct order for any future window:
put -> relay the time -> then prove.

Not filed as a surprise row: self-caused, on-task and in-lane, so the carrier is the proof instance, the
ledger leg proof and the report to the issuer.

## Session total (final, superseding the earlier total)

Three orders held, three terminal. **Six** ledger entries opened and closed, zero sentinels left. Four
secret-reader windows (eight legs, sixteen negative controls, twenty-four simulated decisions, 55 min 38 s
open in total), every REMOVE on G2's call ahead of its own armed alarm. Live `svc-irpt` policy narrow (dell2
occurrences 0); the two Dell IAM policies carry exactly the one action and one ARN TO-APPLY-29 authorised.
Zero `GetSecretValue` calls by this seat all session. One self-reported FAIL control. Scratch deleted at
each close.

---

## TO-APPLY-31 -- the Teams drafting contract, round 8 (CT-i-14)

**archetype:** DEPLOY

ONE targeted `safe-apply` of `module.ldo_001` in `infra/aws/terraform/transcripts`, code only, under both
signed halves (COO @`082e0d865a`, CTO @`c2fa3eb0b4`), both read in full first. **LIVE 23:03Z** (handler
`LastModified` 23:03:08Z, ingress 23:03:14Z, CloudTrail `b53e84c8...` / `df95ca40...` at the same times).
Branch A exactly: `0 add / 2 change / 0 destroy`, hash only, verified by `check_plan.py` rather than
eyeballed. Commit `3af6f043b3`; report + 26 evidence files in
`deliverables/teams_r8_20261009/`. Issuer closed it `complete` and graded both deviations ACCEPTED.

**Three things the next seat should not re-derive.**

1. **The method is reusable and it is in the estate.** `0.7.0_AE_CloudOps`'s `teams_r7_20261008/` carries
   `read_evidence.py` and `check_plan.py`. Both were copied and used; only one line needed changing --
   `read_evidence.py` baked `dt.datetime(2026, 10, 8, 21, 45)` for the End of Day boundary, now derived from
   the read time. Build the packaged-path list from `build.sh` itself, never from the order's prose: it names
   nine path groups, and the order's three-file summary is a diff, not the set.

2. **The root cannot be planned without a foreign `-var`.** `readers.tf` declares
   `second_reader_trust_principal_arns` with no default BY DESIGN ("WHO may assume this role is NOT decided
   in this file"), and that file post-dates the r7 deploy, so the inherited method does not mention it.
   The sanctioned handling is the issuer's A3 ruling on `COMM_ASSIST.TO-CA-d-2`: pass that ONE `-var` at its
   LIVE value read at the act (`aws iam get-role` on `teams-global-transcripts-second-reader-role`), never
   typed from an order, never a second `-var`. Its A4 is the warning: `~CA`'s first run with the var read
   `1 add / 3 change`, pulling in `aws_iam_role.silver_reader` and the KMS key policy as dependencies of
   `module.ldo_001`. Both are applied now (silver reader CreateDate 14:07:25Z), which is the only reason this
   plan read a clean `0/2/0`. **`comp-find` is what surfaced that precedent** -- the rail denied two blind
   greps and the census (35 hits over 245,926 files, banded) put the CA-d-2 order in front of me.

3. **The 60-minute End of Day window is not self-validating.** It returned **0 lines and a positive control
   of 0** tonight. `unmatched_eod=0` on a read that sees nothing is not a clean gate, and the script's own
   `gate_clear` correctly refuses it. Widen on a ladder until `REPORT` fires -- 180 minutes gave 56 lines,
   control 8, 0 unmatched -- and keep the whole ladder in the artifact, not just the passing rung.

**One safety check worth repeating before committing a plan:** `plan.json` embeds 110 environment variable
VALUES. Classify them by SHAPE before committing (no value printed): `MAIL_BEARER_SECRET` holds an ARN
pointer and `BEARER_SECRET_NAME` a secret NAME, so nothing in it is a credential. Inheriting the
predecessor's "it was fine last time" is not the same as checking.

## Session total (final)

Four orders held, four terminal and flipped by the issuer. **Seven** ledger entries opened and closed, zero
sentinels of this lane. Four secret-reader windows (eight legs) plus one code deploy. Zero `GetSecretValue`
calls, zero function invocations, zero test sends, zero untargeted applies all session. One self-reported
FAIL (TO-30 window 5's relay ordering) whose remedy TO-31's step 5 then exercised at 85 seconds.
