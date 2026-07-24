# Session 1307–1515Z — MDPF counts to PRIMARY, off-route staffing, four roster reframes

**Agent:** `2.0.0_SA_COO` · **Date:** 2026-07-24
**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE

---

## 1. Startup

`/watcher` clean: no orphan watcher for my serial, no live peer, registration absent → registered
(PID 30840), persistent Monitor armed (`bp8gdd6dq`), LD-0290 serial file written, zero crons.
`/drive` scoped re-arm **DISCHARGED** @`4cf76d898` — its stop-condition read TRUE on the first
disjunct (MDPF product serving + verified, Andrew sovereign-verified 148 @20260724T0019Z). The
re-point half stays open at Andrew, flagged in the row so a successor cannot arm off it.

## 2. Staffing — off-route, declared

Every main-fabric worker lane dark, MSTR (the spawn router) also dark, and the ~1347Z INF chain
clock ~30 min out. Spawned `0.7.0`, `0.4.0_DS`, `0.6.2~A`, `0.4.0_DE` under my own
`OPAL_AGENT_SERIAL` so the 3/60s cap and audit applied; no `FORCE_SPAWN`; 4th waited out the cap.
Declared to CTO in the same turn as the staffing report, before he could find it in the audit log.
Did **not** spawn MSTR (Tier-1 provisioning a Tier-0 proxy is upward) and did **not** pull the three
idle `0.8.0` ~Z lanes across the fabric split.

Drafted as `LD-0336`; the owned-paths gate blocked it (`lane=TIER0_MSTR`). **Did not override** —
filed in my own lane @`4cf76d898`, routed to MSTR, who claimed and landed it @`16dd604c4` and ruled
it correct. Residual (spawn router has no deputy) carried to Andrew as RV-0055 F-4.

> **MSTR corrected my framing and was right:** the hazard is not absence, it is **absence
> COINCIDING WITH A CLOCK**. Absence alone is harmless — you wait. A deputy scoped to "MSTR absent"
> is broader than the measured hazard. Today's later spawn (`0.6.2~B`) routed through MSTR normally
> with time to spare — the control in a two-point experiment I ran by accident.

## 3. Q1 — the 11:30Z clobber-guard byte-verify: **PASS**

Four limbs, and the first is the one that mattered:
1. **The job actually ran** — RequestId `fda050e2…`, 11:30:35→11:30:39.647Z. "No new version" is
   byte-identical between *guard held* and *job never ran*.
2. All three `DISABLE_PORTAL_*` guards fired **by name** in the runtime log.
3. **Zero versions created today** on all three `json/portfolios/*` keys (versioning confirmed
   Enabled first — Suspended would have collapsed the method to UNDETERMINED).
4. **Counterfactual:** yesterday's identical cron wrote *different bytes* (7720→7656B, 5103→7234B).

**Defect found:** the run prints `OK: Views uploaded …` immediately after skipping all three writes.
Routed to 0.7.0, fixed @`20e3567f0`.

## 4. The six-day dead chain

0.7.0 grounded a premise instead of assuming it and found `nna_coverage_excusals.json` **committed,
pushed, Andrew-grounded — and never staged**. Runner had loaded a 6-day-old 1-account file; INF_C_01
failed nightly; `pipeline-complete` frozen since 07-18.

I narrowed CTO's ruling from *whether* to *who*: the file is a **decision manifest whose entries carry
`decided_by: CTO`**, so staging executes a recorded decision rather than making one. GO at 133738Z,
staged 13:39:36Z, **SSM-confirmed on the box 13:41:02Z**. Chain **CLEARED 15:01:40Z** — first advance
in six days, on the same instance whose manifest was verified, with `pipeline-failed` unchanged as the
discriminating negative.

**85-second margin, and 0.7.0 called it luck rather than competence.** The deploy deadline is the
**dispatch sync**, not instance launch — written into `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`
@`3182d969d` (authored by 0.7.0, committed under my line only because that path is BASE_EXEC lane;
they declined the audited `--force` bypass).

## 5. MDPF Global-Count — decomposition and four reframes

Andrew ~1432Z: **MDPF counts PRIMARY through to VALIDATED**. Decomposed W-1..W-7: W-1 to a
**dedicated** `DS~A` lane (CTO: *"I would have put W-1 on base DS and been wrong — thinking about who
has context rather than who has capacity"*), W-4/W-5 to DE, W-7 to base DS, W-2/W-3/W-6 **visibly
held**.

**W-1 refuted the PRD's mechanism.** The model-cell rule CTO had described to Andrew as close-to-a-
simple-edit **has never fired** — the poison is at the **firm axis** (`:1656`), and that edit would
have changed **zero of the 40 dates**. Cottonwood: CONFIRMED direction, **REFUTED magnitude**
(+442 not +408; −126 masking; +92 not firm-attributable at all). **CVO PASS-VALIDATED** @`6e6c8af47`.

Then four successive reframes of the same roster, each superseding the last:
`permanent defect` → `permanent contract` → `time-varying per-quantity roster` → `NEVER corrected to
forward-only`. CTO's `COUNT effective-from: NEVER` would have **permanently excused Cottonwood from
the count expectation** — the alarm would never fire and would look correct forever. Andrew caught it.

> **The reading CTO adopted from me: a PRECEDENCE FAILURE, not an inference-vs-measurement failure.**
> W-1 had *measured* Cottonwood's first count at 07-22. The number was in his own brief. An inference
> outranked a measurement already in hand — a different defect from "we did not measure," and it needs
> a different fix: not *go measure*, but *check whether you already did*.

Andrew ~1509Z execution order: collect 21 SmartX + 1 Eclipse dates → he visual-smokes → close.
**I held the capability gate against "just collect,"** and CTO adopted the argument verbatim:
**a backfill silently landing today's data would produce a continuous line — exactly what the visual
smoke is looking FOR.** The smoke test cannot detect the failure Andrew himself named. Surfaced to
Andrew with an explicit offer to drop the gate.

## 6. My own errors

- **Dispatched "designs are delivered"** when one of two existed. 0.6.2~A checked the directory and
  caught it in four minutes.
- **Misaddressed a dispatch** — 0.7.0 received DS's body. Corrected both ends inside a minute.
- **Wrote a presence check for a content question** — hours after telling three lanes that existence
  is not content. CTO caught outcome (3); 0.7.0 then caught **3b** (a well-formed fold block carrying
  442, the per-model sum, instead of 294 distinct — passes every structural assertion, inflated by
  148 on a client-facing surface). Three revisions, three people:
  **EXISTENCE → CONTENT → CORRECTNESS**, each level invisible from the one above.
- **Issued an observable without naming its bucket.** DS then read the same key name in
  `opal-data-assets` (which DE had proven is read by nothing) and nearly reported a working hold as a
  P0. I measured across buckets rather than counting two agreeing votes. DS retracted and self-
  diagnosed the deeper error: **an ETag is a content hash, not a key identity.**
- **A `git push` that never ran** — absorbed into a message body by the composition defect MSTR
  measured. I noticed the push had not landed and re-ran it without knowing why.

## 7. Landed

| Artifact | Commit |
|---|---|
| `/drive` discharge + off-route spawn declaration | `4cf76d898` |
| EC2 deploy-deadline standard (authored 0.7.0) | `3182d969d` |
| GC-W45 TO + 3 addenda (W-5 scope, W-4 elevation, declared-contract) | `c6031ceef` … `1aecbc4e0` |
| GC-W1 TO | `939376b88` |
| GC-W7 TO + hygiene→**correctness** re-grade | `269047874`, `af0295106` |
| GC-BF0 + GC-W2a TOs, narrowing, positive-control addendum | `939d7903f0`, `3b9ea142e`, `0a99ec058` |
| **TO template**: easiest-pass + missing-third-state + assertion-ladder | `157278cb3` |
| **RAVC step 3a**: amend a deliverable → re-notify with commit-ish | `d130f1e30` |

## 8. Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which "which producers write json/portfolios/account-distribution.json"` | NO CURATED RULE; routed to `comp-clobber` | Honest non-answer, then correct routing — the right behaviour |
| `comp-clobber --live` | 17 versions, daily 11:30:39Z cadence then stop | **The tool that answered the W-6(bell) producer question.** Exactly the right instrument |
| `comp-blast aum.ts` | **NOT-FOUND**, denominator 2251 nodes | Portal source is structurally outside the graph. Recorded in the TO as NOT-FOUND, **not** a "nothing breaks" clear |
| `comp-transform schema-check ModelPortfolios` | WARN, no `types.ts` resolved | DE later hit the same F-8 gap: 2 of 6 components resolvable |
| `comp-cache` | empty for aum/timeseries | No routing value here |
| `comp-grep account_count portal/src` | 205 occurrences / 20 files | Superseded by DE's attributed enumeration |
| `comp-surface-check` (via safe-commit) | clean on all commits | **Rule 20 was STALE** — DE exercised it: it DOES see portal, returns `rc=2 BLOCKED`, and the portal hook refuses the commit. Routed to CTO; corrected in CLAUDE.md |
| `comp-pipescript io` (via DS~A) | `WRITES: (none detected)` | **Tool gap routed:** a manifest reporting no writes for a producer whose whole job is a served artifact will mislead someone |

**Gap found:** `comp-blast` silently excludes `portal/` — a NOT-FOUND over a 2251-node denominator reads
like a clear to anyone not printing the denominator.

## 9. Open

- **At Andrew:** hold-vs-recompute basis policy (the −5.27% half; the −4.96% frame gap is ours);
  spawn-router deputy (RV-0055 F-4, narrow form).
- **Critical path:** `0.6.2~B`'s B-verdict on SmartX + Eclipse. Nothing else gates Andrew's close-out.
- **Bounded watch:** `mdpf-daily-runner` STOPPED after Door-6 fired — boot latency, or a consumer that
  never ran because its producer was dead longer than anyone was watching.
- **On the board, unstaffed by design:** W-6(count-reconcile), W-7, stamped-frontier staleness,
  bidirectional repo↔runner parity, SENDGUARD, the `org/ref` doc fork.
