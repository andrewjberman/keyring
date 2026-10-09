# DSGN_AMGTV1 task order -- `AV-zzp-1` -- THE THESIS WINDOW PRINTS THE SERVED DESCRIPTION UNDER ITS HEADING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzp-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~138</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal f043b827 (= origin DEV, round 63) -- r64a.cjs 1 of 4 (arms 1-3 FAIL as expected, on a real render of ThesisCardDetail; PLANTED passes); battery29 ALL PASS at the base (round-63 candidates).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzp-1` (round 64, decomposition v64; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round63.md` section 2 first. Do the items in this order.

`components/ThesisCards.tsx` `ThesisCardDetail` (the Investment-thesis window) heads the DRAFTED `company_description` section with its
served label "Company description". On ASML those drafted sentences are machine-drafted Item 5 financial lines ("In Logic, net sales
increased by EUR 2.9 billion ...", ITEM 5 > PARAGRAPH 31). So filed financial detail is labelled as the company description, and the
description itself is never printed, although `/thesis` serves it as the `dossier_sections` entry `company_description`
(`{ field, heading, status, text, reason, citation }`, `types.ts` `DossierSection`; status `served`, 1,535 characters on ASML).

1. **Widen the bundle** (`CardBundle`, about line 36): add `dossier_sections` to the picked fields. The caller already passes the whole
   /thesis bundle.
2. **The served description** (`ThesisCardDetail`, investment_thesis window):
   - Find the `dossier_sections` entry whose `field` is `company_description`.
   - When its `status` is `served` and its `text` is not empty, print the text verbatim, once, on an element marked
     `data-thesis-description="served"`, directly under a heading that is the entry's served `heading`.
3. **The empty state:** otherwise (no entry, status not `served`, or no text), print ONE line marked `data-thesis-description="absent"`.
   That line is the entry's served `reason` when one is served, else `No company description is on file.` No text is printed as a
   description.
4. **No false label:** the DRAFTED `company_description` section's sentences (with their passages and the sentence press, as now) are
   headed `From the filing` (`data-thesis-block-heading="company_description"`), never with the description heading. Keep
   `data-thesis-description-verdict` on their wrapper. The investment_thesis section's own sentences follow as now.
5. **Harness:** if `__harness__/` reads the old heading, re-anchor it with its claim kept, and record it in the instance.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Move and fold, never reword served text; never compute a figure the page does not serve** (C-PRESENTATION-ONLY).
   `reasonWords.ts` and `cscTable.ts` are not yours. No non-ASCII characters (use `--`). Keep each file's line endings as you find
   them (read them first). Edit tool for existing files.
4. Portal files commit inside `portal/` on your portal branch (set the author with `-c user.name=... -c user.email=...`; the nested repo
   has no identity), then the outer commit with safe-commit. Do not commit the portal gitlink.
5. If an item cannot be met within your paths, file a row and stop on that criterion. In particular, if battery29 goes red on a
   harness file outside your paths, file a row naming the harness and the assertion, and stop: the issuer rules it.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~138/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `components/DossierSections.tsx` (how the tab face draws the same served notes), and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round64/checks/r64a.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzp-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round64/checks/r64a.cjs"; echo "exit=$?"</invocation><expect>ROUND 64 THESIS DESCRIPTION: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzp-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzp-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): ASML's Investment-thesis window prints the served description text under its heading, and the Item 5 lines sit under 'From the filing'.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~138/DSGN_AMGTV1.TO-AV-zzp-1.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-64 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W138-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 64 = `ledger/ROUND_ANALYSIS.round63.md` @f7d74e6665 section 2: item 1 is AV-zzp-1, and items 2-3 are the
issuer's close walk, made possible by AV-zzp-2 (the walker's press flags). Base portal f043b827 (= origin DEV). LF only (ruling R2,
row D1-S1).

<status>pending</status>
<round>64</round>
<to_id>DSGN_AMGTV1.TO-AV-zzp-1</to_id>
<slot>~138</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
