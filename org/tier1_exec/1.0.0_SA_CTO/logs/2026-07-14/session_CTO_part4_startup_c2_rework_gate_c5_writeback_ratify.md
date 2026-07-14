# CTO session part 4 — fresh-session startup, the C2 REWORK gate (polluted-prefix denominator), the C5 write-back ratification + coexistence rider

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, DIAGNOSE
**Serial:** 1.0.0_SA_CTO · **Date:** 2026-07-14 (~04:30Z–04:45Z) · fresh Andrew-launched session
**Continues:** `session_part3_opal_assets_refinement_into_opal_runners_schwab_smartx_etl.md` (+ its post-log addendum)

## Startup (org/XXX.md, all steps)
/watcher: killed orphan watcher pid 2517063 (parent 2516998 dead, prior session PID 25344 gone natively
— the broker's "LIVE 50s ago" was a manufactured verdict, the orphan-thief class exactly as documented);
left `1.0.0_SA_CTO~Z`'s watcher alone (live wrapper, not my serial). Re-registered PID 26948, Monitor
task bb3yzjfdy, LD-0290 serial file written, owned-paths hook confirmed, `.agent_context` set, zero
crons (CronList clean). Read all five 07-14 logs + prompt + registry state via MCP scan.

## Gate rulings issued this window
1. **C2 corrected-fix plan (55dd545d2): REWORK, NARROW** (to COO 04:39Z, relay to 0.7.0).
   ACCEPTED at source: (i) {type}-preserving strip_prefix, (ii) pre-write injective guard (set-logic on
   the mapping, orphan-immune), (a) concurrency=1, (b) list-once. REWORK: the (iii) denominator is
   CARDINALITY over the whole dst_prefix listing (`distinct_landed >= expected_unique`) — and I measured
   live that `orion/inflection/bronze/` holds EXACTLY 2,269 keys, all flat corrupt orphans, zero
   type-segmented. First corrected run: expected 4,640, so ANY collapse down to 2,371 landings PASSES —
   a 2,269-key masking budget; the instrument structurally cannot fire on the exact run it exists to
   verify, and it has no surplus detection. Required shape: per-key set-membership (missing = RAISE) +
   classified surplus (known flat-orphan class count-reported, RAISE on growth; any other surplus =
   RAISE), converging to clean set-identity after Andrew's orphan deletion. Mutant bar m1/m2/m3, transcript
   committed. Binding authority: the C5 design-gate ruling (~04:17Z) ratified set-identity-with-surplus
   as "the reference pattern for the C2 fix" — this plan was authored 00:04ET, BEFORE that ruling, so
   the gate applies it now (convergence, not reversal). GO pre-granted on the reworked commit at the
   same 0/1/0 plan shape.
2. **C5 auth write-back opt-in: RATIFIED + RIDER** (04:41Z). Daily lambda writes back; concurrent
   backfill workers read + mint-in-memory — single-writer on stored state honors 3a's INTENT (SM single
   source, re-mint LOUD) while killing the last-writer-wins race on `smartx/jwt/current`. RIDER: the
   design assumed two live SmartX JWTs COEXIST — unexamined premise. Required a 2-token overlap probe
   (mint B while A live, assert A still accepted) recorded in the design note BEFORE any at-scale
   concurrent backfill; EXCLUSIVE result → workers never mint, single-minter window. 0.5.0 ACK'd 04:43Z:
   probe recorded as HARD GATE (PENDING), correctly scoped to gate concurrency not first pull; verbatim
   3a + scoped reading travel together in note §5.

## RAVC closes + reconciliation
- **mdpf per-partner gate first-fire verify (DS, 04:33Z): VALIDATED + CLOSED** — all 6 checklist items
  on the served artifact, 49f roll exact-to-cent, LD-0292 +$528.2mm tie-out, nothing actioned, Door 6
  untouched, the comp-freshness 85.6h FAIL correctly named a NEVER#1 flat-hours instrument error.
  MEMORY.md overdue trigger closed by DS.
- **NFRA_COMPRAIL.TO-2 flipped pending → complete** (`2e365655a`) on live exercise: classifiable
  question routes; tool-less search auto-runs on-rails comp-grep (20,579 files scanned / 972
  sovereign-held excluded, denominators printed, rail-logged). Regression + coverage bars re-taken by
  NFRA_COMPCLOSE Phase E (CVO~Z SOUND `3d816c650`).
- 0.5.0 broker-summary staleness: timing cross, self-resolved (their 04:39Z refresh preceded my read).

## Open on my board
- **AWAITING 0.7.0 (via COO):** the reworked C2 denominator commit → my pre-granted GO → apply → clean
  re-mirror → close bar (4 distinct types per orion date on landed bytes).
- **AWAITING ANDREW (unchanged, via COO):** the 2,269-orphan deletion; FAM/SLM vendor doc.
- **EVENT [22:00Z]:** ETF parity day-2 + first monolith bronze + ligament rows (0.5.0/0.7.0 report).
- **Standing/parked (part-3 §D unchanged):** send_message forgery gate; gate-candidate batch for
  Andrew's nod; HALTGT latch; MEMORY.md cap. OPAL_RUNNERS build gates on Andrew's word (§C).
- Not mine but visible: 0.8.0_AE_CloudComp (9 pending TOs) and 0.6.0_AE_PartnerETL (2) are NOT live —
  COO's coordination lane per the fabric shape; noted in my oriented summary, not chased.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-which` ×2 | classifiable q ("which lambda writes platinum mdpf aggregate aua") + tool-less marker search | PASS — routed (ranked, rank-6920.yaml) / auto-ran on-rails comp-grep, denominator printed | the TO-2 AC1 exercise; also this session's search reflex |
| `aws s3api list-objects-v2` + `aws s3 ls` (operational verify) | orion/inflection/bronze/ census | 2,269 keys, ALL flat, 0 type-segmented — grounded the C2 REWORK arithmetic | live-primitive grounding for a gate ruling; denominator printed |
| native `git show`/`Read`/`Glob` | 55dd545d2 source read (both files), logs, TO-2 | PASS | Rule 22: ruling grounded on source at a pinned vintage, not the relay |
**What worked:** reading the guard CODE rather than the commit message caught that the "distinct
landings" check is cardinality-not-membership — the message's own description (`>=`) was the tell.
**What failed (mine):** a `cat` with a relative path + `2>/dev/null` from a lingering cwd returned
empty and I nearly read "file missing" — the control-on-the-retrieval class; re-ran absolute, file
existed. **Gap:** none new; the C2 rework IS the reference-template propagation working.

Appending one line to `org/compiler-tools-log.md` in this commit.
