# 3.0.0_SA_CVO — session 2026-07-28T2235Z .. 2026-07-29T0108Z

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

Continuation of `a07438eece` (1445-2235Z). Andrew-direct throughout: MDPF certifier pins, then a
redirect to the INFRA missions and the tooling layer. **4 commits. The through-line: I found the
estate's commit gates were SILENTLY OFF, fixed the cause, and then made three edits to the commit
gate — which is two more than a verifier should make, and is why the fourth went to another lane.**

## Work completed

**1 · Served-prefix registry v0.2 (`bf8aae9c40`)** — closed a gap I had recorded as unresolvable.
v0.1 listed 7 live `json/` prefixes with no ServedURL and I said I could not tell *"nothing serves
this"* from *"the graph does not model what serves this."* **I can: a prefix still being WRITTEN is
being produced for someone.** Banded mechanically (ALIVE ≤7d / DORMANT ≤90d / STALE >90d). The 7
split **1 / 2 / 4** and only the ALIVE one is a defect (`json/latest/`, 6 keys, written that day, no
consumer edge). `json/model_portfolios/` (25 keys, 57d) surfaced as the **pre-revamp MDPF serving
path** — routed to MSTR for `DEBT.BACKEND`, with the ALIVE one deliberately routed AWAY from the debt
item because filing a live blind spot as debt is how it gets deprioritised.

**2 · PATH forwarders 5 → 94 (`7051f9410b`)** — and the motivating defect is the session's worst
find. `safe-commit.sh:483` guarded the COMPUNIFY gate on `command -v comp-coverage-check`. **That tool
was not on PATH. The guard failed, the block was skipped, and THE GATE REPORTED NOTHING WHILE BEING
OFF — on every commit, indefinitely.** A gate that cannot be FOUND is not advisory; it is absent, and
absence looked exactly like a pass. Replaced the hand-named set of 5 with a DERIVED enumeration of
`.tools/comp-*`, each Windows interpreter **read from its own shebang** (70 bash / 23 python, 0
without). Exercised both interpreter classes through the shims. Corrected the script's own header,
which my change had made false.

**3 · manifest_check_cli YAML cache (`fe477c2629`)** — cProfile located the cost rather than
assuming it: `cmd_check` on ONE file = 3.048s, `yaml.safe_load` ×12 = **2.683s (88%)**. Cached per
path, returning `copy.deepcopy`. **The deepcopy is load-bearing, not politeness:** `load_config()`
mutates its result (5× `setdefault`), so a bare cached reference would make those shared state — a
silent correctness bug introduced while making something faster. **/seams-validated before landing,
all 3 axes PASS**, report at `logs/2026-07-28/seams_2340Z_manifest-check-yaml-cache.md`.

**4 · `comp-coverage-check` ADVISORY → BLOCKING (`463a6579b9`)** — on a measured basis (538ms, FIXED,
does not scale with commit size) and **exercised in both directions**: injected an unregistered
`.tools/comp-zzprobe9137` → `rc=1` naming it UNPLACED; removed → `rc=0`. It can fail, so its pass
carries information. Deliberate asymmetry: **rc=1 BLOCKS, rc=2 (UNVERIFIABLE) WARNS LOUDLY** — rc=2
means the gate itself is broken, and blocking on it would convert a broken instrument into a
self-inflicted outage. Also made a missing gate binary LOUD instead of silent.

**5 · Handoff + independent verify (0.8.0_AE_CloudComp)** — handed the post-cache remainder to the
lane Andrew instantiated; they closed it in ~25 min (`b917f2fafd`, worst class 1176→467ms engine
path). **I verified rather than accepted:** re-derived `CSafeLoader` parse-equality on all 5 YAMLs
myself **with a negative control**, and checked the `getattr` fallback guard first because an
unguarded `yaml.CSafeLoader` would make the COMMIT GATE un-importable on a box without libyaml.
RAVC4 closed.

## Corrections against myself (the honest output)

| # | I claimed / did | Truth | Mechanism |
|---|---|---|---|
| 1 | rc=2 override keyed on `$COMMIT_MSG_RAW` | **that variable does not exist in the script** | a documented escape hatch that could NEVER fire — removed rather than made plausible |
| 2 | "AE's timings are 3.7× off" (nearly filed) | **my `~/bin` shim adds ~330ms PER WRAPPER LAYER** | I measured the shim path, they measured the engine path; both right about different things |
| 3 | `/seams` v1 reported PARITY BROKEN | **the harness was broken**, not the patch | copied the module to a temp dir; workspace resolves from `__file__`, so `git ls-files` failed |
| 4 | "the false claim is gone" (grep -c → 1) | the hit was **my own retraction quoting the phrase** | a predicate matching both the claim and its correction |
| 5 | projected ~11× speedup | **measured 1.6–2.3×** | extrapolated from a per-parse micro-bench on the wrong file |
| 6 | read an rc through `\| tail -3`, got 0 for a FAIL | `$?` after a pipe is the LAST stage's | VERIFICATION LAW 13 / PIPESTATUS — hit while proving a gate discriminates |

**Every one was caught by a control, a denominator, or another agent — none by care.** #2 is the one
that mattered: I was one step from filing a false divergence against a lane's delivered work, and
checking my own setup first is what stopped it.

## MCP traffic

~14 messages handled. Significant: **certifier PINS 1-5 ruled by CTO** (all four I raised + a fifth
closing my continuity risk); **PIN-1 design set delivered by 0.7.0_AE_CloudOps** @`d6c9562318` —
**ordering independently verified** (publisher's last invoke 07-23T19:30Z, five days BEFORE the pin,
so it is genuinely pre-publish); **stage-1 certifier notice** from CTO; **DEBT.BACKEND items to
MSTR**; **handoff + RAVC4 close with 0.8.0_AE_CloudComp**.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-coverage-check` | PASS→FAIL→PASS | exercised on injected drift; the flip's evidence |
| `comp-manifest-check` | PASS + `selfcheck` PASS | post-cache; selfcheck is the independent confirmation |
| `comp-kuzu` | PASS | S3Key/ServedURL traversals for the opalbizcluster root cause |
| `comp-heat` / `comp-which` / `comp-glob` | PASS | shim-path exercise after the forwarder widening |
| `cProfile` (×2) | located both costs | 88% YAML in the gate; 330ms/layer in my own shim |
| `safe-commit.sh` | 4 commits | all clean |

**What worked:** the parity-harness pattern — live module, real path, one variable — is reusable and
I handed it to AE for their routing-identity control. **What failed:** my first `/seams` harness
(§corrections #3). **Gap found:** each `~/bin` wrapper layer costs ~330ms on this box; the shim could
`exec` the interpreter directly for Python tools and skip a bash hop. Not chased — flagged.

## Blockers

**None at me.** The advisory→blocking flip for `comp-manifest-check` is **routed to 1.0.0_SA_CTO**
with both measurement sets (engine-path governs; shim-path labelled CLI-ergonomics). **Both AE and I
recused — neither should pull a flip on a gate we built and verified.** That is a routing state, not
a blocker.

## Current state

- **PATH:** 94 tools × 2 forms in `~/bin`, DERIVED from `.tools/comp-*`. Re-run
  `bash .tools/provision-path-shims.sh` (idempotent). **CTO's "only 4 of 92 resolve bare" is STALE.**
- **Gates:** `comp-coverage-check` **BLOCKING** (538ms fixed, rc=1 blocks / rc=2 warns);
  `comp-manifest-check` **ADVISORY**, now ~467ms worst class on the engine path (clears the bar;
  flip decision at CTO). `commit_gate_runner` imports in-process and pays no shim cost.
- **Registry:** `.tools/served_prefix_registry.yaml` v0.2 — 46 keys in PREFIX scope of 957 live;
  residual classified ALIVE 1 / DORMANT 2 / STALE 4.
- **MDPF certifier:** STANDING, attaches to the **SERIAL** (PIN-5). Stage-1 reviewable; **D2 CANNOT
  close before the three unattended fires (~15:00Z chain / ~16:15Z publisher / 17:15Z emitter) and
  stage-1 evidence NEVER closes it.** PIN-1 diff against `d6c9562318` is **runnable and NOT YET RUN**
  — Andrew deprioritised the MDPF detail mid-session; it is ready whenever called.

## Next steps

1. **[3.0.0_SA_CVO — successor if I do not survive to fire time]** D2 stage-2 certification off each
   run's own trigger-identity log. Role transfers via `org/critical_paths/MDPF_RESET_DIRECTIVE_20260728T2220Z.md`, in writing.
2. **[1.0.0_SA_CTO]** the `comp-manifest-check` advisory→blocking call; package delivered by AE.
3. **[0.8.0_AE_CloudComp]** residual they named: `git ls-files` spawns twice per completeness batch (~130ms each).
4. **[3.0.0_SA_CVO]** unstarted, no signal: PORTAL_AUTHHARD W2+, smartx first-conversion.

— 3.0.0_SA_CVO
