# leg-4 L4 refused, not closed: `cse` is clobbered out of the branch-head marker and the reader omitted it silently. (2) landed; (3) refused on a sovereign lock and retracted by CTO; (1) held to daylight.

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Agent:** 0.7.0_AE_CloudOps
**Window:** 2026-07-09T23:04Z (session start, post-Monitor-death) -> 2026-07-09T23:35Z
**Session context:** Monitor died ~22:40Z; agent was deaf until 23:04Z. Both open deploy ledgers were
HELD-SOVEREIGN-GATED across the deaf window. Nothing half-landed.

---

## Summary

Came up deaf, re-armed, and was tasked to verify `freshguard-leg4` L4 on the ~02:10Z nightly derive and
close its ledger. **The ledger is not closeable and I did not close it.** Grounding the L4 property
surfaced a real defect in the leg-4 marker contract, which was then confirmed at source, at applied
state, and by exercising the reader.

**The defect.** `_provenance.stamp_marker` rebuilds `table_metadata` from its caller's `table_names`
(`:203-212`) and `put_object`s the **whole** marker (`:226-235`) -- it reads `existing` only for the
monotonicity guard, then discards `existing.table_metadata`. `derive_runner:413` and `cse_store:91` stamp
**4** tables (incl. `cse`); `incremental_updater:575` stamps **3** and is the **modal** writer (hourly).
So every incremental stamp **erases `cse`**. The reader then iterated `for name in sorted(tm)` (`:255`) --
an **absent** table emitted **no line at all**. Its "never a silent fresh" guarantee only ever covered a
*present key with a null value*. Meanwhile `TABLE_CADENCE_MAX_HOURS` declares a 26h cadence for `cse`:
**a staleness check that could never fire, on the one table whose absence it existed to catch.**

**Why L4 could not close.** L4's criterion -- *"`last_write_iso` populated on all 4 tables"* -- is
satisfiable by reading at 02:11Z, **a moment chosen to make it pass**; the next hourly stamp falsifies it.
Closing on that read is LD-0267(C) -- measuring with an instrument aimed at the wrong moment -- in the
lane that found LD-0267(A). CTO re-specced L4 to a durable criterion. **It stays OPEN, and without the
merge fix it FAILS at ~03:00Z, correctly.**

---

## What I did NOT claim

`cse`'s actual vintage is **UNRESOLVED**. Its newest S3 metadata is ~28.6h old against a 26h cadence --
a louder finding, and I refused it, because **that is the mtime oracle `_provenance.py:141-145` formally
RETIRES** ("newest-metadata-by-mtime is not HEAD"). Seven `00000-*.metadata.json` pointers exist for
`cse`; mtime cannot pick the current one. Nessie (`nessie.opal-globgrph.local:19120`) is VPC-internal and
unreachable from the dev box, so `current_snapshot().timestamp_ms` is unresolvable here. **INFERRED,
non-actionable, not asserted.** The structural finding stands without it.

Likewise I did **not** call `graph_nodes` STALE a writer stall: it reads `[STALE > 6h cadence]` at 7.0h,
but SQS `opal-globgrph-incremental-events` depth is `0/0` and the Lambda invoked in every hour tonight.
**Benign quiet, not a stall** -- and a hint that the 6h cadence is mistuned (already item #14's
`graph_nodes 6h->26h` footgun fix).

---

## Rulings received / issued

| # | Item | Outcome |
|---|---|---|
| Q1 | `served-guard-49f` inside the 49F sovereign fence? | **CTO: SUSPENDED** (ruled `230329Z` while deaf). Both 49F ledgers `gate=sovereign`. **L4 DOES NOT RUN.** On release: *"out of scope, sovereign -- VERIFY NOT RUN"*, an explicit gap, **never a pass.** `NEVER#6` binds on **applied legs**, not on **assurance**. |
| Q2(2) | Reader names absent cadence-configured tables | **CTO GO, unconditional. LANDED `b9f991994`.** |
| Q2(3) | Versioning on the marker key | **REFUSED by me, then RETRACTED by CTO as void.** See below. |
| Q2(1) | `stamp_marker` merges instead of replaces | **CTO HOLD** -- my proposal was a read-modify-write race. Held to daylight w/ 4 conditions. |
| L4 | Criterion | **RE-SPECCED by CTO.** Ledger stays open. |

### (3) refused, and why it mattered
CTO GO'd *"versioning on the marker key."* I refused and did not apply. Void three ways:
1. **S3 has no key-level versioning** -- it is bucket-level.
2. It reverses **`Andrew-locked decision #5`** (`infra/aws/terraform/shared-infra/s3.tf:365-368`,
   *"VERSIONING NEVER-ENABLED on purpose"*) whose **cited authority is CTO's own prior ruling**
   (`CTO 163827Z` + Path-B GO `164234Z`). **A CTO GO cannot lift an Andrew lock.**
3. Under versioning, the nightly mark+sweep (`derive_runner.py:720`, bare-Key `delete_objects`) creates
   **delete markers**, and the lifecycle has **no `NoncurrentVersionExpiration`** (`s3.tf:404-405`,
   "keep-all"). The GC would keep printing `MAINT_SWEEP_COMPLETE deleted=N` **while reclaiming nothing.**

**I measured before claiming:** bucket is `1.01 GB / 166,843 objects`. A "cost explosion" argument was
available and **untrue**; the defect is the **lying log**, not the bill. I nearly sent the loud version.

**The lock's blind spot (recorded, not acted on):** the lock says history lives at Iceberg-snapshot +
Nessie-catalog + unique-timestamped-tarball-key layers. `warehouse/_branch_head.main.json` is **none of
the three** -- the one mutable, destructively-overwritten, history-less object in a bucket whose entire
no-versioning argument is "history lives elsewhere."

**Alternative adopted by CTO (better than what he GO'd):** archive the superseded marker to
`warehouse/_branch_head.history/{committed_at_iso}.json` -- a unique-timestamped key, **the lock's own
sanctioned mechanism.** ~1.2 KB/stamp, ~10 MB/yr. No versioning, no sovereign, no GC interaction. Lands
with (1).

### (1) held -- and CTO's objection was better than my proposal
My merge turns a wholesale put into a **read-modify-write** against an hourly writer with no conditional
put: last-writer-wins over a stale merge base, **silently dropping a row written between read and write**
-- a *visible* erasure traded for an *invisible* one, undetectable by the reader I just fixed. I had the
race in front of me and did not see it.

I found the hole in **his** condition in return: `stamp_marker` is best-effort/never-raises, so an
unsupported `IfMatch` would raise `ParamValidationError`, be **swallowed into a WARN**, and **silently
stop stamping the marker altogether** -- a conditional write degrading into no write at all. **Fail
closed, loud, never degrade to an unconditional put.** (The `exit 3` vs silent `exit 0` asymmetry of
LD-0267, third application tonight.)

`PutObject.IfMatch` is SUPPORTED on the dev box (boto3 1.42.54 / botocore 1.43.0). **The dev box is not
the runtime** -- Lambda `python3.12` bundled botocore and the derive image's pinned boto3 are
**unverified**. Not inferring it from a version number. **Daylight.**

---

## Deployment Sequence + Verification (AE role requirement)

**Deployed:** nothing to AWS. `b9f991994` is a **read-path-only** repo change.

**Proved (not asserted) zero deploy risk:** `format_provenance_header` / `_per_table_vintage_lines` are
called ONLY by dev-box comp-tools (`comp_cluster_cli:62`, `comp_debt:86`, `comp_detect:92`,
`canon_motif_scorer:68`, `debtscan_canon_scorer:80`). **The deployed writers never call the read path.**
No zip rebuild, no CodeBuild, no `safe-apply`.

**EXERCISED against the LIVE marker** (`s3://opal-313476888478-globgrph/warehouse/_branch_head.main.json`,
LastModified `2026-07-09T16:13:18Z`, `writer_id=incremental_updater`, 3 tables, versioning OFF):
```
BEFORE b9f991994:
  cadence-configured but ABSENT from marker: ['cse']
  cse mentioned in output: False          <- the defect: silence

AFTER b9f991994:
  cse: ABSENT FROM MARKER -- vintage unverifiable (26h cadence declared;
       last writer 'incremental_updater' did not stamp it)
  graph_contracts: last-write 556.5h ago
  graph_edges: last-write 21.2h ago (< 26h cadence)
  graph_nodes: last-write 7.2h ago  [STALE > 6h cadence]
```
**All 4 branches exercised offline** (fresh 4-table -> `cse` normal; `cse` 40h -> `[STALE > 26h]`;
`cse` null `lw` -> `UNRECORDED`; `cse` key absent -> `ABSENT FROM MARKER`): **ALL BRANCHES PASS.**
Case C incidentally proved the fix is **general, not `cse`-special-cased** (`graph_edges` absent also
reports ABSENT). `commit-gate.sh` clean.

**Declared drift (not hidden):** the Lambda zip and derive image carry a vendored `_provenance.py` now
one commit behind repo. **Behaviourally identical** (they call `stamp_marker` only). Reconciles on the
next rebuild, which (1) forces anyway.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | "globgrph marker tables / where `stamp_marker` writes `last_write_iso`" | PARTIAL | near-tie router; surfaced `comp-symbols`, did not dead-end |
| `comp-symbols` | `infra/aws/globgrph/_provenance.py` | PASS | 12 fns / 6 constants -> located `MARKER_KEY`, `TABLE_CADENCE_MAX_HOURS`, `stamp_marker` in one call |
| `comp-glob` | `**/*LEDGER*` | PASS | located `.tools/deploy_ledger.py` |
| `comp-grep` | `LD-0266\|LD-0265` then `LD-0266|LD-0265|LD-0267` | PASS (after correction) | **the tool taught me**: it WARNed that `\|` is a literal in Python `re` and that a 0-match may be the escaping, not an absence. Bare pipe worked. Found LD-0267 already landed -> **I did not duplicate it.** |
| `comp-grep` | `stamp_marker` / `format_provenance_header` callers | PASS | SYSTEMS-CONTEXT footer routed to `comp-aws` / `comp-iam gaps` |
| `comp-grep` | `bucket = "opal-313476888478-globgrph"` over `infra/aws/terraform` | PASS | **the find of the night** -- surfaced `shared-infra/s3.tf:376`, a root I was not looking in. A raw grep of `globgrph/` would have missed the Andrew lock entirely. |

**What worked.** `comp-grep`'s repo-scoped sweep found the bucket declared in `shared-infra/`, not
`globgrph/` -- exactly the coupled-thing-a-text-local-grep-misses case Rule 21 exists for. Without it I
would have authored a versioning change against a bucket whose lock lives in another root, on a valid GO.

**What failed / GAP FOUND.** `comp-grep` **cannot see `org/mcp/inbox/`** -- it is `.gitignore`-aware and
the inbox is gitignored, so it reported `0 match(es); scanned 0 file(s)`. Its own footer says *"0 matches
is a real result here"* -- **which is false for a gitignored tree, and reads as a confident absence.**
Same shape as tonight's through-line: a report of success detached from the property it names. I fell
back to a `# rail-checked:` raw grep. **Recommend:** `comp-grep` should either (a) name the excluded-tree
count (`scanned 0 files; 1 path excluded by .gitignore`) or (b) accept an `--include-ignored` flag for the
inbox/ ledger trees. Filed here; routed conversationally to CTO.

---

## MCP traffic

**5 messages** (2 in, 3 out; +2 CTO replies inbound mid-window). Significant:
- **IN** COO `223932Z` -- correction: my *"zero ycharts calls from this lane, **ever**"* was an unbounded
  negative, refuted by my own telemetry (`ycharts_freshness`, `2026-07-02T17:19:39.885Z`). **Accepted
  without reservation.** The bounded claim (tonight) was true; the unbounded one quantified over a
  universe I never queried.
- **IN** COO `224036Z` -- P1 audit-lake pull. **MOOT**, do-not-action per Andrew; independently confirmed
  from `7a58c12d8` (CTO pulled it: 34 calls / 29,461 records / `dt=06-26..07-09`). **Not actioned.**
- **OUT/IN** CTO `231820Z` -> `232022Z` -- Q1 SUSPENDED; Q2 rulings.
- **OUT/IN** CTO `232906Z` -> `233006Z` -- (3) refused -> **(3) RETRACTED as void.**
- **OUT** CTO `233213Z` + COO CC -- **CLAUDE.md Rule 18 is LD-0267's missed drift target.**

**Relay status (honest):** COO asked me to relay the *"'no its alright' was about an Outlook draft, it is
NOT a YCharts lift"* broadcast to `~A`/`~B`. **No `0.7.0_AE_CloudOps~A` or `~B` lane is live**
(`get_live_agents`, 9 agents, neither present). **The relay is a no-op, not a completed action.** Banked
for the next lane spawn rather than reported as delivered.

---

## Findings issued

1. **`cse` marker clobber** (above). SOURCE + APPLIED + EXERCISED. Fixed on the read path; write path
   held.
2. **(3) would have broken the GC in tonight's own grammar** -- `deleted=N` true, nothing reclaimed.
   CTO: *"the thirty-fifth instance of the class I have spent seven hours cataloguing, and I would have
   authored it."*
3. **CLAUDE.md Rule 18 still asserts a safety property that does not exist.** `grep -c "LD-0267"
   CLAUDE.md` -> **0**. Rule 18 tells every agent `[STOP]` *"hard-blocks"* and safe-apply *"fails
   closed."* LD-0267's drift list named `org/XXX.md` and `HALTGT_SEVERITY_CONVENTION.md` and **missed the
   one doc loaded into every session, whose preamble calls its rules "law."** The `fails closed` clause
   is the dangerous half: **true**, but it advertises fail-closed on the **rare** branch (no serial ->
   loud `exit 3`) while the **modal** branch (empty inbox, because your watcher did its job) is a
   **silent open.** Routed to CTO (governance; not an AE edit), CC COO per LD-0116.
4. **LD-0267(A), independently corroborated before reading the record.** `halt-gate-check.sh:144-150`
   enumerates pending at `find -maxdepth 1` excluding `read/`; `inbox-watch.sh:117-124` `mv`s to `read/`
   **before** emitting `[INBOX]`, on a `sleep 5` poll. **The watcher archives the message before it
   announces it.** Formulation adopted verbatim by CTO into the record: *"the healthier your watcher, the
   more reliably the interlock fails. The only agent a `[STOP]` reliably blocks is one whose watcher is
   dead -- which is exactly what mine was tonight."*
5. **`-F` is not a `safe-commit.sh` flag.** Andrew relayed *"use `-F` for every commit"*; `safe-commit.sh`
   (`:85-105`) accepts `--force` only, and a bare `-F` falls through `*)` into `COMMIT_ARGS` -> `git
   commit -F`, which consumes the next arg as a **message file**. **CTO: SUSTAINED, confusion was his** --
   he had told the fabric to use `git commit -F <file>` to stop backticks executing in `-m`. Two
   different `-F`s. Used `--force` (audited) and flagged rather than silently substituting.

---

## Blockers

**None self-owned.** Both ledgers wait on named external/sovereign gates, evidence-cited:

- `served-guard-49f-new-deploy` -- `gate=sovereign`. Andrew's standing 49F OUT-OF-SCOPE prohibition
  (CTO `2235Z` / COO `2254Z`; ledger collision ruled CTO `230329Z`). **L4 does not run.** Not a
  coast-failure: *a verification is knowledge, not state; knowledge can wait for a sovereign.*
- `freshguard-leg4-writer-wiring-finish` -- `gate=external`. L4 re-specced; **fails by design** at
  ~03:00Z until the merge+CAS lands. CTO deliberately pushed (1) to daylight.

---

## Current State

- **`b9f991994`** on `origin/CLOUD` (`c408ed64d..b9f991994`). `infra/aws/globgrph/_provenance.py`
  `_per_table_vintage_lines` now iterates `sorted(set(tm) | set(TABLE_CADENCE_MAX_HOURS))` and prints
  `ABSENT FROM MARKER -- vintage unverifiable` for a cadence-configured table missing from the marker.
  Three outcomes, none silent. Read path only; no AWS artifact changed.
- **Live marker** `s3://opal-313476888478-globgrph/warehouse/_branch_head.main.json` --
  `writer_id=incremental_updater`, `committed_at 2026-07-09T16:13:16Z`, tables
  `{graph_nodes, graph_edges, graph_contracts}`. **`cse` ABSENT.** Bucket versioning **OFF**
  (Andrew-locked); no recoverable prior version.
- **Ledgers:** both `HELD`, tracked, non-RED, HELD-STALE at 4d. Gate refs carry the full re-spec and the
  suspension reasoning. **Nothing half-landed, nothing in flight, no ledger opened for (3) because
  nothing was applied.**
- **Durable memory corrected.** `project_pending_trigger_leg4_l4_freshness_cascade` previously instructed:
  *"at 02:20Z verify 4 tables, then `close-leg L4` + `close`."* **My own record would have walked the next
  instance of me into the exact false close I refused.** Rewritten to the re-specced criterion + the
  do-not-enable-versioning lock + the CAS conditions. MEMORY.md index line updated to match.
- At ~02:10Z the derive stamps 4 tables; the next incremental erases `cse`; **the header now prints
  `ABSENT FROM MARKER`. L4 fails, visibly, on the record.** CTO: *"a verify designed to be able to fail is
  the only kind worth running."*

---

## Next Steps

| # | Item | Owner | Gate |
|---|---|---|---|
| 1 | **(1) `stamp_marker` merge + CAS.** Confirm `PutObject.IfMatch` in the **DEPLOYED** runtime (Lambda bundled botocore + derive image pinned boto3) -- **exercise, do not infer**. Then `IfMatch` + bounded `412` retry + **loud raise on exhaustion AND on `ParamValidationError`**. Exercise both directions. Fold in `_branch_head.history/{ts}.json`. | **[0.7.0_AE_CloudOps]** | CTO GO; **daylight, not tonight** |
| 2 | Then L4 re-verify on the durable criterion -> close `freshguard-leg4` ledger | **[0.7.0_AE_CloudOps]** | after #1 |
| 3 | **CLAUDE.md Rule 18** correction (carry LD-0267's ratified *"a HALTGT PASS is not evidence you were not halted"*) | **[1.0.0_SA_CTO]** | governance; may want MSTR LD-0267 amendment |
| 4 | `served-guard-49f` -- close as *"out of scope, sovereign -- VERIFY NOT RUN"*, an explicit gap | **[0.7.0_AE_CloudOps]** | **Andrew** sovereign release |
| 5 | `comp-grep` gitignored-tree blindness: name the excluded count or add `--include-ignored` | **[1.0.0_SA_CTO]** to route | tool gap, filed above |
| 6 | P3 image rebuild (#26) -- reconciles the vendored `_provenance.py` drift | **[0.7.0_AE_CloudOps]** | after leg-4 ledger CLOSES (one image-ledger at a time) |
| 7 | Not-a-lift relay to `~A`/`~B` | **[0.7.0_AE_CloudOps]** | on next lane spawn (no lane live now) |

**Not idle. Available.** Offered CTO to build the (1) runtime `IfMatch` probe tonight -- **design only,
landing nothing** -- so it is ready to exercise at first light.
