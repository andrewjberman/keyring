# {PROJECT_CODE} — {Project Name}
**PRD v{X.Y} — {author serial} — {YYYY-MM-DD}**

> Forward-only template (ADHC_COMPIL.003 / 2026-04-29). Existing PRDs are not
> required to backfill §5 Compiler Evidence; new PRDs (created on or after
> 2026-04-29) MUST. See `docs/architecture/PRD_AUTHORING_PROTOCOL.md`.

---

## §1 — Scope

Single-paragraph problem statement. Then:

- **In scope:** what this PRD authorizes
- **Out of scope:** what is deliberately excluded (cite the project that owns it, if any)
- **Non-goals:** desirable but not in this version

---

## §2 — Existing State

Snapshot of what is currently deployed/active relevant to the change. Cite
commit refs, S3 prefixes, Lambda names, portal components, dashboards. Do
NOT speculate — only state what is verifiably true today (the compiler
evidence in §5 is what makes "verifiably true" load-bearing).

---

## §3 — Architecture

End-state architecture. Diagrams or block lists. Identify every:

- New component (with target tag if it ships under a pipeline)
- Modified component (with current tag → target tag)
- Removed component (with deprecation/migration path)

Include data flow direction and gating dependencies.

---

## §4 — Component Specs

One subsection per component touched. Each spec has:

- **Purpose** — one sentence
- **IO contract** — inputs, outputs, schema, error shape
- **Downstream consumers** — what breaks if this changes (compiler-tool sourced)
- **Error cases** — explicit list of what callers must handle

This is the contract every TO will be checked against.

---

## §5 — Compiler Evidence (MANDATORY)

> **Required.** This section MUST be populated before TO decomposition begins.
> PRDs without compiler evidence cannot be handed to COO. See
> `docs/architecture/PRD_AUTHORING_PROTOCOL.md` for the full required-runs
> matrix and worked examples.

### 5.1 — Required runs by PRD type

Identify every PRD type this PRD touches and run every tool in the matching
row. A PRD that touches multiple types runs the union.

| If this PRD touches… | Required compiler runs |
|---|---|
| Gold script | `comp-pipescript io <script>` + `comp-blast <fn>` + `comp-platinum reverse <artifact>` |
| Portal component | `comp-routes trace <fn>` + `comp-cache collisions` + `comp-transform schema-check <Component>` |
| Lambda | `comp-iam service <lambda>` + `comp-routes trace <fn>` |
| EC2 service | `comp-iam service <ec2>` + EC2_MANIFEST.json check |
| New artifact claim | `comp-platinum reverse <artifact>` (must show producer exists) |
| Cross-firm portal | `comp-routes trace <fn>` for both firm scopes |

`comp-build` once at the start if the repo has changed since the last build.

### 5.2 — Evidence table

| Tool + command | Key output (excerpt) | Disposition |
|---|---|---|
| `comp-build` | (cache rebuilt YYYY-MM-DD HH:MMZ) | Cache fresh |
| `comp-pipescript io <gold_script>` | _(paste the COLUMN GAPS / PORTAL CONSUMERS / S3-DYNAMIC sections that informed the design)_ | Confirmed §3.X / Changed §4.Y |
| ... | ... | ... |

"Disposition" is one of: **Confirmed §X.Y** (output validated an assumption);
**Changed §X.Y** (output forced an edit to that section); **Surfaced new TO**
(output revealed a dependency that required adding/splitting a TO in §6).

Append one row to `org/compiler-tools-log.md` for each tool run, per the
standard logging protocol.

### 5.3 — Findings that updated this PRD

Bullet list of compiler-tool findings that triggered changes to §1-§4. Empty
list = "no changes; tools confirmed initial design." If empty, say so
explicitly — do not omit the subsection.

---

## §6 — TO Candidates

Numbered list of work units the COO will decompose into task orders. Each TO
sketch has:

- **Receiver** — agent serial (e.g., `0.4.0_DS_ClientPlatform~A`)
- **Scope** — files modified
- **`<compiler_tools_mandate>`** — three phases:
  - Phase 1 (before write): tools to confirm blast radius + dependencies
  - Phase 2 (before commit): tools to confirm change hasn't expanded blast radius
  - Phase 3 (after commit): tools to validate
  - Use the §5.1 matrix as the floor; add tool-specific runs as the work
    requires.
- **Acceptance criteria** — machine-checkable (artifact path + field-level
  asserts; not "code runs")
- **Gates** — dependencies on other TOs, wall-clock events, or external
  inputs
- **Effort estimate** — human-readable range

The COO copies the `<compiler_tools_mandate>` verbatim into the issued TO.

---

## §7 — Open Questions

Items needing Andrew's input or further investigation before TO decomposition.
These do NOT block PRD authoring; they block COO dispatch on specific TOs.

Format: numbered Q list with proposed-answer + decision-required-by-when.

---

## Appendices (optional)

A. Compiler tool raw output (full transcripts, if §5.2 excerpts are not enough)
B. Design alternatives considered (and why rejected)
C. Risk register
D. Cross-domain coordination — list of files / S3 keys shared with other
   active projects (sourced from `comp-pipescript overlap A B`)
