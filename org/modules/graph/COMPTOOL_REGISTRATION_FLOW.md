# The Canonical comp-tool Flow -- Create / Revise / Register / Exclude

**Status:** CANONICAL -- MSTR-canonized 2026-07-18 (0.0.0_AB_MSTR) per LD-0313; CTO arch-gated
(1.0.0_SA_CTO, GO 143314Z); authored by 0.8.0_AE_CloudComp~B (NFRA_COMPREG, Andrew-direct @04bee845a).
**THIS FILE IS THE CANONICAL HOME:** `org/modules/graph/COMPTOOL_REGISTRATION_FLOW.md`, colocated with
`comp-tools.yaml` / `graph-call-manifest.yaml` / `comp-coverage-map.yaml`. **Source draft (historical):**
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_COMPREG/CANONICAL_COMPTOOL_FLOW.md` @990927f89.
Referenced from `0.8.0_AE_CloudComp/prompt.md`. The general ANY_EXEC_OR_AE registration grant
(graph-call-manifest.yaml) is LIVE per LD-0313 (additive-only; engine globs preserved).

**One sentence:** a comp-tool is not "made" when its script runs -- it is made when its **executable and its
registration land in ONE commit** such that `comp-which` routes an agent to it and the command actually
runs; this document is the ordered, repeatable process that produces that state and the gate that proves it.

**Why a written flow at all** (the estate this governs): 77 tracked `comp-*` launchers today, up from 62 on
2026-07-14 -- "constantly adding more" (Andrew). The *mechanism* to enforce registration already exists
(the completeness gate, section 1); what did not exist was a documented *process* an author follows so the
next tool does not rediscover the two gate-blocks and the chicken-and-egg by trial. This is that process,
EXTRACTED from real registrations (no-retrofit): comp-iam-usage + comp-debris (NFRA_DECOMTOOL) and
comp-kuzu-full/comp-kuzu-inc (NFRA_KUZUSPLIT-P1) are the worked examples in section 8. *(Both were RETIRED 2026-09-02 -- consolidated onto `comp-kuzu --mode inc|full`, NFRA_COMPEFFICACY unit 2, Andrew-approved; the example stands as the RECORD of a CREATE-via-SPLIT, and its inverse -- RETIRE-via-CONSOLIDATE -- is that unit's commit.)*

---

## 1. What "REGISTERED" means -- the completeness gate family (the enforcing mechanism)

`comp-manifest-check` (engine `org/modules/graph/manifest_check_cli.py`) runs a **five-member completeness
family** at commit time. Every member is **deterministic, ramp-exempt (blocks regardless of the config
`mode: advisory` knob), fail-closed (an unevaluable member does NOT read as passed), and substrate-scoped
(it evaluates only when the commit touches a file that can INTRODUCE its defect, and derives its universe
from the files being COMMITTED, never `os.listdir` -- we share one worktree).** The five members ARE the
definition of "registered":

| # | Member | Asserts | Substrate that triggers it | Fix if it blocks |
|---|---|---|---|---|
| 1 | **routable** | every `tools_index` tool is a live routing candidate (`routable=true` in the capability provider) | graph-call-manifest.yaml, comp-coverage-map.yaml, comp_capability_provider.py | add the coverage-map role to `_ROUTABLE_META_ROLES`, or declare `routing_exempt: <reason>` |
| 2 | **placement** | a comp-tool has exactly ONE coverage-map home (`tools[]` xor `meta_tools[]`) | comp-coverage-map.yaml, any `.tools/comp-*` | add it to `tools[]` (single-surface) OR `meta_tools[]` (cross-surface/tooling) -- never both, never neither |
| 3 | **self-routes** | a catalogued tool SURFACES for its own `use_case` via comp-which (hard-block on MISS; WARN on NEARTIE) | comp-coverage-map.yaml, comp_capability_provider.py, .tools/comp-which, manifest `entries:`/`tools_index` | give it distinctive curated vocabulary in `.tools/comp-which`; do NOT let its catalog text name a sibling tool; re-run `comp-which-routing-test.py` |
| 4 | **existence** | registered ⟹ the executable EXISTS on disk AND is git-tracked (two legs) | graph-call-manifest.yaml, any `.tools/` | create the launcher and **force-add** it (`git add -f`) -- `.gitignore` ignores `.tools/` wholesale, so a plain `git add` silently no-ops |
| 5 | **registration** | disk ⟹ registered: every tracked `comp-*` is a `tools_index` key OR in `excluded_not_graph_use_cases` (with a reason) OR the `tool:` of an `entries:` row -- AND is in the coverage-map union | graph-call-manifest.yaml, comp-coverage-map.yaml, any `.tools/comp-*` | register it (section 4) OR exclude it with a reason (section 7) |

Members 4 and 5 are **inverses** and this is the load-bearing pair (see section 3): member 4 says a
registration with no runnable tracked executable is a lie; member 5 says a runnable executable with no
registration is invisible ("a tool nobody can find is indistinguishable from a tool that was never built").

**Run it by hand any time:** `comp-manifest-check completeness` (whole estate, legible PASS with denominator)
or `comp-manifest-check completeness --only <routable|placement|self-routes|existence>`. On a commit it runs
automatically inside `safe-commit`. **The gate is the check -- do not hand-assert "registered".**

**Relationship to comp-which -- router vs gate, do NOT conflate the two.** `comp-which` is the RUNTIME router:
at QUERY time it surfaces the top-N high-confidence tools for a plain-English question -- it is what an agent
USES. `comp-manifest-check` routes nothing; it is the COMMIT-time gate that guarantees the router's candidate
POOL is complete and honest, so a tool can never be half-registered -- **built-but-unfindable** (invisible to
comp-which), **registered-but-broken** (comp-which routes to a call that fails), or **homed-but-dropped** (the
routable filter removes it before scoring). They are coupled by PURPOSE, not by code path: **one surfaces, the
other polices.** This is exactly why "a comp-tool is MADE when its registration lands," not when its script
first runs -- the gate is the proof the surfacing pool has no phantoms or dead links. (It is a *commit-time*
control, and per the intro it is **substrate-scoped** -- it fires only when the commit touches a file that can
introduce a defect -- and **fail-closed** -- an unevaluable member reads as FAILED, never passed.)

**Each member guards ONE registration PART -- skip a part, its member blocks.** Read the table forward and it
is member -> substrate; read it BACKWARD and it is the registration checklist, so whichever part you skip is
the member that stops you: no tracked executable -> `existence`; executable but unregistered -> `registration`;
registered but zero/two homes -> `placement`; homed but not `routable: true` -> `routable`; registered but
comp-which cannot surface it for its own use-case -> `self-routes`. You cannot commit a tool that fails any of
these (barring an audited `override`, whose over-use is monitored). So the canonical flow's parts (section 4)
and this gate are two sides of ONE coin -- the flow is what you do; the gate is the proof you did all of it.
*(Worked live 2026-07-21 building comp-clobber: a grain-map-only registration -- calibration, not a real home
-- was caught by `routable` as `ABSENT-FROM-PROVIDER`; a `meta_tools` home with `routable: true` cleared it,
and `existence` then held until the executable was `git add -f`'d in the atomic bundle.)*

---

## 2. Decide the DISPOSITION first (three outcomes)

Before touching any registry, decide which of three homes the tool takes. This choice determines the rest of
the flow.

- **ROUTABLE** -- a graph-query / inspection use-case an agent should be ROUTED to by a plain-English
  question. Gets the full registration (section 4): tools_index + entries row + coverage-map home +
  `routable: true` + a comp-which curated route. *(58 of 77 tools today.)*
- **ENTRIES-ONLY** -- registered and homed, but NOT a first-class `tools_index` rank target: a subcommand
  variant, a split sibling, or the router itself. Gets an `entries:` row + a coverage-map home, no
  `tools_index` key. *(3 today: comp-describe, comp-state, comp-which. comp-kuzu-full / comp-kuzu-inc were ENTRIES-ONLY until their retirement 2026-09-02.)*
- **EXCLUDED** -- NOT a graph-query use-case at all: an enforcement gate (comp-manifest-check,
  comp-surface-check, comp-*-gate), a worklist producer (comp-canon-motif), a graph producer/write-path
  (comp-stitch-refresh), an on-rails search/inspection primitive (comp-grep, comp-glob, comp-imgread), or a
  context/session primitive (comp-to). Gets ONE line in `excluded_not_graph_use_cases` **with a reason**
  (section 7). *(14 today.)*

**Decision rule:** *Would an agent reach this by asking comp-which a question?* If yes and it should rank ->
ROUTABLE. If yes but it is a variant/sibling/the router -> ENTRIES-ONLY. If it is police, a producer, or a
primitive the router RUNS rather than routes TO -> EXCLUDED.

---

## 3. The ATOMIC-BUNDLE law (the ONE deterministic rule -- resolves chicken-and-egg + the AE-vs-exec boundary)

**A new comp-tool's executable and its registration MUST land in the SAME commit.** This is not a
convention; it is forced by the gate, and it is the single rule that dissolves both tensions base flagged:

1. **Why it is forced (the two gate-blocks close on each other):** member 5 blocks committing the executable
   unless the registration is present in that commit (disk-implies-registered). Member 4 blocks committing
   the registration unless the executable exists on disk AND is git-tracked (registered-implies-exists,
   force-add). Neither half is committable without the other -> they land together or not at all. There is no
   "register first, add code later" and no "add code first, register later" -- both are gate-blocked. The
   *only* passing state is the atomic bundle. **This is the answer to "registration before code?" -- it is
   registration WITH code, one commit** (CTO seam: *exec-lands-the-bundle*; *registered-implies-reachable*;
   *existence-needs-a-tracked-executable*).

2. **What the bundle contains** (a ROUTABLE tool -- the maximal case):
   - the launcher `.tools/comp-<name>` (+ any `.tools/comp_<name>.py` engine) -- **force-added**
   - `graph-call-manifest.yaml`: a `tools_index` key + one or more `entries:` rows
   - `comp-coverage-map.yaml`: exactly one home (`tools[]` or `meta_tools[]`) with `routable: true`
   - `.tools/comp-which`: a curated routing tuple (keywords -> the tool)
   - (if a new meta-role) `comp_capability_provider.py`: the role in `_ROUTABLE_META_ROLES`

3. **Who may commit the bundle (the AE-vs-exec boundary):** `.tools/` is gitignored and the registries under
   `org/modules/graph/**` are owned-path-gated. Today `org/modules/**` is `ANY_EXEC` (excludes AE), so an AE
   authoring a tool cannot self-commit the bundle -- an EXEC (CTO/COO) lands it, or a grantor carves it out.
   **NFRA_COMPREG's governance deliverable (section 6 / deliverable 5) grants `0.8.0_AE` an
   `ANY_EXEC_OR_AE` ownpath over the registration surface** so the AE lands its own bundle -- **additive-only,
   preserving every deliberate exec-lock** (the debtscan do-er-gate, comp_system.py, etc.). Until that grant
   lands, the boundary rule is: **AE authors + stages the full bundle and hands the exact pathspec to an EXEC
   to commit** (the DECOMTOOL precedent: comp-iam-usage engine folded by CTO under single-editor SoD).

**The deterministic checklist form (an agent follows this without rediscovering the gate-blocks):** *stage
everything in section 3.2, run `comp-manifest-check completeness`, commit the whole set in one `safe-commit`
pathspec.* If any member blocks, its own output names the exact fix; add it to the same staged set. Never
split the bundle to "get the code in first."

---

## 4. FLOW: CREATE a new comp-tool (ordered)

0. **Disposition** (section 2). If EXCLUDED, skip to section 7.
1. **Build the executable.** Launcher `.tools/comp-<name>` (thin shim -> a `.py`/`.sh` engine is the norm;
   see `.tools/comp-manifest-check` for the shim shape: `cd`/`dirname`/`pwd`/`python` only, Rule-16 clean).
   Include a `self-test` subcommand where the tool makes a falsifiable claim (the completeness gate itself
   ships one; a control that cannot fail is not a control).
2. **Register across the surfaces** (all in the working tree, not yet committed):
   - **`graph-call-manifest.yaml` `entries:`** -- one row per use-case: `id` (`<layer>.<domain>.<slug>`),
     `use_case` (what it answers), `canonical_call`, `tool`, `mode` (query/rebuild), `layer`, `cost`,
     `freshness`, `anti_pattern`, `status: canonical`, `notes` (the comp-which routing phrase +
     discriminator vs any sibling). *Exemplar: `cloud.iam.usage_coldness`, section 8.*
   - **`graph-call-manifest.yaml` `tools_index:`** (ROUTABLE only) -- one compact line:
     `comp-<name>: { does: "...", subcommands: [...], entries: [<id>, ...] }`.
   - **`comp-coverage-map.yaml`** -- exactly ONE home: `tools[]` (single surface) or `meta_tools[]`
     (cross-surface / tooling-layer), carrying `tool`, `role`, `routable: true`, and -- if it shares a
     `touches_resource` with a sibling -- a `distinct_from` record naming the differing `concern` (the
     non-redundancy invariant).
   - **`.tools/comp-which`** -- a curated routing tuple `(keywords[], label, example_calls[],
     discriminator_description)`. Give it DISTINCTIVE vocabulary; do NOT name a sibling tool in the
     description (a description is routing input -- naming a sibling hands it your intent).
   - **`comp_capability_provider.py`** -- only if the tool introduces a NEW meta-role: add it to
     `_ROUTABLE_META_ROLES`.
3. **Validate** (section 5) BEFORE committing.
4. **Commit the atomic bundle** (section 3): one `safe-commit` pathspec covering the executable (+engine) and
   all touched registries. `safe-commit` force-adds explicit file pathspecs under `.tools/`.
5. **Post-commit:** the gate ran inside safe-commit; confirm the legible PASS printed a denominator (a mute
   pass is indistinguishable from a member that no-op'd out). Exercise the route:
   `comp-which "<the plain-English question>"` returns your tool.

---

## 5. VALIDATE (before commit -- the gate is the oracle, not your intent)

- `comp-manifest-check completeness` -- the five-member family over the estate. MUST print
  `registration-invariant PASS` and, for the tools your commit touches, no BLOCK.
- `python .tools/comp-which-routing-test.py` -- routing no-regress (member 3's engine); confirms your tool
  self-routes and no sibling regressed.
- `comp-which "<question>"` -- exercise the actual route the way an agent will (member 3 asserts self-route;
  a curated cross-tool route -- e.g. comp-iam-usage rank-1 on lifecycle queries -- is exercised here, not
  asserted). **Ground on the run, not the YAML.**

---

## 6. FLOW: REVISE an existing comp-tool

**First question: extend IN-PLACE or make a new tool?** Default is **in-place, anti-sprawl** (CTO ruling B,
NFRA_DECOMTOOL: comp-debris gained `--types ddb,s3,ec2,events` as a mode of the existing tool, NOT a new
`comp-debris-ext`). Make a NEW tool only when the concern genuinely differs (a new coverage-map `concern` /
`distinct_from`), not merely a new mode of the same concern.

- **In-place (new subcommand/mode):** edit the executable; update the `tools_index` `subcommands`/`does`;
  add/adjust `entries:` rows if it answers a new use-case; keep the coverage-map home unless the `concern`
  changed. Validate (section 5). Commit -- still atomic if the executable and its registration both change.
- **New tool:** section 4.
- **Curated-route revision (rank tuning):** editing `.tools/comp-which` is a corpus change (member 3
  re-checks the full set). This is how a tool moves from near-tie to rank-1 (comp-iam-usage rank-3 -> rank-1
  @e7fec72ec). Route curated-route diffs to the router owner if outside your ownpath.

---

## 7. FLOW: EXCLUDE (not a graph-query use-case) or RETIRE

- **Exclude:** add the extensionless name to `excluded_not_graph_use_cases` in `graph-call-manifest.yaml`
  **with a reason** (the file carries a running inline comment naming each excluded tool + why -- keep that
  discipline; member 5 reads the name, a human reads the reason). Categories with precedent: enforcement
  gates, worklist producers, graph producers/write-paths, on-rails search/inspection primitives, context
  setters, regression tests, perf benchmarking. **A tool with no rich-tool use-case is EXCLUDED-with-reason,
  never left unaccounted** (unaccounted = a member-5 block).
- **Retire:** if the executable is deleted, remove its registration in the SAME commit (member 5's inverse:
  a delete/rename can orphan a `tools_index` key -> member 4 then blocks on the dangling registration). If a
  use-case is superseded, set the `entries:` row `status: deprecated` with `superseded_by: <canonical id>`
  (member A of the graph-access scanner then routes callers to the replacement automatically).

---

## 8. Registration-gap AUDIT (deliverable 2 -- run cadence + the denominator discipline)

**Purpose:** confirm no tracked `comp-*` is unregistered, and NAME what was covered. **Engine (authoritative):**
`comp-manifest-check completeness`. **Legible per-tool view:** `registration_audit.py` (colocated),
reproducing the gate's registries and printing a per-tool verdict row + the denominator.

**Discipline (CTO gate point 3):** every audit prints its DENOMINATOR -- `universe / tools_index / excluded
/ entries-tools / coverage-map` -- and a per-tool row. A gap-closure sweep that cannot name what it did not
cover is the silent-truncation class. **Result 2026-07-18: CLEAN, 0 gaps across 77 tools** (report:
`NFRA_COMPREG_registration_audit_20260718.md`). The estate has been gap-free since the member-5 gate went
live 2026-07-14; the audit is a periodic confirmation, run after any batch of tool additions.

---

## 9. Worked examples (the flow was extracted from these -- no-retrofit)

- **CREATE, ROUTABLE (comp-iam-usage, NFRA_DECOMTOOL @57d9c8fd2 + route @e7fec72ec):** engine
  `comp_iam_usage.py` + launcher; `entries:` row `cloud.iam.usage_coldness`; `tools_index` line; coverage-map
  `meta_tools[]` home (cross-surface lifecycle sibling of comp-iam); comp-which curated tuple with the
  discriminator "usage/lifecycle/reachability -> comp-iam-usage; grant-sufficiency/correctness -> comp-iam".
  Landed by CTO under single-editor SoD (the AE-vs-exec boundary before the ownpath grant). Route promoted
  rank-3 -> rank-1 by a curated-route revision (section 6).
- **REVISE, in-place (comp-debris `--types`, NFRA_DECOMTOOL @97f6a8b70):** new modes on the existing tool
  (anti-sprawl), NOT a new `comp-debris-ext`. tools_index `subcommands`/`does` updated; concern unchanged so
  the coverage-map home stayed.
- **CREATE via SPLIT (comp-kuzu-full / comp-kuzu-inc, NFRA_KUZUSPLIT-P1):** two ENTRIES-ONLY siblings homed
  in `meta_tools[]`, registered in `entries:` without their own `tools_index` rank key (comp-kuzu remains the
  rank target). COO-landed as the SoD exemplar. **RETIRED 2026-09-02** (NFRA_COMPEFFICACY unit 2): both siblings
  consolidated onto `comp-kuzu --mode inc|full`; the NEVER-full guarantee moved from the `-inc` NAME onto the FLAG.
  This bullet stands as the worked example of the REGISTER half; the retirement commit is the worked example of the inverse.

---

## 10. Governance -- the ANY_EXEC_OR_AE ownpath (deliverable 5, CTO-gated)

To close the AE-vs-exec boundary (section 3.3) so the AE lands its own atomic bundle, `0.8.0_AE` receives an
`ANY_EXEC_OR_AE` ownpath **scoped to the registration surface only** and **additive over current
owned-paths**: `graph-call-manifest.yaml`, `comp-coverage-map.yaml`, `.tools/comp-which`,
`comp_capability_provider.py` (routable roles), and the tool's own `.tools/comp-*` wrapper/engine. **It must
NOT widen ownpath onto any deliberate exec-lock** -- the debtscan do-er-gate, `comp_system.py`, and any other
intentionally-locked do-er surface stay `ANY_EXEC`. The grant proposal (separate deliverable) presents the
exact path-set delta vs current owned-paths so CTO can verify additive-only before landing; **CTO owns and
lands the grant, the AE only proposes.**

---

## Appendix: exemplar registry shapes

```yaml
# graph-call-manifest.yaml  entries:  (one per use-case)
  - id: cloud.iam.usage_coldness
    use_case: "Is this IAM role/grant still USED? Who still reaches a resource?"
    canonical_call: "comp-iam-usage {role-cold | who-can-reach <arn> | reach-check <role> <action> <arn>}"
    tool: comp-iam-usage
    mode: query
    layer: cloud
    cost: "~seconds-minutes (read-only; per-role get-role; one simulate per reach-check)"
    freshness: "live AWS IAM (APPLIED, not DESIRED)"
    anti_pattern: "using comp-iam (DESIRED, (action)-not-(action,resource)) for a reachability question"
    status: canonical
    notes: "comp-which routing: 'role last used / who can reach / decommission a role' -> comp-iam-usage."

# graph-call-manifest.yaml  tools_index:  (ROUTABLE only -- one compact line)
  comp-iam-usage: { does: "Access-plane coldness + reach (lifecycle sibling of comp-iam)",
                    subcommands: ["role-cold", "who-can-reach <arn>", "reach-check <role> <action> <arn>", "self-test"],
                    entries: [cloud.iam.usage_coldness] }
```
```yaml
# comp-coverage-map.yaml  -- exactly ONE home (tools[] xor meta_tools[])
  - { tool: comp-system, role: system-compiler, routable: true, not_homed_reason: "..." }   # compact meta form
  - tool: comp-drift                                                                          # full form
    role: compdrift-loop
    routable: true
    concern: "structural-cruft / abandonment DISPOSITION over the propagation seams"
    distinct_from:
      - { tool: comp-dups, why: "comp-dups ENUMERATES the duplicate set; comp-drift CLASSIFIES it" }
```
```python
# .tools/comp-which  -- a curated routing tuple
    (["reachable", "who-can-reach", "decommission", "dormant", "usage", "still-used", "role-cold"],
     "IAM usage / reachability (lifecycle)",
     ["comp-iam-usage role-cold", "comp-iam-usage who-can-reach <arn>"],
     "is this role/grant still USED / who still REACHES a resource -- the lifecycle SIBLING of comp-iam. "
     "Discriminator: usage/lifecycle/reachability -> comp-iam-usage; grant-sufficiency -> comp-iam"),
```
```yaml
# graph-call-manifest.yaml  -- the EXCLUDED escape hatch (flat list; reason in the running inline comment)
excluded_not_graph_use_cases: [comp-perf, comp-manifest-check, comp-grep, comp-glob, comp-to, ...]
  # comp-perf = tool-perf benchmarking (not a graph query); comp-manifest-check = D6 enforcement gate;
  # comp-grep/comp-glob = the on-rails search PRIMITIVES comp-which RUNS when no rich tool fits ...
```
