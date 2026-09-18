# TO LGIC_ENFORCE.TO-EN-c-31-r5 -- R-39's card: a card whose stated reason is wrong retires the question

<to_id>LGIC_ENFORCE.TO-EN-c-31-r5</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- C31R5-AC1 PASS, C31R5-AC2 PASS, C31R5-AC3 UNVERIFIABLE-BY-INSTRUMENT (judgment, for 3.0.0_SA_CVO at L9). proof-of-spec-check.py rc=0 VALID at f67dbcbbc0. 0.9.0_WK_LGIC_ENFORCE~1.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-c-31` (decomposition v3.4 s.0e) | **outcome_ref:** FWD-5 | **depends_on:** `EN-h-29-r5` drained (same queue, same folder grant)

---

## WORKER FACE

### THE CELL

`EN-c-31`. **You correct the stated REASON on two owner cards, and you mint nothing.** Ruling **R-39**
(`1.0.0_SA_CTO`, on row `LGIC_ENFORCE-W1-S30`) is the authority and its two halves are both binding:

1. **`security` is NOT minted, and the vocabulary is NOT reshaped for one measured collision.** One `systems.json`
   row keys purely on the token (`lib/opal_naming.py` `_system_of` :1087-1093) and would resolve BOTH the D12 opsec
   buckets AND `NFRA_TERRAFORM`'s closed, unregistered security-sweep tooling -- misattributing one group whichever
   owner it names. Both groups STAY CARDED.
2. **The CARD'S REASON CHANGES to `TOKEN_COLLISION`.** Today `opal-data-security[-access-logs]` is carded as though it
   lacked an owner, and it has a genuine citable one: **D12 / `NFRA_OPSEC202609`, `DIRECTIVES.yaml` :485.** A card
   whose stated reason is wrong RETIRES the question instead of holding it open.

**WHY THE REASON IS THE DELIVERABLE, not a nicety.** The per-context split of `systems.json` is a `LGIC_NAMING` schema
question and becomes justified on the SECOND collision. **A census of `TOKEN_COLLISION` cards is one grep; a census of
"tokens that would misattribute if minted" is not a question anyone can ask.** The corrected reason is what makes the
second instance findable.

**WHAT YOU DO.** In `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/OWNER_CARDS_R4.md`:

- **Card 5** (security-sweep tooling, `NFRA_TERRAFORM`, closed and unregistered) -- state its reason as
  `TOKEN_COLLISION` and say which OTHER group shares the token.
- **Card 6** (`opal-data-security` and `opal-data-security-access-logs`) -- state its reason as `TOKEN_COLLISION`,
  and name its genuine owner: **D12 / `NFRA_OPSEC202609`**, citing `DIRECTIVES.yaml` :485. Say plainly that this group
  is carded NOT for want of an owner but because the token cannot carry two owners.

**MEASURED AT THE CUT, so you can tell what you changed:** `OWNER_CARDS_R4.md` is markdown with **zero JSON fences**
and 12 `## Card <n> -- ...` sections; `TOKEN_COLLISION` occurs **0** times in it; the whole value `"security"` occurs
**0** times in `systems.json`; `systems.json` carries 25 minted keys and 3 `unresolved` tokens.

**DO NOT:** mint `security` (or any token) in `systems.json`; add a row to `resources.json`; rename
`security-sweep-*` -- that surface belongs to a CLOSED project and R19 says an existing surface reaches conformance
through its own migration, never as a rider on unrelated work; or edit any card other than 5 and 6.

**Read:** `OWNER_CARDS_R4.md` Cards 5 and 6; row `LGIC_ENFORCE-W1-S30` on the project's investigation channel and its
remediation row in `.../remediations/REMEDIATION_v2.md`; `DIRECTIVES.yaml` around :485; decomposition v3.4 s.0e.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="C31R5-AC1" cell_refs="EN-c-31"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py c31-card</invocation><expect>PASS-C31-TOKEN-COLLISION-CARDS-CORRECTED</expect></criterion>

<criterion id="C31R5-AC2" cell_refs="EN-c-31"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py c31-not-minted</invocation><expect>PASS-C31-SECURITY-NOT-MINTED-WITH-A-LIVE-CONTROL</expect></criterion>

<criterion id="C31R5-AC3" cell_refs="EN-c-31" judgment="true"/>

<expected_criteria>C31R5-AC1, C31R5-AC2, C31R5-AC3</expected_criteria>

**AT THE CUT:** `C31R5-AC1` reads **FAIL** (`TOKEN_COLLISION` occurs 0 times). **`C31R5-AC2` reads PASS and is a
GUARD** -- R-39's bar is that `security` STAYS unminted, so that arm refuses your work only if you mint it. It carries
its own POSITIVE CONTROL and prints a key it can see, because "`security` is absent" and "this arm cannot read
`systems.json`" would otherwise be the same output.

**`C31R5-AC3`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the corrected cards hold the question open
rather than retiring it -- a reader arriving at Card 6 in three months should be able to tell that the group has an
owner, that the token is what blocks the mint, and where the schema question lives.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. **`OWNER_CARDS_R4.md` is inside YOUR OWN serial's folder, which is why this cell is yours and not another slot's** -- `.tools/owned-paths-validate.py` clause 4 permits exactly the serial named by the `deliverables/<SERIAL>/` sub-folder, and it REFUSES any other, measured the same night on a sibling project.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only.** A wrong arm is a BLOCKING row, never an edit.
- **Surprises** go to the project's `INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array, id `LGIC_ENFORCE-W<n>-S<k>` with `<k>` one above the highest already present in ANY document under that channel. Keep working after filing.
- **Judge from the files this order names and cite them** (`path:line @commit`).
- **Numbers here are CONTEXT, never acceptance values.** Re-measure at your own tree.
- **Commit before you grade.**
- **Nothing live moves.** No apply, no AWS write, no deploy, no rename of a live resource.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.4, round-5 cell `EN-c-31` (section 0e).
<owned_cells>EN-c-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `C31R5-AC1`, `C31R5-AC2`, `C31R5-AC3`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-c-31-r5.token-collision-card.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> C31R5-AC1,C31R5-AC2,C31R5-AC3 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-c-31-r5.token-collision-card.md` BEFORE the `complete` flip.
Result file `token-collision-card.r5.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`C31R5-AC3` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-5 cut: no schedule is created or read.
comp-iam: RUN at the round-5 cut: no grant moves; the cell edits prose in one markdown document.
comp-adversary: RUN at the round-5 cut: the not-minted arm is exercised with a LIVE POSITIVE CONTROL and prints a key it can see, because an absence read by a blind instrument is indistinguishable from an absence.
lane: the <paths> block is the grant (RULING 1 shape c); OWNER_CARDS_R4.md sits under deliverables/0.9.0_WK_LGIC_ENFORCE~1/, which the tree convention grants to THIS serial and to no other -- the seating follows the folder, not a preference.
contention: OWNER_CARDS_R4.md is written by no other open order in either LGIC project at the cut. EN-c-28-r5 writes OWNER_CARDS_R5.md, a different file in the same folder, and runs after this cell in the same queue.
</preflight>

Seating: slot ~1, level 1, SECOND of a three-order queue (`EN-h-29-r5` -> `EN-c-31-r5` -> `EN-c-28-r5`). Round 5 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.4 s.0e. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/`. Rulings carried: R-39, R19 (the rename is NOT ruled), R-40.
