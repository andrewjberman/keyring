# TO LGIC_ENFORCE.TO-EN-m-39-r8 -- TEMPLATE-VS-KEY: the 15 are TEMPLATES and S3Key is EVERY KEY, and the schema has no field carrying the difference

<to_id>LGIC_ENFORCE.TO-EN-m-39-r8</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-m-39` (decomposition v3.7 s.0h) | **outcome_ref:** FWD-5 | **depends_on:** none -- the only order on slot `~3`

---

## WORKER FACE

### THE CELL

`EN-m-39`. Build the MECHANISM that distinguishes an **S3 KEY TEMPLATE** from an **S3 KEY**.

`W1-S70`'s 15 rows are S3 key FORMAT TEMPLATES -- producer format strings like
`blackdiamond/49f/{snap}/...` whose braces are RUNTIME SUBSTITUTION FIELDS, not gaps in a name. Round 7
carded them under a TRUE reason (`ROW_IS_NOT_A_NAME`), and the round-7 analysis records that this was
more than a rewording: `NON_SYSTEM_PLACEHOLDER_TOKEN` PRESUPPOSES a name, while `ROW_IS_NOT_A_NAME`
says the placeholder question never applied. **`R-62` calling it INTERIM understated it.**

But the card is still a card. **The schema has no field carrying the distinction**, and
`types_not_graded_by_kind` is keyed BY TYPE while every S3 key shares the type `S3Key`.

### THE CONSTRAINT THAT DECIDES THE DESIGN

⛔ **`R-62` REFUSED removing all `S3Key` from the name grade**, and its ground is the bar your mechanism
must clear: **the 15 are TEMPLATES; `S3Key` is EVERY KEY.** Rule 30 makes S3 addresses the core naming
surface, so a mechanism that removes every S3 key in the estate to fix 15 rows is strictly worse than
the carding it replaces.

**SO YOUR MECHANISM NEEDS A WORKING NEGATIVE ARM.** Round 7's single most reusable output was a
selector proven on BOTH directions -- 51 of 51 two-remedy rows selected AND 0 of 15 key templates. Same
bar here:

```
  selects_templates       == 15   of the 15
  rejects_ordinary_keys   == every ordinary S3 key you test, and the number tested is POSITIVE
```

⛔ **ZERO ORDINARY KEYS TESTED IS A VACUOUS NEGATIVE ARM** and the checker refuses it by name.

### THIS IS A SCHEMA ACT, SO RULE 24 BINDS IT

`R-62`: a schema change needs **Rule 24's four-postulate record plus a word-boundary token census**, and
is **never a rider on another round**. That is why it is its own cell.

Your record carries all four postulates with text: `mece_over_a_declared_domain`, `same_grain`,
`intent_coherence`, `state_coherence` -- and under (iv), name which values your remedy does NOT move.

**THE TOKEN CENSUS IS WORD-BOUNDARY, WITH ITS DENOMINATOR, AND BOTH COUNTS PRINTED.** This project has
been bitten twice by a substring read in two days: `C6` matching inside the criterion id `C33R6-AC6`,
and a `sentiment` hit that was a word inside a quoted grep pattern rather than a registry row. Record
`denominator`, `whole_value_hits` and `substring_hits` separately.

### THE STANDING HAZARD ON THE FILE YOU ARE EDITING

⛔ **`types_not_graded_by_kind` IS A ROUTING TABLE, NOT AN EXCLUSION LIST, AND ITS NAME IS THE OPPOSITE
OF ITS BEHAVIOUR.** `lib/opal_naming.py:493` UNIONS the whole table into `graded_types`; the real switch
at `:1012` is `str(why).startswith("NOT GRADED")`. **REWORDING A REASON SILENTLY RE-GRADES A TYPE**, and
nothing announces it. Measured at the cut: 15 entries, **8 genuinely out**, **7 still graded**
(`EVENT_RULE`, `LOG_GROUP`, `S3Key`, `S3_BUCKET`, `S3_BUCKET_POLICY`, `SCHEDULE`, `SECRET`).

`m39-no-grade-change` re-asserts that 8/7 split unchanged **for every type you do not DECLARE you are
moving**. Declaring a move is legal and the arm accepts it; moving one silently is what it refuses.

**Read:** `R8_BASE.json`'s `exclusion_table_at_the_cut`; `lib/opal_naming.py:493` and `:1012` AT THE
BYTES; `R-62` at its carrier `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260917.md`; round 7's `LABEL_TRUTH_R7.json` for the 15's identity.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/TEMPLATE_VS_KEY_R8.json`

```
  {"four_postulates": {"mece_over_a_declared_domain": "...", "same_grain": "...",
                       "intent_coherence": "...", "state_coherence": "..."},
   "token_census": {"denominator": <int>, "whole_value_hits": <int>, "substring_hits": <int>},
   "exclusion_table_after": {"deliberately_moved": [...], "genuinely_not_graded": [...],
                             "still_routed": [...]},
   "discrimination": {"selects_templates": 15, "rejects_ordinary_keys": <int>,
                      "ordinary_keys_tested": <int>}}
```

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="M39R8-AC1" cell_refs="EN-m-39"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py m39-four-postulates</invocation><expect>PASS-M39-FOUR-POSTULATES</expect></criterion>

<criterion id="M39R8-AC2" cell_refs="EN-m-39"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py m39-token-census</invocation><expect>PASS-M39-TOKEN-CENSUS</expect></criterion>

<criterion id="M39R8-AC3" cell_refs="EN-m-39"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py m39-no-grade-change</invocation><expect>PASS-M39-NO-GRADE-CHANGE</expect></criterion>

<criterion id="M39R8-AC4" cell_refs="EN-m-39"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py m39-discriminates</invocation><expect>PASS-M39-DISCRIMINATES</expect></criterion>

<criterion id="M39R8-AC5" cell_refs="EN-m-39" judgment="true"/>

<expected_criteria>M39R8-AC1, M39R8-AC2, M39R8-AC3, M39R8-AC4, M39R8-AC5</expected_criteria>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, MEASURED. Note `m39-no-grade-change` grades YOUR
RECORD rather than the live schema, so unlike round 7's analogous guard it FAILS at the cut with the
rest -- there is no guard-shaped criterion in this round.

**`M39R8-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the four postulates are
SUBSTANTIVE rather than four filled fields, and whether the mechanism's distinction is principled
rather than a pattern that happens to select today's 15. The arms can only check presence, arithmetic
and the negative arm.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives **31 arms, 13 POSITIVE-SATISFIABILITY**. Run it
first. An arm a correct record cannot satisfy is a BLOCKING surprise row quoting the arm and its output.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **YOU ARE THE ONLY ROUND-8 CELL PERMITTED TO TOUCH `org/standards/NAMING_SCHEMA.json`.** Every type you move is DECLARED in `deliberately_moved`. A type that moves without being declared is what `M39R8-AC3` refuses.
- ⛔ **NO GRADE MOVES FOR ANY TYPE YOU DO NOT DECLARE**, and the 15 rows' SIGNIFICANCE is not yours to re-decide -- round 7 settled their reason.
- ⛔ **NOTHING LIVE MOVES.**
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump the array; assert the non-ASCII CHARACTER count and the backslash-u count unchanged. `len(b)-len(b.decode())` is a BYTE DELTA, not a character count.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, re-measured at your own write time. **Three other orders are open this round.**
- **Commit before you grade.**

<paths>
org/standards/NAMING_SCHEMA.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.7, round-8 cell `EN-m-39` (section 0h).
<owned_cells>EN-m-39</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `M39R8-AC1` through `M39R8-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-m-39-r8.template-vs-key.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> M39R8-AC1,M39R8-AC2,M39R8-AC3,M39R8-AC4,M39R8-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-m-39-r8.template-vs-key.md` BEFORE the `complete` flip.
Result file `template-vs-key.r8.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`M39R8-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the token census's THREE numbers (denominator, whole-value, substring), the discrimination pair with its tested denominator, and the exclusion table's 8/7 split before and after with anything you moved NAMED.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-8 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-8 cut: no grant moves. The cell edits one schema file in the repo.
comp-adversary: RUN at the round-8 cut: the adversarial control is m39-discriminates' negative arm with a POSITIVE tested denominator. A mechanism that selects the 15 by matching something only they carry today would pass a selection-only arm and quietly take every S3 key with it the first time a key grows a brace. The negative arm with a printed denominator is what separates a principled distinction from a pattern fitted to fifteen rows.
lane: the <paths> block is the grant. org/standards/ is lane ANY; NAMING_SCHEMA.json is granted to THIS CELL ONLY this round and refused to the other three by a BOUND in each of their orders.
contention: NAMING_SCHEMA.json is written by NO OTHER open order in any LGIC project at the cut -- this cell is its sole writer this round. The channel is shared with all three slots and no slot isolates there per 14b.
</preflight>

Seating: slot `~3`, level 0, the only order on its slot. Round 8 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.7 s.0h, from the REGISTER's ROUND 8 MATERIAL block `(b)`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/`. Rulings carried: R-62, R-30, Rule 24.
