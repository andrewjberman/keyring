# DSGN_AMGTV1 task order -- `AV-zu-1` -- BATCHED REPAIR: NO BARE NUMBER AS A PEER TICKER; THE PLAIN NAME WHEREVER IT IS SERVED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zu-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~104</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; four portal page files, graded offline on fixtures the issuer captured from the deployed API.
comp-adversary: RUN by the issuer at the cut on portal DEV 4fa0312e -- r43.cjs 2 of 5 (arm 1 FAIL: 4 member rows show 688910 / 677172 / 677381 / 645026; arm 2 FAIL: the price face prints SYNOPSYS INC, ADOBE INC, CADENCE DESIGN SYS; arm 3 FAIL: RankedList, cscTable and postureCites read name before display_name; KEEP and PLANTED pass). 5 of 5 on scratch reference edits of the four files via CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zu-1` (round 43, decomposition v43; two repairs batched)

The deployed producer now serves what the page needs:
- per peer member, the plain `display_name` and, for a numeric exchange number in `ticker`, either `security_key` (the resolved
  security, e.g. `688910` -> `TSM_US_Equity`) or a plain `ticker_reason` ("This listing has only an exchange number; we have no
  company match for it yet.");
- per price-ranking row, `display_name` ("Synopsys Inc") beside the vendor `name` ("SYNOPSYS INC").

The page ignores both. Presentation only: read what is served and change no served value.

**1. FWD-8: no bare number as a peer ticker** (`src/pages/SecurityAnalysis/cscTable.ts`, `buildCscTable`'s member rows).
- When `member.ticker` is all digits:
  - with `member.security_key`: the ticker cell shows that key in house form (drop `_Equity`, underscores to spaces:
    `TSM_US_Equity` -> `TSM US`);
  - without it: the ticker cell shows the served `ticker_reason` verbatim.
- A letter ticker (GOOG, GOOGL, AAPL, ...) is unchanged.

**2. FWD-27: the plain name wherever it is served.** Read `display_name` first, then fall back to what is read today:
- `components/PriceBars.tsx` (~:191, the bar label);
- `components/RankedList.tsx` (`rowLeadName`, ~:131);
- `cscTable.ts` (~:184, the member label);
- `postureCites.ts` (~:298, the peer cite's name).
Officer names are people's names and stay as they are.

**3. AMENDMENT 1 (issuer, 2026-10-06 ~04:3xZ): the tabs harness clears the producer's cache between its scenarios**
(`src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs`, the Python adapter `PY`).
- On current CLOUD the producer caches the rankings pointer per (axis, date) for 60 s (`lib/research/api/scoped_amgt.py:456`,
  `served_cache`, RESAPP au-6).
- The adapter runs its "mismatch" and "control" scenarios in ONE process, so the control reuses the mismatch's pointer
  (row_count 10) and is refused SHORT_READ. `short_read_control_served` reads false WITHOUT your change (issuer-measured on the
  shared tree and on the adapter alone).
- Fix: in the adapter, import `served_cache` from `lib.research.api` and call `served_cache.clear()` at the top of each
  scenario (each loop pass and before the `series` read), so each scenario is a fresh read.
- Change nothing else in the harness, and no assertion.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the four files above and the tabs harness's adapter (item 3) change (plus your deliverables, the surprise channel, and `types.ts` ONLY to declare the optional
   served fields `display_name`, `security_key` and `ticker_reason` if TypeScript needs them).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep each file's line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/cscTable.ts
portal/src/pages/SecurityAnalysis/components/PriceBars.tsx
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~104/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zu-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round43/checks/r43/r43.cjs"; echo "exit=$?"</invocation><expect>NO BARE NUMBER AS A PEER TICKER; THE PLAIN NAME WHEREVER IT IS SERVED: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zu-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~104/DSGN_AMGTV1.TO-AV-zu-1.peer-ticker-and-plain-names.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W104-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **AMENDMENT 1 (~04:3xZ):** AC2 went red on `tabs.harness.cjs short_read_control_served`. It is green at base DEV 4fa0312e with the old
  outer and red on current CLOUD without any round-43 change. Cause: the au-6 `served_cache` pointer (60 s TTL) is shared across the
  adapter's two in-process scenarios. Granted the harness file plus a cache clear between scenarios. No gate limb graded the modification
  (to-pipeline-gate fires on new orders only). Production effect: a regenerated list within 60 s is refused SHORT_READ (designed
  state) until the TTL passes.
- **Source:** CTO countersign + list @0bcdb77515 (msg 29884): FWD-8 and FWD-27 NOT_REALIZED page-side.
- **Census:** `deliverables/2.0.0_SA_COO~D/round42/fwd8-27-census/` @662434b2cf.
- **Fixtures:** `round43/fixtures/*.deployed-2lUlZomo.json`.
- **Issued by hand, no loop** (Andrew ~21:4xZ "Yes stop the loop"; the CTO: "do not re-arm it").
- **Proof at close:** a render on the deployed payload (AC1) plus a :5174 walk by the issuer. The DEV push and PROD are each Andrew's
  word.

<status>pending</status>
<round>43</round>
<slot>~104</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
