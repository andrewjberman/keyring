# TO NFRA_TRNSPT.TO-TR-w2 -- the two classes the wipe misses, as planted cases: removed or a stated limit

<to_id>NFRA_TRNSPT.TO-TR-w2</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-w-2` (`decompositions/NFRA_TRNSPT_DECOMP_R2.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-w-2` (CTO analysis ruling 4): "Round 2 adds the two classes the builder named as missed (a standalone lower-case name with no
same-message capitalised sighting; an English-word surname at sentence start) as PLANTED cases in the planted-token gate. Each either
passes (the wipe improved) or is recorded as a stated limit in C-WIPE; the gate's result stays 'the planted classes were removed',
never 'no PII remains'."

**What exists (read first):** `data/transcripts/scripts/outlook/wipe.py` (allowlist first, case-sensitive dictionary names,
salutation context, a name seen capitalised elsewhere in the message is also wiped in other cases, `[ID]` rule, residual flags) and
`data/transcripts/scripts/tests/test_wipe_planted.py` (8 tests; it writes the round-1 record
`org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/WIPE_GATE_RECORD.json`). The worker that built it recorded
(row W4-S8): "A standalone lower-case name is not wiped unless the same message shows it capitalised or in ALL-CAPS. English-word
surnames like 'Ask' and 'Mail' are wiped at sentence start unless they are in the small stopword list."

**Build (LOCAL):**
1. Add two planted cases to `test_wipe_planted.py` (SYNTHETIC text, invented names from the vendored dictionary files):
   `lowercase_standalone_name` -- a dictionary name that appears ONLY in lower case in its message (e.g. "please send it to tarquin
   tomorrow"); `sentence_start_word_surname` -- a dictionary surname that is also an ordinary English word, used as a person's name
   at sentence start, in a message where it does NOT appear elsewhere capitalised mid-sentence. Also plant one ordinary-word use of the
   same word (not a name) and assert it survives or state that it does not.
2. For each class: improve `wipe.py` if a precise rule removes it WITHOUT wiping allowlisted finance words or the numbers the round-1
   tests keep (all 8 existing tests must stay green); otherwise leave the rule and record the class as a STATED LIMIT with one
   sentence of limit text. Do not over-wipe to pass: an ordinary word that is not a name wiped everywhere is a regression, not a fix.
3. The test writes the round-2 record
   `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/WIPE_GATE_RECORD_R2.json` =
   `{"result": "the planted classes were removed", "not_claimed": "no PII remains", "classes": {<name>: {"planted": n, "removed": n,
   "outcome": "removed" | "stated_limit", "limit_text": "..." (when stated_limit)}}, "residual_flagged": n}` covering EVERY class,
   the round-1 eleven and the two new ones. "the planted classes were removed" stays the literal result string; a stated-limit class
   is reported by its outcome, never by changing that string.

### ACCEPTANCE

<criterion id="TR2-w2-AC1" cell_refs="TR-w-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_CHECKS/r2_wipe_record_check.py org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/WIPE_GATE_RECORD_R2.json</invocation><expect>WIPE-RECORD-OK</expect></criterion>
`TR2-w2-AC1` -- both new classes planted with a stated outcome; every round-1 class still fully removed. (Read the check first.)

<criterion id="TR2-w2-AC2" cell_refs="TR-w-2"><invocation>python -m pytest data/transcripts/scripts/tests/test_wipe_planted.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR2-w2-AC2` -- a BOUND: the planted gate stays green with the new cases in it.

<expected_criteria>TR2-w2-AC1,TR2-w2-AC2</expected_criteria>

Dry-run at the base c31230ea02: AC1 WIPE-RECORD-BAD unreadable (no R2 record) -- FAIL as expected; AC2 `8 passed` -- the bound PASSES at
the base, as a control should.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL.** No bucket, no mailbox, no real text anywhere.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W2-S<k>`, next unused after W2-S1), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/outlook/wipe.py
data/transcripts/scripts/tests/test_wipe_planted.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R2.md</decomp_doc> (round 2), cell `TR-w-2`.
<owned_cells>TR-w-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR2-w2-AC1, TR2-w2-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-w2.planted-missed-classes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR2-w2-AC1,TR2-w2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** each new class's outcome (removed, or the limit text), any wipe.py rule change, the two check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched.
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (Andrew's IAM user), 1 bucket policy with 2 Deny statements; BLIND: the live IAM plane outside this root (0 of the account's roles read). This cell reads and writes no bucket.
comp-adversary: RUN -- the two classes are the builder's own named misses (W4-S8); the over-wipe regression arm is on the face.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @acd1033e60 ruling 4 and section 4 item 4; row W4-S8; decomposition round 2 cell TR-w-2.
