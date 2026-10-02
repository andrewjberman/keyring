# DSGN_AMGTV1 task order -- `AV-zg-6` -- THE TABS READ IN PLAIN WORDS, PEERS MONEY READS ONE WAY, AND THE ACCOUNT MENU LETS GO

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zg-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~85</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render page sources statically from captured and planted fixtures and read App.tsx's source.
comp-adversary: RUN by the issuer at the cut on portal dcdc89b1 (= DEV ec65c5d6 for src/pages/SecurityAnalysis) -- tabwords.cjs 1 of 4, peersmenu.cjs 1 of 4 (FAIL as expected; PLANTED arms pass by design).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zg-6` (round 29, decomposition v29; serves FWD-27 on the tabs and the account menu)

PRD `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md` FWD-27 (lines ~387-402); register rows SAUX-30 (three of its strings), 31
("No profile (no match found)"), 32, 33/34 on Peers, and 35, in `docs/briefs/amgt-security-analysis-ui-findings-20261002.json`.

Build (the checks grade exactly this):
1. **`tabs/ExecManagementTab.tsx`**
   - **Order (SAUX-32):** row 1 is the officer whose `name` equals the served `management.ceo_public_profile.ceo_name`. Row 2 is the one
     officer whose served `role` contains "Chief Financial Officer". The rest follow in served order. Sorting by served fields is
     presentation (issuer ruling); nothing is computed.
   - **Row hook:** keep `data-exec-officer="<served name>"` on every officer row, and drop no officer.
   - **No-source lines (SAUX-31):** an officer that is not MATCHED or has no `profile_url` prints nothing in its profile cell. The
     rendered tab contains none of "no profile", "no match found", "not attempted" or "not found", not even inside a closed
     `<details>`. A MATCHED officer keeps `<a href="<served profile_url>">`.
   - **Source caption (CTO msg 28729, CVO~Z row Z-C-S41):** on the Bloomberg fallback roster, the management caption
     (~lines 279-280) appends ", the company's filing". It names ONLY the served source: a Bloomberg-fallback roster never says
     "filing", and a filing-sourced roster (the VLO control) keeps its filing wording. Graded at the L9 read.
   - **Pool line (SAUX-30):** no "in a union of" on the face. Use reader words, or put it in a closed `<details>`; the `<summary>`
     text counts as face text. Do NOT change the Exec subtitle, which `execText.harness.cjs` `subtitle_resolved_unchanged` pins.
2. **`tabs/ThesisTab.tsx`.** When the basis is ABSENT_ON_OBJECT, "held back uncited" is not on the face. Use reader words or a closed
   `<details>`.
3. **`components/ThesisDriverChart.tsx`.** The unresolved-passage branch prints no "no served drafted sentence carries" on the face. The best
   fix deletes the phrase from every string in the file. If it stays, it sits in a closed `<details>` whose open state starts as
   `useState(null)` or `useState(false)`.
4. **`tabs/PeersTab.tsx`**
   - **No `$` sign (SAUX-33)** anywhere on the tab.
   - **Keep the hooks:** `data-csc-table`, `th[data-csc-column-code="price|mkt_val_sec|ev"]` and `tr[data-csc-row="subject|member"]`.
     Cells run Name, Ticker, then the columns in `th` order.
   - **Subject currency:** the subject Price, EV and Mkt Cap cells show the served code, e.g. "USD 196.80"; the column head may carry it
     instead. Price and EV take it from the overlay `header_figures` PX_LAST and CURR_ENTP_VAL `.currency`. Mkt Cap takes it from
     `subject.cap_currency`, or `currency` if that is missing.
   - **Cap as-of (SAUX-34):** inside the subject Mkt Cap cell, a child `<span data-peers-cap-as-of="<subject.market_cap_vintage verbatim>">`
     prints the date through `longDate`, e.g. "as of September 19th, 2026". Put this hook on a span, NOT on the `td`: the battery's
     `peersPattern` `not_carried_em_dash` regex expects a `td` with only a class attribute.
   - **Types:** `types.ts` is owned by no cell this round; extend the row type locally for `market_cap_vintage` and `cap_currency`.
5. **`portal/src/App.tsx`, the account menu (SAUX-35).** Every page under `DashboardLayout` reads it: /market, /portfolios,
   /investor-reporting, /philosophy, /security-analysis, /positioning, /attribution, /factor-tilts, /valuations, /correlations, /macro,
   /advisor-intelligence, /security-scanner, /ticket-center, /portfolio-management, /trade-submission, /data-refresh and
   /dev/page-surface-control. It is not on /login and the password pages. Three InvestorReporting tests read `App.tsx`'s source
   (`fe-s-49`, `fe-s-88`, `fe-s-2`); keep what they read. The "Log Out" text stays in `App.tsx`. Use ONE of:
   - (a) A `keydown` listener (document or window, or `onKeyDown`) that checks `'Escape'` and calls `setShowUserMenu(false)`. Remove the
     `fixed inset-0` backdrop and close on an outside click with a document `pointerdown` listener instead, so a tab click still works
     while the menu is open.
   - (b) Headless UI `Menu` / `MenuButton` / `MenuItems` with `modal={false}` on `MenuItems`. No Dialog.
6. **Two battery harness clauses, amended to the new rule (issuer grant; precedent: round 15's harness grant).** These clauses pin the
   wording SAUX-30 and 31 remove. Change ONLY these two clauses and nothing else in either file:
   - `portal/src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs`, `absent_profile_cells` (~lines 223-241). It now asserts an
     unmatched officer's row keeps `data-exec-officer` and its profile cell prints none of "No profile (", "no match found" or "not
     found". The old form required an icon plus "No profile (".
   - `portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs`, `held_uncited_line_present` (~247-261). It now asserts the
     held-uncited sentence is NOT on the face at rest (absent, or inside a closed `<details>`). The old form required it word for word.
   Each amended clause must still FAIL on a planted page that breaks the new rule: show that in your report with one run on a planted
   input.

**Contracts:** C-PRESENTATION-ONLY. Design law: a code may sit in a data attribute, never in visible text.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; in the two harness files only the two named clauses change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/App.tsx
portal/src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~85/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zg-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/tabs/tabwords.cjs"; echo "exit=$?"</invocation><expect>THE EXEC AND THESIS TABS READ IN PLAIN WORDS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zg-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/tabs/peersmenu.cjs"; echo "exit=$?"</invocation><expect>PEERS MONEY READS ONE WAY WITH ITS DATE, AND THE ACCOUNT MENU LETS GO: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zg-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~85/DSGN_AMGTV1.TO-AV-zg-6.tabs-plain-words-and-account-menu.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W85-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, the two amended harness
clauses with their planted-failure runs, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Not graded by the checks** (L9 PNG read or live check): the order after rows 1-2; CEO-first when `ceo_name` is not served; whether
  the replacement wording reads plainly; whether the dated Peers cap reads as agreeing with the header; member price/EV currency; other
  Exec no-source lines ('not stated', "no public profile is on file yet", the "with tenure against the pool" subtitle); and the live
  menu behaviour (Escape with focus anywhere, a real tab click with the menu open, outside click, focus return).
- **Producer gap for the CTO at close:** R-1 serves no currency for a member's price or EV (only `cap_currency`); that is an AMGT_RESAPP
  ask. No filing-sourced driver chart has been served on a QA name, so that branch is planted.

<status>pending</status>
<round>29</round>
<slot>~85</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
