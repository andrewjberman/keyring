# DSGN_AMGTV1 task order -- `AV-zw-1` -- THE TOP OF THE PAGE SAYS WHAT THE COMPANY IS AND WHAT IS SAID TODAY; EACH INPUT SHOWS ITS SOURCE, LAST RUN AND RESULT; THE RE-RUN BUTTON IS GONE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~106</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; portal page files graded offline on fixtures the issuer captured from the deployed API.
comp-adversary: RUN by the issuer at the cut on portal DEV 34803ef6 -- r45.cjs 1 of 5 (arms 1-3 FAIL: no TopBand.tsx, no InputProvenance.tsx; arm 4 FAIL: nothing mounted, `useRequestRefresh` and `onRefresh` / `refreshPending` still present; PLANTED passes). 5 of 5 on scratch reference components via CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/wk-dsgn-amgtv1-106`. Its `portal/` is a nested checkout at portal DEV 34803ef6 on its own branch. Work and
commit only there. Start every shell call with `cd /c/tmp/wk-dsgn-amgtv1-106`: a call that starts elsewhere resolves
`git rev-parse --show-toplevel` to the base checkout.

## 1. THE CELL -- `AV-zw-1` (round 45, decomposition v45)

The deployed `/overlay` body (the one `useSecurityOverlay` already reads) now serves two blocks the Security Analysis page does not
draw. The page also still carries a re-run button that the product has retired. All work is under
`portal/src/pages/SecurityAnalysis/`.

**(a) The top band** -- a NEW `components/TopBand.tsx`.
- Served block: `top_band: {description_line, description_reason, day, items: [{title, url, publisher, published_utc, mentions}],
  items_reason, items_without_link, social}`.
  - BA: a `description_line`, `items: []`, and a plain `items_reason`.
  - MSFT: an empty `description_line` with a plain `description_reason`.
  - `social` is always the sentence "no social source is admitted yet".
- Export `TopBand: FC<{ band?: <that block> | null }>`:
  - **No block:** render nothing (null).
  - The root carries `data-top-band`.
  - **The company in one line:** an element carrying `data-top-band-description` holds `description_line`. When that is empty it
    holds `description_reason` instead. Never both, never an empty box.
  - **The day's items:** one element per served item, in the served order, each carrying `data-top-band-item`:
    - show the `title`, the `publisher`, the time it was published in words (`etStamp` from `../dateWords`), and how many times it
      was mentioned when `mentions` is a number;
    - an item WITH a `url` is an `<a>` whose `href` is exactly that url, with `target="_blank"` and `rel="noopener noreferrer"`;
    - an item with NO `url` is drawn the same way but is not a link.
  - Name the day the items are from in words above them (`longDate(day)`).
  - **No items:** an element carrying `data-top-band-items-reason` holds the served `items_reason`. Draw no item. When there ARE
    items, do not draw this element.
  - **Social:** an element carrying `data-top-band-social` holds the served `social` sentence. Never an empty box.

**(b) Where each input came from** -- a NEW `components/InputProvenance.tsx`.
- Served block: `input_provenance: [{input, source, last_run, outcome, reason}]`, four entries per name.
  - `last_run` is either a compact stamp such as `20261006T132334Z`, or the token `NEVER`.
  - `outcome` is `landed`, `never read` or `failed`.
- Export `InputProvenance: FC<{ entries?: <that array> | null }>`:
  - **No entries (undefined, null or empty):** render nothing (null).
  - The root carries `data-input-provenance`. Give it a small header in plain words, for example "Where this page's data comes from".
  - One element per entry, in served order, carrying `data-provenance-row`. Each row shows:
    - the served `source`, unchanged;
    - when it last ran, as a date in words (parse the compact stamp; "October 6th, 2026" style, with the time if you can keep it
      readable). The raw stamp is never printed;
    - whether it worked, in plain words: `landed` reads "Worked", `failed` reads "Failed" followed by the served `reason`;
    - a `never read` entry shows the served `reason` instead of a date. The raw token `NEVER` is never printed.
  - The word "landed" must not appear on the page. The served `reason` for a `landed` entry contains the raw stamp, so do not
    print that reason for a `landed` entry.

**(c) Mount both above the tabs** -- `SecurityAnalysis.tsx`.
- In Security mode only, directly under `<IdentityHeader ... />` and above `<TabNavigation`, render
  `<TopBand band={top?.top_band} />` and then `<InputProvenance entries={top?.input_provenance} />`, where `top` is
  `overlayQuery.data` read through the type in (e).
- Universe mode (the `<LeadPanel>` branch) draws neither.

**(d) Remove the re-run button.**
- `SecurityAnalysis.tsx`: remove the `useRequestRefresh` import and call, and the `onRefresh` and `refreshPending` props.
- `hooks/useLeadPanelApi.ts`: remove `useRequestRefresh` and its now-unused `requestRefresh` import.
- `components/SecurityOverlay.tsx`: remove the `onRefresh` and `refreshPending` props and the button that uses them (near lines 70,
  321 and 452), plus any import only that button used.
- `__harness__/posture.harness.cjs` passes those two props (near line 397); remove them there.
- Do NOT edit `portal/src/api/endpoints/amgt-lead-panel.ts`. Another lane is writing that file. Its `requestRefresh` function
  stays, unused.

**(e) Types** -- a NEW `topBandTypes.ts` beside `types.ts`.
- Declare the item, the band, the provenance entry, and `OverlayTopFields { top_band?: ...; input_provenance?: ... }`.
- Do NOT edit `types.ts`. A sibling cell is writing it. In `SecurityAnalysis.tsx` read the two blocks as
  `overlayQuery.data as (SecurityOverlayBundle & OverlayTopFields) | undefined`.

**The look.** The page's light card family, as `components/SegmentBreakdown.tsx` uses it: hairline border, white panel, navy ink,
Lato. Use only the design tokens already used in that file. No new colour. Plain words on the page; no internal names (identity,
security key, crosswalk, dossier, landed, input ledger).

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the paths below change. Presentation only: no served value is changed, computed or rewritten.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool for existing files; Write for the new files; keep line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TopBand.tsx
portal/src/pages/SecurityAnalysis/components/InputProvenance.tsx
portal/src/pages/SecurityAnalysis/topBandTypes.ts
portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~106/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zw-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round45/checks/r45/r45.cjs"; echo "exit=$?"</invocation><expect>THE TOP OF THE PAGE AND THE INPUT PROVENANCE ARE DRAWN; THE RE-RUN BUTTON IS GONE: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zw-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zw-1" judgment="true"/>
</proof_of_spec>

AC3 is the CTO's judgment on a render of the page, not a mechanical check. For it, write
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~106/RENDER_ZW1.md`: the rendered text of the top band and of
the provenance panel for BA and for MSFT, from the two fixtures in
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round45/fixtures/` (each file's `payload` is the served body).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~106/DSGN_AMGTV1.TO-AV-zw-1.top-band-input-provenance-no-rerun.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W106-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ) and
`disarm_owner` `2.0.0_SA_COO~D`.
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

## AMENDMENT 1 (2026-10-07, issuer) -- THE ONE-LINE DESCRIPTION LEADS THE PAGE

The order's first pass is built and committed on your portal branch (TopBand, InputProvenance, the mounts, the re-run button gone).
The reviewer read the page and ruled one change: the company's one-line description is the first thing a reader needs, so it moves
up into the name header. Everything else stays where it is.

1. **`components/TopBand.tsx`:** add a second export, `CompanyLine: FC<{ band?: <the same top_band block> | null }>`.
   - No block: render nothing (null).
   - Otherwise it renders the ONE element carrying `data-top-band-description`: the served `description_line`, or the served
     `description_reason` when the line is empty. It draws no news item and no social line.
   - Style it as body text in the name header: navy ink, the page's normal text size, no new colour.
2. **`TopBand` itself no longer draws the description.** Remove the `data-top-band-description` element from it. It keeps the day's
   items (or their reason) and the social line, exactly as built.
3. **`components/SecurityOverlay.tsx`:** in `IdentityHeader`, mount `<CompanyLine band={top?.top_band} />` directly under the
   identity card block (the element carrying `data-identity-card` and its row) and ABOVE `<HeaderCards bundle={bundle} />`, so it
   sits above the key figures and above `<TimelinePanel`. Read the block as `bundle as SecurityOverlayBundle & OverlayTopFields`
   (from `../topBandTypes`), as you did in `SecurityAnalysis.tsx`. Do not edit `types.ts`.
4. **`SecurityAnalysis.tsx`:** unchanged. It keeps `<TopBand>` and `<InputProvenance>` above the tabs and does not mount `CompanyLine`.
5. If a harness under `__harness__/` asserts the header's markup and your change moves it, re-anchor only that assertion and say which.

The check for this order was amended to this contract (same invocation, AC1). On your current commit it reads 2 of 5: arm 1
"does not export CompanyLine", arm 2 "TopBand still draws the description", arm 4 "SecurityOverlay.tsx does not mount <CompanyLine ...>".
AC1 and AC2 are unchanged in text and must both be green again. Update `RENDER_ZW1.md` to show the company line and the band as they
now render for BA and MSFT. Re-write your proof instance on the new commits, and flip `<status>` to `complete` again in that commit.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** AMGT_RESAPP `ROUND_ANALYSIS.round75.md` @326aea63b3 rulings 2-3 and its "DSGN round 45" line; `ROUND_ANALYSIS.round76.md`
  @c8bbeeac10 (az-2 deployed as OVpDhfwD) and ADDENDUM 1 item 4 @a7b2c3e0ba (CTO msg 30491: the /refresh control removed, PRD v0.41).
- **Fixtures:** `round45/fixtures/overlay.{BA,MSFT}_US_Equity.deployed-OVpDhfwD.json`, read-only invokes at the cut.
- **Items:** a scan of all 95 covered names at the cut found 0 serving a news item, so the item arm plants two and says so. RESAPP
  round 77 changes the news-day rule (round-76 ruling 5); the block's shape is expected to hold.
- **Disjoint from `AV-zw-2`:** that cell owns `types.ts`, `ThesisDriverChart.tsx`, `SegmentBreakdown.tsx`; hence `topBandTypes.ts`.
- **Collision notes honoured:** RESAPP ba-4 writes `api/endpoints/amgt-lead-panel.ts` and `pages/Freshness/` (COO~Z msg 30485).
- **Issued by hand, no loop.**

<status>complete</status>
<round>45</round>
<slot>~106</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**AMENDMENT 1 (issuer, 2026-10-07):** CTO render review `ledger/CTO_RENDER_REVIEW_ROUND45_0aa353a6.md` @e3d1e62b06 (msg 30533), re-opened for one change. No gate limb graded this modification.
<status>pending</status>
