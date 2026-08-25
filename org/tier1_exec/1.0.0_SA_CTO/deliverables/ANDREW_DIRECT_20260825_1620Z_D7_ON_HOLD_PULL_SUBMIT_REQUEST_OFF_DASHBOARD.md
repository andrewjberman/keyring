# ANDREW-DIRECT 2026-08-25 ~16:2xZ -- D7 EFFECTIVELY ON HOLD + pull the client-facing request form off the dashboard

**Channel:** CTO terminal, direct to `1.0.0_SA_CTO`. **Recorded by:** `1.0.0_SA_CTO`.
**Broadcast:** MSTR (action owner), same turn. **Record+broadcast law discharged.**

---

# ⛔ SCOPE AMENDED ~16:4xZ -- READ THIS BEFORE THE RECOMMENDATION BELOW. FULL REMOVAL, NOT PARTIAL.

**The "SCOPE RECOMMENDATION" section further down is WITHDRAWN.** It recommended retaining the
route, page and intake client so D7 could resume. **That is wrong and must not be executed.**

Andrew-direct, same terminal, ~16:4xZ, VERBATIM:

> "D7 is fine, the issue is some agent at some point some agent thought it would be a good idea to
> make a separate page/function from Ticket Center rather than repurposing a client-facing version
> of Ticket Center (which was the wrong direction) and this page has existed ever since and I do not
> want it,"

**HIS OBJECTION IS ARCHITECTURAL, NOT A PAUSE.** `SubmitRequest` should never have been built as a
separate page; the correct shape was a client-facing MODE of Ticket Center. So the page is not an
asset to preserve for a resumed D7 -- it is the mistake itself. Retaining it would preserve exactly
what he is asking us to delete and would hand the next D7 seat the wrong starting point.

**MY ERROR, NAMED:** I inferred from "D7 is on hold" that the artifact was paused work worth keeping.
He had said nothing about the artifact's merit at that point, and I supplied a rationale
("on hold is not licence to delete the work") that read as caution but was an unfounded assumption
about WHY he wanted it gone. **The lesson is narrow and worth keeping: "on hold" describes the
DIRECTIVE's status and says nothing about whether a given artifact under it is wanted.**

**AMENDED SCOPE -- REMOVE ALL OF IT:**

| path | disposition |
|---|---|
| `portal/src/App.tsx:122` | REMOVE -- nav entry |
| `portal/src/App.tsx:34` | REMOVE -- lazy import |
| `portal/src/App.tsx:480-486` | REMOVE -- the `<Route path="/submit-request">` |
| `portal/src/lib/firmAccess.ts:52,83,98` | REMOVE -- three firm allowlist entries |
| `portal/src/pages/SubmitRequest/` | REMOVE -- the page itself |
| `portal/src/api/endpoints/ticket-intake.ts` | REMOVE **only if nothing else imports it** -- verify by reference search, not assumption; if something does, keep it and say so |

**STILL NOT IN SCOPE -- TICKET CENTER SURVIVES.** `/ticket-center`, `tickets.ts` and
`pages/TicketCenter/` all stay. His complaint is that Ticket Center was the RIGHT vehicle and
something got built beside it, so Ticket Center is the survivor, not a co-casualty. A seat reading
"remove the ticket stuff" quickly could take both; it must not.

**ALSO NOT IN SCOPE:** the backend `/api/scoped/tickets/submit` route and the `opal-ticket-api`
Lambda. This is a FRONTEND removal. Anything server-side is a separate act.

---

## VERBATIM

> "D7 is effectively on hold, however with that said, I want the "Submit a Ticket" sidebar item
> pulled off dashboard. That whole functionality is broken and shouldnt even be on the dashboard.
> Mention this to MSTR and have them bring out an 0.3.0_DT_TradingOperations to go get rid of it
> and /prod-deploy"

## TWO INSTRUCTIONS

1. **D7 (Ticketing intake) is EFFECTIVELY ON HOLD.** Register-relevant; MSTR's surface.
2. **Remove the client-facing request form from the dashboard and promote to PROD**, executed by a
   spawned `0.3.0_DT_TradingOperations` (he named the seat himself).

## ⚠ THE LABEL HE USED DOES NOT EXIST IN THE CODE

He said **"Submit a Ticket"**. `comp-find -i "Submit a Ticket"` over `portal` returns a **MEASURED
ZERO across 1,088 files scanned**. The real item is:

```
portal/src/App.tsx:122
{ path: '/submit-request', label: 'Submit a Request', icon: Send },
```

**"Submit a Request"**, in the Tools section, immediately above "Ticket Center". Unambiguously the
item he means -- it is the D7 client-facing intake form -- but a seat handed his words verbatim and
no map would search for a string that is not there. Recording the discrepancy so the identification
is auditable rather than assumed.

**TICKET CENTER IS NOT IN SCOPE.** It is a separate internal board (`/ticket-center`), with a
separate client (`tickets.ts`) that never imports the intake client. Two subsystems, one word.

## LIVE ON PROD -- verified against the remote

```
git -C portal show origin/PROD:src/App.tsx  ->  :122 nav entry, :481 route
```
A genuine PROD removal, which is why the `/prod-deploy` is required rather than optional.

## ⚠ EXPOSED TO THREE PARTNER TENANTS RIGHT NOW

`portal/src/lib/firmAccess.ts` allowlists `/submit-request` for **49financial (:52), cottonwood
(:83), demo (:98)**. Inflection deliberately does not have it (the 2026-05-28 no-Tools-section
ruling). **A broken client-facing form is presently reachable by three partner tenants** -- the
detail that makes this more than cosmetic.

## THE FULL SURFACE

| path | what |
|---|---|
| `portal/src/App.tsx:122` | the sidebar nav entry -- **his literal ask** |
| `portal/src/lib/firmAccess.ts:52,83,98` | three firm allowlist entries (what actually exposes it) |
| `portal/src/App.tsx:34` | the lazy import |
| `portal/src/App.tsx:480-486` | `<Route path="/submit-request">` |
| `portal/src/pages/SubmitRequest/` | the page (`SubmitRequest.tsx`, `index.ts`) |
| `portal/src/api/endpoints/ticket-intake.ts` | the submit-path client (intake ONLY) |

## SCOPE RECOMMENDATION -- offered to MSTR/Andrew, not adjudicated here

**Remove the nav entry + the three firmAccess entries. Retain route, page and intake client.**

- The nav entry is exactly "off dashboard".
- The firmAccess entries are what expose it to the three tenants; removing the nav alone leaves the
  route reachable by direct URL for them. His stated reason is that the functionality is BROKEN --
  leaving a working door to a broken form is half the job.
- Retaining route+page keeps the diff small and lets D7 resume without rebuilding. **He said ON
  HOLD, not cancelled; "on hold" is not licence to delete the work.**
- **RESIDUAL, named:** with route+page retained, an internal (non-partner) user could still reach
  `/submit-request` directly. A deliberate trade, not an oversight. Full removal is the same PR and
  one more hunk if he wants it.

## BINDING ON THE EXECUTING SEAT

- **`/prod-deploy` is DT-ONLY**; it is the canonical procedure, not to be improvised.
- **Rule 19:** portal main worktree stays on **DEV**, always; the promote runs in an **ephemeral
  worktree**. (Verified: `git -C portal rev-parse --abbrev-ref HEAD` = `DEV`.)
- **Zero typescript errors before promote.** `ci.yml:56`'s "Type Check" step is a zero-file
  `tsc --noEmit` -- a log-honesty defect already on the record. The real typecheck is step 5's
  `bun run build` (`tsc -b && vite build`). Do not read a green "Type Check" as coverage.
- **NEVER#6:** a begun deploy finishes in-session or rolls back loud. Deploy-completion ledger entry
  opened at start under `org/critical_paths/change_management/`, closed at completion.
- Verify the CI conclusion with `gh run view --json` (`gh run watch` can hang on benign warnings).

## WHAT THIS SEAT DID NOT DO

**I did not verify his "that whole functionality is broken" claim.** He owns the product and the
instruction is sufficient on his word alone; re-litigating it would cost time and change nothing.
Recorded so that nobody later cites this seat as having *confirmed* the defect -- **the removal
rests on his word, not on a diagnosis anyone ran.**
