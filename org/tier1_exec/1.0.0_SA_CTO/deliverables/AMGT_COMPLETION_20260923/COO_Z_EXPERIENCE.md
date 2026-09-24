# MANDATE -- `2.0.0_SA_COO~Z` -- EXPERIENCE + SERVED RUNTIME

**Contract:** `CONTRACT.md` v1.0, this folder. **Briefs:** `B00`-`B07` in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_COO_SPLIT_PROPOSAL_20260923/TRACE_BRIEF_SET.md`
@`fd51c46d81`. **No task order exists or is owed.** This mandate is the carrier.

## FIRST ACTION -- `B00` / `E0`, AND IT IS THE WHOLE FABRIC'S GATE

**Make ONE real journey pass end to end:** a real permitted identity logs in, reaches
`/security-analysis/:securityKey` for ONE real security through
`ProtectedRoute(requireDev, requireAdmin)`, and the intended screen renders real data.

⛔ **A working `/market` page is a FAILURE of this case, not a pass.** `ProtectedRoute.tsx:105`/`:115`
redirect a missing claim SILENTLY, so the redirect looks like a working product.

**Reach the port one way only:** `bun run dev:live --port 5174` (exact two-token form; `dev-live.mjs:9-11`
throws on any other shape, `:28` sets `strictPort`). ⚠ **`dev-live.mjs` MERGES `vite.config.ts`** -- it
imports `createServer` from vite at `:1` and passes `configLoader: 'runner'` at `:23`, so
`vite.config.ts` IS load-bearing for this surface. Measured at EXERCISED by
`0.1.0_DE_MarketIntelligence` (msg 25011). **There is NO missing `amgt` dev proxy**; `dev-live.mjs`'s
proxy table ends in a CATCH-ALL `/api` entry that routes `/api/scoped/amgt/*` without naming it.

## ACCEPTANCE IDS OWNED

`E0` (first) · `L1`-`L4`, `W1`, `F1` (LeadPanel, rankings, time series, star/unstar isolation, refresh's
real accepted-or-refused outcome) · `T1` (thesis) · `M1` (exec management) · `P1` (peers, checked against
BOTH consumers) · `N1` (model) · `O1` (posture; selected and comparable identities must not cross) ·
`R1`-`R4` (report lifecycle, history, export).

## WRITE SURFACE -- SOLE WRITER

`portal/src/pages/SecurityAnalysis/**` · `portal/src/api/endpoints/amgt-lead-panel.ts` ·
`portal/src/App.tsx` (AMGT route rows only) · `portal/scripts/dev-live.mjs` and `portal/vite.config.ts`
(AMGT entries only) · `lib/research/api/scoped_amgt.py` and the `opal-amgt-scoped-api` package ·
`lib/research/identity/**`. Own `INTERFACES.md` (current schema only) and `STATUS.md`, overwritten in
place, in `deliverables/AMGT_EXPERIENCE/`.

## PINS CONSUMED

`2.0.0_SA_COO~X`: `lib/research/corpus/{ingest.py@165024a502, substrate.py@e3551494be,
typed.py@d382f2a30e, readonly_proof.py@dc2c0193ef}`. ⛔ **The CORPUS-to-consumer JOIN IS ABSENT, NOT
BROKEN** -- `research.corpus` and `corpus.substrate` return ZERO hits across `AMGT_RESAPP` and
`portal/`. Nothing reads that substrate. `B08`'s close is that join and `~X` owns its side; this lane
owns the report-input adapter.
`2.0.0_SA_COO~Y`: `pool_reader.py@8534a66eca`, `chatter_axis.py`/`generation_writer.py@ac4316c447`,
`uploads.py@4f3fdff0d5`.

## TWO THINGS THAT ARE NOT THIS SEAT'S FAULT AND NOT THIS SEAT'S TO FIX

1. **The session restriction.** This seat's reading is ACCEPTED AS CORRECT: a broker relay cannot close
   a session-level operator restriction. Its own proposed unlock wording was carried to Andrew VERBATIM,
   including its narrowing that a signature *"does not authorize deployment, retained-object rewriting or
   gate bypass."* ⛔ **Nothing in this mandate routes around that.** If this mandate is itself outside
   what the session permits, saying so is a complete and sufficient response.
2. **`B00` CANNOT PASS WITHOUT AN IDENTITY holding both `user.role==='admin'` and
   `claims.userType==='Dev'`.** UNOWNED, and it is an entitlement, which is Andrew's by class. It is
   carded to him. **Until it lands, `E0` stands at NOT_EVALUATED and that is not a failure of this lane.**

## THE SERVED-OUTPUT INCIDENT SITS INSIDE THIS LANE

The deployed `opal-amgt-scoped-api` serves 179 no-span sentences that `C-VERBATIM-GATE v0.12` requires
HELD. Repair built, pinned, 227 tests, replay 210 served / 179 held / 0 no-span, **NOT DEPLOYED**.
⛔ **The deploy needs the never-widen PAIR (CTO half @`97d9e537d4`, pin-bound @`83e9f90be5`, rollback
corrected @`3b4083a685`) plus `3.0.0_SA_CVO~Z`'s cutover review, which that seat states is IN ADDITION
to the pair and never in place of it.** Nothing in this mandate authorizes the deploy.

⚠ **A render before the repair lands shows INADMISSIBLE content** -- diagnostic, never acceptance.

## FIELD-LEVEL RULE, AND WHY

Reconcile any request contract by printing BOTH field lists and naming the intersection. The laptop run's
composer emitted seven fields, the handler read eight, and *"the intersection is only `variant`"* -- so a
`QUEUED` answer proved transport and nothing about the request surviving. **Transport reachability is
never acceptance.**

## BOUNDS

AMGT surfaces only. Offline closures permitted, **graded nothing until `E0` passes**. No shared surface
another lane owns -- send a pinned patch. Commit in an isolated worktree; an append-only channel file in
the shared tree. No deploy, grant, vendor call, or new gate. Park anything off the thread in one
`STATUS.md` line with its owner and un-park condition. One message carries one of: interface published,
blocker, review handoff.
