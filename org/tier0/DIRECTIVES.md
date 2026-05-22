# DIRECTIVES — The Active Mandate for `0.0.0_AB_MSTR`

**Status:** v1.3 — D-001 active (rewritten 2026-05-22 to the broad two-phase whole-workspace mandate); format + authoring protocol ratified v1.2
**Authority:** Andrew authors; the CTO transcribes. A Directive's mandate is Andrew's alone — MSTR may *propose* and the CVO may review and recommend, but a Directive is added, amended, or retired only by Andrew, via the Directive Authoring Protocol below. A Tier-0 law document, never CVO-ratifiable (Constitution Art. III, XIV). (owned-paths: `TIER0_LAW`, `permitted_agents: []` — no standing agent write access.)
**Version:** 1.3 · **Last updated:** 2026-05-22
**Amendment history:** v1.1 — Directive format tightened to a full schema (external Phase-3 review). v1.2 — Directive Authoring Protocol codified (Andrew directive 2026-05-22). v1.3 — D-001 rewritten from "Finish ADVI" (task-altitude) to the broad two-phase whole-workspace mandate; the ADVI-specific substance moved to the ADVI_VALFIN PRD / project (Andrew directive 2026-05-22).

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
                          closes, and run a final exhaustive cross-product sweep once
                          the active queue is drained: numbers correct AND reasonable,
                          methodology consistent across surfaces, pipelines robust as
                          new data flows (not merely correct at one snapshot), and the
                          front end verified by screenshot / acceptance test to display
                          the validated state. MSTR governs through the org — it
                          charters and delegates; the validation it performs directly
                          is read-only meta-analysis.
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
                          independently validated (numbers correct + reasonable,
                          methodology consistent, pipelines self-healing), the front end
                          is verified to display the validated numbers, and every defect
                          found is chartered to a fix — not merely logged.
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
