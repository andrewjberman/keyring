# DSGN_AMGTV1 task order -- `AV-t-1` -- THE LEAD-PANEL ROW LEADS WITH THE COMPANY NAME THE ROW CARRIES, OR ITS SERVED TICKER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut -- AC1 reads 1 of 4 arms at the base and 4 of 4 on a scratch reference implementation, so it discriminates both ways; AC2 reads 3 of 3 at the base (a bound). Blind spot, stated: static markup only; the look of the row is AC3's.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-t-1` (round 1, the thread's hops 2-3)

The page is Security Analysis (`/security-analysis`). A portfolio manager must pick **Valero** out of today's Trending x Price
list by its company name. Today every row leads with its ticker (`VLO US`), because the served rows carry no name.

Build, in `portal/src/pages/SecurityAnalysis/components/RankedList.tsx` (the list's ONE row renderer; `StarredList` composes it):

1. **Each row leads with the company name the ROW carries**: `row.name` when it is a non-empty string, else
   `row.classification.name` when that is a non-empty string. The row's served ticker (`row.ticker`) shows beside or under
   the name as a secondary label. A row carrying neither leads with its served ticker, exactly as today.
2. **The row states which**, as a data attribute on the row: `data-row-name-state="SERVED"` when a name leads,
   `data-row-name-state="NOT_SERVED"` when the ticker leads. The lead label sits in an element carrying `data-row-lead`;
   when a name leads, the ticker sits in an element carrying `data-row-ticker`.
3. **Type the two optional fields** on `RankingRowBase` in `portal/src/pages/SecurityAnalysis/types.ts`, as the ask will serve
   them: `name?: string | null` and `classification?: { name?: string | null; asset_class?: string | null;
   sub_asset_class?: string | null; sector?: string | null } | null`, each with a one-line comment saying the scoped API
   serves it once the owning team adds it, and that the page never derives it.

**The rule this cell must not break (the project's contract, C-PRESENTATION-ONLY):** the page derives nothing. It does not
look a name up, join it from another payload (the overlay's `NAME` is NOT used here), title-case it, or build it from the
ticker. It renders the field the row carries, or the ticker the row carries. The canonical key (`row.security_key`, e.g.
`VLO_US_Equity`) never prints on the face.

**Unchanged:** row order (producer order, no sort), the star toggle, the click (still sends `row.security_key`; a row with
none still does not navigate), the loading / read-failure / refused / ABSENT / EMPTY states, and every other file.

**Design law (portal `DESIGN.md`, binding):** this list renders inside the lead panel's dark band, so its ink stays the band
tokens it uses today (`--palette-white` for the lead, `--palette-mediumGray` for secondary). No translucent white, no new colour.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. Standing: REFUSE, do not rescue.
2. Only the two files in `<paths>` under `portal/` change. No other page, no shared component, no harness.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~1/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/components/StarredList.tsx`,
`portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/t-1.AC1.cjs"; echo "exit=$?"</invocation><expect>ROW NAME RENDER: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/bound.cjs" RANKEDLIST errorEmpty.harness.cjs:12 tabs.harness.cjs:20 join.harness.mjs; echo "exit=$?"</invocation><expect>RANKEDLIST BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-t-1" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on the served 2026-09-25 generation (32 rows, VLO US third) plus two arms that add the name the
ask will serve (`name`, and `classification.name`) and one that keeps the canonical key off the face. AC2 is the bound: the
three page harnesses that load this row and read green at the base stay green, with no fewer checks. AC3 is JUDGMENT, graded by
`3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: on the band, a PM reads each row's lead
label first and the ticker as secondary, and a ticker-led row reads as a ticker, not as a code dump (DESIGN.md C5, C6).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~1/DSGN_AMGTV1.TO-AV-t-1.the-row-leads-with-the-company-name.proof_of_spec.json`.
Report once: what changed and where, the AC1/AC2 output lines, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1 = THE THREAD (PRD v0.2 :159-176), CTO msg 26416. Base 8fa7abde: AC1 FAIL (1 of 4), AC2 PASS (3 of 3).
Scratch GREEN arm for AC1: 4 of 4. Hop 3 cannot pass FWD-1 until AMGT_RESAPP serves the name (C-ASKS row 1); this cell builds
its consumer. Worker class light: under 100 product lines.

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
