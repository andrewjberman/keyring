# DSGN_AMGTV1 task order -- `AV-zy-2` -- A NAME WITH NO STORED FIGURES SAYS SO ONCE, NOT ON SEVEN TILES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zy-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~109</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; one portal page file, rendered offline by the check.
comp-adversary: RUN by the issuer at the cut on portal DEV 8ddfe409 -- r47b.cjs 2 of 3 (arm 1 FAIL: 7 key-figure tiles drawn, 0 ALL_ABSENT elements, the reason printed 7 times; KEEP and PLANTED pass). 3 of 3 on a scratch reference edit of the one file, with r42.cjs still 5 of 5 (the tree restored after, 0 changes).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zy-2` (round 47, decomposition v47; one repair)

The CTO's round-47 item 5 (`ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md`, section CORRECTION): a name the firm does not cover
says so ONCE, in plain words, where its header figures would be, in place of seven tiles repeating one sentence.

**Today** (`portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx`, the `HeaderCards` component, about lines 131-160): for a
name with no stored company record, the producer serves all seven key figures with `value: null` and the SAME `reason`, for example
"We hold no stored company data for this name yet." The row draws seven tiles, and each one prints that sentence.

**Make it:**
- After `slots` is built and after the existing empty-state branch, add ONE branch: when NO slot has a resolved figure AND every
  slot's reason is the same string, do not draw the tiles. Draw one element with the attribute `data-key-figures-state="ALL_ABSENT"`
  whose text is that served reason, verbatim, once. Use black ink at the page's body size (`text-[14px] text-black`).
- Every other case is unchanged:
  - a row with at least one served figure keeps its tiles (served ones and reasoned ones);
  - a row whose reasons differ from each other keeps its reason tiles;
  - a row with neither a figure nor a reason keeps the existing empty state ("No key figures have been published for this name yet.").
- The rule reads the served shape only. Do not match on the sentence's words, and do not add any new sentence of your own.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the one file above changes (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep the file's line endings.
5. If a page harness in the battery asserts seven tiles for an all-absent row, update ONLY that assertion's expectation, inside the
   harness file that asserts it, and name it in your report. That file is granted to you only for that line.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~109/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zy-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round47/checks/r47b/r47b.cjs"; echo "exit=$?"</invocation><expect>A NAME WITH NO STORED FIGURES SAYS SO ONCE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zy-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round42/checks/r42/r42.cjs"; echo "exit=$?"</invocation><expect>THE HEADER SHOWS A MISSING FIGURE'S REASON, ITS TOOLTIP CARRIES THE FULL VALUE, THE EXEC EMPTY STATE READS PLAINLY: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zy-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~109/DSGN_AMGTV1.TO-AV-zy-2.no-stored-figures-says-so-once.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W109-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** CTO countersign `ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md` section CORRECTION @50e71b5b8d, item 5 (msg 30810).
- **Item 5's first read:** MSFT US draws 7 tiles with one sentence (walk `round35/walk/read-20261007T093016Z/17-fwd24-overlay-census-MSFT-US.json`).
  The served payload carries NO coverage marker; the page rule is keyed on the served shape. The marker is a producer item, named in the close.
- **Issued when** `prd-signoff status DSGN_AMGTV1` read ADMITTED on PRD v0.17 @8730d6c042.

<status>pending</status>
<round>47</round>
<slot>~109</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
