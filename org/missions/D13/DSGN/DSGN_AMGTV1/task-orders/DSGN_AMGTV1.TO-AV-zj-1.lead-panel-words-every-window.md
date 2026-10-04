# DSGN_AMGTV1 task order -- `AV-zj-1` -- THE LEAD PANEL SPEAKS ONE DATE FORMAT AND NO SYSTEM WORDS AT EVERY WINDOW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~90</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from fixtures captured on the deployed route.
comp-adversary: RUN by the issuer at the cut on portal 76a15c1b (the CTO-approved round-31 candidate) -- words32.cjs 1 of 4 (arms 1-3 FAIL as expected; its four KEEP checks exit 0 there; PLANTED passes by design).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zj-1` (round 32, decomposition v32; a batched repair, DIRECT ACT; serves FWD-27 on FWD-26's faces)

The Lead Panel now has 30D / 90D / 365D presets on its Chatter and Price faces. The round-31 close walk read four wording faults.
Repair them in `portal/src/pages/SecurityAnalysis/components/`:
1. **The Chatter footer prints its date in words.**
   - In `LeadPanel.tsx`, the `[data-chatter-footer]` line reads "Articles collected, from the harvest. As of {chatterData.as_of}."
     That prints "2026-10-02".
   - Print `longDate(chatterData.as_of)` from `../dateWords` instead ("October 2nd, 2026"). Keep the raw value on the element's
     `data-chatter-as-of` attribute.
2. **An unserved Price window draws no source line.**
   - At 90D and 365D the price route serves no list (0 rows, `ranking_status` "ABSENT", a `window_reason`). The face prints that
     reason correctly.
   - Under the reason, the footer still draws `SourceCaption`: "Source: ranking details are not carried on this payload", plus a
     Details line repeating it.
   - When the served list is empty and a `window_reason` is served, draw no `SourceCaption` and no `[data-source-caption]` element.
   - Optional, in `GenerationCaption.tsx`: the "... not carried on this payload" wording may become reader words. "payload" must
     not print anywhere on the Lead Panel.
3. **"this period" becomes "in this window".** In `ChatterBubbles.tsx` the count line reads "<k> of <n> covered names have
   collected articles this period". Make it "... in this window" when the face shows a window. Month mode, for a caller that hands
   `month`, may keep its own wording.
4. **The stale comment goes.** `LeadPanel.tsx`'s header comment says the controls are `Segmented`, `ground="band"`, but no control
   passes a ground. Correct the comment so the text `ground="band"` appears nowhere in the file. No code change.

Served prose stays as served (C-PRESENTATION-ONLY). A bubble hover's served `places_moved_reason` may carry a served date; leave it.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep each file's
   existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~90/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository. In particular, the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round32/`, `round31/`, `round30/` and `round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zj-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round32/checks/repairs/words32.cjs"; echo "exit=$?"</invocation><expect>ONE DATE FORMAT, NO SYSTEM WORDS, AT EVERY WINDOW: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zj-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1's arm 3 also runs four checks, and needs each to exit 0: the round-31 `presets.cjs` and `windowread.cjs`, the round-29
`leadface.cjs`, and the round-30 `resolutionwords.cjs`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~90/DSGN_AMGTV1.TO-AV-zj-1.lead-panel-words-every-window.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W90-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Not graded** (the close's real run): how the 90D/365D Price face reads with the source line gone; the footer's date in place.
- **Not cut:** printing the served `window_note` (CTO note, msg 28898): it carries ISO dates. The composed "since <date>" says the
  same thing in words.
- **Direct act** (/dispatch Step 2): one small LOCAL cell; no L8-L10; the close is the issuer's one real run.

<status>complete</status>
<round>32</round>
<slot>~90</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
