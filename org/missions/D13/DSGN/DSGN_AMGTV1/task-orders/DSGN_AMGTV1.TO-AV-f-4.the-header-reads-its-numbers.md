# DSGN_AMGTV1 task order -- `AV-f-4` -- THE SELECTED-NAME HEADER READS ITS SERVED NUMBERS, AND NO INTERFACE CODE REACHES A FACE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-f-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~58</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV a41cf763 -- headerread.cjs 2 of 3 (FAIL as expected: 15 faults -- "Breakout (price)" reads the Trending value, places moved not printed, "today" wording, no served day in words, the M-1 code on 6501's Exec; arm 2 the negative on b336b141 and arm 3 the planted faces PASS by design); green arm (scratch r15-green-c @993d933c, renamed by the issuer to the af-2 served names) 3 of 3, tsc -b rc=0, round-14 reasonwords and execfooter 3 of 3. Blind spots: places moved checks the number, not its direction word; only long-form dates are graded.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-f-4` (round 15, decomposition v15; serves FWD-24, FWD-11)

The CTO's round-14 analysis s.3 row 4 (PRD v0.6 FWD-24; CONTRACT s.2-4) with row DSGN_AMGTV1-Z-S9 (a repair, batched here). The
served field names are AMGT_RESAPP af-2's (its COO's msg 27543), typed at DEV a41cf763: per overlay axis read `as_of_date`,
`requested_as_of`, `dated`, `stale_trading_days`, `absent_reason`; `places_moved` on a served row; the BREAKOUT/PRICE row is the top-level
`breakout_price` (and the BREAKOUT/PRICE axis read), its jump `pct_jump_pct` in percent; `price` stays the TRENDING row. Build in `portal/src/pages/SecurityAnalysis/`:
1. **`components/SecurityOverlay.tsx` (the selected-name header):** the readings print the served `as_of_date` in words ("Readings of
   September 30th, 2026"), never "today" and never a date the page built; the cell labelled "Breakout (price)" reads the BREAKOUT/PRICE
   row (rank and `pct_jump_pct` as served with sign and "%", never x100), not the Trending value; `places_moved` prints where served
   ("up 3 places"); a reading the payload truly lacks renders a designed empty sentence carrying the served `absent_reason` in plain
   words; the words "not served", "unsupported", "ABSENT", "REFUSED" never reach the face for a field the payload carries. The axis
   footnote element carries `data-axis-footnote`.
2. **`reasonWords.ts` (row Z-S9):** the shared reason mapping drops an interface code of the shape letter(s)-dash-digit(s) (e.g. "M-1")
   from visible words while the served reason stays whole in its data attribute; keep the noun after it ("management object") so the
   round-14 execfooter check still reads its words.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Granted harness change (exact, tested on the green arm):** `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/fixtures/r15c.grant.shell.harness.diff` -- `axis_footnote` counts the
footnote ELEMENT by `data-axis-footnote=` instead of the "On today's rankings:" wording. Apply with `git -C portal apply`. No other harness
may change.

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
portal/src/pages/SecurityAnalysis/reasonWords.ts
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~58/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-f-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/headerread.cjs"; echo "exit=$?"</invocation><expect>THE HEADER READS ITS NUMBERS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-f-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" F4 shell.harness.cjs:10 drafting.harness.cjs:8 execFallback.harness.cjs execPattern.harness.cjs:9 execText.harness.cjs errorEmpty.harness.cjs:12 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>F4 BOUND: 7 of 7 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-f-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/reasonwords.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/execfooter.cjs"; echo "exit=$?"</invocation><expect>SERVED REASONS READ AS WORDS: 3 of 3 arms, then the execfooter line 3 of 3 arms -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders the selected-name header on the r15c overlays of BA, VLO and 6501 (axis reads dated 2026-09-30, distinct Trending vs
Breakout values, served places moved, one truly absent reading as the positive control) and 6501's Exec on the live /thesis capture with
"no M-1 management object has landed for this name"; arms 2-3 the negative and the planted faces. About 1 second. AC2 the bound on every
harness that loads the header, the reason mapping or Exec. AC3 keeps round 14's reason-word and Exec checks green (report both lines;
they live under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/`). Run `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs` too and report its line. No judgment criterion: the close walk reads the header
on 3 names.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~58/DSGN_AMGTV1.TO-AV-f-4.the-header-reads-its-numbers.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** analysis s.3 row 4 + row Z-S9 (repairs batched into one cell). Leads chain ~58 (f-4 -> f-5; both may write reasonWords.ts). Base: headerread 2 of 3; green 3 of 3. Field names per AMGT_RESAPP af-2 (COO~Z 27543); fixtures renamed by the issuer.

<status>pending</status>
<round>15</round>
<slot>~58</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
