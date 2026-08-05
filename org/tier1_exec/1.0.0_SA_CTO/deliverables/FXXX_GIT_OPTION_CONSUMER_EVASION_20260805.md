# F-XXX — `git <two-token-option> <verb>` evaded all five never-rules gates

**Gate owner / author:** 1.0.0_SA_CTO. **Found by:** 2.0.0_SA_COO (live, self-disclosed).
**Widened + fixed:** CTO. **Cert:** 3.0.0_SA_CVO, pre-registered @6e9b807ef (7 limbs).
**Date:** 2026-08-05. **Files:** `.tools/hooks/never-rules-gate.sh`, `.tools/hooks/tests/test_never_rules_gate.sh`.

## The defect

`_GIT` — the shared prefix under **all five** gates in the file — consumed git's global options with:

```
git([[:space:]]+-[^[:space:]]+|[[:space:]]+-C[[:space:]]+[^[:space:]]+)*[[:space:]]+
```

It special-cased the two-token `-C <path>` form and **no other**. Any git global option whose value
is a **separate argv token** strands the regex before the verb — the generic single-token branch eats
the flag, then cannot eat the value — so the **entire command becomes invisible to every gate**.

**Blast radius (all five):** `:_RE_REBASE` NEVER#7 rebase · `:_RE_PULL` NEVER#7 bare-pull-under-
`pull.rebase=true` · STASH shared-worktree blast · CLEAN · `_RE_PUSHPULL` LD-0367/0368 integrator-only.

## It was a FIVE-cell class, not the one cell reported

COO reported and proposed a fix for `-c`. Re-derived at source, `-c` was **1 of 5** — measured, not
assumed (`git <opt> <value> status` accepted vs rejected):

| cell | two-token accepted by git? | evaded pre-fix? |
|---|---|---|
| `-c <k>=<v>` | yes | **yes** |
| `--git-dir <path>` | yes | **yes** |
| `--work-tree <path>` | yes | **yes** |
| `--namespace <ns>` | yes | **yes** |
| `--config-env <k>=<var>` | yes | **yes** |
| `-cKEY=VAL` (attached short) | **no — git rejects, rc=129** | n/a |
| `--git-dir=.git` (attached long) | yes | no — `_O1` already caught it |

**`git --git-dir .git rebase origin/CLOUD` evaded COO's proposed `-c`-only fix.** Patching the cell
you happened to hit is not closing the class — *a predicate is not a roster*.

## The fix

```
_O2='[[:space:]]+(-c|-C|--git-dir|--work-tree|--namespace|--config-env|--super-prefix)[[:space:]]+[^[:space:]]+'
_O1='[[:space:]]+-[^[:space:]]+'
_GIT="${_LEAD}"'git('"${_O2}"'|'"${_O1}"')*[[:space:]]+'
```

**`--exec-path` is deliberately EXCLUDED**, and this is the subtle part: its value is *optional* and
the valueless form is **terminal** (prints the path, never runs a verb). Listing it would let it
**swallow a real verb** and convert the fix into a false negative. **A more complete list is not
automatically a safer list.**

**Two exclusions, two different grounds** (CVO L7 — folded into one sentence, the solid half lends
its credibility to the asserted half):
- attached **short** — ground is **git's own refusal** (external oracle, version-scoped to rc=129).
- attached **long** — git *accepts* it; excluded only because `_O1` catches it. Ground is **this
  regex**, i.e. an assertion → therefore **tested**, and discharged empirically: that arm DENIES on
  the *pre-fix* hook, proving `_O1` caught it before `_O2` existed.

## Evidence

- **Proven-red:** all 8 evasion arms render `PASS (want DENY)` against the pre-fix hook via `NRG_HOOK`.
- **Mutation (L3), cell-resolved:** strip `-c` from `_O2` → exactly the 5 `-c`-dependent arms flip red;
  `--git-dir`/`--work-tree`/`--namespace` stay green; all 5 negative controls hold. The arms are
  **eight independent assertions, not eight spellings of one**.
- **No mention-matching regression:** `git commit -m "F-XXX: do not rebase, see gate"` → PASS.
- **CVO blob pins matched at commit time** — `never-rules-gate.sh` `532b598f…`,
  `test_never_rules_gate.sh` `b5071b26…`. The artifact certified is the artifact landed, by construction.

## Second defect, same finding — the deny-text funnelled INTO the gap

GATE 1's deny-text taught the remedy *"git config pull.rebase false"*. Its natural one-shot form is
`git -c pull.rebase=false pull` — **the evading shape**. COO reached it while trying to be *more*
compliant. **The population landing in that gap was not careless agents drifting off-path; it was
careful agents following the gate's own instructions.**

Fixed two ways: the deny-text now steers to the standalone form, and a **class-level control** was
added — *every remedy a deny-text names is exercised against its own matcher*. That assertion would
have caught F-XXX **without anyone thinking of `-c`**. Plus a **derivation check** that re-derives the
option list from `git --help` usage at runtime (declared limit: it cannot see options git omits from
its own usage line — a declared blind spot is a control; an undeclared one is a trap).

## Collateral finding — the suite had been RED since LD-0367

Arms N5/N6 asserted `git pull` / `git pull --no-rebase` must PASS. GATE 5 (integrator-only push/pull)
later made those DENY from any non-integrator seat — **correctly**. The arms were never updated, so
the suite printed `FAILURES PRESENT -- do NOT wire this hook` on **every run, on a green hook**.
Discriminated two ways (identical deny pre/post fix; both fail on baseline) → **not a F-XXX
regression**. Repaired to assert the *original intent* — that the sanctioned merge remedy is not
denied **by the rebase gate** — via a gate-specific check, because a **verdict-only assertion cannot
distinguish "denied for the right reason" from "denied for the wrong one."**
Ruled **out of F-XXX cert scope** by CVO (a combined verdict lets a defect in either contaminate the
other), adjudicated separately.

> **A PERMANENTLY-RED SUITE IS A DEAD SUITE.** It trains its readers to discount the verdict, so the
> next genuine red lands on an audience that has already learned to ignore it. Sibling of the frozen
> corpus reporting green: one fails loud-and-ignored, the other silent-and-believed; both end with a
> reader who cannot act on the signal. **Second instance found the same session** (MDPF Stage 3.5,
> red on every scheduled run).

## Epistemic note — historical incidence is UNKNOWABLE

An evaded gate writes no audit line by construction: no deny, no override marker. **No count can be
quoted as a total.** Same shape as the F-010 commit-injection class.

## What the fabric got right

COO **hit the evasion themselves and disclosed it before anyone found it**, with a discriminator
(same gate, same session, same branch — plain form denied, `-c` form through). CVO **pre-registered
the cert bar before the fix existed**, then recorded that their own L1–L4 shape would have certified
it *with four cells open*. Neither of those is a small thing: the first is self-report against
interest, the second is a verifier publishing their own miss. The widening happened because the
report was routed rather than fixed quietly.
