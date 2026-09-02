# AGENT START HERE — Opal Capital

> **BEFORE YOU ADD ANYTHING TO THIS FILE, APPLY THE TEST:**
> ### **Is this directly and explicitly OPERATIONAL for the fabric as it is RIGHT NOW, for EVERY agent, EVERY session?**
>
> **If yes — keep it, however long it needs to be.** A rule is unobeyable without its **mechanism** (an
> orphan watcher *manufactures* a REACHABLE verdict; `.agent_context` is last-writer-wins across all
> agents), and **a bare prohibition loses to an agent's own instruments.** Never cut a mechanism to save space.
>
> **If no — it does not belong here.** Anecdotes, incident histories, dated corrections, empirical anchors,
> retired mechanisms, and anything scoped to one project or one moment go to `org/tier0/ledger/` and the
> linked docs. **The scar is not the rule.** *This doc is read by someone who has done nothing yet: it must
> tell them what to DO.*
>
> **A time-bounded hold does not belong in the doc every agent reads at startup.** If something must reach
> every agent, that is a signal it needs a **GATE**, not a paragraph here.

---

## STOP — READ THESE FIRST

**BANNED: Explore agent** — produces fabricated output. Use comp-* tools and Grep/Read instead.
**BANNED: Task agent** — unreliable. Do the work directly.

---

## Andrew-direct instructions — RECORD + BROADCAST, same turn

**Andrew writes directly to worker agents, not only to Tier 1.** So a lane can be carrying a sovereign
instruction that COO, CTO and MSTR never learn exists — and **`latest + most-restrictive binds`, our
governing conflict rule, cannot bind on an instruction nobody surfaced.**

```
ANY AGENT RECEIVING AN ANDREW-DIRECT INSTRUCTION RECORDS IT DURABLY AND BROADCASTS IT -- SAME TURN.

  DURABLE   a commit (memory entry / ledger / org record), quoting him VERBATIM, with channel + time.
            NEVER A PARAPHRASE. THE PHRASING *IS* THE RULING.
  BROADCAST MCP to COO + CTO + MSTR, so `latest + most-restrictive` has something to bind on.
  SCOPE     The receiving agent does NOT adjudicate scope. SURFACE, DO NOT ADJUDICATE.
```

**An agent relaying "Andrew ruled" is not suspect merely because you did not see it — that is the normal
case.** Do not challenge the provenance of a relayed sovereign ruling from your own vantage point.

**The RELAYER half (2026-08-06) — if the receiver may not challenge provenance, the grounding obligation
sits ENTIRELY on the relayer.** A relay is not a lower-evidence act than an assertion; it is the same act
with a longer fuse, because the receiving seat reasonably treats a routed finding as grounded.
**WHEN YOU FORWARD A FINDING, FORWARD ITS GROUNDING OR FORWARD IT AS UNGROUNDED** — carry the evidence
pointer (`file:line @ commit` / tool + output / live primitive) or carry the caveat, one word ("unratified",
"inferred"). A record is not the plane: a relay of a ruling document inherits that document's staleness
silently — measured 2026-08-06, three senior seats in one day; in the sharpest case a live cron cited from
its own governing clock ruling was 10 minutes wrong about the very member the ruling was written to pin.

---

## RAVC Protocol (Non-Negotiable)

Every inter-agent request follows **Request → Acknowledge → Validate → Close**. Full spec:
`org/ref/RAVC_PROTOCOL.md`.

- Asked to do something by a registered agent: **acknowledge immediately**, do it, report back **with
  evidence** (commit hash, artifact path, tool output).
- You asked someone for something: **validate their evidence before closing.** REWORK requests must tie
  the gap back to the original expected evidence.
- **Silent receipt and silent completion are both violations.**
- **Scoped work still needs a SURPRISE CHANNEL.** When a mandate says *do this and not that*, you will
  still see things outside it. **Report one line to the coordinator, take NO action, keep working** —
  never suppress, never chase. **A "do not chase" instruction without a named channel makes seats
  suppress, because suppression looks like compliance.** Task-order authors: name the channel.
  `docs/doctrine/THE_SURPRISE_CHANNEL.md` (Andrew-named 2026-08-06). **FORMALIZED 2026-08-21
  (Andrew-ratified): `3.0.0_SA_CVO` MANS THE CHANNEL, and every new project runs the canonical
  pipeline — register → PRD → COO decomp-before-TOs → execute ON SPEC (frozen mid-round) →
  investigation/remediation rounds. Only BLOCKING/HAZARD classes interrupt; OBSERVATION never
  does. Protocol: `org/ref/DIRECTIVE_EXECUTION_PIPELINE.md` (CLAUDE.md Rule 27).**
- CTO and COO drive every loop to close; escalate to Andrew only on the five triggers in the spec.
- **Issuing a STOP/halt:** prefix the message subject with `[STOP]` (or `[HALT]`) as the **first
  characters**. The HALTGT deploy checkpoint classifies on it. **A routine message must never begin with
  either token** — they hard-block deploys. For non-blocking urgency use `URGENT` / `ESCALATION`.

---

## Authority hierarchy

> **Andrew (sovereign) › MSTR / Tier 0 › CTO · COO / Tier 1 › Tier 2 (DE/DT/DS/AE) › Tier 3 (RD)**

- **MSTR** (`0.0.0_AB_MSTR`) is the autonomous principal-proxy: it originates strategy and charters and
  directs the fabric through Tier 1. A Tier-0 directive outranks Tier-1 planning.
- **Tier 1 may push back on a Tier-0 charter on operational grounds.** MSTR sets *what* and *why*; Tier 1
  informs *whether* and *how*. That is the org working, not insubordination.
- **Andrew remains sovereign.** A real-Andrew instruction overrides any MSTR directive.
- **CVO independence:** when the CVO (`3.0.0_SA_CVO`) exercises ratification or review authority it is
  **constitutionally independent** — MSTR does **not** outrank a CVO ratification verdict.
- **Never stop at a fork.** A fork you cannot resolve is **escalated** — never halted on, never
  sat-silent-on.
- **Escalation chain:** worker → CTO/COO → MSTR (terminal resolver) → Andrew. Runs **upward only, never
  sideways.** Andrew gets only the forks MSTR explicitly defers to sovereign judgment.

---

## Step 1 — Identify yourself

**Your serial resolves ONLY from session-scoped evidence, in this precedence:**
1. **Andrew's word**
2. `org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial` (the session id survives compaction)
3. **Your own armed Monitor** — a session watching serial X's inbox **is** serial X
4. Your own pre-compaction registrations

> **`.comp-graph/.agent_context` is NOT an identity source.** It is a shared file that whichever agent ran
> last rewrote. It answers *"what TO context"*, never *"who am I"*. **No gate, audit line, or attribution
> may resolve an actor from it.** The sound sources are `$OPAL_AGENT_SERIAL` (per-process) and the session
> serial file above.

**Cross-check before acting.** If `org/mcp/liveness.json` shows your claimed serial LIVE at a **different
PID** (fresh heartbeat), or a **different serial at your PID** — **STOP, you have an identity conflict.**
Resolve it before registering.

**Inverse-first rule:** before reporting a "duplicate stream under my serial", **check whether YOU are the
phantom** (`liveness.json` + `org/mcp/agent-spawn-audit.log` say who holds the serial).

Then read your agent folder:
```
org/{tier_folder}/{your_serial}/README.md    — your ID, role, responsibilities
org/{tier_folder}/{your_serial}/prompt.md    — your scoped persona (read in Step 3)
```
Tier folders: `tier1_exec/` (SA) | `tier2_senior/` (DE, DT, DS, AE) | `tier3_junior/` (RD)

---

## Step 1a — Your BASE is the workspace root; `portal/` is a work-site, never a base

Your cwd is `C:\Users\AndrewBerman\Desktop\ajb_workspace`. Every agent's files — logs, task orders,
deliverables, identity — live under `org/` there.

You may **WORK** in the portal repo, but you are never **BASED** there: address it explicitly
(`git -C portal ...`, or a scoped `cd portal && <work> && cd -`) and return to the workspace root when the
task ends.

**A CWD that lingers in `portal/` is itself a defect.** Portal is its own git repo: a lingering portal CWD
breaks workspace tooling (`safe-commit.sh`, `.tools/*`) at best, and at worst **silently substitutes the
WRONG repo's git history into evidence pulls** — a bare `git log` inside `portal/` reports portal commits
only, **with no error.**

---

## Step 1b — MCP startup (MANDATORY, every session)

### Codex runtime branch (use this instead of the Claude watcher/poller path)

Codex sessions must read and follow `org/mcp/CODEX_INBOX_MONITOR.md`. The
canonical parts are deliberately separate:

| Role | Codex component | Launch rule |
|---|---|---|
| Registration + broker heartbeat | `org/mcp/codex-agent-heartbeat.py` | Start once with the full suffixed serial; keep it running. It imports `server.py`, registers, cancels the consuming broker poll task, and heartbeats separately. |
| Non-consuming inbox detector | `org/mcp/codex-inbox-monitor.py` | Start once inside the documented persistent `functions.exec` bridge. It emits only `[HARD-NUDGE] <filename>` and repeats while the exact root-level `.md` remains unread. |
| Codex notification bridge | The `notify()` + `yield_control()` bridge in `org/mcp/CODEX_INBOX_MONITOR.md` | Hand-draw in the Codex tool cell; it is host orchestration, not an OS script. |
| Broker implementation dependency | `org/mcp/server.py` -> `org/mcp/broker.py` | Used by the heartbeat companion. Do not launch a second broker manually. |

**Codex must NOT run** `inbox-watch.sh ... stream`, `check-inbox.sh`, or
`agent-poller.py` alongside this path. The first two consume/move inbox files;
the generic poller belongs to the Claude MCP-server lifecycle and documents the
consuming watcher as its delivery companion.

The detector sees existing backlog on its first scan and repeats every 15
seconds until handling completes. At the start of every active Codex turn,
also sweep the full suffixed serial's canonical unread root before other work.
For a Base message: read the exact file -> ACK and begin immediately -> act ->
move that exact file to `read/`. Never infer READ from a nudge or a moved file.

**Host boundary:** Codex `notify()` can surface an event at an active tool
boundary, but the currently exposed Codex host cannot start a new reasoning
turn after a final response. Repeated non-consuming nudges prevent loss; exact
dormant-turn parity with Claude's harness-native Monitor requires a Codex host
wake/resume callback.

The A/B/C commands below are the Claude runtime branch unless a paragraph says
otherwise; their identity, inbox-path, task-order, and ACK semantics still bind
Codex.

**A. Register — use your FULL serial, including any `~lane` suffix:**
```python
register_agent("{your_serial}", summary="Starting session")
```
Makes you visible, starts the broker, enables message push, reaps your own orphaned watchers.

> **Lane agents register as `0.4.0_DS_ClientPlatform~C`, NOT the base serial.** Registering under the base
> means your `~C` inbox is never watched — you will silently miss every GO addressed to your lane.

**A.1 — Write your session-keyed serial file:**
```bash
mkdir -p org/mcp/sessions
if [ -n "${CLAUDE_CODE_SESSION_ID:-}" ]; then
    echo "{your_full_suffixed_serial}" > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"
fi
```

**A.2 — Audit-archive durability + tamper-evidence (audit-archive-invoker, CTO-gated 2026-07-19):**
Runs after A.1 (it reads the serial file to resolve the exec-permitted author). An EXEC session mints a
committed snapshot when the archive is due (>=12h since the newest snapshot + a covered log grew); a NON-EXEC
session defers the commit but STILL runs the append-only + liveness detection (findings to FINDINGS.md +
stdout). Never blocks startup. Owner `0.7.0_AE_CloudOps`, gate `1.0.0_SA_CTO`; design/why in
`docs/briefs/audit-archive-invoker-spec-20260716.md` + the gate-2 deliverable.
```bash
python .tools/audit-archive-invoker.py || true   # append-only verify + archive-when-due; never blocks startup
```

⛔ **ON SITE Z, EXPECT 12-18 TAMPER-VOCABULARY FINDINGS HERE AND DO NOT CHASE THEM. READ THIS
BEFORE YOU RUN IT, NOT AFTER.** Three separate seats independently spent a message reaching "surface
it, do not chase it" — the explanation was real but its only carrier was a broker message id, which
a fresh seat has no reason to open.

>> **MECHANISM, MEASURED 2026-08-27 at source by `0.0.0_AB_MSTR~Z` (not relayed):**
   `audit-archive-invoker.py chain_root()` returns `archive/<device>/` **only if that directory
   exists**; otherwise it falls back to the legacy flat root, and its own docstring says that root
   **IS THE LAPTOP CHAIN**. `org/audit/archive/` currently holds FLAT timestamp dirs with no
   `<device>/` level, so **a site-Z seat compares its device-local live logs against the LAPTOP's
   baseline** — two different files sharing a path. The tool renders that difference in tamper
   vocabulary because tamper vocabulary is the only vocabulary it has. <<

**THE DISCRIMINATOR IS DIRECTION, NOT MAGNITUDE** (`0.4.0_DS_ClientPlatform~L`, 2026-08-27, correcting
their own first figure before it propagated):
```
DEVICE-AXIS  every covered log SHRINKS, each by its own local activity -> a WIDE SPREAD is expected.
             MEASURED: 8 of 8 shrank, 0 grew; 1.46x - 23.81x, median 5.96x, only 2 of 8 reach 10x.
TAMPER       selective truncation of the interesting ones -> a MIXED direction set, some UNCHANGED.
             0 of 8 unchanged is the observation that argues against it.
```
⛔⛔ **THE DISCRIMINATOR COVERS ONE CLASS OF FINDING, NOT THE OUTPUT.** The invoker emits at
least TWO classes and **they INTERLEAVE in the output** — a reader meets them mixed, not in blocks:
```
NON-APPEND-EDIT   (a log SHRANK vs baseline)   <- the direction test below covers EXACTLY this
ERROR-FAILCLOSED  (a covered log is ABSENT)    <- ⛔ NOT COVERED. "did any log GROW or stay
                                                  UNCHANGED?" says NOTHING about a file that is
                                                  not there.
```
**MEASURED at two seats, RECONCILED by `0.4.0_DE_ClientPlatform~Y` by set-compare** — and the
reconciliation is the part a reader needs, because the raw line count invites a frame error:
```
tool header  18 finding(s)  =  5 COVERAGE  +  13 INTEGRITY
                                  |              |-- 8 NON-APPEND-EDIT  (the shrink class)
                                  |              |-- 5 ERROR-FAILCLOSED (absence)
                                  \--------------/  THE SAME FIVE FILES, EACH PRINTING TWICE
```
⛔ **SO IT IS FIVE ABSENT FILES PRODUCING TEN LINES, NOT TEN FILES.** `3.0.0_SA_CVO~Z` scoped to
INTEGRITY and read 13; `0.4.0_DE_ClientPlatform~Y` counted printed lines and read the tool's own 18.
**Neither was wrong — two denominators over one world**, and both independently measured **8**
NON-APPEND-EDIT, which is the only number the discriminator turns on. **A count without its unit is a
frame error waiting for a reader: say FILES or say LINES.** ⛔ **So do NOT read a clean direction
verdict as clearing the run** — it clears the shrink half and is silent on the rest. **Read the
ABSENT rows yourself; this note does not adjudicate them.**

⛔ **FOR THE SHRINK CLASS ONLY: ASK "did any log GROW or stay UNCHANGED?", never "did they shrink by a similar amount."**
A 16x spread is what the benign reading PREDICTS; uniform magnitude would be the surprise. **The
magnitudes are not written here on purpose** — a number in a durable carrier is wrong by next week,
and the direction is the invariant.

**THIS IS NOT A DEFECT AND NEEDS NO FIX** — `chain_root()` is transition-safe BY DESIGN so the code
change and the 238-file migration could land in either order. The code landed; the migration has not.
⭐ **THIS IS A NAMED MIGRATION IN FLIGHT, NOT AN ARTIFACT, AND IT HAS A TERMINUS** (`1.0.0_SA_CTO~Z`):
`rv0057-f001` moves 238 files to `archive/<DEVICE>/<TS>/`. **RESOLUTION CONDITION, so this note
retires itself:** when that migration lands the fallback stops firing and these findings clear.
**If they persist after it lands, the device-axis explanation no longer covers them and it IS a
finding.** Owner `0.7.0_AE_CloudOps`, gate `1.0.0_SA_CTO`; carrier gap surfaced by `3.0.0_SA_CVO~Z`.

⛔⛔ **DO NOT `mkdir org/audit/archive/<device>/`. THE MECHANISM ABOVE READS AS AN INVITATION
TO AND IT IS A TRAP** (caught by `1.0.0_SA_CTO~Z` on this note's own wording). One `mkdir` drops the
findings to zero — **by making the tool believe we are POST-migration while all 238 files are still
in the flat root, so it would compare live logs against an EMPTY CHAIN.** The docstring's
"a half-finished migration cannot strand the instrument" guarantee covers **files-moved-before-code**;
creating the directory without moving the files is the half-finished state in the OTHER direction and
**is not covered**. ⛔ **UNTESTED AND NOT TO BE TESTED ON A LIVE AUDIT CHAIN.** The noise is cleared by
LANDING THE MIGRATION, never by satisfying the predicate.

⛔ **AND THE COST OF THIS NOTE, STATED SO IT STAYS VISIBLE** (`1.0.0_SA_CTO~Z`): telling every seat
to EXPECT tamper-vocabulary findings removes wasted messages **and simultaneously NORMALISES IGNORING
A TAMPER DETECTOR.** Both effects are real. **It is the right trade ONLY BECAUSE the migration has a
terminus** — **if `rv0057-f001` stalls, this note quietly becomes standing permission to ignore a
tamper detector. Re-read this paragraph if it is still here and the migration has not landed.**

⭐ **TWO MORE FINDINGS THIS NOTE DID NOT COVER, NOW OWNED (2026-08-28, `1.0.0_SA_CTO`, after three seats
re-filed them in one day):** `[LIVENESS/STALE-BASELINE]` (baseline 2026-08-20T042433Z ageing past 24h with
an uncaptured tail) and `[COVERAGE/UNCOVERED-AUDIT-LOG] org/to-pos-override-audit.log` are NOT the
device-axis tamper-vocabulary class above — they are a stale baseline + one uncovered file, and both
are **OWNED-UNTIL-rv0057-f001**: the exec A.2 ALSO defers (`snapshot=deferred: DEVICE-CHAIN-PENDING`,
measured at three seats), so no seat archives on this device until that migration lands; the MANIFEST
add rides the same sitting (owner `0.7.0_AE_CloudOps` base, gate `1.0.0_SA_CTO`; COO carrier
`D2_CUT_TIME_OBLIGATIONS_20260827.md` row 3 items d+e; re-raise trigger 2026-08-30). **If you see these
two at A.2, they are known: do not re-file them; surface only a THIRD finding or a shrink/absence row.**

⚠ **REACH IS BOUNDED BY WHO ACTUALLY RUNS A.2, WHICH IS NOT EVERYONE** — the first broadcast of this
note claimed "every seat meets A.2 at load" and **that claim was false**: `0.4.0_DS_ClientPlatform~W`
reported running A.1 and A.3 and skipping A.2 entirely (measured, n=1, self-reported). **A note beside
a step reaches only the seats that run the step.** A.2's MANDATE and A.2's EXECUTION RATE are
different quantities. No gate is proposed for this.

**A.3 — PATH check (added 2026-07-25, NFRA_TOOLARCH.PATHFIX; CORRECTED 2026-07-25 — see below):** harness
shells are non-interactive and source NO profile, so `.tools/` is reachable only via the `~/bin` forwarders
(`b519fb1c2e`). **Print the DENOMINATOR — never a boolean:**
```bash
F=0; T=0; for t in .tools/comp-*; do t=$(basename "$t"); T=$((T+1)); command -v "$t" >/dev/null 2>&1 && F=$((F+1)); done
echo "PATH: $F of $T comp-tools resolve bare." ; [ "$F" -lt "$T" ] && echo "  -> the REST need an explicit .tools/<tool> prefix. 'bash .tools/provision-path-shims.sh' provisions a NAMED SUBSET (read its header for the current list) -- it is not, and does not claim to be, all $T."
# MANDATORY SECOND HALF: RESOLUTION IS NOT EXECUTION. Actually RUN one, and score it on OUTPUT,
# not on rc -- the rc does NOT discriminate match-vs-no-match (a real question and a no-match
# question BOTH exit 0; only `comp-which --help` exits 1).
comp-which "how do I grep the repo" 2>&1 | grep -q "comp-which --" && echo "EXERCISE: a forwarder RAN (produced its own banner)." || echo "EXERCISE: *** RESOLVED BUT DEAD *** -- the forwarder exists and its TARGET does not. Run: bash .tools/provision-path-shims.sh"
```
> ⚠ **The remedy line above once named the subset literally ("aws + comp-which + comp-system"). It went
> stale the same day** — `~D` added `comp-grep`/`comp-glob` to close Rule 21's dead fallback, and the line
> kept saying three. **A hand-copied list inside the fix for a hand-copied-list defect**; it now points at
> the provisioner's own header instead of restating it. *The count is deliberately `$T`-derived, never a
> digit.*
> ⚠ **THE OLD ONE-LINE PROBE WAS ANTI-CORRELATED WITH THE FAILURE IT SCREENED FOR, and it passed while the
> rail was broken.** It tested `command -v comp-which` — **the member MOST likely to be provisioned**, because
> the provisioner forwards a small named subset and `comp-which` is in it. **A probe aimed at the privileged
> member cannot fail in the state it exists to detect.**
>
> ⚠ **SECOND, WORSE INSTANCE — 2026-07-29, and it is why the EXERCISE line above is mandatory.**
> `0.0.0_AB_MSTR~Z` rebooted. **A.3 reported `PATH: 93 of 93 comp-tools resolve bare`. ZERO of them
> ran.** `command -v` tests that the **forwarder FILE EXISTS** in `~/bin`; it never executes it, so it
> **structurally cannot see that the forwarder's TARGET is gone.** All 186 forwarders had been
> generated while LD-0340's `mount -f C: /c` was live, so every one pointed at `/c/...`; the reboot
> took the mount and killed all of them at once.
>
> **THE PROBE READ 100% HEALTHY PRECISELY BECAUSE THE BREAKAGE WAS TOTAL AND SINGLE-CAUSED** — all 93
> exist *because* the provisioner ran, and all 93 are dead *because* they share one prefix. Same
> anti-correlation as the orphan watcher: **the cleaner the pass, the more complete the failure.**
> Downstream, `safe-commit`'s surface-check and risk-reflex hooks printed `No such file or directory`
> and **let the commit through** — a live gate failing OPEN and SILENT.
>
> **GENERAL FORM, worth carrying past this probe: A NON-DURABLE FIX THAT GENERATES DURABLE ARTIFACTS
> PROPAGATES ITS OWN EXPIRY INTO THEM.** `mount -f` was correctly labelled *"dies at reboot."* Nobody
> labelled the 186 forwarders it had silently made conditional on itself.
>
> **EXERCISE THE TOOL; DO NOT RESOLVE ITS NAME.** Found by `~Z` 2026-07-29, approved by Andrew-direct.
>
> **RECORD OF THEN — 2026-07-25 morning, NOT a current claim.** *At that moment `~/bin` forwarded 3 tools and
> exactly 2 of 91 `.tools/comp-*` resolved bare; the probe returned a clean pass at that coverage, one call
> before `comp-grep` returned `command not found`.* **Those digits are frozen ON PURPOSE and WILL be wrong —
> ~D provisioned `comp-grep`/`comp-glob` hours later and the ratio moved the same day. For the CURRENT state,
> RUN THE PROBE ABOVE; it derives both numbers.** *(This block has now gone stale twice within one day — first
> its hand-listed tool set, then its counts. Both times the mechanised half was fine and the prose decayed.
> Dating it is the fix; chasing the digits is not.)*
>
> **And the failure landed on Rule 21's rail:** `comp-which` resolved, so the reflex worked — then it *routed
> to* `comp-grep`/`comp-glob`, **which did not resolve** (since provisioned). The rail failed open at its own
> designated fallback, having just told you it was healthy.
>
> **~D's `provision-path-shims.sh` never overclaimed** — its header scopes itself to the three named tools.
> **The CHECK inherited a generalization the FIX never made**, and that check was this file's text, i.e.
> mine. Surfaced by `0.8.0_AE_CloudComp~C`, independently re-measured before landing.

Why this matters: a bare `aws` without the shim is UNPROTECTED against the MSYS leading-`/` silent-mangle
class, and `command not found` on comp-tools is the comp-rail failing open. Mechanism + fix record:
~D's NFRA_TOOLARCH.PATHFIX delivery (2026-07-25).

**B.0 — YOUR DELIVERY LEDGER, BEFORE YOU RESUME ANYTHING (LD-0480, 2026-08-30):**
```python
get_delivery_state(agent_serial="{your_FULL_suffixed_serial}", since="<when this serial's PREVIOUS session was last alive; after a reboot, the reboot time>")
```
Every row addressed to you that is **not READ — or is READ `by` a serial that is not yours** — is UNREAD MAIL:
open the file in your own `read/` dir, act on it, ack it FROM ITS `Msg-ID` LINE. A message OFFERED to a session
that died reads `OFFER-EXHAUSTED` and is invisible to `check-inbox`, `get_agent_status` and the `read/` listing;
"resume from your last log" cannot surface an obligation that arrived AFTER that log. Measured 2026-08-30 after
the 22:57Z reboot: eight rows at one lane, one a `[DRIVE]` contract ruling closed against the wrong shape (84859/84902);
four FOREIGN READ stamps hiding the same class at another (84900); the coverage line counts a stolen slot as covered
(84892). Cost: one call, ~1 s. Non-application: a context-clear is the SAME session — you find only your own READ rows.
⛔ Never ack a row you did not open: a batched ack asserts reading that did not happen.
CODEX SEATS: no `ack_messages`/`get_delivery_state` surface exists on the canonical Codex path (3.0.0_SA_CVO~X, 03:17Z: 48 rows, none ackable); the exact-file backlog sweep at load IS the equivalent act, the rows stay un-stamped honestly, and a checked-in Codex ACK helper is `1.0.0_SA_CTO`'s org/mcp item, not a seat's improvisation.

**B. Check inbox — BOTH paths, both required:**
```bash
check-inbox {your_serial}           # filesystem: base -> inbox/{base}/ ; lane -> inbox/{base}/~{lane}/
                                    # NEVER inbox/{base}~{lane}/ (flat) -- nothing reads it. See "Inbox path" below.
```
```python
get_agent_status("{your_serial}")   # broker channel
```
`send_message` writes to **both**, but each probe reads only one. **`check-inbox` alone is insufficient.**

**B.1 — Find the work you actually hold. RUN THIS; do NOT read your folder:**
```bash
python .tools/to-check.py --all --assignee {your_FULL_suffixed_serial}
```
**`--all` IS LOAD-BEARING — never trim it.** The default view scopes to projects whose PRD is <=14d old,
so **a TO whose project PRD has aged out DISAPPEARS WHILE STILL OPEN — the view goes blind to exactly
the TOs that have been stalled LONGEST.** Trimming `--all` silently restores that blindness.
**MEASURED 2026-08-04: 237 of 272 live TOs — 87% — are invisible in the default view; 60 of them are
`pending`.** The default shows 35 of 272. This is the estate-wide condition, not a quirk of one seat.

Two reading notes so the output does not mislead you: `--assignee` is a **substring** match (`:12`
"partial match ok"), and the rollup groups by **PRIMARY** assignee — so a JOINT TO appears under the
other seat's heading while still being yours. Read the rows, not just the headings.

⛔⛔ **MEASURED-BROKEN 2026-08-25 09:3xZ -- `--assignee` RETURNS ZERO FOR EVERY TILDE LANE, AND THE COMMAND
ABOVE MANDATES THE SUFFIXED FORM. IF YOU ARE A `~lane` SEAT, THIS READ WILL TELL YOU YOU HOLD NOTHING.**
```
SOME lanes return 0        |  OTHER lanes return real counts    |  bases
~G  0   ~H  0   ~C  0      |  ~A 10   ~B 9   CRO~C 1            |  DS 90  AE 105  CTO 14
```
⛔ **A ZERO HERE IS NOT PROOF YOU HOLD NOTHING, AND A NON-ZERO IS NOT PROOF YOU HOLD EVERYTHING YOU HOLD.**
Positive control: `~C`'s own TO text contains `0.4.0_DE_ClientPlatform~C` **4 times verbatim** and that exact
query returns `total=0` over `scanned=2101`. *(The substring note above therefore describes behaviour this
command does not have: it explains why you might see TOO MUCH; the measured failure is that you see NOTHING.)*

⛔ **AUTHOR'S CORRECTION -- MY FIRST VERSION OF THIS WARNING SAID "EVERY LANE SERIAL -> 0, EVERY BASE SERIAL
-> A REAL COUNT". THAT IS FALSE** (`0.4.0_DS_ClientPlatform~G` 70076): `~A`=10, `~B`=9, `CRO~C`=1 all return
non-zero. **I SAMPLED THREE LANES THAT HAPPEN TO SHARE A PROPERTY AND GENERALISED TO EVERY LANE -- a sample
of three read as the population.** The tilde was never the variable.
⛔⛔⛔ **MECHANISM CORRECTED AT SOURCE 09:4xZ (`0.7.0_AE_CloudOps~G` 70008) -- THE TILDE IS EXONERATED. IT IS
NOT A CAUSE AT ALL, AND MY MATRIX ABOVE WAS A CONFOUND.** `.tools/to-check.py:98` --
`SERIAL_RE = r"\d\.\d\.\d_[A-Za-z]+_[A-Za-z0-9]+(?:~[A-Z])?"` -- **EXPLICITLY CAPTURES THE LANE SUFFIX.**
Run against a failing TO field it finds BOTH serials **with tildes intact**, and `_assignees_from_field` then
**DISCARDS them as UNCLASSIFIED** (`assignee_serials = []`); the filter at `:639` compares against that empty
list. **Nothing about the tilde is involved.**

**THE CONTROLLED EXPERIMENT, ONE VARIABLE CHANGED:**
| `<issued_to>` shape | tilde | result |
|---|---|---|
| `**SEATED: \`serial\`**` prose | `~G` | **[] -- fails** |
| `**SEATED: \`serial\`**` prose | base | **[] -- STILL FAILS with the tilde REMOVED** |
| clean `<serial>` | `~G` | **MATCHED -- works WITH the tilde present** |
| `-> <serial>` arrow target | `~G` | **MATCHED** |
> **THE DISCRIMINATOR IS THE `**SEATED: \`serial\`**` PROSE NOTATION. A TILDE LANE IN CLEAN NOTATION MATCHES
> PERFECTLY.** The tilde/base split in my matrix is a **CONFOUND**: the TOs that seat tilde lanes are the
> recent ADVI_PERFRP-era ones written in SEATED prose, and the base counts come from older TOs in clean
> notation. **TWO VARIABLES MOVED TOGETHER AND THE VISIBLE ONE GOT THE BLAME.**

⛔ **THEREFORE A FIX TO TILDE MATCHING WOULD CHANGE NOTHING AND WOULD READ AS SUCCESSFUL** -- lane seats
would still see zero and the fix would be reported as landed. **THE CORRECT FIX IS TO WIDEN THE RECOGNISED
ASSIGNMENT NOTATION SET to include `SEATED: <serial>`.**

*Author's note, kept because it is the transferable half: I ran a six-row matrix, saw a perfect split, and
named the visible variable **without reading the source**. Rule 22 -- a causal claim is a HYPOTHESIS until
source-confirmed -- and **a perfect correlation across a controlled-LOOKING matrix is exactly what a confound
looks like.** The PATTERN below stands (lane seats do see zero) and the operational guidance is unaffected;
only my CAUSE was wrong, twice.*

⛔⛔ **AND THE SECOND HALF STANDS ON ITS OWN EVIDENCE -- `0.4.0_DE_ClientPlatform~D` 69987 MEASURED THAT MY
FIRST REMEDY HERE ("RUN THE BASE SERIAL") DOES NOT WORK:**
```
--assignee '0.4.0_DE_ClientPlatform~D'  total=0
--assignee '0.4.0_DE_ClientPlatform'    total=10, projects=7
POSITIVE CONTROL: `ADVI_PERFRP` occurs ZERO times in BOTH outputs.
```
**THEIR LIVE TO -- executing all session, naming their full serial TWICE in its own file -- APPEARS UNDER
NEITHER QUERY.** The second cause is the **`<issued_to>` NOTATION**:
| indexed | `<issued_to>0.4.0_DE_ClientPlatform</issued_to>` -- a BARE SERIAL and nothing else |
|---|---|
| **invisible** | `<issued_to>DE-class (portal...). **SEATED: ``0.4.0_DE_ClientPlatform~D``** ... watches ``0.4.0_DS_ClientPla...`` ` -- **leads with a CLASS, serial in backticks behind a label, and names a SECOND serial it merely WATCHES** |
⛔ **SO "TILDE -> 0, BASE -> A REAL COUNT" IS TRUE OF THE SERIAL AND FALSE OF THE TO. BASE-SERIAL RECOVERY
RECOVERS SOME TOs AND NOT OTHERS, AND NOTHING IN THE OUTPUT SAYS WHICH.**

> **THEREFORE, UNTIL THIS IS FIXED: YOUR TO IS THE FILE NAMED IN YOUR DISPATCH MESSAGE. THAT IS THE ONLY
> READ THAT HAS NOT FAILED.** Run the base serial AND read your own folder as CROSS-CHECKS -- **but treat a
> zero or an absence from EITHER as telling you nothing**, and the caution below still holds (a lane's TOs
> may live in the BASE folder).

⛔ **AND DO NOT "FIX" THIS BY WIDENING THE PARSER TO PULL SERIALS OUT OF THAT PROSE** (DE~D's warning, and it
is the load-bearing half): **their field contains TWO serials and the second is a WATCH TARGET, not an
assignee. A naive widening would assign their TO to the DS lane.** **THE CURRENT ZERO IS AT LEAST HONEST; A
NAIVE WIDENING IS WORSE THAN THE ZERO.**
**AND THE TOOL ALREADY SAYS SO ON ITS OWN FACE** -- every run prints `unresolved_serials=N` with the note
*"a real assignee written in an unusual notation lands here -- UNCLASSIFIED, not counted as non-assignments...
do not read this residue as zero."* **The instrument has been disclosing this limit in every output, and we
read past it.**
⛔ **AND KNOW WHAT THIS COLLIDES WITH: a `~lane` seat that runs the mandated check, reads `total=0` and
concludes it is idle is COMPLYING WITH THIS PROTOCOL WHILE VIOLATING THE DRIVE IMPERATIVE** (*"NEVER
self-wind-down... passive idling = a coast-failure"*). **Neither failure is visible to that seat.**
*Found by `0.4.0_DE_ClientPlatform~C`, isolated by `1.0.0_SA_CTO`, severity named by `3.0.0_SA_CVO`. Tool fix
routed, not taken. This warning is ADDITIVE -- no line above it was altered -- and `0.0.0_AB_MSTR` may revert
or rewrite it as the protocol's owner.*

⛔ **Two reads that will tell you you are IDLE while you hold a live P0:**
- **YOUR AGENT FOLDER.** A lane's TOs frequently live in the **BASE** folder — `issued_to` is the only
  truth, never file location. A lane agent reading `{agent_folder}/task_orders/` sees an empty-or-stale
  set. *(Step 1's "read your agent folder" is for IDENTITY, not for work.)*
- **`get_agent_status`'s pending-TO list.** It is FOLDER-keyed (`org/mcp/server.py:809-812`), so a lane
  query returns the whole base folder's work — one measured case returned **12 TOs spanning 5 assignees
  when the lane held 3**. A list that is mostly other seats' work trains you to skim it. Use it for
  liveness and messages; **it is not the authority on what you hold.**

*Why this line exists: a CTO-gated closure row on an Andrew-direct P0 sat `pending` for TEN DAYS in
plain sight of a WORKING instrument nobody was pointed at (CI-R7R8, 2026-07-24 -> 08-03). The tool was
already correct; the guidance pointed at the folder. Measured + falsified by `0.7.0_AE_CloudOps~B`,
2026-08-04.*

**C. Arm the persistent inbox Monitor — run `/watcher` (once, at load).**

It arms a persistent Monitor running `inbox-watch.sh {serial} stream`; each `[INBOX] <file>` line becomes a
chat notification. **Arm once — it never exits and you never relaunch it.** If arming by hand, use the
**Monitor tool** with `persistent: true`, `timeout_ms: 3600000`, and the **absolute** script path.

> **RESOLVE THE DRIVE PREFIX — never hardcode either form.** BOTH prefixes may be mounted at once (measured
> 2026-08-06, CRO: `/c` and `/cygdrive/c` same device, same inode — the old "one or the other, never both"
> mechanism sentence here was FALSE), but they are NOT equally durable: `/c` is a non-`auto` user mount that
> has vanished at reboot before (LD-0340 class — 2026-07-29 it died and took all 186 `~/bin` forwarders that
> had baked `/c/` into themselves, while A.3 read healthy). `/cygdrive/c` is the system-provided `auto,noumount`
> mount. So: `test -d /cygdrive/c && echo /cygdrive/c || echo /c`, then build the path.
> **A wrong prefix arms NOTHING and returns a task id anyway** — it dies `exit 127` in a separate
> `<task-notification status=failed>`, so an agent that misses that notification is **deaf for the session
> while registration, `check-inbox` and `get_agent_status` all still read healthy.** Confirm the arm with
> `TaskOutput(<id>, block=false)` → `running`; that is the only probe that observes a consumer.
> *(Bit two agents on the 2026-07-25 fleet respawn off a hardcoded `/c/` in the watcher skill doc.)*

**BANNED:**
- Launching `inbox-watch.sh ... stream` under Bash `run_in_background` — the Bash tool only notifies on
  *exit*, and stream mode never exits, so **you go silent for the session.** It MUST run under the Monitor tool.
- The bare-path relative launch (`bash org/mcp/inbox-watch.sh ...`) — guard-hook blocked.
- A recurring `/watcher` cron — the persistent Monitor is the standing mechanism.

> **ORPHAN WATCHERS — the one thing you must know.** `inbox-watch.sh` stream mode **HAS** a parent-liveness
> self-exit (`:161-165`, the 2026-07-14 root fix) — but it is **OFF when `$PPID <= 1`** (`:137-141`, a
> deliberate fail-open: MSYS can render a live parent as 1, and a naive check would make healthy watchers
> ⛔ **NOT the `ps -p 1` trap: OBSERVING a parent from outside shows the eval-WRAPPER at ppid=1; a CHILD
> READING ITS OWN `$PPID` sees a REAL pid.** Measured at this seat, one tree: banner `parent-tied: pid
> 515411` - child 515417 ppid=515411 - wrapper 515411 ppid=1. Both statements true, different processes;
> composing them falsely concludes the self-exit never fires.
> suicide). **READ YOUR OWN ARM BANNER** (`:159`, stderr, in the Monitor's output file): `parent-tied: pid
> <N>` = armed, `parent-tied: OFF` = orphan-capable. Measured at this device 2026-08-27: **458 of 471**
> `orphan-audit.log` lines are `WATCHER-SELF-EXIT` — the routine path, not a theoretical one. So orphans are
> **narrower than this file used to claim, and still possible in exactly the fail-open cell.**
> ⛔ **WHY THIS SURVIVED SIX WEEKS: THE DOC, THE FIX AND THE BANNER ARE THREE CARRIERS AND ONLY TWO
> AGREED** (`0.0.0_AB_MSTR~Z`). The fix landed in source with an attributing comment; the banner
> reported truthfully every session; the doc kept describing the pre-fix world — **and the doc is what
> agents read.** A correction is only as complete as its last surviving carrier. An
> orphan is **not inert, it is a thief**: it `mv`s each arriving message into `read/` **before** echoing
> into a dead pipe — **so it eats your mail while manufacturing the strongest possible REACHABLE verdict**
> (a process exists; the inbox is empty *because the orphan drained it*).
> - **`ps`, an empty inbox, and the `read/` dir are BANNED as delivery oracles** — they observe the
>   *watcher*, not the agent. **Only an agent-side ACK proves an agent HEARD a message.**
> - **A fresh session that finds a matching `inbox-watch.sh` process has found an ORPHAN, not a watcher.**
>   Reap it (**your own serial only**) before arming, or two streams race the same `mv` and split your inbox.
> - **BUT ASK WHOSE PID FIRST — the rule above has TWO EXERCISED FALSE-POSITIVES, and killing on it blind
>   makes you deaf while every probe still reads REACHABLE.** Reason from PID identity (**measurable**), never
>   from "am I a fresh session" (**inferred**):
>   `liveness PID == MY PID` → **it is MINE and ALIVE** — a context-clear is the SAME session and you will not
>   remember arming it (**MSTR reaped its own live watcher this way, 07-16**). **DO NOT KILL.**
>   `liveness PID != MY PID` (fresh heartbeat) → a **LIVE PEER** holds your serial — **STOP, identity conflict**
>   → Andrew/CTO (the dual-COO collision, 07-14). · `STALE`/absent → genuine orphan; reap your own, then arm.
>
> Depth: `.claude/skills/watcher/SKILL.md`.

**Never use `TaskList` to check your watcher.** It lists `TaskCreate` to-do items, not Monitors, and returns
"No tasks found" even when your Monitor is alive — treating that as a dead watcher makes agents double-arm.

### ⚠ TILDE-LANE PATHS: THE TWO FAMILIES USE **OPPOSITE** FORMS. CHECK WHICH ONE YOU ARE IN.

| you are writing… | canonical form | substituting `{serial}` whole gives… |
|---|---|---|
| **your AGENT FOLDER** (`org/{tier}/…`) | **FLAT** — `org/tier2_senior/0.7.0_AE_CloudOps~B/` | **the RIGHT answer.** Do substitute. |
| **an INBOX** (`org/mcp/inbox/…`) | **NESTED** — `org/mcp/inbox/{base}/~{lane}/` | **the DEAD answer.** Never substitute. |

**The same habit is correct in one family and silently fatal in the other**, which is why "flat is
legacy" is a **false generalization** — it is true of inboxes only. Measured 2026-07-30: agent
folders carry **148 tracked files under FLAT lane dirs vs 1 under nested** (newest flat commit
2026-07-29; the lone nested dir's only commit is a 2026-05-27 emergency SALVAGE sweep, not a lane
agent working). `Step 1`'s own `org/{tier_folder}/{your_serial}/README.md` **tells you to substitute**
— and there that is right.

**So: ask which FAMILY you are in before you build the path. Do not carry a rule across.** The
inbox rule below is scoped to inboxes; it is not a principle about tilde serials in general.
*(Both failure directions are live: an agent that over-applies "always split" creates a dead
`org/{tier}/{base}/~{lane}/` agent folder; one that over-applies "flat is legacy" avoids the very
folder its whole lane writes to.)*

### Inbox path — CANONICAL vs the FLAT form that silently swallows mail

| | path | |
|---|---|---|
| base serial | `org/mcp/inbox/{base}/` | ✅ |
| **lane serial** | **`org/mcp/inbox/{base}/~{lane}/`** — NESTED | ✅ **CANONICAL** |
| **lane serial** | **`org/mcp/inbox/{base}~{lane}/`** — FLAT | ⛔ **NEVER. INVISIBLE TO THE ENTIRE FABRIC.** |

**⛔ NEVER write, read, watch, or hand-construct the FLAT form `inbox/{base}~{lane}/`.** The broker
never writes it (`org/mcp/server.py:1615`), `check_inbox` never reads it (`:1745`), and no watcher
ever polls it (`org/mcp/inbox-watch.sh:73-77`, header `:28-30` — *"Serial WITH ~suffix watches ONLY
the nested dir"*). **A message placed there is delivered to nobody and reported missing by nothing.**

**THE TRAP IS SUBSTITUTION, and it is why this keeps happening: for a lane serial, `inbox/{serial}/`
IS the flat path.** Writing your own serial into a `{serial}` slot silently produces the dead form —
so **never substitute a lane serial into an INBOX `{serial}` path slot; split it into `{base}` +
`~{lane}` first.** ⚠ **SCOPE — INBOXES ONLY. This is NOT a general rule about tilde serials, and
reading it as one breaks your agent folder** (see the two-families table above: there, substituting
the whole serial is CORRECT). *The unscoped phrasing of this sentence is itself what made a reader
generalize it, 2026-07-30.*

Ratified: **LD-0202** (Andrew-direct 2026-06-18: *"the tilde suffix strip has all kinds of errors…
fix every case of collapsing, clobbering, bullshit"*). Regression test: `org/mcp/test_ld0202_tilde_routing.py`.
Design: `docs/architecture/AGENT_COMMS_ARCHITECTURE.md`.

⛔ **WRITING A MESSAGE TO MORE THAN ONE SEAT? NAME THE SERIAL, NEVER "YOU"/"YOUR".** One body goes to
N inboxes and each is header-stamped `To: <that recipient>`, so **a second person resolves per reader** --
"you were right" reads as addressed to all of them. Write `3.0.0_SA_CVO's 70924 found X`, not "your
finding". CLAUDE.md carries the rule; it is repeated here because this is where messages get composed.

**When an `[INBOX]` event fires, that IS a new message.** Read it from your canonical inbox's `read/`
subdir — base `inbox/{base}/read/<file>`, lane `inbox/{base}/~{lane}/read/<file>` (the
watcher already moved it there) and **act this turn** — ack (RAVC step 2), do the work, or validate the
evidence (RAVC step 4). **No "standing by" silence. Do not relaunch anything.**

**If the inbox has a GO:** read the referenced task order, flip `<status>` to `pending`, **begin
immediately.** The GO **is** your authorization — do not ask Andrew.

**If the GO lists a SEQUENCE of TOs:** execute **all of them in order** without waiting for a new GO. Skip
any already complete. Keep going until a TO is blocked (deps unmet) or the list is exhausted. **Stopping
mid-sequence to ask for a new GO is a protocol violation** — the batch GO covers the whole lane.

**D. Install the owned-paths hook (idempotent):**
```bash
test -L .git/hooks/pre-commit || bash .tools/git-hooks/install-owned-paths.sh
```

**E. Set compiler-tool context (enables auto-logging):**
```bash
mkdir -p .comp-graph && printf "SERIAL=%s\nTO_ID=\n" "{your_serial}" > .comp-graph/.agent_context
```
Comp-* runs record to `org/mcp/comp-tool-runs.jsonl` only. **The `org/compiler-tools-log.md` auto-append is RETIRED** (Andrew-direct 2026-07-29, *"just constant commit nonsense"*) — killed at source in `comp_log_auto.py:_append_log`, exercised. **SCOPE: the WRITE is gone, THE FILE IS PRESERVED** at its committed state as readable history — never commit it, never re-point a writer at it. ⚠ **`comp-tool-runs.jsonl` IS GITIGNORED (`.gitignore:447`) = DEVICE-LOCAL, NOT a durable cross-device record** — each device sees only its own runs, so any "estate's comp-tool runs" claim read from it is silently short by every other device's traffic. **

**When you start a new TO, set it with `comp-to` — never by writing `TO_ID=` into `.agent_context`:**
```bash
comp-to {TO_filename_without_.md}      # e.g. comp-to ADVI_OFFICE.W1
```
`.agent_context` is one repo-global file, last-writer-wins across all concurrent agents; `comp-to` writes a
race-free per-session file instead.

**F. Loop arming — EVERY serial, including the COO, arms ZERO crons at launch. There is no exception.**

Loops are **operator-initiated**. `/watcher` is not a loop — it arms the persistent inbox Monitor once.

| Serial | Launch arming |
|---|---|
| `0.0.0_AB_MSTR` | `/watcher` once. **`/agentbus` once** (Andrew-direct 2026-07-29; arm-at-load, same pattern as `/watcher`, NOT a loop) — it arms this **device's** cross-device SQS consumer, and while none runs, mail to this device is not delivered, it **accumulates** (measured cost when unarmed: 1h26m on a priority TO). **ONE CONSUMER PER DEVICE: an `rc=3` refusal naming a live pid IS SUCCESS** — do not work around it; SQS is exactly-once, so a second consumer *steals* mail rather than duplicating it. Zero crons. **`/integrate` once at load — the JOINT FABRIC PARITY ASSESSMENT, and it REPLACES the `/git-pull once` step.** (Andrew-direct 2026-08-12, VERBATIM: *"something I want to bring in to the mstr launch script is not just blindly running git pull, its better to run /integrate as a joint fabric parity assessment and this parity can either be just an assessment (default), or it can be /integrate merge, which is assess and proceed the merge."*) **BARE `/integrate` IS ASSESS-ONLY and is the load form — it measures and reports, it MERGES NOTHING AND PUSHES NOTHING**; `/integrate merge` is assess-and-proceed and is **NEVER** the automatic load form (a startup that silently merged two fabrics would be a shared-branch write nobody asked for, on a device that may have just woken with stale context — reading is always safe at load, writing is not). ⚠ **THE PULL IS NOT DROPPED, IT IS ABSORBED** as `/integrate` **Step 1b** (fetch + `merge --ff-only` your OWN branch) — the precondition that makes the assessment trustworthy, because **a parity assessment computed from a STALE LOCAL REF is wrong the same way a SHALLOW CLONE is wrong**: both produce confident, well-formed divergence numbers off an incomplete graph. **WHY THE SWAP: `/git-pull` answered SAME-BRANCH currency, and the question that matters at load is CROSS-BRANCH parity** — a seat can run the pull perfectly and still be *structurally* unable to notice the other fabric moved. *Measured at site Z 2026-08-12 ~1320Z: `/git-pull once` printed the CLOUD advance ON SCREEN, the seat ff'd its own branch, saw 0 behind and moved on; the other fabric had advanced ~34h, and that session then spent four hours discovering the divergence by hand.* The severity split below is now Step 1b's. **`/mstr-review` DOES NOT RUN AT STARTUP** — on-demand / event-triggered only, like every other MSTR skill. Both changes Andrew-direct 2026-07-30 ~2000Z at the MSTR~Z terminal, VERBATIM: *"i dont want auto /mstr-review at load anymore, its too noisy. The only thing id recommend is auto /git-pull at mstr load, just an ad hoc pull though not a looped pull."* **The ad-hoc/looped distinction is his, stated explicitly, and is the load-bearing half** — `/git-pull` bare arms a 15-minute loop, so the correct call was `/git-pull once`; **SUPERSEDED 2026-08-12 — the load step is now `/integrate` (assess-only), which ABSORBS that pull as its Step 1b; the never-arm-the-loop half of this clause still binds**; arming the loop is the thing he ruled against, and it would also breach the standing zero-crons-at-launch rule this very row states. *(A prior session banked the pull need in memory after he asked "did you pull git?"; this makes it law. Startup previously had no pull step at all, which is why CLOUD routinely moved under a session mid-work.)* >> **SYMMETRIC IN MECHANISM, ASYMMETRIC IN WEIGHT — Andrew-direct intent clarification, same ~2000Z exchange, VERBATIM:** *"the bigger reason i want that function is not so much for us on this device but for the ~Z machine because they are not the primary fabric worker so i want to make sure they are updating at load. Because we are primarily working on this device and are constantly committing and pushing, im not so worried about us needing to do ad hoc pulls; we are the reason other machines would NEED to pull, we are effectively source."* **The step is identical on both devices; what it BUYS is not.** On a **NON-PRIMARY device (site Z / any `~Z` seat)** the load-pull IS the sync guarantee and **a failed or skipped one is a REAL FINDING** — that machine is downstream of a tree that commits and pushes continuously, so a stale HEAD there silently poisons every startup evidence read. On the **PRIMARY laptop** it is incidental hygiene: it is *effectively source*, so deferring a load-pull past live uncommitted seat-work is **consistent with this rule's intent, not an exception to it**. ⚠ **A LAPTOP PULL-DEFERRAL IS THEREFORE NOT PRECEDENT FOR A SITE-Z ONE** — reading it as precedent inverts the rule on the exact machine it was written for. **STANDING RULE — SEMANTIC-EVOLUTION GOVERNANCE BACKSTOP (Andrew-direct 2026-07-30, ~2135Z original + ~2158Z AMENDMENT at the CVO terminal, amendment VERBATIM: *"~B is cleared to start, CVO owns the loop, MSTR is backstop."*): the OPERATIONAL daily loop — pull the 9a-Eastern Kimi/K3 estate report, review with Andrew, land ratified semantic changes, flip the per-day manifest — is **CVO's**. MSTR-BASE (no tilde) is the **GOVERNANCE BACKSTOP**: verify the CVO loop RAN — **the oracle is `s3://opal-estate-report/manifest/{YYYY-MM-DD}.json`** — the contract-v2 AS-BUILT key (producer source: `estate_report_runner.py:921` @4e69b1dbc5; every live manifest self-declares `"contract": "v2"`). Lifecycle: born **RUNNING** at run start → rewritten **PENDING** on producer success → terminal via **ADJUDICATED** / **NO-SEMANTIC-CHANGES** (the live estate-pull flipper's vocabulary) or **FAILED** with a named reason. ⚠ **CORRECTED 2026-08-05 (CTO~B grounded read 131259Z, first-scheduled-fire day): this row previously pinned the `{YYYY-MM-DD}/manifest.json` DAY-ROOT and `signed-review` terminal — that is ESTATE_REPORT **v4 SPEC VOCABULARY AND LAYOUT** (@150d45b5b7, RULING 8), and v4 WAS NEVER BUILT (registered open scope on CTO~B's lane @ce84bcfca1). A backstop keyed on the v4 path returns ABSENT forever on healthy days, and one keyed on `signed-review` reads every properly-ADJUDICATED day as un-flipped — two false-finding classes from one version skew, caught pre-arm. When CTO~B lands the v4 migration they notify MSTR AT PLACEMENT and this clause repoints then, not before.** **The finding classes, each distinct: a stale RUNNING (started, never finished) · an un-signed PENDING · a FAILED day · an ABSENT day (reader-computed vs the config anchor — no producer-side record can cover a run that never started, by construction).** ESCALATE gaps to Andrew; MSTR does not run the loop and does not land semantic changes. ⚠ The manifest has **two writers by design** — producer writes, reviewer flips, IAM-separated on mid-key patterns — deliberate, not a race; an oracle reading manifest state is reading a two-writer object with one human-gated writer. **RULING-5 INTEGRITY HALF (Andrew-direct ~2312Z, VERBATIM: *"What i want to be able to do is use this system end to end through MSTR to be able to accurately update that reference artifact and then ~A can use that live fire to do the investigative work for CTO."*): the end-to-end chain runs THROUGH MSTR — beyond the flip check, MSTR verifies the REFERENCE ARTIFACT accurately reflects what Andrew RATIFIED (landed-vs-ratified parity per adjudicated day, so `0.7.0_AE_CloudOps~A` can trust the live fire for CTO investigative work). The first end-to-end fire is the acceptance event for this half.** Human-in-the-loop stays load-bearing (pipeline SUGGESTS, Andrew RATIFIES, CVO LANDS; a semantic change remains a naming act). Event-driven, inert until the pipeline ships (`0.7.0_AE_CloudOps~B` building, cleared ~2158Z); binding from its first report-day. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_RULING_SEMANTIC_EVOLUTION_PIPELINE_20260730.md` RULING 3 (supersedes the ~2135Z MSTR-surfaces form this row carried for ~25 min).** >> **RETIRED CLAUSES -> `org/tier0/ledger/LD-0471.md`** (Andrew-direct 2026-08-28, VERBATIM: *"yes manage the xxx.md rulings"*): the DISCHARGED `/govern` scoped re-arm (Andrew stood it down 2026-08-05 ~1550Z; **successors do NOT re-arm**) and the EXPIRED 2026-08-25 ADR pre-check with its superseded overnight-run chain -- both moved VERBATIM to the ledger on THEIR OWN stop-conditions, which is executing the row, not amending it (`1.0.0_SA_CTO~Z` ruling, msg 13636). **Zero crons still stands.** **`/govern` arms ONLY on Andrew's explicit word** and is the sole exception to this seat's integrator-and-observer envelope -- `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260828_MSTR_INTEGRATOR_AND_OBSERVER_ONLY.md` @3da6c6506a. |
| `1.0.0_SA_CTO` | `/watcher` once. Zero crons. `/ws-charter` is ad-hoc. ~~**⚡ LIVE SCOPED ARM -- site-Z `1.0.0_SA_CTO~Z` ONLY, 2026-08-24 ~20:0xZ, ANDREW-DIRECT AT THE CTO~Z TERMINAL** (VERBATIM: *"[30m] <Run /open-calls, pitching the calls with your recs to CVO to adjudicate, then proceed. This workflow and process applies exclusively to ETFS_POSITIONING work and that is the only work your fabric should be doing this session.>"* + *"Then make this loop a skill called /self-drive ..."* + *"the loop persists until the directive is done. Once complete, the loop turns off and the driver writes a log on the self-drive process or every 2 loops, whichever comes first."*; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_ANDREW_DIRECT_20260824_LOOP30M_OPENCALLS_CVO_ADJUDICATES_FABRIC_SCOPE_ETFS_POSITIONING_ONLY.md`): **`/self-drive D4`** (`.claude/skills/self-drive/SKILL.md`), cadence 30m -- each tick = `/open-calls` scoped to D4 (`ETFS_POSITIONING` + `ETFS_INGEST`) -> ADJUDICABLE calls pitched with recs to `3.0.0_SA_CVO~Z` -> proceed on verdicts; RESERVED (NEVER-class) calls stay at Andrew; dispatches NOTHING on a timer (not `/drive`). **STOP-CONDITION: D4 DONE per the skill's §4 register read (every member/claimed project `status: complete`), or his stand-down -> the driver STRIKES this clause and returns to zero-crons.** **THIS ROW IS THE ONLY DURABLE CARRIER -- the cron is SESSION-ONLY; a successor `1.0.0_SA_CTO~Z` RE-ARMS `/self-drive D4` while D4 is not DONE, because his word is the persistence, not the cron.**~~ **⛔ DISCHARGED 2026-08-27 ~15:2xZ BY ANDREW-DIRECT AT THE CTO~Z TERMINAL** — shown the row-vs-word conflict as `/open-calls` CALL 1 (rec = strike the exclusivity half, keep D4 in the ordered set), ruled **VERBATIM: *"recs approved"***. **NOT the clause's own stop-condition — D4 is NOT done.** The discharge is a LATER, WIDER sovereign word: 2026-08-27 he placed six directives here (*"identifying any dependency order in sitez directives and begin full-forcing"*) and then made Model Portfolios top priority — so the 08-24 clause's *"the only work your fabric should be doing this session"* is superseded, and its own words scoped it to *"this session"* regardless. **A SUCCESSOR MUST NOT RE-ARM OFF THIS STRUCK CLAUSE**; a new loop needs fresh Andrew word (the COO-row standing rule, which this row now shares). **WHY IT WAS SURFACED RATHER THAN SELF-STRUCK: `1.0.0_SA_CTO~Z` armed nothing and did NOT strike a sovereign-authored clause on its own authority — the 2026-08-21 COO precedent, where refusing to self-strike was ruled correct. A STANDING INSTRUCTION THAT CONTRADICTS THE LIVE PRACTICE IS A TRAP WITH THE SOVEREIGN'S NAME ON IT, and the row is the only durable carrier, so leaving it would have instructed the next CTO~Z into a superseded scope.** D4 remains rank 2 of his Model Portfolios set and is worked directly; nothing is lost by the strike. Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_SITEZ_DIRECTIVE_DEPENDENCY_ORDER_20260827.md`. ~~**⚡ LIVE SCOPED ARM -- laptop `1.0.0_SA_CTO~X` ONLY, 2026-08-27 ~20:4xZ, ANDREW-DIRECT AT THE CTO~X TERMINAL (fresh word: he invoked `/self-drive D11` directly this session): `/self-drive D11` (`.claude/skills/self-drive/SKILL.md`), cadence 30m -- each tick = `/open-calls` scoped to D11 (`NFRA_SUBSTRATECARDING`) -> ADJUDICABLE calls pitched with recs to `3.0.0_SA_CVO~X` -> proceed on verdicts; RESERVED calls stay at Andrew; dispatches NOTHING on a timer. `paired_with: /drive D11 @ 2.0.0_SA_COO~X (+15m)` per sec 0.6 (his 2026-08-27 ratified drive-pair word), consuming the verdict ledger at `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/D11/VERDICTS.jsonl`. **STOP-CONDITION: D11 DONE per sec-4 register read (every member/claimed project `status: complete`), or HELD-AT-STOP, or his stand-down -> the driver STRIKES this clause (the strike covers BOTH halves) and returns to zero-crons.** A successor `1.0.0_SA_CTO~X` RE-ARMS while D11 is not DONE -- his word is the persistence, not the cron.**~~ **STRUCK 2026-08-28 13:0xZ by `1.0.0_SA_CTO~X` -- HELD-AT-STOP (SKILL sec 4), NOT DONE: after wave 3 flipped @f43e6a7c36, BOTH members are UNREACHABLE by the driver's acts on Andrew's named L2 hold (R1) -- NFRA_SUBSTRATECARDING's remainder (production population + L3 cells) HELD; NFRA_C3MATERIALIZE's only open TO (TO-L2-CROA) HELD; REACHABLE 0 / UNREACHABLE 2; cards D11-T30-R + D11-T31-R at Andrew. The strike covers BOTH halves: `2.0.0_SA_COO~X`'s `/drive D11` reads this and stands down. Cron deleted; zero crons. Final log `org/tier1_exec/1.0.0_SA_CTO/logs/2026-08-28/ctoX_self_drive_D11_tick31_HELD_AT_STOP.md`. Delivered under the arm: ISCK round 4 closed, v0.3-candidate+27 frozen, WP-3 the identity ledger BUILT + certified (receipt eb15d30b6b @a8982310d8), wave 3 flipped. RE-ARM ONLY on his word that lifts L2 or names the act that makes a member reachable -- never off this row's history alone.** **⛔ STRUCK 2026-08-31 15:3xZ -- STOPPED-BY-OPERATOR. THE CLAUSE BELOW IS HISTORY, NOT AN INSTRUCTION; A SUCCESSOR MUST NOT RE-ARM FROM IT. Strike record follows the clause.** **⚡ RE-ARMED 2026-08-28 14:08Z ON THAT WORD -- ANDREW-DIRECT AT THE CTO~X TERMINAL, VERBATIM: *"Lift everything, time to work buddy"* (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260828_1408Z_LIFT_EVERYTHING_TIME_TO_WORK.md`; ledger row 17). The L2 hold (R1) is LIFTED; both D11 members are REACHABLE again. `/self-drive D11` (`.claude/skills/self-drive/SKILL.md`), ~~cadence 30m at :11/:41~~ **cadence 60m at :11 (AMENDED 2026-08-28 16:28Z, ANDREW-DIRECT AT THE CTO~X TERMINAL, VERBATIM: *"push self-drive tick to 60m"* -- cron re-cut at tick 36; the paired half keeps its +15m offset)**, scope RE-RESOLVED from the register each tick; `paired_with: /drive D11 @ 2.0.0_SA_COO~X (+15m)` on the SAME word. STOP-CONDITION: D11 DONE per sec-4 register read, HELD-AT-STOP, or his stand-down -> the driver STRIKES this clause for BOTH halves. A successor `1.0.0_SA_CTO~X` RE-ARMS from THIS clause while D11 is not DONE.** **⛔ STRUCK 2026-08-31 15:3xZ by `1.0.0_SA_CTO~X` -- STOPPED-BY-OPERATOR, on the clause's own enumerated stop-condition (*his stand-down*), ANDREW-DIRECT AT THE CTO~X TERMINAL, VERBATIM AND ENTIRE: *"turn off your self-drive tick for now"*. NOT DONE and NOT HELD-AT-STOP -- D11 reads 0 of 2 complete with BOTH members REACHABLE, so this is an operator stand-down and nothing about the directive's state is implied by it. **THE STRIKE COVERS BOTH HALVES**: `2.0.0_SA_COO~X`'s paired `/drive D11` stands down from this same clause on its next read. Cron `31950a5f` DELETED (measured on `CronList` before deletion, not assumed); this seat returns to ZERO CRONS. Final log `org/tier1_exec/1.0.0_SA_CTO/logs/2026-08-31/ctoX_self_drive_D11_tick106_STOPPED_BY_OPERATOR.md`. ⚠ **HIS WORDS WERE "FOR NOW" AND THAT IS PRESERVED DELIBERATELY** -- a pause in intent, but struck rather than left live because THIS ROW ALREADY CARRIES THE LESSON TWICE: *a standing instruction that contradicts the live practice is a trap with the sovereign's name on it*. An armed clause over a stood-down loop is that trap. **RE-ARM IS CHEAP AND EXPECTED: any fresh word from him re-arms `/self-drive D11` from the skill, never from this struck clause.** ⛔ **AND THE STATE THIS STRIKE DOES *NOT* CHANGE, because a stand-down is not a closure:** D11 NOT DONE (0 of 2, both REACHABLE); W4-COX face `<status>` **pending** with the face proof CUT but NOT jointly passed and NOT read by this lane; cards 7 of 7 CELLS-ONLY of 12 wave-4 REMOTE, which is **NOT** the class close; `NFRA_C3MATERIALIZE` typed `B-NO-DECLARED-RELATION-YET` on the firm-carry condition with gate `after-bridge-declared` **STAYING OPEN**; HALTGT assigned to `0.7.0_AE_CloudOps` with this lane's five design clauses binding, NOT started; RULE 3 Class A remainder 2 + 2 unclosed; 2 CARRIED cards still at Andrew. ⛔ **ALL FIVE ~X D11 PEER SEATS WERE MEASURED DOWN AT THE STRIKE** (issuer, both executors, both certifiers) -- the loop had no counterparty for ~14 hours, which is the substantive reason a heartbeating loop was worth stopping rather than merely quiet.** ~~The laptop base CTO arms NOTHING.~~ **SUPERSEDED for ONE scope 2026-08-27 ~20:5xZ -- ANDREW-DIRECT AT THE LAPTOP BASE CTO TERMINAL: `/self-drive D2 & D3` invoked by him, THE FIRST DRIVE PAIR (protocol @ac4a79fc2c, his 'DO it get this set up' + this invocation).** Scope = D2 + D3, RE-RESOLVED from the register each tick (predicate, never the arm-time list; at arm: 10 projects [D2: 9 incl. same-day registrations ADVI_49F + ADVI_BDPARITY; D3: D3_MODELOVERLAY], 27 open TOs, device laptop, claims scan 339 JSONs 0 lag). Cadence 30m at :07/:37 (off the fleet marks). **`paired_with: /drive D2 & D3 @ 2.0.0_SA_COO (+15m, :22/:52)` per s.0.6 default-yes -- the COO half arms on this SAME word**; verdict ledger `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/D2-D3/VERDICTS.jsonl`. **STOP-CONDITION (ONE for both halves): every member project `status: complete` per the s.4 register READ, or HELD-AT-STOP when only structurally-unreachable members remain, or his stand-down -> whichever half reads it first STRIKES this clause for BOTH and the peer stands down on its next tick.** THIS ROW IS THE ONLY DURABLE CARRIER -- crons are SESSION-ONLY; a successor at EITHER seat re-arms its half from THIS ROW ONLY while the scope is not DONE. **RE-ARMED 2026-08-28 15:46Z by the successor `1.0.0_SA_CTO` from THIS clause after the 00:5xZ reboot stand-down, on Andrew's fresh word at the CTO terminal 15:32Z, VERBATIM: *"We need to get back to work on D2 and D3, I'll pull COO online"* (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260828_1532Z_D2D3_RESUME_AND_SPAWN_KILL_TO_COO.md`); cron bde882a4 :07/:37, tick 9; the COO half re-armed 15:41Z (78180). Scope + stop-condition unchanged.** **RE-ARMED AGAIN 2026-08-30 ~01:0xZ by the successor `1.0.0_SA_CTO` from THIS clause after the 2026-08-29 21:2xZ reboot wind-down (handoff `org/tier1_exec/1.0.0_SA_CTO/handoffs/2026-08-29_2140Z_winddown_D2-D3.md` -- the clause was deliberately left un-struck: a pause, not a stand-down), on Andrew's word at the CTO terminal 00:20Z, VERBATIM: *"relaunch after the reboot. Read handoffs/2026-08-29_2140Z_winddown_D2-D3.md and re-arm /self-drive D2 & D3 from your XXX.md clause. MSTR is relaunching COO base + your D2/D3 seats now."* (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260830_0020Z_RELAUNCH_REARM_D2D3_FROM_CLAUSE.md`); resumes at tick 69 (tick 68 died mid-Step-0 at the wind-down); at re-arm the register reads 26 open TOs (D2 20 / D3 6) and a fresh to-check extraction AGREES at 26; the COO half re-arms on this SAME word. Scope + cadence (:07/:37) + pairing + stop-condition unchanged.** **RE-ARMED AGAIN 2026-09-01 ~07:0xZ by the successor `1.0.0_SA_CTO` from THIS clause (crons read ZERO at re-arm -- the 08-30 session died at tick 102; resumes at tick 103), on Andrew's fresh word relayed VERBATIM by `0.0.0_AB_MSTR` 90895 from the MSTR terminal 06:5xZ: *"Then i wand full force on D2 with coo on laptop fabric being instructed to put together a drive loop to run it down all 22 TOs and CTO base on /self-drive loop targeting d2 first, then d8"* (push limb of the same word discharged: origin/CLOUD `2912ff3973`, 122 commits / 16 authors, D8 ON ORIGIN as LAPTOP). ⛔ **SCOPE AMENDED, AND ONE LIMB IS DELIBERATELY NOT RESOLVED: he named an ORDER -- D2 FIRST, THEN D8 -- and D8 JOINS this clause's scope (it is LAPTOP-placed as of `e1e2ff275b`, so the s.0.2 device guard passes). D3 IS NEITHER NAMED NOR STRUCK BY HIS WORD. This driver does NOT strike it (that is narrowing on the driver's own authority, the 2026-08-21 COO precedent) and does NOT silently keep it ahead of D8 (that is widening against his stated order). D3 REMAINS IN SCOPE, ITS ORDER RELATIVE TO D8 IS SURFACED TO ANDREW AS A CARD, and until he answers the driver works D2 -- which his word makes unambiguous and which is FIRST under every reading.** Register at re-arm: D2 22 open TOs / 10 member projects (8 active, 2 complete; claims scan 348 JSONs, 7 claims, 0 lag, 0 malformed); D3 4 open TOs / 1 project; D8 1 open TO / 3 projects. Verdict ledger stays `drive_pairs/D2-D3/VERDICTS.jsonl` (19 rows) until his answer renames the pair. **The COO half re-arms on this SAME word and he instructed it directly at the MSTR terminal ("coo ... put together a drive loop to run it down all 22 TOs").** Cadence + pairing + stop-condition otherwise unchanged.** Beyond this scope the arms-NOTHING default stands. |
| `2.0.0_SA_COO` | `/watcher` once. **ZERO crons -- `/drive` is OFF (Andrew-direct, standing; LD-0288/0289/0293).** The COO **coordinates and routes; it does NOT re-drive the estate.** ~~**LIVE SCOPED RE-ARM -- site-Z `COO~Z` ONLY** (Andrew-direct 2026-08-11 ~1020Z at the MSTR~Z terminal, VERBATIM: *"also might as well bring COO~Z on too with a drive loop just to check on the fabric every 10m and make sure this gets done."*): ARM `/loop 10m /drive` **SCOPED TO the OPAL_ANALYST atom-decomp program** -- record `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260811_OPAL_ANALYST_ATOMDECOMP_PROGRAM.md` @c4972dab41; **CTO~Z owns the PRD and the routing.** SCOPE, so the loop cannot widen itself: it **checks progress and unblocks**; it does **NOT** re-route around CTO~Z, re-drive the wider estate, or open non-program workstreams. **STOP-CONDITION: the program completes OR Andrew stands it down -> discharge the clause and return to OFF-by-default.** **THIS ROW IS THE ONLY DURABLE CARRIER -- the cron is SESSION-ONLY and expires in 7d, so a respawned `COO~Z` MUST RE-ARM while the scope is live.** **The laptop base COO arms NOTHING.**~~ **DISCHARGED 2026-08-20 ~1230Z by 1.0.0_SA_CTO~Z (law-file strike + same-turn MCP broadcast to every live seat): NOT by the row's own stop-condition (the OPAL_ANALYST program is still active -- D6 build done, certs queued) but by a TIER-0 DIRECTIVE that `latest + most-restrictive` binds on -- MSTR~Z's 08-19 kickoff 192420Z under Andrew's ~19:0xZ co-oversight instantiation (record @219bbc246c), VERBATIM: *"ZERO CRONS at launch -- every scoped /drive re-arm in the XXX.md COO row is DISCHARGED; a new loop needs Andrew's fresh word."* Reaffirmed by the 08-20 ~0418Z launcher law @4bbc0ccbeb (launch scripts SESSION-AGNOSTIC, zero loops at launch) and honored by both COO~Z sessions (08-19 night + 08-20 morning armed NOTHING, each grounded in its log). A successor MUST NOT re-arm off this struck clause -- a new scope needs a NEW Andrew authorization (standing rule 1 below). Verbatim clause relocated as cycle #6 in `docs/references/COO_DRIVE_REARM_HISTORY.md`.** ~~**⚡ LIVE SCOPED RE-ARM -- site-Z `COO~Z` ONLY, 2026-08-20 ~14:2xZ, ANDREW-DIRECT AT THE CTO~Z TERMINAL** (VERBATIM, his second instruction of the minute after *"you dont need to be working on sysparity, you should be working on the D6 D7 D9 etc sitez directives"*: *"get COO~Z online and redirect focus to the sitez directives and begin the relevant /drive loop to proceed those projects to completion"*; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_ANDREW_DIRECT_20260820_SITEZ_DIRECTIVES_NOT_SYSPARITY.md` @2b3b2eaeaa): ARM `/loop 10m /drive` **SCOPED TO the site-Z D-family directives -- D6 (Opal Analyst + partner query layer) / D7 (Ticketing intake) / D8 (live-edit modals) / D9 (Tax SMA) -- to completion.** Cadence 10m = the 08-11 precedent for this seat (he named none; stated as precedent, not his word). **CTO~Z rules + routes the D-family (@550b20ec5b).** SCOPE, so the loop cannot widen itself: it **checks progress and unblocks** inside the site-Z D-family program; it does **NOT** re-route around CTO~Z, re-drive the wider estate, or open non-program workstreams. **THIS IS A NEW AUTHORIZATION, NOT a re-arm off the struck 08-11 clause above (that discharge stands).** **STOP-CONDITION: the site-Z D-family directives COMPLETE or Andrew stands it down -> discharge this clause (COO-cell form) and return to OFF-by-default.** **THIS ROW IS THE ONLY DURABLE CARRIER -- the cron is SESSION-ONLY and expires in 7d, so a respawned `COO~Z` MUST RE-ARM while the scope is live.** The laptop base COO arms NOTHING.~~ **⛔ DISCHARGED 2026-08-21 ~07:3xZ BY ANDREW-DIRECT AT THE CTO~Z TERMINAL -- he was shown the row-vs-practice conflict as an open call and ruled STRIKE, VERBATIM: *"approved on all"* (on `1.0.0_SA_CTO~Z`'s /open-calls CALL 4, rec = strike). NOT the clause's own stop-condition: the site-Z D-family is still live. THE REASON IS THE CONFLICT ITSELF -- `2.0.0_SA_COO~Z` relaunched 2026-08-21, was told to arm nothing, armed nothing, and CORRECTLY REFUSED TO STRIKE A SOVEREIGN-AUTHORED CLAUSE ON ITS OWN AUTHORITY; so the row and the practice disagreed ON DISK and the next COO~Z would have read a row instructing it to re-arm. **A STANDING INSTRUCTION THAT CONTRADICTS THE LIVE PRACTICE IS A TRAP WITH THE SOVEREIGN'S NAME ON IT.** A new scope needs NEW Andrew authorization (standing rule 1 below). Verbatim clause preserved struck above.** >> **TWO STANDING RULES -- these are why this cell is short, and a successor cannot work without them:** **(1) A DISCHARGED RE-ARM IS NEVER A WARRANT.** Never arm `/drive` off an expired scope: a new scope needs a NEW Andrew authorization. *(Every one of the five discharged cycles ends with this same warning, which is why it is stated once here as a rule instead of a sixth time as an anecdote.)* **(2) THE MECHANISM, which is the reason the loop is OFF and not merely unused:** `/drive`'s own gate treats "all standing by" as a FAILURE, so it is **structurally unable to conclude "dispatch nothing"** -- armed during a dispatch hold it is obligated to break that hold on a timer, reasoning correctly from a real mandate. **Dispatch authority during a hold rests with the GO-issuing owner, never a timer** (`014de1937`, 2026-07-14). << **⚡ LIVE SCOPED ARM -- LAPTOP BASE `2.0.0_SA_COO`, 2026-08-27 ~20:4xZ, ANDREW-DIRECT AT THE COO TERMINAL:** he invoked **`/drive D2 & D3`** himself (the invocation IS the fresh word under standing rule (1); command-args verbatim: `D2 & D3`). **ARM `/drive` SCOPED EXACTLY TO THE D2 + D3 REGISTER PREDICATES** (member sets re-resolved from `org/missions/DIRECTIVES.yaml` each tick, never a pinned list -- at arm time D2 carried 9 projects, D3 carried D3_MODELOVERLAY), cadence 20m per the skill's own table (ACTIVE > 2 in scope), cron minute OFF the :00/:30 fleet marks. SCOPE, so the loop cannot widen itself: it finds blocks, routes seats, and cuts TOs inside D2 + D3 ONLY; the SOVEREIGN EXCLUSION list, the ~X-cohort fence, the PERFRP-subject restriction, and D3's ruled fold-in sequencing (brief @e4f7ecbfdc s.4: full fold-in at P1-green + P3-clear; preparation acts legal before it) all ride every tick. **PAIRED (amended same-session ~20:5xZ, minutes after the first write): Andrew invoked `/self-drive D2 & D3` at the CTO terminal on the SAME word -- THIS IS THE FIRST DRIVE PAIR** (`paired_with:` the CTO row's D2 & D3 clause @310a20e38c; protocol org/ref/DRIVE_PAIR_PROTOCOL.md). CTO half cron 17fc9648 at :07/:37; **this half at :22/:52 (+15m)**, cadence 30m paired form; ledger org/tier1_exec/1.0.0_SA_CTO/drive_pairs/D2-D3/VERDICTS.jsonl (COO writes ONLY `consumed`); scoped obligation = unconsumed rows + measured in-scope blocks, **EMPTY TICK LEGAL** (the designed exception); ONE stop-condition strikes BOTH halves from the shared clauses. The first write's "NOT a pair / 20m / hard gate binds" text is superseded by this sentence -- preserved in the git history, corrected here because a successor arming 20m-unpaired off the stale words would run the wrong instrument. **STOP-CONDITION: D2 + D3 read complete off the register, OR Andrew stands it down -> discharge this clause (strike, COO-cell form) and return to OFF-by-default.** **THIS ROW IS THE ONLY DURABLE CARRIER -- the cron is SESSION-ONLY and expires in 7d; a respawned base COO RE-ARMS from THIS ROW while the scope is live, never from memory.** **⚡ LIVE SCOPED ARM — SITE-Z `2.0.0_SA_COO~Z`, 2026-08-28 ~02:3xZ, ANDREW-DIRECT AT THE COO~Z TERMINAL:** he invoked **`/drive [20m]`** himself with args, VERBATIM: *"No need for taking logs, you just need to keep the fabric discipined and proceed through D1 and D4 TO completion. No distractions, pure execution, if there are issues they go to surprise-channel and CVO investigates. Make sure CVO doesnt get distracted either, we all need to stay on schedule here."* **The invocation IS the fresh word under standing rule (1)** — a discharged re-arm is never a warrant, and this is a NEW authorization, not a re-arm off any struck clause above. **ARM `/drive` at 20m SCOPED EXACTLY TO D1 + D4 TO COMPLETION** — members re-resolved from `org/missions/DIRECTIVES.yaml` each tick, never a pinned list (at arm time: D1 = `D1_CATVIEWS` + `D1_NAMEDISCOVERY`; D4 = `ETFS_POSITIONING` + `ETFS_INGEST` + `ETFS_SATELLITES`, with **`ETFS_CANON` DEFERRED by his 2026-08-24 word and OUT of the completion set**). ⛔ **NOT A PAIR** — no `paired_with:`, no verdict ledger; this is an estate-form `/drive` narrowed to a scope by his args. ⛔ **HIS THREE STANDING CLAUSES RIDE EVERY TICK: (a) NO COMMITTED DRIVE LOG per tick** (*"no need for taking logs"*) — Step 7 is stood down, and a `[STUCK]` conviction still requires its window stated in the escalation itself; **(b) ISSUES GO TO THE SURPRISE CHANNEL AND `3.0.0_SA_CVO~Z` INVESTIGATES** — the driver does not stop to chase them; **(c) KEEP `3.0.0_SA_CVO~Z` UNDISTRACTED** — relayed to that seat same-turn; an OBSERVATION/INERT item never interrupts the schedule. **STOP-CONDITION: D1 + D4 read complete off the register, OR Andrew stands it down → discharge this clause (strike, COO-cell form) and return to OFF-by-default.** **THIS ROW IS THE ONLY DURABLE CARRIER — the cron is SESSION-ONLY and expires in 7d; a respawned `2.0.0_SA_COO~Z` RE-ARMS FROM THIS ROW while D1+D4 are not done, never from memory.** **This row is the ONLY source of truth for a live scoped authorization** -- `.tools/ajb.ps1` deliberately carries no cadence and defers here. Loop *mechanics* (not arming): `org/ref/COO_LOOP_OPS.md`. ⛔ **DISCHARGED 2026-08-31 ~21:2xZ BY ITS OWN TERMS, struck by `2.0.0_SA_COO` (the cell's owner; `0.0.0_AB_MSTR` and `0.0.0_AB_MSTR~Z` both surfaced the condition and both correctly DECLINED to strike another seat's row).** The rider's own stop-condition was *"when it lands this rider is SPENT and should be struck"* -- and **B.0 HAS LANDED ON SITEZ**. VERIFIED AT THIS SEAT on a fresh `git fetch origin SITEZ` rather than on the relay: `git show origin/SITEZ:org/XXX.md` (91,316 B) carries the **B.0 STEP HEADER** (line-anchored `^\*\*B\.0`, 1 hit), POSITIVE CONTROL `Step 1b` = 3, NEGATIVE CONTROL = 0. ⭐ Probed for the **STEP**, never the token -- the rider itself warns the token count now returns a FALSE 1 against the rider's own text, so a token probe would confirm nothing. **CONSEQUENCE, so nobody re-adds it:** new site-Z seats read B.0 from the tree like any other seat, so a `--say` hint need not carry it. ⭐ **AND THE MECHANISM IS WORTH MORE THAN THE HOUSEKEEPING: THE LEG-1 SYNC MERGE CARRIED THE STARTUP LAW ACROSS AS A SIDE EFFECT, AND NEITHER INTEGRATOR PREDICTED IT.** The two things both called *"leg 2"* (the cross-site sync leg and LD-0480's leg 2) were flagged as a NAME COLLISION, i.e. unrelated -- yet the sync leg is what delivered the startup law to site Z. ⚠ That does NOT make them the same leg 2 and nobody has verified that: **one CARRIED the other, which is a different claim.** >> **THE GENERAL FORM: A BULK MERGE DELIVERS LAW, NOT JUST FILES. 749 commits crossed a device boundary and one of them silently satisfied a standing rider's condition; nobody scoped the merge as a law change and it was one.** << ⭐ **THE ONLY DISCHARGE EVIDENCE THAT IS AN EXERCISE RATHER THAN A READ (folded from the SITEZ rendering @`26585faa03`, `2.0.0_SA_COO~Z`, after the 22:2xZ leg-1 merge took this rendering):** the probe above and the two ~Z probes are all READS of the same text -- SAME RUNG, one signal counted three times. `2.0.0_SA_COO~Z` was spawned 21:14Z with a `--say` that DID NOT carry the B.0 hint, read B.0 from the TREE like any other seat, and RAN it: `get_delivery_state` **1/1 READ on its own serial, no foreign stamp**. ⛔ **The reads establish the text is PRESENT; only that run establishes it WORKS** -- a live seat behaving correctly WITHOUT the hint is precisely what the rider existed to guarantee, and it is the only evidence on a different rung (`1.0.0_SA_CTO~Z`, which also ruled the strike the ROW OWNER's act after `git log` falsified its own starting premise that it had authored the rider). The struck text is preserved verbatim below. ~~⚠ **SPAWN RIDER, HELD BY THIS SEAT 2026-08-30 ~03:3xZ** (`0.0.0_AB_MSTR~Z` 17119, routed HERE because spawn/kill of work-population seats is the COO’s own function on this device): **UNTIL LD-0480 LEG 2 LANDS ON SITEZ, EVERY SITE-Z SPAWN CARRIES THE B.0 ACT IN ITS `--say` HINT.** Step 1b’s B.0 -- *at load, run `get_delivery_state` on your OWN full serial covering the previous session’s last life; any row not READ, or READ by a serial that is not yours, is UNREAD MAIL* -- is on **origin/CLOUD ONLY**. CONFIRMED AT THIS SEAT, not taken on report: `get_delivery_state` in the SITEZ working tree = **0 hits** MEASURED AT 03:3xZ **BEFORE THIS RIDER EXISTED**, POSITIVE CONTROL `Step 1b` = **2 hits**, so the zero was ABSENCE and not a broken read. ⛔ **DO NOT RE-RUN THAT GREP AS THE TEST -- THIS RIDER NOW CONTAINS THE TOKEN AND THE PROBE RETURNS 1 AGAINST ITSELF.** A re-checker reading 1 hit would conclude B.0 had LANDED. **The sound probe is whether Step 1b carries a B.0 STEP**, not whether the token appears. ⭐ **THE MECHANISM IS WHY THE HINT WORKS: `--say` IS READ AT LOAD FROM THE LAUNCHER, NOT FROM THE TREE**, so it reaches a new seat with no merge and no law edit. ⛔ **A STARTUP LAW REACHES FUTURE SEATS ONLY VIA THE TREE OR THE LAUNCHER -- a broadcast reaches LIVE seats, and those are DIFFERENT POPULATIONS**, which is the half CLAUDE.md’s law-edit rule does not cover. The class B.0 closes: a dead session’s offered-but-unread messages are invisible to `check_inbox`, `get_agent_status` AND `read/`. Leg 2 is ANDREW’S and is NOT nudged here; **when it lands this rider is SPENT and should be struck.**~~ Discharged re-arm history, 5 cycles with every Andrew verbatim preserved: `docs/references/COO_DRIVE_REARM_HISTORY.md`. **⚡ LIVE SCOPED ARM -- laptop `2.0.0_SA_COO~X` ONLY, 2026-08-28 ~05:04Z, ANDREW-DIRECT AT THE COO~X TERMINAL, VERBATIM: *"Initiate a /drive loop with concise, directed text focused solely on completing NFRA_C3MATERIALIZE."* + ~05:08Z *"it needs to have one, register it and get it locked in, it should be attached to D11 in directives.yaml"* (record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260828_050xZ_COOX_DRIVE_LOOP_NFRA_C3MATERIALIZE.md`; registered @2130cc49e0). ARM `/drive NFRA_C3MATERIALIZE` -- scope = that project ONLY (`org/projects/NFRA_C3MATERIALIZE.json`, directive D11, PRD `docs/architecture/NFRA_C3MATERIALIZE_PRD.md`; "completing" = the PRD's sec-6 falsification tests, never milestones); cadence 20m at `4,24,44` (off the fleet marks and the D11 pair's :26/:56); output concise and directed per his word. NOT a pair by his word (he invoked `/drive` at COO; CTO~X declined the `/self-drive` half 77456; the D11 ledger stays the D11 tick's to consume). It does not displace the D11 pair half at this seat -- he did not name it; if "solely" was meant to, that is his to say. **STOP-CONDITION: `org/projects/NFRA_C3MATERIALIZE.json` reads `status: complete` (the 2-step atomic close), or Andrew stands it down -> discharge this clause (COO-cell form) and return to OFF-by-default.** THIS CLAUSE + the record are the ONLY durable carriers -- the cron is SESSION-ONLY; a successor `2.0.0_SA_COO~X` RE-ARMS from here while the scope is not DONE.** **LIVE SCOPED ARM -- LAPTOP BASE `2.0.0_SA_COO` (THIS SEAT), 2026-09-01 ~06:5xZ, ANDREW-DIRECT at the `0.0.0_AB_MSTR` terminal, relayed VERBATIM by that seat at msg 90894: *"i wand full force on D2 with coo on laptop fabric being instructed to put together a drive loop to run it down all 22 TOs and CTO base on /self-drive loop targeting d2 first, then d8"*. ARM `/loop 20m /drive D2` -- SCOPE = the D2 directive's **22 OPEN TASK ORDERS ONLY**, which is his own ruled done-bar (03:4xZ "agreed with all recs", record @c203d78efc; `1.0.0_SA_CTO` records D2 scope as RULED at 22 TOs). **CADENCE 20m IS THIS SEAT'S CHOICE AND NOT HIS WORD** -- he named none; 20m follows the 2026-08-28 `COO~X` precedent, and a tighter tick does not make lanes faster, it only adds coordinator overhead to seats already executing. SCOPE DISCIPLINE so the loop cannot widen itself: it CHECKS PROGRESS AND UNBLOCKS across the 22; it does NOT open non-D2 workstreams, does NOT absorb the UNCOVERED per-date flow-ingestion defect (unowned, at Andrew), and does NOT re-drive D8 -- his order is D2 FIRST, THEN D8, and `1.0.0_SA_CTO` base holds the paired `/self-drive` half. **STOP-CONDITION: the 22 D2 TOs read terminal, or Andrew stands it down -> discharge this clause and return to OFF-by-default.** THIS CLAUSE + the record are the ONLY durable carriers -- the cron is SESSION-ONLY; a successor `2.0.0_SA_COO` RE-ARMS from here while the scope is not DONE.** ⛔ **HELD BY ANDREW 2026-09-02 ~17:2xZ, VERBATIM: "D2 stays off for now."** Asked as `/open-calls` CALL 1 by the base COO (armed at startup from this row, then disarmed on his "finish your startup and await further instruction"; stop-condition MEASURED NOT MET -- 8 of 10 D2 member projects read `active`). ⛔ **THIS IS A PAUSE, NOT A DISCHARGE, AND THE CLAUSE IS DELIBERATELY NOT STRUCK** -- "for now" is a DURATION clause and striking it would adjudicate WIDER than his word, which a relay may not do in either direction. **CONSEQUENCE FOR A SUCCESSOR: DO NOT RE-ARM OFF THE SENTENCE ABOVE.** It still reads "re-arms from here while the scope is not DONE", and the scope is genuinely not done -- so the row and the practice DISAGREE ON DISK, which is exactly the shape the 2026-08-21 strike was ruled on (a standing instruction contradicting live practice is a trap with the sovereign's name on it). The pause is recorded HERE, in the carrier a successor reads, rather than in a broadcast -- Andrew ruled the XXX.md same-turn broadcast "not a viable solution" the same session. **LIFT NEEDS HIS FRESH WORD, exactly as a new scope would (standing rule 1).** |
| `3.0.0_SA_CVO` (base = MAIN) | `/watcher` once. **Zero crons** (LD-0175). **MAIN-fabric verify ONLY (LD-0325 restructure, 2026-07-20):** PORTAL_AUTHHARD W2+, smartx first-conversion, MDPF 49F parity, general main-fabric closeout verify. **SYSPARITY IS NOT YOURS** — LD-0318/0319 (the "verify parity FIRST" responsibility + the 30-min cron) MOVED to `3.0.0_SA_CVO~Z` (next row). A base-CVO load must NOT arm the SYSPARITY cron and must NOT adopt "verify parity FIRST"; this cell previously said the opposite and is the exact stale-record-with-authority hazard the split closes (main CVO flagged it P1, 2026-07-20). `/spot-check` + `/verify-channel` ad-hoc / closeout-triggered. |
| `3.0.0_SA_CVO~Z` (NFRA/~Z group) | `/watcher` once. **FIRST RESPONSIBILITY ON LOAD (Andrew-direct, LD-0319, PERMANENT): verify the system is AT PARITY** — that `infra/system/` + `infra/system/sdk/` faithfully represent the live estate — BEFORE other work (`comp-system --check` must read CURRENT + the drift-gate sweep; AT PARITY → note + proceed, DRIFTED → that drift is your first work item). STANDING control (survives NFRA_SYSPARITY closing), distinct from the LD-0318 loop. **SCOPED RE-ARM (Andrew-direct, LD-0318): a 30-min NFRA_SYSPARITY per-domain assumption-verification loop — cron `13,43 * * * *` (off the :00/:30 fleet marks), body = per item `/molecule` + `/verify` (+ `/prd-delta` once the CTO PRD lands), report new verdicts to MSTR (NOT COO — CVO~Z comms confined to {~Z}+{MSTR}+{0.8.0_AE} per LD-0325). RE-ARM EACH CVO~Z SESSION while NFRA_SYSPARITY is active — THIS ROW IS THE ONLY DURABLE CARRIER; a session that reads "zero crons" and does not re-arm silently drops the standing role (record-is-the-only-carrier lesson).** STOP-CONDITION: NFRA_SYSPARITY closes OR Andrew stands it down → then DISCHARGE this clause (strike-through, per the COO `/drive` precedent above) and return CVO~Z to zero-crons-by-default. Arm confirmed 2026-07-19 (cron 02d90dce, first-fire exercised). |
| Tier-2/3 workers (+ `~lanes`) | `/watcher` once. Zero crons. **Event-driven:** act on Monitor-delivered dispatches. Keep your broker summary accurate: `WORKING: <task>` / `IDLE: available` / `BLOCKED: <what>` / `BLOCKED-SOVEREIGN: <decision>`. `/work` is ad-hoc. |

**Find a stale cron from a prior session? Cancel it:** `CronList` → `CronDelete`.

---

## Step 2 — Read your recent logs

```
{your_agent_folder}/logs/{most_recent_date}/
```
Read **all** logs from the most recent date. **You are continuing prior work, not starting fresh.**

---

## Step 2b — Ground-truth reconciliation (SA / COO only)

Reconcile TO statuses and project JSON against logs, commits, and **deployed artifacts**. Correct every
stale document before presenting your summary. **Logs and commits are ground truth — `<status>` is a
claim.** Full protocol: `org/ref/COO_STARTUP.md`.

---

## Step 3 — Read your prompt

Read `{your_agent_folder}/prompt.md` and adopt that role.

---

## Step 4 — Understand your place

Read `org/ORG_CHART.md` — reporting chain, pod members, escalation path.

---

## Step 5 — Give an oriented summary

One paragraph: what projects you're on, what's pending, what's blocked, **what you're starting now.**
**Do not ask permission — state what you are doing.**

---

## `/loop` — operator-initiated only

`/loop` is fired by Andrew or an operator at a specific agent, on demand. **Nothing self-ticks.** It is not
a launch mechanism and not a standing mode: the fabric is event-driven, and your inbox Monitor delivers the
work. **There is no centralized tick — `/drive` is OFF (Andrew standing order; see the COO row in Step
1b-F).** Blocked-agent discovery is event-driven too: keep your broker summary accurate
(`BLOCKED: <what>`), escalate blockers to COO/CTO by MCP, and COO/CTO run `/fabric-check` +
`/stimulus-scan` ad hoc — on signals, not on a timer.

---

## Session log — required sections

Full template: `org/ref/SESSION_LOG_STANDARD.md`.

Every session log must include **`## Compiler Tools`** — a table of tools run, results, what worked, what
failed, any gap found. **Do NOT append to or commit `org/compiler-tools-log.md`** (retired 2026-07-29, Andrew-direct).
**"Blank" and "N/A" are not acceptable.** One sentence explaining why you didn't run one is fine.

**`comp-which "<plain-English question>"` is the DEFAULT for every search and inspection — all roles.** It routes
your question to the right tool, or runs the on-rails `comp-grep` / `comp-glob` itself. **A raw `grep` / `find` /
`aws` inspection is the EXCEPTION** and is gated: it needs an inline `# rail-checked: <why no comp-tool fits>`
marker (audited). Raw search is text-local and connection-blind — it misses coupled things the graph would catch.

**Minimum compiler tools by role:**

| Role | Minimum |
|------|---------|
| DS | `comp-pipescript io <script> --pipeline <tree>` for every gold script touched (**`--pipeline` REQUIRED — flagless is rc=2 REFUSED since 07-30**). `comp-pipescript deployed` before every gold run. `comp-pipescript postdeps <script> --firm <firm>` before any ad-hoc run (flagless silently defaults to bd). `comp-validate <script> --artifact <file>` before signaling AE. |
| DE | `comp-transform schema-check` before touching data props; `comp-blast` before deleting. `comp-routes behaviors` for 4xx/auth debugging. **New cohort/metric/mode:** `comp-transform schema-check --feature [token]` + `comp-transform ternary-audit [Component]` at Phase 1. |
| DT | `comp-pipescript io <script> --pipeline <tree>` for every script deployed (**`--pipeline` REQUIRED — flagless is rc=2 REFUSED**). `comp-iam service <lambda>` after any new boto3 call **(necessary, NOT sufficient — see below)**. `comp-routes behaviors` before CloudFront / Lambda@Edge changes. |
| AE | `comp-pipescript deployed` before every gold-run trigger. `comp-pipescript postdeps <script> --firm <firm>` before any gold run (flagless silently defaults to bd). `comp-iam gaps` after any `iam.tf` change **(necessary, NOT sufficient — see below)**. `comp-blast` on infra before changes. |
| RD | `comp-transform fields` for every component rendering data. |
| COO | `comp-pipescript overlap A B` before authoring cross-domain coordination. `comp-blast` + `comp-routes` + `comp-cache` before decomposing PRDs into TOs. |

> **`comp-iam` IS NOT SUFFICIENT FOR A NEW RESOURCE, AND IT FAILS GREEN.** It models `(action)`, never
> `(action, resource)` — **a role holding `s3:GetObject` on ANY bucket reports `[GRANTED]` for a call to EVERY
> other one.** For a boto3 call against a **new bucket / table / ARN**, verify on the live primitive:
> ```
> aws iam simulate-principal-policy --policy-source-arn <role> --action-names <action> --resource-arns <exact key>
> ```
> **ONE `--resource-arns` per call** (2+ ARNs poisons the held ones to `implicitDeny`), **run the positive control
> as a SEPARATE invocation** (a control batched with the target is corrupted by its own presence), and pass
> `--context-entries` for any conditioned statement (an unsatisfied condition returns a deny byte-identical to a
> real one). Also note `comp-iam`'s default view is **DESIRED** (parsed Terraform) — it cannot tell landed from
> planned. For a fresh change, ground on live `aws iam get-role-policy`.

> **`comp-validate` returning `NO_CONFIG` or `ZERO_CHECKS` means UNVALIDATED — NEVER signal SAFE on it.** Only
> `PASS` / `WAIVED` are safe; `ADVISORY` means read the WARNs. *A script with no validate config produces an
> output that looks like a pass and asserts nothing.*

> **`comp-surface-check` IS RETIRED (Andrew-direct 2026-08-06).** The tool, its registry rows,
> its comp-which route, the S3 publish leg, and BOTH portal enforcement surfaces (CI workflow +
> pre-commit hook) were removed together. **MP/benchmark/ADVI now have no commit-time surface
> guard.** Do not reach for the tool and do not re-add a route to it -- the retired-alias
> invariant polices exactly that.

**Archetype tag.** Every substantive log entry carries a single-line `**archetype:** TAG` header after the
title — one of `EXPLORE` / `TRACE` / `DIAGNOSE` / `VALIDATE` / `DEPLOY` / `IMPLEMENT` / `COORDINATE` /
`SCRIBE`, or `MIXED`. Under-classifying is fine; no scoring. It feeds the stimulus-scan's cost signal.
Taxonomy: `org/tier0/COMPILER_ARCHETYPES.md`. Heartbeats, watcher self-checks and housekeeping commits do
**not** need tags (they dilute the signal).

---

## Task orders

Full template + filename convention: `org/ref/TASK_ORDER_PROTOCOL.md`. Stored in the receiving agent's
`task_orders/` folder.

**Statuses:** `staged` = assigned, wait for GO · `pending` = active · `complete` = done (self-marked) · **`superseded` = the NEED WAS MET ANOTHER WAY (name what superseded it)** · **`cancelled` = the NEED WENT AWAY, a ruling killed it (cite the ruling)**. The last two are set by **COO or the ISSUER, never the assignee alone**, and a terminal status **without its pointer is the rot with a tidier label**. (Andrew-direct 2026-08-07: *"you need to be able to 'supersede' or 'cancel' outstanding task orders in status to clean that up."* `to-check.py` already accepted both — only this line did not name them, so killed work had nowhere honest to go and stayed `pending`.)

**Every TO must include:**
- `<compiler_tools_mandate>` — three-phase (before write, before commit, after commit)
- `<cross_domain_coordination>` — populated by COO/CTO at PRD decomposition using `comp-blast`; `<none/>`
  only if confirmed no shared files or S3 keys with other active TOs
- `<acceptance_criteria>` — **machine-checkable output validation**, not "code runs"
- `<proof_of_spec>` — **the machine-readable data contract (ANDREW-DIRECT 2026-08-11: "I do not
  want TOs being issued that do not have machine-readable data contracts"): the issuer mints the
  criterion-id set at decomposition; the ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance
  from their own efforts, validated by `.tools/proof-of-spec-check.py` before the `complete`
  flip. A TO without the contract is non-conforming — not issued.** Full contract:
  `org/ref/TASK_ORDER_PROTOCOL.md` `<proof_of_spec>`
- A session log with a Compiler Tools section as an explicit deliverable

**A TO with no compiler check logged is NOT accepted as complete** (`org/standards/TO_COMPILER_GATE.md`).

**Author + GO pairing (non-negotiable).** Every TO commit MUST be paired with an MCP `send_message` GO to
the assignee, **addressed to the EXACT registered serial including any `~lane` suffix**, in the same
operational window.
- **A TO file landing on disk via `git commit` alone does NOT notify the assignee.**
- **A GO addressed to the wrong serial lands in a directory the assignee is not watching** (a lane's inbox
  is `inbox/{base}/{~lane}/`).

**The TO author owns the GO and its addressing.** Check `<issued_to>` and address the MCP to that exact
string, suffix included.

**Parallel-wave protocol (COO/CTO).** Before writing TOs for a parallelized wave, run `comp-blast` on every
affected component. **Any node in 2+ blast radii is a CROSS-DOMAIN resource** — flag it in the PRD and in
each TO's `<cross_domain_coordination>`. Agents must MCP each other before committing to cross-domain files.

---

## Closure discipline (SA / COO / CTO only)

Closing a project is a **2-step atomic operation in one commit** — never a single JSON edit:

1. **JSON status flip** — `org/projects/{CODE}.json` → `"status": "complete"` + `"completed": "YYYY-MM-DD"`
   + rewrite `phase` as a closure summary + set `blocking` to `"None"`.
2. **REGISTRY row move** — `org/projects/REGISTRY.md` → delete the row from Active/On-Hold, insert at the
   **top** of Completed/Archived with the completed date + closure notes citing ship evidence.

**Either step alone is silent drift.** Do both, in one commit.

**PRDs are NOT a close step.** They stay in `docs/architecture/`; do not archive them and do not bump their
`Status:` line on close. **`org/projects/{CODE}.json` is the single authoritative close-state.**

**Closure triggers:** **Complete** (goal achieved, no unshipped work) · **Complete-as-superseded** (scope
absorbed elsewhere; `phase` cites the successor) · **Cancelled** (explicit Andrew/CTO directive; `phase`
cites it) · **Inactive / On Hold** (blocked by an external dependency — stays On Hold, do **not** move to
Completed).

---

## Core documents (Tier 2+)

Update your core document **in the same commit** as any structural change (new resource, contract change,
removal).

| Role | Document | Location |
|------|----------|----------|
| RD | `page_inventory.xml` | `{agent_folder}/deliverables/` |
| DE | `pod_inventory.xml` | `{agent_folder}/deliverables/` |
| DS | `data_contract.xml` | `{agent_folder}/deliverables/` |
| DT | `deployment_map.xml` | `{agent_folder}/deliverables/` |
| AE | `pipeline_inventory.xml` | `{agent_folder}/deliverables/` |
| SA | `architecture_brief.xml` | `{agent_folder}/deliverables/` |

**Do not edit another agent's core document.** If your change makes theirs stale, note it in your log and
issue them a task order.

---

## Quick reference

| Thing | Value |
|-------|-------|
| Working branch | `CLOUD` (parent repo) / `DEV` (portal submodule) |
| Commit | `.tools/safe-commit.sh --author "..." -- <paths>` (see CLAUDE.md Rules 14 / 14a) |
| Terraform binary | `.tools/terraform.exe` (apply via `.tools/safe-apply.sh` — never bare) |
| Bun | `/c/Users/AndrewBerman/.bun/bin/bun` |
| `MSYS_NO_PATHCONV=1` | **Only** for Terraform imports / ARN-path args, and `git show <ref>:<path>` when both contain `/`. **NEVER for `git push`** (breaks the VALGATE hook) **or the aws launcher.** |
| Times to Andrew | US Eastern only (never UTC) |
| MCP server | `org/mcp/server.py` — `opal-agent-comms` |
| Broker | Auto-launched by `register_agent`, port 7800 |
| Compiler tools | Trigger table in CLAUDE.md § "Compiler Tools". Runs: `org/mcp/comp-tool-runs.jsonl` — **gitignored/device-local, not a cross-device record**. `org/compiler-tools-log.md`: auto-append RETIRED, file preserved, never committed |
