# DSGN_AMGTV1 task order -- `AV-zza-1` -- THE MODEL TAB'S FOOT PRINTS MONEY IN THE PAGE'S ONE MONEY FORMAT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zza-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~111</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; one portal page file, rendered offline by the check.
comp-adversary: RUN by the issuer at the cut on portal 97598dc3 -- r49.cjs 2 of 3 (arm 1 FAIL: the foot reads "USD 152,320 million" and "USD 1,356,158,848", the header formatter gives "USD 152B" and "USD 1.36B"; KEEP and PLANTED pass). 3 of 3 on a scratch reference edit of the one file, with r47.cjs still 4 of 4 (the tree restored after, 0 changes).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zza-1` (round 49, decomposition v49; one repair)

The Model tab's foot line prints two money figures in two long forms: "Market capitalisation: USD 152,320 million" and "Average
daily value traded (three months): USD 1,356,158,848". The header of the same page prints market cap as "USD 152B". A reader sees
three money formats on one tab. Both foot figures are formatted by the page, so the page can print them in its one short form.

**The file:** `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`. **It uses CRLF line endings. Keep them.**

**Today** (function `v3FactValue`, about line 379): a numeric fact is written out with `toLocaleString`, " million" is appended when
the served unit starts with MILLIONS, and the currency code is put in front.

**Make it:**
- For a numeric fact, format the value with the page's shared formatter `formatStatValue` from `../components/StatTile` (the header
  uses the same function). Pass the format `'currency-millions'` when the served unit starts with MILLIONS (case-insensitive, as
  today), otherwise `'currency-abs'`; pass the fact's currency (or null) and the fact's unit.
- When `formatStatValue` returns a string, that string is the fact's value. Keep today's code only as the fallback for a null return.
- `ModelTab.tsx` already imports from `../components/StatTile`; add `formatStatValue` to that import.
- Do not change non-numeric facts (Country prints its served text), the labels, or the "not served" branch.
- Do not type a currency code, a magnitude letter or a number format of your own: the formatter decides all of them. A fact served
  with no currency must not gain one; the formatter already says "currency not stated" for it.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the one file above changes (plus your deliverables and the surprise channel).
3. The portal file commits inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep the file's CRLF line endings (count carriage-return bytes before and after).
5. If a page harness in the battery asserts one of the old long forms, update ONLY that assertion's expected words, inside the harness
   file that asserts them, and name it in your report. That file is granted to you only for that line.
6. Do not edit `components/StatTile.tsx` or `modelSheet.ts`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~111/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zza-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round49/checks/r49/r49.cjs"; echo "exit=$?"</invocation><expect>THE MODEL TAB'S FOOT PRINTS MONEY IN THE PAGE'S ONE MONEY FORMAT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zza-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round47/checks/r47/r47.cjs"; echo "exit=$?"</invocation><expect>THE MODEL TAB HAS NO SMALL TEXT, NO VENDOR SHORT NAME AND A PLAIN-WORDS LEDGER: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zza-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~111/DSGN_AMGTV1.TO-AV-zza-1.model-foot-one-money-format.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W111-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** CTO ruling msg 30869 on `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_AMGTV1_FWD20_CLAUSE_COUNT_AND_FWD27_REGRADE_20261007.md`
  @7ca923a956, FWD-27 ground 1. Grounds 2 (the country's capitals) and 3 (the Filings ledger row) are the producer's, routed by the CTO to
  `2.0.0_SA_COO~Z`.
- **The first read the CVO asked for:** both foot figures are page-formatted (`v3FactValue`); the What-changed row label in the vendor's
  words was not read in this round and is named in the close.
- **Base:** the worker's portal is at 97598dc3, so the candidate becomes 97598dc3 + 1 product commit; the CTO re-reviews that commit.
- **The round's second cell,** `AV-zza-2` (planted fail-and-clean pairs for the render check), is an issuer act with no order file.

<status>complete</status>
<round>49</round>
<slot>~111</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
