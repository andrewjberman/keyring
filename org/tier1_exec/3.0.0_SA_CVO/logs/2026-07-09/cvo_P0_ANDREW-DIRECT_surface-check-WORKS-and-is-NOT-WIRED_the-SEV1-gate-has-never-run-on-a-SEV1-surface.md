# CVO — **[ANDREW-DIRECT P0]** `comp-surface-check` **works, and is not wired to anything.** The SEV1 gate has never once run on a SEV1 surface. 17 commits.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~03:12–03:20Z · **Agent:** 3.0.0_SA_CVO
**Andrew, verbatim (via CTO `031159Z`):** *"It is P0 above all else that we sort out the correctness of our comp tools, discuss with CVO."*
**Refutes:** CTO's (A) — *"comp-surface-check … I can find no evidence it has ever printed anything but OK … if no input makes it go RED, our SEV1 gate is decorative."*

---

## 1. The tool is CORRECT. It is one of the very few instruments proven tonight to say NO.

Exercised. Exit codes read **without a pipeline** (`$?` after `| tail` is *tail's* — I made that error first and caught it):

    portal/src/api/endpoints/aum.ts             -> rc=2   "CRITICAL ... BLOCKED (SEV1, block-with-ack)"
    portal/src/components/BenchmarkHeatmap.tsx  -> rc=2
    portal/src/pages/ModelPortfolios.tsx        -> rc=2   (SEV1 benchmark + SEV2 aum -> resolves SEV1)
    CLAUDE.md                                   -> rc=0
    org/XXX.md                                  -> rc=0
    selfcheck                                   -> rc=0   (the 2026-06-12 FAILs are a REPAIRED tool, not a mute one)

**3/3 positive, 2/2 negative.** It discriminates. **CTO's premise is falsified.**

## 2. It is not wired to anything it guards. Every zero below carries a control.

    safe-commit.sh mentions "portal"            : 0        CONTROL: mentions "surface-check" = 4
    portal pre-commit hook                       : ABSENT   CONTROL: 14 .sample files readable in the same dir
    portal working tree invokes surface-check    : 0 files  CONTROL: 233 files match "react"
    portal pre-push (69-line VALGATE) invokes comp-* : 0    (it gates tsc + VALGATE)
    portal core.hooksPath redirect               : unset
    portal CI: ci.yml / deploy.yml / promote-to-prod.yml, references to surface-check or comp-* : 0
                                                            CONTROL: 3 workflow files match "run"

**ALL THREE SEV1 WATCH PATHS LIVE IN `portal/`, a separate git repo.**

> **`comp-surface-check` is invoked at NO point in the portal lifecycle — not at commit, not at push, not in CI.**

## 3. And the surfaces were touched. Seventeen times.

    src/pages/ModelPortfolios.tsx        16 commits since 2026-06-01
    src/components/BenchmarkHeatmap.tsx   1 commit
    src/api/endpoints/aum.ts              0

Measured **inside the submodule**. The workspace-root query `git log -- portal/src/pages/ModelPortfolios.tsx`
returns **0** — **the parent repo cannot see submodule paths.** Positive control: `git -C portal log --` on the same
path returns **122**. Negative control: a path that cannot exist returns 0.

**I was one line from reporting "0 commits touched SEV1 surfaces since June, so the gap is theoretical."** It is 17,
and one of them is `BenchmarkHeatmap.tsx` — the benchmark surface that produced BMKAUD.

## 4. The `safe-commit` triple-discard: real, and now IRRELEVANT

    safe-commit.sh:409   # Advisory surface-check gate (QUERY-only; never blocks).
    safe-commit.sh:417   comp-surface-check check --mode advisory ... 2>&1 \
    safe-commit.sh:418      | sed 's/^/  [surface-check] /' || true

`--mode advisory` forces **rc=0 even on a SEV1 file** (measured: advisory 0, default 2). Then a pipe into `sed`
(so `$?` is sed's). Then `|| true`. **Three independent neutralizations; any one suffices.**

And the tool still prints `BLOCKED (SEV1, block-with-ack) … set SURFACE_ACK="<reason>" and re-run (audited)`.
**`SURFACE_ACK` is DEAD CODE** — safe-commit never reads the exit status, so the ack branch is unreachable and
nothing is audited. **The gate announces a block, offers an override for the block, performs no block, audits nothing.**

CLAUDE.md:38 lists it under **"Gates:"**. CLAUDE.md:68: *"(auto in safe-commit) | SEV1 = must-always-be-right."*

**I would have shipped the `|| true` fix and reported the SEV1 gate restored.** It would have changed nothing:
`safe-commit` is never in the path for a portal file. **The fix is a portal-side pre-commit hook or a CI gate** —
CTO's arch ruling, DT's lane. Not mine, and I have not drafted it.

## 5. This inverts the whole night, and it is the one finding that runs the other way

Every other defect tonight was **an instrument that could not say NO.**
This is **an instrument that says NO, correctly, specifically, with the right exit code — and is never asked.**

> **CTO's law:** *"A tool that has only ever printed one value is not a tool."*
> **The companion it needs, or it condemns this one:** *A tool that has only ever printed one value may be a
> perfectly good tool that was never asked the other question.* **Before condemning an instrument, establish that
> its INPUTS ever varied. Silence from a tool that was never called is a fact about the CALLER.**

**Ranking principle** (CTO asked for one, by blast radius):
> **Rank by what a wrong verdict AUTHORIZES, not by how wrong the tool is.**
> An instrument that cannot say NO: blast radius bounded by what it is trusted to permit.
> An instrument that says NO and is not heard: **blast radius unbounded** — the false confidence is *affirmative*,
> printed into the transcript, and cited. (`D8 surface-check OK` and `VALGATED-1 PASS + D8 surface-check OK` both
> appear in `org/compiler-tools-log.md`.)

## grounding

- **exercised:** `comp-surface-check check --file <5 files>`, exit codes captured without a pipeline; `selfcheck`;
  advisory-vs-default mode comparison on the same SEV1 file
- **applied/source:** `safe-commit.sh:409,:417-418`; `critical-surfaces.yaml` (6 surfaces, 3 SEV1); portal
  `.git/hooks/` (1 active hook: `pre-push`, 14 samples); `portal/.github/workflows/{ci,deploy,promote-to-prod}.yml`
- **retrieval controls:** every zero above paired with a positive control on the same query shape; the parent-repo
  submodule-blindness caught by `git -C portal` (0 vs 122)
- **NOT established:** whether any of the 17 commits changed a served value (**unmeasured; harm not demonstrated and
  not implied**); whether any *other* mechanism gates portal SEV1 changes; the disposition of the 83 E4 candidates

## What you should have asked but did not

**"Is the gate connected?"**

Not *does it work* — it works. Not *has it ever said no* — it says no, on 3 of 3, with rc=2 and a precise message
naming the surface, the severity, the firms, and the override procedure. Somebody built that carefully. Somebody
wrote a `SURFACE_ACK` path and an audit note.

**Nobody ever ran the wire.** And because the tool is correct, every time it *was* invoked — on a CVO log, on
`CLAUDE.md`, on an infra file — it printed `OK: no critical surface`, truthfully. Those OKs went into
`org/compiler-tools-log.md` **5,347 times**. Agents read them and wrote `D8 surface-check OK` into their session
logs. The gate's honesty is exactly what made its absence invisible: **it never lied, it was never asked, and its
truthful silence was recorded thousands of times as evidence of a control that does not exist.**

We spent the night hunting instruments that cannot fail. **This one can. It has simply never been in the room.**

— 3.0.0_SA_CVO
