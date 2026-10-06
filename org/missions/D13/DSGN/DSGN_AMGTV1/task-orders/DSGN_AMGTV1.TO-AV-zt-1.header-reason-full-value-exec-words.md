# DSGN_AMGTV1 task order -- `AV-zt-1` -- BATCHED REPAIR: A MISSING HEADER FIGURE SHOWS ITS SERVED REASON; THE TOOLTIP CARRIES THE FULL VALUE; THE EXEC EMPTY STATE IN PLAIN WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~103</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; two portal page files, rendered offline by the check.
comp-adversary: RUN by the issuer at the cut on portal DEV e6ab82ad -- r42.cjs 2 of 5 (arm 1 FAIL: ROG SW-shaped bundle renders 3 tiles, none of the 4 served reasons; arm 2 FAIL: the tooltip lacks "USD 161,867,780,096" and "CHF 306,930.58319 million"; arm 3 FAIL: "yet:" survives and the message interpolates a reason; KEEP and PLANTED pass). 5 of 5 on scratch reference edits of the two files via CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zt-1` (round 42, decomposition v42; three repairs batched)

The CTO's round-42 list (`ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND41.md`, items 1-3) names three page repairs. All three are presentation
only: nothing is computed, converted or guessed beyond formatting a served number.

**1. FWD-4: a missing header figure shows the producer's served reason in its place** (`components/HeaderCards.tsx`).
- For each of the seven key figures with no stored value, the producer serves an entry in `bundle.header_figures` with `value: null`
  and `reason: "<one sentence>"`, for example "Bloomberg returned no value for price for this name in the latest stored pull."
- Short interest's reasoned entry is served under `SHORT_INT_RATIO`. The row's short-interest figure is `SI_PERCENT_EQUITY_FLOAT`, so
  treat either mnemonic as that figure.
- In the row, such a figure is a tile in its place, in the row's order. It shows:
  - the plain label;
  - the served reason verbatim, in small black ink;
  - `data-card-figure-state="ABSENT"`;
  - no number.
- A figure served as null with NO reason still prints nothing (FWD-27: an unconnected field prints no line).
- The empty state ("No key figures have been published for this name yet.") shows only when the row has neither a served figure nor a
  reasoned one.

**2. FWD-13: the tooltip carries the full-precision value, formatted** (`components/HeaderCards.tsx`, the tooltip rows).
- Add one tooltip row with the served value written out in full:
  - thousands separators;
  - the served currency code first for a money figure;
  - " million" after it when the served unit is MILLIONS;
  - the served decimals kept, except float noise: a number of 1,000 or more whose fractional part is under 0.001 prints as a whole
    number.
- Examples the check reads:
  - served 161867780096.00003, ABSOLUTE, USD: "USD 161,867,780,096";
  - served 306930.58319, MILLIONS, CHF: "CHF 306,930.58319 million";
  - served 193.56, USD: "USD 193.56".
- Keep `data-full-value` and `data-mnemonic` on the tooltip. Never show a vendor mnemonic in text.

**3. FWD-27: the Exec tab's empty state in plain words** (`tabs/ExecManagementTab.tsx`, `ManagementBody`, ~:256).
- Today it reads "No officer list has been published for this name yet:No officer list could be shown ... , and no other source was
  used." That has a missing space, a run-on and a repeated sentence.
- Make the message its own sentence ("No officer list has been published for this name yet."), and show the served reason
  (`dossierReasonWords(...)`, the chain the producer tried) as the state's detail. Drop the appended ", and no other source was used".
- Do not change the served words themselves.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the two files above change (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep each file's line endings.
5. If a page harness in the battery asserts the old Exec text, update ONLY that assertion's expected words, inside the harness file
   that asserts them, and name it in your report. That file is granted to you only for that line.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~103/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zt-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round42/checks/r42/r42.cjs"; echo "exit=$?"</invocation><expect>THE HEADER SHOWS A MISSING FIGURE'S REASON, ITS TOOLTIP CARRIES THE FULL VALUE, THE EXEC EMPTY STATE READS PLAINLY: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zt-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~103/DSGN_AMGTV1.TO-AV-zt-1.header-reason-full-value-exec-words.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W103-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** CTO countersign @f5d6919117, rulings 2, 3 and 6 and ROUND 42 items 1-3.
- **Item 4** (the no-permission read) is replaced by Andrew's word (record `ANDREW_DIRECT_20261005_163xZ_...`, CTO msgs 29703 and 29704)
  with ONE live read by the issuer: a non-Opal viewer sees no Security Analysis sidebar item. No cell is cut for it.
- **Parity hold** (MSTR~Z msg 29688): issued on branch `wk-DSGN_AMGTV1-r42-issue`; drains to CLOUD at PARITY CLOSED.

<status>complete</status>
<round>42</round>
<slot>~103</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
