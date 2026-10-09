# DSGN_AMGTV1 task order -- `AV-zzq-1` -- THE SERVED DESCRIPTION DOES NOT REPEAT ITS HEADING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzq-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~140</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal 686ced10 (= the approved round-64 DEV candidate) -- r65.cjs 3 of 4 (STRIPPED FAILS as expected; LEFT WHOLE and HEADING KEPT hold as guards; PLANTED passes); battery29 ALL PASS at the base (round-64 candidates).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzq-1` (round 65, decomposition v65; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round64.md` section 2 first. Do the items in this order.

`components/ThesisCards.tsx` `ThesisCardDetail` prints the served dossier description (`dossier_sections` entry `company_description`,
about lines 383-415) on `data-thesis-description="served"` under the entry's served `heading`. On ASML the served text itself begins
"COMPANY DESCRIPTION:", so the label reads twice.

1. **Strip a repeated leading label, and only that.** Before printing, if the served text begins (after leading whitespace) with the
   entry's served `heading`, compared case-insensitively, followed by optional spaces and a colon, drop that prefix and the whitespace
   after it. Print the rest verbatim. Use a small helper in the same file; build the pattern from the served heading, regex-escaped,
   never a hard-coded string.
2. **Leave everything else whole:** the same words mid-text, a different leading label (e.g. "Overview:"), and a text with no label.
   Nothing else is trimmed, re-spaced or reworded. The missing spaces between sentences are a producer defect (AMGT_RESAPP round 85,
   jj-1) and are NOT patched here.
3. **The heading itself still prints once** above the text.

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
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~140/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `components/DossierSections.tsx`, and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round65/checks/r65.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round65/checks/r65.cjs"; echo "exit=$?"</invocation><expect>ROUND 65 REPEATED LABEL: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzq-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): ASML's Investment-thesis window shows 'COMPANY DESCRIPTION' once, as the heading, with the description text starting 'What started as...'.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~140/DSGN_AMGTV1.TO-AV-zzq-1.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-65 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W140-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 65 = `ledger/ROUND_ANALYSIS.round64.md` @3f30e42354 section 2 item 1, one cell. Base portal 686ced10 (the
approved round-64 DEV candidate, not yet on origin DEV at the cut). LF only.

<status>complete</status>
<round>65</round>
<to_id>DSGN_AMGTV1.TO-AV-zzq-1</to_id>
<slot>~140</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
