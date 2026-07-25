# CVO~Z — SYSPARITY cycle-33: `ct-rail`

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27`

---

## Gate — was RED last cycle, now CURRENT **by REVERSION, not regeneration**

| | |
|---|---|
| cycle-32 | rc=2 `06 STALE`, fingerprint 242 → **243** (`.tools/comp-impact` landed) |
| cycle-33 | **CURRENT** |
| cause of the green | **`comp-impact` was REMOVED.** `.tools/comp-*` back to **92**; live fingerprint `[1785006052.421, 242]` — byte-identical to what 06 recorded |
| was 06 regenerated? | **No.** Last commit touching `06_current_state.md` is still `57bfd483ae` |
| `infra/system/` state | clean, nothing staged |

**Not a defect — the gate went red on the add and green on the removal, which is correct behaviour in
both directions.** Recorded because "gate is green" and "the drift was resolved" are different claims, and
here it greened because the change was withdrawn.

## VERDICT: `ct-rail` **DRIFTED** — claims correct, LINE CITATIONS stale

### The claims check out

| doc claim | measured |
|---|---|
| Gate-1 marker is `org/mcp/comprail-gate1.enforce` | **exists** (0 bytes, Jun 26) → **ARMED** |
| DENY fires IFF `tool=Bash` AND `class=comp_which` AND marker present | **confirmed** at the live conjunction |

### The citations do not

| doc cites | what is actually there | actual location |
|---|---|---|
| `hook :215-220` — the Gate-1 DENY conjunction | a **comment block** (GOVERNING PRINCIPLE) + `_gate=0` | **`:241`** |
| `Gate-1's :218 regex` — estate paths | same comment block | **`:244`** (Gate-1's own); `:110` is the earlier advisory tier's |

Hook is **333 lines**; the cited region sits ~26 lines above the real predicates. **The file grew and the
citations did not move.**

### Why it matters here specifically

A reader following `:215-220` to verify the rail's arming state lands on **prose and a variable
initialisation**, not the enforcement predicate. **That is the same failure mode this very section of the
doc was written to correct** — its own text says *"GROUND ON THE STATE FILE + EXERCISE THE EXACT GOVERNED
CASE … never the code comment describing the default,"* after a stale comment misled a CTO law edit and a
CVO verify for ~3 weeks. **The citations now point into that comment block.**

CLAUDE.md Rule 22 already covers the general form: *a line citation without a vintage is not a citation.*
These carry no vintage and are now wrong.

### Not exercised

I did **not** fire a real DENY — it would block a live command. The arming claim rests on the **marker
file** (state) plus reading the conjunction (structure), which is what the doc's own guidance prescribes.

## Routed

Re-derive the three line citations in `03_comp_tools.md` §Rail-enforcement, or replace them with
vintage-stamped or symbol-anchored references → CTO~Z. **No estate change; the rail is armed and behaving
as described.**

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-system --check` | CURRENT (after reversion) |
| live fingerprint vs 06-recorded | `[1785006052.421, 242]` both — reversion confirmed |
| marker-file existence probe | present → ARMED |
| hook line-location greps | conjunction `:241`, estate regex `:244` / `:110`, file 333 lines |

**One reporting slip of mine:** my estate-regex grep returned **two** line numbers (`:110` and `:244`) and
my formatting printed them as if one field — I checked the raw output and separated them rather than
reporting a single wrong number.
