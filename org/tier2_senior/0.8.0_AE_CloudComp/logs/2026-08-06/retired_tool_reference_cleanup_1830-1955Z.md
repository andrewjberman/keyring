# A retirement is not finished when the binary is deleted — 26 records that still told agents to run comp-surface-check — 0.8.0_AE_CloudComp

**archetype:** SCRIBE
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-08-06
**Task Order:** ad-hoc — `org/tier1_exec/1.0.0_SA_CTO/deliverables/BRIEF_RETIRED_TOOL_REFERENCE_CLEANUP_20260806.md` (CTO~B authored, Andrew hand-off at this terminal)
**Status:** COMPLETE

---

## Objective

Execute the CTO citation-integrity brief: correct every record that still tells an agent to run
`comp-surface-check` (RETIRED 2026-08-06, Andrew-direct) or bare `pipescript` (retired rc=2 stub,
renamed `comp-estate` 2026-07-30). Records only — no code, no infra, no deploy. Leave
correctly-historical mentions intact, and leave `comp-pipescript` (a DIFFERENT, LIVE tool)
untouched everywhere.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 EXERCISE half — forwarder RAN (own banner), not merely resolved |
| comp-manifest-check | `comp-manifest-check completeness` | PASS | Ran BEFORE and AFTER the rule-bank edits. Registration / output-contract / stage-2-vocab / retired-alias invariants all PASS; 76 registered tools |
| comp-manifest-check | (auto, via safe-commit commit-gate) | FAIL | Blocked commit 1/3 on `comp-drift UNDECLARED: reconcile` — a FALSE claim. See Gap found |
| comp-system | `comp-system` (x2) | PASS | Two-phase discharge. Re-ran because peers advanced HEAD between commit 3 and the first regen (had stamped `as_of=fb05a250bc`, HEAD was `c626e83da9`) |
| comp-pulse | (auto, via safe-commit `[risk-reflex]`) | PASS | Fired [HOLD] on 4 of my paths; I read the cited claims rather than committing through them. Denominator printed: 1659 danger nodes |
| comp-estate | — | SKIPPED | Named as the live successor in the records I fixed; no traversal question arose, so invoking it would have been theatre for the table |

**What worked:** `comp-manifest-check completeness` was the right instrument for the wrong-looking
reason — it PASSED both before and after, and that pass is what proved the 26 defects were
structurally invisible rather than newly introduced. `comp-system`'s BLOCKED-ON-PEER-LANDING
message did not just refuse, it explained the two-gate deadlock and named the reserved override
prefix, which is why the two-phase took one read instead of an escalation.

**What failed:** the commit-gate's subcommand-declaration invariant blocked a correct edit on a
false premise (below). Separately, `comp-system`'s first regen stamped an already-stale HEAD —
correct behaviour under concurrency, but it means the artifact is only as good as the moment you
commit it.

**Gap found — TWO, both routed to `1.0.0_SA_CTO~B`, neither fixable from this lane:**

1. **`manifest_check_cli.py:1193` @`29c3fedeb8` is comment-blind.**
   `_ADD_PARSER = re.compile(r"add_parser\(\s*['\"]([a-z][a-z0-9-]*)['\"]")` — a raw regex over
   file TEXT. `drift_cli.py:296` @`eeccc217ad` is the comment
   `# reconcile is ESTATE-WIDE: iam_cli.py add_parser('reconcile') takes NO positional`.
   EXERCISED: that regex returns `['reconcile']` on that comment line, and it is the **only** match
   in the entire file — so `comp-drift`'s "ACTUAL exposed derivation surface" is one string
   harvested from a comment about a **different tool**. `comp-drift` has no subparsers at all
   (positional `target` :755, `--deep` :758, `--json` :761).
   NEGATIVE CONTROL: the same regex finds **8** real subparsers in `manifest_check_cli.py` — so it
   is not an undiscriminating matcher, it is specifically comment-blind.
2. **The estate's retired-alias gate cannot see prose, by design — and that is correct.**
   `graph-call-manifest.yaml`'s own TRIGGER_LAYER note says "lint the structured field, not a
   text-match over mentions", so the invariant does not fire on the ~330 design-doc proposal names.
   All 26 defects lived in prose (a `notes:` string, an accounting comment, a `description` field);
   the structured half was already correct. This gap is not closable by widening the gate without
   turning it into the open prose scan it deliberately is not — the manual sweep IS the control.

---

## Work Completed

### 1. HIGH — the six action-misdirecting defects

| # | Site | What it claimed | Fix |
|---|---|---|---|
| H1 | `org/modules/graph/critical-surfaces.yaml:143-146` | `commit_gate: tool: comp-surface-check / SEV1: block-with-ack` — a MACHINE-READ config key naming a deleted binary as the live blocking gate | `status: RETIRED`, `tool: null`, `former_*` preserved |
| H2 | `org/modules/graph/graph-call-manifest.yaml:33` | `comp-surface-check = D8 critical-surface commit-gate ... auto in safe-commit` — 17 lines above the same file's own retirement row | re-pointed to `retired_aliases:` |
| H3 | `docs/architecture/NFRA_GRAPHS.md:393-397` | standing CTO ruling to flip the DELETED tool to a hard block, in an `active` project | STRUCK + marked MOOT / NEVER TO BE EXECUTED |
| H4 | `org/modules/graph/graph-call-manifest.yaml:723` | `comp-which`'s own curated router map emitting bare `pipescript` in two named-thread slots | both -> `comp-estate` |
| H5 | `org/critical_paths/README.md:14-15` | `SURFACE_ACK` bypass declared a live STRUCTURAL writer of approval entries | struck; nothing writes them now |
| H6 | `docs/architecture/NFRA_PIPESCRIPT_PRD.md:12,:43` | present-tense entry-point claim + three dead invocations, in a PRD carrying **no rename note at all** | banner + 6 sites re-pointed |

**H1 is the one that needed grounding, not just editing.** Before touching it I grepped the estate
for readers of `monitor.commit_gate`: there are **none** — every `commit_gate` hit in `.tools/`,
`org/modules/`, `infra/`, `portal/src` is the unrelated `commit_gate_lib.sh` /
`commit_gate_runner.py` family. The only reader was `comp-surface-check` itself. So the key is
ORPHANED, which is what makes "declare the retirement in place" correct and "delete the key" wrong
(deleting destroys the decommission record). I also recorded what did **not** change: the
per-surface SEV1/SEV2 tiers stay live, read by `severity_resolution` + `scheduled_scan`. Without
that sentence a reader cannot tell whether RETIRED nulls the whole severity model.

### 2. MED — the two PRDs

`NFRA_PIPESCRIPT_PRD.md` got a top banner (correct name, the
`pipescript -> comp-semantic-estates -> comp-estate` lineage, the explicit
"`comp-pipescript` is a DIFFERENT LIVE tool", and a pointer to `comp-estate --list` for counts)
plus six re-pointed action sites (`:12 :25 :43 :50 :63 :69`). **Left verbatim: `:21`, Andrew's own
2026-06-15 quote** — the phrasing IS the ruling; you do not edit a sovereign quote to tidy a doc.

`NFRA_GCONTR_PRD.md` got **one suspension banner instead of seven line edits** — the brief offered
this and it is the right call: GCONTR is sovereign-suspended INDEFINITE, so the document is
historical in full, and seven line edits would leave a suspended PRD reading like live instruction
in between them. The banner names both dead mechanisms it is built on and states that the
suspension is untouched.

`org/projects/NFRA_GCONTR.json:30` — the `pipeline` field was a machine-readable registry value
composed of two names that no longer resolve. Corrected in place; project NOT re-planned.

### 3. LOW + the frozen-count class

`NFRA_NERVES_PRD.md:45`, `NFRA_COMPRAIL_HARDENING_BATCH.md:23` (which listed retired `pipescript`
BESIDE live `comp-pipescript` — the exact conflation the brief warns about, inside a Rule-21
enforcement doc), `critical-surfaces.yaml :48 :128-132 :139`, `graph-call-manifest.yaml:1335`.

**Frozen counts (brief §6): fixed the cheap half only.** `comp-tools.yaml:309` now states no count
and defers to `comp-estate --list`. I deliberately **left `graph-call-manifest.yaml:710`** — it is
dated ("as of 2026-07-30") and already carries its own do-not-re-freeze warning, so after the edit
exactly one record states a count and it declares its vintage. The two-records-two-numbers
contradiction is gone without deleting a vintage-stamped observation.

### 4. Two items BEYOND the brief's 26 — one fixed, one reverted

- **Fixed and flagged:** `critical-surfaces.yaml:136` read "(R3 — a write **is** a
  comp-surface-check'd commit)". Present-tense copula naming a deleted tool = a FIX-IT under the
  brief's own §2 rule, but absent from its 26-item list. Corrected. Called out in the commit
  message because a silent scope creep and a caught sweep miss look identical afterwards, and only
  one of them is honest.
- **Reverted, deliberately:** `graph-call-manifest.yaml:1749` — `comp-drift`'s `does:` string says
  it calls seam engines "(comp-heat/**pipescript**/lambdamap/...)". Ground-truthed against
  `drift-topology.yaml`: there is no pipescript engine; seam-2's real engine is
  `comp-pipescript deployed` (`:85`). So the row emits the prohibited bare name AND misnames the
  live engine. **I fixed it and the commit-gate blocked me on the false `reconcile` claim above.**
  Fixing the record would have required declaring a command that does not exist into `comp-which`'s
  routing map. I reverted rather than write the false declaration.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Revert the `comp-drift` fix rather than declare `reconcile` | The gate's remediation text says "add the missing subcommand(s)"; its own refusal doctrine says why not — "a derivation nobody can find is indistinguishable from one that was never built", and the inverse is worse: one that CAN be found and does not RUN. A gate satisfiable only by a false declaration is not a gate on correctness. |
| One banner for GCONTR, not seven line edits | Sovereign-suspended in full. Declaring the body historical satisfies the brief's §2 classification rule; partial edits would imply the rest was reviewed and kept live. |
| Declare `commit_gate` RETIRED in place; do NOT delete the key | This estate has ruled that deleting a decommission record is the same class of loss as an un-ruled retirement. Grounded first: zero readers remain. |
| Leave `graph-call-manifest.yaml:710`'s counts | Dated + self-flagged. Fixing the other record already resolves the contradiction; deleting a vintage-stamped observation would cost evidence for no gain. |
| Three commits, one lane each | Rule 14a: `GIT_COMMIT_AUTHOR_OVERRIDE` is SINGULAR. Lanes resolved per path with both controls fired first. |
| Do NOT push | Standing: lanes commit, integrators push. Also avoided racing a live peer mid-commit. |
| Do NOT touch the code residue | Brief §8: records only; if a fix needs a code change, STOP and route it back. |

---

## Files Modified

See commit messages: `8e3beb8e1`, `5073e4986`, `26dea574e`, `c99582c33`. Rows needing extra context:

| File | Change | Committed |
|---|---|---|
| `org/modules/graph/critical-surfaces.yaml` | H1 + 3 LOW + 1 beyond-scope; 5 sites | Yes — `5073e4986` (ANY_EXEC override) |
| `org/modules/graph/graph-call-manifest.yaml` | H2, H4, LOW `:1335`; `:1749` fix REVERTED (gate-blocked) | Yes — `8e3beb8e1` |
| `docs/architecture/NFRA_GCONTR_PRD.md` | ONE suspension banner in place of 7 line edits | Yes — `26dea574e` (ANY_CTO override) |
| `infra/system/06_current_state.{md,json}` | comp-system regen, `as_of` HEAD=`c626e83da9` | Yes — `c99582c33` (two-phase discharge) |

---

## Verification

No Deployment Sequence table: this was a records-only cleanup with no code, infra, Terraform or
deploy leg — there is nothing deployed to verify. Actual output instead:

```
comp-manifest-check completeness (AFTER the edits):
  [manifest-check] registration-invariant PASS: 90 tracked+committed comp-* executable(s) all accounted
  [manifest-check] output-contract invariant PASS: 76 tools_index tool(s) all declare an output contract
  [manifest-check] stage-2 vocab invariant PASS: 34 declared tool(s)
  [manifest-check] retired-alias invariant PASS: 7 retired name(s) declared, all disjoint from
                   live+excluded (93 live), successors valid, none cited in committed routing surfaces.
  PASS: routable + placement + self-routes + existence, over 76 registered tool(s).

yaml.safe_load re-parse AFTER editing:
  critical-surfaces.yaml    -> monitor.commit_gate = {'status': 'RETIRED', 'tool': None,
                               'former_tool': 'comp-surface-check', 'former_SEV1': 'block-with-ack',
                               'former_SEV2': 'warn'}
  graph-call-manifest.yaml  -> retired_aliases keys = [comp-adapter-audit, comp-coverage-view,
                               comp-learns-run, comp-opalbizsem, comp-semantic-estates,
                               comp-surface-check, pipescript]
  NFRA_GCONTR.json          -> JSON OK, 17 keys, status=suspended-indefinite

comp-system: wrote infra\system\06_current_state.md + .json (grounded-against-live; as_of HEAD=c626e83da9)
```

**One of my own edits broke `graph-call-manifest.yaml`** — I nested double quotes inside a
double-quoted YAML scalar (`:1335` col 342). **The Edit tool reported success on the broken write;
the parser is what discriminated.** Caught and fixed pre-commit. This is why the re-parse is run
after editing and not treated as ceremony.

**A silent retrieval failure caught by a positive control, while writing this log:**
`git log --author="0.8.0_AE_CloudComp" --since="2026-08-06 18:00"` returned **empty** — no error.
`--since` parses as LOCAL time, and my commits are `15:34 EDT` = `19:34 UTC`, so the filter was set
in the future. Four commits that exist rendered as zero. Positive-controlling the four known hashes
is what exposed it. Same class as `grep -c` counting zero inside an error message.

**Residual-token audit (denominators, not booleans):** every remaining bare-`pipescript` token in
every touched file was enumerated and read in context — `NFRA_PIPESCRIPT_PRD.md` 2 (Andrew's
verbatim + my lineage note), `NFRA_NERVES_PRD.md` 1 (my lineage note),
`NFRA_COMPRAIL_HARDENING_BATCH.md` 0, `comp-tools.yaml` 2 (both lineage notes),
`graph-call-manifest.yaml` remainder all in `retired_aliases:` / lineage / the reverted `:1749`.
**Zero action-directives remain.**

**owned-paths lane resolution, both controls fired before choosing any override:** DENY on
`org/tier0/ledger/**` (negative), ALLOW on my own home folder (positive).

**risk-reflex `[HOLD]` citations were read, not committed through.** The `critical-surfaces.yaml`
hold pointed at `org/critical_paths/DO_NOT_DECOMMISSION_portal-v2_json_mdpf_49financial_20260722.md:100`,
whose control #3 is "this document + `critical-surfaces.yaml` row" — and that yaml row is still
marked **proposed**, never landed. My diff removed no surface row. Unrelated to my change; cleared.

---

## Blockers

None. Two findings are OPEN AT `1.0.0_SA_CTO~B` but neither blocks me — my deliverable is complete:

- `graph-call-manifest.yaml:1749` is a records fix that is **currently unlandable** until the
  `manifest_check_cli.py:1193` extractor is fixed. That is a code fix in the CTO lane, correctly
  out of this brief's scope (§8). Routed with mechanism, vintages and an exercised negative control.

---

## Current State

The CTO retired-tool citation-integrity brief is DISCHARGED: all 26 enumerated defects corrected
across 10 files in three lane-split commits — `8e3beb8e1` (ANY_EXEC_OR_AE + ANY:
`org/modules/graph/graph-call-manifest.yaml`, `org/modules/graph/comp-tools.yaml`,
`org/projects/NFRA_GCONTR.json`, `org/critical_paths/README.md`), `5073e4986` (ANY_EXEC audited
override: `org/modules/graph/critical-surfaces.yaml`), `26dea574e` (ANY_CTO audited override: the
five `docs/architecture/` docs) — plus `c99582c33` discharging both STRUCTURAL-TWOPHASE/rule-bank
overrides via a `comp-system` regen stamped `as_of HEAD=c626e83da9`. **Nothing is pushed** (lanes
commit, integrators push). No replacement guard, checker, monitor or alerter was added anywhere:
every record now states in place that the absence of `comp-surface-check` is the ruling, not a gap,
so the next reader cannot mine it as a TODO. `retired_aliases:` rows untouched (they are the
policing mechanism); `comp-pipescript` untouched everywhere. RAVC2 delivered to `1.0.0_SA_CTO~B`
(`20260806T195036Z`) carrying both findings; RAVC-ACK sent to `0.7.0_AE_CloudOps~B`
(`20260806T195115Z`) for its 08-04 freshness-harvest named input, with the lane note that
`ADHOC.comp-tool-universe-audit` is issued to `0.8.0_AE_CloudComp~B` and is still `staged` — banked,
correctly addressed, and consumed by nobody until that lane is spawned or COO re-points it.

---

## Next Steps

1. **[1.0.0_SA_CTO~B] Fix `manifest_check_cli.py:1193` so the subcommand extractor ignores comments**
   — it currently blocks a correct records fix unless an agent declares a nonexistent command. The
   gate also reports **11 tools** with standing subcommand drift; how many are this same
   false-positive class is UNMEASURED and I am claiming no number. Once it lands, the
   `graph-call-manifest.yaml:1749` records fix becomes landable (one line, mine to take).
2. **[1.0.0_SA_CTO~B] Route the code residue the brief's §8 kept me out of** — sharpest is
   `.tools/portal-hooks/commit-msg`, which still auto-appends `SURFACE_ACK` and self-tests against
   `portal .github/workflows/surface-check.yml`, a workflow the retirement deleted; still installed
   by `install.sh:31`. Also `.tools/freeform.sh:7,32` (names surface-check as a live SAFETY gate),
   `org/modules/graph/comp-coverage-map.yaml:125-126,:561-562,:840,:1031`,
   `org/modules/graph/comp-output-contracts.yaml:430,:784`, `.tools/TOOL_CLASSIFICATION.yaml:1573`,
   `org/modules/graph/comp_aws_cli.py:2165`. Grep-level candidates, not verified findings.
3. **[2.0.0_SA_COO] Decide the seat for `ADHOC.comp-tool-universe-audit`** — issued to
   `0.8.0_AE_CloudComp~B`, still `staged`, and now holding a delivered named input from
   `0.7.0_AE_CloudOps~B` that nothing is consuming.
4. **[0.8.0_AE_CloudComp]** IDLE, event-driven. 74 active TOs carry my serial; none dispatched this
   window.
