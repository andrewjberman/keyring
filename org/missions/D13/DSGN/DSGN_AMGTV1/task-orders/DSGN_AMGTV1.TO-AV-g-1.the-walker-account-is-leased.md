# DSGN_AMGTV1 task order -- `AV-g-1` -- THE WALKER ACCOUNT IS LEASED, AND THE WALKER WALKS THE FRIDAY FACES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-g-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~59</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut -- walkerlease.py 1 of 3 (FAIL as expected: arm 1 0 of 6 -- no DynamoDB lease before SSM, no HELD refusal, no holder on disarm; arm 3 vacuous on the base module) and walksteps.cjs 2 of 3 (arm 1 FAIL: 7 faults -- the walk still names List view / Chart view / Breakout, never reads data-price-bar or the bubbles, never presses the cursor, threads by data-row-lead); green arm (scratch r16-green-f @49bf677ac4, an issuer-spawned helper) walkerlease 3 of 3, py_compile and node --check OK. Blind spots: the lease protects only seats running the new code (the laptop runs its own copy until it pulls CLOUD); the CLI path of `disarm <holder>` and the walker steps are static reads; no live AWS.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-g-1` (round 16, decomposition v16; serves FWD-20, FWD-1)

The CTO's round-15 analysis @68e34e1e97 s.4 row 1 and ruling 1 (row DSGN_AMGTV1-Z-S10: a laptop seat shares the one walker account;
its end-of-walk disarm killed this seat's walk). Build in `.claude/skills/ui-walk/`:
1. **`ui_walker_account.py` -- the lease:** `arm` first writes ONE conditional DynamoDB UpdateItem on the walker's row that sets
   `armedBy` (a holder id unique per walk: `<hostname>:<pid>:<8 hex>`) and `armedAt`, conditional on the row carrying no live lease
   (`attribute_not_exists(armedAt) OR armedAt < <now - 60 minutes>`), and only THEN mints the SSM password; a lost condition prints
   `HELD by <armedBy> since <armedAt>` and mints nothing (it never steals a live lease). `arm` prints `HOLDER <id>`. `disarm <holder>`
   runs only for that holder: its UpdateItem is conditional on `armedBy = <holder>`, removes armedBy/armedAt with the disable, then
   deletes the SSM parameter; a non-holder disarm refuses and changes nothing. `status` prints armedBy/armedAt.
2. **`walk.mjs`:** passes the holder id from its arm to its finally-disarm. Its lead-panel walk steps the Friday faces (rulings R5/R6
   -- Trending only, no List/Chart, chatter = bubbles, price = bars): it steps 'Chatter' and 'Price', reads the price bars by
   `data-price-bar` (into lead-lists.json), reads the bubbles and presses the month cursor ('Earlier month'), and finds a name for
   the thread by its price bar (not `data-row-lead`). Update `SKILL.md`'s usage lines to match.
**Walker rule (CTO msg 27641):** do NOT run `.claude/skills/ui-walk/walk.mjs` or `ui_walker_account.py arm|disarm|secret` -- the one walker account is shared across two devices; no criterion here needs a walk.

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
.claude/skills/ui-walk/ui_walker_account.py
.claude/skills/ui-walk/walk.mjs
.claude/skills/ui-walk/SKILL.md
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~59/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-g-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/walkerlease.py"; echo "exit=$?"</invocation><expect>THE WALKER ACCOUNT IS LEASED: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-g-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/walksteps.cjs"; echo "exit=$?"</invocation><expect>THE WALKER WALKS THE FRIDAY FACES: 3 of 3 arms -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 loads the checkout's `ui_walker_account.py` with a stubbed boto3 (a fake DynamoDB that evaluates condition and update expressions,
a fake SSM; every web request 401) and grades arm on a free row (one conditional UpdateItem with armedBy/armedAt BEFORE any SSM write),
arm on a live lease (HELD, no SSM call), arm on a stale lease (taken), disarm by the holder (conditional, then DeleteParameter), disarm by
a non-holder (refused, no DeleteParameter), and walk.mjs passing the holder id from arm to disarm; arm 2 the base files fail; arm 3 two
planted mutants. No live AWS. AC2 a static read of walk.mjs (node --check + the Friday faces). The real run is the issuer's next close
walk with the new code.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~59/DSGN_AMGTV1.TO-AV-g-1.the-walker-account-is-leased.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** analysis s.4 row 1 (ruling 1). Chain ~59 leads (g-1 -> g-5; file-disjoint, g-5 queued here for throughput). The walker-steps item is the issuer's addition (round-15 close walk 20261001T073050Z: walker:control-missing x4). Base 1 of 3 / 2 of 3; green r16-green-f @49bf677ac4 3 of 3.

<status>complete</status>
<round>16</round>
<slot>~59</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
