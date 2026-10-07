# DSGN_AMGTV1 task order -- `AV-zy-1` -- BATCHED REPAIR: THE MODEL TAB HAS NO TEXT UNDER 11 PX, NO VENDOR SHORT-NAME LINE, AND ITS INPUT LEDGER READS IN PLAIN WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zy-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~108</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; two portal page files, rendered offline by the check.
comp-adversary: RUN by the issuer at the cut on portal DEV 8ddfe409 -- r47.cjs 1 of 4 (arm 1 FAIL: 34 rendered text-[10px] nodes; arm 2 FAIL: "Company short name" and "BOEING CO/THE" are printed; arm 3 FAIL: "inputs have run" and "this page has no name for" survive, no "Articles we collect", no "source not named"; PLANTED passes). 4 of 4 on scratch reference edits of the two files (the tree restored after, 0 changes).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zy-1` (round 47, decomposition v47; two list items batched, four small edits)

The CTO's round-47 list (`ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md`, items 1 and 2) names two repairs on the Model tab. Both are
presentation only: nothing is computed, converted or fetched.

**1. FWD-20: no text under 11 px** (`portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`, about line 547).
- The gap mark, `<sup data-model-gap-mark="" className={`ml-0.5 text-[10px] font-bold ...`}>`, is 10 px. The page contract's floor is 11 px.
- Change `text-[10px]` to `text-[11px]` on that element. Leave every other class on it as it is.
- If any other text size under 11 px exists in this file, raise it to 11 px as well and name it in your report.

**2. FWD-27: the vendor short-name line is removed** (`portal/src/pages/SecurityAnalysis/modelSheet.ts`, about line 173).
- The Model tab's foot prints "Company short name: BOEING CO/THE" beside the page's display name "The Boeing Co". A reader sees two names.
- Remove the `SHORT_NAME: 'Company short name',` entry from `V3_HEADER_LABELS`. The line is built by looping over that object's keys, so
  removing the key removes the line.
- Keep the other three entries (Country, Average daily value traded (three months), Market capitalisation) exactly as they are.

**3. FWD-27: the input ledger's count in plain words** (`tabs/ModelTab.tsx`, the `data-input-ledger-count` paragraph, about line 736).
- Today it reads "2 of 6 inputs have run."
- Make it read: `{counts.classes_with_a_run} of {counts.classes} kinds of input have been collected for this name.`
- Keep the numbers adjacent as "N of M" (another check reads "N of M").

**4. FWD-27: a source the page cannot name, in plain words** (`tabs/ModelTab.tsx`, `LEDGER_SOURCE_WORDS` and `ledgerSourceWords`, about lines 675-690).
- Today the News row reads "News: a source this page has no name for yet; last ran ...".
- The news class is served with the source string `harvested news (the overlay feed, gold article_security_mention)`. Add ONE entry to
  `LEDGER_SOURCE_WORDS` keyed by that exact string, with the words `Articles we collect`.
- Change the fallback in `ledgerSourceWords` from `'a source this page has no name for yet'` to `'source not named'`.
- Never print the served source string itself.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the two files above change (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep each file's line endings.
5. If a page harness in the battery asserts one of the old words ("Company short name", "inputs have run", "a source this page has no
   name for yet") or imports a name you removed, update ONLY that assertion's expected words, inside the harness file that asserts
   them, and name it in your report. That file is granted to you only for that line.
6. Do not edit `CardFooter.tsx`, `publisherNames.ts` or `WhatChangedPanel.tsx`: their similar phrases are not in this order.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~108/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zy-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round47/checks/r47/r47.cjs"; echo "exit=$?"</invocation><expect>THE MODEL TAB HAS NO SMALL TEXT, NO VENDOR SHORT NAME AND A PLAIN-WORDS LEDGER: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zy-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~108/DSGN_AMGTV1.TO-AV-zy-1.model-tab-text-floor-and-plain-foot.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W108-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** CTO countersign `ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md` @43d2e5eb3c, rulings 6 and 7, ROUND 47 items 1 and 2 (msg 30797).
- **Item 2's first read** (page or served): all three foot lines are page text. The served news source string carries storage words; named
  for AMGT_RESAPP in the round's close.
- **Item 3** (the instrument's FWD-18 clause) is cell `AV-zy-I`, NOT cut: it follows the PRD addendum. **Item 4** (FWD-21) is the issuer read
  `round47/FWD21_READ.md` @8a1ebcf475, 10 of 10 by hover.
- **Issued when** `prd-signoff status DSGN_AMGTV1` read ADMITTED on PRD v0.17 @8730d6c042 (LIMB 6; CTO msgs 30802 and 30806).

<status>complete</status>
<round>47</round>
<slot>~108</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
