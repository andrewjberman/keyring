# Respawn startup + stale-TO ground-truth reconciliation (lane ~A)

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

## Objective

Session killed and respawned with the rest of the program's lanes. Run `/watcher` + the XXX.md
startup protocol, re-establish reachability, then determine what is genuinely open for ~A and
drive it — rather than resume the remembered state, which turned out to be stale in both
directions.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | `command -v comp-which` (XXX.md A.3 PATH check) | PASS — resolves via `~/bin` forwarder | shims active this session; no `provision-path-shims.sh` needed |
| `comp-system` | `comp-system --check` (WS-1 phase-1 gate) | `SYSTEM CURRENT` (06 sources unchanged, age 2h < TTL 24h; 24 managed regions across 6 files, 0 drifted) | this is the WS-1 `<if_mismatch>` STOP condition firing — see finding 2 |
| `system_parity.py` | `python infra/system/system_parity.py` (WS-1 acceptance #2) | PASS — per-domain, denominator printed, exclusions named, vintage `40bbcb1933` | comp-tools 7/7, infrastructure 5/5, engineering 5/5, ontology 4/5 (`ont-rulebank-version-current` FAILs BY DESIGN — SYSPARITY.DENOM item A closes it) |
| `audit-archive-invoker` | `python .tools/audit-archive-invoker.py` (XXX.md A.2) | rc=0, 0 findings, snapshot not-due | |
| `watcher-status.sh` | `bash org/mcp/watcher-status.sh 0.8.0_AE_CloudComp~A` | `VERDICT: NONE` | used ONLY to enumerate legacy watchers, never as a liveness oracle (it structurally cannot see stream watchers) |
| `safe-commit.sh` | `-F` form, 3 TO paths | PASS `19aafc15e` | `-F` not `-m` per Rule F-010 |

**What worked:** reasoning from PID identity rather than from "am I a fresh session" — the
XXX.md discriminator. Registration read STALE at PID 18348 against my PID 888230, and no
`inbox-watch.sh` existed for my serial, so this was the genuine-orphan-absent case: nothing to
reap, arm clean. No false-positive kill.

**What failed:** the `/watcher` skill's own arming command. It hardcodes an absolute
`/c/Users/...` path; this is a Cygwin-shell session where `/c/...` does not resolve and
`/cygdrive/c/...` does, so the first Monitor died `exit 127`. Re-armed on the resolvable form
(the same form MSTR's live watcher uses) — task `budrra3wj`, confirmed `running` by `TaskOutput`.
**It failed LOUD** (exit 127 + a `failed` task-notification), which is the lucky case; the
concerning sibling is that XXX.md Step 1b-C mandates "the **absolute** script path" without
naming which absolute form, and an agent that read the skill's literal command and did not check
the death-notification would be silently deaf for the session.

**Gap found:** see findings 1 and 3.

## Work Completed

### Startup
Registered (PID 20852), LD-0290 session-serial file written, owned-paths hook confirmed wired,
`.comp-graph/.agent_context` set, branch `CLOUD`, zero crons armed (correct per Step 1b-F —
Tier-2 lanes arm none), `CronList` empty so none to cancel. Inbox drained and current; newest
message was CVO~Z's 161248Z routing correction, already processed pre-kill.

### The reconciliation (the actual finding)
Last-known state was "self-test + over-perm honesty fix pending verify". Both are true but
**neither is mine to act on** — they sit at CVO~Z, which respawned from the same fleet kill and
is working its SYSPARITY sweep. So I checked what ~A actually owns, and found the inverse
problem: **three TOs issued to `~A` read `<status>pending</status> while their work had landed
days earlier.**

| TO | Status read | Actually landed | CVO gate |
|---|---|---|---|
| `NFRA_SYSPARITY.WS-1` | pending (P1, "DO FIRST") | 2026-07-19 | SATISFIED `@b8e63282ec` "metric SOUND"; vintage finding folded `@2399689ee1` |
| `NFRA_SYSPARITY.WS-3` | pending (P1, load-bearing) | 2026-07-19 `@a8917afdfd` + `@322fde6327` | SATISFIED `@565729348c` "WS-3 CLEAR ... both fire rc1" |
| `NFRA_MSBEFF.R2` | pending (P2) | 2026-07-23 `@b24099572b` | accepted CTO~Z `@194300Z`, RAVC-closed `@194401Z` |

Closed all three `@19aafc15e` with evidence cited **in each TO file**, not only in the commit
message. Verified rather than assumed: re-ran the WS-1 metric live, and read the WS-3 surface_map
to confirm the ONTOLOGY row genuinely carries `NFRA_ONTOLOGY_RULE_BANK.yaml` +
`variance_dimensions.yaml` with its exercised evidence (`0f5ba0d92` clean-before / drift-after).

## Findings

**1. Stale-pending TOs are not inert — they misprice the fabric's idle capacity.** Three P1/P2
items showed ~A as loaded while it held no open build work. This is the
`STALE RECORD SAYS SOMETHING FALSE WITH AUTHORITY` class pointed at the allocation surface: COO
owns idle-agent reallocation by context, and the input to that decision was wrong for six days.
The closure signal for WS-1 *already existed inside COO's own record* — WS-3's priority line
reads "Unblocked now (WS-1 landed @62b28c5fb)" — so the record contradicted itself and the
`<status>` field was the limb nobody advanced. **Landing work and closing its record are two
acts, and only the first has a gate.**

**2. WS-1's phase-1 STOP condition is TRUE and DISCHARGED, not open.** `comp-system --check`
reports `SYSTEM CURRENT`, not the PRD S1 "250 commits stale" premise. The TO says to STOP and
surface if this happens — but it moved **by being fixed** (~C's SYSPARITY units + the
managed-region refresher), which is the intended end-state, not a baseline shifting under the
PRD. Recorded in-file so a future reader does not re-raise a closed STOP as a live one, and
surfaced to COO rather than adjudicated.

**3. Two residuals carried, not silently absorbed.**
- **R2's standing CVO~Z verification never landed** (the RF-7 flag + the isolated / same-file
  4-read controls). Acceptance and RAVC close came from the *issuing* chain, so the TO is
  complete as BUILD work while the verification is open. Marked as exactly that, and routed to
  CTO~Z as its call — not self-resolved, not asserted done.
- **WS-3 phase-3 was COO's**, as drift-gate cadence-owner: the post-widen authoritative sweep +
  checkpoint advance. I built the surface add and deliberately did not self-advance the
  checkpoint; I found no evidence that sweep ran. If it never did, the widened surface has not
  had its authoritative post-widen sweep. Surfaced to COO.

## Blockers

None. ~A holds no open build work. WS-6 remains `staged` — awaits GO, untouched.

## Current State

Reachable (Monitor `budrra3wj`, confirmed running), registered, event-driven. Records are at
parity with the estate for this lane. Two of my prior deliverables await CVO~Z's verify
(`--self-test @760fd29c9`, over-perm honesty `@91bc39980`); neither is blocked on me.

## Next Steps

1. **[2.0.0_SA_COO]** WS-3 phase-3 authoritative post-widen drift-gate sweep + checkpoint
   advance (cadence-owner; I must not self-advance it).
2. **[1.0.0_SA_CTO~Z]** Route or discharge R2's open CVO~Z verification. Separately, the
   `investigate-candidates` fleet-scale residual is still named and still unrouted — worth an
   item BEFORE anyone schedules that tool as a routine sweep, not after.
3. **[3.0.0_SA_CVO~Z]** `--self-test @760fd29c9` + over-perm honesty `@91bc39980` verify.
4. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by for dispatch.

---

# ADDENDUM -- CTO~Z rulings on both residuals, landed @1ecfe671f

**archetype:** IMPLEMENT

Both residuals I surfaced came back ruled @20260725T170702Z, same session. Actioned this turn.

## Ruling 1 -- MSBEFF.R2: discharged as a gate, retained as a label

Status is now the literal string `ACCEPTED (build) -- CVO~Z standing verify NEVER OBSERVED`,
not `complete`. CTO~Z's reasoning, carried into the TO: the standing verify gates nothing and
CVO~Z's queue holds items gating live builds, so it is discharged -- but it must not be recorded
as verified, because it is not. **"Complete" and "independently verified" are different claims,
and this estate's recurring failure is the second silently inheriting the first's authority.**
The distinction now lives in the status field, where a reader cannot miss it, rather than in a
comment or a message where it would decay.

## Ruling 2 -- investigate-candidates BLOCKED from routine scheduling

Recorded at three surfaces (module docstring in the tool's own refusal voice, CLI subcommand
help, runtime banner in sweep mode) rather than as a backlog note.

### I got the banner placement wrong twice, and inspection could not see it

The hazard is a run killed mid-sweep rendering a clean fleet verdict over an unstated subset.

1. **First cut: printed AFTER the loop.** So it appeared only on runs that COMPLETED -- exactly
   the set that never needed it.
2. **Second cut: moved above the loop.** A 25s-truncated sweep showed it STILL did not print:
   `_build()` (the TF parse) runs before any output and consumed the entire budget. The process
   died having emitted only comp-iam's own NOTE lines.
3. **Third cut, correct:** emitted first -- before `_build()`, before the header, before any AWS
   call -- with an explicit `sys.stdout.flush()` so it survives a kill during the parse.

**The reusable form: both bad placements looked correct and were merely DOWNSTREAM OF SOMETHING
EXPENSIVE.** A truncation warning is worthless if anything costly precedes it, and that ordering
is invisible to code review -- it only appears when you actually kill the run. *Print the
constraint before you spend anything.* Neither error was caught by reading the diff back; both
were caught by running the control.

Also added the completion line: `SWEEP COMPLETE: examined X of M intended role(s)`, denominator
from INTENDED roles, never from `results` -- a results-derived denominator is tautological (the
same shape as the tautological-`derived_count` STOP CTO~Z called on ~C). **Its absence is the
discriminator** between a complete sweep and a truncated one.

### Acceptance -- all four exercised on the real tool

| # | Control | Result |
|---|---|---|
| B | truncated sweep (`timeout 20`, exit 124) | banner present 1, `SWEEP COMPLETE` absent 0 |
| C | targeted `--role`, **isolated** invocation | banner absent 0 (correctly suppressed) |
| A | targeted `--role` | `SWEEP COMPLETE: examined 1 of 1 intended role(s)` |
| D | `investigate-candidates-self-test` | 12/12 PASS, rc 0 (regression, zero AWS) |

`py_compile` PASS on both modified modules. Negative control run in a SEPARATE invocation from
the target, per the mode-1 discipline.

### Scope held

The fleet path was explicitly NOT assigned and is NOT built: no batching, no parallelism, no
timed-out-vs-clean state machine. All three remain owed and are named in the docstring.
**This does NOT lift the constraint** -- it makes truncation detectable at the OUTPUT layer, but
a scheduler that never reads the banner is unaffected, so the prohibition still carries the
weight. The docstring states that explicitly rather than letting the mitigation imply the
problem is solved.

## Current State

~A clear, event-driven, no open build work. R2 correctly labeled accepted-not-verified. The
investigate-candidates scheduling constraint is mechanical at three surfaces and exercised in
both directions. Awaiting the next TOOLUNIFY item from CTO~Z.

---

# ADDENDUM 2 -- Andrew-direct STANDING ruling on NFRA tool design; audit of my own surface

**archetype:** VALIDATE

Three copies of one ruling landed within ~16s: base 0.8.0's relay (190040Z), CTO~Z direct
(190050Z), base CTO's safety carve-out (190056Z). **Read all three before acting** -- the second
corrected the first's routing and the third bounded what may be touched.

## The ruling (verbatim, Andrew-direct to `1.0.0_SA_CTO`, ~2026-07-25T185538Z)

> *"our comp tools should absolutely never be limited on governance. governance is handled at the
> aws cli/aws user iam level, not at the tool level, If i am understanding properly what youre
> saying, that sounds like the tools have built in blind spots for absolutely no reason"*

STANDING, binding on NFRA tool design generally: no comp-tool gets a governance predicate, a hold
check, or an `*_INCLUDE_HELD` env var. Durable record already committed by base @9e886f7e2a --
not duplicated here.

**Nothing was dispatched to me. All three notes explicitly authorize nothing. I edited nothing.**

## Forward trigger fired on my own surface

CTO~Z said this arc's thesis is now law and the surface would be mine. Audited the tools I own:
`comp_iam.py`, `comp_iam_investigate.py`, `iam_cli.py`, `comp_dataflow` — **all clean.**

`extract_iam.py` is **not**, and it is comp-iam surface:
- imports `is_held_path` + `include_held` from `sovereign_held` (`:27-33`)
- carries `COMP_IAM_INCLUDE_HELD` — literally the `*_INCLUDE_HELD` var the ruling names
- `_read_source_if_allowed()` gates a `read_text()` of **local repo files** (`:58-68`)

That last limb is CTO~Z's sharper half instantiated: **IAM does not govern local file reads, so
this path was never governed, only PRETEND-governed.** The file's own comment calls the decision
"a pure str.startswith on the relative path" — and *startswith is not an access control.*

**STATE, measured not assumed: the blindness is DORMANT, not live.** `SOVEREIGN_HELD_PATHS = ()`
(`sovereign_held.py:40`), so `is_held_path` returns False for everything and no read is currently
skipped. What remains is dead governance scaffolding. "Silently under-reporting right now" and
"carries a retracted, inert guard" are different claims and only the second is made.

## The finding worth reusing: the two tuples are byte-identical

```
RETRACTED_20260709_PATHS   = ("data/black_diamond/", "data/canonical/schwab/silver/", "schwab/silver/")
PROD_WRITE_FORBIDDEN_PATHS = ("data/black_diamond/", "data/canonical/schwab/silver/", "schwab/silver/")
```

Same for both BUCKET tuples. **The retracted governance set and the live safety set are
INDISTINGUISHABLE BY VALUE — separable only by IDENTIFIER NAME.** So the most natural way to
honour this ruling (grep the bd/schwab literals, remove them) is exactly the one that destroys
`PROD_WRITE_FORBIDDEN` while appearing to work. Base CTO warned the rip takes out the safety half;
**this is why.** Operational rule routed to both CTO lanes: **a rip must key on the SYMBOL NAME,
never on the path literals.** The split comment in the file does not say this, and a careful
reader can still reach for the values. The `@1fcf560b8` regression detector protects the control
but trips *after* deletion — naming the symbol-not-value rule up front is the cheaper control.

## Not adjudicated

Whether `extract_iam`'s guard is in scope is CTO~Z's; whether `PROD_WRITE` is in or out is open at
Andrew via base CTO. Neither resolved from inference. Routed, not acted on.

## Tool defect found in passing

**`comp-grep` is broken in this session type**: `rg: command not found`, after which the shim
executes the Python body as bash (cascading syntax errors). The on-rails search primitive fails in
a Cygwin-shell session — which pushes agents toward raw grep precisely where the rail wants them
on-rails. Used native `Grep` instead; did **not** override the rail with a `rail-checked` marker.
Flagged to CTO~Z as its own item, not fixed off a broadcast. (The rail gate itself worked
correctly — it caught a `.tf` token in one of my probes and denied it.)

## Current State

~A clear, nothing edited, no dispatch held. ACKs + the finding routed to CTO~Z and base CTO;
record-custody leg to MSTR including the base-addressed-mail delivery gap.

---

# ADDENDUM 3 -- GOVRIP review exchange with base CTO: two findings adopted, one claim of mine REFUTED

**archetype:** VALIDATE

Review exchange off base CTO's carve-out (which authorized nothing and dispatched nothing).
Recording the refutation as prominently as the adoptions -- a log that carries only the wins is
the stale-record class applied to oneself.

## Adopted

1. **Byte-identical tuples.** `RETRACTED_20260709_*` and `PROD_WRITE_FORBIDDEN_*` are identical in
   value; separable only by identifier name. Now a standing rule in the GOVRIP spec: **a rip must
   key on the SYMBOL NAME, never the path literals.** Landed in the new module's own docstring.
2. **Control ordering.** The `@1fcf560b8` regression detector is a *detector* -- it fires after
   the deletion is written. A rule in the dispatch *prevents*. Base CTO: "I had been relying on
   the catcher." Both ship.
3. **Import atomicity.** Verified by base CTO across **all seven importers, no exceptions** (4
   dual-import, 3 bare -- all fail unhandled on delete). My three-step order adopted: extract the
   safety half -> de-guard every importer -> delete last.
4. **Denominator/classification split** kept wholesale: one pass establishes the denominator,
   another classifies within it. Collapsing them is what let base CTO's scopes drift.

Chasing (3) exposed a defect in base CTO's own census: the deletion scope included
`RETRACTED_20260709` but the census predicate did not, so a file consuming only that half was
invisible. Their line, worth keeping: **"'Re-derive it' does not protect against a wrong
predicate; it propagates one."** That deletion is now HELD -- `RETRACTED_*` has 4 live green
consumers.

## REFUTED -- my module-name census was NOT complete

I claimed a consumer census keyed on the **module name** is *structurally complete*, because a
consumer cannot consume the leaf without naming the module at its import edge. **Base CTO tested
it before adopting and it is false.** Verified the counterexample at source myself:

```
extract_s3.py   grep -c sovereign_held -> 0        (misses my census)
extract_s3.py:19    from .trace_graph import ... _held_path_hit
extract_s3.py:337, :358             two live calls
trace_graph.py:30/32   imports is_held_path from the leaf
trace_graph.py:149-163 defines _held_path_hit over it
```

**True at depth 1; I stated it as true at depth N.** A re-export creates a consumer whose import
edge names the *re-exporter*, not the leaf. Correct form: **the import edge must be FOLLOWED, not
MATCHED -- a consumer census over a re-exported symbol is a transitive-closure problem, not a
grep.** The two censuses were not even nested (27 vs 30, unique members both ways), so neither
was ever the superset.

Refinement I sent back: `_held_path_hit` is a locally-`def`'d **wrapper that WIDENS**
(`:163` ORs `is_held_path` with `HELD_BUCKET_PREFIXES`), not a rebound import -- so a pass-2
implementation keying on re-exported *names* would still miss it. The criterion that catches it is
**any local binding whose body reaches the leaf**. `extract_s3.py` is now mandatory in the
de-guard set; it would have raised ImportError at import time.

## The lesson, which is the actual deliverable

**Both censuses failed the same way: each was complete against the failure its author had just
seen.** Base CTO's against "wrong symbol"; mine against "wrong symbol list"; neither against
"consumer never names it at all." **A predicate hardened against the last miss is not a predicate
that cannot miss.**

And the control was not a better pattern -- it was base CTO *running the claim against a file
neither of us had reason to suspect.* The predicate is the input to the control, not the control.
I deliberately did NOT respond by proposing a third predicate certified complete; the closure is
complete against STATIC import edges and I did not enumerate what sits outside that.

## Current State

Nothing open at me, nothing edited, no dispatch held. GOVRIP step 1 has passed both gates (31
passed, mutant 3/3 RED, guard still armed post-extraction). `PROD_WRITE` IN FORCE; the boundary
question remains unanswered at Andrew and is not mine to resolve.
