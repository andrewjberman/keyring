# Session — `1.0.0_SA_CTO` (base) — the identity gate, the four NEVER-gates, and the AoR chokepoint key

**archetype:** MIXED (IMPLEMENT primary; secondary: VALIDATE, COORDINATE, SCRIBE)
**Window:** 2026-07-13 ~0510Z → ~0625Z. Fresh session; `/watcher` armed at load; ZERO crons (LD-0157).

## Headline

**Every instrument that failed tonight failed the same way, and five of them were mine.**
An instrument whose verdict *cannot see the distinction it is being asked to license*. It hit
`comp-iam` (`(action)` vs `(action, resource)`), `ps`-as-delivery-oracle, `_pid_alive()`, my own
G-A promotion path, my own AoR freshness key — twice — and finally the review that was sequencing
my gate work. **The fix is never a better comparison. It is a better identity.**

## What shipped

| Item | Commit | State |
|---|---|---|
| NFRA_IDENTITY.G-A broker PID guard | `786fb085d` | LIVE (built by 0.7.0~A, arch-gated + landed by me) |
| G-A audit denominator (guard-version + `IDENTITY_GUARD_ACTIVE`) | `462f2c44c` | LIVE |
| **F-008** spawn-agent birth pid | `bf0b4cc87` | BUILT, exercised |
| **F-009 + F-010 + NEVER#3** — `never-rules-gate.sh` | `0778215a5` | **LIVE, denied a real Bash call in-harness** |
| **F-001** safe-apply INTENT/OUTCOME + sound actor resolver | `74f30864a` | BUILT, exercised 4/4 |
| CLAUDE.md Rule 22a doctrine (3 amendments) | `7f6611ea7` | LANDED |
| AoR gate-1 brief: F1 corrected + settled key | `462f2c44c`, `0bd5343b4` | LANDED |

**All four RV-0046/0047 "RULED AND NEVER BUILT" gates are now BUILT and EXERCISED.**

## The rulings

**G-A severity (CROSS = HARD, SERIAL_HELD = ADVISORY).** I overrode the builder's direction-2.
`_pid_alive(pid)` answers *"does SOME process hold this PID"*, never *"is THAT AGENT alive"* — it
cannot separate a live incumbent from a lingering orphan or a **recycled Windows PID**. A hard
refusal there blocks a legitimate **respawn**, and the agents most exposed are the ones *recovering
from a death*. **A guard that blocks the recovery path converts a transient failure into a permanent
one.** Advisory + unconditional audit takes us from zero signal to a measurable one with no new way
to lose an agent.

**AoR F1 — the chokepoint key. Four shapes; each killed by EXERCISE, never a re-read.**
1. `as_of` (mine) → **falsified**: the pin is the *source partition*, and a partition serves many
   runs. I argued the defect *as if it were the feature* ("weekend self-agreement avoids false
   raises") — that self-agreement **is** the blindness.
2. `run_id` (CVO~B) → **falsified**: over-condemns. `--single` bypasses chain membership entirely,
   and the dispatch's own help text example (`--single INF_D_00c`) is a consumer. *A condemnation
   instrument with a destructive remedy gets disabled by whoever it wrongly condemns.*
3. `(as_of, fold_mode)` (CVO) → **falsified**: under-condemns. **6 of 69 `accounts_v2` partitions
   were REWRITTEN IN PLACE** (measured independently by me). The key repeats across different bytes.
4. **`(source_digest, fold_mode, code_digest)` — SETTLED.** Complete *because the input surface was
   finally enumerated*: `resolution == f(source_content, mode, THE CODE)`.

**And the reframe that settled it:** every key answers *"is this leftover artifact safe to reuse?"* —
a question that only exists because a chain can run without the resolver. **THE CHAIN-WIRING IS THE
FIX; THE GUARD IS THE BACKSTOP. We spent the night asking a guard to do a wiring job.**

**CLOSED by exercise at `c16b0c73b`** (CVO~B, 8/8, A3 through the dispatch). Blocker moved to **F2**,
now confirmed live and *more severe than gate-1 stated*: the `<NA>` `rep_bucket` row is **silently
dropped** at `INF_09:193` → under-counted per-advisor NNA. **Silent row loss, not a visible null.**

## Findings against my own work / the record

- **My gate-1 got F1's mechanism BACKWARDS** (predicted a loud abort; it fails **open**). 32
  adversarial agents, 3.43M tokens, and all of them reasoned about the state we are *in* rather than
  the state the *rollback creates*. **We enumerated the CODE axis and never the STATE axis.**
- **`orion-gold-dispatch.sh:396-400` asserts the guard AS ACCOMPLISHED FACT** — a guard that was never
  built and, as specified, would not have held. Third instance (`INF_A_00:233`, `INF_A_01:173`).
  **A COMMENT IS A CLAIM WITH NO VINTAGE AND NO TEST** (CTO~B). Landed in Rule 22a — and it caught
  RV-0047 within the hour.
- **RV-0047 F-009's premise is FALSE.** *"The `terraform` shim it was modeled on EXISTS at
  `.tools/terraform`."* → `file` says **PE32+ executable**. There is no shim. CLAUDE.md's NEVER#7
  says it too. **Consequence nobody drew: `.tools/` is on PATH, so bare `terraform apply` (NEVER#3)
  ran straight through, ungated — and it was not even on the overdue list.**
- **`headmove-guard` was a FALSE WITNESS.** It resolved the actor for a *destructive HEAD move* from
  the shared `.agent_context` — naming whoever ran Step E last. Demonstrated live by the new test's
  own output: it would have named `0.7.0_AE_CloudOps~A` for a move made by me. **An absent field is a
  gap; a confident wrong field is a false witness — and this one names the innocent.**
- **My own G-A promotion path was unmeasurable** (0.7.0~A caught it): the guard activates when the
  MCP server reads `server.py` *off disk*, not at the git land — so sessions on the pre-audit build
  **enforce but do not record**. A quiet log was indistinguishable from nobody measuring. Fixed: the
  rows now carry their own denominator.

## Process ruling

**COMMIT BEFORE VERIFY.** The lib moved under CVO~B **four times**; two of her citations went stale
mid-analysis, and her F2 finding was correct at her hash while an uncommitted fix already sat in the
tree. *A verifier chasing a moving tree produces findings that are stale on arrival — and worse,
findings that look like defects when they are already fixed.* That is now the binding constraint on
this release, not the code.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-freshness` | attempted on `accounts_v2` vintage | **GAP FOUND** — it takes `{chain,script,artifact,ddb,all}`; it cannot do a forensic *mtime-vs-key-date* sweep to detect in-place rewrites. Fell back to a **`# rail-checked:`** raw `aws s3 ls` (audited), which is how the 6/69 rewrite was measured. **Coverage gap worth a tool.** |
| comp-rail (PreToolUse HUD) | gated my raw `aws s3 ls` | **WORKED AS DESIGNED** — it stopped me, I reached for the comp-tool first, and only overrode with a stated why. |
| `.tools/safe-commit.sh` (`-F`) | 7 commits | PASS. Used `-F` throughout per LD-0276 — the rule I then *gated*. |
| HALT-GATE (safe-deploy push checkpoint) | blocked a push | **FIRED CORRECTLY** — unread inbox; I read, then `HALT_ACK=1`. |
| `git show <ref>:<path>` + `grep -c` | vintage checks at `c16b0c73b` | PASS — and it is what caught that CVO~B's F2 finding was hash-correct but tree-stale. |

**What worked:** the two-lane adversarial design paid for itself three times in one hour — CVO~B
falsified my key, base CVO falsified hers, she applied *his* test to *his* key and falsified that.
Base CVO **retracted his own "VERIFIED 7/7"** unprompted and recused himself as an author.
**What failed:** my own instruments, five times. **Gap found:** `comp-freshness` cannot detect an
in-place partition rewrite — the exact fact the AoR key now turns on.

## Blockers

None owned by me. AoR go-live is correctly gated on F2 + the rest of round-8.2; both gates WITHHELD.
Nothing served, switch OFF, SERVE-HELD, zero live impact throughout — and that held across four
ruling changes, which is the other thing that went right.

## Next

1. **[0.4.0_DS]** F2: honour the pin **AND** assert the read digest (structure alone cannot close the
   health-walk-back). Then **ground the blast census** — 6 more `load_resolution()` consumers load
   `accounts_v2` themselves with **zero pin refs** (`INFERRED`, not ruled; per-script grounding first).
2. **[3.0.0_SA_CVO~B]** F3/F4/F7/F8 + the 35/35 battery, at a **committed hash**.
3. **[1.0.0_SA_CTO~B]** gate-1 re-review at `c16b0c73b`; the F1 withhold lifts, the rest does not.
4. **[me]** `comp-freshness` in-place-rewrite detection (the gap this session found).
