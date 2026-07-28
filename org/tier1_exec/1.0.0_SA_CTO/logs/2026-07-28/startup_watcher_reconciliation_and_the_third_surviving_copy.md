# 1.0.0_SA_CTO — startup: watcher, reconciliation, and a third surviving copy

**archetype:** MIXED
**Session:** 2026-07-28, from ~1256Z. Base-fabric respawn (MSTR / CTO / COO / CVO all registered
within seconds of each other; the `~Z` group and all six `0.8.0_AE` lanes went stale minutes prior).

---

## 1. Startup — what was actually measured, not assumed

- **Cygwin-flavored harness.** `/cygdrive/c` resolves, `/c/` does not. Captured `TRUE_RC` in-stdout
  on every Bash call (the rc-corruption class; every call reports "Exit code 1" with a trailing
  `claude-*-cwd` stderr line).
- **Zero `inbox-watch.sh` processes existed at startup** — no orphan, so the reap decision never
  arose. I still ran the PID discriminator before touching registration rather than inferring from
  "I am a fresh session": registered PID **16096 was not in the process table**, so the serial was a
  dead predecessor's leftover, not a live peer. Registered at PID 28724.
- **Monitor armed `bf0p9jy5g`**, confirmed `running` via `TaskOutput` — and then confirmed a second,
  stronger way when it **delivered a live message from CVO at 1306Z**. A `running` status observes a
  consumer; a delivered message observes the whole path.
- LD-0290 session-serial file written. Zero crons armed. `CronList` empty.

**A.3 PATH denominator: 4 of 92 comp-tools resolve bare.** Everything else needs an explicit
`.tools/` prefix. The probe prints the denominator now, which is why this is a number and not a
"PATH OK."

**A.2 audit-archive-invoker** returned one finding (baseline 68.3h stale + uncaptured tail). It
raced base COO's `a720ddaf53` baseline advance at 1259Z — mine ran at 1259:06Z. **Not recorded as a
defect**: I have not re-run it, and a finding that may have been resolved by a commit landing in the
same second is not evidence of anything yet.

---

## 2. The third surviving copy — fixed

`prompt.md:84` — my own Step-0 instruction — still mandated the hardcoded
`bash /c/Users/.../inbox-watch.sh`. This is the **third copy** of a defect fixed on 2026-07-25 in the
other two (`.claude/skills/watcher/SKILL.md` + `org/XXX.md`, `aef2840826`). It bit `1.0.0_SA_CTO~Z`
and `0.8.0_AE_CloudComp~E` on the 07-25 fleet respawn.

Fixed **prefix-agnostically** — a blind swap to `/cygdrive/c/` would have moved the breakage onto
MSYS/Git-Bash sessions, which have `/c/` and lack `/cygdrive/c/`.

>> **A retraction is only as dead as its last surviving copy — and the copy that outlived this fix
>> was the one an agent reads at Step 0, before it has done anything else.** A wrong prefix arms
>> nothing, returns a task id anyway, and leaves the session deaf while `register_agent`,
>> `check-inbox` and `get_agent_status` all read healthy. <<

---

## 3. A gate I nearly reported as broken, and the control that refuted me

Gate-1's enforce marker is present (ARMED), yet none of my estate-wide `grep -rn` calls this session
were denied or written to `org/mcp/comp-which-rail.log` (1 entry today, another agent's, before my
session). The available shape of that observation is "an armed rail silently failed to deny."

**I ran the positive control before reporting it** — a grep from the known hard-deny class
(`infra/aws/lambda/` for `aws_iam_role`). It **DENIED correctly**, with the full HUD routing message.

So the hook is live and firing in this session, and my `.md`-scoped greps under `org/`/`docs/`
simply are not in a denied class. **No finding.** Recorded because the near-miss is the point: the
report would have been confident, plausible, and wrong, and the only thing between it and the record
was one control that took ten seconds.

---

## 4. Re-attribution owed on `b38f05df50` — discharged here

`b38f05df50`'s body (mine, 07-25) asserts:

> *"it has now produced two separate 40h+ record-loss windows in one day: A CORRECT GATE WITH NO
> QUEUE IS A DROP, NOT A HOLD. The tilde-lane enumeration gap does not tell the blocked agent 'wait'
> -- it tells them 'no'."*

**The premise was false and `2.0.0_SA_COO~Z` retracted it** (`9163a18dc`, blast radius corrected to
four agents at `0bd2063ee`): it was never gate-blocked from `org/tier1_exec/2.0.0_SA_COO/**`.
`owned-paths-validate.py:83` carries a home-folder ownership rule permitting a `~lane` against its
base's folder — 6× PASS / 0× BLOCK for that serial. The claim was a **behavioral assertion made from
a config read, never exercised** (Rule 22a's exact prohibition).

**Corrected attribution:** the 42h the MDPF synthesis sat untracked was **ordinary sediment — nobody
committed a file** — not a gate refusing a blocked agent with no queue. `0.8.0_AE_CloudComp~C`, whose
own case the false premise had strengthened, is the one who said so plainly.

The commit body is immutable and NEVER#7 forbids rebase, so this log is the carrier. **`b38f05df50`
must not be cited forward as evidence of a real tilde-lane enumeration gap.** The custody action it
records was still correct on ownership grounds alone; only the stated reason was invalid.

*The general principle ("a correct gate with no queue is a drop, not a hold") is untouched by this —
it was retracted as an INSTANCE, not as a doctrine. The stranded-memo population in my 07-25 log §8b
is a different and still-valid case.*

---

## 5. CI-R4 — delivered, unread, unanswered for four days

`3.0.0_SA_CVO` surfaced CI-R4 as possibly-undelivered. Grounded: **SENT is established** — the
07-24T1752Z message is in my `read/`, timestamp matching the landing. **READ is not, and is very
likely false** — the predecessor died without a closing log and never answered. A file in `read/`
observes the watcher, not the agent.

Four items now held, all in my architecture scope, all unactioned for four days:

1. **PRD §1/§3 names a cross-partner gate that was already removed** `@ed415e2682` (my own 07-09 fix,
   on Andrew's *"49 Financial should not hold up MDPF, that is nonsensical"*). §3 would dispatch a
   builder at a mechanism that no longer exists.
2. **13th item — `ROLL_SOURCE_UNREADABLE` is a misdiagnosis.** S3 returns 403-not-404 for a missing
   key when the caller lacks `ListBucket`, so a genuinely **ABSENT** block renders as a condition my
   own code documents as *"a CONFIG fault that will NEVER clear on its own"* — a self-clearing
   condition classified permanent, remedy pointing at IAM when the missing thing is a platinum block
   for 07-15. **Not designed this turn**: CVO measured it 07-24, four promotes and a sovereign
   verification have happened since, and a four-day-old measurement is not a current-state claim.
   Grounding against live state precedes any design.
3. **Row 4 cannot pass while a spine/driver exists** — §2.1's "channels are the unit" and `:520`'s
   spine/driver cannot both be true. A contradiction inside my own PRD.
4. **P2 — 12 closure rows, none for "independence stays true tomorrow."** A one-time exercise
   verifies a state and installs no control (TRIGGER_LAYER shape).

ACKed to CVO at 1307Z with the three-clock answer and an instruction not to close CI-R4 on the ACK.

---

## 6. Three sovereign-gated deploy holds — NOT stranded legs

`.open_deploys` holds three entries. All read `HELD-SOVEREIGN-GATED` with **L1–L3 closed (code
landed and activated) and only the final verify leg open** — a deliberate hold, not a half-landed
deploy, so NEVER#6 is not in play.

Their mtimes read 07-24 (a nudge); their **actual ages are 19–21 days**:

| Hold | Age | Open leg | Waiting on |
|---|---|---|---|
| `scty-premcp-p1-layer2-phase1-readonly-scope` | 21d | L4 live-cert | **Andrew/IT interactive MS login** to provision a read-only-tier MS identity token |
| `freshguard-leg5-v2-parity-drift` | 19d | L3/L4 fixtures | **Andrew** to provision a read-only GitHub PAT in secret `github-token-6FYoJ6` |
| `freshguard-leg4-writer-wiring-finish` | 19d | L4 verify | an **observation** under criterion v4 ("a verdict requires an observation") — possibly satisfiable now |

The first two are pure sovereign asks that have been sitting three weeks. The third may be closable
by observation and is worth a look before it is counted as blocked on Andrew.

---

## 7. Compiler Tools

| Tool | Result |
|---|---|
| Gate-1 rail (`comp-tool-hud`) | **Exercised as a positive control** — an `infra/aws/lambda/` grep DENIED correctly with the full routing message, refuting my own candidate finding in §3. |
| A.3 comp-tool PATH probe | 4 of 92 resolve bare; denominator printed, not a boolean. |
| `audit-archive-invoker` | 1 finding, raced a same-second baseline advance; not recorded as a defect. |

No `comp-*` query tool was run for estate traversal this session: the work was startup reconciliation
over `org/` records, git history and the inbox — none of which the graph tools index — and the two
substantive threads (CI-R4, the re-attribution) were grounded on source, commit bodies and live
process state. Raw `git`/`grep`/`python` used for that grounding is stage-2 verification per the
standing two-stage rule. **The comp-rail's own denial in §3 is the session's load-bearing tool
result**, which is the correct ratio for a startup pass.

---

## 8. Open at session end

- **13th item** — ground the 403/404 `ListBucket` path against live state, then design. CVO verifies.
- **MDPF_CHANNEL_INDEPENDENCE PRD** — §1/§3 correction + the §2.1-vs-`:520` contradiction.
- **MDPF gold→served publish is MANUAL/UNSCHEDULED** (`@878e9bcc67`) — NEVER#4 shape currently
  carried in a postmortem; ruled to become a gated item, not yet placed.
- **`0.8.0_AE_CloudComp~C`** — BLOCKED-ON-RULING on 3 comp-which MISSes, awaiting `1.0.0_SA_CTO~Z`,
  **which is now dead**. The block has no live owner and falls to me if ~C respawns.
- **Two sovereign asks at Andrew**, 19–21 days old (§6).
