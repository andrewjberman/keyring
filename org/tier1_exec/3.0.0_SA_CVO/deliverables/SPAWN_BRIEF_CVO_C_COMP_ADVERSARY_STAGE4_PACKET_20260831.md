# SPAWN BRIEF -- `3.0.0_SA_CVO~C`: build `comp-adversary` STAGE 4 (the PACKET stage)

Author `3.0.0_SA_CVO` (base/MAIN). Andrew-direct at the CVO terminal 2026-08-31 ~23:4xZ, VERBATIM:
> Yes we need to build this, give me a briefing with all relevant paths and I will spawn an
> additional CVO~C to build it out. ... that way you can keep focusing on managing the proof of
> specs of the active fabric as they come in ... and we will let you know when it is ready to test.

Base `3.0.0_SA_CVO` retains proof-of-spec management of the active fabric and does NOT build this.
Testing is Andrew-triggered: `~C` reports READY, it does not self-certify and does not ship.

---

## 1. THE ONE-SENTENCE MISSION

`comp-adversary` v1 implements 2 of its 5 spec'd stages. **Stage 4 (PACKET) is spec'd and absent.**
Build it: turn the complement set from a list of POINTERS into a set of `comp-read` DIGESTS sized
for a validator context.

---

## 2. WHY IT MATTERS (the gap, in Andrew's own framing)

Andrew's standing mental model was that comp-adversary "spawns a subagent with context fed to it
that differentiates from the agent owner/operator of the tool." **It does not, and never did** --
`.tools/comp-adversary:22` reads *"Read-only over the repo + git. No AWS calls, no model calls,
deterministic."* Source-confirmed: its only three subprocess call sites are `git rev-parse`,
`git -C <root> ...`, and `python .tools/comp-state --json`.

>> **BUT the half he remembers WAS spec'd, and it is exactly stage 4.** "A packet of comp-read
   digests sized for a validator context" IS the differentiated-context feed. It is the one stage
   that would let a validator READ the complement instead of being handed 542 file paths. <<

⛔ **This does NOT authorize building a subagent, an LLM call, or a spawned reviewer.** The tool
stays deterministic. The build is: pointers -> digests. Nothing about the process model changes.

---

## 3. ALL RELEVANT PATHS (verified present at 2026-08-31T23:4xZ unless marked)

### Build target
```
.tools/comp-adversary                                    322 lines, python3, THE FILE YOU EDIT
~/bin/comp-adversary                                     bootstrap shim, DO NOT hand-edit
                                                         (regenerate: bash .tools/provision-path-shims.sh)
```

### The spec (authority for what stage 4 must be)
```
org/tier1_exec/1.0.0_SA_CTO/deliverables/DESIGN_NOTE_CHECK_SYSTEM_DEFINITIONS_AND_COMP_ADVERSARY_20260819.md
    12,387 bytes, 2026-08-19 17:08. Section 3.1 = the five stages. Section 3.2 = interfaces.
    Section 4 = build routing + acceptance. READ SECTION 3 IN FULL BEFORE EDITING ANYTHING.
```

### The dependency stage 4 is built ON (build-ladder rung 2 -- the estate already has it)
```
.tools/comp-read                                         42,720 bytes, executable, 2026-08-07
~/bin/comp-read                                          shim resolves
```
⛔ **DO NOT WRITE A DIGEST ENGINE.** `comp-read` exists. The spec says "comp-read digests"
by name. Writing a second digester is a build-ladder violation AND a shadow-pipeline violation.

### Doc + test surface you must update
```
.claude/skills/comp-adversary/SKILL.md                   6,174 bytes, 2026-08-29 -- ALREADY STALE
                                                         (see s.6 -- it describes the pre-fix world)
.tools/tests/test_comp_adversary_path_truncation.py      5,488 bytes -- the existing test pattern
                                                         to imitate for a stage-4 test
```

### Internal anchors in `.tools/comp-adversary` (line numbers at read-vintage; re-derive before editing)
```
:19    usage block ...................... add any new flag here
:49    COMMIT_RE = @([0-9a-f]{7,40})\b ... the bound-1 regex (see s.6)
:63    PATH_RE ........................... carries the 2026-08-20 truncation-fix comment; READ IT
:112   def uncited_neighbors(paths, cap) . produces the complement set stage 4 consumes
:136   def comp_state_drift() ............ the existing subprocess-shellout PATTERN to imitate
:155   ("comp-read digests (the packet stage)", "v1: the packet lists POINTERS, not digests")
                                           <- THE EXCLUSION ROW YOU ARE RETIRING
:160   def _emit(body, out_path)
:169   def compose(path, out_path, cap, open_mode=False)   <- where the packet section slots in
:241   "## DECLARED EXCLUSIONS" header ... 6 rows today, must become 5
:256   def self_test() ................... 4 controls today, must gain a stage-4 control
:294   def main()
```

### Lane infrastructure
```
org/mcp/inbox/3.0.0_SA_CVO/~C/                           EXISTS. Your inbox. Canonical nested form.
                                                         NEVER org/mcp/inbox/3.0.0_SA_CVO~C/ (flat = dead)
org/tier1_exec/3.0.0_SA_CVO/deliverables/                where your deliverables land
org/tier1_exec/3.0.0_SA_CVO/prompt.md                    CVO persona; read the LANE ROUTING section
org/XXX.md                                               startup protocol (register, /watcher once)
```
`3.0.0_SA_CVO~C` is NOT in `org/mcp/liveness.json` as of this brief -- no incumbent, no identity
conflict expected. Verify anyway at load per XXX.md Step 1.

---

## 4. WHAT STAGE 4 MUST DO -- the spec, verbatim

Design note s.3.1, stage 4, in full:
> **PACKET**: comp-read digests of the complement set, sized for a validator context.

And the stage-5 sentence that tells you what the packet is FOR:
> **The declaration is the product**: a validator who knows what they were not shown can refuse
> to conclude.

### The design question you must answer FIRST, before writing code
Stage 3 on a real artifact returned **542 uncited siblings** (measured tonight on the D2
proof-of-spec). A packet that digests 542 files is not "sized for a validator context" -- it is a
context bomb. **So the deliverable is not "digest everything"; it is a SELECTION RULE plus digests.**
State your selection rule, its denominator, and what it EXCLUDES, in the declaration itself --
the tool's whole contract is that partial coverage is honest by construction, never silent.
⛔ Do not invent the rule and bury it in code. It is a schema-shaped decision: Rule 24 TAXONOMY
LAW applies (MECE over a declared domain, same grain, one axis, state coherence).

---

## 5. ACCEPTANCE -- criteria that CAN FAIL (write these before you write the feature)

The design note s.4 sets the v1 bar as "a packet built for one REAL validator run (a CVO-class
review), its declaration conformance-checked against the family shape." Stage 4's bar inherits it:

1. `comp-adversary --self-test` still returns **PASS 4/4**, plus a NEW 5th control that
   **fails on the pre-build binary** (a planted case where a digest must appear and does not).
   A control that passes against the old code proves nothing -- run it red first.
2. On `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_PERFRP.TO-R1-DS_PROOF_OF_SPEC.json`
   the output contains real `comp-read` digest CONTENT, not paths, for the selected subset.
3. The selection rule prints its **denominator** (selected N of 542) on its own line.
4. The DECLARED EXCLUSIONS block drops from 6 rows to 5 -- `:155` retired, the other five intact.
5. `--open` mode still emits the empty-context declaration and still runs NO complement sources.
6. Runtime stays sane. The design note records a measured **71.5s** freshness constraint behind
   the "snapshot rows, never live-render" rule for comp-axes. Time your run and print it; if
   digesting pushes a compose past that order, the selection rule is too wide.
7. **Negative control:** an artifact with ZERO cited paths (use
   `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/AUTH_SELFHEAL_PRD_v0.1.md`) must still fire
   the ZERO-PIN banner and must NOT emit a packet section claiming coverage.

---

## 6. SECOND, SMALLER ITEM -- NAMED SEPARATELY, DO NOT LET IT ABSORB STAGE 4

CVO finding msg **90276/90277/90278/90279** (2026-08-31 23:32Z) reported a verified live defect:

```
  COMMIT_RE at :49 is  @([0-9a-f]{7,40})\b   -- requires @ IMMEDIATELY against the hex
  so a backticked pin  @`6bac8e6cdb`         -- MISSES. Reports 0 attempted / 0 verified.
  and "0 attempted" reads exactly like "0 problems".
```
Reproduced 2026-08-31 on `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260828_MSTR_INTEGRATOR_AND_OBSERVER_ONLY.md`
(artifact-vintage `3da6c6506a`, unchanged since 08-28; the hash IS present, backtick on both sides).

v1 HAS a ZERO-PIN banner, but its trigger is profile-emptiness, so it fires on a 0-commit/0-path
artifact and stays **silent** on the 0-commit/1-path case -- the half that looks well-evidenced.
**Recommended predicate: warn when `commits_found == 0 AND raw_hex_runs_present > 0`.**

⛔ **COLLISION WARNING, AND IT IS REAL.** The design note s.4 routes this build to **0.8.0-class**,
and finding 90279 is already QUEUED in `org/mcp/inbox/0.8.0_AE_CloudComp/` (no live session at send
time). If `0.8.0_AE_CloudComp` wakes and starts the same regex fix, two seats edit `:49`.
**`~C` MUST message `0.8.0_AE_CloudComp` BEFORE touching `:49`** and take stage 4 as the
uncontested lane. Stage 4 is not in contention; the regex fix is.

---

## 7. CONSTRAINTS (non-negotiable)

- **No shadow/build-alongside pipeline, no duplicate output path, no standing parity comparator**
  (Andrew complete veto). Edit `.tools/comp-adversary` in place; do not create `comp-adversary2`.
- **Build ladder:** `comp-read` exists -- use it. New code is the LAST resort.
- **No non-ASCII** in code/logs. Use `OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`.
- **Commit:** `.tools/safe-commit.sh --author "3.0.0_SA_CVO~C <3.0.0_SA_CVO~C@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. `-F` not `-m`. The message file must be written by a NON-SHELL writer
  (Write tool / python) -- a printf/heredoc-built file re-opens the injection one step earlier.
- **Gate:** run `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39). `.tools/comp-adversary`
  is python without a `.py` extension -- run the gate on it anyway rather than assuming exemption.
- **Never rebase on CLOUD.** Rejected push = pull-merge, re-push.
- **Zero crons at launch.** `/watcher` once. It is not a loop.
- Andrew's word is the test trigger. `~C` reports READY; base CVO grades; neither self-certifies.

---

## 8. REPORTING

- Report to `3.0.0_SA_CVO` (base, this author) + `1.0.0_SA_CTO` (design-note author, owns the spec)
  + `0.8.0_AE_CloudComp` (declared build owner -- coordination, see s.6).
- Surprise channel: anything odd off-task = ONE line to `3.0.0_SA_CVO`, KEEP WORKING.
- Carry the tool's own bound in any result: **a declaration is a statement of what was and was not
  looked at. It is NEVER a pass.**

---

## 9. WHAT `~C` MUST NOT DO

- Do not build a subagent, an LLM call, or any model call into this tool.
- Do not adjudicate D2/D8 substance -- base CVO holds proof-of-spec management.
- Do not ship or self-certify. Andrew triggers the test.
- Do not widen into stages 2 and 3 (comp-blast/comp-trace expansion, toolgraph independence oracle,
  comp-axes, comp-pulse, comp-cochange). They are also unbuilt and they are NOT this brief.
  Surface them; do not absorb them.

`3.0.0_SA_CVO`
