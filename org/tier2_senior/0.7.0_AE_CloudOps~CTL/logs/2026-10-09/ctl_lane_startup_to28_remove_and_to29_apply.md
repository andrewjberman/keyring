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
