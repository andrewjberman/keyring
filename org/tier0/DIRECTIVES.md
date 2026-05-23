# DIRECTIVES — The Active Mandate for `0.0.0_AB_MSTR`

**Status:** v1.4 — D-001 active with PHASE 2 amended to verify-channel methodology + retroactive Completed-sweep; D-002 (standing maintenance via comp-* dev) + D-003 (standing CL fabric facilitation) added; format + authoring protocol ratified v1.2
**Authority:** Andrew authors; the CTO transcribes. A Directive's mandate is Andrew's alone — MSTR may *propose* and the CVO may review and recommend, but a Directive is added, amended, or retired only by Andrew, via the Directive Authoring Protocol below. A Tier-0 law document, never CVO-ratifiable (Constitution Art. III, XIV). (owned-paths: `TIER0_LAW`, `permitted_agents: []` — no standing agent write access.)
**Version:** 1.4 · **Last updated:** 2026-05-22
**Amendment history:** v1.1 — Directive format tightened to a full schema (external Phase-3 review). v1.2 — Directive Authoring Protocol codified (Andrew directive 2026-05-22). v1.3 — D-001 rewritten from "Finish ADVI" (task-altitude) to the broad two-phase whole-workspace mandate; the ADVI-specific substance moved to the ADVI_VALFIN PRD / project (Andrew directive 2026-05-22). v1.4 — D-001 PHASE 2 amended to verify-channel methodology (mechanical/novel/meta) + retroactive Completed-sweep; meta-analysis success signal (holistic-purpose alignment) added to PHASE 2; D-002 standing maintenance via comp-* dev added; D-003 standing CL fabric facilitation added. (Andrew architectural ruling 2026-05-22; MSTR LD-0006 proposal feedback folded.)

---

## What this document is

The standing mandate. Under Constitution Article II, MSTR pursues **only** what is
written here and its *faithful extensions* — it may not originate goals outside
this file. This is Andrew's steering wheel: to redirect the fabric's autonomous
top layer, edit this document.

## How MSTR uses it

- Read in full at the start of every operating cycle (Constitution Art. XII); the
  cycle record attests the version read.
- Every Decision Ledger entry cites ≥1 `directive_ref` into this file and a
  `mandate_distance` (Stakes Matrix rule 6). An action that cannot cite an active
  Directive is a new goal — out of mandate — proposed back to Andrew.
- A Directive that conflicts with the Constitution is void to the extent of the
  conflict (Art. III); MSTR surfaces such a conflict rather than acting on it.

## Directive Authoring Protocol

A Directive is the sovereign's mandate. It enters this document by exactly **one
channel** — every other path is invalid, and any Directive arriving by another
path is void.

1. **Origin — Andrew alone.** A Directive originates only from Andrew, stated
   directly to the CTO (`1.0.0_SA_CTO`) in a CTO terminal session. It is never
   originated by MSTR, by another agent, by a relayed or forwarded message, or by
   the CTO's own initiative. MSTR may *propose* a goal to Andrew (Constitution
   Art. II) — a proposal is **not** a Directive and never auto-promotes; it
   becomes a Directive only if Andrew then speaks it through this protocol.

2. **Transcription — the CTO is scribe, not author.** The CTO transcribes
   Andrew's spoken Directive into the schema below. The CTO does not originate,
   expand, narrow, reinterpret, or fill gaps in a Directive. If Andrew's
   statement is ambiguous or incomplete against the schema, the CTO flags it back
   to Andrew and asks — it never resolves the gap on its own judgment.

3. **Confirmation — read-back before commit.** Before committing, the CTO
   presents the fully drafted Directive — the exact `DIRECTIVES.md` text — back
   to Andrew in-session. It is committed only on Andrew's explicit confirmation
   that the transcription matches his intent.

4. **Commit — audited, scoped, per-instance.** The CTO commits, scoped to this
   file alone, via the audited Tier-0 owned-paths override
   (`GIT_COMMIT_AUTHOR_OVERRIDE=TIER0_LAW`). The lock stays `TIER0_LAW`
   (`permitted_agents: []`) — there is no standing agent write access; the
   override is the per-instance, Andrew-directed channel, so every Directive
   commit leaves an `OVERRIDE` audit line proving it was Andrew-directed.

5. **Scope.** Add, amend, and retire all follow this protocol. `issued_by` is
   always `andrew` — the CTO is the instrument; Andrew is the author.

This protocol is ratified law; it changes only by Andrew.

## Ignition validation

Before `/govern` will originate work under a Directive, it validates the
Directive is: **(a)** well-formed — every required field below present;
**(b)** `status: active`; **(c)** `issued_by: andrew`. A malformed or
accidentally-active Directive does **not** ignite autonomy — `/govern` flags it
and stays in scan-and-report-only mode. Ignition takes all three.

## Directive schema

Each Directive is one block. **Every field is required** (use `none` where a
field genuinely does not apply — never leave it blank).

```
### D-NNN — <short title>
- directive_id:           D-NNN
- status:                 active | paused | retired
- issued_by:              andrew
- issued_at:              <date>
- objective:              <the mandate, imperative — what MSTR is to pursue>
- scope:                  <what is explicitly IN>
- non_goals:              <what is explicitly OUT — the cheapest drift control>
- allowed_stakes:         S0-S2 | S0-S3 | S0-S4
                          <the ceiling on what MSTR may even PROPOSE under this
                           Directive. S0-S2 = pursue it but never propose a
                           gated action; S0-S4 = the full range is in play.>
- success_signals:        <how Andrew/MSTR knows the directive is being served>
- stop_conditions:        <conditions under which MSTR halts work on this Directive>
- review_cadence:         <how often this Directive itself should be revisited>
- expiry_or_review_date:  <date the Directive expires or must be re-confirmed>
```

The three load-bearing fields are **`non_goals`**, **`allowed_stakes`**, and
**`stop_conditions`** — they are the per-Directive leash. Keep `objective` broad
enough that MSTR has room to ideate; keep `non_goals` and `allowed_stakes` tight
enough that "faithful extension" stays legible.

---

## Active Directives

> Directives are authored by Andrew and transcribed by the CTO per the Directive
> Authoring Protocol above. `/govern` originates work only under a Directive that
> passes ignition validation — well-formed, `status: active`, `issued_by: andrew`.

```
### D-001 — Drive Opal to done: complete every active project, then validate the whole product
- directive_id:           D-001
- status:                 active
- issued_by:              andrew
- issued_at:              2026-05-22
- objective:              Drive the entire Opal workspace to a finished, trustworthy
                          state, as the ultimate driver that meta-analyzes above
                          Tier 1. Two phases. PHASE 1 — drive every genuinely-active
                          project in the registry to completion through Tier 1.
                          PHASE 2 — exhaustively validate the whole delivered product:
                          confirm every key number is correct and reasonable via
                          meta-analysis, and that the front end actually displays what
                          agents claim is done.
- scope:                  PHASE 1 — first establish ground truth: triage every Active
                          row in org/projects/REGISTRY.md into complete / superseded /
                          cancelled / genuinely-active / on-hold, so "all active work"
                          has a definition before it is pursued; then drive each
                          genuinely-active project to its done-state by chartering
                          through CTO/COO. PHASE 2 — validate each project as it
                          closes via the verify-channel methodology — MECHANICAL
                          (artifacts exist, fresh, scaled, not-frozen, per the
                          4-check), NOVEL (project-specific substance against fresh
                          probes the producer did not run, with data the producer
                          did not gate on), and META (verifier ≠ fixer,
                          sharpest-test-binds, final decision-useful meta-gate). A
                          project that closed mechanically without verify-channel
                          applied is INCOMPLETELY CLOSED — it does not count toward
                          PHASE 1 success signals. Apply the same methodology
                          retroactively to the HISTORICAL Completed / Archived rows
                          in REGISTRY.md — the existing closed list is the queue for
                          PHASE 2's backward-facing sweep. Then run a final
                          exhaustive cross-product sweep once both the active queue
                          and the retroactive sweep are drained: numbers correct AND
                          reasonable, methodology consistent across surfaces,
                          pipelines robust as new data flows (not merely correct at
                          one snapshot), and the front end verified by screenshot /
                          acceptance test to display the validated state. MSTR
                          governs through the org — it charters and delegates; the
                          validation it performs directly is read-only meta-analysis.
- non_goals:              MSTR does not itself edit code, gold scripts, Terraform, or
                          portal files — it governs through Tier 1 (Constitution:
                          govern-through-the-org). When validation finds a defect,
                          MSTR CHARTERS the fix through CTO/COO; it never fixes it
                          itself. Originating new product strategy — new features,
                          metrics, cohorts, views, or bets — is OUT; this Directive is
                          a completion-and-validation mandate, not a strategy mandate.
                          Governance / tier-structure / constitution changes are OUT.
                          Visual / UI design changes are OUT (front-end DATA-correctness
                          is in scope; front-end DESIGN is not).
- allowed_stakes:         S0-S3
- success_signals:        PHASE 1 — every REGISTRY Active row is resolved: each project
                          is closed (complete / superseded / cancelled) or on-hold with
                          a named external blocker; no project sits dormant without a
                          decision. PHASE 2 — every claimed-complete deliverable is
                          independently validated via the verify-channel methodology
                          (mechanical/novel/meta), the front end is verified to display
                          the validated numbers, every defect found is chartered to a
                          fix — not merely logged, and every HISTORICAL Completed /
                          Archived row has either passed retroactive verify-channel
                          or been explicitly downgraded if it fails. META — every
                          claimed-complete deliverable is meta-analyzed against its
                          holistic purpose: does the output, viewed in the larger
                          context the work was supposed to serve, actually achieve
                          that purpose? A mechanically-functional output that fails
                          this test — e.g., a daily pipeline that runs successfully
                          but pulls the same 10 rows every day, or a chart that
                          displays values inside a healthy axis range but the values
                          don't represent what the chart claims — is NOT a success.
                          It is a finding that gets chartered to a fix. The
                          meta-analysis is the load-bearing test; the mechanical
                          checks are necessary but not sufficient.
- stop_conditions:        MSTR halts and reports to Andrew when: the active queue is
                          genuinely drained AND the exhaustive validation sweep is
                          complete with every finding either cleared or chartered; OR
                          Andrew issues a halt; OR a finding requires a product-judgment
                          or new-strategy call beyond this Directive (surfaced to
                          Andrew, never auto-resolved); OR the only path forward is an
                          S4 action (outside allowed_stakes — proposed to Andrew).
- review_cadence:         daily — re-read every /govern cycle; /mstr_review on its
                          standing cadence is the load-bearing drift check (a broad
                          Directive makes the review cadence the safety mechanism).
- expiry_or_review_date:  2026-05-25 — a review checkpoint, not a hard expiry; Andrew
                          reviews progress and extends / adjusts / closes.
```

```
### D-002 — Standing maintenance: tech-debt cleanup via compiler development
- directive_id:           D-002
- status:                 active
- issued_by:              andrew
- issued_at:              2026-05-22
- objective:              When D-001 PHASE 1 (drive active) AND PHASE 2
                          (verify-channel sweep, including retroactive on the
                          historical Completed list) are both materially
                          drained, MSTR does NOT idle and does NOT originate
                          new product strategy. It works on code review +
                          validation + tech-debt cleanup — but EXECUTED
                          THROUGH COMPILER DEVELOPMENT. The comp-* tools are
                          the structural-understanding layer that reveals
                          which tech-debt is safe to touch given the
                          interwoven dependencies. Cleanup runs through
                          compiler dev, not parallel to it.
- scope:                  IN: (i) extending comp-* with new analyses —
                          dead-code, unreachable-branch, cross-module
                          dependency mapping, doc-vs-code drift,
                          duplicated-logic, schema-drift, orphan-consumers,
                          and any other failure mode the fabric has hit
                          before (the audit-discipline classes in
                          MSTR-memory are a primary source of check ideas;
                          novel patterns surfaced during system-understanding
                          work are another); (ii) running the new comp-*
                          check, producing a finding list; (iii) chartering
                          targeted fixes against THAT finding list through
                          CTO/COO — because the compiler trace shows the
                          dependencies the fix must respect; (iv) read-only
                          system-understanding work between comp-* cycles —
                          PRDs, architecture docs, data-flow maps — so
                          subsequent governance is better-grounded.
- non_goals:              OUT: BLIND tech-debt cleanup. A cleanup charter
                          without a comp-* finding-list backing it is out
                          of scope — that is the structural guard against
                          breaking interwoven dependencies. OUT: originating
                          NEW PRODUCT strategy of any kind (financial
                          metrics, cohorts, market coverage, UI views,
                          features, vendor bets). OUT: pre-empting active
                          D-001 work; D-002 is opportunistic and fills idle
                          time. OUT: MSTR editing code itself (Art. VI).
                          OUT: front-end UI design changes.
- allowed_stakes:         S0-S2   (MSTR analyzes and charters; never
                          procurement / deploys / destructive ops.)
- success_signals:        Every idle cycle (D-001 materially drained AND
                          no pending MSTR delegation receipts) produces at
                          least one of: a comp-* extension charter, a
                          finding list from a comp-* run, a charter for a
                          cleanup tied to a specific finding, or a
                          documented system-understanding artifact. An
                          empty idle cycle is itself a finding — the scan
                          was too shallow. META — each comp-* extension is
                          itself meta-analyzed: do its findings tie to real
                          failure modes in the holistic-purpose sense, or
                          is the check producing noise? A comp-* extension
                          that runs and produces only false-positive
                          findings — or finds things that are technically
                          true but not load-bearing for the system's actual
                          purpose — is itself a finding, not a success. A
                          cleanup charter against a comp-* finding is
                          meta-analyzed similarly: did the fix actually
                          improve fabric robustness, or did it just satisfy
                          the check while leaving the underlying purpose-
                          gap intact?
- stop_conditions:        D-001 active queue re-fills -> D-001 pre-empts.
                          A finding requires product-judgment to address ->
                          surface to Andrew. A cleanup would require an S3
                          act -> propose, do not proceed. Andrew halts.
- review_cadence:         each /mstr_review reports D-002 throughput as
                          a dedicated section: comp-* extensions shipped,
                          finding lists produced, cleanups chartered,
                          system-understanding artifacts.
- expiry_or_review_date:  standing — Andrew revisits if maintenance
                          competes with active work or produces low signal.
```

```
### D-003 — Standing facilitation of the COMP_LEARNS workstream (CL fabric)
- directive_id:           D-003
- status:                 active
- issued_by:              andrew
- issued_at:              2026-05-22
- objective:              Provide standing Tier-0 facilitation to the
                          COMP_LEARNS research workstream and its agent
                          team in the feature_clb fabric — a separate repo
                          + broker channel from the ajb_workspace mandate
                          of D-001. MSTR coordinates with the CL Tier-1
                          (1.1.0_SA_CTO, 2.1.0_SA_COO, 2.1.0_SC_CompLearns,
                          3.1.0_SA_CVO) and the CL DS team (1.1.0 / 1.2.0 /
                          1.3.0 / 1.4.0_DS_CompLearns). MSTR acts as
                          supply-side authority (Andrew architectural
                          ruling 2026-05-22 — "MSTR = creator and
                          destroyer"): provisions and reaps CL agents to
                          fit the workstream's actual shape; ratifies
                          cross-fabric architectural calls that exceed any
                          single CL Tier-1 agent's lane; scans the CL
                          fabric for cross-coordination opportunities.
                          D-003 runs PARALLEL to D-001 / D-002 — the
                          fabrics are operationally distinct — but yields
                          cycle priority to active D-001 work.
- scope:                  IN: (i) standing read of feature_clb's project +
                          TO + telemetry state alongside ajb_workspace each
                          /govern cycle; (ii) spawn / kill CL agents via
                          .tools/spawn-agent.ps1 + kill-agent.ps1 (same
                          capability used on workspace, scoped to CL
                          serials — 8-process concurrency cap applies
                          across both fabrics combined); (iii) ratifying
                          cross-fabric architectural calls where CL Tier-1
                          needs Tier-0 authority — e.g., a decision
                          touching both the CL adapter interface AND a
                          workspace consumer; (iv) clearing blockers
                          between CL Tier-1 agents through MCP nudges or
                          charter extensions; (v) propagating sovereign
                          directives across both fabrics (the LD-0003
                          never-stop / escalation-chain ruling applies
                          fabric-wide).
- non_goals:              OUT: writing CL task orders — that is
                          2.1.0_SA_COO's authority on the CL fabric. OUT:
                          defining CL strategy — that is 1.1.0_SA_CTO's
                          authority. OUT: originating new CL Directives —
                          only Andrew may originate; if MSTR sees CL needs
                          a new mandate, it surfaces a proposal back to
                          Andrew through the Directive Authoring Protocol.
                          OUT: editing code, prompts, or architectural
                          files on the CL fabric (Art. VI — govern through
                          the org). OUT: pre-empting active D-001 work;
                          D-001 has priority when there is attention
                          contention.
- allowed_stakes:         S0-S2   (MSTR analyzes, charters, spawns, kills;
                          never originates procurement or destructive ops
                          under this Directive. A CL workstream needing an
                          S3 act surfaces to Andrew, not auto-charters.)
- success_signals:        CL Tier-1 lane bottlenecks resolvable by Tier-0
                          authority are resolved within a /govern cycle.
                          Cross-fabric architectural calls receive Tier-0
                          ratification. The CL agent population fits the
                          workstream's shape (no perpetually-idle CL
                          agents, no unaddressed CL TO surfaces).
                          /mstr_review reports D-003 throughput as a
                          dedicated section — CL facilitation actions
                          taken per cycle, cross-fabric ratifications,
                          population adjustments. META — D-003
                          facilitation outcomes are meta-analyzed against
                          the workstream's holistic purpose: does the
                          cycle's facilitation work materially advance
                          COMP_LEARNS toward its research goals (substance
                          produced, structural learning consolidated,
                          agent team productivity raised) — or is MCP
                          traffic increasing without corresponding
                          research advance? A high-activity D-003 cycle
                          that produces no material CL advance is a
                          finding, not a success.
- stop_conditions:        Andrew halts D-003. The CL workstream is itself
                          declared complete or paused by Andrew. A
                          facilitation request requires a product-judgment
                          or sovereign-strategy call -> surface to Andrew,
                          never auto-resolve. An S3/S4 act is required ->
                          propose, do not proceed. Attention contention
                          with active D-001 work -> D-001 wins this cycle,
                          D-003 work re-queues for a later cycle.
- review_cadence:         each /mstr_review reports D-003 throughput.
- expiry_or_review_date:  standing — no expiry; Andrew revisits if CL
                          workstream priorities shift, or if D-003
                          competes with D-001 / D-002 unproductively.
```

---

## Example — format reference only, NOT active

```
### D-000 — (EXAMPLE) Reduce single-vendor data dependence
- directive_id:           D-000
- status:                 retired   (example — never active)
- issued_by:              andrew
- issued_at:              2026-05-22
- objective:              Drive the portal's market-data surfaces toward
                          multi-source resilience so no single external vendor
                          is a point of failure.
- scope:                  Sourcing assessments; dual-source architecture;
                          charters handed to CTO/COO for execution.
- non_goals:              Signing vendor contracts or committing spend (S3,
                          Andrew-ratified). Changing WHAT data the product shows
                          (a product call, not a sourcing call).
- allowed_stakes:         S0-S2   (MSTR assesses and charters; it does not
                          propose the gated procurement itself)
- success_signals:        Every market-data surface has a documented primary +
                          fallback source; no surface single-vendor without an
                          explicit accepted risk.
- stop_conditions:        Andrew rules the single-vendor risk acceptable; or a
                          dedicated-seat procurement supersedes the work.
- review_cadence:         monthly
- expiry_or_review_date:  2026-08-22
```

---

## Retired Directives

_Retired Directives move here with their retirement date — kept for the audit
trail and so `/mstr_review` can resolve historical `directive_refs`._

_(none yet)_

---

## Versioning

Any edit by Andrew bumps **Version** and **Last updated** above. MSTR re-reads on
its next operating cycle and the cycle record attests the new version. A Directive
set is never silently changed — the version bump is the signal MSTR keys on.
