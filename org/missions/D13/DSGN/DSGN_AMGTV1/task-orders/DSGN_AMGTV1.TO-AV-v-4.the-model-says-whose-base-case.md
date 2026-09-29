# DSGN_AMGTV1 task order -- `AV-v-4` -- THE MODEL FACE SAYS WHOSE BASE CASE EACH IS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-v-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~20</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 09bd04b1 -- modelwords.cjs 1 of 3 (FAIL as expected: an unlabelled rule case prints a bare "Base case: 159.61 EUR"; the tile reads "Forecast divergence score"); green arm 3 of 3; bound 2 of 2 (PASS); vv-5.AC1 YES (PASS). Blind spot: static markup with the estate chrome stubbed.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-v-4` (round 5, decomposition v5; serves FWD-6, FWD-11)

The CTO's ruling (round-4 analysis, ruling 2): on the Model face, "The research team's Base case is not served on this page yet"
and "Base case: 159.61 EUR (adjusted consensus EPS x trailing-median P/E)" are both true but read as a contradiction; each line
must name whose case it is. And ruling 1: the divergence score tile reads "Divergence from consensus forecast".

In `tabs/ModelTab.tsx`:
1. `ModelCaseLine`'s head is the served `label` when the case carries one (today's served payloads label the rule's base case
   "Historical-multiple reference" -- print a served label AS SERVED) and otherwise `${name} case`. Build: when no label is served,
   the rule's Base case reads "Opal's rule-based Base case" (e.g. "Opal's rule-based Base case: 159.61 EUR (...)" / "Opal's
   rule-based Base case: not in the pack yet -- ..."). The research team's own lines already read "The research team's Base case
   ..." -- keep them. After this, every visible "Base case" on the face is preceded by "research team's " or "Opal's rule-based ".
2. The divergence tile (`ScoreTile id="divergence"`) label reads "Divergence from consensus forecast" (the producer's own
   definition: model NTM free cash flow against consensus, `lib/research/scores/divergence.py:1-8`). The other tiles are unchanged.
The served state, value, formula and reason still ride the case element's attributes (`data-model-case`, `data-model-case-status`,
`data-model-case-formula`, `data-model-case-reason`).

FWD-30's page/export parity harness (`__harness__/exportCompare.harness.cjs`, graded by AC3) rebuilds each page case line as
"<head>: <STATUS> -- <detail>" from the page's text and compares it with the export's line, whose head stays "Base case". If
AC3 goes red because the page head now says "Opal's rule-based Base case", re-anchor `pageCases` to take the head from the
element's own served identity (`data-model-case` -> "<Name> case", or the served label) -- never weaken a set comparison.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound harness check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged. This slot's
   next orders also edit `ModelTab.tsx` (the served words; the panel-header date): change only the case head and the tile label.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~20/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/` (never edit them).
Also read-only: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh` (AC3's check).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-v-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/modelwords.cjs"; echo "exit=$?"</invocation><expect>WHOSE BASE CASE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-v-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/bound.cjs" V4 modelPattern.harness.cjs:12 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>V4 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-v-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh"; echo "exit=$?"</invocation><expect>FWD-30 HARNESS READS THE REDESIGNED PAGE: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-v-4" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour (a served-label payload and the same payload without the label, the shape the round-4 walk read); AC2 the bound; AC3 (the one further criterion this cell needs) the page/export parity, which reads the case heads this cell rewrites. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: the Model face never shows two Base cases without saying whose each is, and the divergence tile says what it diverges from (FWD-6, FWD-11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~20/DSGN_AMGTV1.TO-AV-v-4.the-model-says-whose-base-case.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 5 = the round-4 analysis's enrichment list @177c576c80 section 4 item 4 + rulings 1 and 2. Decomposition v5.
Slot ~20 queue: AV-v-4 -> AV-v-7 -> AV-v-6 (all three write `ModelTab.tsx`). Base 09bd04b1: modelwords.cjs 1 of 3 (arm 3, the
served-label floor, passes); green arm (scratch fallback head + tile label) 3 of 3; V4 bound 2 of 2; vv-5.AC1 YES. MEASURED at the
cut: every captured fixture's rule case carries the served label "Historical-multiple reference" (AMGT-vv-1), the current AMD
capture @8f50bcb837 included; the round-4 walk's bare "Base case: 159.61 EUR" was read at 19:15Z, before ww-1's redeploy. So on
today's served payloads the contradiction is already absent; the cell builds the unlabelled fallback the ruling names.

<status>pending</status>
<round>5</round>
<slot>~20</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
