# CVO — **F-004 pass 2: NEVER#7.** I ran the banned operation. **It executed. HEAD was rewritten.** Three of four enforcement cells are open — and the rule with an incident behind it is the least enforced NEVER in CLAUDE.md.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~04:14–04:22Z · **Agent:** 3.0.0_SA_CVO
**F-004 (MSTR, assigned to me):** *"every rule that ASSERTS a safety property without naming the gate that enforces it, and every gate whose failure mode has never been exercised."*
**Method:** the negative control for a rule — **disobey it in a throwaway tree and see whether anything stops you.** Scratch repos only; no Opal remote, no shared branch, nothing that can be harmed.

---

## The claim under test

> **NEVER#7:** *"NEVER rebase — **not `git rebase`, not `git pull --rebase`** — on any shared branch (CLOUD/DEV/PROD)…
> **Gate: headmove guard (ADHC_OWNPTH.010; `pull --rebase` extension pending).**"*
> Incident cited inline: *"Andrew-direct 2026-06-12, DT incident — rebase 'succeeded' only because the commits
> happened not to overlap."*

**This rule has a real incident behind it, an Andrew directive, and a named gate.**

## Exercised

    the git() shadow is ACTIVE in a Claude Code Bash shell:   `type git` -> "git is a function"
    the real guard is .tools/git-hooks/headmove-guard.sh (245 lines), sourced from ~/.bashrc
        mentions rebase 9 | reset 14 | amend 8 | pull 0 | push 0

**POSITIVE CONTROL** — scratch repo, 2 commits, `git rebase HEAD~1`:

    rc=1   "ABORTED: destructive rebase would discard/rewrite 1 local commit(s)"
    => BLOCKED. The guard is real and it fires.

**THE TEST** — scratch repo + scratch bare upstream, **real divergence**, `git pull --rebase`:

    rc=0   "From .../up  cd6d3ce..99016ea  master -> origin/master"
           "Rebasing (1/1)Successfully rebased and updated refs/heads/master."
    HEAD before 166ec3ff   ->   HEAD after 6c46599b
    => *** THE REBASE EXECUTED. HEAD WAS REWRITTEN. The guard never fired. ***

**THE SECOND SHELL** — `Get-Command git` under the PowerShell tool:

    CommandType : Application      Source : C:\Program Files\Git\bin\git.exe
    => the git() shadow DOES NOT EXIST in PowerShell. It is a bash function; PowerShell never sources ~/.bashrc.

## The enforcement matrix — 3 of 4 cells open

| operation | Bash tool | PowerShell tool | `permissions.deny` |
|---|---|---|---|
| `git rebase` | **BLOCKED** (exercised) | **UNGATED** | **none — 0 rules** |
| `git pull --rebase` | **UNGATED** (exercised, HEAD rewritten) | **UNGATED** | **none — 0 rules** |

For contrast, measured from `.claude/settings.json`:

    deny rules mentioning 'rebase'       : 0    []
    deny rules mentioning 'reset --hard' : 2    [Bash(...), PowerShell(...)]
    deny rules mentioning 'push --force' : 2    [Bash(...), PowerShell(...)]

> **`reset --hard` and `push --force` are not NEVER rules — they sit in the "human confirmation required" list —
> and both carry two-shell deny twins. `rebase`, which IS a NEVER rule, with a named gate and a cited incident,
> carries none.**
>
> **The rule with an incident behind it is the least enforced NEVER in CLAUDE.md.**

## And the one gated cell is the one nobody types

CLAUDE.md's own remediation for a rejected push is *"`git pull` (merge) then re-push."* An agent reaching for
reconciliation reaches for **`git pull`**, not `git rebase`. **The single blocked cell is the invocation an agent is
least likely to use; the idiomatic one is open.** The rule's parenthetical — *"`pull --rebase` extension pending"* —
has been pending across the incident it was written for.

## Residual vector nobody has named

**`git config pull.rebase true` makes a bare `git pull` rebase.** Neither the guard (which inspects `$sub` and
`$@`) nor any argv-reading shim can see that from the command line. A complete control must read
`git config pull.rebase` / `branch.<name>.rebase`, or set `pull.rebase=false` at the repo level and gate the config
itself. **Recorded as a residual, not a finding — I have not exercised it.**

## Recommendation (verifier is not do-er; CTO's arch ruling, DT/AE build)

1. **Add `pull` to the guard's subcommand `case`** — block on `--rebase` / `-r`, and on a `pull.rebase` config that
   makes a bare `pull` destructive.
2. **Cover the second shell.** A bash `git()` shadow cannot. **A `git` shim earlier on PATH sees `argv` in both
   shells** — the identical architecture I recommended for the bare-`terraform apply` path, and MSTR routed. **One
   mechanism, two NEVER rules.** A `permissions.deny` text rule would work in neither: MSTR established it fires on
   mentions, so `deny Bash(*git rebase*)` would refuse every commit message and PRD that discusses rebasing —
   including this one.
3. Until it lands, **NEVER#7 must not read as gated.** State what is enforced: *"`git rebase` is blocked in
   Bash-tool shells only; `git pull --rebase` and all PowerShell paths are unenforced."*

**Do NOT weaken the rule to match its enforcement** — CTO's NEVER#1 ruling, verbatim. *Fix the gate.*

## grounding

- **exercised:** `git rebase HEAD~1` in a scratch repo → ABORTED by the guard (positive control);
  `git pull --rebase` in a scratch repo with a scratch bare upstream and real divergence → **rc=0, HEAD rewritten**;
  `Get-Command git` under PowerShell → `Application`
- **applied:** `~/.bashrc` sentinel block; `.tools/git-hooks/headmove-guard.sh` (245 lines, `pull` ×0);
  `.claude/settings.json permissions.deny` (0 rebase rules; 2+2 twins for `reset --hard` / `push --force`)
- **safety:** every write occurred in `scratchpad/` throwaway repos. **No Opal remote, no shared branch, no Opal
  history touched.** The one destructive act — a HEAD rewrite — happened to a two-commit repo I created for the
  purpose and deleted.
- **NOT established:** the `pull.rebase=true` config vector (**residual, unexercised**); whether any agent has ever
  run `git pull --rebase` against CLOUD (**no oracle: a rebase that does not conflict leaves no trace, which is the
  DT incident's own lesson**)

## What you should have asked but did not

**"How would we know if it had already happened?"**

The DT incident is in CLAUDE.md because a rebase *"succeeded only because the commits happened not to overlap."*
That is the whole hazard: **a non-conflicting rebase on a shared branch is silent.** It rewrites history, pushes
clean, and leaves an artifact indistinguishable from an honest merge.

So the gate is not a convenience. **It is the only detector we have**, because after the fact there is nothing to
detect. And for the operation the rule names *first* — `git pull --rebase` — the gate has never existed, in either
shell, since the day the rule was written to stop it.

We have spent this night proving that instruments cannot audit their own completeness. **NEVER#7 is worse: it has no
instrument at all, and its subject matter is specifically the class of event that erases its own evidence.**

— 3.0.0_SA_CVO
