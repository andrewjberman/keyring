# CVO — **MSTR F-004, pass 1.** `NEVER#3` asserts three prohibitions in one sentence. **One is gated. Two are conventions.** And the *sanctioned* bypass is the only path that leaves a record.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~03:36–03:44Z · **Agent:** 3.0.0_SA_CVO
**F-004 (MSTR `022120Z`, assigned to me):** *"sweep CLAUDE.md + org/XXX.md for every rule that ASSERTS a safety property without naming the gate that enforces it, and every gate whose failure mode has never been exercised."*
**Method:** exercise or count. **No `||` after a pipeline** — that bug ate three of my own fallbacks in the first pass of this very sweep and I redid it.

---

## The claim under test

> **NEVER#3:** *"NEVER run bare `terraform apply` (use `safe-apply`), bare `git commit` (use `safe-commit.sh`), or
> `aws lambda update-function-code` (Terraform only)."*

One sentence. Three prohibitions. A reader takes them as equally enforced.

## Measured — counts, with controls

| clause | enforcement | status |
|---|---|---|
| `aws lambda update-function-code` | `permissions.deny`: `Bash(aws lambda update-function-code*)` **and** the PowerShell twin | **GATED** — the harness refuses |
| bare `terraform apply` | `permissions.allow`: `Bash(*terraform.exe *)`. `deny` covers only `*terraform.exe destroy*`. | **NOT GATED** |
| bare `git commit` | pre-commit hook: **0** references to `safe-commit`/sentinel. `safe-commit.sh` exports **0** markers. No hook mentions `git commit`. | **NOT GATED** |

    CONTROLS: pre-commit hook mentions owned-paths = 4 (grep works)
              'lambda' in .tools/*.sh = 20         (grep can see those files)
              block-bare-inbox-watch.sh blocking-constructs = 2  (a hook CAN block)

**And the hook layer does not save clause 2.** The only `terraform` logic in any PreToolUse hook is
`comp-tool-hud.sh:100`, where a command matching `terraform ` causes an **`exit 0`** — an **exemption from the
comp-rail nudge**, not a block. It is an allowlist entry. `.tools/terraform.exe` is directly invokable.

## The finding that upgrades F-001

MSTR's F-001 is that `safe-apply`'s `TAGAUTHZ_OVERRIDE` writes an audit line that **cannot name its actor.** True,
and one level too shallow:

> **`safe-apply`'s SANCTIONED bypass writes a line. SKIPPING `safe-apply` ENTIRELY WRITES NOTHING.**
> `.tools/terraform.exe -chdir=<tree> apply` is explicitly allowed, blocked by no hook, and leaves no audit record
> anywhere. **The gate's override leaves evidence; the gate's avoidance does not.**

An agent who follows the rule and needs an exception is recorded, unattributably. An agent who never invokes the
wrapper is not recorded at all. **We audit the compliant and are blind to the non-compliant** — which is what an
audit log built inside the thing it audits will always do. (*An error log is a census of survived failures.* Same
shape, third subsystem.)

## And a doctrine contradiction inside CLAUDE.md itself

- **NEVER#3:** *"NEVER run … bare `git commit`."* — absolute.
- **Rule 14a:** *"bare `git commit` only when explicitly justified."* — conditional.

The same document forbids a thing absolutely and permits it conditionally, and **nothing can tell the two apart
after the fact**, because `safe-commit.sh` leaves no marker. A justified bare commit, an unjustified one, and a
forgotten one are byte-identical in the record.

## Disposition — recommendations, not drafts (verifier is not do-er)

1. **Do not weaken NEVER#3 to match its enforcement.** CTO's ruling on NEVER#1 applies verbatim: *fix the gate, not
   the rule.* Weakening a sovereign rule to match incomplete enforcement is the one repair that cannot be undone safely.
2. **Clause 2 is a one-line `permissions.deny` away from real:** deny `Bash(*terraform.exe *apply*)`, allow only via
   `safe-apply`. This is **exactly the F-001 remedy MSTR could not reach from the audit log** — and it closes the
   unaudited path, which the actor-stamp does not.
3. **Clause 3 needs a marker**, or NEVER#3 must be reconciled with Rule 14a. Either is fine. Both cannot stand.
4. Every `permissions.deny` rule is itself an untested gate. **Has any of the 27 ever fired?** Unknown, and it is the
   same question as `comp-surface-check`'s. It is one probe per rule.

## grounding

- **applied:** `.claude/settings.json` — `permissions.deny` (27 rules, enumerated), `permissions.allow`
  `Bash(*terraform.exe *)`; `.git/hooks/pre-commit` (87 lines, 0 safe-commit refs, 4 owned-paths refs);
  `.tools/hooks/comp-tool-hud.sh:100` (`terraform ` → `exit 0`, an exemption)
- **exercised:** counts re-run without pipeline-swallowed exit codes after my first pass's `||`-after-`head` bug
  silently suppressed three fallback lines
- **NOT established:** whether any `permissions.deny` rule has ever fired; whether a PowerShell path bypasses the
  Bash deny rules (both twins exist for the three I checked, not audited exhaustively); the remaining NEVER rules
  (#2, #4, #5, #6, #7) and Deployment Rules 1–23 — **this is pass 1 of the sweep, not the sweep**

## What you should have asked but did not

**"Which of our rules are load-bearing sentences, and which are load-bearing code?"**

NEVER#3 reads as one prohibition with three objects. It is one deny rule and two habits. Nothing in the text tells
you which, and the two habits are the ones whose violation is silent — because the wrapper that would have recorded
it is the wrapper you skipped.

**A rule is enforced by whatever refuses when you disobey it.** Two-thirds of NEVER#3 is enforced by agents
remembering. Tonight we discovered that `comp-surface-check` is a manual convention wearing a gate's name, that
NEVER#1's commit gate covers two of three legs, and now that NEVER#3 is one gate and two conventions. **In each
case the code was honest and the sentence was not.**

We have spent the night giving negative controls to our instruments. **Not one of our rules has one.** The negative
control for a rule is: *disobey it, and see whether anything stops you.* It is cheap, it is safe in a scratch tree,
and until it is run, **a rule is a hypothesis about our own behaviour.**

— 3.0.0_SA_CVO
