# ADVI — lock white-label user patricia to Demo + hide partner selector
**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT

**Agent:** 0.4.0_DE_ClientPlatform
**Window:** 2026-06-17 ~1430Z -> 1501Z (session start -> this log)
**Commits (this author):**
- `378fd8ff` (portal DEV) — fix(ADVI): lock white-label user patricia to Demo + hide partner selector (Andrew-direct)

## Summary

Andrew-direct, in-session (no formal TO). Yesterday (commit `8f564d42`) patricia@whitelabelcreative.com
was given a Demo landing DEFAULT on the Advisor Intelligence (ADVI) page. Andrew smoked localhost today
and found she still had the full "Select Partner" dropdown + access to all partner data. Diagnosed the
gap, converted the default into a hard LOCK, committed to portal DEV. Andrew re-smoked as patricia and
confirmed fixed.

## Diagnosis (root cause)

- Patricia is provisioned `firmId=opal-capital`, so `isInternal()` (AuthContext.tsx:551,
  `claims.firmId === 'opal-capital'`) returns true.
- `AdvisorIntelligence/index.tsx` passes `allFirms` + `onFirmChange` to the partner view for ANY
  internal user. Every partner view gates the selector on `internal && allFirms && onFirmChange`
  (e.g. demo/index.tsx:184). So patricia got a rendered, fully switchable dropdown.
- Yesterday's `ADVI_DEFAULT_BY_EMAIL` map set only the initial `useState` value to 'demo' — a
  landing default, not a restriction. She could switch to 49F/inflection/cottonwood real data.

## Fix

`portal/src/pages/AdvisorIntelligence/index.tsx` — converted the email map from a default to a lock:
- `ADVI_LOCKED_FIRM_BY_EMAIL[user.email.toLowerCase()]` -> `lockedFirmId` ('demo' for patricia).
- `firmId = lockedFirmId ?? (internal ? selectedFirmId : claims.firmId)` — firm PINNED, non-switchable.
- `showSelector = internal && !lockedFirmId` -> false for her; `allFirms`/`onFirmChange` passed as
  `undefined`, so the dropdown short-circuits OFF (a locked internal user behaves like an external
  single-firm user on ADVI while keeping full-portal access via opal-capital).
- Normal internal users provably unaffected: no lock -> `showSelector = internal`, identical prior
  behavior. `tsc -b --noEmit --force` clean.

## Architecture decision (Andrew-direct 2026-06-17)

FE one-off, NO `opal-partners-misc` DynamoDB permissions table. Confirmed no such table exists (only
`opal-partners-*` hit is the existing ADVI *data* Lambda `opal-partners-data`, unrelated). A
permissions table would need reader plumbing (auth-handler -> claims injection -> FE consumer) that
nothing currently has; not worth it for a single one-off user. Reaffirms the prior trace
(memory: reference_portal_user_provisioning_and_per_page_view_defaults).

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-transform schema-check` | AdvisorIntelligence / DemoAdvisorIntelligence | N/A (not found) | tool keys on a registered component name not matching these exports; change is prop-gating not schema/data-prop, so not applicable |
| `comp-which` | "hide partner selector for one user on ADVI" | NO MATCH | router returned no specific tool; expected for a render-gate change |
| safe-commit `[surface-check]` | advisor_intelligence (SEV1) | ADVISORY (passed) | critical-surface touch flagged; advisory mode (not blocking); justified one-off, no data-contract change |

**What worked:** Direct read of the consumer chain (index.tsx -> 4 partner views) was the real
dependency check — every view gates the dropdown identically on `internal && allFirms && onFirmChange`,
so passing those undefined is the clean hide. surface-check correctly flagged the SEV1 ADVI touch.
**What failed:** `comp-transform schema-check` could not resolve the ADVI component by export name —
not a blocker here (no data-prop/schema change) but a recurring naming-resolution gap for page-level
components. **Gap:** none new; schema-check component-name resolution for `src/pages/*` exports is the
known limitation.

## Files Modified

See commit message `378fd8ff`. One file: `portal/src/pages/AdvisorIntelligence/index.tsx`
(+17 / -11).

## MCP / coordination

3 Andrew-direct messages handled (the task + 2 scope clarifications converging on FE-not-table).
No inter-agent dispatches. No RAVC loops opened.

## Blockers

None.

## Current State

- Fix committed to portal DEV as `378fd8ff` (LOCAL — **not yet pushed** to origin/DEV).
- Andrew verified on localhost (logged in as patricia): dropdown gone, Demo-only — CONFIRMED good.
- Verification dependency (banked to memory): the lock keys on `user.email`; it only applies under a
  REAL patricia login. The dev-bypass (`window.__devBypass`) hardcodes `dev@opalcapital.com`
  (AuthContext.tsx devBypass), so a dev-bypass smoke will NOT show the lock — must log in as patricia.

## Next Steps

- [0.4.0_DE_ClientPlatform] Push `378fd8ff` to portal DEV on Andrew's go (deploys to DEV server).
- [DT] PROD promote is the separate batched DT-lane step (`/prod-deploy`), Andrew's call — fold this
  ADVI commit into the next portal DEV->PROD batch.
