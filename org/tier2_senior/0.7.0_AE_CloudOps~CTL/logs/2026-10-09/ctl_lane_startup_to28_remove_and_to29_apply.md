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
