# AMGT_HARVST task order -- `HVST-r-1` -- ROUND 2, FIRST: the timeline spec gains ONE STATE for the call itself FAILING and ONE ERROR ENVELOPE; no build cell exists against this spec until both land; SPEC ONLY, no code

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-r-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~11</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a document; arms nothing, runs nothing, deploys nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~11`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/` and every path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~11;`.
- **NEVER RUN AN INSTALL. NEVER CALL AWS OR A PUBLISHER. WRITE NO `.tsx`, `.ts` OR `.py` FILE, AND NOTHING UNDER
  `portal/` OR `infra/`.**

## 1. THE CELL, inlined in full -- `HVST-r-1` (manifest row H8; outcomes FWD-5, FWD-6)

**WHY THIS CELL EXISTS, and it is the round's first act.** Round 1 delivered
`deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md`, and `1.0.0_SA_CTO~Z`'s round-1 analysis
(@`f869aa705c`) found it **FAILS one clause of its own judgment criterion: EVERY STATE DRAWN.**

**The measured defect, quoted from that analysis:**
> Section 6 enumerates Loading, a quiet security, the floor clamp, PARTIAL/DENIED and a never-collected security -- and
> PARTIAL/DENIED are DATA states read from `chatter_daily`. There is NO state for "the timeline call itself FAILED", and
> section 5 names no error envelope.

**Why that matters more than a missing paragraph.** It is the same defect `3.0.0_SA_CVO~Z` graduated six hours earlier one
project over (`Z-S227` / `C-S400`), on evidence that its absence **made a real outage invisible for days** and let a page
assert something false about data we hold. The analysis's sentence: *"A spec that omits the state is how a build
reproduces it."* The timeline is a NEW surface on the SAME page, so the omission would have been built.

**RULED -- what you write, and nothing else:**
1. **ONE NEW STATE in section 6**, distinct from every data state already there. It covers **the timeline request itself
   failing** -- a non-200, a timeout, a malformed envelope, an exception in the route. It must state:
   - what the panel DRAWS (never a blank panel, never an empty chart, never a zero series);
   - that it is VISIBLY different from a quiet security and from PARTIAL or DENIED, because those mean *we hold nothing
     for this day* while this means *we do not know what we hold*;
   - what a reader is told, and what they can do next.
2. **ONE ERROR ENVELOPE in section 5**, the API shape: the field or fields that carry a failure, their values, and the
   rule that **a failure is never rendered as data**. Name no implementation file; the route belongs to the build cell.
3. **A one-line pointer, in section 7 (what this spec does not decide), to the precedent** -- that the same omission was a
   real, graduated defect on this page's other panels. One line, no history lecture.
4. **NOTHING ELSE CHANGES.** The other seven sections stand as written and graded strong. Do not restructure, renumber or
   re-word them.

**What this cell does NOT do:**
- no `.tsx`, no route, no API code -- **the build cell against this spec is cut only after Andrew approves the AMENDED
  spec**, per the analysis;
- no change to any other deliverable;
- no change to the gold tables or their contracts.

## 2. WHERE THIS CAME FROM
Round 2, decomposition v1.1 @04a235adb7 section 10a, cell 1 of 5, ranked FIRST by the round-1 analysis @`f869aa705c`.
All five round-2 cells are independent; none makes a vendor call.

## 3. SURFACES -- what you may read and write

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~11/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-r-1.timeline-spec-failed-call-state-and-error-envelope.md
</paths>

**READ-ONLY REFERENCES -- read these, and they are deliberately NOT in the write grant** (round-1 lesson: an order's
`<paths>` may name only what the issuing seat's lane admits, and a read is not a write):
- `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md` -- `C-HV-DESIGN-SPEC-FIRST`, FWD-5 and FWD-6.
- `org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md` -- section 10a for this cell's text.

- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~11 <0.9.0_WK_AMGT_HARVST~11@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with a non-shell writer.

## 4. BOUNDS
- **SPEC ONLY. Pure ASCII. The file stays ONE document with its eight `##` sections**, plus whatever sub-bullets your new
  state and envelope need. Do not add a ninth top-level section.
- **Surprise rows:** `AMGT_HARVST-Z-W11-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "import re;p='org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md';t=open(p,encoding='utf-8').read();h=re.findall(r'^## (\d)\. ',t,re.M);print('sections',''.join(h));print('non_ascii',sum(1 for c in t if ord(c)>127));b=open(p,'rb').read();print('crlf',b.count(bytes([13,10])))"</invocation><expect>"sections 12345678", "non_ascii 0", "crlf 0" -- the eight sections intact, pure ASCII, LF only</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "import re;p='org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md';t=open(p,encoding='utf-8').read();s6=t.split('## 6.')[1].split('## 7.')[0];s5=t.split('## 5.')[1].split('## 6.')[0];print('s6_chars',len(s6),'s5_chars',len(s5));print('s6_mentions_request_failure',any(k in s6.lower() for k in ('request fail','call fail','failed call','route fail','timeout','non-200','error state')));print('s5_names_envelope',any(k in s5.lower() for k in ('error envelope','envelope','error field')));print('never_blank_rule',any(k in s6.lower() for k in ('never a blank','not a blank','never blank','never rendered as data')) or any(k in s5.lower() for k in ('never rendered as data','never as data')))"</invocation><expect>"s6_mentions_request_failure True", "s5_names_envelope True" and "never_blank_rule True" -- the failing-call state is in section 6, the error envelope is in section 5, and the never-render-a-failure-as-data rule is stated in one of them</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --name-only "$(git merge-base HEAD SITEZ)" HEAD -- portal infra lib && git status --porcelain -- portal infra lib && echo "--- end"</invocation><expect>NOTHING printed before "--- end" -- no code, no .tsx, no infra, nothing under lib</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-r-1" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.**
- **AC4 is a JUDGMENT criterion**, graded by `3.0.0_SA_CVO~Z` at L9, never by you. Its question: does the amended spec now
  draw EVERY state, including the timeline call's own failure, such that a build cannot reproduce the `Z-S227` / `C-S400`
  defect on this new surface?
- Record AC4 as `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO.
- **AC2 is a keyword probe and it is deliberately weak.** It cannot judge whether the state is well drawn; that is AC4's.
  Do not write to satisfy the keywords. Write the state, then let the probe confirm it is present.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~11/AMGT_HARVST.TO-HVST-r-1.timeline-spec-failed-call-state-and-error-envelope.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4`, which must return rc 0.
3. Flip to `complete` only if AC1, AC2 and AC3 pass.
4. Commit with `--only`.
5. Report once, quoting the new state's own words and the envelope's fields.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **This cell is FIRST in the round because the analysis ranked it first**, and because the build cell it gates cannot be
   cut until Andrew approves its output (decomposition section 11).
2. **AC2 is a presence probe, not a quality gate.** The quality is AC4's, which is the CVO's. Stating that inside the
   worker face is deliberate: a worker told only "make the probe pass" writes keywords.
3. **The spec file lives in `~8`'s deliverables folder** and is edited in place, because it is ONE document that the page
   build reads; a second copy in `~11`'s folder would fork the spec.

<status>complete</status>
<round>2</round>
<slot>~11</slot>
<fabric>site-z</fabric>
