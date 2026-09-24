# AMGT_RESAPP task order -- `AMGT-rm-3` -- THE RESIDUE, MEASURED FIRST: every failing element inside the page's main, traced and attributed to a file, no fix

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rm-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~142</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-37 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. Renders against a LOCAL vite dev server with the stubbed session and fixtures; no fetch to any origin but localhost.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~142`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`grep -c 'scope' portal/scripts/ui-contract-check.mjs` (rm-1's re-keyed instrument has merged before you; 0 = BLOCKING row,
stop). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~142;`. **NEVER RUN AN INSTALL.** Never push,
merge, rebase, `checkout --` or `clean`. **Portal is a NESTED repository at `<worktree>/portal`:** portal files are committed
inside it (`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~142 <0.9.0_WK_AMGT_RESAPP~142@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts, logs and
captures under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~142/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rm-3` (round 38, decomposition s.46) -- WAVE 1, after rm-1; MEASURE, DO NOT FIX

The round-37 analysis (s.3.3) ruled: *"SIZE 10 AND THE RADII COUNT VARIANCE -> UNRESOLVED, AND NAMED AS UNRESOLVED ...
round 38's cell carries them as measure-first rather than as fix. A cell that 'fixes' an unattributed criterion is a cell
that will discover its own scope mid-flight."* The CVO's invariance sweep (ADJUDICATION_v47 s.2.3) read size 10 at 47 on
thesis and model / 26 elsewhere and 8px radii at 17-18, varying; the CRO's subtraction read, INSIDE main on thesis, weight
600 on 6 chars, one 8px radius and 21 chars at 10px. And the band count, now re-keyed by rm-1 to the Panel's own marker,
is a number nobody has read per state yet.

**WHAT YOU BUILD: `--trace` on `scripts/ui-contract-check.mjs`** -- for each state and each graded predicate that FAILS
inside `--scope main` (weights outside {400,700}, sizes below 11, radii outside {2,3,4,pill}, shadows, purpleFills over the
FWD-27 count, bandContainersTopLevel other than 1), dump the offending elements: tag, the full class string, the nearest
ancestor carrying a `data-*` attribute (name and value), the first 60 chars of text, and the computed value that failed.
Write `trace.<state>.json` per state. Then **ATTRIBUTE** every dumped element to a source file by its class string (the
class census's own patterns over `src/pages/SecurityAnalysis/**`, `src/ui/**`, `src/components/**`, `src/App.tsx`), and
write `ATTRIBUTION.md`: a table predicate x state -> (count, elements, owning file or UNATTRIBUTED with the reason), with
the denominators printed (elements dumped vs elements attributed), and a closing section "WHAT A FIX WOULD TOUCH" listing
the distinct owning files with counts -- the round-39 input. **You edit no source file.**

## 2. BOUNDS

1. **The dev server:** from `portal/`, the bun binary at
   `C:/Users/Opal Bloomberg/AppData/Local/Microsoft/WinGet/Packages/Oven-sh.Bun_Microsoft.Winget.Source_8wekyb3d8bbwe/bun-windows-x64/bun`
   (`"<bun>" run dev --port 5184 > ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~142/dev.log 2>&1 &`),
   wait for `Local:` (up to 90 s), run, then stop it by the PID you recorded. Port **5184**.
2. **Measure, never fix.** A source edit outside `scripts/ui-contract-check.mjs` is a refusal of this cell's shape; the
   trace mode changes no predicate, threshold or set.
3. **An element you cannot attribute is UNATTRIBUTED with the reason** (a class string the census patterns do not carry, a
   component rendered from `node_modules`, a computed style with no class) -- never guessed to a file.
4. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-measure.mjs
portal/scripts/ui-smoke.mjs
portal/scripts/ui-class-census.mjs
portal/src/pages/SecurityAnalysis/**
portal/src/ui/**
portal/src/components/**
portal/src/App.tsx
portal/src/index.css
portal/DESIGN.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~142/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

You WRITE `portal/scripts/ui-contract-check.mjs` (the trace mode only) and your deliverables; every other path is a
read-only input.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rm-3"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-contract-check.mjs --port 5184 --scope main --trace --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~142/trace; echo "exit=$?"</invocation><expect>THE TRACE RUNS ON ALL SIX STATES: a trace.&lt;state&gt;.json per state whose per-predicate element counts EQUAL the summary table's failing counts for that state (print the pairs -- a trace that dumps fewer elements than the summary counted is a trace with a hole, reported as such), each element carrying tag, class string, nearest data-* ancestor, text head and the failing computed value; the graded table printed unchanged from rm-1's shape</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rm-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; test -s org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~142/ATTRIBUTION.md &amp;&amp; grep -c "UNATTRIBUTED" org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~142/ATTRIBUTION.md; head -60 org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~142/ATTRIBUTION.md</invocation><expect>EVERY DUMPED ELEMENT ATTRIBUTED OR NAMED UNATTRIBUTED WITH ITS REASON: the table predicate x state with counts, the denominators (dumped vs attributed) printed per state, the weight-600 / size-10 / 8px residue inside main each landing on a named file, the re-keyed band count per state with the element named where it is not 1, and the closing WHAT A FIX WOULD TOUCH list of distinct files with counts</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rm-3"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; git diff --name-only $(git merge-base HEAD DEV) -- src | wc -l &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis | tail -1</invocation><expect>NO SOURCE MOVED: the diff over src/ against the base reads 0 files, and the page census reads FILES 31 TOTAL 0 exactly as at the cut</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~142/AMGT_RESAPP.TO-AMGT-rm-3.the-residue-measured-first.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
per-state band count after re-keying, the WHAT A FIX WOULD TOUCH list, the UNATTRIBUTED count with reasons, the two commit
hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** wave 1, after rm-1 merges (its `--scope main` and marker-keyed band count are what this cell traces).
Item 3 of the round-37 analysis, plus item 2's per-state band read on the re-keyed number (s.46a).

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~15:0xZ.** Flipped by the ISSUER; the worker left the record face alone.
3 of 3 criteria PASS, proof-of-spec rc=0 VALID (re-run by this seat inside the worker's worktree C:/tmp/wk-amgt-38-142).
AC1: --trace on all six states, trace.<state>.json per state with counts EQUAL to the summary's failing counts (18 of 18 elements
dumped), the graded table unchanged from rm-1's shape, exit=1 on the standing FAILs (printed). AC2: ATTRIBUTION.md -- 18 dumped /
18 attributed / 0 UNATTRIBUTED. Band count re-keyed reads 1 of 1 on all six (no element to name). weight 300 -> PageHeaderVariants.tsx:46
(rm-2's). weight 600 and the 8px radii -> PanelHeader.tsx (title h3 :75, strip container :62; 5 of 6 states, peers has no strip):
the radii are rm-2's, the 600 is THE RESIDUE, attributed for the first time (rm-2's face moves that same title to 700, so it may
close in the same drain). size 10 -> DataTimestamp.tsx:38 rendered through PanelHeader.tsx:99's text-[10px] (thesis and model, the two
PanelHeader calls passing a timestamp): THE RESIDUE. Exhaustive: every dumped 8px traces to the identical PanelHeader.tsx:62 string;
no non-strip 8px exists. WHAT A FIX WOULD TOUCH: 3 files, 18 elements -- PageHeaderVariants.tsx (6), PanelHeader.tsx (10),
DataTimestamp.tsx (2). AC3: 0 src files off the base; census FILES 31 TOTAL 0. No rows. Drained @20d0d02a7a; portal DEV ffef75aa
(merge of f326daff), gitlink c7b022a1 -> ffef75aa. Round-39 input: PanelHeader.tsx:99 text-[10px] and DataTimestamp.tsx:38 (size 10);
weight 600 if rm-2's 700 does not cover it.

<status>complete</status>
<round>38</round>
<slot>~142</slot>
<fabric>site-z</fabric>
