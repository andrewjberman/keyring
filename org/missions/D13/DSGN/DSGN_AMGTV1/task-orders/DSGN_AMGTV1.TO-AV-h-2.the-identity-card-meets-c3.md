# DSGN_AMGTV1 task order -- `AV-h-2` -- THE IDENTITY CARD'S NAME MEETS C3 ON A SOLID NAVY PANEL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-h-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~63</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the round-16 close on DEV 03311745 -- headerchrome.cjs 2 of 3 (arm 1 FAILS only on lowContrastChars 5 in each of the five Security states: the identity card's "BA US" on a navy panel with no solid background; sizes and the four-card layout PASS). Blind spot: contrast by the instrument's own rule.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-h-2` (round 17, decomposition v17; serves FWD-23, FWD-20)

DIRECT ACT. The CTO's round-16 analysis section 3 row 2 (ruling 2). In `portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx`, the identity card
(`IdentityHeader`'s `GraphicCard`, ~line 342) gets the same solid navy panel background the header cards carry
(`HeaderCards.tsx`'s `HEADER_PANEL`: `bg-[hsl(224_58%_20%)]` under the image), so the name's contrast grades against navy, never the
card's white root. Change only that panel's classes; never `GraphicCard.tsx` (/philosophy stays byte-identical). **Walker rule:** do NOT run `.claude/skills/ui-walk/walk.mjs` or `ui_walker_account.py arm|disarm|secret` -- the issuer runs the live walk at close (one device at a time, posted to 0.0.0_AB_MSTR~Z).

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
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~63/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/headerchrome.cjs"; echo "exit=$?"</invocation><expect>THE HEADER CHROME MEETS C1 AND C3: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/nolabel.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/headerread.cjs"; echo "exit=$?"</invocation><expect>NO INTERNAL NAME, THE NAME HEADER IN THE CARD FAMILY: 3 of 3 arms, then THE HEADER READS ITS NUMBERS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" H2 shell.harness.cjs:10 errorEmpty.harness.cjs:12 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>H2 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 builds and renders the page (about 10 minutes): sizes and lowContrastChars PASS in all six states (the five Security states read 5
low-contrast characters today), four equal header cards; /philosophy byte-identical. AC2 keeps the identity card in the card family and
the header readings. AC3 the harness bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~63/DSGN_AMGTV1.TO-AV-h-2.the-identity-card-meets-c3.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (one line, LOCAL). round-16 analysis s.3 row 2. Base headerchrome 2 of 3 (the close re-run 09:22Z).

<status>complete</status>
<round>17</round>
<slot>~63</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
