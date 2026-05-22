# `org/tier0` — The Tier-0 Control Plane

Home of `0.0.0_AB_MSTR`, the autonomous principal-proxy. This README is the
operational map. It is a **guide**, not an authority — the binding documents are
the three law files below and the Constitution. If this README and a law file
disagree, the law file wins.

---

## Layout

```
org/tier0/
  CONSTITUTION.md     14 articles; fixed operating law.        [LAW — Andrew-only]
  STAKES_MATRIX.md    the S0–S4 autonomy dial.                 [LAW — Andrew-only]
  DIRECTIVES.md       the active mandate.                      [LAW — Andrew-only]
  README.md           this map.                                [MSTR]
  ledger/             Decision Ledger — one file per decision (LD-NNNN).   [MSTR]
  cycles/             operating-cycle records (CY-NNNN).                   [MSTR]
  ratifications/      S3 / operational-S4 verdicts (RT-NNNN).   [CVO / Andrew]
  audit/              the enforcement-hook audit log.
```

Ownership is enforced by `.owned-paths.yaml`: the three law files are
`TIER0_LAW` (no agent may commit them — Andrew-only); `ledger/`, `cycles/`,
`reviews/` are `TIER0_MSTR`; `ratifications/` is `TIER0_RATIFY` (CVO).

## How the pieces connect

A `/govern` operating cycle (**`CY-NNNN`**) reads the three law docs, scans the
fabric, and produces decisions. Every decision that is a *commitment* (stakes
class S1+) is one Decision Ledger entry (**`LD-NNNN`**), written **before** it
propagates — Constitution Article V. A gated decision (S3 / S4) produces a
ratification request; its verdict is recorded as **`RT-NNNN`**, which flips the
`LD` entry to `status: ratified`. `/mstr_review` walks all of it since the last
review flag.

## ID schemes — distinct prefixes, never confused

| Prefix | Artifact | Lives in |
|---|---|---|
| `D-NNN`   | directive        | `DIRECTIVES.md` |
| `LD-NNNN` | ledger decision  | `ledger/` |
| `CY-NNNN` | operating cycle  | `cycles/` |
| `RT-NNNN` | ratification     | `ratifications/` |

A `directive_ref` (`D-`) can never be misread as a decision (`LD-`).

## The Decision Ledger entry

One Markdown file per decision — `ledger/LD-NNNN.md` — so each decision is a
single diffable git unit. **S0 actions need no entry; S1+ require one.** The
**authoritative schema is the `STAKES_MATRIX.md` appendix** (29 fields). Fill
from `ledger/_TEMPLATE.md`. The `decision_id` is monotonic — take max+1.

### `decision_type` — the closed enum (Constitution Article II is authoritative)

Every S1+ entry names exactly one:

`directive_execution` · `directive_decomposition` · `directive_conflict_resolution`
· `directive_risk_reduction` · `clarification_request` · `escalation` · `halt`
· `amendment_proposal` · `bypass_exception`

Coverage notes (so the enum stays stable without amendment): a **ratification
request** is an `escalation`; **(re)prioritizing or (re)sequencing** directive
work is `directive_decomposition`; producing a **drift review** is not a decision
type at all — a review is a *record*, integrity-checked by the hook, not a
strategic action. An action that fits **no** type, or cites no Directive, is by
definition a **new goal** → `S4`, `proposed`, surfaced to Andrew.

## Enforcement — and its honest scope

The pre-commit hook `.tools/git-hooks/mstr-ledger-check.sh` makes Article V
structural. It runs **two checks**:

1. **Record integrity (universal).** Any commit, by any agent, that changes a
   `LD-*` / `CY-*` / `RT-*` file has that file schema-validated. A malformed or
   internally inconsistent Tier-0 record is rejected — including a false or
   incomplete cycle record.
2. **Strategic-action ledger requirement (MSTR-scoped).** A `0.0.0_AB_MSTR`
   commit that touches any path *outside* `ledger/` `cycles/` `reviews/`
   `ratifications/` must carry a valid `LD-NNNN` — included in the commit or
   named in a `Ledger: LD-NNNN` trailer. If that `LD` is S3/S4 it must be
   `status: ratified` or the commit is blocked.

> **Scope, stated plainly.** This hook structurally governs MSTR's **git
> commits**. It does **not**, by itself, govern non-git side effects — MCP
> messages, tool calls, scheduling. The git hook is *one* enforcement point, not
> the entire regime.
>
> **Companion principle.** Any MSTR-capable tool that can create external,
> destructive, monetary, or irreversible side effects must check the same
> ledger / ratification state before executing. Structural enforcement of
> non-git actions — the `/govern` skill's own classify-and-ledger-before-acting
> discipline, plus PreToolUse hooks on side-effecting tools — is a Phase 3
> deliverable, not a claim Phase 2 makes.

## Audit

The hook writes every verdict to `audit/ledger-hook-audit.log`. A git-tracked
file cannot be made truly append-only by git — so the integrity guarantee is
**git history itself**, and `/mstr_review` is required to walk the audit log and
flag any non-append edit (a deletion or rewrite is a finding).
