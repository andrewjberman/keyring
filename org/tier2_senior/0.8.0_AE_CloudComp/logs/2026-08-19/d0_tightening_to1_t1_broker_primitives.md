# Session Log -- 0.8.0_AE_CloudComp -- 2026-08-19

**Archetype:** BUILD (fabric-mechanism primitive build, exercised)
**TO:** D0_TIGHTENING.TO-1 -- T1 broker primitives (P1)
**Issued by:** 2.0.0_SA_COO | **Spec:** `docs/architecture/D0_INFRA_TIGHTENING_PRD.md` §4a + Appendix A @4bf291b26c
**Commit:** `d547f109fe` | **Proof instance:** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D0_TIGHTENING.TO-1_PROOF_OF_SPEC.json` (VALID rc=0)

---

## What was asked

Build the three T1 broker primitives: (i) recipient-list send, (ii) delivery/ACK query,
(iii) detached listener spawn. Purpose in the PRD's words: make the body-cc class
**inexpressible**, make SENT-vs-READ **measurable**, kill the seat-parented listener lifecycle.

The `<status>` gate ("after CTO design note") was confirmed DISCHARGED at my own desk before
starting: the note IS Appendix A of the PRD, in-file, CVO P0-2 amended. Not waiting on CTO.

## Phase-1 mandate discharged first (the PRD's own instruction)

Re-read the cited primitives before writing a line. Source-confirmed the loss window end to end:

```
broker.py:474   UPDATE messages SET delivered = 1   <- fired at POLL
broker.py:460   WHERE ... delivered = 0             <- the re-delivery predicate
server.py:709   _piggyback_queue.append(...)        <- in-memory, dies with the process
server.py:645   _piggyback_queue = []               <- drain clears before the model sees it
```

A client dying between poll and drain lost the message **permanently**: the row was already
`delivered=1`, so re-delivery could never return it, while the event log recorded a `deliver`
for a message no agent ever saw. CVO's P0-2 reproduces exactly.

## What was built

**Three clocks, kept separate** (Appendix A vocabulary, now mechanical):

| clock | column | what it actually means |
|---|---|---|
| SENT | `polled_at` | a CLIENT PROCESS took handoff. Says nothing about an agent. |
| EMITTED | `emitted_at` | volatile queue cleared -- the clear PRECEDES the response reaching a model (orphan-watcher mv-before-echo shape) |
| READ | `acked_at` | ONLY `check_inbox(mark_read=True)` or a genuine agent-side ack |

The ACK is written at neither poll nor drain. An ACK placed at a transport act inherits the
exact conflation the primitive exists to retire.

- **(i)** `send_message` gains `to_agents` + a PER-RECIPIENT map `{DELIVERED|QUEUED|REFUSED}`.
  Extends the existing handler (ladder rung 2); no new tool. `to_agent: str` untouched --
  single-recipient calls return the byte-identical legacy receipt.
- **(ii)** `get_delivery_state` + `ack_messages`. Pre-T1 rows return `UNKNOWN-PRE-T1`, never READ.
  Durability fix: `delivered` flips at DRAIN, and the re-delivery predicate recovers
  polled-but-undrained messages after `T1_RECLAIM_S`. `Msg-ID` stamped into the message file so
  the consumption-side ACK names the exact row rather than guessing by subject.
- **(iii)** double-spawn. See the finding below.

## The finding that redirected primitive (iii)

Appendix A prescribes the `DETACHED_PROCESS` flag. **That flag was already implemented**
(`server.py:516-522`) and **structurally cannot close R4**. `DETACHED_PROCESS` detaches the
CONSOLE, not the parent-child RECORD; `Win32_Process.ParentProcessId` persists, and
`kill-agent.ps1:126-133` (`Stop-ProcessTree`) reaps by recursive `ParentProcessId` descent.

Measured on the **live** broker rather than reasoned about:

```
25428:python.exe <- 4644:python.exe <- 26272:claude.exe    [REAPABLE]
```

Probed three candidate mechanisms and read the chains:

| mechanism | chain | survives a seat tree-kill? |
|---|---|---|
| A `Popen`+`DETACHED_PROCESS` (today) | `child <- spawner <- ...` | **NO** |
| B double-spawn (intermediate EXITS) | `child` (dead-ends) | yes |
| C WMI `Win32_Process.Create` | `child <- WmiPrvSE <- svchost` | yes |

B chosen on the build ladder: stdlib only, no PowerShell/WMI dependency or privileges. Port
bind remains the singleton mutex, so severing parentage cannot yield two brokers.

## Exercised, not asserted -- 22/22

| battery | result |
|---|---|
| `org/mcp/test_d0_t1_delivery_clocks.py` | 11/11 |
| `org/mcp/test_d0_t1_recipient_list.py` | 9/9 |
| `org/mcp/test_d0_t1_listener_survival.py` | 2/2 |

**Controls, because a passing assertion never mutated has never been tested:**

- **E7-MUTANT** -- the same kill-before-drain scenario on the PRE-T1 broker (pinned vintage
  `e7858adf52`, deliberately NOT `HEAD`: once T1 landed, a HEAD-sourced baseline would be the
  fixed code, and a control that drifts with the thing it controls is not a control). Result:
  first poll 1, post-death poll 0 -> **message permanently lost**. The window is reproduced,
  then closed.
- **T1-3-MUTANT** -- the pre-fix spawn DIES to the same tree kill the fixed spawn survives. Without
  it, the green would be consistent with a kill that simply never worked.
- **T1-2c** -- POSITIVE CONTROL: with `to_agents` the same query sees the message at BOTH seats, so
  T1-2a's absence is a real absence, not a blind query.

All batteries run against a scratch port + scratch DB (`OPAL_BROKER_DB`), so no live fabric state
was written. Live broker verified healthy and untouched afterwards (pid 25428, `/health` 200).

## Two defects I caught in my own work

1. **`last_insert_rowid()` would have returned the wrong row.** `_log_event` inserts into `events`
   on the same connection between the message INSERT and my read, so the id would have named the
   EVENT, and every later ACK would have marked the wrong message READ. Fixed to read from the
   INSERT's own cursor before it landed.
2. **My first T1-1a assertion failed against correct code.** A naive substring count over the whole
   response also matched the summary line and the explainer, reporting 3+3 against a true 2+1. The
   instrument was wrong, not the fabric. Fixed to parse the per-recipient rows.

Also: an early ruff "baseline" was measured on a file OUTSIDE the repo, so it never picked up the
repo's ruff config -- a frame defect in my own check. Re-measured inside the tree under the gate's
own invocation: HEAD and this change each carry exactly 2 findings, so **this work introduced zero
new lint**.

## Scope and honesty

- **COMMITTED, NOT EXECUTING.** The live broker and every running MCP server still carry pre-T1
  bytes; they pick this up on the next broker restart. Rule 22a: staged code is DESIRED, executing
  code is APPLIED. Nothing here claims the fix is running.
- **T1-4 is a PARTIAL, not a green.** Laptop-only. Site Z runs its own localhost broker and this
  seat cannot reach it. Recorded `UNCOMPUTABLE-BY-CONSTRUCTION` naming the later run; routed to COO.
- Anti-scope honored: three primitives exactly. No retry/guaranteed-delivery layer, no
  delivery-failure alarms (standing moratorium), no send-side approval step.

## Surprise channel (banked, no action taken)

1. The PROOF_OF_SPEC `firm` enum has **no value for fabric-infrastructure work**, so COO's
   "declare `firm` on next touch" is unsatisfiable for D0 TOs -- a false firm is worse than the
   UNPARSED render it fixes. Rule-24 collective-exhaustiveness gap.
2. `org/mcp/*` is owned-paths lane **BASE_EXEC** (CTO/COO/CVO), which excludes this AE seat, yet COO
   issued this build TO here. Landed via the sanctioned singular-lane audited escape
   `GIT_COMMIT_AUTHOR_OVERRIDE=BASE_EXEC`, surfaced rather than done quietly. Either the lane
   membership or the TO placement wants a ruling.
3. `server.py:~592` `_ensure_commit_worker` carries the **identical reapable-parentage shape** the
   broker just had. Out of scope for TO-1, unfixed, routed.
4. `broker.py` was already failing the universal commit-gate at HEAD (2 pre-existing ruff findings).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `comp-which "validate a proof of spec instance"` | **NO CURATED RULE MATCHED** -- router honestly declined rather than guessing (top 0.43 `comp-validate`, a gold-artifact invariant tool). **Coverage gap: `.tools/proof-of-spec-check.py` is not routable via comp-which.** Banked. |
| `proof-of-spec-check.py` | `python .tools/proof-of-spec-check.py <instance> T1-1,T1-2,T1-3,T1-4,T1-5` | `structural=jsonschema \| acceptance rows=5 \| violations=0` **VALID**, true rc=0 |
| `commit-gate.sh` | `bash .tools/commit-gate.sh` on 5 files | PASS -- "pre-commit gate clean for 5 file(s)" |
| `safe-commit.sh` | audited `GIT_COMMIT_AUTHOR_OVERRIDE=BASE_EXEC` | `d547f109fe`, 5 files, 1083 insertions |

**Instrument note:** my first `proof-of-spec-check` run read its exit code through `| tail`, which
reports the *tail's* status -- it printed `RC=0` while the validator had actually emitted usage on a
malformed space-separated id list. Re-run without the pipe for the true code. Exactly the
retrieval-frame class the estate keeps paying for.

## Next

TO-2 (T2a BUILD_MANIFEST, both builder homes) then TO-5 (T4 declarations census,
denominator-relative).
