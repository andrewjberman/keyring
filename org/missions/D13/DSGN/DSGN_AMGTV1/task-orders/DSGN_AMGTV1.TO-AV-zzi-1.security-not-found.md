# DSGN_AMGTV1 task order -- `AV-zzi-1` -- DIRECT ACT: A NAME NOT FOUND IS SAID AS NOT FOUND, NEVER AS A FEED OUTAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzi-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~121</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files and their tests, rendered offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) at the cut on DELL1, on portal DEV 0008ddd3 in a worker-shaped nested worktree -- r57a.cjs 1 of 4 (arms 1-3 FAIL: no notFound.ts, no wiring; PLANTED passes); battery29 ALL PASS. On a scratch reference edit (the helper and the import + slot), r57a 4 of 4. The tree was not edited.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzi-1` (round 57, decomposition v57; serves FWD-27 and FWD-11)

On `/security-analysis`, a name the route does not know is drawn as a feed outage. Typing "Boeing" into "Search any ticker" and
pressing Enter sends the typed text as the security key (`components/LeadPanel.tsx` `handleSearchSubmit` -> `onSelectSecurity`).
Each read then answers 404, and every panel says "... could not be loaded. Try again; if it keeps failing, the feed is down." The feed is
not down: the text is not a key the route knows. `apiRequest` (`portal/src/api/api-client.ts`) throws
`Error("API request failed: <status> <statusText> - <body>")`, so the status is readable only in the message. Paths are under
`portal/src/pages/SecurityAnalysis/`.

1. **New file `notFound.ts`** exporting exactly:
   - `isNotFound(error: unknown): boolean`: true only when `error` is an `Error` whose message starts with `API request failed: 404`
     (followed by a word boundary). False for any other status, a network error, a non-Error and null.
   - `notFoundWords(text: string): string`: exactly `No security found for "<text>".` (straight double quotes, a full stop).
2. **`SecurityAnalysis.tsx`**: import both from `./notFound`. When a security is selected and the identity read's error
   `isNotFound`, draw ONE element carrying `data-slot="security-not-found"`, in place of the security overlay and the five tabs. It
   prints `notFoundWords(<the selected text>)` and keeps the page's existing way back to all names (the same action the overlay's
   "Back to all names" uses). Use the estate's state component (`PanelEmpty` from `@/ui/components/states`), not a new one. Every
   other error keeps today's card unchanged. Do not touch `LeadPanel.tsx`, `api-client.ts` or any tab.
3. **A test, new file `__tests__/notFound.test.tsx`, run with `bun test`.** Its test names contain `no security found`. It shows:
   - a 404 identity error draws `data-slot="security-not-found"` with `No security found for "Boeing".` and no "feed is down";
   - a 500 identity error does NOT draw that slot (today's error card stands).
   Render `SecurityAnalysis` with `renderToStaticMarkup`. Mock its data hooks with `bun:test`'s `mock.module`; no network.


## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY for existing files; keep each file's line endings exactly as you find them (read them first, for example
   `python -c "print(open(p,'rb').read().count(b'\r\n'))"`). A new file is written with the Write tool.
5. **If a bound harness check (battery29) is anchored on markup this cell changes,** re-anchor that ONE check onto the same fact as
   the page now states it, keep its claim, never drop it, and record each re-anchor (old -> new) in the instance. Only a harness
   named in `<paths>` may be edited; if the red harness is not named there, file a row and stop on that criterion.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/notFound.ts
portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx
portal/src/pages/SecurityAnalysis/__tests__/notFound.test.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~121/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/api/api-client.ts`, `hooks/useSecurityAnalysisState.ts`, `components/LeadPanel.tsx`,
`components/SecurityOverlay.tsx`, `portal/src/ui/components/states/PanelStates.tsx`, and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round57/checks/r57a.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzi-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round57/checks/r57a.cjs"; echo "exit=$?"</invocation><expect>A NAME NOT FOUND IS SAID AS NOT FOUND: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzi-1"><invocation>cd "$(git rev-parse --show-toplevel)"/portal &amp;&amp; bun test src/pages/SecurityAnalysis/__tests__/notFound.test.tsx -t "no security found"; echo "exit=$?"</invocation><expect>at least 2 pass and 0 fail -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzi-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~121/DSGN_AMGTV1.TO-AV-zzi-1.security-not-found.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), and only
when every criterion passes. Before you flip, also run `cd portal && node node_modules/typescript/bin/tsc -b --noEmit` (expect no output)
and record it in the instance; a red tsc is not a pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W121-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the exact diff, the output line of every criterion and of tsc, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** `ledger/ROUND_ANALYSIS.round56.md` ruling R1, half (b) (the honest not-found). Half (a) (Enter resolves a typed name
  "exactly as choosing it from the suggestions does") is NOT cut: the page has no suggestions list and no resolve call, and matching
  typed text against served names is a page-side lookup that C-PRESENTATION-ONLY forbids. It is routed back to 1.0.0_SA_CTO~DELL1 as
  a producer/contract question (the route's own resolution, `hooks/useSecurityAnalysisState.ts:45-51` comment).
- **Scope note:** a valid key whose identity read 404s would also read "No security found". The walk measured only unknown typed
  text answering 404.
- **Base:** portal 0008ddd3 (origin DEV HEAD at the cut). `__harness__/` is granted for a battery29 re-anchor only.

<status>pending</status>
<round>57</round>
<to_id>DSGN_AMGTV1.TO-AV-zzi-1</to_id>
<slot>~121</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
