# CVO — TO-1: the telemetry hook, source-read AND exercised. `/freeform` falsified. `seq` is placement-dependent, not self-blind.

**archetype:** DIAGNOSE

**Date:** 2026-07-10 ~00:57–01:11Z · **Agent:** 3.0.0_SA_CVO
**Trigger:** CTO `235553Z` — PRD accepted, P0 reordered, *"TO-1 (source-read the hook) precedes both, and it is a read, not a fix."*
**Scope:** fabric instrumentation. No 49F path touched. No vendor API called. Read + one isolated-cwd exercise.

---

## 1. The ruling I was handed rested on a mechanism nobody had grounded

CTO reordered my P0 with two arguments. Only one of them was grounded, and I said so **before** reading the hook:

- **GROUNDED (and sufficient):** *"Build the second instrument first — it works no matter what the first one does."*
  Robustness-under-uncertainty. Needs no mechanism.
- **UNGROUNDED:** *"A counter minted inside the lossy component is silent about its own losses … `max(seq) - count`
  reads **zero**. It would be the thirty-eighth vacuous control."* A **mechanism claim** (CLAUDE.md Rule 22),
  presupposing both that the hook is the dropper and that `seq` would be minted inside it. CTO named the gap in the
  same message: *"seq is worthless until we know whether the hook is the dropper."*

A hypothesis cannot authorize a ruling. So I executed TO-1.

## 2. What the hook actually is

`.tools/hooks/post-tool-telemetry.sh` is **diff-clean against canonical** `org/mcp/hooks/post-tool-telemetry.sh` —
the file I read is the file that runs. (`.tools/` copy is tracked-and-modified vs HEAD; both working-tree copies agree.)

**It is not atomically lossy. It has a safe prologue and a lossy body:**

    :15  set -euo pipefail
    :17  HOOK_INPUT="$(cat)"      <-- nothing above this line can fail silently
    :19-172                        <-- EVERY silent-death path lives below it

## 3. EXERCISE — the decisive test (isolated scratch cwd, real hook, real jq, prod untouched)

Injected a `seq` at **line 18** — before jq, before the freeform check, before `date`/`tonumber`; fail-open, own
append-only file. Fired 7 calls: 3 valid, 2 malformed-stdin, 2 under a live freeform marker.

| | |
|---|---|
| tool calls actually made | **7** |
| prologue `seq` entries | **7** |
| telemetry records written | **3** |
| `hook_errors.log` lines | **0** |
| `max(seq) − count` | **4 — all drops DETECTED** |

**CTO's mechanism claim is REFUTED.** A prologue-minted `seq` catches every in-hook loss — including the freeform
standdown, which writes *literally nothing*. It is blind to exactly **one** class: the hook never being invoked.

**`seq` is therefore PLACEMENT-DEPENDENT, not worthless.** Mint it in the body (inside the `jq -nc` at `:137` — where
a reasonable engineer puts it) and CTO is right: self-blind, vacuous. Mint it at `:18` and it is a real instrument.
**The PRD must specify the LINE, not the feature.** "Add a `seq`" under-specifies onto the vacuous side by default.

**CTO's CONCLUSION survives** — on the robustness limb alone. The one class a prologue `seq` cannot see (non-invocation)
is exactly the class I could not eliminate for COO's window. Only a cross-oracle reconciler catches it. P0b stands.

## 4. The dropper: narrowed 6 → 2. `/freeform` FALSIFIED.

**ELIMINATED** — all three *log before exiting*, and `hook_errors.log` holds **zero 2026-07-09 entries** (511 lines,
last `2026-07-08T18:26:51Z`):
`NO_JQ` starvation `:43-67` · `JSONL_WRITE_FAIL` `:156-159` · unresolved-serial WARN `:113-117`.

**FALSIFIED by a second oracle** — the freeform standdown `:84-93`. `freeform.sh:30/:36` appends `FREEFORM-ARM`/`-OFF`
to `org/mcp/comp-tool-hud.log`. **The entire population of freeform events, ever, is two lines:**
`2026-06-18T19:39:54Z ARM` / `19:40:06Z OFF`, `sid=SID-1` — a literal placeholder, 12 seconds, matching no real session.
Zero on 07-09. Zero for COO's `81c1c799`. **Freeform has never been armed for a real session.**

> I found this branch first. It fit COO's seven-minute total blackout beautifully. **It is not the cause.** The only
> reason this is not the COTETL error with new nouns is that I went looking for the second oracle instead of asserting
> the first. A mechanism that *explains* the symptom is not thereby the mechanism that *caused* it.

**STILL LIVE (both write nothing, log nothing):**
- **(a) `set -euo pipefail` death.** EXERCISED: malformed stdin → jq parse error at `:71` → `rc=5`, zero jsonl, zero
  error-log. Silent and total. But **per-call**, not windowed — it does not obviously produce a 7-minute contiguous blackout.
- **(b) hook NON-INVOCATION.** Fits the windowed+total signature. **NOT ESTABLISHED** — I have no oracle for it. That
  absence is itself the argument for P0b.

**COO's 22:17:22–22:24:15Z window remains MECHANISM UNDETERMINED.** I narrowed it from six candidates to two. I did
not close it, and I will not write that I did.

## 5. The finding in neither document: `/freeform` is a loaded gun

The skill doc and `freeform.sh:4-9` both state freeform suspends *"ONLY the comp-tool RAIL"* and that *"SAFETY gates
are UNAFFECTED."* **That is false as built.** `post-tool-telemetry.sh:84-93` exits 0 on a live marker. Telemetry is
not the comp rail.

**An agent under `/freeform` can call `ycharts_*` and no telemetry record is written.** The vendor-egress instrument
has an Andrew-authorized, time-boxed, **silent** blind spot — and freeform-silence is byte-identical to
instrument-failure-silence. That is the PRD's founding sentence occurring *inside the subject of the PRD*.

It has never fired in production, so it corrupts nothing today — and, checked against my own headline number:
**the 22.8% is NOT contaminated by designed standdowns** (zero real windows; I expected contamination and found none,
so the number stands as measured). It is a loaded gun with the safety off, and it is the concrete mechanism behind
CTO's *"do not audit the prohibition, ENFORCE it."*

**P1 recommendation (CTO, PRD):** freeform must emit a **standdown sentinel** (`kind:"standdown"`, arm/expire
bracketing), never silence. *An instrument that goes quiet on purpose must say so, or it has taught its reader that
quiet means nothing happened.*

**P2, same file:** empty stdin writes `tool_name:""` — not `_unknown_` — because jq on empty input emits nothing, so
`// "_unknown_"` at `:120` never evaluates. A row that exists and names no tool.

## grounding

- **desired:** `post-tool-telemetry.sh` `:15,:17,:71,:84-93,:120,:137,:154-159`; `freeform.sh:29-37`; `comp-tool-hud.sh:42-47`
- **applied:** installed == canonical (diff-clean); `hook_errors.log` 511 lines, **zero** dated 2026-07-09;
  `comp-tool-hud.log` 11,371 lines, **exactly 2** `FREEFORM-*` lines, both `sid=SID-1`, both 2026-06-18
- **exercised:** 7 synthetic calls through the REAL hook, isolated cwd → seq 7 / records 3 / errorlog 0 / drops 4;
  malformed stdin → `rc=5`, nothing written, nothing logged
- **NOT established:** the actual cause of COO's 22:17–22:24Z window (2 candidates, both silent); whether Claude Code
  surfaces a nonzero hook `rc` anywhere readable; the ferry-message fraction still inflating the 22.8%

## What you should have asked but did not

**"What does our error log prove?"**

In that run the hook dropped **4 of 7** calls and `hook_errors.log` recorded **zero lines**. It was not wrong. It was
**clean**. Every path that logs is a path that *survived*; the paths that die cannot write. **An error log is a census
of survived failures — structurally incapable of counting the fatal ones.**

I eliminated three candidate mechanisms tonight on the strength of *"hook_errors.log has zero 07-09 entries."* That
inference is sound **only because I separately proved those three paths log before exiting.** Had I reasoned from the
silence alone, I would have concluded the hook was healthy on the night it dropped a third of the fabric's sends —
which is, precisely and exactly, the sentence this whole PRD exists to prevent, committed by the person auditing it.

COO ruled ninety minutes ago that a usage log may never ground a WORKS verdict, because *"a tool that has always been
wrong produces a flawless usage log."* I arrived at the same law from the other end, in a different instrument, with
an exercised demonstration, and neither of us was reading the other. When two independent verifiers converge on the
same law inside one night, it is not a telemetry rule. It is the general one:

> **No instrument may ground a claim about its own completeness.** Not the error log. Not the usage log. Not `seq`.
> Not the reconciler.

— 3.0.0_SA_CVO
