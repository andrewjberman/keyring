# /self-drive LGIC rulings -- 2026-09-17

`1.0.0_SA_CTO`, laptop fabric. Continues `SELF_DRIVE_LGIC_RULINGS_20260916.md` (R-28 .. R-34); ids run on from it.
Routing law in force: Andrew-direct 2026-09-17 ~13:0xZ -- any open call is closed by the driver on its own
recommendation the same tick; a design fork goes to CRO for research first; a governance fork goes to CVO.

---

## R-35 -- an engine's own MEASURED RUN OUTPUT is a RECORD, and the exemption is the RUN DIRECTORY, never the tree above it

**Call:** `2.0.0_SA_COO~G`, msg 97667 CALL 1, row `LGIC_LGCTFM-W2-S1`. The naming gate's record-tree subtraction is
`RECORD_TREE_PREFIXES = ("org/", "docs/")` plus the registry prefix and `/tests/`. It does not reach
`workflows/legacy_transform/`, DEC-12's RUN HOME, so the LGCTFM engine's own outputs -- `contract.json`, `plan.json`,
`PLANT.json`, `PLANT_UNTYPEABLE.json`, `MARK.json` -- are refused wholesale (1719 REFUSE + 49 RAISE measured by the
worker, confirmed by its issuer at HEAD). Every prior LGCTFM round wrote only into the exempt `org/**` deliverables
tree, so nothing exercised this until the first real run; the gate has ENFORCED since `d181e0ac5a`, so it is a hard
stop on committing any run's artifacts. The gate is this seat's lane and `2.0.0_SA_COO~G` correctly did not touch it.

**RULING: the REC is right on the principle and TOO WIDE on the mechanism. Adopted in the narrow form.** A measured run
artifact is a RECORD of the estate, not a mint -- exactly R-13's reasoning applied to a tree R-13 did not enumerate.
But `workflows/legacy_transform/` is NOT a record tree: it also holds `run_home.py`, ENGINE CODE that mints names and
must stay graded. A prefix exemption on the run home's parent would blind the gate to precisely the declarations it
exists to grade, and it would do so silently, because nothing in a prefix test can tell code from output.

The discriminator is the RUN ID'S OWN SHAPE, read from its producer rather than invented here
(`workflows/legacy_transform/run_home.py:7`, `:46`: `run_dir = <root>/<subject>/<run-id>`, run-id =
`<UTC YYYYMMDDTHHMMSSZ>-<short repo head>`). It is self-limiting: nothing hand-authored lives in a directory named by
a UTC stamp plus a commit pin, and `run_home` REFUSES a run directory that already exists (`:48`), so the name is
minted once by the engine and never reused.

**APPLIED** in `.tools/naming-gate.py`: `RUN_ARTIFACT_RE = ^workflows/[^/]+/[^/]+/[0-9]{8}T[0-9]{6}Z-[0-9a-f]{7,40}/`,
read by a new `_is_run_artifact()` that `_is_record_tree()` now ORs in, so all three existing call sites inherit it.
The DENOMINATOR line prints the exclusion set -- including the pattern itself -- and counts run artifacts separately
from `org/`//`docs/`, per the REC's own "keep the subtraction printed with its denominator".

**EXERCISED, on the engine's REAL bytes, with a negative control** (a green alone would not have shown the widening
risk). Instrument: the gate's own CLI against unified diffs built from
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/walk/contract.json` (37,744 lines, the engine's
actual output), the same bytes placed at three paths:

| path | pre-edit gate | post-edit gate |
|---|---|---|
| `workflows/legacy_transform/blackdiamond-49financial/20260917T202556Z-bb29248/contract.json` (a run dir) | **1062 REFUSE** | **0** |
| `workflows/legacy_transform/contract.json` (same tree, NOT a run dir) | 1062 REFUSE | **1062 REFUSE** |
| `workflows/legacy_transform/blackdiamond-49financial/notarun/contract.json` (run home, malformed run id) | 1062 REFUSE | **1062 REFUSE** |

The first row is the repair; rows two and three are what say it did not widen. Separately, the committed run directory
(6 paths) grades `domain = 6 MINUS EXCLUDED 5 = 1` post-edit against `6 MINUS 0 = 6` pre-edit.

**COST:** one regex per run-home family; a new engine's run home is a one-line gate edit, deliberately, so a tree
enters the exemption by a decision and not by a prefix that happened to match. **NON-APPLICATION:** engine code, a
subject directory's own files (a `MANIFEST.md` beside the runs is not in a run dir), and any path outside `workflows/`.

---

## R-36 -- the contract enum stays equal to the naming schema by subtraction; the untypeable PLANT becomes OPT-IN, and a genuinely untypeable node is CARRIED, never dropped

**Call:** `2.0.0_SA_COO~G`, msg 97667 CALL 2, row `LGIC_LGCTFM-W2-S2`, raised as a design fork with both options and
the facts. `org/standards/LGCTFM_CONTRACT.schema.json` `$defs.node_type.enum` holds 33 values and they are EXACTLY the
33 of `org/standards/NAMING_SCHEMA.json` (`kind.by_type` plus `types_not_graded_by_kind`) -- re-measured by this seat:
`len(enum) == 33`, `sorted(enum) == sorted(naming types)` TRUE, `COGNITO_USER_POOL in enum` FALSE. `LT-e-3`'s
untypeable plant emits a row with `node_type: COGNITO_USER_POOL`, and the plant is UNCONDITIONAL in `cmd_walk()`, so
every contract this engine writes for any subject fails validation on that one row -- all of `X1R1-AC1`'s FAIL.

**RULING: REC (A), and ALT (B) is REFUSED.** The enum's equality with the naming schema BY SUBTRACTION is the
invariant that makes the contract falsifiable at all (Rule 24(i)); a sentinel member re-opens it, and a schema that
can absorb an ungraded type stops being able to say a type is ungraded. The plant becomes opt-in behind
`--plant-untypeable`, `LT-e-3`'s own criterion passes that flag so the untypeable path keeps being exercised
DELIBERATELY, and both drained cells' claims stay true.

**And (A) alone leaves a hole this ruling closes:** with the plant off, a GENUINELY untypeable node met in a live walk
would fail validation for a real reason, and the cheapest repair for a future seat is to drop the row. So: a node
whose type the naming schema does not grade is NOT written into `contract.json` and is NOT discarded -- it is carried
in the run's own `PLANT_UNTYPEABLE.json` (the carrier already exists and already holds exactly one such name), with
its verdict `NOT_COVERED`, and **its COUNT is printed in the contract's summary**, so an empty untypeable carrier
cannot be read as "the walk met none". A zero that is printed is a measurement; a zero that is absent is silence.

**Not routed to CRO**, though it arrived as a design fork: no research would move it. The alternative is forbidden by
the estate's own Rule 24(i) subtraction, which is law rather than pattern, and the carrier the repair needs already
exists in the engine's output. Routing it would have bought a round trip and no information.

**Cut it as ROUND 1's AMENDMENT** (`2.0.0_SA_COO~G`'s own proposal, slot ~2, one order) rather than a round 2, so
`LT-x-2`, `LT-x-3` and `LT-v-1` follow in the same round. The amendment's order carries: the flag, `LT-e-3`'s
invocation change, the untypeable carry-and-count above, and a re-run of `LT-x-1`'s `X1R1-AC1` on a real run.

---

## R-37 -- `prd-signoff status`'s ROUTED SERIAL is the authority on who owns a half; a delivery that names a different seat is the defect

**Call:** raised independently by both COO lanes in the same hour -- `2.0.0_SA_COO~O` ("If the notifier's routed serial
is the authority, say so and I will decline anything it does not route to me; if your delivery is the authority, the
tool should name the same seat") and `2.0.0_SA_COO~G` ("you may want to say which of us holds that duty so neither of
us spends the review twice"). Cause, and it is this seat's: `NFRA_SPMOVE`'s brief half was routed by the tool to
`2.0.0_SA_COO~G`, which refused it @`c1281bfe0a`; my L4-R delivery then asked `2.0.0_SA_COO~O` to take the same half,
which reviewed it @`caedbc4ecd` and could not stamp because the half already carried `~G`'s refusal. Two seats read
one 128-line PRD, roughly twenty minutes duplicated, and both reached the same finding -- the cost of the collision,
not of either review.

**RULING: `python .tools/prd-signoff.py status <CODE>` is the AUTHORITY.** Its `OWED BY` line names the seat that owns
each half; a half is delivered to that seat and to no other, and a seat declines a half the tool does not route to it.
A stand-in stamp carries `--for 4.0.0_SA_CRO` -- my own delivery block omitted that flag, which is the second half of
the same defect. Where a seat has already done the reading for a half that is not routed to it, its review is
EVIDENCE the routed seat may cite rather than re-derive; the STAMP is still the routed seat's, and a review adopted
by citation names the file and its pin.

**Standing practice for this seat:** run `status <CODE>` at the moment of delivery and paste the `OWED BY` line into
the delivery, so the routed serial and the addressed serial are the same string in the same message. A routed serial
read minutes earlier is perishable -- a refusal or a re-route moves it.

**COST:** one `status` read per delivery, which the L4-R step already owes. **NON-APPLICATION:** a half with no live
routed seat -- that is a SEATING ask to `0.0.0_AB_MSTR`, never a re-address to a seat of this driver's choosing.


---

## R-38 -- LGIC_ENFORCE round 5 IS CUT for the 1411-row placeholder population; FWD-5 does NOT close on a census whose canonicals are templates

**Call:** `2.0.0_SA_COO~G`, msg 97676, drain-end of round 4 (issuance `3de3a4e32a`, 5 of 5 drained, 5 of 5 proofs rc=0 at
HEAD `fc2e76f6b4`). The census that stopped on its first RAISE in rounds 1-3 now RUNS TO THE END on both planes --
live `1690 judged + 136 carded == 1826 nameable`, repo `1547 judged + 331 carded == 1878`, `stopped: null`. That is
this seat's stated FWD-5 closure bar, met on its own numbers for the first time. The open question is a POPULATION the
round's own success surfaced: `S25R4-AC3` reads **1411 of 3237** report rows whose `canonical` carries a
`{system}`/`{scope}`/`{cadence}` placeholder. Round 3's census stopped at 21 rows and exposed 8; `EN-h-24` closed
exactly those 8. The other ~1400 were INVISIBLE at the cut because the run that would have shown them could not finish.
The COO offered both branches and cut nothing, correctly, because the choice is this seat's.

**RULING: cut round 5, one cell, on the COO's own shape. FWD-5 does NOT close now.** The bar is `judged + carded ==
nameable`, and its whole point is that a JUDGED row carries a name. A `canonical` of `{system}-{scope}-daily` is a
TEMPLATE, not a name: 1411 of 3237 report rows -- **44%** -- are judged against a string no resource can equal. Closing
FWD-5 on that and carrying the class as a standing finding would convert the exact defect the outcome exists to detect
into a guarantee that it was detected, and it would do so with a printed denominator, which is what makes it dangerous
rather than merely wrong. The bar's numbers being on the table for the first time is the reason to finish it, not the
reason to stop.

**The cell, as the COO proposed it and this seat confirms:** work the placeholder population the way the 351 were
worked -- resolve every row where the `{system}`/`{scope}`/`{cadence}` substitution is MEASURED from a declared source,
card the rest with owner and reason, print `resolved + carded == 1411` with its denominator, and re-run `AC3` against
that. Same fence guard, same 25-over-count timebox (R-33). **And one addition: the 1411 is a count at ONE vintage of a
report that the campaign itself changes. The cell re-measures its own denominator at write time and prints both** --
the population it started from and the population at close -- because a row can leave the placeholder class while the
cell runs, and an inherited count is a subset measurement.

`W1-S29` disarm ACCEPTED as the COO reported it, and its self-correction is the substance: `c23-mint-basis` could not
see a `systems.json` mint at all (25 rows read as 0), demanded fields `RES_FIELDS` does not carry, and FAILED on zero
mints -- a bar R-32 never set. Repaired @`6876b0b526`, 43 of 43 with planted GREEN and RED arms, and `EN-h-24`'s three
real mints then exercised the repaired arm for the first time. A tool that fails on an empty input is the failure mode
R-32 was written against, and the seat that built it found it.

Round 4 goes to `3.0.0_SA_CVO` for L8/L9 with judgment criteria `C23R4-AC5`, `H24R4-AC4`, `D26R4-AC4`, `G27R4-AC3`,
`S25R4-AC4`. **CORRECTION, 2026-09-18 ~00:2xZ:** this ruling first named `S25R4-AC5`, WHICH DOES NOT EXIST. `2.0.0_SA_COO~G`'s drain-end message listed it and this seat restated the list without checking it against the orders -- a handed list re-typed as if verified. Found by `3.0.0_SA_CVO` during round 4's L8/L9 and confirmed here on a different instrument: parsing the five round-4 order files, **20 criteria are declared and exactly 5 carry `judgment="true"`** -- `C23R4-AC5`, `H24R4-AC4`, `D26R4-AC4`, `G27R4-AC3` and `S25R4-AC4`. Four of the five ids were right; the fifth was not, and the cell it belongs to is the one order still PENDING, so the wrong id pointed the adjudicator at nothing on exactly the cell that needed judging. **L10's order is load-bearing: round 5 is cut AFTER round 4's slug, never beside it** (LD-0521 -- the
refuser counts open orders per PROJECT, so a round-5 issuance opened before round 4's slug deadlocks round 4's L10
until round 5 fully drains). `EN-s-25` stays PENDING on `S25R4-AC3` alone and that is the correct state to slug from.

---

## R-39 -- the `security` token collision (row W1-S30, this seat's): BOTH groups stay CARDED with the collision as the reason, and the vocabulary is NOT reshaped for one instance

**Row:** `LGIC_ENFORCE-W1-S30`, ARMED, disarm owner `1.0.0_SA_CTO`, surfaced by `0.9.0_WK_LGIC_ENFORCE~1` and GROUNDED.
The token `security` names TWO differently-owned live systems: D12's `NFRA_OPSEC202609` evidence and access-log buckets
(`infra/aws/terraform/opsec/s3_evidence.tf:1-3`, `s3_access_logs.tf:1-3`, a CURRENT `DIRECTIVES.yaml` member at `:485`)
and `NFRA_TERRAFORM`'s security-sweep tooling (`infra/aws/terraform/security-ops/main.tf:1-8`), whose project is CLOSED
with 0 hits in `DIRECTIVES.yaml`. `lib/opal_naming.py` `_system_of` (`:1087-1093`) keys purely on the token, so one
`systems.json` row would resolve BOTH groups and attribute the second to whichever owner it names.

**RULING: three parts, and none of them is a mint.**
1. **`security` is NOT minted in `systems.json`.** Minting it would misattribute one of two groups no matter which
   owner the row carries -- the worker's reading is exact and the evidence is per-line.
2. **Both groups stay CARDED, and the card's REASON changes.** Today `opal-data-security[-access-logs]` is carded as
   though it lacked an owner; it has a genuine, citable directive owner and is carded for a DIFFERENT reason --
   `TOKEN_COLLISION`: two differently-owned systems share one token and the vocabulary cannot express the split. A card
   whose stated reason is wrong is worse than a card, because it retires the question. The card names D12 /
   `NFRA_OPSEC202609` as the owner of the bucket half and states that the blocker is the vocabulary, not the ownership.
3. **The vocabulary is NOT reshaped for one measured collision (YAGNI, build ladder rung 1).** A per-context or
   per-resource-type split of `systems.json` is a real answer to a real problem and it is a SCHEMA question that
   belongs to LGIC_NAMING, raised there by this seat with this row as its evidence -- never a rider on LGIC_ENFORCE
   (the same boundary C3 draws in both D9 PRDs today). **It becomes justified on the SECOND measured collision**, and
   the card above is what makes that second instance findable: a census of `TOKEN_COLLISION` cards is one grep, where a
   census of "tokens that would misattribute if minted" is not a question anyone can ask.

**Not ruled here, deliberately:** whether `security-sweep-*`'s resources should be renamed out of the collision. They
belong to a CLOSED project, and R19 says an existing surface reaches conformance through its own migration, never as a
rider on unrelated work. If LGIC_NAMING's schema answer makes the rename unnecessary, it is never done at all.

The row disarms on the card's reason landing with its owner, which is a `LGIC_ENFORCE` cell's act inside its registry
grant -- this ruling is its EVIDENCE, not its disposition. Prose disarms nothing.


---

## R-40 -- a criterion that verifies A RUN binds to THAT RUN'S OWN IDENTITY, because tonight the same wrong-object class landed THREE times in three projects

**Not a call -- a standing bar, issued on three measured instances in one evening.** All three are the same shape: a
check PASSED while pointing at an object that was not the one it claimed to grade, and **every one was caught by a
SECOND SEAT, never by the author.**

| # | instance | what the check pointed at | who caught it |
|---|---|---|---|
| 1 | `LGIC_ENFORCE` round 4, ruling R-38 and msg 97695 (THIS SEAT'S) | judgment criterion `S25R4-AC5`, which occurs in no order file; the real one is `S25R4-AC4`. **Both sets have five members, so it survives a count check** | `3.0.0_SA_CVO`, by parsing the orders instead of trusting the message |
| 2 | `LGIC_ENFORCE` S61, `EN-h-24` row 2 | a quoted phrase attributed to `org/projects/ADVI_HISTBF.json` that has not been in that file since 2026-05-04; it lives verbatim in the sibling `ADVI_JWTRES.json`, 1 of 464 files. **A grep for the quote returns ONE CLEAN HIT on the wrong file** | `3.0.0_SA_CVO`, by printing the bytes at the cited span |
| 3 | `LGIC_LGCTFM` S3, `X1R1-AC1` | `LT-x-1`'s run directory, whose four graded files were ADDED by `LT-e-4`'s later commit -- so the criterion reads PASS **on bytes `LT-x-1`'s run did not produce**, and `MARK.json`, the fifth file, no longer exists on this device, so `X1R1-AC2` is not reproducible at all | `2.0.0_SA_COO~G`, on its own work, disclosed unprompted |

**THE COMMON MECHANISM: every one of these checks named its object by a LABEL that something else could later satisfy**
-- an id typed into a message, a phrase quoted from a file, a path to a directory. A label is not an identity. Rule 22's
GRAIN axis says the object read must BE the object claimed; these all passed GRAIN's wording while failing its intent,
because nothing bound the check to the object's own bytes.

**THE BAR, for any criterion whose subject is a RUN or a produced ARTIFACT:** the proof instance records the artifact's
**CONTENT HASH** (`git hash-object`, or the tool's own digest) beside the run id, and the criterion is graded against
that hash. A later commit that replaces the directory then FAILS the criterion instead of silently satisfying it. Where
the artifact is not committed at all -- `MARK.json`'s case -- the criterion records the hash at production time, so its
disappearance is detectable rather than merely inconvenient.

**COST:** one `git hash-object` per graded artifact, at the cell that produces it. **NON-APPLICATION:** a criterion
whose subject is a repository state at a named commit (the pin IS the identity), and a criterion graded live against a
running system rather than an artifact.

**I am not exempting my own instance from this.** Instance 1 is this seat's, it is the one that would have mis-routed
an adjudication, and the discipline it needed was the cheapest of the three: parse the orders before re-typing a handed
list.

---

## R-41 -- `LGIC_LGCTFM`'s ANDREW_CARD basis is SOUND; the run directory's PROVENANCE is what is defective, and `2.0.0_SA_COO~G`'s reading is CONFIRMED on this seat's own instruments

`2.0.0_SA_COO~G` asked (97740) that this seat TEST its reading rather than take it, which is the correct ask and is why
this ruling exists. **Tested, and it holds.**

| claim | this seat's instrument | result |
|---|---|---|
| the run dir's `contract.json` is byte-identical to the amendment's default-off run | `git hash-object` on all three run dirs | **CONFIRMED**: `84d4d1e62b` in BOTH `20260917T202556Z-bb29248` and `20260917T233115Z-a89fd61`; the flag-on run differs (`95b04ca692`) exactly as it should |
| `MARK.json` is gone | direct listing across every run dir | **CONFIRMED**: absent everywhere |
| the directory's `VINTAGE.json` still declares the OLD run | read the file | **CONFIRMED**: `run_id 20260917T202556Z-bb29248`, `repo_head bb292483994d`, while its contents are the later run's -- **the directory's name and vintage claim one run and its bytes are another's** |
| the substantive DEC-9 mark landed | `git merge-base --is-ancestor 53d59778a1 HEAD` + the commit's own stat | **CONFIRMED**: ancestor TRUE, and the commit carries the `ADVI_FIRMBKTS` s3-prefix row into `infra/logic/registry/remediations.json` |
| both runs read the SAME graph and registry, so the ranking is current | read the vintage fields out of both contracts | **CONFIRMED**: `graph_built 2026-09-17 18:16:22 UTC` and `registry_hash scopes.json sha256:b2a54608f8ebbade` in both; 179 tensions and 184 rows in both; `ranking_rule` identical |

**RULING: the card's ranking is the AMENDED engine's output on the CURRENT graph, and nothing in S3 impeaches it.**
What is defective is the run directory's provenance -- which is real, is S3's subject, and is `2.0.0_SA_COO~G`'s to
remedy under R-40's bar. `X1R1-AC1` must NOT be graded PASS on those bytes: that lane is already refusing its own
complete flip on exactly this ground, which is the correct call and is recorded here as such.

⛔ **THIS RULING DOES NOT ADJUDICATE THE CARD.** The card is with ANDREW, round 1 is not terminal (`LT-x-2` and `LT-x-3`
executing, `LT-x-1` pending by that lane's own refusal), and his ~23:5xZ word makes this seat the adjudicator ONLY on
his unavailability. FWD-4 stays APPLIED until the card is read, by him or, if the round reaches terminal without him,
by this seat -- and the answer is RECORDED either way. **A ruling that the card's BASIS is sound is not a ruling on the
card's QUESTION**, and collapsing those two would be this seat answering something reserved to him while he is simply
asleep.


---

## R-42 -- a `disarm_owner` is a SEAT, never a CELL, an ORDER or a CONDITION

**Found by `3.0.0_SA_CVO` in IRPT_BCKEND's round-2 L9 (slug 97752):** rows `W4-S25` and `W4-S28` both name the CELL
`IB-rtb-1` as `disarm_owner`. That cell went terminal and closed without touching either row -- 0 occurrences of each
id in its instance, verified. **R-19 says the CVO writes a clock on an OWNER'S WORD, and a cell cannot give a word.**
So the moment the cell ended, both rows became unownable, and NOTHING NOTICED: no gate refuses a row whose owner has
ceased to exist, because the field was populated and looked fine.

**RULING: `disarm_owner` holds a SEAT SERIAL and nothing else.** A cell is a unit of work with an end; an owner is an
addressee that outlives the work. A condition ("when the served hash matches the built zip") is the DISARM ACT and
belongs in the row's remedy, not in the owner field -- both of these rows carried a condition there, which is how the
defect hid: the field read as informative rather than as wrong.

**The two rows are PLACED on `2.0.0_SA_COO~B`**, the live lane holding that project, which may re-place either on a
seat it prefers. **An orphaned ARMED row is worse than an unowned one**: it is armed, it looks owned, and it waits
forever.

**COST: none -- it is a field-value rule.** **NON-APPLICATION: a row already owned by a live serial**, and the `ANY`
lane convention on a surprise channel, where the seat that sees a row may append to it.

⛔ **AND THE GENERAL SHAPE, which is R-40's sibling in the OWNERSHIP plane rather than the CITATION plane: a reference
to something that can END is not an owner.** R-40 says a label is not an identity; this says an ephemeron is not an
addressee. Both fail the same way -- the field is populated, every check passes, and the thing it points at is gone.


---

## R-43 -- where a PRD and a DECOMPOSITION disagree about a gate, the PRD is the AUTHORITY and the decomposition is the STALE COPY; and an amendment that LIFTS a gate must name that gate's carriers

**Found by `2.0.0_SA_COO~G` (@`a0a63bcc1a`), on its own law-file clause, and it is this seat's defect that it found.**
`LGIC_CANON_DECOMP.md` says in FOUR places that `C6` **STAYS NOT CUT** on Andrew's `G-N` word and on
`ADVI_FIRMBKTS`'s router repoint. **BOTH HOLDS ARE LIFTED IN THE PRD AND NEITHER LIFT REACHED THE DECOMPOSITION.** The
PRD is ADMITTED at v1.7; the decomposition was last cut against v1.5.

⛔ **THE NEAR-MISS IS THE LESSON, and it is that lane's to be credited with:** reading the DECOMPOSITION first, it
drafted the OPPOSITE claim into `org/XXX.md` -- that an unlifted Andrew gate held `C6` -- **which would have parked the
project on a hold Andrew had already released, in the file every seat reads at startup.** It caught its own sentence by
verifying it at the bytes before committing, not by re-reading it.

**RULING 1: the PRD is the authority.** It is the ADMITTED artifact, both halves signed and hash-bound; the
decomposition is cut FROM it and is a derived copy. A derived copy that contradicts its source about a GATE is stale by
construction, and the direction of the correction is never in doubt.

**RULING 2, and this is the part that is mine:** an amendment that LIFTS a gate **names that gate's carriers in the
amendment itself, with a denominator.** When this seat amended `LGIC_CANON` to v1.6/v1.7 and issued R-34, it changed a
GATE and censused nothing.

**MEASURED, after the fact, over 1087 files under three roots:**

| token | files carrying it | inside LGIC_CANON |
|---|---|---|
| `G-N` (the gate) | **22** | 12 task orders, the decomposition, the PRD, 3 round analyses, the project row, an adjudication |
| `ADVI_FIRMBKTS` (the second hold) | **47** | -- |
| **`R-34` (the LIFT)** | **6** | **2** -- the PRD and the project row |

**The gate propagated to 22 carriers and its lift reached 2 of them.** That asymmetry IS the defect, and it is exactly
the shape `feedback_census_every_carrier_of_a_contract_before_amending_one` names.

**THE REMEDY IS ONE DOCUMENT, NOT A SWEEP -- and the discrimination matters more than the count.** Of the 22 carriers,
**every task order mentioning `G-N` reads `complete`** (12 of 12, measured). A completed order is FROZEN HISTORY and is
CORRECT at its vintage: a round-1 analysis SHOULD say what was true in round 1, and rewriting it would be falsifying a
record. **Only a carrier read as CURRENT DIRECTION can be stale**, and exactly one qualifies: the DECOMPOSITION
(`G-N` x11, `ADVI_FIRMBKTS` x6, **`R-34` x0, `CARDED` x0**). `2.0.0_SA_COO~G` has already committed to correcting it in
`LGIC_CANON`'s L5 re-cut (v6) when `LGIC_LGCTFM` round 1 goes terminal, which is the right cut and the right seat.

⛔ **SO THE BAR IS NOT "UPDATE EVERY FILE THAT MENTIONS THE GATE" -- that would corrupt the record.** It is: **when a
gate is lifted, enumerate its carriers with the denominator printed, then correct the ones read as CURRENT DIRECTION
and leave the frozen ones alone, saying which is which.** A census that cannot tell a live carrier from a historical
one produces either a silent miss or a falsified history, and both were reachable here.

**COST:** one token census per gate lift. **NON-APPLICATION:** an amendment that does not move a gate.


---

## R-44 -- the 49 Financial directory build runs under a 49 FINANCIAL PRINCIPAL; the bucket-policy exception is REFUSED by a NEVER line, and holding is refused by Rule 27

**Call:** `2.0.0_SA_COO~B`, drive tick 5 (97785-class), IRPT_BCKEND. **DISCLOSURE FIRST: this call reached this seat
at ~01:49Z and was not answered until ~02:5xZ -- roughly an hour parked at my desk while that lane kept working.** The
lane did everything right: it carried a rec, named its alternatives, and explicitly said the lane keeps moving
meanwhile. The delay is mine, and it is the exact failure Andrew's 2026-09-17 routing law exists to prevent.

**The fork.** FWD-1 and FWD-7 need three firms' directories. Two can be built by the shared `mdpf` host (grants landed
09-12). The third CANNOT be built by ANY `role/mdpf-*` principal, because `opal-data-49financial`'s
`DenyForeignFirmPrincipals` denies that prefix (`iam.tf:598-603`) -- a control this seat itself confirmed at msg 96105.

**RULING: (a), the lane's own rec.** The 49 Financial build runs under a **49 Financial principal**, assumed by the
dispatch for that firm only, reading only that firm's dimensions and writing only that firm's directory prefix; the
other two firms keep the host role.

**Why the alternatives are not merely worse -- they are refused by standing law:**
- **(b) a bucket-policy exception for one `mdpf` role: REFUSED.** CLAUDE.md's NEVER -- *never reference another firm's
  data from a pipeline tree, BUCKET or KEY-PREFIX* -- and the same line's warning that **the guard is only as wide as
  its enumeration.** Carving an exception into `DenyForeignFirmPrincipals` is not a workaround for the control; it IS
  the widening the control exists to refuse. The lane recommended against it for exactly this reason and is right.
- **(c) hold FWD-1/FWD-7 at 2 of 3 until `ADVI_FIRMBKTS`: REFUSED.** `ADVI_FIRMBKTS` is `dep_stage: PRD` with no lane.
  That is a WAIT, and Rule 27's L2 clause is explicit that no FWD is a wait -- the mechanism is driven deliberately.
- **(a) is the cross-firm law's OWN SHAPE**: the firm's data under the firm's principal. It does not widen a deny, it
  does not wait, and it is exercisable on demand once the role exists.

**THREE CONDITIONS ON (a), and the third is the one that makes it falsifiable:**
1. **The role name is BUILDER OUTPUT (Rule 30)** -- `name(<registry key>, ..., kind="role")`, never typed, and the PRD
   cites the builder's output rather than promising it.
2. **The IAM apply is a never-widen-class act.** The sign-off names the BLAST RADIUS -- what the role may touch and the
   rollback per key -- not the producer's intention. Ledger entry opened at start, closed at completion.
3. **A NEGATIVE CONTROL ON THE NEW ROLE, not only a positive one.** It is not enough that the new principal CAN read
   49 Financial's dimensions and write its directory prefix. The cell must also show it CANNOT read another firm's
   prefix -- an attempted read that is DENIED -- and that its name does not match the denied prefixes. **A principal
   proven only by what it can do has not been shown to be fenced**, and a fence is the entire reason this option beats
   (b). Count the WRITERS of the 49 Financial directory prefix while you are there: a second writer makes "this role
   writes it" an incomplete account.

It is an addendum or a round-4 cell with the IAM apply under sign-off; nothing in round 3 assumes it, which is the
correct posture and is why round 3 was right to cut without it.

---

## R-45 -- the bundle's SHAPE: member-level DISTRIBUTION flag plus a REPO-SHAPED unpack, and the flag's own hazard gets a control

**Call:** `2.0.0_SA_COO~B`, drive tick 8, on `0.4.0_DS_ClientPlatform~X`'s rows S57/S58/S59, measured with the guard's
own functions at `e9dc18f302`. Two halves that are one decision:

1. **Declaring the three per-firm `runner_common.py` as bundle members would FREEZE three live production deploy legs.**
   The guard's X-iii routing puts a bundle member in `triggered`, never `loose`; all three are served today on their
   own firms' loose legs with `ETag == repo md5`. A commit would re-mint the IRPT tarball and **leave the firm's served
   module stale while reading green.**
2. **Even a complete closure aboard the bundle cannot reach the runner through the DEPLOYED dispatch.**
   `refresh.runner_script` (`refresh.py:430-443`) unpacks into the runner's own directory and relocates exactly three
   FLAT names, while `directory_runner` resolves at repo-relative depth; a `..` member makes GNU tar exit 2 into the
   dispatch's `|| exit 91`. Measured on one 9-member payload: declared placement IMPORT-OK **3 of 3**; the dispatch's
   own unpack **0 of 3**.

**RULING: the REC is adopted -- a member-level DISTRIBUTION flag (the member keeps its loose leg AND a commit to it
also re-mints the bundle) plus a REPO-SHAPED unpack (members named by repo path, extracted at `$W`).** One authority
per file, one routing mechanism, and the dispatch reaches what the runner derives. Alternative (2) -- the host fetching
each firm's module from its served loose key at build time -- **meets the cross-firm bound first** and collides with
R-44's own subject; alternative (3), a repo checkout at the runner's depth, is heavier and contradicts `W2-S51`'s
finding that the remedy is a SHAPE, not a member list.

⛔ **THE ADDED CONTROL, because the flag creates the hazard it removes, one level over.** A distribution member now has
**TWO deploy legs per commit.** If one lands and the other does not, the result is precisely the divergence the flag
exists to prevent -- a served module out of step with the bundle, reading green on whichever leg is inspected. So the
cell carries a CONSISTENCY criterion graded after a real commit: **the served loose object's `ETag` equals the repo
md5 AND the bundle's member bytes equal the repo bytes**, with a **MUTANT that advances only ONE leg and must FAIL
it.** A flag that routes to two places is only as good as the check that both arrived.

`S58`'s two closure members outside the face's member globs (`data/firm_registry.json`,
`_contracts/DirectoryEntry.schema.json`) are that lane's L6 call to admit, as it proposed -- the bundle already carries
one such member under amendment H3, so the precedent is the lane's own and needs no ruling from here.

On the word, `IB-rtc-2` (guard flag + declaration + re-mint) and `IB-rtc-3` (`refresh.py`'s unpack, a code-home change
that becomes a build+deploy cell under ledger) re-cut in the same issuance. **Both FWD-1 and FWD-7's `inf` and `cot`
thirds become exercisable on this ruling, with no dependency on `ADVI_FIRMBKTS`** -- which is the lane's point and the
reason holding was never the cheap option.
