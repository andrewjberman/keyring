# COMP-TOOL REGISTRATION CANON

**Status:** CANON — the always-followed process for landing a `comp-*` tool
**Authority:** Andrew-direct 2026-08-05 ~2015Z, VERBATIM: *"Comp-tool registration has to be a
rigid, always-followed process. We cannot have situations where we spend all this time to build this
tooling and then the tools aren't fully registered in all canonical locations as required from
comp-tooling registration canon, as well as having all relevant assets for those tools referenced
canonically with proper paths."*
**Author:** `3.0.0_SA_CVO~B`, 2026-08-06 — written immediately after registering `comp-find` and
`comp-read` end-to-end, so every step below is one I performed and every trap is one that caught me.

---

## 0. WHY THIS DOCUMENT EXISTS AT ALL

**The canon was enforced by a gate and never written down.** Before this file,
`comp-which "how do I register a new comp tool"` returned a near-tie on `comp-genesis`/`comp-kuzu` —
and **two independent agents recorded exactly that and moved on**
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_MSBEFF/nl_structured/chunk_10.txt:2260`;
`org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-18/…:51` — *"near-tie … no registration rule;
expected, used to confirm no curated route exists"*).

So the procedure lived in the gate's failure messages, discoverable only by tripping them.

> ### THE LAW THIS DOCUMENT ENCODES
> **A tool registered in 8 of 9 surfaces is not 89% registered. It is UNDISCOVERABLE — which, in a
> routing-dependent estate, is indistinguishable from unbuilt.**
>
> Measured 2026-08-05: ten `comp-pipescript` subcommand entries were added to the manifest
> (`@4b50ddcf3`) and `comp-which` **still** ranked `io` above `skipgate` for *"what would a gold
> script run skip per partition"* — because **comp-which routes from a curated keyword list, a
> DIFFERENT surface from the manifest.** Registration in the catalog does not create reachability.

---

## 1. THE SURFACES — all seven, in the order to do them

Do them in this order. Steps 1–2 are the tool; 3–7 are registration; 8 is verification. **A tool is
NOT COMPLETE until step 8 passes.**

| # | Surface | What lands there |
|---|---|---|
| 1 | `.tools/<tool>` | the executable — **and it must be TRACKED BY GIT** |
| 2 | assets (§2) | every engine/config/test the tool depends on, by canonical path |
| 3 | `org/modules/graph/comp-output-contracts.yaml` | the output contract |
| 4 | `org/modules/graph/comp-coverage-map.yaml` | the coverage ledger row |
| 5 | `org/modules/graph/graph-call-manifest.yaml` → `tools_index` | the one-line catalog entry |
| 6 | `org/modules/graph/graph-call-manifest.yaml` → `entries[]` | the routable entry |
| 7 | `.tools/comp-which` | **the curated route — the surface that decides discoverability** |
| 8 | `.tools/provision-path-shims.sh` | interpreter map, then run the provisioner |

### Step 1 — the executable

`.tools/<tool>`, `chmod +x`, ASCII-only, `#!/usr/bin/env python3` or `#!/bin/bash`.

> **GATE CATCH (hit twice, once per tool):**
> `BLOCKED: registered tool(s) do not EXIST as a runnable, tracked executable: on disk but NOT
> TRACKED by git -- absent from a fresh clone.`
> An untracked executable is a tool that exists only on your box. Staging it in the same commit as
> its registration resolves this.

### Step 2 — assets, by canonical path (Andrew's second clause)

Every artifact the tool reads or writes — engine module, config, snapshot, fixture, test battery —
must be:

- **tracked**, not device-local;
- referenced by **repo-relative canonical path** in the tool and in its contract — never by an
  absolute path, a `~` path, or a path assembled from `cwd`;
- resolved from the **module's own location**, not the caller's working directory.

> **WHY cwd IS BANNED:** a caller in `portal/` or `data/` has the wrong cwd by construction. The
> canonical resolution is from `__file__` upward — e.g. `_THIS_DIR.parent.parent.parent` for a tool
> engine in `org/modules/graph/`. A `REPO_ROOT`-style guard around a name that does not exist is
> dead code that reads as caution: `ruff` caught exactly that (`undefined name 'REPO_ROOT'`) in
> `pipeline_cli.py` on 2026-08-05.
>
> **Device-local assets are NOT registered assets.** `org/mcp/comp-tool-runs.jsonl` is gitignored;
> anything similar cannot be a tool's declared asset, because it is absent for every other agent.

### Step 3 — output contract

`comp-output-contracts.yaml`, under `contracts:`. Required: `coverage`, `blind_spots`,
`failure_direction`, `plane`, `grain`, `scope`, `vintage`, `exit_codes`.

**Enum values are canon-checked** (stage-2 vocab invariant). Current live sets:
`plane: source|projection|desired|mixed|applied` · `grain: artifact|field|partition` ·
`scope: estate|firm|pipeline|single-artifact|partition-window`. **Re-derive them from the file;
do not trust this list — it is prose and prose goes stale.**

> **THE STANDING RULE ON CONTRACTS (CVO base, and it is the point of the whole file):** a contract
> that DECLARES a denominator the tool does not actually EMIT is **worse than a missing contract**,
> because it makes the tool look audited. If the tool cannot emit its denominator, the contract says
> so. A denominator drawn from the instrument's own configuration means the instrument cannot fail
> even when it is wrong (`4.0.0_SA_CRO` §3).

> **YAML TRAP:** a backslash inside a **double-quoted** scalar is an escape. Writing `'\|'` in a
> blind-spot about regex semantics fails with `found unknown escape character '|'`. Use a
> single-quoted scalar, or describe the character in words.

### Step 4 — coverage map

`comp-coverage-map.yaml`, one row: `{ tool: <name>, role: <role>, routable: true|false,
not_homed_reason: "<why>" }`.

**`routable` is a real decision, not a formality:**

- `routable: true` — an **agent invokes it directly**. It must be reachable via `comp-which`.
- `routable: false` — an internal primitive `comp-which` *runs* on the agent's behalf
  (`comp-grep`, `comp-glob`).

> **DO NOT COPY `routable: false` BY PRECEDENT.** That file already records the cost, in its own
> words: *"an unroutable tool is one nobody finds"* — **"the door is real, the key is not."** If an
> agent is meant to type the tool's name, it is `true`.

### Step 5 — `tools_index`

One line in `graph-call-manifest.yaml`: `does:` (what it answers), `subcommands: [...]`,
`entries: [<entry-id>]`.

### Step 6 — `entries[]`

The routable entry: `id`, `use_case`, `canonical_call`, `tool`, `mode`, `layer`, `cost`,
`freshness`, `anti_pattern`, `status`, `notes`.

> **GATE CATCH (this one is subtle and it caught me):**
> `BLOCKED: 1 catalogued tool(s) do NOT surface for their own use_case: comp-find — comp-which
> returns nothing naming it.`
> My first `use_case` was prose no curated route matched, so `comp-which` **grepped** instead of
> naming the tool. **Write the `use_case` in the words an agent would actually type, and make the
> Step-7 keywords match it.** A use_case nobody can route to is a use_case nobody reaches.

> **`canonical_call` MUST RUN AS PRINTED.** Copy it, paste it, run it, before committing. On
> 2026-08-05 the documented `comp-pipescript` call was `rc=2 REFUSED` in **both** doc surfaces for
> five weeks — a code ruling had propagated to the mechanism and to neither record. The one field
> whose entire job is to be copy-pasteable was the field that was wrong.

### Step 7 — the curated `comp-which` route ← **the load-bearing step**

Add a rule tuple in `.tools/comp-which`:

```python
(["<keywords an agent would type>", ...],
 "<short label>",
 ["<canonical call>", ...],
 "<why / what it gives you"),
```

> **INSERT AT THE TUPLE'S OPENING PAREN, NEVER AT ITS LABEL.** Anchoring a text insert on the label
> line drops the new rule *inside* the preceding tuple; `py_compile` still passes and the tool dies
> at runtime with `ValueError: too many values to unpack (expected 4)`. **Syntax-valid is not
> structure-valid** — run `comp-which "<a keyword>"` after editing, every time.

### Step 8 — the shim, then RUN it

Add the tool's interpreter to `_INTERP_WIN` in `.tools/provision-path-shims.sh` — **read the
shebang, do not assume it** — then `bash .tools/provision-path-shims.sh`.

> **RESOLUTION IS NOT EXECUTION.** `command -v <tool>` proves a forwarder *file* exists; it cannot
> see that the forwarder's *target* is gone. On 2026-07-29 a probe reported `93 of 93 comp-tools
> resolve bare` while **zero of them ran**. **Actually run the tool and read its output.**

---

## 2. VERIFICATION — the tool is not done until these pass

```bash
comp-manifest-check completeness              # registration + contract + vocab + routability + existence
python .tools/comp-which-routing-test.py      # routing regression baseline
comp-which "<the use_case, in an agent's words>"   # MUST name your tool
<tool> --help                                 # exercised, not resolved
```

**`comp-manifest-check completeness` is the gate.** It already enforces registration, output
contracts, stage-2 vocab, retired aliases, subcommand declarations, existence-as-tracked-executable,
**and routability**.

> **CORRECTION ON THE RECORD (mine):** the NFRA_SCRIPTGEN spec (§C.4 item 3) proposed *building* a
> routability check — *"extend comp-manifest-check from 'registered?' to 'ROUTABLE?'"*. **It already
> exists and it already BLOCKS.** I proposed building a control that was live, and had simply never
> been pointed at me because I had never registered a tool before. Recorded here rather than left
> standing as a false gap.

### The one WARN that is not a pass

```
self-route WARN: <tool> surfaces only inside comp-which's near-tie list (never rank-1)
```

Non-blocking, and **by this document's own law it is not finished** — near-tie means an agent finds
it only if they were already close. Both `comp-find` and `comp-read` currently carry it, alongside
~11 others. Treat it as the last step, not as noise.

---

## 3. THE TWO-PHASE COMMIT (unavoidable, and legal)

Registration touches `org/modules/graph/` — **the rule bank** — so the `comp-system` gate blocks:
regenerating `06_current_state` would have to compile an **uncommitted** source, i.e. launder
unlanded work into a committed artifact. It correctly refuses. Land-then-recompile is two-phase **by
necessity** (LD-0362), and the override is the legal path, not a lapse:

```
system-current-override: STRUCTURAL-TWOPHASE/rule-bank -- <what landed>
```

**Then discharge it in-session** with the `comp-system` regen commit. **An undischarged STRUCTURAL
override is the discipline event — the override itself is not.**

> A good sign the registration is real rather than declared: the regen's own counts move.
> comp-find moved `tools_index 70 -> 71` and `ledger_union 91 -> 92`; comp-read moved them to
> 72 and 93. Prose registration moves neither.

---

## 4. THE CHECKLIST

```
[ ] 1  .tools/<tool>          executable, chmod +x, ASCII-only, TRACKED by git
[ ] 2  assets                 tracked, canonical repo-relative paths, resolved from __file__
[ ] 3  comp-output-contracts  coverage/blind_spots/failure_direction/plane/grain/scope/vintage/exit_codes
[ ] 4  comp-coverage-map      row + routable decided on purpose (not copied by precedent)
[ ] 5  tools_index            does / subcommands / entries
[ ] 6  entries[]              use_case in an agent's words; canonical_call RUN AS PRINTED
[ ] 7  comp-which             curated route, inserted at the tuple's OPENING PAREN
[ ] 8  provision-path-shims   interpreter from the shebang; provisioner RUN; tool EXERCISED
[ ] 9  comp-manifest-check completeness            -> PASS
[ ] 10 comp-which-routing-test.py                  -> PASS
[ ] 11 comp-which "<use_case>"                     -> names your tool (rank-1 is the bar)
[ ] 12 two-phase override taken AND DISCHARGED in-session
```

---

## 5. WHAT THIS CANON CANNOT DO

It cannot make a tool *good*. It makes a tool **findable, declared, and honest about its own
coverage**. A tool that passes all twelve boxes and lies about its denominator has passed
registration and failed the thing registration exists to protect — see the `deployed` false-clean
(`rc=0` with an all-zero summary, `@6fb81a231`), which was a fully-registered tool.

**Registration is necessary and never sufficient.**

— 3.0.0_SA_CVO~B
