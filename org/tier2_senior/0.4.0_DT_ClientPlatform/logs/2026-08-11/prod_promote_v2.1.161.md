# 0.4.0_DT_ClientPlatform — 2026-08-11 — portal PROD promote v2.1.161 (OPAL_INVPHL)

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, VALIDATE

Window: since `36961296c0` (the OPAL_INVPHL TO-1/TO-2 build log) through the completed
promote. Filed under 2026-08-11 because the whole window is 08-11Z work; the date rolled
during the close-out.

## Current State

**`opalinvest.dev` is serving `portal-v2.1.161`.** All seven promote legs landed; nothing
stranded.

| | |
|---|---|
| PROD commit | `fbbb9b39a0ce4103eaaf8cdf3f84581d3f244448` |
| Tag | `portal-v2.1.161` (object `0f3fda297a05`) — **peels to** `fbbb9b39a0ce` == PROD head |
| CI | run `31541217841` "Deploy to Production" `conclusion=success` |
| Rollback | `dd2907ebf75eacb8b074c04bd54814a9e612e1a8` (v2.1.160), encoded in the merge message |
| DEV | `335dd19833403d8a6646d2f06d6eebaf3eebca40` |
| Workspace pointer | `9bd2365b` -> `335dd198`, committed `@b59a8841ad`, pushed (origin/CLOUD == HEAD) |
| Main portal tree | **DEV** — never left (Rule 19) |
| Ledger | `org/critical_paths/change_management/20260811T215500Z_portal_prod_promote_OPAL_INVPHL.md` — CLOSED |

**What is live for clients:** the model-portfolio modal on two trigger surfaces
(`/portfolios` Benchmark heat map, `/positioning` bar headers) and the Philosophy page
(`/cma` -> `/philosophy` with a redirect, five-pillar strip, pillar modals). Both TOs
**complete** `@5f4a5c6aa0`, proof-of-spec instances VALID at 0 violations.

## Deployment Sequence + Verification (DT role addition — actual output)

Authority: Andrew-direct ~2148Z at this terminal, VERBATIM *"i like it get this build
promoted to PROD"*, after he smoke-tested on localhost:5175 against the live backend
(vite proxies `/api` + `/v1` to CloudFront/API-GW with auth forwarded — real data, not
fixtures). COO's earlier "do not promote" scope note SUPERSEDED by the later sovereign word;
COO confirmed that reading at 215124Z.

| Leg | Actor | Outcome |
|---|---|---|
| 1 push DEV | MSTR | `origin/DEV @335dd198` 21:56:06Z, D-1 PASS |
| 2 re-assert PROD | DT | matched `dd2907eb`, no dry-run pollution |
| 3 worktree + install | DT | `.runtmp/portal-promote-20260811T215752Z`, 420 pkgs FOREGROUND |
| 4 merge + parity | DT | merge `fbbb9b39`; **parity 0 lines** |
| 5 push PROD | MSTR | `dd2907eb..fbbb9b39`, remote read-back confirmed |
| 6 gitlink | DT commit / MSTR push | `@b59a8841ad`; origin/CLOUD == HEAD |
| 7 teardown | DT | prune clean, main tree DEV, cwd root |

```
=== PARITY GATE (leg 4) ===
$ git diff origin/DEV HEAD
(end -- empty above = PARITY OK)
diff line count: 0

=== MERGED-TREE TYPECHECK (leg 4) ===
MERGED-TREE TYPECHECK RC=0
FILES EXAMINED: 1931

=== CI, ENUMERATED BY headSha (leg 5) ===
runs on my sha: 1 of 10 listed
  31541217841  Deploy to Production       completed  success
ALL GREEN

=== TAG PEEL (leg 5) ===
  portal-v2.1.160 -> object 325980b25f3c... | commit dd2907ebf75eacb8b074c04bd54814a9e612e1a8
  portal-v2.1.161 -> object 0f3fda297a05... | commit fbbb9b39a0ce4103eaaf8cdf3f84581d3f244448
PROD head: fbbb9b39a0ce4103eaaf8cdf3f84581d3f244448

=== TEARDOWN (leg 7) ===
error: failed to delete '.../portal-promote-20260811T215752Z': Filename too long
  (documented Windows long-path class; prune cleans git tracking regardless)
main tree branch: DEV
cwd: /cygdrive/c/Users/AndrewBerman/Desktop/ajb_workspace
```

⛔ **EVIDENCE DELIBERATELY NOT CITED: CI's typecheck step.** It resolves
`portal/tsconfig.json` (`"files": []`, references only), examines **zero files**, exits 0
every run. "CI was green" would be true and misleading. The typecheck evidence is the
merged-tree run above — 1931 files, an invocation mutation-proved red earlier in the session.

## The blocker, and why it was not overridden

`git push origin DEV` was DENIED by `never-rules-gate.sh` GATE 5 (LD-0367/LD-0368,
integrator-only push on a shared branch; `:490` lists CLOUD/DEV/PROD/main/master). An audited
`# never-override:` escape existed and was **not used** — the gate's own text requires
coordinating with the integrator first *because the override still republishes the tree*, and
I could not enumerate from my seat what other seats' commits a push would carry. Routed to
`0.0.0_AB_MSTR`, who chose option (a) (they push, I drive everything else) and declined the
override for the same reason.

**Vindicated concretely:** MSTR's own enumeration of the CLOUD payload was **40 commits across
7 authors**. That is exactly the visibility the gate keeps on the integrator's side, and the
reason self-authorizing would have been wrong.

⚠ **STANDING FINDING (CTO/COO, not closed by this promote):** three of `/prod-deploy`'s seven
legs push a shared branch, so **the DT lane that OWNS the procedure structurally cannot execute
it alone.** Tonight worked because the integrator was awake and fast. The fix is a
procedure-vs-gate reconciliation, not a promote-time improvisation.

## Three self-caught errors (recorded because none were caught by a gate)

1. **Fabricated SHA.** I wrote full 40-char hashes into the TO-2 proof-of-spec by expanding a
   short hash from memory. Caught on re-read; replaced with the real `335dd19833403d8a...`.
2. **Wrong worktree path in a handoff.** Told MSTR `...215656Z` when the real path was
   `...215752Z` — I had written it to a file at creation and then quoted from memory instead of
   reading it back. Corrected before they ran it; their re-read discipline confirmed it arrived
   in time. Would have failed loudly, not deployed wrongly.
3. **Close-out table filled ahead of the acts.** The ledger committed at `b59a8841ad` marked
   legs 6 AND 7 `DONE` when neither had happened. Corrected to measured state `@91e1854258` and
   flagged in the artifact rather than quietly fixed — filling a close-out table from intention
   instead of measurement is the precise failure that artifact exists to prevent.

**Common root:** writing a value down and then not reading it back. All three were caught by
re-reading the artifact rather than by any control.

## MCP traffic

~14 messages. Significant: Andrew-direct promote order (recorded VERBATIM + broadcast same
turn); COO 215124Z clearance + supersede of their own scope note; COO 220314Z superseding their
own 214652Z workaround after CVO fixed the schema enum; MSTR option-(a) decision + three
shared-branch push confirmations; CTO 213758Z Rule 25 landing.

**Handoff-latency finding, both directions:** MSTR pushed leg 1 and moved on with no completion
signal, so for ~9 minutes polling the remote was my only oracle; COO then fired an unblock for a
leg already consumed. **Sent is not read, and done is not reported.** Cost was minutes only, but
a multi-seat promote has no ack on the return leg.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `gh run list --json databaseId,headSha,workflowName,status,conclusion` | enumerate CI by headSha, then RE-enumerate after completion | PASS — 1 run on `fbbb9b39`, success. Never the branch badge (the 7d544d27 incident: one workflow SUCCESS, another FAILURE, same commit). Re-enumerated in case a workflow appeared late. |
| `git rev-parse <tag>^{commit}` | peel the annotated tag | PASS — `portal-v2.1.161` peels to `fbbb9b39a0ce` == PROD head. Peeled deliberately; `ls-remote`'s object sha caused the v2.1.114 false double-merge read. |
| `git diff origin/DEV HEAD` | leg-4 parity gate | PASS — 0 lines; merged PROD tree byte-identical to the verified DEV tree. |
| `tsc -b --listFiles` | merged-tree typecheck WITH denominator | PASS — rc=0, 1931 files. The denominator is the point: the CI form prints 0 lines and still exits 0. |
| `proof-of-spec-check.py <instance> C1..C8` | both instances, unpiped, positional id set | PASS after CVO's enum fix — 0 violations each, on an honest `frontend_component` declaration. |
| `safe-commit.sh` | 5 commits this window | PASS — risk-reflex fired on CLAUDE.md (12 recorded claims); citation read, not relevant (vendor-egress/vintage-label scope). |

**What worked:** enumerating CI by headSha and peeling the tag both did real discriminating work
— and the `--listFiles` denominator is what separated a real typecheck from the blind one.
**What failed:** nothing this window; `worktree remove` hit the known Windows long-path failure,
which the procedure already declares acceptable.
**Gap found:** none new. The two carried forward are the CI zero-file typecheck step (routed to
COO as a one-line TO on my lane) and the `/prod-deploy`-vs-GATE-5 collision above.

## Blockers

None. Leg 6's push was the last open act and has landed (`origin/CLOUD == HEAD`, 0 unpushed).

## Next Steps

1. `[1.0.0_SA_CTO]` / `[2.0.0_SA_COO]` — the `/prod-deploy` vs GATE 5 collision: three legs push
   shared branches; the owning lane cannot run its own procedure unattended.
2. `[2.0.0_SA_COO]` — sequence the one-line CI typecheck TO onto my lane (`ci.yml:56` should call
   package.json's `typecheck`). **Whatever lands must be MUTATION-verified, not accepted on a
   green run** — a step that exits 0 is exactly what exists today.
3. `[0.4.0_DT_ClientPlatform]` — live PROD visual smoke of `/philosophy` + the model modals at
   Andrew's convenience; nothing outstanding otherwise.
4. `[0.0.0_AB_MSTR]` — cross-fabric portal note received 20260812T131326Z, unread at log time;
   will action on next turn.
