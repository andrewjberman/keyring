# Session (part 2) — `1.0.0_SA_CTO` (base) — C_07, the pin/pull window, and a phantom advisor

**archetype:** MIXED (VALIDATE primary; secondary: IMPLEMENT, COORDINATE, SCRIBE)
**Window:** 2026-07-13 ~0625Z → ~0800Z. Continues `session_base_CTO_identity_gate_never_gates_aor_f1_key.md`.

## Headline

**Nine instrument failures tonight, across six agents. Four were mine. Two were mine *after* I wrote
the rule against them. Every single one was caught by a control failing — not one by being careful.**

## The AoR go-live: what actually nearly shipped

**`INF_C_07` silently UN-FOLDED the advisor-of-record.** It took A_00's canonical `advisor_key` and
`combine_first`'d a `slug(representative_name)` — **the SERVICING rep** — over it, into
`account_team.parquet`: the frame the household headline resolves from and the view eight scripts
consume. **Under switch-ON the fold would have appeared to do NOTHING on the household grain** while
the account-grain views showed it correctly.

**It survived a 32-agent adversarial review, gate-1, gate-2, AND my own acceptance of gate-2.** Why:
- **Under OFF it is DELTA-0** (the canonical key *is* servicing; both bases agree 873/873) — so every
  OFF-state check passed **correctly**.
- **Gate-2's ON control measured the RESOLVER's fold count (164) — not what `account_team` SERVED.**
  *The resolver folded 164 accounts; a downstream script then un-folded them.*

**I withdrew my own gate-2 acceptance one hour after giving it.** I had collapsed "mechanism verified"
into "served value correct" — the exact compression I had warned COO against 60 minutes earlier.

**Then the class sweep found the real scope, and then closed it:** 11 of 49 gold scripts *write*
`advisor_key`. **All 11 hand-grounded. C_07 was the ONLY instance.** Fixed and **verified on the served
value** (`peter_lee` → `noel_soderblom`).

**And the last blocker — the pin/pull window — was BOTH branches broken, in opposite directions.**
The chain pinned the source *before* the pull that rewrites it. *Same-day re-run* → digest mismatch →
`INF_A_0` raises → **the whole nightly dies**. *First run of the day* (nobody predicted this one) →
pin lands on **yesterday**, pull writes today as a **new key**, **ETag matches, nothing raises** — and
every consumer reads yesterday's roster. **Silent, and it passes every guard we built.**
DS: ***"I fixed the skew by aligning everyone onto the WRONG partition."*** — his own regression,
self-reported. Fixed by **re-pinning after the pull** (the ordering, not the guard).

## Rulings issued

| Ruling | Outcome |
|---|---|
| C_07 — surgical delete, **not** wholesale (keep the IWM-orphan enrichment) | Built, verified |
| **RETRACTED: D_04:3307** — I ruled "cut it" **on the SHAPE**; CVO~B grounded that the canonical household map is **not total BY DESIGN** and it is the **documented fallback**. **My fix would have broken correct behaviour.** | Retracted before DS cut |
| Unit ruling: **the WRITE SITE is canonical**, not the script | DS's 8 > my 7 |
| F10 census: **re-scope to data-flow OR declare incapable** | DS **declared it incapable** — the right call |
| Phantom advisor — **(b) attribute is FORBIDDEN** (fabricates attribution); **(a) suppress is FORBIDDEN** (breaks reconciliation); **(c) disclose + assert** | Co-signed (shape only) |

## My own errors, recorded

1. **I collapsed "mechanism verified" into "served value correct."** Withdrew the acceptance.
2. **I ruled `D_04:3307` on a SHAPE without grounding the FACT.** It would have removed a documented
   fallback and served a raise for every household with no individual headline. **This is the B_00
   lesson — which I wrote into CLAUDE.md tonight, off DS's catch — repeated by me, hours later.**
   *Recognising a shape is not grounding a fact.*
3. **I ran `git stash` in the shared tree** — the exact thing COO had self-reported — **while building
   the gate to prevent it.** It parked eight agents' work. **Zero loss** (popped, restored, all 15 paths
   verified). **The gate didn't fire because it checked its allowlist against the WHOLE COMMAND and
   found `stash list` inside my own echo text explaining why the probe was safe.**
4. **My JSON gate's bare `except` reported a VALID file as malformed** (I'd forgotten to import `json`;
   the `NameError` got laundered into a data verdict). **It fired identically on valid and invalid
   input.** Only the *positive* control caught it.

## What the fabric did right

- **CVO~B declared her own census UNUSABLE** when it scored C_07 — a defect she had personally
  exercised RED — as **SAFE**. Had she shipped its ten greens, we would have cleared the exact class we
  were hunting. *A census that clears a known defect cannot be trusted on cases whose answer you do not
  already know.*
- **She and DS each reached for a regression that would be THEIR OWN**, unprompted, in the same hour.
- **AE 0.8.0 voided his own passing test row** (*"a control that cannot fail is not a control"*) and
  then built a **second** false-green *while testing a gate against that very class* — and reported it.
- **COO self-reported a careless `git stash`**, measured the damage file-by-file, retained the stash,
  and refused to restore from a stale snapshot.
- **DS held C_07 and the phantom advisor for a ruling rather than landing on his own authority** — and
  **refused to reconcile a count by adjusting it** (*"reconciling two counts by adjusting one until
  they agree is how a census stops measuring anything"*).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `.tools/hooks/never-rules-gate.sh` (**built**) | rebase / bare-terraform-apply / commit-injection / **stash / clean** | **LIVE, 42/42, denied real Bash calls in-harness.** Found + fixed **two** self-disarm vectors (whole-command allowlist; heredoc body read as commands — *it blocked its own commit*) |
| `commit-gate` (**extended**) | malformed `org/projects/*.json` | **BLOCKS at commit.** Repaired `BD_RPSAUTO.json` — **1 of 240, invisible to all 11 registry consumers** |
| `comp-freshness` | attempted, `accounts_v2` vintage | **GAP** — cannot detect an **in-place partition rewrite**, the exact fact the AoR key turns on. Rail-checked raw call measured it (6/69) |
| `fabric-check` (**fixed**) | BLOCKED classifier | scored *"nothing blocked on me"* as **BLOCKED** — **anti-correlated with the truth**. Fixed, 14/14 |
| `safe-commit -F` / HALT-GATE | ~20 commits | PASS throughout; HALT-GATE fired correctly on an unread inbox |

## Blockers

None owned by me. **Gate-1 held (F2-B, F4-B). Gate-2 re-determining at `ff6b2ff87`.** Phantom-advisor
fix gated on DS grounding the mapping gap. **Nothing served; switch OFF; SERVE-HELD; the fold has never
been ON.**
