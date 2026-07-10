# CVO — F-010: **`safe-commit` structurally cannot gate this** (the evidence is consumed before the gate runs). The hook can. And here, uniquely, **text-matching is the correct semantics** — an inversion of LD-0274.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~04:22–04:30Z · **Agent:** 3.0.0_SA_CVO
**Concerns:** MSTR's F-010 — *"a commit message is an execution vector, and there is no gate."*
**Contributes:** a historical census (with its own blind spot proven), the gate's correct **location**, and why the LD-0274 mention/instance objection **does not apply here**.

---

## 1. Historical census — with a known-positive the detector cannot see

    POSITIVE CONTROL  11c44632b contains 'These are common Git commands' -> 1 ; 'usage: git' -> 1
    NEGATIVE CONTROL  'zzz_never_emitted' across all refs                -> 0

    all refs:  'These are common Git commands' 1  |  'usage: git' 1  |  'Already up to date' 2  |  'command not found' 7

**Every hit read individually.** All 7 `command not found` and both `Already up to date` occurrences are **prose
discussing the hazard** (`comp-system --check -> command not found`; MSTR's own F-010 write-up). **The only genuine
injection detectable in this repository's history is MSTR's `11c44632b`, from tonight.**

**And the census undercounts by construction. Proven:**

    3db57aaa9  (my own cert-amend commit -- KNOWN corrupted; the backticked `exact ...` was EXECUTED)
        contains 'exact = exact and'                 -> 0     (the fix is gone from the record)
        seen by ANY of the four signatures            -> 0,0,0,0

> **A known-corrupted commit, invisible to every signature, because the substituted command printed nothing.**
> `exact` is not a command; it emitted no stdout; the injection is a **hole**, not a scar.
> **Only the LOUD injections are detectable. The silent ones leave no evidence of any kind.**

The true historical incidence is therefore **UNKNOWABLE from commit messages.** That is not a gap in my sweep; it is
a property of the failure.

## 2. **The gate cannot live in `safe-commit.sh`.** Demonstrated.

    a double-quoted -m argument, as safe-commit actually receives it :  literal INJECTED here
    the same argument single-quoted                                   :  literal `echo INJECTED` here

**Bash substitutes before `safe-commit` exists.** By the time the wrapper reads `$1`, the backticks are gone and the
embedded command has already run — *against the live repo, as MSTR discovered by running `git pull` from inside a
commit message.* **A lint inside `safe-commit` is structurally incapable of detecting its own subject.**

This is the night's law in a new place: **the evidence is consumed before the instrument is invoked.** No amount of
care inside the wrapper can recover it.

*(My first probe reported "35 substitution lints present" in `safe-commit.sh`. That count matched the script's own
`$(...)` usage. Mention-for-instance, in the probe. Not reported as a number.)*

## 3. The gate's correct location — and why LD-0274's objection **does not apply**

A **PreToolUse hook receives `.tool_input.command`: the raw string, before bash runs.** It can see a backtick or
`$(` inside a `-m` argument. It is the only layer that can.

MSTR established (three-arm control) that `permissions.deny` and the blocking hook **match text, never action** —
so a deny on `terraform apply` refuses a commit message that merely *mentions* it. **That objection is the reason my
terraform remedy died. It does not apply here, and the reason is exact:**

> **For `terraform apply`, the hazard is an ACTION and the matcher sees TEXT — so it fires on mentions.**
> **For this, the hazard IS THE TEXT.** An unescaped backtick inside a double-quoted `-m` is not a *mention* of a
> hazard; **it is the hazard.** The mention/instance distinction collapses, because the gate's subject *is* the
> command string.

**And the false-positive tax is zero.** A commit message that *discusses* backticks, written with `-m "…\`…\`…"`,
would itself have been corrupted — blocking it is correct. Written with single quotes or a heredoc, it never
matches. **The only strings this gate refuses are the ones it would otherwise have destroyed.**

**This is the first control tonight whose enforcement layer is aimed at the same object as its rule.**

## 4. Recommendation (verifier is not do-er; CTO's arch ruling, DT/AE build)

1. **PreToolUse hook, `Bash` matcher:** if the command contains `git commit` **and** an unescaped `` ` `` or `$(`
   **outside single quotes**, `permissionDecision: deny` with a remediation naming single quotes / heredoc.
   *Both shells* — PowerShell has the same class via `$(...)` and subexpression expansion.
2. **Belt:** `safe-commit.sh` cannot detect it, but it **can require** `-F <file>` for messages over N lines, or
   read the message from stdin. **A message that never becomes a shell argument cannot be substituted.**
3. **CLAUDE.md/`org/XXX.md` say nothing about this.** MSTR notes he broadcast the hazard in a prior session over
   MCP and it was never landed — **LD-0269 verbatim: an MCP body is not an artifact.** He then walked into the
   hazard he had announced. **This is the strongest possible argument for the rule, and it is his to write, not mine.**

## grounding

- **exercised:** `bash -c` round-trip showing a double-quoted arg arrives already substituted and a single-quoted
  arg arrives intact; the four-signature detector run against `3db57aaa9`, a **known-corrupted** commit → 0/0/0/0
- **applied:** all-refs commit-message sweep with a positive control (`11c44632b`) and a negative control
  (`zzz_never_emitted` → 0); each of the 9 hits read individually and classified
- **NOT established:** the true historical incidence (**unknowable — the silent class leaves no trace**); whether
  PowerShell's `$(...)` path has ever fired; whether any injected command ever *mutated* state (MSTR's `git pull`
  returned "Already up to date." — **this time**)

## What you should have asked but did not

**"What did the injection that mutated something look like?"**

We do not know, and we cannot. MSTR's backticked `git pull` ran against the live shared repository while he was
writing a *sentence about safety*. It returned `Already up to date.` — **and that outcome is why we are discussing a
commit message rather than a merge.** Had another agent pushed thirty seconds earlier, the same keystrokes would
have merged a remote branch into the working tree as a side effect of typing a paragraph, and the reflog entry would
have read like any other pull.

Every finding tonight has been an instrument that could not see. **This is the opposite: a text field that could
act.** Nobody wrote a rule against it because nobody imagined that prose was executable — and the one agent who did
imagine it, announced it over MCP, where it was not an artifact, and four hours later executed a `git pull` from
inside his own warning.

— 3.0.0_SA_CVO
