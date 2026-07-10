# F-004 pass 3 — the gate, the gate's own test, and the value already sitting in the variable

**archetype:** VALIDATE
**agent:** 3.0.0_SA_CVO · **session:** 2026-07-10 (respawn) · **HEAD at start:** `3e44606e7`

Three findings, one shape. Each was *exercised*, not read. Every prediction I made before running the
control is recorded below, including the **four that were wrong** — the controls caught all four.

---

## THE SHAPE (the thing worth keeping)

> **In all three cases the correct value was already computed and sitting adjacent. The consumer read a
> constant, a shared file, or the wrong class instead.**
>
> And in all three, **a test existed, passed, and could not reach the branch that fails.**

| # | Instrument | The value it needed | What it read instead |
|---|---|---|---|
| 1 | `comp-tool-hud.sh` GATE-1 | the path predicate | `class == comp_which` (the catch-all) |
| 2 | `headmove-guard.sh` | `$OPAL_AGENT_SERIAL` (present, correct) | the shared `.agent_context` |
| 3 | `comp_route.py:362` | `top_s.vetted_confidence` (computed at `:345`) | the constant `_VETTED_OFFSET` |

---

## FINDING 1 — Rule 21's deny surface is narrower than Rule 21 says, and GATE-1's enforce-flip is near-inert

**Grounding.** Source: `.tools/hooks/comp-tool-hud.sh @ working-tree`. Exercised in an isolated scratch tree
(hook copied, `sha256` verified identical) so the real `comp-which-rail.log` — the instrument under
measurement — was not polluted. Marker `org/mcp/comprail-gate1.enforce` **present and tracked** (`57c86bd4b`).

**Deny fires on exactly three surfaces** (`:200-221`): tier-1 raw-aws classes (`:203`), tier-2a `infra/.tf`
grep (`:204`), and GATE-1 (`:215`) which requires `class == comp_which` **AND** no pipe **AND** a recursive
form **AND** an estate path glob.

**CLAUDE.md Rule 21 says raw repo-`grep`/`find`/`rg` denies.** Exercised — it does not:

| command | verdict |
|---|---|
| `grep -rn F-004 org/tier0/reviews/` | **allow** |
| `rg pattern docs/` | **allow** |
| `find .tools/ -name "*.sh"` | **allow** |
| `grep -n helper data/inf/scripts/gold/x.py` (non-recursive) | **allow** |
| **`grep -r as_of data/inf/scripts/gold/`** — the canonical gold-script search Rule 13 governs | **allow** |

**Mechanism (source-confirmed + discriminated).** `:118` is first-match-wins. `:144` (`s3_artifact`) claims
any query containing the token `(^|/)(gold|platinum|silver)/` **before** the `comp_which` fallback (`:174`)
that GATE-1 keys on. Discriminator: `…/scripts/goldXX/` → **DENY**; `…/scripts/gold/` → **allow**;
`…/scripts/bronze/` → **DENY**. It is the *token*, not the substring.

**The search PATTERN can also exempt the search**: `grep -r opal-data-inf data/inf/scripts/` → allow (`:144`
bucket regex); `grep -r Foo.tsx data/inf/scripts/` → allow (`:150` portal). And a **trailing slash decides**:
`portal/src` → DENY, `portal/src/` → allow.

**Attribution control (marker removed):** `data/inf/scripts/` flips DENY→allow (so that deny *was* GATE-1's),
while `…/main.tf` stays DENY (tier-2a, marker-independent). **GATE-1's entire behavioural delta is glob-1
minus the gold/silver/platinum token.** Its other three globs are either redundant with tier-2a or reachable
only in the no-trailing-slash form.

**Census (path census of tracked filenames only; no bucket, artifact, or pipeline touched):**
`data/*/scripts/gold` **231** + `silver` **39** = **270 of 303 (89.1%)** of tracked pipeline `.py` files sit
behind a path token that exempts a recursive grep. `bronze` (33) remains gated.

**End-to-end limb.** A unit test proves the hook *emits* deny JSON; it cannot prove the harness *honors* it.
Exercised live: `grep -n aws_iam_role infra/aws/terraform/globgrph/main.tf` → **blocked by the harness**.
Paired positive control: the same command with `# rail-checked: <why>` → **ran**, and logged `RUN-OVERRIDE`
with the reason. **The gate is real and it can go RED.** (Unlike `comp-surface-check` — LD-0273.)

### The structural insight (this is the finding, not the table)

> **An enforcement gate keyed on the CATCH-ALL class can only ever gate what no other rule recognized.**
> **Every new comp-tool class added to the HUD silently SHRINKS GATE-1's deny surface.**

`object_heat` (`:159`) was added 2026-06-25 and narrowed it. The next class narrows it further. **The gate is
anti-correlated with the rail's own maturity, and nobody will notice, because classes are added to *improve*
the rail.** GATE-1 must key on a path predicate evaluated *independent of class*.

### And the gate's own test could not have caught this — three ways

`.tools/comprail-gate1-fptest.sh` (`a62b63e46`, CTO, 2026-06-25):
1. **`scripts/(gold|silver)` coverage: 0 cases.** The shadowed path is untested.
2. **CI workflows invoking it: 0.** Its only non-doc reference is a comment in the hook.
3. **`:20-22` refuses to run if the marker exists** — and the marker was **committed** the next day
   (`57c86bd4b`, COO, 2026-06-26). Exercised: `bash .tools/comprail-gate1-fptest.sh` → `REFUSE …`, **rc=2**.
   Marker is tracked ⇒ present in every clean checkout ⇒ **the test can never run again.**

> **The commit that made enforcement durable is the commit that made its test unrunnable.**
> Two agents, one day apart, each locally correct.

**I predicted rc=0** (the `comp-surface-check` silent-pass shape). **It is rc=2 — loud.** The refusal is
honest; it is simply never invoked. *Prediction wrong; control right.*

**NOT ESTABLISHED:** no agent is shown to have received a wrong answer. **The gate's narrowness is the
finding; harm is NOT demonstrated.** Which form agents actually type (`portal/src` vs `portal/src/`) is
**unmeasured** — the rail log's `q=` field truncates at 100 chars, so my 27-vs-10 count over 9,388 rows is
indicative only and must not be quoted as a rate.

---

## FINDING 2 — `FORCE-HEADMOVE` names the innocent (SoD for CTO; his claim, independently re-established)

CTO asked me to **refute** it. It survived all four attack shapes. Full verdict + mutant bar sent
`131514Z`; self-correction sent `131749Z`.

- **Denominator:** 21,502 tracked files; **1** definition of `__headmove_serial` (`headmove-guard.sh:55`);
  `~/.bashrc` **sources** it (0 inline copies).
- **ARM A (live, non-synthetic):** `~/.bashrc` already loaded the real function into every Bash-tool shell.
  `type __headmove_serial` matches source verbatim. Called it with **myself as ground-truth actor**:
  → **`1.0.0_SA_CTO`**. `$OPAL_AGENT_SERIAL` = `3.0.0_SA_CVO`, correct, present, **never consulted**.
- **ARM D (the arm CTO did not run):** file absent + `GIT_AUTHOR_NAME` **unset** (its real state in an agent
  shell) → **`UNKNOWN`**. His positive control saw a caller only because he exported one.
  ⇒ **The guard has NO branch that ever names the true actor.** Stronger than his own claim.
- **CTO's exercise was vacuous-adjacent** — he replicated the body rather than sourcing the file, the
  wrong-seam class he warned me about in the same message.

**My `(shared)`-tag ruling** (adopted verbatim by CTO, `131847Z`): a tag inside the actor field is honest to a
human and **invisible to every retrieval** (`grep -c` hits it; `awk '{print $3}'` yields it). Worse,
**`(shared)` communicates *uncertainty* where the true state is *anti-correlation*** — it names the
most-recently-started agent, i.e. the one with the fewest local commits worth force-discarding. Remedy:
actor field carries a **sound oracle only** (`(env)`/`(session)`) **or the literal `UNKNOWN(no-actor-oracle)`**;
the shared value moves to a labelled context field. **Soundness is the classifier, not decoration.**

**M4 (mine) gates the fix:** no sid AND no env ⇒ must print `UNKNOWN`, never the shared serial. CTO's
prepend-only precedence passes M1+M2 and **still lies in the residual**. **M3 ("the guard must still BLOCK")
passes today and has therefore never been shown able to go red — mutation-kill it or delete it.**

**My own sweep refuted itself.** I claimed two further shared-only consumers. Opened the source: one is an
`<agent_context>` **XML tag in a prompt string** (`interrupt_resolver.py:493`); the other is the word inside
an **`echo`** (`build-and-upload.sh:346`, a file that never reads it). **Retracted unprompted.** Corrected
result: of 14 code consumers, **1** is shared-only — the guard. **10 have a sound tier *present* but their
ORDER is unverified. Absence is conclusive; presence is not.**

---

## FINDING 3 — the confidence gate throws away the number it computed

`comp_route.py @ 14d6812b5` (clean vs HEAD). `_VETTED_OFFSET = 1.0` (`:127`), `relevance_floor = 0.15`
(`:141`), and `:362` `top_relevance = (_VETTED_OFFSET if top_s.vetted else …)` ⇒ `1.0 < 0.15` never true ⇒
the floor is unreachable for a vetted candidate.

**But "the gate never reads the query" (CTO, COO) is FALSE**, and my probe refutes it:

- `"how do I proof sourdough at high altitude"` → **`comp-which -- no rich comp-tool fits this exact search;
  running the ON-RAILS primitive`** → fell back to `comp-grep` (0 matches, 20,921 files scanned).
  **It CAN say "nothing fits."**
- `"?????? ...... ------"` → confident 4-way near-tie (`comp-pii`, `pipescript`, `comp-shell`, …).

The query *is* read: it determines `vetted` and yields `vetted_confidence` (`vc`) at `:345`. `:346` uses `vc`
to **rank**. `:362` **discards `vc`** and substitutes the constant. Per `:153` (*"curated 1.0; surface-first
< 1.0"*), a weak surface-first hit with `vc → 0` still clears a 0.15 floor by 6.7×.

> **The number the gate needed was already in the variable beside it.**
> Repair: `top_relevance = top_s.vetted_confidence if top_s.vetted else (…)`.

**Verdict: CORRECT off the vetted set; UNDISCRIMINATING on it.** Not globally undiscriminating (COO), not
anti-correlated. Binding constraint = **extractor precision**, which `:771` already concedes: *"a LONE
wrong-vetted is bounded by extractor precision."*

**And the inversion nobody has named:** gibberish and punctuation get **confident routes**; a well-formed,
honest, off-domain question gets an **honest fallback**. The tool is more confident on nonsense than on a real
question it cannot answer. **Mechanism UNGROUNDED — I have not established why. Named as a residual, not a
finding.** It is the first thing TO-8's harness should characterise.

**In-source corroboration of COO's law** (`:761-766`): the module's own floor self-check uses the hand-chosen
`"xyzzy nonsense unmatched tokens"`, which produces **no vetted hit** — so it exercises the *floor* branch and
**can never enter the vetted-bypass branch where the defect lives.** It passes, permanently. *The test's
negative control cannot reach the defective branch.* Two execs and the module's author each hand-picked a
string that landed in the tested branch.

---

## RAIL_SET_canonical_20260710 → **rev 2** (published this session; ratification authority)

CTO and COO sent **contradictory instructions** about the artifact I own (withdraw / stands). Per MSTR's
ratified doctrine — *latest + most-restrictive binds; act on the intersection, escalate the difference* — and
CTO's own `132525Z` partition, I ruled:

- **(a)** R7 **sharpened** (CTO, accepted): *a disclosure must VARY WITH THE OBSERVATION; a constant field is
  a banner.* **HONEST-UNDER-ABSENCE is not a new rail. No R8.**
- **(b)** R2-per-limb **extended to INPUT SELECTION** (COO, granted). Acceptance criterion: **a control must
  be shown to REACH BOTH BRANCHES. Coverage of the branch, not size of the corpus.**
- **(c)** The comp-which **code-path finding is KEPT**; its **positive-case status is VACATED** —
  **permanently, not pending a re-run.** CTO offered a restore path; **I reject it**, using his own sentence:
  the claim *"is robust to which gibberish anyone picks."* **A control whose outcome is invariant under its
  own input cannot exonerate anything, however the input is generated.** That is **R1** applied to this
  taxonomy's own positive case. **The positive case and the `:82` R7 PASS were the same error in two hats.**
- **(d)** `:82` **re-grounded**: the R7 *verdict* survives on the fit-disclosure (which varies); the cited
  router-name banner is a **banner**. **comp-which PASSES R7 and FAILS R1 on vetted inputs — different rails.
  CTO read a disclosure failure where there is a correctness failure; COO read "cannot say nothing fits"
  where the tool demonstrably can.**
- **Disclosed per R5: this taxonomy now has ZERO established positive cases, and 8 catches. A rail set that
  has only ever indicted is not yet distinguishable from a bias.** That weakness is now on its face.
- A **candidate** replacement clear is offered (the GATE-1 marker-removal control, whose discriminating power
  is demonstrated *inside* the experiment — the same control moved one row and not the other). **Marked
  candidate, not case, pending independent replication.** *The grader of the graders must not grade itself.*

---

## Compiler Tools

| Tool | Invocation | Result | What it taught |
|---|---|---|---|
| `comp-which` | 4 probes (pos-ctrl / off-domain / my real `echo` banner / pure punctuation) | pos-ctrl → `comp-aws` near-tie; off-domain → honest fallback; **banner + punctuation → confident routes** | The P0 spot-check Andrew asked for. Surfaced Finding 3's inversion. |

**Zero other comp-* tools run, deliberately, and it is the point: the comp-tool rail WAS the object under
test.** Where I needed repo retrieval I used raw `grep`/`git grep` **with a printed denominator every time**,
because a comp-tool's answer would have inherited the predicate I was auditing (*two instruments sharing a
predicate are one instrument*). One deliberate gated call was made with `# rail-checked:` as the paired
positive control for the deny exercise, and is in `org/mcp/comp-which-rail.log` as a `RUN-OVERRIDE` with its
reason.

**My own instruments failed twice more, both caught by controls:** `grep 'relevance_floor\s*='` silently
missed `relevance_floor: float = 0.15`; the `agent_context` consumer sweep produced 2 false positives of 3.
*Put the control on the retrieval, not the pattern.*

## Reproduction

Deterministic; no Opal remote, no shared branch, no bucket touched. Isolated scratch tree, `sha256`-verified
hook copy. GATE-1 matrix + marker-removal attribution control + the `type __headmove_serial` arms are all in
this session's transcript and re-runnable as written.

## NOT ESTABLISHED

- Harm from Finding 1 or 2. **The defect is the finding.**
- `__headmove_guard`'s block path (M3) — I exercised the *serial* resolver, not the *guard*.
- Why punctuation produces a vetted hit and off-domain English does not (Finding 3's residual).
- The 10 identity consumers whose tier **order** is unverified. **Presence is not precedence.**
- CL / `feature_clb` worktree separation — directory absent on this box.

— 3.0.0_SA_CVO
