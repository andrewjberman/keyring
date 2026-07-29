# 2026-07-29 — 1248-1416Z: state re-check on Andrew's ask — the "nothing pending" answer went stale

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

Andrew asked me to re-check current state. **The answer changed: there IS new DE work on DEV, and
it is NOT promotable.** No deploys this window; the deliverable is the measurement and two routed
findings.

---

## STATE, MEASURED 1416Z

```
origin/PROD  83afea3fb61e6bf744fb4545688c19b1860ac7b2   (v2.1.152, unchanged since 0545Z)
origin/DEV   72f132c5f24c65e0e2d329277313fae48bf842f9
newest tag   portal-v2.1.152, peeled == PROD head
main tree    DEV                                        CLOUD sync: behind 0, ahead 1 (not mine)

UNPROMOTED (1 commit):
  72f132c5  0.4.0_DE_ClientPlatform  2026-07-29T09:22:57-04:00
  "mp(trend): remove the Value/Count toggle from AUA Trend Analysis -- state and count
   branch deleted with it (ANDREW-DIRECT ~0845Z via COO 124351Z)"
```

**This lands AFTER CTO's 124133Z formal answer that DE's shipped queue was EMPTY.** That answer was
correct when given and is now stale — not a contradiction, a change in the world since. Flagged to
CTO so the record given to Andrew does not stand stale, and to Andrew directly.

---

## FINDING 1 — NOT PROMOTABLE: Surface-Check rc=2, no ack at all (THIRD today)

```
72f132c5  CI - Build & Validate : completed/SUCCESS
72f132c5  Surface-Check Gate    : completed/FAILURE (run 30455836058)

Running comp-surface-check --mode blocking on 2 portal file(s) (un-acked SEV1 touch -> exit 2 -> FAIL)
CRITICAL: model_portfolios.benchmark (SEV1) [bd/inf/cot] via ModelPortfolios.tsx -- confirm + justify
CRITICAL: model_portfolios.headline  (SEV1) [bd/inf/cot] via ModelPortfolios.tsx -- confirm + justify
WARN: model_portfolios.aum (SEV2) · WARN: model_portfolios.peers (SEV2)
BLOCKED (SEV1, block-with-ack): a critical client-facing surface backend is touched.
```
**Measured on the commit message:** `grep -c "^SURFACE_ACK:"` = **0** AND `grep -ci surface_ack` =
**0**. The token does not appear at all — so this is NOT the anchor-position variant that bit
`d0fb493e` (ack present, wrong carrier). The ack is simply absent.

**THE RECURRENCE IS THE SIGNAL — third occurrence today on one file:**
```
d0fb493e   ack present, wrong carrier (local env, not the ^-anchored commit-message line)  -> BLOCKED
1e4bdf14   fixed: anchored line at column 0                                                -> PASS
cfc1e879 + 70166741  carried correctly                                                     -> PASS
72f132c5   ack ABSENT entirely                                                             -> BLOCKED
```
**Any commit touching `ModelPortfolios.tsx` alarms SEV1 by construction**, so the ack is mandatory
on every one of them and it is the step that keeps falling off. Twice is chance; three times in one
day on one file is a process gap. Routed to CTO as an observation worth a durable mechanism (commit
template line, or a local pre-push check mirroring the CI extraction) — **explicitly NOT proposing
to build anything, moratorium-aware.** The gate catching it every time is the only reason it stays
cheap.

## FINDING 2 — SCOPE: I judge this OUTSIDE the standing GO, and did not resolve it myself

CTO's standing GO (052600Z) covers a commit that is **"purely a re-point of an MDPF read onto the
platinum contract keys"** and explicitly excludes **"anything that ADDS logic or touches a non-MDPF
surface."** `72f132c5` **deletes a feature and its logic** — `trendMetricType` state, both charts'
count branches, count-only selectors, the W-4 count-basis band, count wiring at the series source,
three imports. **A deletion satisfies neither clause: it adds nothing, but it is plainly not a
re-point.**

**I read that as outside the standing GO and asked CTO for a fresh word rather than resolving the
ambiguity in my own favour.** I had committed to naming which side I judge it to be BEFORE moving
rather than after; this is that. Not a comment on the change's merit (it reads clean — the
zombie-branch deletion class we retired all night) or on its Andrew-direct authority.

---

## Compiler Tools

| Tool | Run? | Result |
|---|---|---|
| `gh run list/view --json` | yes (x3) | **PASS** — surfaced the Surface-Check FAILURE that a "DEV has new work" glance would have missed; `--json`, never `run watch`. |
| `gh run view --log-failed` | yes | **PASS** — gave the exact `rc=2` block text and the two SEV1 surfaces by name. |
| `git log -1 --format=%B \| grep -c "^SURFACE_ACK:"` | yes | **PASS, with its own control** — ran BOTH the anchored probe (0) and a case-insensitive any-mention probe (0). The second is what discriminates "ack present but wrong carrier" from "ack absent"; the anchored probe alone could not. |
| `git rev-list --left-right --count` / `log origin/PROD..origin/DEV` | yes | **PASS** — the range emptiness check is the primary "is anything unpromoted" instrument. |
| comp-* tools | no | Pure state measurement on known refs in a known repo — no estate traversal, no resource change, no search. The comp-rail HUD did not nudge; `comp-routes`/`comp-grep` answer different questions than "what is unpromoted and is its CI green". |

**What worked:** **re-measuring instead of restating.** I had told Andrew "nothing pending" ninety
minutes earlier with CTO's formal confirmation behind it; the honest answer at 1416Z is different,
and only a fresh measurement produced it. **A confirmed answer has a shelf life.**
Also: **running the any-mention probe alongside the anchored one.** Without it I would have reported
"anchor missing" (the `d0fb493e` diagnosis) when the truth is "ack absent entirely" — a different
defect with a different fix.

**What failed:** nothing this window.

**Gap found:** none new. The SURFACE_ACK recurrence is a process gap already routed, not a tool gap.

---

## Current State

- **PROD `83afea3f` / `portal-v2.1.152` — unchanged.** DEV is **one commit ahead** (`72f132c5`),
  **blocked on its own CI**, not on me.
- **Nothing of mine is in flight.** No open deploy ledger, no worktree (pruned), portal main tree on
  DEV, CLOUD 0 behind.
- **Local CLOUD is ahead 1 with `7b7c4a477b`** — a T-2/T-3 specs commit authored by another lane and
  left unpushed by its author. **I have NOT pushed it**; flagged to CTO rather than silently
  propagating another lane's unpushed work.
- Prior window's four promotes + the WO-3 edge flip all stand; served MDPF artifact byte-unmoved
  (`31e64570`), control unmoved (`9bae4b42`).

## Next Steps

- **[0.4.0_DE_ClientPlatform]** re-push `72f132c5` with a `^`-anchored `SURFACE_ACK:` line (draft
  text supplied in my 141909Z). New SHA -> CI green both workflows -> ping me.
- **[1.0.0_SA_CTO]** (1) scope word: does the standing GO cover a DELETION on the MDPF surface, or
  does this need a fresh GO; (2) the third-occurrence SURFACE_ACK process gap; (3) disposition on
  carrying `7b7c4a477b` on my next push.
- **[2.0.0_SA_COO]** D4 pixel read still the only unread leg across the four landed promotes.
- **[me]** HOLDING on CTO's scope word + DE's green re-push. Ready to run the full gates on either.

## Blockers

**None of mine.** The one unpromoted commit is blocked on its own CI (DE's fix) and on a scope
question I routed to CTO (his call). Both have named owners and evidence.
