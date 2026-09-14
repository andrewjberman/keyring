# 2.0.0_SA_COO — /drive Doctrine

Operational steps: `.claude/skills/drive/SKILL.md`. **That file is the imperative; this one is the why.**
Cross-agent learnings: `memory/MEMORY.md` → Driver Discipline.

**Why this doc exists.** On 2026-07-09/10 the COO appended every finding of a long session directly into
`drive/SKILL.md`, taking it from 387 to 949 lines — 521 of them blockquoted incident prose, 678 of them inside a
single step. Andrew, 2026-07-10: *"550 lines is way too much for a skill … all these notes are better suited for a
log."* **A skill is loaded into every COO session; a doctrine doc is read when a rule is questioned.** Putting
history in the skill taxes every future session to save the author one decision about where to file it.

---

## §1 — The imperative, and its limit

**Resolve gates, don't attest them** (Andrew-direct 2026-06-23). Anchor: OPLMCP.02 sat *"gated on ~B-load (outage)"*
for ~5 consecutive cycles while the outage was demonstrably clear and MSTR's respawn contingency sat un-pulled.
The gate was COO-resolvable the whole time.

**But the imperative tells you to ASK whether a gate is real. It does not license you to assume it is not.**

*2026-07-10T05:08Z.* The COO ordered `0.7.0_AE_CloudOps` to run probe `8c0b67afd` immediately, calling it *"a READ
on Opal-owned AWS, pre-authorized"* and warning that *"the window closes on a clock."* **Both premises were false.**
The probe issues four `put_object` calls — one with a deliberately-wrong `IfMatch`, because the `IGNORED` verdict is
only observable by watching a conditional PUT succeed when it must not — and its own docstring reads *"INTROSPECTION
IS NOT EVIDENCE."* Its Lambda limb needs a new scratch function, i.e. the deploy the COO had explicitly excluded in
the same message. And the next derive was **20h49m** away, not imminent.

> **The COO asserted a mechanism from the artifact's NAME.** *"Probe" ⇒ "read."* **That is the same substitution as
> `comp-iam`'s action-for-resource, `comp-freshness`'s filename-for-rows, and `send_message`'s delivered-for-read.**
> CTO reached the same two falsifications independently and ruled: *"your dispatch with the false clock removed."*

**Rule:** before charging a lane with a self-inflicted wait, **name the gate and check it at source.** Offer the lane
an honourable answer (fatigue, context) — and if it refuses one because a hard gate exists, that is a better lane
than the dispatch deserved.

---

## §2 — Sovereign scope, and why the filter must READ

Andrew, 2026-07-09T22:33Z: *"i do not want to deal with 49 right now … not something that we should pursue unless i
explicitly ask for it."* **CANCEL, do not park.**

On 2026-07-10 the COO found **four projects whose entire scope is 49F/Black-Diamond/Schwab still `status: active`**
in `/drive`'s own hot registry, eight days later. Step 2 filtered on `status` and nothing else. There is no
prohibition flag in the schema — the `sovereign` field means **sponsor** (`ADVI_BDAPIMIG: sovereign=Andrew`) — and
`fabric-check`'s `sovereign=0` counts *agent-state* decision requests, not project scope. **Neither instrument saw
it.** The driver built to advance projects would have dispatched on cancelled work while its own health check
printed green.

**Three detectors, three failure directions, one question:**
```
grep -ciE '49f|schwab|black_diamond|rps' per JSON  -> 18 of 39.  Includes NFRA_COSTAWS (one passing mention)
                                                      and every cot project. cot is a SEPARATE FIRM, IN SCOPE.
jq -r '.title'                                     -> "?" for 15 of 18.  A MISSING FIELD. The key is `.name`.
sed 's/^/  drive/SKILL.md: /'                      -> died on the slash, printed nothing.
```
A mention count **over-reports**. An absent field **under-reports**. An instrument error **reads as an absence**.

> **Adjudicate by reading `.name` and `.description`. Print the denominator (39 active).**

**Resolution.** The COO landed a refusal-to-queue (a refusal needs no sovereign permission and touches no 49F
artifact) and escalated the *status flip*, because *"CANCEL" orders a write while "no writes to 49F/bd" forbids one*
— the difference, not the intersection. **Andrew ruled 2026-07-10: *"just exclude those items, we will deal with
them later."*** The four stay `active` in-file, permanently excluded. `MDPF_BASISSWITCH` stays untracked; committing
it would be the write the sovereign declined.

---

## §3 — Freshness and alarms

**The SQS poll (`opal-critical-surface-alerts-coo`) is stripped from Step 2b and stays stripped.** Andrew
unsubscribed seven topics himself on 2026-07-01T02:46:02–02:47:05Z, aws-cli, 63 seconds, `DeleteTopic: 0`. **542
messages, oldest 8.9 days, sit unread. Do not drain them. Do not touch any subscription.**

**The rationale originally recorded for that removal was RETRACTED by its own author (2026-07-09).** It claimed the
alerts were *"uncalibrated noise"* because `comp-freshness` showed cot silver FRESH while the alarm fired. But
`comp-freshness` in partition-key mode parses `YYYY-MM-DD` **out of the object filename** (`:299-317`) and contains
zero row-count reads. It is the *same proxy* as the alarm it was used to discredit, and cannot tell a 0-row stub from
a real partition. `bd-cot-silver-stale-*` sat `OK` on a table dead since 2026-06-18.

> **Freshness grounds on rows or values read out of the artifact — never its name, mtime, size, or existence.**
> **When two freshness instruments disagree, the disagreement is the signal.** Resolve it by finding which one reads
> the property, not by preferring the familiar one.

### A raise is not loudness

*2026-07-10T05:30Z.* The COO specified, and CTO ratified, *"a LOUD raise on `ParamValidationError`, else the CAS
silently degrades to no-stamp."* `0.7.0` found the clause defeated by the caller contract:
```
derive_runner.py:1958-1962   except Exception as e: print(f"WARN: MARKER_STAMP_FAIL err={e}")
incremental_updater:722      except Exception: logger.warning("MARKER_STAMP_FAIL ...")
aws logs describe-metric-filters -> ZERO filters on any MARKER_* token
```
Both callers swallow **every** exception into the string a benign transient emits, and nothing alarms on it.

> **A raiser cannot make itself heard. Only the caller decides whether an exception is an alarm or a shrug.**
> *"Raise loudly" is not a specification; it is a wish about someone else's `except` block.*
>
> **And fail-closed with no alarm is worse than the bug** — a silent outage of the freshness oracle beats the
> clobber it prevents. Precondition: **a metric-filter alarm on `MARKER_CAS_*` must exist before `GLOBGRPH_MARKER_CAS=on`.**

### An absence wearing a reading's costume

`derive_runner.py:743 @ 23c0bb6fb^`: `ts_str = data.get("committed_at", "")`. The marker has only ever carried
`committed_at_iso`. **The staleness alarm read a key that never existed, took its default, and could never fire — a
staleness detector inside FRESHGUARD, blind to staleness on the marker FRESHGUARD exists to watch.**

> **`dict.get(key, default)` on a key that never existed is an absence wearing a reading's costume.**
> **An alarm that has never fired and an alarm that cannot fire are byte-identical in every log we own.**

---

## §4 — Liveness: every detector in Step 2b has been wrong

| Instrument | How it fails |
|---|---|
| telemetry `work-calls` | **blackout windows** — 6 minutes of zero lines of every class, with 6 vendor calls and 4 sends inside |
| `channel push` token | measures the **sender's** `liveness.json`, never the recipient. `pushed=False` is a fact about you |
| `fabric-check --blocks` | read a **decoy directory** for 28 lanes (`inbox/A~B/` flat, while writer+monitor use `inbox/A/~B/`) |
| `ps -ef \| grep` | **matches its own grep**; and MSYS cannot see detached native-Windows processes. `ps -p 1` returns zero rows, so a healthy `ppid=1` wrapper reads as an orphan |
| `u` undelivered = 0 | **an orphan causes it** — `inbox-watch.sh:120` `mv`s the message before `:124` announces it |
| file in `read/` | observes the **watcher**, not the agent. `mv` preserves mtime, so no artifact on disk can date a delivery |

> **`u` and `w` look independent — a filesystem probe and a process probe. They are not. A single orphan sets both
> green.** The more reliably an orphan eats an agent's mail, the more perfectly both limbs hold: **a fully deaf agent
> produces the strongest possible REACHABLE verdict.** This is `ANTI-CORRELATION`, not undiscrimination — it *passes*
> a random-input control.
>
> **The only sound oracle is something only a live consumer can produce: an agent-side ACK. It does not exist.**

**`F-008` — the fabric cannot detect that an agent died.** The spawn audit's vocabulary is `SPAWN · FORCE-SPAWN ·
KILL · KILL-NOOP · FORCE-KILL · WARN · REJECT`. **There is no death event.** A kill is recorded; a spontaneous death
is not. **A spawn count is not a death count**; a respawn is evidence someone *believed* a lane was dead.

**Its mechanism is one missing flag.** `spawn-agent.ps1:218` calls `Start-Process` **without `-PassThru`**, and the
file contains zero `.Id`/pid references. **The fabric never learns the pid of any agent it spawns**, so it can never
ask *is process N alive?* — and every death must be inferred from an absence.

**The orphan reaper closes the loop.** `hook_register_orphan_cleanup.py` is a PostToolUse hook on `register_agent`,
scoped `kill-orphans --serial <S> --force` (Andrew-direct 2026-06-15, replacing a fabric-wide sweep that over-reaped
live watchers). **The cleanup for a dead agent's orphan is gated on that dead agent coming back to life.** DS base
never re-registered; its orphan lived 7h17m.

> **The one lane whose death matters most is the one the fabric is structurally blindest to.** *The death cancels the
> reaping.* **Do not widen the hook** — the narrow scope is Andrew's, and it is the fix for a real over-reap.

**Do NOT run `/watcher rearm`.** `TaskStop` reaps the wrapper, not the grandchild; the repair procedure emits the
orphan it is meant to clear, then arms a second stream to race it. **REAP BEFORE RESPAWN.**

**Do NOT "clean up" `flat_orphans`.** They are the only evidence `operator.py:539` writes lane GOs to a path no
Monitor watches. Folding them into `unread` would pin those lanes DEAF forever and demand a remedy incapable of
fixing the condition — **an alarm decoupled from the action it demands trains the reader to mute it.**

**Never deliver stranded flat-dir mail by moving it.** Four MSTR charters — including a `PROCEED … GO` — have sat 41
days there. **Executing a 41-day-old GO is worse than never delivering it.**

**Still open:** `kill-orphans`' header claims *"every reap is AUDITED (KILL-ORPHAN lines)."* **Zero exist.** Either it
has never reaped or it never writes the line, **and those are byte-identical in the log.**

---

## §4a — The liveness-oracle block, moved whole from the skill (LD-0530, 2026-09-03; same wording)

> ### ⚠ EVERY LIVENESS DETECTOR HERE HAS BEEN WRONG AT LEAST ONCE. **Two signals agreeing convict. One absence convicts nothing.**
> - **Telemetry has BLACKOUT WINDOWS.** `0 work-calls` **only opens an inquiry** — never convicts. Corroborate with a telemetry-independent writer (commits).
> - **`u` (undelivered) and `w` (watcher `ps` count) are BANNED as delivery oracles, jointly and severally.** A single orphaned watcher sets both green — it *drains* the inbox (`u==0`) while its agent is deaf. **A fully deaf agent produces the strongest possible REACHABLE verdict.**
> - **A file in `read/` observes the WATCHER, not the AGENT.** `mv` preserves mtime, so no artifact on disk can date a delivery.
> - **`channel push` measures `liveness.json`, not deafness.** `pushed=False` is a fact about the SENDER. Never report it as a recipient verdict.
> - **`ps -ef | grep …` needs `grep -v grep`** (it matches itself) and **cannot see detached native-Windows processes.** MSYS `ps -p 1` returns zero rows, so a healthy `ppid=1` wrapper reads as an orphan.
> - **The only sound oracle is something only a live consumer can produce: an agent-side ACK.** It does not exist yet.
>
> **Do NOT run `/watcher rearm`** — `TaskStop` does not reap the grandchild, so the repair procedure *generates* the orphan it is meant to clear. **REAP BEFORE RESPAWN.**
> **Do NOT "clean up" `flat_orphans`** — they are the only evidence the dispatch path is broken.
> → `DRIVE.md §4`

## §5 — Verification discipline (the rules that cost the most to learn)

- **Substantive-tick logging (Andrew-direct 2026-08-27 ~22:1xZ at the COO terminal, verbatim: "we
  do not need a committed log with every tick").** The why: on the first paired-drive evening, the
  wire outran the loop on every tick — tick 3's committed log recorded "all rows consumed, 0
  dispatches" as a full findings file, and each such file costs a shared-tree commit slot on a
  worktree where lock contention was already producing rc=128 retries between four seats. The
  log's VALUE is entirely in its deltas (dispatches, consumptions, class changes, findings); a
  no-delta file is commit noise wearing a record's clothing. The guardrails that keep the trim
  from becoming blindness: every substantive log's delta line COVERS the quiet ticks since the
  last one (gapless record, fewer files); a PARKED conviction or [STUCK] escalation still
  requires a logged tick (convictions never rest on unlogged windows); and the paired-mode
  log-derived cursor (@46f4a0563e) tolerates the widened window because over-inclusion errs
  toward ACTIVE — the safe direction — and can never manufacture a PARKED. CTO applied the same
  word to /self-drive's every-2-ticks form the same window.
- **A citation without a vintage is not a citation.** `file:line` resolves at every commit, to different code. Cite `file:line @ <commit-ish>` or `@ working-tree`.
- **Put the control on the RETRIEVAL, not the pattern.** `git show <bad-ref> | grep -c foo` prints `0` — grep counted zero matches *in an error message*. Print the denominator of every scan you reason from.
- **A truncation is not biased toward comfort; it is biased toward whatever is off-screen.** A `head -9` once nearly destroyed a *true* finding three execs had adopted. A negative control cannot catch it — the control runs inside the same truncated window. **Only the denominator can.**
- **The exit code is not a verdict channel.** `rc=1` is any uncaught exception; `rc=2` is also argparse. **Classify by the verdict token on stdout.** *An instrument's failure mode must not be one of its verdicts.*
- **An assertion must carry its observation.** *A negative result that cannot show what it looked at is indistinguishable from a missing observation.*
- **A verification performed against your memory of the artifact cannot fail.** Read the bytes.
- **`HEAD` is not your commit, and a push range is not your commit.** In a shared working tree `HEAD` drifts under you. Verify with `git merge-base --is-ancestor <your-hash> origin/CLOUD`, plus a control that the predicate can say no.
- **`safe-commit` commits the files you NAME, not the files you CHANGED, and returns `rc=0` either way.** Three agents swept the same dirty `CLAUDE.md` into unrelated commits in ninety minutes — one titled *"test subject."* **Verify the pathspec is clean before handing it to the wrapper.**
- **A commit message is an execution vector AND an unverified self-report about the commit carrying it.** Author every non-trivial message via `-F <file>` from a quoted heredoc. **A succeeding substitution leaves no hole** — `date` injects a plausible timestamp — so a census of scars cannot bound a population of injections.
- **When you retract a premise, audit what was built on it — including the things that were right.** `0.7.0` armed the poller that captured the derive transient *because of* a claim that was later retracted. Without that snapshot the leg-4 verdict is `UN-EVALUABLE`, not `FAIL`. **Re-ground the practice on its own merits, in writing, or the retraction takes the detector with it.**
- **A test that patches the wrong seam talks to prod silently.** A function-local `import boto3` defeats a module-attribute patch; the "test" issued real S3 calls and was stopped only by `AccessDenied`. **A test that reaches production is not a test.**
- **A rule that cannot yet be enforced must SAY it is unenforced** (`F-004`), or the next reader cites it as coverage.

---

- **THE LANE-COLLISION FIX (2026-08-29) AND ITS ONE EXCEPTION — the why behind SKILL.md Step 7's
  `{RUNNING_SERIAL}` + refuse-on-ambiguity.** `0397e76d33` (2026-07-10, MINE, a 949->245-line
  compression on Andrew's word) replaced `org/tier1_exec/{COO_SERIAL}/drive_log_...` with the literal
  `2.0.0_SA_COO`. **A working derivation removed while compressing — a semantic change hiding as
  formatting.** Effect: every COO lane wrote `drive_log_<ISO>Z.md` into ONE directory, so
  `ls -t | head -1` returns whichever lane wrote last. **Measured: this seat took its paired-mode
  cursor from `~X`'s log, 83 of 83 commits on that file authored `~X`.** Harm that tick zero —
  nothing was classified PARKED — but the failure direction is rule 5's own (cursor too recent ->
  window narrows -> movement under-reported -> false [STUCK] on a timer). CTO ruling @82648, restated
  @82656 after its evidence was voided, DERIVE confirmed on maintenance cost @82667.
  - ⛔ **THE `%an` TRAP THAT NEARLY SANK THE WHOLE ANALYSIS: `git log --format=%an` IS WHO COMMITTED,
    NOT WHO WROTE.** A census of the directory reported "SEVEN authors, six of them foreign seats."
    **All six were CUSTODIAL commits of base-COO's own untracked files** — `a47d66325f` (salvage
    sweep), `b38f05df50` (whose subject literally reads *"land 18 base-COO-authored artifacts found
    UNTRACKED"*), `d17d45be07` (custodial save). **ZERO foreign writers.** Three seats built on it;
    this seat relayed it to the ruling seat and added a glob check that made it look more measured,
    and it turned a CORRECT per-lane recommendation into a wrong retraction. **A wrong retraction
    spends the credibility of the thing it withdraws.** The discriminator was one field away the
    whole time — the commit SUBJECT, in plain words.
  - ⛔ **THE RESIDUAL, AND IT IS THE EXCEPTION TO WRITE DOWN: (a) AND (b) COVER DISJOINT SETS.**
    Deriving the write path stops the corpus GROWING; it cannot move the six files already sitting in
    the shared directory, which still glob-match. So (b) is the only thing that touches the existing
    corpus — not a belt. **And because `%an` on a custodially-committed file returns the CUSTODIAN,
    (b) refuses SIX OF THIS SEAT'S OWN LOGS.** Correct and costless for those six (5+ weeks old, never
    the `ls -t` winner). ⛔ **But a custodial sweep landing on the CURRENT log — which is exactly how
    all six arrived — makes this seat's own live cursor refuse itself, and the sweeping seat has no
    idea it did that.** Fail-loud, never silent, so the direction is right; **the mitigation is that
    after (a) the PATH carries lane identity for `~X`/`~Z`/`~B`/`~C` and `%an` is not needed for them
    at all. BASE is the sole exposed seat**, because its derived path IS the shared legacy directory.

## §5c — Plane (b) of the live-production probe read a SHARED home (`AMGT_RESAPP-Z-S82`, 2026-09-14)

**The rung said `org/tier1_exec/<BASE serial>/deliverables/` and that is exactly right at what it was
written for** — stopping a seat looking under a lane-suffixed directory that does not exist. ⛔ **It
reads as though the base home ANSWERS FOR the lane. It does not.** That home is shared by the base and
every lane: measured `3.0.0_SA_CVO` 824, `~Z` 246, `~B` 50, `~A` 19, `~C` 16, `~X` 6, `~Y` 1.

    ONE DIRECTORY, ONE BREATH, 08:3xZ
      UNSCOPED, as the rung specified ....... newest 53.2 min    -> MOVING
      SCOPED to ~Z by author ................ 1658.5 min         -> COLD
      POSITIVE CONTROL, base serial ......... 77.7 min  -> responsive, home genuinely active

The artifact that moved was `PRD_REVIEW_LGIC_CANON_v1.0...` @`c2357a9e3b`, author **`3.0.0_SA_CVO`**,
reviewing a **different project**. Author read from git, never inferred from the filename.

⛔ **WHY THIS IS SHARPER THAN THE LANE-BLINDNESS IN `Z-S79`, AND THE ASYMMETRY IS THE WHOLE LESSON:**

    Z-S79  broker limb, lane-blind  -> count TOO BIG -> EXCUSES a quiet seat   -> gets ARGUED WITH
    Z-S82  probe plane, shared home -> reads MOVING  -> SUPPRESSES a nudge     -> SELF-CONCEALING

**A MOVING read is the branch that ENDS the probe**, so the reading that is wrong is precisely the one
nobody follows up. ⭐ **An instrument that fails toward "everything is fine" is not merely wrong, it is
wrong in the one direction that removes the occasion to check it.**

⚠ **THIRD INSTRUMENT IN ONE SESSION WITH ONE SHAPE — a SHARED CONTAINER read as a PER-SERIAL fact:**
the broker's task-order limb, the broker's log limb (both `CLAUDE.md` Rule 22a ROSTER), and this
probe plane. CLAUDE.md Rule 22 already names the class — *a check scoped to the members cannot see a
defect in what the members share* — which is why `1.0.0_SA_CTO~Z` correctly **declined a law edit**
for this one (22574): restating a rule the file already carries is the ratchet the change-policy
forbids. **The actionable defect was the rung's wording, and the rung is this loop's.**

⚠ **DISCLOSED RATHER THAN QUIETLY ADDED TO: `canonical-drive/SKILL.md` was already 106 lines against
its own "under 80" mandate before this edit.** The fix is kept to one clause for that reason, and the
overage is a real debt against the skill, not something this edit created or resolved.

## §6 — Cycle-log discipline

- One log per `/drive` fire: `org/tier1_exec/2.0.0_SA_COO/drive_log_{YYYYMMDDTHHMMZ}.md`.
- **Findings, incidents, and retractions go in the log — never appended to the skill.**
- End-of-session: roll the day's logs into a session summary; **move**, never delete (audit-survivable).

## §7 — Pitfall pointers (memory; do not restate here)

- JSON > REGISTRY at Step 2 read: `feedback_drive_read_json_not_registry.md`
- Verify in-flight by artifact, not SLA: `feedback_track_inflight_to_by_artifact_not_sla.md`
- Read agent ACTIVITY, not project paths: `feedback_drive_read_agent_activity_not_project_paths.md`
- Track by artifact during multi-phase TO execution: `feedback_surface_phase_artifacts_during_execution.md`
