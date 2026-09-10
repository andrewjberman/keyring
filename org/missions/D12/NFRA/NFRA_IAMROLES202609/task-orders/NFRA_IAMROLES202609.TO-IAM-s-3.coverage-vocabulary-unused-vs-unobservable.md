# NFRA_IAMROLES202609.TO-IAM-s-3 -- The COVERAGE vocabulary at PERMISSION grain: `unused` rendered distinctly from `unobservable`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md</decomp_doc>
<owned_cells>IAM-s-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-7; acceptance properties 2, 5)

```
IAM-s-3 mirrors manifest row S3. ACT: author the COVERAGE vocabulary at PERMISSION grain --
`unused` rendered distinctly from `unobservable`, at the grain the claim is made.

THE OUTCOME THIS SERVES, VERBATIM FROM THE RATIFIED ENDPOINT:
  FWD-7  A reviewer can tell "this is unused" apart from "we cannot see whether it is used"
         DONE WHEN  APPLIED -- the assessment reports the two differently, at permission grain
         ACCEPT     Something nobody has looked at never reads as something that was looked at
                    and found clean.
         DO NOT CUT AS GREENFIELD -- HALF OF THIS IS ALREADY BUILT. The existing tool's own
                    self-test already asserts that never-used is not the same as cold, and it
                    carries an explicit UNKNOWN band, ON THE ROLE AXIS. A cell written as new
                    work would re-buy passing, self-testing code. What is missing is the same
                    discipline at PERMISSION grain.

THE VOCABULARY YOU AUTHOR IS A SCHEMA, so CLAUDE.md rule 24 binds it: it arrives with its
FOUR-POSTULATE RECORD and a WORD-BOUNDARY TOKEN CENSUS, or it is not a proposal.
  (i)   MECE over a DECLARED domain -- state the domain (every granted permission of a role at
        assessment time) and HUNT the uncovered member rather than asserting coverage.
  (ii)  SAME GRAIN -- every value is a property of ONE GRANTED PERMISSION, none of a role.
  (iii) INTENT COHERENCE -- one axis: what we know about this permission's use.
  (iv)  STATE COHERENCE -- name which values one remedy does NOT move.

THE TOKEN CENSUS IS A DEBT THIS CELL INHERITS AND MUST DISCHARGE. The L5 decomposition recorded
it explicitly rather than pretending it existed: "OWED BY IAM-s-3 AT PHASE 1, not run here --
IAM-s-3 authors the coverage vocabulary (`unused` vs `unobservable` vs the existing `UNKNOWN`
band) and its census must run against the extended tool's own corpus, which does not exist yet."
The corpus now exists, because IAM-s-1 landed before you. RUN THE CENSUS.

⛔ THE EXISTING `UNKNOWN` BAND IS NOT YOURS TO REPLACE. It is a passing, self-tested value on the
role axis. Decide, and RECORD, whether `unobservable` is a NEW value, a RENAME of UNKNOWN at a new
grain, or a narrower sibling -- and if a rename, the self-test assertion `blind_is_unknown_NOT_unused`
must still be green afterwards. Minting a synonym for a value the estate already has is a
build-ladder violation (rung 2: the estate already has it).
```

## DEPENDENCIES

This cell depends on: **IAM-s-1** (the permission-grain instrument), keyed to OBSERVED COMPLETION --
its deliverable exists and its criteria passed -- never to a status word. You hold IAM-s-1 yourself,
first in this queue, so you carry its context forward.

Downstream, so you know what your output must be usable BY (you do not build these):
IAM-s-2's posture number depends on your vocabulary for its honesty (C-COVERAGE-OVER-COUNT);
IAM-s-9's re-run harness must reproduce your bands comparably.

## BOUNDS -- what this cell may not cross

```
THE BOUND THAT OUTRANKS EVERYTHING ELSE IN THIS CELL, from PRD section 8 row S3 verbatim:
"A GRANT NOBODY LOOKED AT MUST NEVER RENDER AS A GRANT SHOWN CLEAN. This outranks FWD-1's
tidiness." If a rendering choice makes the posture number look better by collapsing
`unobservable` into `unused`, or into silence, THE NUMBER LOSES. Say so in the deliverable.

C-ANALYZER-PRICED-FIRST + G-25: AWS Access Analyzer is the FALLBACK and NO PER-ROLE PRICE HAS
BEEN READ BY ANYONE. You MAY NOT reach for it on the grounds that it is available -- availability
is not authorization. Brief F7 records that AWS's native unused-access finder is STILL not
enabled, measured the same day. That is a FACT ABOUT THE ESTATE, not an invitation to enable it.
If you conclude the cell cannot be served without it, file a surprise ROW and STOP on that
criterion.

C-COVERAGE-OVER-COUNT: a smaller number that states what it could not see BEATS a larger one that
does not. Your vocabulary is the mechanism that makes that statable.

DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED; PRD section 4).
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam-usage self-test (L5 battery, EXERCISED): rc=0, 9 of 9 PASS. TWO of the nine are yours to
keep green and they are the ones that encode FWD-7 at role grain:
  `blind_is_unknown_NOT_unused`            -- blindness renders UNKNOWN, never unused
  `breakglass_never_used_is_stillborn_NOT_reap` -- never-used is not automatically debris
The first is the ROLE-GRAIN ANCESTOR OF THIS ENTIRE CELL. Read it before you author anything.

comp-iam (L5 battery, RUN): BLINDNESS STATED -- `wafv2:UNMODELED` and `UNMAPPED-METHOD` on two
services. comp-iam does not model every action namespace. ⛔ THIS IS ITSELF AN INSTANCE OF THE
DISTINCTION YOU ARE AUTHORING: a permission in an unmodelled namespace is UNOBSERVABLE, not
unused, and comp-iam's silence about it is NEVER evidence that it is unused. Its 304-gap figure is
a FLOOR on the DESIRED plane. Use it as your worked example if it fits.

comp-adversary (L5 battery, RUN on the decomposition): 5 of 5 cited commits VERIFIED, 4 of 4 cited
paths stable. DECLARED BLINDNESS: the L5 lane did NOT read the L1 brief, so every F-number here is
the PRD's rendering of the brief -- one instrument, not two.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/modules/graph/comp_iam_usage.py
.tools/comp-iam-usage
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-3.coverage-vocabulary-unused-vs-unobservable.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-s-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/COVERAGE_VOCABULARY.md && grep -o -E 'unobservable' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/COVERAGE_VOCABULARY.md</invocation><expect>the literal string unobservable, printed at least once -- the distinct band exists and is named; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-s-3"><invocation>.tools/comp-find 'unobservable' org/modules/graph --limit 20</invocation><expect>a printed DENOMINATOR line whose files-scanned count is YOUR WORKTREE's (about 31,000), not the main checkout's (about 55,000) -- discharging the word-boundary token census the L5 decomposition recorded as owed by this cell, over the tree that actually carries your extension. INVOKE IT BY THE EXPLICIT .tools/ PATH AS WRITTEN: the bare name comp-find resolves through a ~/bin forwarder to the MAIN checkout and would census a tree that does not contain your work, returning a large confident denominator over the wrong tree (INSTRUMENT_LIMITS.md LIMIT 4). A scanned count near 55,000 means you invoked the bare name and the census is void</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-s-3"><invocation>.tools/comp-iam-usage self-test | grep -c 'blind_is_unknown_NOT_unused'</invocation><expect>a count of 1 or greater -- the role-grain assertion that encodes FWD-7 is still present and green after the vocabulary work; measured 1 at the cut</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-s-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/COVERAGE_VOCABULARY.md && grep -c -E 'MECE|SAME GRAIN|INTENT COHERENCE|STATE COHERENCE' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/COVERAGE_VOCABULARY.md</invocation><expect>a count of 4 or greater -- the rule 24 four-postulate record is present, one line per postulate; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-s-3" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the distinct band exists and is named `unobservable`, not collapsed into `unused` or into silence
- **AC2** (mechanical): the token census the L5 decomposition recorded as a DEBT is actually discharged, with its denominator printed -- rule 24 requires it of any authored value-enum
- **AC3** (mechanical): the pre-existing role-grain assertion encoding FWD-7 survived -- you may not regress the half that already works
- **AC4** (mechanical): the four-postulate record accompanies the schema, as rule 24 requires of any vocabulary an agent authors
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): FWD-7's ACCEPT in plain English -- on rendered specimen rows INCLUDING at least one genuinely unobservable permission, something nobody has looked at never reads as something that was looked at and found clean. Whether the rendering achieves that for a reader who did not build it is NOT self-gradeable by the builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @cbe45b0db4 -> L2/L3/L4 `1.0.0_SA_CTO~Z` (endpoint RATIFIED) -> L5 `2.0.0_SA_COO~ZI` decomp @9e72041da5 -> L6 this issuance.
**Chain:** A, position 2 of 4 (IAM-s-1 -> IAM-s-3 -> IAM-s-2 -> IAM-s-9). Handed to slot ~1 only when IAM-s-1 is terminal with a valid instance.
**Provenance:** the cell text mirrors PRD section 8 row S3 and the endpoint's FWD-7 verbatim. The token-census debt is carried from decomposition section 2 (rule 24 record), which recorded it as owed by this cell rather than claiming it had been run.
<preflight>
comp-schedule: RUN to completion at --budget 500 (5 of 5 carriers; the default 90s budget returns a PREFIX reporting 7 and says so -- the complete compile reports 26). Denominators C1=23 C2=7 C3=12 C4=20 C5=335. GATES ARMED: 26, NONE owned by this project; G-21 and G-25 bind this cell and are carried into BOUNDS.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED) and UNMAPPED-METHOD on two services. That blindness is itself the worked example this cell's vocabulary must be able to express.
comp-adversary: RUN on the decomposition -- 5 of 5 cited commits VERIFIED, 4 of 4 cited paths stable; DECLARED BLINDNESS on the L1 brief (not read by the L5 lane).
</preflight>

**Preflight disposition:** mandatory core RUN at L5, none declared not-applicable. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell authors a rendering vocabulary and touches no route, cache key, data prop, gold script or deletable resource.
