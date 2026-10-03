# DSGN_AMGTV1 task order -- `AV-zh-1` -- EACH LEAD PANEL FACE READS ONE SERVED UNIVERSE, AND PRINTS NO MOVEMENT-BASIS SYSTEM WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zh-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~86</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render LeadPanel statically with React Query and the endpoints recorded.
comp-adversary: RUN by the issuer at the cut on portal e370eb7c (the CTO-approved round-29 candidate) -- universe.cjs 2 of 4, resolutionwords.cjs 2 of 3 (FAIL as expected; CONTROL and PLANTED arms pass by design).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zh-1` (round 30, decomposition v30; serves FWD-21/22 and FWD-27)

**Sources:**
- Row `AMGT_RESAPP-Z-W208-S1`, placed by the issuer (CTO msg 28772). `components/LeadPanel.tsx` holds three universes in one component:
  the price ranking (94 names), the collected chatter (95 covered names), and the trending CHATTER ranking (1 row). That last one is read
  ONLY to join starred tickers to security keys for the Chatter face (`LeadPanel.tsx` ~419-443: `useLeadPanelRankings(movement, subject)`
  runs on both faces, and `starredKeys` comes from `rankingQuery.data.rows`). RESAPP am-3 now serves `ticker` on every collected row,
  95 of 95 live.
- FWD-27 (CTO msg 28833, from CVO~Z v33): `LeadPanel.tsx:220` prints "Showing the {axis} list (movement is measured)." -- system wording.

Build (the checks grade exactly this):
1. **`hooks/useLeadPanelApi.ts`.** `useLeadPanelRankings` can be switched off, e.g. a third parameter `enabled = true` passed to
   `useQuery`'s `enabled`, or `skipToken`. The price read itself is unchanged.
2. **Chatter face.** No `getLeadPanelRankings` read of any subject and no rank-series read: disable the hook on Chatter, or call it only
   from a Price-only child. The face reads `getCollectedChatter`, and may read `getStarred`.
   `starredKeys` = the `security_key` of each collected row whose own `ticker` is a string in the starred tickers. "Starred only" passes
   exactly those rows to `ChatterBubbles`; "All names" passes all of them.
3. **Price face.** Reads only the PRICE ranking, plus `getStarred` if needed; no collected-chatter read. `PriceBars` still gets the price
   `rows` and `starredTickers`.
4. **Words (FWD-27).** Neither face shows "Showing the <words> list", "(movement is measured)", "(movement is not yet measured)" or "list (",
   in visible text or `title` attributes. The simplest fix stops rendering `<ResolutionNote>`; its export and `data-resolution` attributes
   may stay. The round-29 `data-price-window` caption already names the window.
5. **Imports.** LeadPanel imports only the EXISTING hook names. The battery's `leadPanelPattern.harness.cjs` stubs that module with a fixed
   set of five hooks, so a new hook name would be undefined there and break the battery.
6. **Effects.** No reads are issued from `useEffect`.

The FWD-26 30/90/365 presets are NOT this cell. They wait for RESAPP an-7 to serve `?days=`, and a later cell adds them on top of yours.

**Contracts:** C-PRESENTATION-ONLY. The page joins served fields only (`ticker`, `security_key`) and computes nothing. Design law: no system
words on the face.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~86/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round30/` and `round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zh-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round30/checks/universe/universe.cjs"; echo "exit=$?"</invocation><expect>EACH LEAD PANEL FACE READS ONE SERVED UNIVERSE: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zh-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round30/checks/universe/resolutionwords.cjs"; echo "exit=$?"</invocation><expect>THE LEAD PANEL PRINTS NO MOVEMENT-BASIS SYSTEM WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zh-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~86/DSGN_AMGTV1.TO-AV-zh-1.one-served-universe-per-face.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W86-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Not graded (L9 PNG read): how the starred Chatter bubbles look and the empty-state wording; whether the Price face reads
well without the resolution line. resolutionwords.cjs also grades ResolutionNote's fallback branch on a planted payload (live serves only
CROSSED). The FWD-26 presets cell will later add `days` to the same hook and LeadPanel; it is sequenced after this cell. A stale
`types.ts:207-215` comment ("ticker absent today") is not this cell's file.

<status>pending</status>
<round>30</round>
<slot>~86</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
