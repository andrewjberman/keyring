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

---

# TO-1 CLOSURE + TO-2 + TO-5 (same session)

## TO-1 closed

COO RAVC-4 ACCEPTED with a named partial, then **CLOSED at 22:29Z** once T1-4's named later run
landed: the site-Z leg ran 3/3 batteries rc=0, **22/22 PASS**, validated-accepted at COO~Z and
ferried by MSTR (bus 368f34a6). **Both fabrics: 44/44.** Proof instance amended to PASS with the
site-Z evidence and `firm: FABRIC` added (`b95a3d535e`).

**Frame kept precise, and MSTR corrected their own ferry frame to match mine:** the batteries spawn
SCRATCH brokers from the trunk vintage and do **not** measure either device's running `:7800`
broker. 44/44 certifies *the trunk T1 code exercised green on both platforms* -- the both-fabrics
read T1-4 asks for -- while **both fabrics' running brokers remain pre-T1 until restart.** COO holds
the laptop cycle before THU 12:45Z. MSTR's sharpened fact for both boards: on a live pre-T1 broker
the loss is **deterministic, not probabilistic**, so both restarts are correctness acts, not hygiene.

CTO landed all four of my routed items @64114c5511 -- Appendix A(iii) corrected with my measured
mechanism (the original flag-prescription retained as the record of a wrong design), a sibling TO
cut for `_ensure_commit_worker`, **`FABRIC` added to the PROOF_OF_SPEC firm enum**, and a
`D0_T1_BROKER` window lane granted with the lane-vs-placement ruling (one-off = the audited escape I
used, correct; recurring = a window-scoped enumeration). COO ruled the owned-paths collision **their
placement error, not my workaround.**

## TO-2 -- T2a BUILD_MANIFEST stamps (`1bd55740e9`, proof VALID rc=0 `1670e3e729`)

**Measuring first changed the work.** Both homes *already* emitted an in-zip manifest at HEAD, so
the criterion's headline was satisfied before I started. The real gap was the section-4b field
contract:

| | HEAD | now |
|---|---|---|
| homes emitting in-zip manifest | 2/2 | 2/2 |
| homes emitting a sidecar | 1/2 | 2/2 |
| **homes SECTION-4b COMPLETE** | **0/2** | **2/2** |

**Two of the four contract fields cannot live in-zip**, and forcing them there would each break
something real: `zip_sha256` is self-referential (adding the hash changes the hash), and `built_at`
is wall-clock -- and this builder deliberately pins zip entries to a fixed timestamp so
byte-identical rebuilds stay byte-identical. So in-zip carries **content identity** and stays
deterministic; the sidecar carries the **build event**. The Rule-22a read is served entirely by the
in-zip copy, which is the leg that has to survive the trip to AWS.

**Determinism control is two-sided, because a field can be present and dead:** zip hash must be
IDENTICAL (falsifies "reproducibility survived") *and* sidecar `built_at` must DIFFER (falsifies
"the field is live"). 4/4 held.

**It fired a real fail first, and I isolated it rather than explaining it away:** the publisher's
rebuild hashes differed -- because `--pin HEAD` resolved to two *different* commits
(`4a2b34df76 -> 609aca9b0e`) in ~2 minutes in this shared tree. **`--pin HEAD` is not a pin**, and
that builder's own docstring promises "FROM A PINNED COMMIT ... never the working tree." Banked.

**T2a-3 stated with its measured gap:** the stamp rides the BUILDER, so any EC2 service adopting a
bundling builder inherits it -- but **0 of 27** EC2 services bundle (0 hits across 347 files);
EC2 ships loose objects behind `safe-ec2-deploy.sh:155`. Correct mechanism, inert today.

## TO-5 -- T4 declarations (`b1cd375c32`, proof VALID rc=0 `84b9097f76`)

**The denominator is 22, not the 16+3 prior** (19 Lambda + 3 EC2, +1 declared boundary case).
**+3 Lambda rows the prior would have left undeclared** -- precisely the failure CVO P0-1's
denominator-relative amendment was written to prevent. It earned its keep.

The census's own artifacts carry **four different numbers**: summary 15, prose + both TOs 16,
axis-class sum 19, actual rows 19. I take 19 -- the only figure that is a direct *count* of the
evidence rather than a summary of it. **That census is my own 08-18 delivery, so this is my defect**,
reported rather than silently patched.

**The EC2 axis has no TWO-HOMES class at all** (`UNREAD 14 / STALE-BY-NEGLECT 6 / CURRENT 5 /
STAGED-ORPHAN-ONLY 2`). A scan keyed on that string returned a clean, confident **0** against a
report claiming 3 -- the wrong question asked cleanly, caught only because a 0 against a documented
3 was too tidy to accept. Re-enumerated by shape across both EC2 axes.

**The one FORK-DELIBERATE is the most load-bearing row.** `opal-partners-data`'s two canonical homes
are `data/black_diamond/` and `data/cot/` -- and bd<->cot separation is **law**, gate- and
IAM-enforced. 18 of 19 Lambda rows share the subkind `BUNDLED-COPY-DIVERGED-FROM-CANONICAL` and this
one shares it **while meaning the opposite**. Any subkind-driven pass would have routed a
consolidation the estate forbids at two independent layers. That is why every row is declared from
its evidence, never from its class name.

## Instrument misses I caught in my own work (this session, all four)

1. **`last_insert_rowid()` would have named the wrong row** -- `_log_event` inserts between the
   message INSERT and the read, so every later ACK would have marked the wrong message READ.
2. **A test assertion that failed against correct code** -- naive substring counting matched the
   summary line too (3+3 against a true 2+1). The instrument was wrong, not the fabric.
3. **A ruff "baseline" measured outside the repo** -- so it never loaded the repo's ruff config.
   Re-measured in-frame under the gate's own invocation: zero new lint introduced.
4. **`resolve_lane()` returning `None` for everything, including the positive control** -- I was
   passing the whole config instead of `config['paths']`. Without the control this would have become
   19 rows of false "UNRESOLVED" presented as a finding about the estate rather than a bug in my call.

Plus one near-miss on absence: `.tools/safe-ec2-deploy.sh` is not there, and I nearly reported it
missing -- it lives at `infra/aws/ec2/safe-ec2-deploy.sh`. **A 404 in the wrong directory is the
wrong question asked cleanly.** Caught by re-searching repo-wide with a positive control.

**The through-line: every one of these was caught by a control or a printed denominator, not by
care.** The census's own `0/0` from a bad `parents[]` depth is the cleanest example -- a bare
"0 complete" would have read as a real measurement.

## Compiler Tools (TO-2 + TO-5)

| tool | invocation | result |
|---|---|---|
| `comp-find` | `--name "build_package.py"` | 2 hits / 26,988 scanned -- established "both homes" as a checkable denominator |
| `comp-find` | `"build_package" infra/aws/ec2` + `--name "safe-ec2-deploy*"` | 0 hits / 347 (no EC2 bundling); located the wrapper outside `.tools/`, correcting a clean-but-wrong absence |
| `comp-find` | `--name "*DEPLOYCENSUS*"` | 4 hits -- and surfaced the duplicate T4 dispatch in the same call |
| `stamp_coverage_census.py` (built here) | `--builders --vintage HEAD` / `--builders` / `--deployed` | 0/2 -> 2/2 complete, denominators both sides; deployed plane reported separately |
| `owned-paths-validate.py` | `resolve_lane(...)` w/ positive + negative controls | POD4 9 / ANY 7 / UNRESOLVED 2 / SHARED_OPAL_ETL 1; controls caught the wrong-argument call |
| `proof-of-spec-check.py` | 3 instances, comma-separated id sets | all VALID, true rc=0 (read **without** a pipe -- `\| tail` reports the tail's status) |
| `commit-gate.sh` | all touched `.py` | PASS; one non-ASCII section sign of my own fixed |

## Open at COO

Duplicate T4 dispatch (which TO survives) - my own census's 15/16/19 inconsistency (when to cut the
correction) - E4 `canonical-schwab-si2` taxonomy call - the held broker restart before THU 12:45Z.

## Next

Standing queue: REG w/ REG-0 fixture -> J3 (comp-atomcheck v1, 08-20, load-bearing) -> HELD-STATE ->
W-15 -> T1-DEFROST. CTO's routed comp-pipescript assets-tree universe defect + the H8 conditional
sit in the same queue; COO sequences.
