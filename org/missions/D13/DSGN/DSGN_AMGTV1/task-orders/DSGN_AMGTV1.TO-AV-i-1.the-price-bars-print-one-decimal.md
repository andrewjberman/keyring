# DSGN_AMGTV1 task order -- `AV-i-1` -- THE PRICE BARS PRINT ONE DECIMAL, THE WHOLE SERVED VALUE IN data-price-value

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-i-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~64</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV c6aacc68 -- precision.cjs 2 of 3 (FAIL as expected: 128 faults, every bar prints the full float, e.g. "-25.0123456789012%", no data-price-value; arm 2 the pinned base source and arm 3 four planted mutants PASS by design). Blind spot: the clip is graded by a token-length proxy; the issuer's live walk PNG is the real read.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-i-1` (round 18, decomposition v18; serves FWD-22)

DIRECT ACT. The CTO's ruling msg 27760 = CONTRACT amendment 3 @b9d096f6dd ("the bars print *_pct to ONE decimal with sign and '%', and
the whole served value stays in a data attribute on the bar (e.g. data-price-value). Rounding never rescales."). The acceptance walk
(20261001T101104Z) printed "-25.40217088783747%" and the value column clipped at the panel edge. In `portal/src/pages/SecurityAnalysis/components/PriceBars.tsx`:
each bar prints its served `return_30d_pct` with an explicit sign, ONE decimal (`toFixed(1)`) and "%"; the bar element (the one carrying
`data-price-bar`) also carries `data-price-value` = the whole served number, unrounded; the value column fits inside the panel (no clip,
no truncation of the value). Order, colours, names and everything else unchanged. Do not run the walker.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes:** none. No harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/PriceBars.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~64/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-i-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round18/checks/precision.cjs"; echo "exit=$?"</invocation><expect>THE PRICE BARS PRINT ONE DECIMAL: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-i-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/pricebars.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bubbles.cjs"; echo "exit=$?"</invocation><expect>PRICE IS RANKED BARS, ONE FORM: 3 of 3 arms, then CHATTER IS BUBBLES BY MONTH: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-i-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" I1 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>I1 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders LeadPanel on Price with live-like float values: one decimal printed, the whole value in data-price-value, no long token,
the |value| order kept; arm 2 the base source lacks it; arm 3 planted mutants. Seconds. AC2 keeps round 15's bars and bubbles. AC3 the
harness bound. The real run is the issuer's live walk (the price PNG read for clipping).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~64/DSGN_AMGTV1.TO-AV-i-1.the-price-bars-print-one-decimal.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (one file, LOCAL). CTO ruling 27760 / CONTRACT amendment 3. Base precision 2 of 3 on DEV c6aacc68.

<status>complete</status>
<round>18</round>
<slot>~64</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
