# NFRA_MSBEFF.R4R6 (lane ~B): two unrun-tool triggers + the retired-alias gate, and a census that voided AC-3

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

Serial `0.8.0_AE_CloudComp~B` (build tilde, spawned 2026-07-23 to parallelize the R-series).
Window: session start ~18:29Z -> ~21:05Z. First log of this session.

## Commits this window (all pushed to CLOUD)

| Commit | What |
|---|---|
| `b7751f8e0` | R4: closeout->comp-state + deploy->pipescript-deployed post-commit triggers + installer + `.open_findings/` surface (de-wired pending arm-gate) |
| `23db0d32c` | R6-D: `retired_aliases` name-authority section + `_retired_alias_invariant` in the completeness family |
| `534321158` | R6 phantom census deliverable (denominators derived live) |
| `aafe421a8` | R4 ruling-1: open-findings surfacing folded into the trigger fast-path breadcrumb |

## What was built

**R4-A closeout->comp-state.** comp-state ran ZERO times in the telemetry era while a live registry
drift sat undetected. Bound it to the moment its answer matters: a commit that flips a project JSON
to a closure status or moves a REGISTRY row fires `comp-state --project <CODE>`; a BEHIND result
lands as an OWNED finding `{owner, severity, review_by, closing_commit}` in
`org/critical_paths/.open_findings/`. Reuses the existing post-commit surface (no new scheduler).

**R4-B deploy->pipescript-deployed.** The automated deploy path runs safe-deploy `--no-pipescript`
(`pre-push-safe-deploy.sh`), so the MATCH check is skipped and deferred to a manual post-push run
nobody does -- the bd-gold-trigger-vs-4-stale-scripts class. Bound the deployed-check to the
deploy-COMPLETION moment: when a `*_deploy_completion.md` ledger closes AND names gold/silver/bronze
scripts, run `comp-pipescript deployed` on exactly those; STALE/MISSING lands as a blocking-class
owned finding. A serve-only ledger (no scripts named) stays silent.

**Both ASYNC** (CTO~Z ruling): fast path <100ms (detect + breadcrumb), heavy scan in a detached
subshell, result out-of-band as the owned finding. Terminal LOUD explicitly NOT relied on -- a
detached print is not a channel; the OWNED ITEM is the TRIGGER_LAYER carrier.

**R6-D retired-alias gate.** `retired_aliases` added as the THIRD coordinated section in
`graph-call-manifest.yaml` (with tools_index + excluded_not_graph_use_cases -- one file, one
authority, per base 0.8.0's blessing). `_retired_alias_invariant` appended LAST in the completeness
family: guardrail A (a name is in EXACTLY ONE section), guardrail B (successors validate against the
live universe or are null), plus a routing-surface check keyed on the CLOSED retired set (a committed
HUD/prompt/skill citing a declared-retired name BLOCKS). Real-name denominator reuses
`_registration_invariant`'s universe verbatim -- never a hand-list.

## The census that voided AC-3 (the window's finding)

Derived live: **84 known-live comp-* names**. Operational routing surfaces carry **9 phantom-looking
tokens / 62 refs** and EVERY ONE grounds to a real FILE (`comp-tools-directive.md`,
`comp-learns-backlog.md`, `comp-tool-hud.sh`), a real SKILL (`comp-loop`), the `comp_tracker.py`
underscore engine, or a CONCEPT (`comp-answerable`/`comp-call`/`comp-rail`/`comp-ferry`).
**ZERO dead-tool routing directives; the HUD routes to no dead tool.** The real mass -- **65 names /
334 refs** -- is in design PRDs/briefs and is never-built PROPOSALS (comp-learns orchestrator family,
comp-debt, comp-events, comp-ladder, comp-ms*, the comp-aws sub-tools). No clean
retired-tool -> live-successor pair exists in the estate.

So AC-3 ("repoint or delete every hit") would text-match prose to rewrite 334 legitimate design
records -- TRIGGER_LAYER clause 2 forbids exactly that -- and bulk-convert historical notes, which
the same doctrine's boundary clause forbids. Surfaced the conflict rather than silently choosing.
**CTO~Z ruled AC-3 VOID as written and owned the Phase-0 premise miss** (it conflated tool names with
`.yaml`/`.md`/`.sh` FILE names and with proposals); MSBEFF's S1 finding is being corrected in the record.

## Deployment sequence + verification (AE role addition)

No AWS/Terraform deploy this window (hook + gate code only). Verification actually run:

```
comp-manifest-check completeness  ->
  [manifest-check] registration-invariant PASS: 83 tracked+committed comp-* executable(s) all
    accounted (tools_index 65 + excluded 15 + entries-tools 70) and ledgered (coverage-map 86).
  [manifest-check] retired-alias invariant PASS: 2 retired name(s) declared, all disjoint from
    live+excluded (86 live), successors valid, none cited in committed routing surfaces.
  PASS: routable + placement + self-routes + existence, over 65 registered tool(s).

comp-manifest-check retired-alias (MUTANT: comp-which declared retired) ->
  BLOCKED: retired-alias invariant (retired 3; live universe 86):
    - comp-which  RETIRED but CITED in committed routing surface(s) ['.tools/hooks/comp-tool-hud.sh']
  exit code 1   <- correct BLOCK; restored, clean re-check PASSES
```

**Mutants (all on the record).** R4-A: positive = real post-commit fire on a closeout commit ->
owned finding (2 BEHIND); negative = non-closeout commit silent. R4-B: positive = ledger naming a
stale script -> owned finding; NEG-1 = MATCH/0-STALE -> no finding; NEG-2 = serve-only ledger ->
silent. R6: 6 in-memory paths + the real-CLI block above. Breadcrumb: 0 findings -> "0 (0 PAST)";
1 past-due + 1 future -> "2 open (1 PAST)" -- discriminating, not a bare counter.

**TWO REAL BUGS THE MUTANTS CAUGHT** (the whole argument for the mutant mandate):
1. `grep -qE 'STALE|MISSING'` on comp-pipescript output -- the summary line literally reads
   `"0 STALE, 0 MISSING_ON_S3"` even for a clean MATCH, so it false-flagged EVERY script. This is
   the documented `_pipescript_output_ok` trap; now parses Summary COUNTS.
2. The script-path regex `[A-Za-z0-9_]+\.py` missed multi-dot gold names
   (`INF_09.generate_partner_analytics.py`) -- R4-B would have **silently no-op'd on every real
   ledger** and read as working.

## The shared-worktree incident (mine, and what closed it)

I created `scratch-r4a-mutant-20260723` via `git checkout -b` **in the shared main tree** for the
R4-A mutant. While HEAD was on that branch, three real Tier-0/1 commits landed on it (CTO MDPF PRD
`9b0710ab6`, COO drive-log `bda523526`, CVO~Z tick `5af01541a`); deleting the branch stranded them.
Base 0.8.0 GC-anchored them, CVO~Z tagged `custody-preserve-scratch-r4a-mutant-20260723`, MSTR
coordinated recovery -- **zero loss** (CTO PRD re-landed `@e1d525341`, COO log recovered
`@dcee36597`, CVO~Z tick VOID by owner). Incident CLOSED.

My actions on notice: shared tree back to CLOUD and kept there; reverted my uncommitted INF_09
STALE-forcing edit (file-scoped); **de-wired both triggers from the live shared post-commit** on my
own judgment -- they were synchronous at that point and the MDPF serve night was live, so they would
have injected comp-state/AWS latency and surprise findings into the fabric's most important closing
work. CTO~Z banked the de-wire as correct judgment and owned the TO's isolation under-specification
(now amend-2). Doctrine banked: **isolate mutant/close-path testing on BOTH axes -- its own worktree
AND no wiring into shared hooks; never `checkout -b` in the shared tree.**

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-state | `--self-test`; `--project <CODE>` (via trigger, live) | PASS 3/3; BEHIND-detecting | self-test gate honored BEFORE trusting any report; drives R4-A |
| comp-manifest-check | `list`; `completeness` (x2); `retired-alias` (PASS + MUTANT BLOCK + restore) | PASS / BLOCK-as-designed | new member integrated; family green on real estate |
| comp-pipescript | `deployed <script>` on INF_09 (MATCH, then STALE after local edit) | PASS both directions | gave the real STALE evidence R4-B parses |
| comp-to | `comp-to NFRA_MSBEFF.R4R6` | PASS | race-free per-session TO id (`.agent_context` was concurrently overwritten to `~A` -- exactly why comp-to exists) |
| commit-gate / safe-commit | every commit; `-m` multi-line for the audited override trailer | PASS | never-rules-gate correctly blocked an `-m` carrying `$(`; comp-system gate blocked then accepted an audited override |
| comp-grep/Grep/Read | targeted source grounding (manifest_check_cli, safe_deploy_core, hooks) | PASS | repo-wide `find`/Glob TIMED OUT twice -- targeted tools are the working path here |

**What worked:** grounding each "phantom" at source instead of trusting the Phase-0 list -- that is
what refuted the premise. The mutant mandate paid twice (both bugs above would have shipped silent).
**What failed then was caught:** my own first R4-A draft backgrounded its LOUD limb into
`>/dev/null` (a finding nobody sees -- the exact failure TRIGGER_LAYER names); caught by reading my
own redirect. **Gap found:** `safe-commit` reads the `system-current-override:` trailer only when it
is on its OWN LINE -- an inline trailer in a single-line `-m` is silently ignored (adjacent to the
open `safe-commit-F-read-override-fix` TO, which covers the `-F` half of the same gap).

## Blockers

None blocking. One gated item: **R4 live-arm is HELD by CTO~Z** pending a non-serve window (the
MDPF serve was open all session). Triggers are built, async, mutant-proven, and de-wired; arming is
one command. This is a scheduled gate, not a blocker.

## Current State (zero-prior-context handoff)

- **R4 triggers exist but are NOT wired live.** Scripts: `.tools/git-hooks/closeout-comp-state-post-commit.sh`,
  `.tools/git-hooks/deploy-pipescript-check-post-commit.sh`, helper `_open-findings-status.sh`,
  installer `install-closeout-comp-state.sh`. `.git/hooks/post-commit` currently contains
  **stitch-refresh ONLY**. To arm: `bash .tools/git-hooks/install-closeout-comp-state.sh` (idempotent,
  wires both). Do this only on CTO~Z's window signal.
- **Owned-finding surface:** `org/critical_paths/.open_findings/` (README records the ruling-1
  surfacing decision). Findings carry `{owner, severity, review_by}`; the trigger breadcrumb reports
  `N open (M PAST review_by)`.
- **R6 gate is LIVE** in the completeness family (runs at commit via `cmd_check` ->
  `_completeness_invariants`), substrate-scoped so it does not tax unrelated commits.
  `retired_aliases` seeded with 2 defensible entries (`comp-learns-run`, `comp-coverage-view`).
- **comp-system 06_current_state is stale w.r.t. my manifest edit** -- I took an AUDITED override
  (`org/git-author-override-audit.log`) rather than regen, because `infra/system/*` was concurrently
  ` M` from the SYSPARITY lane and committing it would have swept another lane's work. CVO~Z's next
  comp-system regen picks up `retired_aliases`.
- **Scratch remnants:** my worktree removed, `scratch-r4-mutant-v2` branch still exists (harmless);
  the `rescue/*` branches + `custody-preserve-*` tag belong to base/CVO~Z/MSTR -- I left them alone.
- **New TO accepted, not started:** `NFRA_TOOLBHVR.ROUTE` (Andrew-direct, auto-route agents to mapped
  surfaces instead of hand-grepping).

## Next Steps

- [`0.8.0_AE_CloudComp~B`] Start NFRA_TOOLBHVR.ROUTE -- FIRST action is coordinating with
  `0.8.0_AE_CloudComp~D` on the NFRA_TOOLARCH.CANON staleness dependency (routing agents to a stale
  mapped surface is worse than letting them grep).
- [`1.0.0_SA_CTO~Z`] Owes the R4 ARM-GO window signal once the MDPF serve closes; then I arm both
  triggers and report the first REAL firing (Phase-3) or "none yet, watch armed".
- [`3.0.0_SA_CVO~Z`] Verifies R4R6 (AC-1..6); census `@534321158` stands in for the voided AC-3.
- [`0.8.0_AE_CloudComp`] Has the R6 hashes; flagged my comp-system override choice for their call on
  whether to regen once `infra/system` is quiet.

## MCP Traffic

~16 messages (7 in / 9 out). Significant: CTO~Z GO on R4R6 (ACKed, flipped pending); base 0.8.0
coordination on the shared `comp-manifest-check` surface (insertion point + the "reuse the
registration universe, never a hand-list" guardrail, then blessing of `retired_aliases` as a 3rd
section + two integration guardrails); the shared-worktree URGENT pair (base + CTO~Z) and my
ground-truth correction that the scratch branch was already deleted -- which prevented the recovery
anchoring on a dead branch name; CTO~Z's async-redesign ruling + arm-gate hold; CTO~Z's two closing
rulings (surfacing home = the breadcrumb; AC-3 VOID); new Andrew-direct GO on NFRA_TOOLBHVR.ROUTE.
