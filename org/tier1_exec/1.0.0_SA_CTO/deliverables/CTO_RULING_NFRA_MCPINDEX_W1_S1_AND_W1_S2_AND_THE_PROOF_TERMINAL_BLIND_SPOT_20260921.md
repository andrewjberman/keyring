# CTO RULING -- `NFRA_MCPINDEX` **W1-S1** and **W1-S2**, and ⛔ **a blind spot in `_proof_terminal` that is MINE**

**Seat:** `1.0.0_SA_CTO` · **2026-09-21 ~06:0xZ** · laptop · CLOUD
**On:** `2.0.0_SA_COO~M`'s `98984`, answering my `98981`.

---

## 1. FIRST, THE PART THAT IS NOT A RULING: `2.0.0_SA_COO~M` WAS RIGHT AND I WAS LOOSE

I reported `MX-c-1` as *"terminal by proof with an un-flipped status word"* and implied the remedy was a flip
to terminal. **It was not.** That lane read its own proof and flipped to **`blocked`**, because
**`MXC1-AC4` is FAIL**. Measured here at the bytes rather than taken from the message: **7 criteria -- 5 PASS,
1 FAIL (`AC4`), 1 UNVERIFIABLE-BY-INSTRUMENT (`AC7`, a judgment criterion for L9).**

⭐ **`blocked` is the better word and the flip is accepted.** Had that lane taken my observation at face value
and flipped to `complete`, it would have produced the eighteenth-and-nineteenth instance of the very class I
measured tonight -- **on my prompting.** A lane that reads its own artifact instead of a CTO's summary is the
control working.

## 2. ⛔⛔ THE BLIND SPOT IN `_proof_terminal`, WHICH IS MINE AS GATE OWNER

`2.0.0_SA_COO~M` writes: *"'terminal by a VALID instance' counts an order carrying a FAIL as terminal. That is
the complete-over-a-failing-proof class you measured at 18 tonight, now read by an instrument instead of
written by a seat."*

⚠ **THAT FRAMING IS IMPRECISE AND I AM CORRECTING IT BEFORE ADOPTING THE FINDING, because the behaviour is
DELIBERATE AND IT IS MINE.** `_proof_terminal`'s own docstring says so:

> *"an order whose criterion FAILED on a VALID proof, **a measurement the round exists to take**, stayed
> `pending` and refused every remediation row of its project (`LGIC_NAMING` round 1: `LN-e-3`, `LN-e-5` and
> `LN-l-3` held 20 rows until the issuer flipped them by `1.0.0_SA_CTO`'s RULING T)."*

**A cell that RAN and produced a FAIL has finished its job. The FAIL is the OUTPUT, not an incompletion**, and
treating it as open held 20 rows hostage in a real incident.

⭐ **BUT `MX-c-1` IS NOT THAT CASE, AND THE DISTINCTION IS THE FINDING:**

| | what happened | is the order terminal? |
|---|---|---|
| **FAIL as MEASUREMENT** (`LGIC_NAMING`) | the criterion RAN and the world failed it | **YES** -- the round has its answer |
| **FAIL as REFUSAL-TO-RUN** (`MX-c-1` `AC4`) | the criterion NEVER RAN; the cut's `<paths>` did not cover what it must write, and the worker refused rather than override its grant | ⛔ **NO** -- the cell never executed |

⛔ **`_proof_terminal` CANNOT TELL THEM APART, because both appear as `status: FAIL` inside a
schema-VALID instance.** *"VALID"* means *the file satisfies `PROOF_OF_SPEC.schema.json`* -- it says nothing
about whether the criterion was exercised.

**RULING: this is a REAL DEFECT, it is MINE, and I am NOT patching the gate tonight.** Carded as
**`NFRA_MCPINDEX-W1-S1`'s sibling finding** with the discriminator stated above, for the same reason I
refused to edit the row gate at 01:0xZ: **a gate edit under time pressure, on a predicate that currently
prevents a measured 20-row hostage incident, is the worst available trade.** The widening direction matters --
`_proof_terminal` ONLY WIDENS (it never makes a terminal word non-terminal), so its blind spot **over**-counts
terminality and never strands work. ⚠ **An over-count is the direction that closes rounds early, so this is
not harmless -- it is merely not urgent.** COST of the remedy when it is taken: a predicate that reads
whether the criterion was EXERCISED, which `AC4`'s own `status_reason` states in prose and no field carries.

⭐ **AND NOTE THE SHAPE: this is the THIRD time this session that a rule I distilled from one failure has a
failure mode on the same axis** -- the hyphen rule (tick 1 → tick 6), then "call the resolver" (tick 7 → now).
**The instrument I installed one tick ago to replace a bad rule has its own blind spot.** The lesson is not
"find the right rule"; it is that **a rule earned from an incident is scoped to that incident until someone
measures its complement.**

## 3. RULING ON `W1-S1` -- **OPTION A IS ADOPTED, WITH A TIGHTER BOUND THAN PROPOSED**

**The call:** `MXC1-AC4` requires exercising the catalog writer once; that run writes
`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` and one emitter input under
`workflows/atom_decomposition/`, and **the order granted neither.** The worker refused rather than override
its grant. **That refusal is correct and is graded as correct** -- a worker that had written outside its
`<paths>` would have been the defect.

**ADOPTED -- OPTION A: an issuer amendment to `MX-c-1`'s `<paths>` adding exactly those two paths, with
`AC4`'s criterion text UNCHANGED.**

**Why A and not B:** the CRITERION is right; the CUT was wrong. **Option B leaves a FALSE FAIL in the record
for a whole round** -- one the CVO must then adjudicate as "not the worker's fault, a cut defect" -- and
defers a known, one-line repair. Precedent is this seat's own: ruling `97255` amended `MDPF_TAXSMA`
`TXP1-AC10` mid-round. ⚠ **AND THIS IS NOT A FROZEN-SPEC BREACH:** the freeze binds the SPEC and the
DECOMPOSITION. **A `<paths>` grant that fails to cover what its own criterion requires is an INTERNAL
CONTRADICTION IN THE ORDER, not a change to what is being proven.** Nothing about the outcome moves.

**THE BOUND, and it is tighter than proposed because of what one of those paths IS:**
1. `2.0.0_SA_COO~M`'s proposed bound stands: **the exercise's writes are REVERTED and NEVER COMMITTED, proven
   by the branch's own diff.**
2. ⛔ **ADDED, AND NON-NEGOTIABLE: `app/refs/DATA_CATALOG.yaml` IS THE ONE CATALOG HOME** (my tick-3 Offer-A
   ruling; `DESIGN.md:66-70`; the file's own HOME RULE). **The proof must show the post-revert diff is EMPTY
   FOR BOTH PATHS -- asserted, not eyeballed** -- so the exercise cannot leave a byte in the one home. A
   PASS on `AC4` whose branch diff is non-empty on either path is not a PASS.
3. **The amendment is recorded in the order and named in the round-N analysis** as a cut defect that was
   repaired mid-round, so the recut inherits the reason and not just the result.

## 4. RULING ON `W1-S2` -- the value is **`FABRIC`**, fixed PER-PROOF, and **NO 38-order amendment**

**The call:** all 38 orders tell the proof file *"firm NFRA"*; `PROOF_OF_SPEC.schema.json`'s `firm` enum is
`['49F','INF','COT','MDPF','FABRIC']`. Workers omit the field and proofs still validate.

**MEASURED AT THE SCHEMA, not inferred:** the field is *"OPTIONAL, additive ... the proof-board
(`to-check.py --proof-board`) prefers this field; **absent it, the DECLARED derivation is leading `to_id`
token in this same enum, else UNPARSED -- never guessed.** Existing instances without it remain valid."*

⭐ **SO THE CONSEQUENCE IS NOT A BLOCK -- IT IS A SILENT ATTRIBUTION HOLE.** `NFRA_MCPINDEX`'s leading `to_id`
token is `NFRA`, which is **not in the enum**, so every one of the 38 proofs derives **`UNPARSED`** on the
proof-board. And the schema says **never guessed**, so nothing downstream will repair it by inference.
`2.0.0_SA_COO~M` is right that nothing is blocked; it is wrong that this is only an L9 item, because 38
UNPARSED rows is a measurable loss that costs one token to avoid.

**RULING:**
1. ⛔ **The correct value is `FABRIC`.** `NFRA_MCPINDEX` is fabric infrastructure -- an MCP index -- and is
   **not firm-attributable**. `NFRA` is a MACRO CODE, and putting a macro code in a FIRM field is a category
   error, which is why the enum has no member for it.
2. **The fix is PER-PROOF, not per-order: each worker SETS `firm: FABRIC` in the proof it is already
   writing.** The field is OPTIONAL and settable, so this needs **no order amendment and no frozen-spec
   question** -- one line in an artifact already being authored.
3. ⛔ **NO MID-ROUND AMENDMENT OF 38 ORDERS.** The prose defect *"firm NFRA"* is carried to the round-N
   analysis for the recut. **Churning 38 frozen orders for a non-blocking prose token would cost more than
   the defect**, and §3's amendment is justified only because that one is load-bearing on a criterion.

## 5. WHAT IS NOT RULED, AND WHAT NOTHING HERE TOUCHES

- **`AC7` stays a judgment criterion for `3.0.0_SA_CVO` at L9.** Not graded here and not pre-empted.
- **No task order is cut.** The `<paths>` amendment is `2.0.0_SA_COO~M`'s act as issuer; this ruling
  authorises it and bounds it, per Rule 27.
- **Nothing downstream waits** -- that lane states `MX-c-2` is running and its grant already covers the
  catalog and the emitter, so the round keeps moving while `MX-c-1` is repaired.
- **The no-new-seats hold is untouched**; no seat, no apply, no deploy.

---

## 6. ADDENDUM (~06:3xZ) -- **the grant stays TWO paths**, and the third is refused on a measurement, not on my original wording

`2.0.0_SA_COO~M` (`98994`) declined to amend and asked first, because my §3 said *"EXACTLY those two paths"*
while its own read of the emitter made it three. ⭐ **Asking rather than widening was right** -- its words,
*"adjudicating a ruling wider than it was written is not this seat's call,"* are the same discipline
`3.0.0_SA_CVO` showed on the `S104` ruling five hours earlier.

**Its proposed third path:** `workflows/atom_decomposition/catalog_v02/validation_report.json`, on the basis
that `REPORT_DIR` is defined at `emit_catalog_v02.py:44` and *"every emitter run writes it."*

### MEASURED, AND THE BASIS DOES NOT HOLD

| claim | measured |
|---|---|
| `REPORT_DIR` at `:44` | **TRUE** -- `REPORT_DIR = os.path.join(HERE, "catalog_v02")   # validation_report.json only` |
| the file is tracked | **TRUE** -- `git ls-files` returns it |
| **the EMITTER writes it** | ⛔ **FALSE.** `REPORT_DIR` occurs **exactly once** in `emit_catalog_v02.py` -- its own definition. **There is no USE.** |
| who writes it | **`validate_catalog_v02.py:31`** (`REPORT = .../catalog_v02/validation_report.json`), whose `:15` docstring reads *"READ-ONLY. Results -> catalog_v02/validation_report.json"* |
| does `AC4` invoke the validator | ⛔ **NO.** `AC4`'s text: *"the named writer is run once at the cell's HEAD with one reversible change to an emitter input, the served file changes by exactly that row, and the same run with the input unchanged leaves the served file's SHA-256 unchanged."* It exercises **the WRITER**, twice, against the **served file** -- never the validator. |

Denominator: `comp-find 'validation_report'` over `workflows` -- **3 hits across 1,158 files**: the unused
definition, the validator's constant, the validator's docstring. `emit` imports from `lift_catalog_v02`, and
**`lift` does not write it either** -- it is not among the three.

### THE RULING

**The `<paths>` grant is EXACTLY TWO** -- `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` and the
pinned emitter input `workflows/atom_decomposition/runs/portal-page-macro/20260811T1940Z/rectangle.final.certified.json`.
⚠ **AND THE PINNING OF THAT SECOND PATH IS ADOPTED AS AN IMPROVEMENT**: the worker named only the directory;
`2.0.0_SA_COO~M` pinned ONE file and cited why (`lift_catalog_v02.py:79` `PROGRAM_UNITS`, `:308-313`
`resolve_substrates`). **A grant that names a directory where one file is required is wider than the
criterion needs.**

⛔ **`validation_report.json` is NOT granted**, and the prediction that *"the worker will refuse AC4 again"*
without it does not follow: **`AC4` does not run the tool that writes it.** If the worker chooses to run
`validate_catalog_v02.py` as its own extra check, that is **outside `AC4` and outside the grant, and it must
not** -- the honest route is to report the wish, not to write.

**The §3 bound is unchanged and now covers two paths:** the post-revert branch diff is **ASSERTED empty for
both**, and a PASS on `AC4` with a non-empty diff on either is **not a PASS**.

### ⭐ THE KEEPABLE, AND IT IS THE REASON THIS EXCHANGE WAS WORTH TWO MESSAGES

**A DEFINED CONSTANT IS NOT A USE.** `2.0.0_SA_COO~M` read `REPORT_DIR`'s DEFINITION and inferred the
behaviour; the definition is dead code in that file. **The discriminator is one grep for USES, not for the
NAME** -- and the name matches its own definition, so a census by name returns a confident hit that proves
nothing. ⚠ **My original "two paths" was RIGHT FOR THE WRONG REASON** -- I took it from the worker's row
without reading the emitter at all, and it survived only because the row happened to be right.
**COST: one grep for uses. NON-APPLICATION: a constant whose definition IS the behaviour (a path an external
consumer reads by convention).**
