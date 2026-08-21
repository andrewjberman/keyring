# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-21 0810Z – 0830Z

**archetype:** TRACE
**Projects:** D7_NOTIFY — TO-B (J1 atom-decomp: the client-facing surface)

## Summary

`D7_NOTIFY.TO-B_PROOF_OF_SPEC.json` **VALID rc=0, 4 rows, 0 violations, 4/4 PASS**, plus a generated
rectangle at `D7_NOTIFY.TO-B_RECTANGLE.json`. Read-only: nothing built, no route fetched, no browser
driven. Every claim is CODE-plane and labelled.

## 1 — The rectangle, generated rather than transcribed

**25 routes · 4 firms · 1 exempt path**, computed by parsing `App.tsx` and `firmAccess.ts` and
applying `isPathAllowedForFirm`'s own decision order. No cell was typed by hand, so there is no
INFERRED cell — a re-run regenerates it rather than re-reading my prose.

| reachability | n | routes |
|---|---|---|
| ALL-PARTNER-FIRMS | 8 | `/market` `/portfolios` `/philosophy` `/positioning` `/valuations` `/macro` `/advisor-intelligence` `/change-password` |
| PARTIAL 3 of 4 | 2 | `/trade-submission` `/submit-request` |
| NO-PARTNER-FIRM | 12 | incl. `/ticket-center`, `/security-scanner`, `/data-refresh` |
| PUBLIC | 3 | `/login` `/forgot-password` `/reset-password` |

## 2 — ⛔ My first rectangle was flat, and it would have shipped a false security claim

The router has **two** `<Routes>` blocks: an outer one in `App`, and an inner one in
`DashboardLayout` reachable **only** through the outer `/*`, whose element is
`<ProtectedRoute><DashboardLayout/></ProtectedRoute>` — verified: `<DashboardLayout />` has **exactly
one** render site, `App.tsx:583`, inside that wrapper.

A flat parse reports an inner route carrying no inner wrapper as *public*. Mine labelled
**`/dev/page-surface-control` "NONE (public)"**. It is not — it inherits the outer guard and is
internal-only.

**What caught it was not the parse, which was self-consistent and wrong.** It was the rule that any
row about to become a security claim gets verified at source before it is reported.

## 3 — B-2: no per-ticket deep link, by two independent routes

**Route param:** of 25 routes, exactly 2 carry a param/wildcard (`*`, `/*`), both catch-alls.
**Query param:** zero `useSearchParams` / `location.search` in the TicketCenter page — its 6
`ticket_id` hits are React keys, a table cell, and claim/complete button targets. The page is a
**list** with no single-ticket view and no selection-by-URL.

**Discriminating control:** the same regex against a synthetic `/ticket-center/:ticketId` fixture
**does** return it and **does** flag the param — so the absence is measured, not a broken search.

→ **A4's CTA resolves to the list page by fact, not by choice.**

## 4 — B-3: the boundary, with the denominator stated as FIRMS

`/ticket-center` is in **0 of 4 firms** *and* behind `requireInternal`, which fires **before** the
matrix is consulted — two independent gates, and the board is correctly internal.
`/submit-request` is in **3 of 4 — 49financial, cottonwood, demo; NOT inflection**, deliberately
(`firmAccess.ts:66` names the 2026-05-28 ruling).

Denominator stated as firms rather than paths at COO~Z's pre-emptive request: the allowlist is keyed
by firm, so a path-framed count is the one frame a later reader cannot re-derive from it.

**Plane check, and it was wrong first:** I ran `git log origin/PROD..origin/DEV`, which asks whether
DEV is ahead — but the served plane is PROD, so the question is the reverse. Re-measured: PROD is 11
ahead overall, **0** on the two files. **The conclusion survived by luck, not by the check I ran.**
Residual held open: branch agreement is not proof the deployed bundle was built from `origin/PROD`
HEAD. That is CI's plane and nothing here claims it.

## 5 — The finding that lands on E-0

`/cma`'s redirect is commented *"deliberately OUTSIDE ProtectedRoute"* because *"advisors bookmark
pages and links live in email"* and gating it would bounce a partner-firm user *"instead of forwarding
them."* **It sits in the inner block, so the outer layout guard runs first** — `/cma` is in 0 of 4
allowlists and is not exempt, so a partner-firm user **is** bounced to `/market`, which is exactly
what the comment was written to prevent.

Bound: CODE-plane reading of the router's structure; **not exercised in a browser**, so it is a claim
about the code path rather than an observed bounce. It bears directly on E-0 — the very case the
comment reasons about, a link that lives in email, is the case that fails.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find -i requireInternal portal/src/` | 5 / 412 files — **both** gates (`App.tsx:459` declaration, `ProtectedRoute.tsx:44` predicate) | the concept spans two files; a single-file token count cannot see it |
| `comp-find -i` × 3 more (firmAccess, TicketCenter, allowlist) | denominators printed, read **unfiltered** | after this morning's filter defect, no comp-find output is truncated here |
| rectangle generator (python parse) | 25 routes / 4 firms, generated not transcribed | flat version wrong on 5 guards; nested version landed |
| route-regex positive control | synthetic `:ticketId` fixture detected | the B-2 absence is measured |
| `git -C portal` plane check | PROD 11 ahead, 0 on the two files; fetch freshness verified | direction corrected mid-check |
| `proof-of-spec-check` positional | rc=0, rows=4, violations=0, VALID | PASS |
| own-instance mutant, anchor-asserted | rc=1, violations=2, INVALID naming B-1 | CONTROLLED |

## Blockers

**None.** TO-A next — eight criteria, re-read from the ref for A-3b, and **A4 is now resolved to the
list page by TO-B's own measurement**, so nothing in it waits on a decision. Per CTO~Z's standing
instruction I am reporting on completion of A rather than per-TO. The W-F import edge remains
unwritten and is TO-F's last act. Zero crons, nothing applied.
