# BRIEF — retired-tool reference cleanup (records only, no code)

**To:** AE CloudOps lane · **From:** `1.0.0_SA_CTO~B` · **Handed off by Andrew 2026-08-06.**
**⚠ SERIAL CHECK BEFORE ROUTING:** Andrew named *"0.8.0_AE_CloudOps"*. The serials that exist are
**`0.7.0_AE_CloudOps`** (+ `~A`, `~C`) and **`0.8.0_AE_CloudComp`**. Those are two different seats.
Confirm which one before delivering — a brief sent to a serial that does not exist is never read.

**Scope: DOCUMENTATION AND REGISTRY TEXT ONLY. No code, no infra, no deploy.**
**Evidence:** a citation-integrity sweep across 29 files — 212 raw hits, 99 in scope, **26 defects**
and **78 correctly-historical mentions** left alone. All 13 zero-hit files were positive-controlled,
so every zero is a real zero rather than a failed search.

---

## 1. THE FACTS THE RECORDS MUST NOW MATCH

- **`comp-surface-check` is RETIRED**, 2026-08-06, Andrew-direct. VERBATIM: *"I want
  comp-surface-check retired. i do not like that tool."* Confirmed four independent ways: the
  executable is gone; retirement commit `1a962886be` deletes it plus the GitHub workflow and portal
  pre-commit hook and strips it from `safe-commit.sh`/`CLAUDE.md`/`TOOL_MASTER.yaml`;
  `graph-call-manifest.yaml:50-62` carries its `retired_aliases:` row; `safe-commit.sh:454` records
  the gate removal. **The MP/benchmark/ADVI surfaces now carry NO automated commit-time guard — that
  is the accepted consequence of the ruling, not a gap to re-fill.**
- **Bare `pipescript` is a retired rc=2 stub.** Lineage: `pipescript` → `comp-semantic-estates` →
  **`comp-estate`**; the old names DO NOT RESOLVE.
- **`comp-pipescript` IS A DIFFERENT, LIVE TOOL.** It is NOT a synonym for `pipescript`.
  **Do not touch `comp-pipescript` references.** The sweep found 111 of them and correctly excluded
  every one; a cleanup that conflates them would break live routing.

---

## 2. THE CLASSIFICATION RULE — apply it to every hit before editing

**FIX IT** when the text tells an agent what to run, what a field's value IS, or what fires right
now: a present-tense copula (*is*, *gains*, *returns*, *polices*, *auto in safe-commit*), an
imperative, a machine-read config key, or a routing-table row.

**LEAVE IT ALONE** when it is a dated historical record, a past-tense finding, or part of a
retirement/rename declaration. Example of a mention that is CORRECT and must survive:
`NFRA_GCONTR_PRD.md:68` — *"comp-surface-check list (2026-06-15): 5 critical surfaces"*. That is
dated evidence of what was true then.

> **The `retired_aliases:` rows in `graph-call-manifest.yaml` are the POLICING MECHANISM, not
> defects. Do not delete them.**

**A record that correctly describes history is not a defect. Over-correcting history destroys the
evidence trail — and this estate has already ruled that deleting a decommission record is the same
class of loss as an un-ruled retirement.**

---

## 3. DEFECTS — HIGH (would misdirect an agent's action). Do these first.

| # | file:line | verbatim wrong text | correct fact |
|---|---|---|---|
| H1 | `org/modules/graph/critical-surfaces.yaml:144-146` | `commit_gate:` / `tool: comp-surface-check` / `SEV1: block-with-ack` / `SEV2: warn` | **A MACHINE-READ CONFIG KEY naming a deleted binary as the live blocking gate.** The sharpest item in the set. |
| H2 | `org/modules/graph/graph-call-manifest.yaml:33` | `comp-surface-check = D8 critical-surface commit-gate (polices critical-surfaces.yaml at commit, auto in safe-commit)` | Both clauses false. **Sits 17 lines above the same file's own retirement row — the routing surface contradicts itself.** |
| H3 | `docs/architecture/NFRA_GRAPHS.md:393-397` | `**CTO RULING — advisory->blocking flip (comp-surface-check, D8-AE Part A):** flip when ALL THREE hold ... Expected ~1-2 days — fast ramp.` | **A standing unexecuted directive, in a project whose status is `active`, telling a future agent to promote a DELETED tool to a hard block.** Highest action-misdirection. |
| H4 | `org/modules/graph/graph-call-manifest.yaml:723` | `...S3-key->comp-pipescript io/pipescript --resource; portal->comp-transform/comp-routes...` | **The comp-which ROUTER emitting the prohibited bare name — the router itself hands an agent an rc=2 command.** |
| H5 | `org/critical_paths/README.md:14-15` | `- \`SURFACE_ACK\` bypass (comp-surface-check) -> approval entry` | Declares a live writer contract; nothing writes `SURFACE_ACK` entries anymore. |
| H6 | `docs/architecture/NFRA_PIPESCRIPT_PRD.md:12` + `:43` | `**\`pipescript <name>\`** is that entry point...` / `\`pipescript news\` enumerates the 20 news sub-threads` | Present-tense entry-point claim + three concrete dead invocations. **This file carries NO rename note anywhere** — a propagation gap, unlike the manifest which got one. |

## 4. DEFECTS — MED

`NFRA_PIPESCRIPT_PRD.md` `:25`, `:50`, `:63`, `:69` — architecture-diagram line, executable example,
imperative build instruction ("Wire `pipescript <name>`"), and an acceptance criterion stated as live
behaviour.
`NFRA_GCONTR_PRD.md` `:18`, `:62`, `:64`, `:84`, `:85`, `:93`, and `:4`/`:75-79` — seven items:
present-state claims (*"**Today** it gates on FILE touches"*), forward build instructions
(*"`pipescript` **gains** `--contract`"*), acceptance criteria naming the retired binary as the
blocking mechanism, a live enforcement-ramp directive with a pending CTO action, and open task-order
assignments naming both retired tools as deliverables.
`org/projects/NFRA_GCONTR.json:30` — `"pipeline": "globgrph (Nessie/Iceberg) + comp-surface-check + pipescript"`
— **a machine-readable registry field composed of two retired names.**

> **CONTEXT THAT LOWERS URGENCY BUT NOT VALIDITY:** `NFRA_GCONTR` is **`suspended-indefinite`**
> (Andrew-direct 2026-07-20, *"Pause GCONTR we are not addressing htat"*). **Do NOT restart GCONTR
> work.** But the PRD does not say it is suspended, so an agent who opens it reads live instruction.
> **The cheapest correct fix for the seven GCONTR items may be ONE prominent SUSPENDED banner at the
> top of the PRD rather than seven line edits** — use judgement; that is a real option, not a
> shortcut.

## 5. DEFECTS — LOW

`NFRA_NERVES_PRD.md:45` (bare `pipescript` in a live node-source list) ·
`NFRA_COMPRAIL_HARDENING_BATCH.md:23` (lists retired `pipescript` beside live `comp-pipescript` as
currently-mandatory — the exact conflation this brief warns about, inside a Rule-21 enforcement doc) ·
`comp-tools.yaml:309` (hands the reader `pipescript news`; mitigated by the rename note at `:306`) ·
`critical-surfaces.yaml:129-130`, `:139`, `:48` (three present-tense claims that the retired gate is
actively watching surfaces — including `:48`, which assigns a real coverage leg to a tool that cannot
cover it, **converting a "recorded division" into an unrecorded gap**) ·
`graph-call-manifest.yaml:1335` (locates the live risk-reflex block by reference to a
`[surface-check]` block `safe-commit.sh` no longer emits).

## 6. SEPARATE CLASS — FROZEN COUNTS (fix only if cheap; do not let it delay §3)

*Measured directly 2026-08-06 by CTO~B (the sweep agent assigned to this was killed before producing
findings, so these are re-derived, not inherited).*

**LIVE TRUTH:** `comp-estate`'s own header reports **29 semantic verticals / 138 chains**, and
carries a dated vintage (`estate census 2026-07-30`) — the honest pattern.

| # | file:line | frozen text | status |
|---|---|---|---|
| F1 | `org/modules/graph/comp-tools.yaml:309` | *"25 named threads / 134 sub-threads / 169 lambdas"* | **STALE — 25 vs 29, 134 vs 138.** Apples-to-apples against the tool's own header. |
| F2 | `org/modules/graph/graph-call-manifest.yaml:710` | *"the COUNTS ARE THE RESOLVER'S, live via `--list` — 29 named … 138 … 188"* | **NAMES THE CORRECT PRINCIPLE AND FREEZES THE NUMBERS IN THE SAME SENTENCE.** Its 29/138 match today — **which makes it worse, not better.** |

> **A FROZEN NUMBER THAT IS CURRENTLY RIGHT IS INDISTINGUISHABLE FROM A LIVE ONE UNTIL THE DAY IT
> DRIFTS** — and it will drift exactly as F1 did. F1 *is* F2 a few months older.

**⚠ ONE COMPARISON DELIBERATELY NOT MADE.** F2 also carries a lambda figure of **188**; the live
account total is **196** (token-walked, not `--no-paginate`). **DO NOT record that as an 8-lambda
drift.** It is not established what 188 counts — "lambdas in the estate census" and "all functions in
the account" are DIFFERENT DENOMINATORS, and comparing them would manufacture a discrepancy out of
two different questions. **UNRESOLVED. Establish 188's denominator before touching it, or leave it.**

**THE DURABLE FIX IS TO STOP STATING THE NUMBER, NOT TO UPDATE IT.** The model already exists in
CLAUDE.md, which refuses to state the comp-tool count at all, declares the number to be the gate's,
and points the reader at `comp-manifest-check`. Copy that shape: replace the digits with the call
that produces them.

---

## 7. THE PATTERN WORTH CARRYING — this is why the brief exists

**15 of the 26 defects sit in three files:** `NFRA_GCONTR_PRD.md` (7), `NFRA_PIPESCRIPT_PRD.md` (6),
`critical-surfaces.yaml` (4).

**And the sharpest instance is self-illustrating: `critical-surfaces.yaml` was re-grounded on
2026-07-30 precisely as an "at-risk dated baseline under a live SEV1 gate" finding — and the gate it
was re-grounded FOR was deleted seven days later without anyone re-touching the registry.**

**A retirement is not finished when the binary is deleted. It is finished when every record that
tells an agent to use it has been corrected.** The retirement commit did the hard, correct part —
consumers first, binary last, so no caller silently skipped. What it did not do is sweep the
*descriptive* surface, and that surface is what the next agent reads.

## 8. RULES OF ENGAGEMENT

- **Records only.** No code, no infra, no Terraform, no deploy. If a fix seems to need a code change,
  STOP and route it back — it is out of scope for this brief.
- **Do not restart `NFRA_GCONTR`.** It is sovereign-suspended.
- **Do not re-add any commit-time guard** to replace `comp-surface-check`. Its absence is a ruling,
  not a gap. **And do not build an alert, monitor, or checker in its place** — standing moratorium.
- **Do not touch `comp-pipescript`** (live) or the `retired_aliases:` rows (the policing mechanism).
- Commit under your own author line via `.tools/safe-commit.sh -F <msgfile>`; several targets are
  outside the AE lane, so expect an owned-paths refusal and use the audited
  `GIT_COMMIT_AUTHOR_OVERRIDE=<LANE>` — **one lane per commit**, so this will be several commits.
- **Verify each fix by re-reading the line, not by trusting the edit.**

**Full sweep record incl. the 78 non-defects and the classification method:** this brief's source
sweep, summarised in the row-12 section of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/KIMI_SVP_PHASE0_LIFECYCLE_PROPOSAL_TABLE_20260804.md`.
