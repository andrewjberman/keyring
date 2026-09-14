# TO IRPT_FNTEND.TO-FE-s-23 -- the checker cannot see a prompt/record divergence, and returned VALID over one

<to_id>IRPT_FNTEND.TO-FE-s-23</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (no PRD surface -- this cell's subject is the FABRIC's record integrity, stated at the FABRIC grain in decomp R3.5(ii)) | **Decomp cell:** `FE-s-23` (round 3, v0.3 @38f68b965c) | **outcome_ref:** none -- serves the record, not an outcome | **depends_on:** none -- READY ROOT | **slot:** ~3, queue position 1 | **rows:** S31

---

## WORKER FACE

### THE CELL

`FE-s-23` -- **`proof-of-spec-check.py` returned `VALID (rc=0)` over an instance whose recorded invocations were not the invocations its task order carried.**

Measured, round 2 (`S31`): the issuer corrected two print-route URLs in the SPAWN PROMPT and never in the task-order FILE. The worker ran the corrected URLs, they passed, and the instance recorded them faithfully. The governing task order still carried the OLD ones. The checker validated the instance anyway -- **nothing in the fabric compares a recorded invocation against the text of the criterion it claims to satisfy.**

Why that matters more than the one incident: the spine has the issuer substitute `<WS>` and `<PORT>` into the worker face at spawn, so an issuer is ALWAYS editing that string on the way out. Once you are editing it, nothing stops a substantive correction going only there. The prompt is gone the moment the worker ends; the RECORD is what the CVO grades and every successor reads.

**Add the limb.** For each acceptance row in an instance, compare its recorded invocation to the invocation of the same-id criterion in the governing task order, **modulo the declared placeholders** (`<WS>`, `<PORT>`, and any other placeholder the order declares). A mismatch is a VIOLATION that names BOTH strings and the criterion id. Normalisation is limited to placeholder expansion and whitespace at the ends of the string -- **do not normalise away a difference in a flag, a path, a query parameter or a quoted argument**, which is exactly the class `S31` was.

⛔ **THIS LIMB MUST NOT BREAK THE EXISTING CORPUS.** Round 2's instances are honestly aligned and must stay VALID. A limb that refuses everything is as useless as one that refuses nothing, and you prove both directions.

### ACCEPTANCE

<placeholders>WS</placeholders>
⚠ **THE ONE ELEMENT THE WORKER ADDED TO THIS ORDER (row `IRPT_FNTEND-W3-S16`).** It declares, IN THE FILE, the substitution the spawn prompt declared -- `<WS>` = the worktree root -- and nothing else. It changes no criterion id, no invocation, no expectation and no `<expected_criteria>`. Its effect is that THIS order's instance is graded on the new limb's **ENFORCE** branch: every recorded invocation below must equal its criterion's text modulo `<WS>` alone, so the limb ships EXERCISED on a real instance rather than proved only by fixtures. Delete the line and this instance returns to ANNOUNCE; nothing else in the estate keys on it.

<criterion id="F23-AC1" cell_refs="FE-s-23"><invocation>cd <WS> && timeout 120 python .tools/proof-of-spec-check.py --self-test</invocation><expect>RESULT: (\d+) of \1 arm</expect></criterion>
`F23-AC1` -- the checker's own self-test passes with the limb in place: every arm behaves, whatever the arm count has grown to. **The expectation is a BACKREFERENCE and not a literal count** because your limb ADDS arms -- at this cut the tool prints `RESULT: 12 of 12 arm(s) behaved` (verified by the issuer), and a literal `12` would refuse your own correct work. ⛔ And it carries NO literal parenthesis: `<expect>` is graded as a REGEX, so `arm(s)` would match the text `arms` and not what the tool prints (round 2's S16).

<criterion id="F23-AC2" cell_refs="FE-s-23"><invocation>cd <WS> && timeout 180 python .tools/tests/test_invocation_limb.py</invocation><expect>DIVERGENCE CAUGHT: 4 of 4</expect></criterion>
`F23-AC2` -- **the negative control, and the reason this cell exists.** Four seeded divergences between a recorded invocation and its criterion's text -- a changed flag, a changed path, an added query parameter, a changed quoted argument -- are each REFUSED by the checker, each naming both strings and the criterion id.

<criterion id="F23-AC3" cell_refs="FE-s-23"><invocation>cd <WS> && timeout 180 python .tools/tests/test_invocation_limb.py</invocation><expect>PLACEHOLDER EXPANSION TOLERATED: 3 of 3</expect></criterion>
`F23-AC3` -- the other arm: three pairs differing ONLY by placeholder expansion (`<WS>` to an absolute path, `<PORT>` to a number, both at once) are each ACCEPTED. A limb that cannot tell substitution from alteration would refuse every honest instance.

<criterion id="F23-AC4" cell_refs="FE-s-23"><invocation>cd <WS> && timeout 300 python .tools/tests/test_invocation_limb.py</invocation><expect>ROUND-2 CORPUS STILL VALID: 7 of 7</expect></criterion>
`F23-AC4` -- **the regression arm on real bytes, not fixtures.** All seven of round 2's committed instances (FE-s-12, 13, 14, 15, 16, 17, 18) still validate with the limb active. A fixture that cannot represent the real corpus cannot certify it, so this arm reads the committed files.

<criterion id="F23-AC5" cell_refs="FE-s-23"><invocation>cd <WS> && timeout 120 python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-15.generate-composer.proof_of_spec.json F15-AC1,F15-AC2,F15-AC3,F15-AC4,F15-AC5,F15-AC6,F15-AC7,F15-AC8,F15-AC9,F15-AC10,F15-AC11,F15-AC12,F15-AC13,F15-AC14</invocation><expect>\bVALID</expect></criterion>
`F23-AC5` -- a named real instance from round 2 validates end to end under the new limb, run through the tool's own CLI rather than through a function call. ⛔ **The bar carries a WORD BOUNDARY deliberately: `<expect>` is a REGEX, and a bare `VALID` MATCHES INSIDE `INVALID`** -- it would pass on exactly the failure it exists to catch. `\bVALID` cannot match `INVALID` because `IN|VALID` has no word boundary between the two.

<criterion id="F23-AC6" cell_refs="FE-s-23"><invocation>cd <WS> && timeout 120 python .tools/proof-of-spec-check.py --self-test</invocation><expect>invocation</expect></criterion>
`F23-AC6` -- the limb is DISCOVERABLE: the self-test's own arm descriptions name it, so a seat that hits the refusal can learn what it keys on without reading the source. ⚠ **This criterion was cut against `--help` and the issuer changed it before issuing, because `--help` DOES NOT EXIST on this tool**: it is read as a FILE PATH, printing `READ-ERROR (rc=2): [Errno 2] No such file or directory: '--help'` -- and **returning rc=0 while doing so**. Do not add a `--help`; that is a different cell's business. Record the rc=0-on-error behaviour as a surprise row if you touch that code path.

<criterion id="F23-AC7" cell_refs="FE-s-23" judgment="true"/>
`F23-AC7` -- graded at L9: the normalisation is narrow enough that `S31`'s actual divergence would have been caught, and wide enough that a legitimate spawn does not trip it. RECORD; NO VERDICT.

<expected_criteria>F23-AC1, F23-AC2, F23-AC3, F23-AC4, F23-AC5, F23-AC6, F23-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. ⛔ **THIS IS THE ONLY ROUND-3 CELL WRITING THE WORKSPACE REPO, AND IT TOUCHES NO PORTAL PATH AT ALL.** You need no portal worktree and you must not create one.
- ⛔ **NEVER EDIT AN EXISTING PROOF INSTANCE.** Round 2's instances are the corpus you are testing against. If one of them fails under your limb, that is a FINDING -- a surprise row with the criterion id and both strings -- and quite possibly a real divergence worth having. It is never a reason to edit the instance or to widen the normalisation until it passes.
- **Workspace paths bind MECHANICALLY** through the lane resolver: `.tools/` is not a lane you hold by default, so if a write is refused, that is a BLOCKING row naming the path and the refusal text -- never an override, and never `GIT_COMMIT_AUTHOR_OVERRIDE`.
- **`.py` edits pass `.tools/commit-gate.sh`** (py_compile + ds-precommit + ruff py39) -- that is universal law, not this order's invention.
- **Two repos?** No. One: the workspace. Never stage `portal`. Never push, merge, rebase, `checkout --` or `clean`.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W3-S<k>` continuing the W3 sequence (last is `W3-S12`, so yours start at `W3-S13`). Re-read the file immediately before minting each id; never edit an existing row; keep working.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL.

<paths>
.tools/proof-of-spec-check.py
.tools/tests/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.3 @38f68b965c, cell `FE-s-23`.
<owned_cells>FE-s-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F23-AC1` .. `F23-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-23.checker-invocation-limb.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F23-AC1,F23-AC2,F23-AC3,F23-AC4,F23-AC5,F23-AC6,F23-AC7` BEFORE the `complete` flip. ⚠ Your instance is graded BY THE TOOL YOU ARE CHANGING -- say so explicitly in the result file, and record the validation twice: once with the limb active, and once noting that a tool validating its own change is a weaker oracle than `F23-AC4`'s real-corpus arm. `F23-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `checker-invocation-limb.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource; the subject is a repo-local checker.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; this cell has no PRD surface and is declared at the FABRIC grain in R3.5(ii) rather than folded into a portal cell.
the gap: RUN by the issuer -- proof-of-spec-check returned VALID (rc=0), 20 rows, 0 violations, over the FE-s-18 instance whose F18-AC12/AC13 recorded invocations carried query params the governing TO did not, for the whole interval between 74cefaf7a2's prompt and its record fix (row S31).
instrument: RUN by the issuer BEFORE issuing, and it changed two criteria. (1) `--self-test` EXISTS and prints `RESULT: 12 of 12 arm(s) behaved`; F23-AC1's bar is a BACKREFERENCE so a grown arm count still passes, and it carries no literal parenthesis because <expect> is a REGEX (S16). (2) `--help` DOES NOT EXIST -- it is read as a file path, prints `READ-ERROR (rc=2)` AND RETURNS rc=0; F23-AC6 was re-cut onto --self-test. An instrument that returns 0 on a read error is why no criterion in this order keys on rc alone.
lane: .tools/ is workspace-mechanical; a refusal is a BLOCKING row, never an override.
</preflight>

Seating: slot ~3, queue position 1; READY ROOT, seated at issuance on a WORKSPACE-ONLY worktree (no portal pair), with the `<status>` flip committed BEFORE the worktree is cut (row IRPT_FNTEND-S26).
