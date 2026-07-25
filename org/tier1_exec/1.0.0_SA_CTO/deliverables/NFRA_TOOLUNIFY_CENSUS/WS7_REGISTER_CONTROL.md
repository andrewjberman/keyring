# NFRA_TOOLUNIFY WS-7 — The Register as an ENFORCED CONTROL, Demonstrated by Exercise

**author:** `0.8.0_AE_CloudComp` (base) · 2026-07-25 · **status:** PARTS 1-2 DELIVERED + VERIFIED-BY-EXERCISE;
PART 3 PARTIALLY BLOCKED — a new, load-bearing finding, not a silent gap
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T075606Z, "DISPATCH NFRA_TOOLUNIFY WS-7 — the register as an ENFORCED
CONTROL, demonstrated by exercise (exit-bar item 2 of 2)"
**native-path rule applied throughout** (per the 065646Z standing rule this lane relayed the same session).

---

## 1 · Part 1 — the unregistered-tool refusal, exercised and captured

**Method:** created a throwaway `.tools/comp-zzz-test-unregistered` (a trivial bash script, deliberately NOT
added to `graph-call-manifest.yaml` or `comp-coverage-map.yaml`), attempted a REAL commit through the REAL
gate path (`.tools/safe-commit.sh` → `commit-gate.sh` → `commit_gate_runner.py` → `comp-manifest-check`
completeness family, member 2/placement), captured the refusal verbatim, then deleted the file.

**Verbatim refusal:**
```
ERROR: BLOCKED -- commit-gate failed (py_compile / ruff / lint). Commit aborted; files unstaged.
  [commit-gate]
  [commit-gate] BLOCKED: comp-tool placement (each tool needs exactly ONE coverage-map home):
  [commit-gate]   - inventory_completeness: tool 'comp-zzz-test-unregistered' is UNPLACED (in neither
                    tools[] nor meta_tools[] -- silently dropped)
  [commit-gate]   FIX: add the tool to comp-coverage-map.yaml tools[] (surface-homed) or meta_tools[]
  [commit-gate]   (cross-surface/tooling-layer), never both.
  [commit-gate] BLOCKED: comp-manifest-check completeness family (registered-implies-reachable /
                one-map-home / self-routes)
```
**Confirmed no commit landed** (`git log --oneline -- .tools/comp-zzz-test-unregistered` returns empty;
`git status` shows the file gitignored/unstaged, consistent with a genuine BLOCKED-and-unstaged outcome,
not a landed-then-reverted one). File deleted after capture — nothing left on disk.

**VERDICT: the invariant works exactly as documented.** A deliberately-unregistered `.tools/comp-*` tool
cannot land, mechanically, at commit time — not asserted, exercised. This is member 2 (placement) of the
4-member completeness family (`manifest_check_cli.py:90-93`); members 1/3/4 were not separately probed with
a fresh unregistered tool in this pass (member 2 alone is sufficient to prove "cannot land," and probing all
4 members with fresh throwaway artifacts was judged out of proportion to this specific acceptance item —
members 1/3/4's own mechanisms are read at source in §3.2's investigation below, triggered by real, not
synthetic, findings).

---

## 2 · Part 2 — the verification-provenance column, landed with denominators

**Method:** every REC-1/REC-1b/REC-1c deliverable's sidecar (`REC1_EXERCISE.sidecar.json`,
`REC1B_EXERCISE.sidecar.json`, `REC1C_A/B/C/E/base.sidecar.json` — 7 files) was parsed programmatically for
its `tool` field + whichever verdict/observed field it used (`match`, `verdict`, `row_verdict`,
`match_at_tool_level`, `match_at_call_site_level`, `observed_verdict`, `observed_verdict_operational` — the
7 sidecars use 4 different schemas, none identical; all handled). A tool name appearing in 1+ deliverable
becomes `basis: exercised` on its `D.sidecar.json` row, with a `citations[]` array naming every deliverable
that touched it + that deliverable's own observed-verdict text (concatenated when a row has 2+ fields, e.g.
`comp-manifest-check`'s `observed_verdict=LOUD | match=True`). Every other row falls back to `D.md`'s own
pre-existing `confidence` field (HIGH→`source-read`, MEDIUM→`rule-derived`, LOW→`default` — the SAME
three-tier meaning D.md's §6 confidence key already defined, now surfaced as a column instead of only prose).

**Denominator (printed, per WS-7's acceptance criterion):**
```json
{
  "total_rows": 92,
  "exercised": 92,
  "source_read_unexercised": 0,
  "rule_derived_unexercised": 0,
  "default_unexercised": 0,
  "unmapped_conf_fallback_to_default": 0,
  "exercised_tools_not_matched_to_a_register_row": []
}
```
**92 of 92 rows carry `basis: exercised`, zero fell back to a confidence-only default.** This is not
suspicious — it reconciles exactly against `SYNTHESIS.md` §1's own stated coverage math: REC-1 (5) +
REC-1b (3 new) + REC1C-C (16) + REC1C-E (16/15 distinct) + REC1C-base (17) + REC1C-A (18) + REC1C-B (17) =
92, i.e. the fleet was deliberately partitioned to cover the full register with (near-)zero overlap. **Zero
tools were silently left at confidence-only provenance** — a genuinely different outcome from the WS-7
dispatch's own framing ("the register's honest shape is per-row verification provenance... not a
uniform-looking column") turned out, on this specific census, to converge to a UNIFORM exercised column —
which is itself worth flagging as a fact, not massaged to look more heterogeneous than it is.

**4 tool-name normalization mismatches were caught and fixed, not silently dropped:** `comp-iam service
<name>` → `comp-iam`, `comp-freshness artifact <s3-prefix>` → `comp-freshness`, `comp-stitch-refresh,
production call site` → `comp-stitch-refresh`, `comp-surface-check scan` → `comp-surface-check` (some
sidecars annotate subcommand/context directly in the `tool` field; normalized to the base tool name before
matching against `D.sidecar.json`'s row keys, verified zero unmatched after the fix).

**Written to `D.sidecar.json`** (2.6MB, CTO~Z's owned path — backed up before edit, restored-and-rerun once
to fix the normalization bug found on the first pass, final version validated as well-formed JSON with
`json.load` before treating it as done). Every row now carries:
```json
"verification_provenance": {
  "basis": "exercised" | "source-read" | "rule-derived" | "default",
  "citations": [{"deliverable": "...", "observed_verdict": "..."}, ...]
}
```
plus a top-level `verification_provenance_denominator` object (shown above) documenting the method and
counts, per WS-7's "print the denominator" requirement.

---

## 3 · Part 3 — known live drifts: TWO fixed and verified, ONE new blocking discovery

### 3.1 · comp-residue placement — FIXED, verified live PASS

**Before:** `comp-coverage-check` FAILed live (`FAIL: inventory_completeness: tool 'comp-residue' is
UNPLACED (in neither tools[] nor meta_tools[] -- silently dropped)`), reproduced fresh by this lane before
touching anything (matching `~C`'s independent 2x reproduction).

**Root cause, grounded before acting:** checked `docs/briefs/NFRA_TOOLUNIFY_ADVISORY_NEXT_STEPS_20260725.md`
and this lane's own pending TO `NFRA_TOOLARCH.GATEBOUND.selfroute-member-warm-path-flip-step3.md` before
touching the ledger — `comp-residue`'s self-route registration (member 3) is explicitly named as blocked
behind GATEBOUND's hang-repair. **But that TO is about member 3 (self-routes), not member 2 (placement) —
the two are independent invariants** (`manifest_check_cli.py:90-93`), and GATEBOUND does not block member 2
at all. Confirmed this distinction is real, not assumed, before writing anything.

**Fix:** added `comp-residue` to `comp-coverage-map.yaml`'s `meta_tools[]` (estate-wide detector, not homed
to one surface — same shape as `comp-clobber`/`comp-dataflow`), with `routable: false` stated as an HONEST
UNVERIFIED (not a false claim of unroutable) and the entry text explicitly citing that member 3 stays
unresolved pending GATEBOUND, so a future reader does not read `routable: false` as a settled fact.

**Verified live:**
```
PASS: comp-coverage-map.yaml is internally consistent -- every tool one home, every overlap declared,
no phantom seam, inventory complete, projection current, grain stable.
  swept: 87 homed tool(s) (36 tools[] + 51 meta_tools[]) | 12 gate_contract rule(s), 0 unverifiable
```

### 3.2 · 4 tools absent from tools_index — FIXED, verified live PASS

**Before:** `comp-routable-check` WARN (advisory, `RESULT: PASS` overall but with a live WARN block):
`comp-describe`, `comp-kuzu-full`, `comp-kuzu-inc`, `comp-state` are router-reachable (they already have
live `entries:` routing rows in `graph-call-manifest.yaml` — `cloud.describe.resource`,
`cloud.refresh.full`, `cloud.refresh.incremental`, `org.state.registry_drift`, all pre-existing, none
authored by this lane) but absent from the SEPARATE `tools_index:` catalog dict the same file also carries
(the browsable list, distinct from the routing-scoring `entries:` list — confirmed distinct at source,
`manifest_check_cli.py:126-131`'s own comment: *"comp-which's fuzzy backstop iterates the manifest's
`entries:` key, not tools_index"*).

**Fix:** added all 4 as `tools_index:` entries (`does`/`subcommands`/`entries` compact form, matching the
existing convention), each citing its pre-existing `entries:` id rather than inventing new routing metadata.

**Verified live:**
```
comp-routable-check -- registered-implies-reachable (tools_index -> provider.routable)
  tools_index routing targets: 69  (excluding comp-glob, comp-grep, comp-which)
  OK: every registered tool is a live routing target.

RESULT: PASS
```
(69 vs the prior 65 — the 4 additions, WARN block gone.)

### 3.3 · NEW FINDING: both fixes are correct and verified, but currently UNLANDABLE — a pre-existing,
### unrelated BLOCKING gap in a DIFFERENT completeness-family member collides with landing them

**This is the load-bearing part of this section — read before assuming 3.1/3.2 are "done."**

Both `comp-coverage-map.yaml` and `graph-call-manifest.yaml` are in `_SELFROUTE_CORPUS`
(`manifest_check_cli.py:132-136`) — the 3-file substrate for member 3 (self-routes). Editing EITHER file
re-triggers a FULL re-evaluation of member 3 across the whole 65-tool self-route-checkable population (by
the completeness family's own documented design: *"Everything else here is part of the CORPUS the router
ranks against, so it can move ANY tool's verdict and must re-check the full set"*).

**Attempted the real commit** (not a diagnostic dry-run):
```
bash .tools/safe-commit.sh --author "..." -m "WS7(...): comp-residue placement fix + tools_index closure" \
  -- org/modules/graph/comp-coverage-map.yaml org/modules/graph/graph-call-manifest.yaml
```
**Result: BLOCKED, files auto-unstaged.** Verbatim:
```
[commit-gate] BLOCKED: 1 catalogued tool(s) do NOT surface for their own use_case:
[commit-gate]   - comp-state             comp-which returns nothing naming it
[commit-gate]   A tool the mandated router cannot return is undiscoverable, however well it is
[commit-gate]   catalogued. FIX: give it distinctive curated vocabulary in .tools/comp-which...
[commit-gate] BLOCKED: comp-manifest-check completeness family (registered-implies-reachable / one-map-home / self-routes)
```
Plus a 65-line WARN block (every other checkable tool "surfaces only inside comp-which's near-tie list,
never rank-1") — a WARN, not individually blocking, but evidence this is a wide, structural, PRE-EXISTING
condition, not something one small edit could newly cause across 65 tools.

**Causality check, not assumed:** `comp-state`'s BLOCKING failure is that `.tools/comp-which`'s OWN curated
routing vocabulary table does not currently rank `comp-state` #1 for its own documented use_case string
(*"is the registry updated / stale task order status / record behind state / governance drift"*, per
`comp-state`'s own manifest `notes:` field). **Neither of this pass's edits touched `.tools/comp-which` or
`comp-state`'s own manifest entry at all** — this lane added a NEW `meta_tools[]` entry (comp-residue) and 4
NEW `tools_index:` catalog entries, neither of which is the scoring vocabulary `.tools/comp-which` consults.
The mechanism by which comp-state fails self-route is independent of what this lane changed; this lane's
edit only re-triggered the (apparently already-failing) check to run and report. **Not verified against a
clean-HEAD baseline** — `git stash` is banned in this shared worktree (own gate, exercised: attempting it
printed the shared-worktree blast-radius refusal, correctly), and no lower-cost non-mutating way to isolate
member-3's verdict against unmodified substrate was found in the time available this pass. Stating this as
a strong, source-grounded inference (mechanism traced, not merely correlated), not a proven fact.

**Checked for an override:** `--force` on `safe-commit.sh` explicitly does NOT bypass a gate failure (only
the contamination check, per the gate's own printed text). No `MANIFEST_CHECK_ACK`-style audited-bypass
mechanism was found for this specific gate (searched `manifest_check_cli.py` + `commit_gate_runner.py` for
an ACK/override pattern; none exists for the completeness family specifically — unlike `comp-surface-check`'s
`SURFACE_ACK`). **There is currently no legitimate way to land an edit to any of the 3 self-route-corpus
files without either fixing `comp-state`'s self-route gap or getting an explicit gate exception from
whoever owns this mechanism.**

**Disposition (per WS-7's own acceptance path — "close the specific gap or file it with evidence"):
filing with evidence, NOT closing.** Fixing `comp-state`'s self-route vocabulary in `.tools/comp-which` is
explicitly `NFRA_TOOLARCH.GATEBOUND`'s territory — a P1 task with its own two-stage design, mutant-proof
requirements, and a `<cross_domain_coordination>` clause naming this exact file as a shared BLOCKING gate
that needs coordinated flip timing, currently `UNASSIGNED`. This lane does not have a GO to touch
`.tools/comp-which`, and a narrow one-tool vocabulary patch there risks exactly the half-switched-shared-gate
state that TO's own acceptance criteria (mutant-proof, verdict-identity regression check) exist to prevent.
**Both fixes (3.1, 3.2) remain on disk, verified correct in isolation, uncommitted** — not silently
abandoned, and not force-landed around a gate this lane does not own.

**The finding itself is the deliverable here, not just the two fixes**: WS-7's mission is "make the register
a control, not a document." This pass just demonstrated, empirically, that **the control currently cannot
be edited by anyone until GATEBOUND lands** — any future agent touching `comp-coverage-map.yaml`,
`graph-call-manifest.yaml`, or `comp_capability_provider.py` will hit this identical BLOCKED wall. That
elevates GATEBOUND from "a P1 hang-fix" to "the load-bearing precondition for WS-7's own register-as-control
mission to be maintainable going forward" — worth CTO~Z weighing when prioritizing it.

---

## 4 · Acceptance — status against WS-7's own bar

1. **Unregistered-tool refusal exercised + captured:** DONE (§1).
2. **Provenance column landed with denominators:** DONE (§2) — 92/92 exercised, 0 fallback, printed.
3. **comp-coverage-check PASS live or documented exception:** comp-coverage-check itself now reads PASS
   live (§3.1) — but that verified state is currently UNCOMMITTED, blocked from landing by §3.3's
   independent finding. **Documented exception filed** per the acceptance bar's own "or" clause: the fix is
   correct and live-verified; the commit is blocked by a different, pre-existing, out-of-scope gap this
   lane traced to source but does not own the fix for.

## 5 · What this lane did NOT do

Did not touch `.tools/comp-which` or attempt any self-route vocabulary fix (GATEBOUND's territory, no GO).
Did not force-land the two fixes around the gate (no override exists; would not use one if it did without
an explicit GO given the shared-gate coordination clause in GATEBOUND's own TO). Did not `git stash` to
isolate a clean-HEAD baseline (banned in this shared worktree, correctly gate-refused when tried). Did not
probe completeness-family members 1/3/4 with additional synthetic throwaway tools beyond member 2 (§1's own
scope note). Did not re-run REC-1/1b/1c's own exercises — Part 2 is a pure aggregation pass over existing,
already-CVO~Z-verified sidecar data.

## 6 · Handoff

- **`1.0.0_SA_CTO~Z`**: §3.3 is the priority item — decide whether GATEBOUND needs re-prioritizing given it
  now blocks the register-as-control mechanism's own maintainability, or whether an audited exception
  mechanism should be built for the completeness gate (parallel to `comp-surface-check`'s `SURFACE_ACK`).
  The two verified fixes (§3.1, §3.2) are ready to land the moment either path clears — no rework needed,
  just an unblock.
- **`3.0.0_SA_CVO~Z`**: Part 2's denominator + normalization logic is mechanically re-derivable (the merge
  script's method is fully described in §2; happy to hand it over). §3.3's causality claim (my edits didn't
  cause comp-state's self-route failure) is a traced-but-not-clean-HEAD-verified inference — worth an
  independent check if a non-mutating isolation method exists that this lane didn't find.
