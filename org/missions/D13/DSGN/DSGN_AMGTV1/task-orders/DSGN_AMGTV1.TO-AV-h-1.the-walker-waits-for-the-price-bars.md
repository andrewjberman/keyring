# DSGN_AMGTV1 task order -- `AV-h-1` -- THE WALKER WAITS FOR THE PRICE BARS AND FLAGS A RAW-KEY BUBBLE LABEL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-h-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~62</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut -- pricewait.cjs 2 of 3 (FAIL as expected: the walk never waits for [data-price-bar]; no raw-key label flag); walksteps.cjs 3 of 3 at base (keep it). No green arm: a one-file walker change. Blind spot: a static read; the issuer's live close walk is the real run.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-h-1` (round 17, decomposition v17; serves FWD-22, FWD-21, FWD-20)

DIRECT ACT. The CTO's round-16 analysis @ce875b7bc1 section 3 row 1, rulings 1 and 3 (walk 20261001T090446Z settled 1.5 s after the
Price click and read 0 bars while the price route answered 200). Build in `.claude/skills/ui-walk/walk.mjs` only:
1. **The Price step waits** for `[data-price-bar]` (e.g. `await page.locator('[data-price-bar]').first().waitFor({ timeout: 30000 })`,
   or a `PRICE_WAIT_MS = 30000` constant passed to the wait) BEFORE it reads the bars into lead-lists.json and before the Price
   screenshot; it records how long the wait took in lead-lists.json. A wait that ends with no bar pushes ONE finding with a check
   name such as `price:no-bars-after-wait` carrying the wait time, and then also saves the price face's DOM text and the response
   body of the last `lead-panel/rankings/trending/price` request (from the walk's own network log) into the walk's OUT folder --
   never silent.
2. **The Chatter step flags a raw-key label:** for each sized bubble, if its visible label equals its `data-bubble` key (e.g.
   "BA_US_Equity"), push ONE finding with a check name such as `chatter:raw-key-label` carrying the count.
**Walker rule:** do NOT run `.claude/skills/ui-walk/walk.mjs` or `ui_walker_account.py arm|disarm|secret` -- the issuer runs the live walk at close (one device at a time, posted to 0.0.0_AB_MSTR~Z).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes:** none (no portal file is in this order).

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
.claude/skills/ui-walk/walk.mjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~62/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round17/checks/pricewait.cjs"; echo "exit=$?"</invocation><expect>THE WALKER WAITS FOR THE PRICE BARS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/walksteps.cjs"; echo "exit=$?"</invocation><expect>THE WALKER WALKS THE FRIDAY FACES: 3 of 3 arms -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 a static read of walk.mjs: a wait for [data-price-bar] of at least 30000 ms before the Price read and shot, a recorded no-bars
finding, a raw-key label finding; arm 2 the base walker (e41e28e641) fails; arm 3 a 1500 ms mutant is rejected. AC2 keeps round 16's
Friday-face steps. The real run is the issuer's live close walk, which proves the price face or root-causes it the same round.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~62/DSGN_AMGTV1.TO-AV-h-1.the-walker-waits-for-the-price-bars.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (one cell, ~30 lines, LOCAL). round-16 analysis s.3 row 1 (build half; the walk is the issuer's close act). Base pricewait 2 of 3.

<status>pending</status>
<round>17</round>
<slot>~62</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
