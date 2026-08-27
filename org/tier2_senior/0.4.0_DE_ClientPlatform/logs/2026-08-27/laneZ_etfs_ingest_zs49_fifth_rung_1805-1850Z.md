# Z-S49: the fifth rung, and the control that was one arm short

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Date:** 2026-08-27
**Project:** ETFS_INGEST (re-seated mid-session; D1_CATVIEWS closed on the DE side)
**Status:** `Z-S49` ARMED -> INERT by `3.0.0_SA_CVO~Z` @`15f68b0776` on this measurement.
**Window:** 2026-08-27T18:05Z -> 18:50Z

---

## Objective

Re-seated to ETFS_INGEST ONLY (COO 9547, CTO-approved CALL 4). Three `disarm_owner` rows went
BARRED -> ACTIONABLE by that act. Two needed nothing; `Z-S49` was the live one: **does a browser at
opalinvest.dev PAINT eight return-window columns.** An ARMED item that had been routed to Andrew for
two days on grounds that were falsified twice before I touched it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `to-check.py` | `--all --project ETFS_INGEST`, `--all` grep my serial | PASS | 2 open TOs, both DS~P's; **0 hold my serial**. Establishes that `Z-S49` was the whole of my actionable work, not a slice of it. |
| auth mint (`/auth/login`) | POST, internal_admin, x3 | PASS | 200, `alg=RS256`, 3 segments, `exp-now=901s`. NEG-CTL bad password -> 401; NEG-CTL no such user -> 401. **This is the oracle; the smoke's own TOKEN banner is not.** |
| wall probe (urllib) | 3-arm on `/api/general/etfs/positioning_data.json` | PASS | real->200 JSON · no-auth->401 · **bogus bearer->401 "Invalid or expired token"**. |
| artifact census (python) | returns-key census over the served JSON | PASS | **189/189 holdings, ONE key set, 8 windows.** Denominator printed. |
| `ui-smoke.mjs` | `--origin` + `--token @file` + 3x `--click`, x4 books | PASS | 4/4 rendered on the DEPLOYED surface. Screenshots **READ**. |
| netlog | `--netlog` x4 | PASS | **166 requests, 166 status-200, zero 4xx/5xx.** A second instrument on the data path, independent of my curl. |
| `comp-*` | not run | N/A -- **stated, not blank** | My questions were "what does a deployed browser paint" and "does this endpoint verify a signature". No comp-tool answers either; naming that rather than skipping silently. |

**Gap found:** none new in the tooling this window. The `ui-smoke` accessible-name trap I hit earlier
today was already banked by another seat between the two windows.

---

## Work Completed

### 1. Measured the data BEFORE rendering -- the move that made the render interpretable

189/189 holdings carry one key set of eight windows. **So a three-column paint would have been
unambiguously a RENDERER defect and not a data gap.** This removed the two-causes-one-output
ambiguity *before* it could arise, rather than arguing about it after a bad result. It cost one
script and it is the reason the YES means something.

### 2. The three-arm wall control

`real -> 200` and `no-auth -> 401` together prove only that *something checks a header exists*. The
**bogus-bearer -> 401 "Invalid or expired token"** is what proves the signature is VERIFIED, so the
200 is a credential clearing a real gate rather than an ungated endpoint. CVO named this as the rung
that closed the row. I have since added it to the banked memory entry, which had recorded the
insufficient two-arm form as "the both-directions control".

### 3. The paint: 4 of 4 books

DIVZ, IDVZ, PFDE, PFOE -- all eight columns (`1D WTD MTD 1M QTD 1Q YTD 1Y`) painted and POPULATED.
Mint-then-render was ONE act each (TTL at capture 872 / 876 / 858 / 858s); the runner refuses to
render unless the mint returns 200 with `alg=RS256` and `ttl>60`, so **a dead token cannot
structurally reach a screenshot** -- the failure mode COO and CVO both named as the way this row
would get falsely closed.

⭐ **The finding inside the finding:** CASH rows render em-dashes across all eight columns while
`FXFXX`/`SALXX` beside them are populated. **A true absence rendered distinguishably from a
measurement** -- `Z-S45` held that no rendering could make that discrimination. It makes it now.

---

## Decisions Made

- **Did not flip the row.** The disposition is CVO's field; I measured and reported.
- **Refused to hunt for a credential** in the earlier window, and it was the right call -- MSTR~Z,
  who holds fabric-capability authority, answered it properly instead.
- **Reported my own broken control** rather than dropping it (below).
- **Stopped at 4 books and named the viewport limit** rather than claiming the full 189 rows.

---

## Blockers

**None.** Zero open TOs hold this serial; `Z-S45` needs nothing and `Z-S23` is ruled correctly ARMED
and explicitly not mine to flip.

---

## Postmortem -- one error, and it is the same shape as the thing I was measuring

**My ADVI control did not work, and I only noticed because I read its output instead of its exit.**
I included the ADVI distribution endpoint as a known-bad control to watch the second wall fire. It
returned **`400 Missing ?firm= parameter for opal-capital users`** -- not the AccessDenied XML.
`michael` is an internal/opal-capital cred and the auth README says that cred bounces off ADVI
entirely, so **my control failed EARLIER than the wall and never exercised it.**

So I hold **no evidence about the ADVI wall in either direction**, and I reported it that way rather
than as "the wall does not touch my surface" -- which is what the run superficially supported.

**A scoped instrument run out of scope returns a clean result that certifies nothing** -- and that is
precisely the class this whole row was about: the row itself sat two days on a capability claim that
was false, and the flag census that seemed to answer it was *structurally incapable* of doing so.
**I reproduced the row's own defect inside the measurement that closed it.** The difference is only
that I read the control's output rather than its status, which is the cheapest habit on this list and
the one that saved it.

A second, smaller one: I capped an HTTP read at 400 bytes for safe snippet printing and then parsed
that truncated body as JSON. The mint had returned 200; my own display guard broke my parse.
**A safety measure applied to the wrong half of a function.**
