# Lane ~MP post-reboot startup; MP-x-4's G-REL gate measured OPEN on the r29 limb -- 0.7.0_AE_CloudOps~MP

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

**Date:** 2026-10-09
**Task Order:** NFRA_MCPORTAL.TO-MP-x-4 (held, `staged`, NOT started)
**Status:** BLOCKED

---

## Objective

Bring lane `~MP` back up after the Site Z reboot (/watcher, then the org/XXX.md protocol and the
/cloud-ops one-shot), establish what this lane holds, and decide whether the one order it holds
may start. No deploy was authorized or attempted.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md step A.3 forwarder exercise; a forwarder RAN, 102 of 102 comp-tools resolve bare |
| comp-find | `comp-find 'TO-MP-x-4' --files` | FAIL | rail-denied F4 (census into a receiver that can cut the denominator); correct, my `\| head -20` was the defect |
| comp-find | `comp-find 'TO-MP-x-4' --files --limit 20` | FAIL | exceeded the 120 s tool timeout and was backgrounded; native Glob answered in one call |
| comp-schedule | not run | SKIPPED | MP-x-4's own `<preflight>` declares it NOT-APPLICABLE (one-shot deploy, no cron/alarm/cadence) |
| comp-iam | not run | SKIPPED | MP-x-4's `<preflight>` declares it NOT-APPLICABLE (no IAM in this cell; the grant is MP-x-3's, already applied) |
| comp-blast | not run | SKIPPED | AE minimum is "before infra changes"; zero infra changes this window, the order never started |
| comp-pipescript deployed | not run | SKIPPED | AE minimum is "before every gold-run trigger"; no gold run in scope |

**What worked:** `comp-which` confirmed the rail is live end to end rather than merely resolving.
The rail's F4 denial was correct and its RUN NEXT line was the exact fix.

**What failed:** `comp-find 'TO-MP-x-4' --files --limit 20` did not return inside 120 s on this
device and was moved to the background. A known-path question beat it: the TO lives in the mission
tree, and `Glob org/missions/**/NFRA_MCPORTAL/**/*MP-x-4*` resolved it in one call. I had been
looking in `org/tier2_senior/.../task_orders/`, which is the flat-project home; a tree project files
its orders under `org/missions/D*/<MACRO>/<CODE>/task-orders/`.

**Gap found:** a `<round>` tag and a gateway RELEASE number are two different series in NFRA_OPLGTW,
and a census keyed on the wrong one returns rows. Selecting OPLGTW task orders on
`<round>29</round>` returned three `complete` orders, one of them named `gateway-release-r28` -- so
the filter printed a plausible non-empty answer to a question I had not asked. Round 29 produced
release r28; release r29 is cell `OG-rl-15` at `<round>32</round>`. The tell was an incidental
figure inside the hit: a file whose name says r28 answering a query for r29. Reading the named cell
directly is the sound instrument.

---

## Work Completed

### 1. /watcher and registration

Lane `~MP` read NOT REGISTERED at load. Registered (PID 16168), census of
`inbox-watch.sh <serial> stream` rows went 0 -> 1, so nothing was reaped. Three arms this window as
the harness killed each at 30 minutes: task `b4a128yjh` pid 31012, then `bu0thfpcc` pid 3904, then
`bc3fl99fy` pid 38120. Each expiry was re-armed the same turn in one Monitor call with no skill
load. Both expiries carried zero events, which is consistent with the delivery-state read below
rather than with a broken filter.

Drive prefix resolved to `/c` (no `/cygdrive`), and the script path is quoted in the Monitor command
because this device's workspace path contains a space.

### 2. org/XXX.md steps 1 through F

- Identity cross-checked: `liveness.json` shows `0.7.0_AE_CloudOps~MP` at PID 16168 and no other
  serial at that PID; `$OPAL_AGENT_SERIAL` agrees. 6 of 19 rows printed, filtered on the base name.
- A.1 session serial file written for `8b0598e5-84ce-4f2d-8d96-b85bcab8d302`.
- A.2 `audit-archive-invoker.py`: rc=1, 15 findings, baseline 2026-10-09T051048Z, snapshot not due.
  All 15 are standing device classes with owners (5 MANIFEST-ENTRY-MISSING-LIVE, 2
  UNCOVERED-AUDIT-LOG, 3 NON-APPEND-EDIT, 5 ERROR-FAILCLOSED), so none was re-filed.
- A.3 PATH: 102 of 102 comp-tools resolve bare, forwarder exercised live.
- D: owned-paths pre-commit hook already wired, idempotent no-op.
- E: `.comp-graph/.agent_context` set to `SERIAL=0.7.0_AE_CloudOps~MP`, `TO_ID=` empty.
- F: zero crons armed, per this serial's row (every non-MSTR, non-COO serial: /watcher once, then
  event-driven).
- `/cloud-ops` loaded once as the seat's session orientation.

### 3. What this lane holds

`to-check.py --all --assignee 0.7.0_AE_CloudOps~MP` returns **1 active TO**:
`NFRA_MCPORTAL.TO-MP-x-4`, `<status>staged</status>`, issued by `2.0.0_SA_COO~MP`, `<risk>WORLD</risk>`.

Two reads that would have misled and did not:
- `get_agent_status` lists "Pending task orders (5)". Those are BASE-scoped and exact-string
  matched (CLAUDE.md 22a), so they are not this lane's orders. `<issued_to>` is the only truth.
- The tail of the `to-check` output is its THIRD-POPULATION list -- 91 of 5085 faces carrying a
  `<status>` tag and no recognised assignment field. I read the tail first and briefly had a page
  of other seats' completed orders in hand. The head carries the answer and the denominator.

### 4. The decision: MP-x-4 does not start

MP-x-4's record face carries **G-REL: spawn only when MP-x-3 is drained AND NFRA_OPLGTW r29 is
drained by `2.0.0_SA_COO~O`.** Measured from artifacts, not from any seat's status prose:

- MP-x-3: drained. `2.0.0_SA_COO~MP` flipped it complete at `93052772a7` after draining this lane's
  proof fix at `bee68a57eb`.
- OPLGTW r29: **OPEN.** `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-rl-15.gateway-release-r29.md`
  is `<status>pending</status>`, `<issued_to>0.9.0_WK_NFRA_OPLGTW~43</issued_to>`, `<round>32</round>`.

Independently, the host is not on r29. So the gate is open on one limb, and the order is `staged`
with no GO -- two separate reasons not to act. MP-x-4 step 1 orders the release built on the live
`deployed_commit` read at the act, and that base does not exist on the host yet; starting now would
build on r28.

---

## Decisions Made

1. **Did not start MP-x-4.** `staged` means wait for the GO, and G-REL is open besides. Recorded
   rather than messaged as a question, because nothing is adjudicable here -- the gate is the
   issuer's own text.
2. **Did not chase r29.** `2.0.0_SA_COO~O` owns OPLGTW and is live and working it. Chasing it would
   convert this seat's precondition into pressure on another lane's round.
3. **Did not mint a surprise row for the four stale IRPT `.open_deploys/` sentinels** (see Blockers).
   They belong to a project this lane does not hold, so naming a `disarm_owner` would be
   adjudicating wider than this seat's scope. Surfaced instead.
4. **Sent one readiness message** to `2.0.0_SA_COO~MP` (the issuer, live and at startup) carrying
   the measured G-REL state so it need not re-derive it. One point, under the word cap, paths cited.

---

## Files Modified

| File | Change |
|------|--------|
| `org/mcp/sessions/8b0598e5-....serial` | written (A.1; device-local, gitignored) |
| `.comp-graph/.agent_context` | `SERIAL=0.7.0_AE_CloudOps~MP` (E; device-local) |
| this log | new |

No product, infra or Terraform file was touched. Nothing was deployed, applied or pushed.

---

## Verification

```
=== OG-rl-15 tags (the gate's second limb) ===
FILE org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-rl-15.gateway-release-r29.md
10:<issued_to>0.9.0_WK_NFRA_OPLGTW~43</issued_to>
252:<status>pending</status>
253:<round>32</round>
257:<risk>WORLD</risk>

=== live deployed_commit on i-07dccb1615503ac99 (infra/aws/ec2/EC2_MANIFEST.json) ===
deployed_commit          = aa75078e1b72a28219e6148d3ec8e9bf705ea111
previous_deployed_commit = 510c8cfed2c852946e3e57fb4dd1c0467e2f3a52
mcportal_commit          = a3bff71ffa3f5c73aa0fb7ea1e7386434e233054
release_note             = "NFRA_OPLGTW OG-rl-14 PHASE B (the r28 release: ...)"
```

The manifest's own `release_note` names `aa75078e1b` as the r28 release, so the live host and the
pending `OG-rl-15` agree: r29 has not shipped.

```
=== mail, after the second watcher gap ===
check_inbox            -> Inbox empty for 0.7.0_AE_CloudOps~MP.
get_delivery_state since 2026-10-09T07:04:00Z -> 0 rows ("Zero ROWS MATCHED -- not zero delivered")
get_delivery_state (all) -> TOTALS: READ=4 (denominator 4); ACKABLE 4 of 4; coverage 4/4
```

---

## Blockers

**BLOCKED (evidence-cited):** `NFRA_MCPORTAL.TO-MP-x-4` cannot start.
- Limb 1 of G-REL holds (MP-x-3 drained @`93052772a7`).
- Limb 2 does not: `OG-rl-15` is `pending` (file + line cited above) and the host runs r28
  `aa75078e1b` per `EC2_MANIFEST.json`.
- Separately the order is `staged`, and `staged` waits for the GO from `2.0.0_SA_COO~MP`.
- Owner of both: `2.0.0_SA_COO~MP` issues the GO; `2.0.0_SA_COO~O` owns the r29 drain. This seat
  chases neither.

**SURFACED, not blocking this seat, no owner asserted:** four `org/critical_paths/.open_deploys/`
sentinels sit OPEN and **untracked** in this shared tree, all IRPT, dated 09-23 to 09-25:
`irpt-p-live-scope-20260923`, `irpt-performance-49f-engine-20260924`,
`irpt-holdings-principals-dispatch-m-20260925`, `irpt-performance-inf-one-use-20260925`. Under
NEVER-2 an open entry proves only that the writing device saw no completion, so each needs an
artifact measurement (rev-parse + describe + is-ancestor with a positive control) by its owner
before anyone acts on it, and world-done closes SUPERSEDED rather than re-executing. Being untracked,
they are invisible to every other worktree's read. The IRPT-seated sibling on this device is
`0.7.0_AE_CloudOps~DB2`. This lane took no action on them.

---

## Current State

Lane `0.7.0_AE_CloudOps~MP` is LIVE on Site Z, PID 16168, branch `box/sitez`, workspace root
`C:/Users/Opal Bloomberg/Desktop/ajb_workspace`. One inbox watcher armed: Monitor task `bc3fl99fy`,
script pid 38120, census exactly 1 row. Inbox empty; all 4 ackable rows ever addressed to this lane
are READ; 0 rows delivered since 07:04Z. Broker summary reflects the blocked state and names the
gate. Zero crons armed.

The lane holds exactly one task order, `NFRA_MCPORTAL.TO-MP-x-4`
(`org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-x-4.control-plane-release.md`),
`staged`, not started, nothing cut from it. Its three AC scripts live under
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/x4.AC{1,2,3}.sh`
and the issuer's own dry-run at base has all three FAIL, which is the expected pre-act state.

This lane's previous session (same day, pre-reboot) completed MP-x-3: the gateway read grant
`gateway-mcportal-fabric-read-policy` is LIVE, its NEVER-2 ledger entry
`nfra-mcportal-r4-fabric-read-grant` is CLOSED, and the proof instance is VALID at `42ed038fea`.
Nothing from that window is left half-landed and this lane holds no open deploy ledger entry.

Issuer context for a reader with none: `2.0.0_SA_COO~MP` is live and at startup;
`2.0.0_SA_COO~O` is live and working the OPLGTW post-reboot resume including the r29 halves.
The cold-read figure MP-x-4 step 2 turns on was measured by the issuer at 04:2xZ on
`i-07dccb1615503ac99`: cold 21.3 s, warm 0.8 s, 3,004 records, against R-13's 30 s bar -- a thin
margin that grows with daytime commit volume, so the release-time measurement is the one that counts.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~MP]` Hold event-driven. Act on the next `[INBOX]` event the same turn, and
   re-arm the Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.
2. `[2.0.0_SA_COO~MP]` Issues the GO on MP-x-4 once G-REL closes. On that GO this lane reads the
   order, flips `<status>` to `pending`, cuts a linked worktree from `box/sitez` HEAD with a no-cone
   pattern list (row Z-W5-S2), and runs step 1's census against the live `deployed_commit` read at
   the act -- never the r28 value recorded here.
3. `[2.0.0_SA_COO~O]` Owns the r29 drain (`OG-rl-15`, worker `0.9.0_WK_NFRA_OPLGTW~43`). This lane
   does not chase it and re-reads the limb only when a GO arrives.
4. `[0.7.0_AE_CloudOps~DB2]` The four untracked IRPT `.open_deploys/` sentinels named under
   Blockers want an artifact measurement by their owner. Surfaced, not assigned.
