# DSGN_AMGTV1 task order -- `AV-zzi-2` -- DIRECT ACT: THE REPAIRS -- A PRICE LABEL WHOLE ON FOCUS, A SERVED REASON IN ONE DATE FORM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzi-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~122</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files and their tests, rendered offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) at the cut on DELL1, on portal DEV 0008ddd3 in a worker-shaped nested worktree -- r57b.cjs 1 of 4 (arms 1-3 FAIL: the keyed row takes no focus, no daysInWords, the raw reasons print; PLANTED passes); battery29 ALL PASS. On a scratch reference edit, r57b 4 of 4 and every battery29 harness green. The tree was not edited.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzi-2` (round 57, decomposition v57; repairs batched; serves FWD-27)

Two repairs on `/security-analysis`. Paths are under `portal/src/pages/SecurityAnalysis/`. Change nothing else.

1. **A Price label reads whole on focus** (`components/PriceBars.tsx`). The label span is cut at `w-36 ... truncate` ("Advanced Micro
   Devices ..."). The row's `title` already holds the full words (`hoverText`, label first), but a keyboard reader cannot reach them.
   On each `<li data-price-bar>` that has a `securityKey`, add:
   - `tabIndex={0}`, `role="button"`, `aria-label={bar.hover}` (the same words as the title);
   - an `onKeyDown` that selects the security on Enter or Space, exactly as the click does (and prevents Space from scrolling).
   A row without a `securityKey` gets none of these. The label span, its width and its truncation stay as they are.
2. **A served reason's days read in the house form.**
   - In `dateWords.ts`, export `daysInWords(text: string | null | undefined): string`. It returns `''` for null/undefined, and
     otherwise the text with every `YYYY-MM-DD` replaced by `longDate(day)` ("as of 2026-09-22." -> "as of September 22nd, 2026.").
     Other text is unchanged. This is the rule `components/SecurityOverlay.tsx:96` already applies inline; do not edit that file.
   - `components/model/WhatChangedPanel.tsx`: the compare-reason paragraph prints `daysInWords(compare.reason) || 'These two versions
     could not be compared just now.'`. Its `data-model-compare-reason` attribute keeps the raw served reason.
   - `tabs/ModelTab.tsx`: both no-figure reason forms print the reason through `daysInWords`:
     `` `Lines with no figure: ${daysInWords(reason)}` `` and `` `${daysInWords(reason)} Lines: ${labels.join(', ')}.` ``.
     `byReason` keys stay raw.


## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY for existing files; keep each file's line endings exactly as you find them (read them first, for example
   `python -c "print(open(p,'rb').read().count(b'\r\n'))"`). A new file is written with the Write tool.
5. **If a bound harness check (battery29) is anchored on markup this cell changes,** re-anchor that ONE check onto the same fact as
   the page now states it, keep its claim, never drop it, and record each re-anchor (old -> new) in the instance. Only a harness
   named in `<paths>` may be edited; if the red harness is not named there, file a row and stop on that criterion.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/PriceBars.tsx
portal/src/pages/SecurityAnalysis/dateWords.ts
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~122/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `components/SecurityOverlay.tsx` (the precedent at :96), and the issuer's check
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round57/checks/r57b.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzi-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round57/checks/r57b.cjs"; echo "exit=$?"</invocation><expect>THE REPAIRS: A PRICE LABEL READS WHOLE ON FOCUS, A SERVED REASON READS ONE DATE FORM: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzi-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~122/DSGN_AMGTV1.TO-AV-zzi-2.repairs-focus-and-reason-days.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), and only
when every criterion passes. Before you flip, also run `cd portal && node node_modules/typescript/bin/tsc -b --noEmit` (expect no output)
and record it in the instance; a red tsc is not a pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W122-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the exact diff, the output line of every criterion and of tsc, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** `ledger/ROUND_ANALYSIS.round56.md` R3 (dates on the Model card) and R5 (the two truncated Price labels), batched as
  repairs.
- **Not cut, with evidence (walk `tmp/ui-walk/20261009T032433Z`):**
  - R2 (money): the page has no "$" formatter (code map, 0008ddd3). The "$" is in quoted news HEADLINES ("Nvidia's $150B buyback...",
    "Trump's $5,000 Handout"), which must not be rewritten. The page's own money already reads one way ("USD 645.86").
  - R4 (contrast): the three samples are the HeroDialog header text on the dark navy band, measured by the walker against white.
    The screenshot shows them legible.
  - R5's "clipped element": an empty `tspan` in a chart SVG, 2 px; no reader text.
  - R6 (Chatter earlier months): the month cursor was removed on purpose (AV-zi-1) in favour of the 30D/90D/365D windows, which reach
    back a year. The walker's "Earlier month" control check expects the older design.
- **Base:** portal 0008ddd3.

<status>pending</status>
<round>57</round>
<to_id>DSGN_AMGTV1.TO-AV-zzi-2</to_id>
<slot>~122</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
