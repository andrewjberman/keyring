# The 3-state freshness contract, wired -- and a CSE sweep that overturned its own premise

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE

**Agent:** 0.8.0_AE_CloudComp
**Date:** 2026-07-09
**Window:** 2026-07-09T19:45Z -> 20:45Z (continues `nfra_graphs_p0p1_existence_invariant_and_denominator_rule.md`)
**TO:** none -- Andrew-direct NFRA-first drive; CTO GO 20260709T201214Z

---

## Summary

CTO GO'd a 4-state freshness contract, then set a hard precondition: **audit the population, do not
inherit it from the token list.** The audit changed his GO in two ways and changed the contract from
four states to three. Nothing was wired until he re-ruled. Then five commits.

Separately, answered a read-only CSE sweep that was blocking `NFRA_SEMCTL`'s close. **The premise was
wrong** -- the artifact everyone measured is not a CSE log.

---

## The audit (CTO's hard precondition), and what it changed

| finding | evidence | consequence |
|---|---|---|
| **`--fresh` is a NO-OP alias of DEFAULT** | `graph_cache.load()` takes ONE branch for DEFAULT/FRESH; exercised across all 3 reachable states + a FORCE control that CAN see a difference | contract is **3 states, not 4**. `comp-platinum` -- the reference we were told to copy -- ships a dead flag |
| **`comp-aws derive` is a PURE PRODUCER** | `comp_aws_cli.py` has no persistent cache, only in-process memo dicts | CTO's GO had wrongly placed it IN the contract |
| **the trace cache backs FIVE launchers** | `cli.py::_get_graph` fronts comp-build/trace/blast/diff/xref; the token list named ONE | four cache-backed rebuild-capable tools were silently outside the contract |
| **`comp-graph status`'s TTL verdict is not predictive** | exercised at `age=4000s, drift=0`: status says "STALE (next call rebuilds)", actual = SERVED | wrong in BOTH directions; `_TRACE_TTL=300` re-models a predicate the enforcing code never evaluates |

Root cause of the `--fresh` collapse is honest history: NFRA_GRAPHUNI P2/D2's head-pin **correctly**
made DEFAULT honor the source fingerprint (killing the stale-cache-phantom class) and in doing so
collapsed FRESH into DEFAULT. Nobody retired the flag.

**CTO accepted the audit in full** and noted he had inherited the token list he told me to derive from
capability -- the rule violated in the message that issued it.

---

## Landed (all on origin/CLOUD)

| commit | what |
|---|---|
| `01b6807fb` | `comp-system --check` binds the PROPERTY, not `as_of == HEAD` |
| `2ff96d734` | 3-state contract on comp-trace/blast/diff/xref + `_freshness_probe()` + the exit-code fix |
| `44d93e9a1` | `graph_cache`: `--fresh` WARNS instead of lying |
| `735a4d86d` | regenerate `06_current_state` (the chore that turned out to be a finding) |
| `8ad26c612` | commit-gate's BLOCKED summary named one of three assertions as the cause of all of them |

### The oracle that could never be green (`01b6807fb`)

`check_stale()` returned 0 iff `emitted.as_of_head == current HEAD`. But **landing the artifact
requires a commit, and that commit advances HEAD.** Exercised:

    comp-system --check   "06 CURRENT"                                     rc=0   <- uncommitted only
    safe-commit           [CLOUD 735a4d86d]
    comp-system --check   "06 STALE: as_of=fe02f71e5 vs HEAD=735a4d86d"    rc=1

It reported the freshly-regenerated artifact STALE against the very commit that shipped it. A signal
that is **always RED** carries exactly as much information as one that **never fires** -- both are
checks whose output is independent of the property. CTO banked the formulation.

Repointed to `(source fingerprint drift) OR (TTL exceeded)`, reusing `graph_cache.source_fingerprint`
-- **the same expression the caches enforce**, imported never forked (MSTR's ratified rule). T5, the
decisive test: `--check` now survives its own commit (`as_of=b7813dfd9`, `HEAD=01b6807fb`, rc=0).

### The exit-code collision, found by exercise (`2ff96d734`)

argparse exits **2** on a usage error. The contract reserves **2** for STALE. `comp-trace --check`
hit "the following arguments are required: query" and exited 2 -- indistinguishable, to a CI job, from
a stale cache. **The probe had never run.** Worse: my own first drift test "passed" with rc=2 for
exactly this reason -- a coincidence, not a test. Fixed both ways: the positional is `nargs='?'` so a
PROBE needs no target, and `_ContractParser.error()` exits 1 (a usage error is a tool failure).

---

## The CSE sweep: the premise was wrong

CTO asked, read-only: *do any CSE producers attach `execution_meta`, or is the promote emitter the
only omitter?* -- citing a 4-event file with zero timestamps and duplicate `event_id`s.

**`promote_materialize_cse.jsonl` is not a CSE log.** Its keys are `commission_id / cse_kind /
lifecycle_verb / subject_ref / vintage ...` -- a flattened **inspection projection**, written after
`validate_or_raise`. A CSE has `producer / compiler / transformation / execution_meta / head /
qualifiers`. The filename says `_cse.jsonl`; the contents are not CSEs. My own first sweep reported
"35 events, 6 with execution_meta" -- **conflating two schemas into one denominator.** Classifying by
SHAPE before counting changed the answer completely.

**Every real CSE emitter attaches a non-empty timestamp** (agent/deploy/frontend_coevolution/graphhead
via `_now_iso()`; promote via `_stamp()` from the commission vintage). Not an emitter defect, not a
contract defect in the data I can see.

**But the latent contract hole is real**, and it composes from three source-confirmed facts:
1. `validate()` never inspects `execution_meta` (the author says so: *"timestamp is not validated"*).
2. `partition_key()` derives `event_date = ts[:10]` from that unvalidated field -> `""` when empty.
3. Iceberg's `event_date` is `required=True` -- and `""` **satisfies** it. Required binds NULLABILITY
   (a proxy), not presence-of-a-date (the property).

So any producer that forgets `_stamp()` emits an unorderable, empty-partition event that passes
`validate()` and satisfies a required column. `comp_promote_materializer` builds exactly such a CSE
today; only a call in a *different module* saves it.

**`event_id` is a LABEL, not a key.** Iceberg has no primary key; `append_cses` is append-only with no
dedup; the projection carries byte-identical duplicates; 25 of 29 projection events have no `event_id`
at all. Uniqueness is enforced by nobody.

**Denominator stated, and what I could not reach:** 15 code producers swept; 5 logs (1 CSE-shaped --
the synthetic seed -- and 4 projections). **I did not query the live Iceberg `globgrph.cse` table.** So
I cannot say whether any real row carries `event_date=""`. I reported "none of the producers I swept
omit it" and explicitly refused to report it as "no unordered row exists."

---

## Corrections against myself (continuing the pattern; CTO hit the same class twice)

1. `touch`ing a source did NOT drift the trace graph -- **correct behaviour**: `check_node_freshness`
   binds CONTENT-SHA, not mtime. My test was wrong, not the tool.
2. Then I drifted `comp_system.py` and still got rc=0 -- because it is **not an indexed node**.
3. My first CSE sweep conflated two schemas into one denominator.
4. My W605 first count (19 violations / 8 files) was polluted by summary + syntax-error lines. Real:
   **14 / 4**, of which **12 first-party in 3 files**.
5. I forced commit-gate onto an **untracked** vendored file it would never see in a real commit, and
   briefly mistook my own probe for a vendor-detection defect. **Non-finding, reported as one.**
6. My `echo "=== is \`time\` imported?"` **executed `time`** -- one minute after discovering the
   backtick hazard.

**CTO's own instrument lied twice today**: his `rc=0` on `comp-system --check` was `head`'s exit code
(`| head -3; echo rc=$?`), and his "chore, not a finding" call was ungrounded. He declined my grace and
corrected both in the record.

**Banked: when a tool looks mute or a check looks green, check the pipe before you check the tool.**

---

## SAFETY: commit messages are shell-evaluated

A backtick inside a double-quoted `-m` is **command substitution**. It:
- **silently corrupted `8ad26c612`** (mine -- the subject of a sentence is gone from the record), and
- **corrupted `442984f04`** (CTO's -- `comp-which` and `comp-system --check` OUTPUT was substituted
  into his commit message where his sentences were), and
- can **execute arbitrary commands** with the agent's credentials at commit time.

**It cannot be gated in `safe-commit`** -- bash substitutes before the wrapper sees the string. CTO's
ruling: build it in the **PreToolUse hook**, the only layer holding the un-substituted text.
Convention effective immediately: `-F <file>` or a single-quoted heredoc, never `-m "..."` with
backticks. Of the last 60 commits only **8** carry a surviving literal backtick, and the corrupted and
the never-used cases are **indistinguishable after the fact** -- we cannot know how much of the audit
trail is missing text. Not "no damage," but "undetectable."

Every commit from `01b6807fb` onward was authored via `-F`.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-system | FIXED | `--check` was unsatisfiable-by-construction; now survives its own commit |
| comp-build/trace/blast/diff/xref | WIRED | 3-state contract; `_freshness_probe()` is the one enforcing expression |
| comp-platinum | PASS | `--fresh` vs default output byte-identical (X4) -- the no-op, now announced |
| comp-graph status | **DEFECT** | TTL verdict not predictive; awaiting 0.7.0 co-sign to fix |
| comp-manifest-check / comp-coverage-check | PASS | denominators printed (prior window) |
| commit-gate / safe-commit | PASS + FIXED | mislabelled BLOCKED summary corrected; `-F` path exercised |
| ruff (W605 measurement) | GO | 12 first-party violations, 3 files -- CTO GO'd, gated on DS's fixes |

**What worked:** the audit CTO demanded before wiring. It caught a no-op flag, a mis-classed tool, and
four tools outside their own contract -- none of which any amount of reading would have surfaced.

**What failed:** six of my own measurements (above), all caught before routing except one, which a peer
closed.

**Gap found:** `ruff`'s default select omits W605, so `commit-gate.sh` is blind to invalid escape
sequences fabric-wide.

---

## Blockers

**None.** Two items sit with their owners, both by design:
- `comp-graph status` (items 1+2) -- **0.7.0_AE_CloudOps co-sign requested**; CTO authorized, I will not
  touch his tool without his word.
- `W605` in commit-gate's ruff select -- CTO GO'd it "in the SAME commit as DS's fixes" so HEAD never
  goes red. Gated on **0.4.0_DS_ClientPlatform**.

---

## Current State (handoff surface)

- **Contract LIVE on 7 tools**: default / `--check` (0=fresh, 2=stale, 1=error) / `--force`.
  `--fresh` accepted with a deprecation WARN, removed next cycle.
- **`_freshness_probe()`** (`cli.py`) is the single enforcing expression for trace-graph freshness;
  `comp-build --check` was re-pointed at it. `comp-graph status` must CALL it, not re-model it.
- **`comp-build` intentionally has no `--force`**: its default IS the rebuild verb. Adding one would be
  another lying affordance. Flagged to CTO as a refinement of my own audit.
- **CSE**: `NFRA_CSE` should NOT reopen on the promote evidence. `NFRA_SEMCTL`'s close condition is
  still unfalsifiable, for a different reason: it would certify against a lossy projection with a
  non-unique label. Re-specify against the Iceberg table.
- Watcher: persistent Monitor `bc0flur89`. Zero crons.

---

## Next Steps

1. **[0.7.0_AE_CloudOps]** co-sign `comp-graph status`: (a) call `_freshness_probe()` instead of
   `_TRACE_TTL`, (b) print three named classes (contract / pure producers / query-only).
2. **[0.4.0_DS_ClientPlatform]** the two independent C_05 docstring fixes (bd, cot -- never mirrored) +
   confirm `edge_scraper_original.py` is reachable. Then I add W605 in the same commit.
3. **[1.0.0_SA_CTO]** disposition on the CSE latent hole: `validate()` rejects an empty
   `execution_meta.timestamp`, or `partition_key()` refuses `event_date=""`. One line, fail-closed.
4. **[1.0.0_SA_CTO / 0.7.0_AE_CloudOps]** the backtick PreToolUse hook, routed with 0.7.0's hook bundle.
5. **[2.0.0_SA_COO~B]** AC1 registry reconciliation (42 tools_index vs 60 coverage-map). Sequencing ask
   outstanding. Also: reap the SFNBRIDGE TO.
6. **[me]** on 0.7.0's word: `comp-graph status`. Driving, not idling.
