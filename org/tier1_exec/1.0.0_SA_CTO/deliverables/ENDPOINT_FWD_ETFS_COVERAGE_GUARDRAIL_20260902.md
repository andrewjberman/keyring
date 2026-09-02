# ENDPOINT (step 2, `/endpoint --forward`) — ETFS coverage guardrail

**Emitted by:** `1.0.0_SA_CTO` · **Date:** 2026-09-02 · **Pipeline step:** 2 (before the PRD, before any TO)
**Status:** ⛔ **NOT YET LANDED IN A PRD.** This block is ready to paste; see "Where this belongs" below.

---

## F1 — The brief this reads (and it reads nothing else)

| | |
|---|---|
| **Path** | `docs/briefs/ETFS_COVERAGE_GUARDRAIL_BUILD_SPEC_20260901.md` |
| **Vintage** | `1890d7785c97e5531139dceff85d6fbacb026bf6` @ 2026-09-01T14:35:06-04:00 |
| **Author** | `4.0.0_SA_CRO` |
| **Size** | 18,680 bytes / 299 lines / 50 sections |
| **No `generated:` line** | the brief carries none; the commit above is the vintage |

---

## F2/F3 — Capability outcomes

`FWD-n` ids are **permanent and never reused**. A retired outcome leaves its number vacant.

```
  FWD-1  A day that went missing from the monthly ETF report gets filled in
         on its own, before anyone has to notice it was gone

         DONE WHEN  EXERCISED -- a real missed day has actually been caught up
                    without a person intervening
         ACCEPT     a day the report should have covered but did not gets
                    picked up on its own before the month goes out -- including
                    one where the partner's own data does not reach us until
                    nearly two weeks later
         SOURCE     brief s.3 (lines 81-129), incl. the s.3 lag table at 93-110

  FWD-2  The monthly report cannot go out over incomplete data unless a
         person decides to let it

         DONE WHEN  EXERCISED -- the check has actually refused a month, and
                    the refusal reached a person
         ACCEPT     when days are genuinely missing, the report does not go
                    out, and someone is told which days and why -- rather than
                    it arriving looking normal
         SOURCE     brief s.4 (lines 130-162), s.5 (163-189)

  FWD-3  The report states how complete it is, on its own face

         DONE WHEN  APPLIED -- the statement is in the report itself
         ACCEPT     someone reading the report can tell, without asking anyone
                    and without opening anything else, how much of the month it
                    really covers and how much was filled by repeating the
                    previous day
         SOURCE     brief s.4 (lines 155-158)

  FWD-4  A day that is legitimately empty is never "repaired" into a number
         nobody measured

         DONE WHEN  EXERCISED -- the system has actually met such a day and
                    left it alone
         ACCEPT     on a day the market was shut, or a day the partner sent us
                    holdings with no prices attached, nothing is invented and
                    nothing is reported as broken
         SOURCE     brief s.2 (lines 63-80), s.5 (185-189)

  FWD-5  Andrew and AJ both receive the monthly report automatically

         DONE WHEN  EXERCISED -- both people have actually received one
         ACCEPT     both get the same monthly report in their own inbox without
                    anyone sending it by hand, and neither one is dropped
         SOURCE     brief s.6 (lines 190-205), ruling card 3 (JOIN, not replace)

  FWD-6  The three partners' figures in the report describe the same day as
         each other

         DONE WHEN  APPLIED -- the alignment is in place
         ACCEPT     a figure shown for one partner on a given date can be set
                    beside another partner's figure for that same date without
                    the two being a day apart
         SOURCE     brief s.6a (lines 206-232)

  FWD-7  Going outside Opal to ask a provider for missing data stays a
         decision a person makes

         DONE WHEN  EXERCISED -- the system has actually stopped and asked,
                    rather than going ahead on its own
         ACCEPT     if the only way to fill a gap is to ask the outside
                    provider for it, the system stops, names the days it wants,
                    and waits for a person to say yes
         SOURCE     brief s.5 (lines 163-189), ruling card 4
```

---

## Deliberately NOT an outcome

- **Retiring `etfs-canon-fanin`** (brief s.9.1) — the brief states s.9 is *"not part of this build."*
  Carried as an independent finding with its own owner, not folded into this endpoint.
- **`ETFS_CANON` activation** — ruling card 5 sequenced it *after* the guardrail.
- **Restating already-published figures** — ruling card 2, forward-only. Excluded by ruling, not oversight.

## Where this belongs

- **Proposed PRD:** `docs/architecture/ETFS_GUARDRAIL_PRD.md` (sibling to the existing
  `ETFS_INGEST_PRD.md` / `ETFS_POSITIONING_PRD.md` / `ETFS_SECIDX_PRD.md`)
- **Section title, verbatim:** `ENDPOINT (step 2, /endpoint --forward)`
- ⛔ **The project code is UNCONFIRMED.** No register row and no PRD exist for the guardrail
  (measured: `comp-find COVERAGE_GUARDRAIL` returns the brief and tool logs only, no PRD).
  `ETFS_GUARDRAIL` is a PROPOSAL from this seat, not a ratified code.

---

## F5 — Provenance

**READ:** the brief named above, at the vintage named above, in full (299 of 299 lines).

**NOT READ, deliberately, as Phase 0 requires:**
- the task-order register (`to-check`) — at step 2 there are no task orders; reading it would blend
  *what we intend* with *what is already moving*, and nothing downstream marks which is which
- the project registry / any project JSON
- any PRD
- the directives register

**Every outcome traces to a brief line, cited inline above.** No outcome was synthesised from the
topic string or from this seat's own judgement about what the project ought to want.
