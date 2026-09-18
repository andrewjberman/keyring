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


---

## R-46 -- when one row id lives in several documents, the REMEDIATION row governs its standing ONLY IF it carries a real disposition; INERT alone is not a close

**Call:** raised by `2.0.0_SA_COO~G` (97809) out of the 57-vs-54 reconciliation, and explicitly NOT ruled by it --
"it is doctrine and it changes what the sweep is FOR". Three rows read **ARMED in `INVESTIGATION_v1.md` and INERT in
`REMEDIATION_v2.md` at the same time**: `W1-S29`, `W2-S12`, `W3-S10`.

**THE RECONCILIATION FIRST, because it is the model for how a count disagreement should end.** That lane REPRODUCED
ITS OWN BROKEN METHOD deliberately and watched it return exactly 54 -- proving the defect rather than arguing it. The
cause: a dict keyed by row id, so an id in several documents kept only the LAST one read, and sorted paths put
`REMEDIATION` last. It also confirmed the multi-owner guess: `W2-S12` names `disarm_owner 0.7.0_AE_CloudOps` in the
investigation and `owner 1.0.0_SA_CTO` in the remediation -- **one row, two different owners in two documents** -- and
its reader never read the top-level `owner` at all, **the field R-42 had established as an addressee forty minutes
earlier.** Its distinct-id count with the owner split is 57 / 46 / 8 / 2 / 1, identical to this seat's. Two
instruments, two seats, one answer.

**RULING, and it is PER-ROW rather than a class rule -- which is the whole point:**

**The governing carrier of `hazard_standing` for an id present in several documents is the REMEDIATION row, BUT ONLY
WHERE THAT ROW CARRIES A REAL DISPOSITION** -- `remediation.state == REMEDIATED`, or a `disarm` block with
`state == DISARMED` AND an `at`. The estate's own reading is why: **ARMED is a CLOCK on a remediation row and a LABEL
anywhere else**, and GRADUATED is a TRANSFER rather than a close. A remediation row that carries the clock governs the
standing; an investigation row's ARMED is the record of what the finding WAS.

⛔ **`INERT` WITH NO CLOCK BEHIND IT IS NOT A CLOSE -- it is a row whose clock was never set**, and there the
investigation's ARMED STANDS.

**MEASURED ON THE THREE, and they do not split the way either seat guessed:**

| row | remediation row | disarm block | governs? | standing |
|---|---|---|---|---|
| `W1-S29` | `REMEDIATED` | `DISARMED` @ 2026-09-17T23:55Z | YES | **CLOSED** -- the investigation's ARMED is stale bookkeeping |
| `W2-S12` | `REMEDIATED` | `DISARMED` @ 2026-09-17T18:39Z, owner `1.0.0_SA_CTO` | YES | **CLOSED** |
| `W3-S10` | **`OPEN`** | **absent** | **NO** | **STILL ARMED** -- `INERT` here is a label with no clock behind it |

**So the population needing work is 55 -- not 54 and not 57.** `2.0.0_SA_COO~G`'s instinct ("nearer 54 than 57") was
directionally right and **would have closed one row too many**: a blanket "the remediation document governs" rule
silently closes `W3-S10` while its remediation is OPEN. ⛔ **THAT IS WHY THE RULE IS PER-ROW AND CARRIES A DISPOSITION
TEST, and it is the second time tonight a rule that was right in direction would have been wrong applied as a class**
(the other being R-43's "update every carrier", which would have falsified frozen history).

**AND A NUMBER WITHOUT ITS METHOD IS NOT A MEASUREMENT.** The same channel yields **92** ARMED OCCURRENCES and **57**
distinct ids with at least one armed occurrence. "57 ARMED" is only meaningful carrying "distinct ids, >= 1 armed
occurrence, `hazard_standing` string equality at top level". The sweep prints its predicate, its owner-resolution order
and its occurrence-vs-distinct choice BEFORE its count -- which is R-38's clause and now has a measured reason.

**A CORRECTION OF MY OWN, made here rather than left standing:** I flagged `W2-S12` to `0.0.0_AB_MSTR` as a SEATING
question because its investigation row names a seat that is not live. **That row is CLOSED on the remediation plane --
`REMEDIATED` and `DISARMED` at 18:39Z under `1.0.0_SA_CTO`.** It needs no live `0.7.0_AE_CloudOps` seat and I should
not have raised it as one; what remains is the DUAL-OWNER shape itself, which is a finding about the channel rather
than a hazard about that row. `2.0.0_SA_COO~G` was right to decline to re-own it and right that leaving it visible was
better than adopting it.


### R-46 CORRECTION (2026-09-18 ~03:5xZ): the RULE stands, the NUMBER was wrong -- 43, not 55

**`2.0.0_SA_COO~G` (97815) implemented R-46's predicate from the RULING TEXT rather than from its answer -- explicitly
because "two seats agreeing is not corroboration when the second takes the first's reasoning" -- and applied it to the
WHOLE population. RE-RUN INDEPENDENTLY HERE, from the ruling's text, and every figure matches:**

| | lane's | this seat's re-run |
|---|---|---|
| row occurrences / distinct ids | 275 / 183 | **275 / 183** |
| ids with >= 1 ARMED occurrence | 57 | **57** |
| CLOSED BY A CLOCK | 14 | **14** |
| **STILL ARMED** | **43** | **43** |
| owners of the 43 | 35 `~G` / 7 CTO / 1 CVO | **35 / 7 / 1** |
| where the 14 clocks live | `REMEDIATION_v1` 10, `v2` 4, adjudication 0 | **identical** |

**My 55 was wrong and the error was mine: I applied R-46's disposition test to the THREE rows under discussion and
left the other 54 at their investigation-row standing.** Twelve more ids carry a closing clock -- `S46`, `S52`,
`W1-S14`, `W1-S17`, `W1-S19`, `W1-S20`, `W1-S22`, `W1-S3`, `W3-S6`, `W4-S1`, `W5-S3`, `W5-S4` -- **dated 2026-09-14,
-15 and -16, days old, not tonight's.** The per-row verdicts in R-46 are unchanged and correct; only the population the
test ran over was too small.

⛔ **THE SHAPE, AND IT IS NOW MINE BECAUSE I NAMED IT TWICE AND THEN COMMITTED IT: A RULE THAT IS RIGHT IN DIRECTION,
APPLIED TO A SUBSET RATHER THAN TO ITS WHOLE POPULATION.** Three instances tonight, three different seats:
- R-43's "update every carrier" -- would have falsified frozen history, until it was scoped to LIVE carriers only.
- the lane's "nearer 54 than 57" -- would have closed `W3-S10`, whose remediation is OPEN.
- **R-46's disposition test applied to 3 of 57** -- leaves twelve closed rows counted as open.

**It is the tempting version every time BECAUSE THE SUBSET IS THE PART YOU ARE LOOKING AT.** The discipline is not "be
careful"; it is: when a rule is written against the rows in front of you, RUN IT OVER THE POPULATION BEFORE QUOTING A
NUMBER FROM IT.

**And why it is not bookkeeping:** a sweep graded on 55 would demand a disarm-or-restate on twelve rows a clock closed
days ago -- **putting a RESTATED REASON on properly closed rows, which is the opposite of the sweep's purpose and makes
the channel less readable, not more.**

**The lane stated its own debt falling 43 -> 35 IN THE SAME BREATH as the correction, named that the arithmetic helps
it more than anyone, and asked to be re-run rather than believed.** That is the reason this correction is trustworthy,
and it is why I re-ran it rather than accepting it.

**ROUND 6'S SWEEP TAKES N = 43** (35 `2.0.0_SA_COO~G` / 7 `1.0.0_SA_CTO` / 1 `3.0.0_SA_CVO`), re-measured at the cell's
own write time per R-38, with the predicate, the owner-resolution order and the occurrence-vs-distinct choice printed
before the count. **My own number is 7, not 8:** `S52` is among the twelve a clock had already closed.


---

## R-47 -- A VACUOUS PASS IS THE DANGEROUS HALF OF A BRANCH-RELATIVE ARM, and the census that finds it CANNOT start from the failures you observed

**Found by `2.0.0_SA_COO~G` (97829), as a CORRECTION TO `3.0.0_SA_CVO`'s own row `S10` rather than a complaint about
it.** S10 named two branch-relative arms and then asserted the remainder: *"the other twelve re-run clean off-branch
and need nothing."* **That second clause is FALSE for two of the twelve**, and the way it is false is worse than the
defect S10 caught.

An UNSCOPED read of `base_ref()` over `check_lt_r1.py` returns three lines -- the definition at `:147` and **TWO
REMAINING CALLERS**, `x2-flag` at `:1508` and `x3-filed` at `:1567`. Re-run in the shared checkout they do **NOT** read
FALSE FAIL. **THEY READ VACUOUS PASS.** `x2-flag` prints an empty commit window and PASSES -- so it would pass
IDENTICALLY had that cell touched `org/mcp/naming-gate.enforce`. `x3-filed` prints `OPENED tensions 0; ADVI_FIRMBKTS
channel rows added on this branch 0 []` and PASSES on `0 >= 0`.

⛔ **A FALSE FAIL GETS INVESTIGATED. A VACUOUS PASS GETS ACCEPTED.** The two nobody named are the dangerous half,
because the arm that cannot fail is indistinguishable from the arm that passed for the right reason -- and the one
S10 found announces itself.

**THE DISCRIMINATOR WAS A SIBLING ARM, NOT AN ARGUMENT.** `x3-nontrivial` re-run beside `x3-filed` reads
`FAIL-X3-WAVE-MOVED-SOMETHING`, "CLOSED 0 + OPENED 0 = 0", while `x3-two-runs` reads "run directories 5; with
contract.json + VINTAGE.json: 5". **So the zero is not the wave -- it is WHICH PAIR the arm resolved**, because
`_last_two()` picks its subject BY POSITION in a directory five runs now share. **That is R-40's position-resolution
defect, closed in `x1` by the HASHES manifest and STILL LIVE in `x3`** -- the same class surviving in a sibling of the
place it was fixed.

**AND THE PART THAT GENERALISES, WHICH IS WHY THIS IS A RULING AND NOT A NOTE:** `3.0.0_SA_CVO` could not have found
it. That seat's read started from **the failures it OBSERVED while grading** -- the correct instrument for finding a
false FAIL, and **structurally blind to a vacuous PASS**, because a vacuous pass produces no observation to start from.
What found it was an UNSCOPED read of the SHARED MECHANISM both remaining arms call.

⛔ **THIS IS RULE 22's SHARED-DEPENDENCY CLAUSE, MEASURED ON A FINDING RATHER THAN ON A CODEBASE: THE MEMBERS' OWN
LIST IS THE WORST AVAILABLE DOMAIN FOR THE CENSUS, AND IT ARRIVES LOOKING AUTHORITATIVE PRECISELY BECAUSE IT CAME FROM
A REAL FINDING.** A list of defects is a list of what someone could SEE. Census the MECHANISM, not the sightings.

**FOURTH INSTANCE TONIGHT OF THE SUBSET-NOT-POPULATION SHAPE**, and the first where the subset was itself a correct
finding: R-43's carriers, the "nearer 54", R-46's 3-of-57, and now S10's twelve.

**RULING: NOT REPAIRED IN ROUND 1, and the lane's reasoning is adopted whole.** Both arms are FIXED INPUTS of a
CLOSED, GRADED round; on their own branches the windows were NON-empty, so the grades they fed are SOUND and an edit
now moves no grade. **R-43 scopes a frozen-history defect to the live-direction document, never to a sweep.** What is
owed is that `LGIC_LGCTFM` round 2 carries the corrected inputs FROM THE CUT, and **no round-1 arm is re-run as
acceptance for anything.** No round re-opens and nothing is asked of `3.0.0_SA_CVO`.

**THE ONLY CONTROL THAT CATCHES THIS CLASS IS THE POSITIVE-SATISFIABILITY ARM** -- run the checker against a SIMULATED
CORRECT RECORD and require PASS -- which round 6's `check_en_r6.py` already drives eight of, against two simulated
correct records. ⛔ **A MUTANT TEST CANNOT CATCH A VACUOUS PASS**: the mutant proves the arm can FAIL, and a vacuous
arm fails the mutant happily while passing everything real. The two controls are not redundant and must both exist.

---

## R-48 -- a seat's ROSTER SUMMARY is a live claim about the fabric, and mine advertised a false block for a whole night

`2.0.0_SA_COO~G` closed 97829 by reading THIS SEAT'S OWN registered summary and finding it said:

> BLOCKED: LGIC waits on a COO~G seat (asked `0.0.0_AB_MSTR`)

**It has said that all night while `2.0.0_SA_COO~G` was live and closed four rounds.** The lane put it exactly right:
*"If that summary is stale it costs nothing; if a real gate is being held open against a seat that does not need
seating, it is holding LGIC for no reason, and `1.0.0_SA_CTO` is the only seat that can tell which."*

**IT WAS STALE, AND IT IS MINE.** Corrected at this tick. The defect is not the wrong words -- it is that **a summary
is READ BY OTHER SEATS AS CURRENT STATE and by `0.0.0_AB_MSTR` as a seating obligation**, and nothing in the estate
grades it: no gate refuses a stale summary, no census counts one, and the seat that wrote it is the last to re-read it.
⛔ **EVERY DEFECT CLASS TONIGHT HAS THE SAME SPINE -- A CARRIER NOBODY RE-READS: a stale citation, a wrong credit, a
row whose premise moved, an unpinned card, and now a roster line.**

**THE BAR, and it is cheap:** a seat that reports a BLOCK in its summary re-reads that summary whenever it reports the
block resolved anywhere else. This seat said "not blocked" in messages and analyses for hours while its own roster line
said otherwise, and **the roster is what a seat reads when it does not have the messages.**

---

## R-49 -- DEC-9 ADMITS NO PREFIX AT ALL, so `LGIC_LGCTFM-W2-S3`'s question has no answer: it is a category error, and the row DISARMS on that

`2.0.0_SA_COO~G` routed this as an open call with its recommendation in the same act (msg 97836). Under the
call-routing law (Andrew-direct 2026-09-17 ~13:0xZ) **any open call is the driver's to decide on its own rec the same
tick**, and this one is additionally mine by lane: DEC-9 lives in `LGIC_LGCTFM_PRD.md`, and the PRD is the CTO's.

**THE ROW ASKS:** a second DECIDED-but-unmarked prefix (`opal-data-bd/silver/`, `infra/logic/06_CONFORMANCE_LEDGER.md:72`)
sits on the same bucket with the same evidentiary shape DEC-9 accepted for `gold/`, and *"whether DEC-9's acceptance
EXTENDS to a second prefix is a decision no one has made."*

**RULING: there is nothing to extend, because DEC-9 never admitted a prefix.** Read at its own bytes rather than from
the row's characterisation -- `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md:246`:

> **DEC-9 The mark act appends to the three existing registries only, under the subject's migration project, in the
> run's own commit, through `safe-commit` and the naming gate.** ... A fourth mark is a Rule 24 act nobody has asked for.

DEC-9's axis is **WHICH REGISTRIES THE MARK ACT MAY WRITE** -- three, and no fourth. It does not enumerate prefixes,
and `gold/` is not named in it. Unscoped read of `DEC-9` over the PRD: **6 occurrences** (`:60`, `:178`, `:246`, `:356`,
`:368`, `:377`); none names a prefix. `gold/` was simply the prefix a cell reached first. **So "does the acceptance
extend to a second prefix" presupposes a prefix admission that does not exist**, and answering it either way would
have MINTED that admission by implication. `2.0.0_SA_COO~G`'s reading is correct and is adopted.

⛔ **THE GENERAL FORM, and it is the night's shape inverted:** every other instance tonight was a rule applied to a
SUBSET of its population. **This is a rule read as having a population it never had.** Both come from taking a
decision's SCOPE from where it was first exercised rather than from its own text. The remedy is the same one: read the
decision's bytes, not the record of its first application.

**W2-S3 DISARMS on this ruling** -- it named a decision nobody had made, and the decision is now made. This seat is its
`disarm_owner`, so this is the owner's word; the CLOCK stays `3.0.0_SA_CVO`'s, and no `adjudicates` is carried.
It was the last open id on composite `C-S3`.

---

## R-50 -- the markable population is `DECIDED` **AND** `MIGRATE` -- SEVEN of eleven, not eleven; the rec censused the right file on the WRONG COLUMN

`2.0.0_SA_COO~G` was right to refuse to answer the row as asked and to hand me a population instead of a sighting --
*"Census the mechanism, not the sighting. I would rather hand you the eleven than the one."* **That instinct is R-47 one
level up and it is correct.** But the census reads one column too far left, and I am ruling against the rec's number.

**MEASURED, on a different instrument than the lane's** (mine admits header and legend rows, so the denominators differ
by construction and are printed rather than reconciled): `infra/logic/06_CONFORMANCE_LEDGER.md`, **261 lines**;
**102** pipe-table rows detected; **73 DECIDED**, 29 not. The lane's detector saw 76 body rows / 64 DECIDED. **Neither
number is the markable set, and that is the finding.**

**THE LEDGER'S OWN HEADER, `:68`, NAMES TWO COLUMNS:**

> `| bucket · plane | objects | newest | rules | disposition | decided |`

`decided` answers **"has a word been given on this row?"**. `disposition` answers **"what happens to this surface?"**.
They are different axes, and the mark act needs the second. **The rec censused `decided`.**

**THE ELEVEN `opal-data-bd` ROWS, `:70-:80`, BY DISPOSITION:**

| disposition | n | lines |
|---|---|---|
| **MIGRATE** | **7** | `:70` platinum/, `:71` gold/, `:72` silver/, `:73` schwab/silver/, `:75` bronze/, `:76` smartx/bronze/, `:79` gold/_state+_parity+manifests |
| RETIRE | 3 | `:74` canonical/schwab/, `:77` schwab/bronze/, `:80` logs/gold/ |
| CONFORMANT IN PRINCIPLE | 1 | `:78` code/ |

**DECIDED 11 of 11. MIGRATE 7 of 11.** All three registries DEC-9 names describe **a surface that MOVES** --
`remediations.json` surface kinds `bucket-alias` and `s3-prefix`, `LEGACY_SERVED_PATHS.json` served paths, `scopes.json`
`bucket_aliases`. **A RETIRE row has nothing to alias to; a CONFORMANT row is already at its home.** Marking those four
would write four rows asserting a destination the ledger does not give them.

⛔ **RULE 24 (iii), INTENT COHERENCE, IS THE TEST THAT SEPARATES THEM:** one axis, one intent. `decided` is a
PROCESS-STATE column (is a word owed?); `disposition` is an OUTCOME column (does this move?). **A census that selects
on process-state and acts on outcome is reading a schema across two axes**, and it passes every count check because
both columns are populated on every row. The lane's own exclusion work was real and correct -- it printed the 12
not-DECIDED rows and flagged that three are WAITING ON ANDREW -- **but a correct subtraction on the wrong axis is still
the wrong set**, and it arrives looking measured because the denominator is real.

**MARKABLE ON THIS BUCKET: the seven at `:70`, `:71`, `:72`, `:73`, `:75`, `:76`, `:79`.** `silver/` (`:72`) IS among
them, so the row's practical ask is granted -- by the mechanism, not by an extension of DEC-9.

**WHAT THIS RULING DOES NOT MOVE, stated because Rule 24 (iv) requires it:** the three `opal-data-etfs` rows at
`:106-:108` read **WAITING (Andrew)** and are untouched -- no ruling of mine reaches them. The two `OWED` register
entries `X3`/`X5` (`:137`, `:139`) name Andrew as decider and are untouched.

⚠ **AND ONE EXCLUSION IS RULED BUT NOT MEASURED, disclosed rather than smoothed.** I tried to falsify the RETIRE
exclusion against `LEGACY_SERVED_PATHS.json` -- if a retiring prefix still carried a served path, it would need a mark
after all. **The positive control DID NOT FIRE**: zero hits for the three RETIRE prefixes AND zero for all seven
ADMITTED ones, so the instrument discriminated nothing. Reading the file's real shape showed why -- it is
`mapping`, **8 rows** of `{path, reason}`, and its paths are **BUCKET-RELATIVE** (`platinum/advi/{firm}/{leaf} ...`),
so a search for `opal-data-bd` was the **WRONG GRAIN** and could only ever return zero. **The RETIRE exclusion
therefore rests on the disposition axis alone and is NOT independently corroborated.** It is ruled, and it is open to
one measurement nobody has taken: whether any of the three retiring prefixes is still served. **Owner: the
`ADVI_FIRMBKTS` migration project at its mark act**, which is the first cell that can measure it against a live read.

⭐ **The positive control is the only reason I know that zero was empty rather than clean** -- and I had written R-47
about exactly this four hours earlier, which did not stop me running the wrong-grain search. **A lesson you have
written down is not a control; the control is the arm you run beside the answer.**

---

## R-50 CORRECTION -- I named the WRONG KEY in my own disclosure, and the true answer is STRONGER than the one I disclosed: the RETIRE exclusion is not un-corroborated, it is UNFALSIFIABLE BY THAT FILE

`2.0.0_SA_COO~G` took the measurement R-50 said nobody had taken (msg 97839) instead of accepting the open item. Two
things come back, and **one of them is a defect in my own committed text.**

**THE DEFECT, MINE.** R-50 and row `LGIC_LGCTFM-S20` both say `LEGACY_SERVED_PATHS.json` "is `mapping`, **8 rows** of
`{path, reason}`, and its paths are BUCKET-RELATIVE". **That names the wrong key.** Measured at the file's own shape:

| key | type | n |
|---|---|---|
| `paths` | list of **str** | **39** -- these ARE the served paths |
| `excluded` | list of dict `{path, reason}` | 8 -- what I reported |
| `mapping` | dict | 6 route templates -- the key I named |

⛔ **AND THE MECHANISM IS THE PART WORTH KEEPING, because my FIRST read was RIGHT AND I OVERWROTE IT WITH A WRONG ONE.**
The falsifier printed `served-path rows: 39` -- correct, from `d.get("paths")`. The follow-up "characterize the file"
read used a generic *first list-of-dicts* heuristic, which **skips `paths` precisely because it is a list of STRINGS**
and lands on `excluded`. **A heuristic written to be robust selected the wrong object, and because it ran SECOND it is
the number that reached the record.** The later read was not more careful; it was more generic. **A second look is not
automatically a better look, and when it disagrees with the first, that is a finding to resolve, not a refresh.**

**THE SUBSTANTIVE ANSWER, and it strengthens R-50 rather than disturbing it.** The grain was real but it was never the
reason. That file cannot answer the question **at any grain**, twice over, and `2.0.0_SA_COO~G` measured both:

1. **ITS TIER DOMAIN EXCLUDES EVERY PREFIX IN QUESTION.** Its title scopes it to *"every served path below
   `{source}/{scope}/platinum/` that the frozen portal requests"*. Over its own denominator of 39, re-measured here on
   my instrument: **`platinum` 39 of 39, and ZERO paths without it.** The three RETIRE prefixes are
   `canonical/schwab/{silver,gold}`, `schwab/bronze/` and `logs/gold/` -- **not one is platinum**, and neither are four
   of my seven ADMITTED ones. **So the positive control was SOUND and the instrument's DOMAIN was wrong** -- which is
   the failure Rule 24 names when the subtraction's domain is not the claim's population, arriving here as a zero.
2. **IT HAS NO BUCKET AXIS AT ALL.** `opal-data-bd` occurs zero times in the file, and its `key_form` says why in its
   own first sentence: each entry is a key template **BELOW THE BUCKET**. So bucket-relative was the right grain **and
   still insufficient.**

⭐ **CONCLUSION, upgraded: the RETIRE exclusion is not merely UN-CORROBORATED by this file -- it is UNFALSIFIABLE BY
IT.** No re-grained search there moves it either way. **So R-50's exclusion stands on the best evidence that exists
rather than on a gap**, and my "open measurement, owner `ADVI_FIRMBKTS`" now carries an INSTRUMENT instead of only an
owner: a live read of the objects under those three prefixes with their newest timestamps, or a portal-source census
below a non-platinum tier -- the census this file's own `census` block records that it did **not** do. Weak
corroboration already sits in the ledger's `newest` column: `:74` 08-18, `:77` 04-08, `:80` 04-01, **30 to 170 days
stale.**

⛔ **AND THE TRAP FOR THE NEXT READER, which is why my zero was the lucky outcome:** a whole-file token count of this
file returns `gold` 3 and `canonical` 2, **all PROSE hits** in the title, `key_form` and `excluded` -- zero in `paths`.
**A grep for a retiring prefix's tier returns NON-ZERO here and reads as a hit.** My wrong-object read produced an
honest zero; a slightly less careful one would have produced a FALSE POSITIVE and corroborated the opposite ruling.

**ONE DISCREPANCY BETWEEN OUR TWO COUNTS, resolved in the lane's favour rather than split.** I measured `canonical` = 1
across the 39 paths where `2.0.0_SA_COO~G` measured 0. The hit is
`advi/{scope}/platinum/firm/advisor_nna_canonical.json` -- **`canonical` in a FILENAME, not the tier segment
`canonical/`.** The lane's claim was about segments and is correct; mine was a substring count and is the loose one.
**The numbers never disagreed; the grains did.**

**R-43 DISPOSITION: row `LGIC_LGCTFM-S20` IS NOT REWRITTEN.** It is a filed row carrying a frozen measurement, and the
correction stands BESIDE it here, in the live-direction document -- the same disposition the lane took on `W1-S6`. The
markable set is unchanged: **the seven at `:70`, `:71`, `:72`, `:73`, `:75`, `:76`, `:79`.**

---

## R-51 -- a PHANTOM ANSWER in a register row is worse than a stale block, and DONE resolves on the PRD's outcome array; NO `completion_test` FIELD IS MINTED

`2.0.0_SA_COO~G` read `org/missions/D14/LGIC/LGIC_ENFORCE/project.json` **because the arm told it to read the register
rather than its recollection**, and found three of the four items in `blocking` stale or wrong (msg 97838). **That row
is MY L3 carrier -- Rule 27 puts it in the CTO's carrier set and says the CTO writes every carrier itself in its own
commit -- so the lane routed it with a recommendation and did not edit it. That is exactly right.** Every claim below
was re-measured on this seat's own instruments before the edit.

| # | the row said | measured | verdict |
|---|---|---|---|
| 1 | CVO holds round 4; round 5 cannot be cut | round 4 closed, round 5 cut AND drained, L10 written @`b683398fda` | **SATISFIED -- struck** |
| 2 | "Round 5's **one cell**" | **FOUR** `-r5` order files: `EN-c-28`, `EN-c-31`, `EN-g-30`, `EN-h-29` | **WRONG ON ITS FACE -- struck** |
| 3 | W1-S30 disarms when the card lands | condition MET; row `S65` is the owner's word; clock open at `3.0.0_SA_CVO` | **reduced to the clock** |
| 4 | W2-S13 "is **answered by round 5**" | `remediation.state` **OPEN**, `disarm.state` ARMED, `disarm.at` **null** | **FALSE -- rewritten** |

⛔ **(4) IS THE ONE THAT MATTERS AND THE LANE NAMED THE ASYMMETRY EXACTLY: a stale BLOCK costs a WAIT; a phantom ANSWER
costs the WORK.** Round 5's `EN-c-28-r5` stopped on the R-33 timebox and **carded the population forward** -- the order
file's own bar is `judged + carded`, and `stopped_on_timebox` is a field it reports. The register converted "carded
forward" into "answered", and a reader who trusts it stops looking. **R-48 said a roster summary is a live claim about
the fabric; this is the same defect one object over, in the carrier the estate treats as authoritative** -- and it was
found only because a COO read the register instead of its own memory of the register.

⚠ **AND THE STALENESS IS NOT EVEN GRADEABLE ON THIS ROW: `LGIC_ENFORCE/project.json` HAS NO `last_updated` KEY AT
ALL** (27 keys, measured; the field is simply absent), while `LGIC_LGCTFM`'s HAS one reading `2026-09-17T14:20:00Z`
**while its own prose cites `@662d53b793` from 02:21Z on the 18th.** ⛔ **Same disease, opposite halves: one row cannot
be checked, the other can be checked and LIES IN THE DIRECTION A READER TRUSTS** -- an old timestamp over fresh text
reads as "nothing has happened since", which is the one inference a timestamp exists to license. Both are repaired in
this seat's own commit; `last_updated` is added to `LGIC_ENFORCE` and corrected on `LGIC_LGCTFM`.

### The second call: what does DONE read from?

The lane reported that **its own stop condition names an instrument that does not exist** -- *"both projects DONE on
the register per the completion test"* -- and censused it unscoped rather than assuming: **`completion` ZERO
occurrences in either `project.json`, `complete_when` zero, `completion_test` zero**, and `done_when` once, as prose
inside an Andrew-direct citation. Re-run here: **confirmed, 0 / 0 / 0 / 1.** It has been reporting "not DONE" from the
PRD's FWD outcomes and **saying so every tick**, which is the correct behaviour for an unfalsifiable stop.

**RULING: the lane's recommendation is ADOPTED VERBATIM, including its refusal.** DONE = **every FWD outcome REALIZED
on the PRD, plus `status` off `active`**. ⛔ **NO `completion_test` FIELD IS MINTED.** The lane's reason is better than
any I would have written and it is the ruling's reason:

> Minting a field so a stop condition has something to read is how a test ends up describing whatever the last round
> happened to do.

⭐ **A STOP CONDITION THAT NAMES A MISSING INSTRUMENT IS FIXED BY RE-POINTING IT AT AN EXISTING OWNED ARTIFACT, NEVER BY
CREATING THE ARTIFACT THE SENTENCE ASSUMED.** The PRD's outcome array already exists, already has an owner (this seat),
and is already what the L10 analyses grade against -- so the sentence resolves mechanically against a thing that was
built to be graded, rather than against a field invented to make a sentence resolve. **COST: none -- it deletes a
field nobody writes. NON-APPLICATION: a project with no PRD outcome array, which cannot reach L4 and so cannot reach
this question.**

---

## R-52 -- THE NO-HALF-LANDED-DEPLOY LEDGER IS INVISIBLE TO EVERY SHARED-TREE READER AT EXACTLY THE MOMENT IT MATTERS, AND MY OWN WATCH PROVED IT BY FAILING

**This ruling is written against my own instrument.** For three ticks I watched the `NFRA_OPLGTW` `OG-r-1` release
cutover -- the night's one world act -- with a check I wrote into the tick-30 log myself:

> `org/critical_paths/.open_deploys/` carried **6 entries and none for this cutover** at log time, which is consistent
> with the worker still being pre-deploy ... and is **NOT yet a finding**. It BECOMES one if the deploy completes with
> no entry ever opened, or if an entry is left open.

⛔ **THE CHECK WAS STRUCTURALLY INCAPABLE OF SEEING THE ENTRY, AND THE ENTRY EXISTED THE WHOLE TIME.** Measured at
tick 32 by listing the SAME path in BOTH trees:

| tree | entries | carries `nfra-oplgtw-og-r-1-first-release.json` |
|---|---|---|
| `CLOUD` (what my watch read) | **7** | **NO** |
| `wk-nfra_oplgtw-2a` (the worker's worktree) | **8** | **YES** |

`0.9.0_WK_NFRA_OPLGTW~2` opened it @`7752ea3bdb` at **05:08:50Z**, with a commit subject that names the discipline it
was obeying: *"opened BEFORE the deploy, per the no-half-landed-deploy discipline."* **The worker did exactly the right
thing and my instrument reported the opposite.**

⛔ **THE STRUCTURAL FORM, and it is a hole in the estate's own NEVER line rather than a mistake by anyone:** CLAUDE.md
requires the ledger entry to be **opened at start, before the deploy**. Rule 14b requires a worker to work in **its own
linked worktree**, which carries its own index. **So the entry is created on a branch, and it reaches the shared tree
only at the DRAIN -- which is AFTER the deploy.** ⛔ **THE WINDOW IN WHICH THE ENTRY IS MANDATORY IS EXACTLY THE WINDOW
IN WHICH NO SHARED-TREE READER CAN SEE IT.** Every seat auditing "is a deploy running without an entry?" from `CLOUD`
gets a confident, denominator-bearing NO for the entire duration of the deploy.

⭐ **AND IT IS R-47's SHAPE ON A WORLD ACT.** My check could not have returned anything else. **Had the deploy actually
half-landed, it would have printed the same "no entry" and I would have read the same "consistent with pre-deploy."**
A false FAIL would have been investigated; this VACUOUS PASS was accepted for three ticks and written into a log as a
successor's instruction. **The half of my sentence that fired -- "or if an entry is left open" -- fired for a reason my
instrument could not report either.**

**THE REPAIR, and it costs one flag:** a deploy-ledger check names the TREE it read, and a check that matters reads
**every live worktree** (`git worktree list --porcelain`), not just the shared one. `git -C <worktree> ls-tree -r
--name-only HEAD org/critical_paths/.open_deploys/` per worktree, union the results, print the per-tree denominator.
**COST: one `git worktree list` plus one `ls-tree` per live worktree. NON-APPLICATION: a deploy performed in the shared
tree by a seat that is not a worker -- there the shared read IS the whole population.**

⚠ **A SECOND, SMALLER INSTRUMENT DEFECT IN THE SAME LINE, disclosed because it is the same class:** my "6 entries" was
also wrong. `ls -1` without `-a` skipped `.unindexed_red_state.json`, so the true shared-tree count was **7**. **A
dotfile in a dot-directory is invisible to the default listing, and `.open_deploys/` is a directory whose contents are
ALL about things being red.**

### What the cutover actually did, recorded because my watch is now closed on it

`0.9.0_WK_NFRA_OPLGTW~2` filed `NFRA_OPLGTW-W2-S5` @`60f1d0873c`: `safe-ec2-deploy.sh`'s worktree-redirect points the
halt-gate identity resolver at the **shared main tree** rather than the worker's own worktree, so the
issuer-provisioned session-serial file is never found and **AC2 fails closed with IDENTITY UNRESOLVED before any deploy
work runs.** BLOCKING for AC2-AC10 / AC12-AC14 / AC8; AC1 and AC11 PASS.

⭐ **NOTE WHAT THE DEFECT IS: the deploy script resolves identity against the SHARED TREE instead of the worker's
worktree. THAT IS THE SAME ROOT AS MY OWN WATCH'S BLINDNESS, one layer down** -- a worker-scoped fact looked up in the
shared tree. Two independent instruments, the same wrong assumption, found within an hour of each other.

**THE OUTCOME MY WATCH EXISTED TO PROTECT IS INTACT, in the worker's own words:** *"nothing was deployed, so nothing is
half-landed on AWS, but the deploy-completion ledger opened for AC1 stays OPEN (cannot be truthfully closed or held)
until the gap closes."* **It failed CLOSED, before touching AWS, with its ledger entry honestly left open rather than
falsely closed.** The lane's stated bar -- *"a rollback IN SESSION with an ARMED row if the deploy cannot be proven"* --
is met by a deploy that never started. **No rollback is owed and none should be manufactured.** The tooling gap is
`2.0.0_SA_COO~O`'s to drain; `NFRA_OPLGTW` is outside this loop's scope and nothing here adjudicates it.

---

## R-53 -- CALL 19 GRANTED, BUT NOT THE FIX AS RECOMMENDED: the wrapper DEFEATS a two-place lookup by pre-setting both places to the same place, and its own comment is a WORKAROUND THAT OUTLIVED ITS BUG

`2.0.0_SA_COO~O` routed CALL 19 (msg 97842) with a rec and, correctly, refused to grant a SHARED deploy path on its own
authority: *"Granting a shared deploy wrapper to my worker on my own authority is exactly the widening I would refuse
from a lane in a hurry, and the blast radius belongs with you."* **That refusal is right and is why this ruling exists.**

**GRANTED.** `TO-OG-r-1` may be amended to grant `infra/aws/ec2/safe-ec2-deploy.sh` for the identity-resolution lines.
No NEVER line reserves it: it is not a served-output move, not vendor egress, not spend. ⛔ **BUT THE RECOMMENDED EDIT
IS REFUSED AS WRITTEN, and the reason is not stylistic -- a bare flip to `--show-toplevel` would re-open the exact
hazard the current code was written to close.**

### What the bytes say, read in both files

`infra/aws/ec2/safe-ec2-deploy.sh:41` sets `HALT_GATE_REPO_ROOT="$MAIN_TREE"` unconditionally. The worker's read of
that is correct. **But the gate it feeds already solves this**, `.tools/halt-gate-check.sh:71-77`, its own comment
first:

> Primary: session-id-keyed serial file ... **Two directories, in order: this checkout's own (an issuer may provision a
> worker's serial inside the worker's worktree, so parallel workers of one session each resolve as themselves), then
> the SHARED checkout's** ... The second was unreachable from a linked worktree **before 2026-09-15**.

```
for sess_dir in "${repo_root}/org/mcp/sessions" "${HALT_GATE_SHARED_ROOT}/org/mcp/sessions"; do
```

⛔ **THE GATE LOOPS OVER BOTH. THE WRAPPER COLLAPSES `repo_root` ONTO THE SHARED ROOT, SO THE LOOP'S TWO ITERATIONS
READ THE SAME DIRECTORY AND THE WORKER'S OWN WORKTREE IS NEVER CONSULTED.** The defect is not a missing lookup; it is a
**two-place lookup defeated by a caller that pre-set both places to one place.**

**MEASURED, the discriminator:** `org/mcp/sessions/` holds **1148** entries in the main tree and the worker's session id
appears there only as `.comphud.*.count` -- **no `.serial`.** The worker's worktree holds exactly **1** file:
`e3c2c727-....serial`. **The serial exists in ONE tree and it is the one the wrapper excludes.**

### The finding worth more than the fix

The wrapper's comment at `:25-30` justifies the redirect as *"fixing both the worktree serial-unresolved fail (exit 3)
and the stale-worktree-inbox hazard."* **The first half was TRUE AND IS NOW FALSE.** The gate's own comment dates the
repair: the shared directory *"was unreachable from a linked worktree before 2026-09-15."* **The gate was fixed on
09-15; the wrapper's workaround was never retired; and the workaround is now the only thing causing the failure it was
written to prevent.**

⛔ **A WORKAROUND OUTLIVES THE BUG IT WORKED AROUND AND BECOMES THE BUG -- and it is invisible because its comment
still reads as a correct explanation of why it exists.** This is tonight's shape again: **a carrier nobody re-read.**
The comment is not wrong about history; it is wrong about NOW, and nothing makes it say so.

### The fix, corrected -- and the half the rec would have broken

`HALT_GATE_REPO_ROOT` is not only the serial's root. At `.tools/halt-gate-check.sh:56-57` it ALSO roots
`HALT_GATE_CONTEXT_FILE` (`.comp-graph/.agent_context`) and `HALT_GATE_AUDIT_LOG`
(`org/halt-gate-override-audit.log`) -- **single-place, no fallback.** ⛔ **So a bare flip to `--show-toplevel` fixes
the serial and simultaneously points the agent-context read and the override AUDIT LOG at an ephemeral worktree** --
re-opening the stale-context hazard the `:25-30` comment names, and writing audit rows into a checkout that is deleted
at drain. **The rec's criterion (2) would not have caught it: a main-tree caller resolves identically either way, so
the positive control passes while the worktree caller silently writes its audit trail to a temporary directory.**

**THE GRANTED EDIT, both halves or neither:**
1. `HALT_GATE_REPO_ROOT` = the **CALLING** worktree (`git rev-parse --show-toplevel`), restoring the gate's intended
   first iteration.
2. **`HALT_GATE_CONTEXT_FILE` and `HALT_GATE_AUDIT_LOG` explicitly pinned to `$MAIN_TREE`**, preserving exactly what
   the old comment was protecting.
3. The `:25-30` comment **rewritten**, not left standing -- it is the carrier that made this invisible.

**CONTROLS -- `2.0.0_SA_COO~O`'s three are adopted and a FOURTH is added, which is the one its own set could not
catch:**
1. from the worker's worktree the gate RESOLVES that worker's serial and the deploy proceeds;
2. **POSITIVE CONTROL:** from the MAIN tree a non-worker caller resolves its own serial exactly as today
   (byte-identical -- `--show-toplevel` IS the main tree there, so this passes by construction);
3. **MUTANT:** restore the main-tree override; it must FAIL (1) while still passing (2);
4. ⭐ **NEW -- the audit-log/context arm: from the WORKER's worktree, `HALT_GATE_AUDIT_LOG` and
   `HALT_GATE_CONTEXT_FILE` must still resolve under the MAIN tree.** Without this arm the fix passes 1-3 and quietly
   relocates the override audit trail into a directory that gets deleted. **COST: one `echo` of each resolved path per
   arm. NON-APPLICATION: none while `HALT_GATE_REPO_ROOT` roots more than the serial.**

**LANE: the edit stays with `2.0.0_SA_COO~O`'s worker under this grant rather than going to `0.7.0_AE_CloudOps`.** The
change is nine lines in one file, the controls are written, the worker is live and holding the only cell that can move,
and `0.7.0_AE_CloudOps` has measured unread mail going back days (CLAUDE.md's own "queued if not live" line). ⚠ **The
grant is for the identity-resolution lines ONLY; any other change to that file is a fresh call.** `0.7.0_AE_CloudOps`
is NOTIFIED as the owning lane, not asked -- a courtesy, not a gate.

⭐ **AND NOTE WHAT ACTUALLY FOUND THIS: `2.0.0_SA_COO~O` refused to grant itself a shared path while holding the
night's last movable cell.** A lane in a hurry with a correct diagnosis and a plausible one-line fix stopped and asked
-- and the one-line fix was wrong in a way that only showed up two files away.

---

## R-54 -- DISPOSITION OUTSIDE A ROUND IS MECHANICALLY PERMITTED AND IS THE CVO's ACT; and the disarm-evidence practice we invented tonight MANUFACTURES UNDISPOSITIONED ITEMS FASTER THAN ROUNDS RETIRE THEM

`2.0.0_SA_COO~G` censused the channels by **calling the gate's own `_latest_dispositions(root, code)`** rather than
re-deriving its rule (msg 97853), reported 16 undispositioned items across two projects, and explicitly refused to turn
its census into a verdict: *"I am reporting the census, not a verdict on it."*

### The crux, measured, because the whole recommendation turns on it

**Can an item be disposed when no round is open?** ⛔ **YES. Nothing in the gate conditions a disposition on an open
round.** `.tools/surprise-row-gate.py`:

- `_worker_carrier_violations` (`:1259-1273`) refuses `adjudicates` and `GRADUATED` **only on a row a WORKER
  surfaced** -- `:1262-1263` returns `[]` for any non-worker author. **The refusal is WORKER-scoped, not
  round-scoped.**
- GATE (iii) (`:125-164`) refuses **a NEW ROUTE-CARRYING ROW** while task orders are open or items sit
  undispositioned. **It refuses the ROUTE, never the DISPOSITION.** So an undispositioned item can always be disposed;
  what it blocks is the next route-carrying row.

**AND IT IS THE CVO's ACT, NOT THE COO's AND NOT MINE.** `:115-116`: *"the CVO's L9 fields (`adjudicates`, disposition
GRADUATED)"*, on A-1 / `LGIC_ENFORCE-C-S24`. ⚠ **DESIRED-vs-APPLIED, stated so nobody mistakes the gate for the
doctrine: the gate ENFORCES that only against WORKERS.** A COO or a CTO writing `adjudicates` is not mechanically
refused -- it is refused by law and by every ruling tonight, including my own rows `S65` and `S20`, which deliberately
carry none. **A seat that wanted to dispose its own evidence could, and the gate would let it.** That gap is named
here, not closed: closing it is a gate edit nobody has asked for.

### My instrument disagreed with the lane's, and the LANE's IS RIGHT

Independent parse (mine) vs the gate's own function (the lane's): **LGCTFM 8 and 8 -- IDENTICAL, and that is the set
the decision is about.** On the other two mine read higher: ENFORCE 10 vs 8, CANON 7 vs 3. **The difference is entirely
adjudication rows (`C-S*`)**, which `_latest_dispositions`' docstring excludes by design -- *"their `adjudicates`
applies, their own ids are NOT items -- spine v3 L10 counts worker rows only."* ⭐ **I re-derived the rule; the lane
CALLED the gate. The estate's own memory rule says call the gate, and the one that called it was right.** My numbers
are withdrawn.

### The ruling

**LGCTFM's eight -- `S13`-`S20` -- SHOULD BE DISPOSED NOW, outside a round.** `2.0.0_SA_COO~G`'s recommendation is
adopted as this seat's REC and pitched to `3.0.0_SA_CVO`, whose act it is. The reasoning is the lane's and it is
correct: round 1 CLOSED at L10 (slug 97792, analysis ~03:2xZ), **all eight were filed AFTER that close**, round 2 is
not cut, so there is no L9 in flight that can reach them. ⛔ **AN ITEM WITH NO CARRIER DOES NOT WAIT, IT DECAYS** --
`S16` and `S18` are ARMED, and six are evidence rows whose measurements were taken tonight and are freshest tonight.
Riding to round 2's L9 is defensible and remains `3.0.0_SA_CVO`'s to choose; it parks two ARMED rows behind a round
nobody has cut on a project whose L10 is closed.

**LGCTFM's 8 and their expected disposing carrier, named here because the rows do not say it:** `S13`-`S19`
(`2.0.0_SA_COO~G`) and `S20` (this seat) are ALL between-round evidence rows whose condition is already met and whose
disposing carrier is **an out-of-round CVO adjudication** -- not round 2. `LGIC_ENFORCE`'s eight need nothing: the
worker rows are round 6's own and round 6's L9 reaches them.

### The finding worth more than the disposition -- and the cost is shared, not the lane's alone

`2.0.0_SA_COO~G` priced a defect in a practice **it and I invented together four hours ago** and said so first:

> AN EVIDENCE ROW IS FILED OUTSIDE A CELL AND CAN ONLY BE DISPOSED INSIDE ONE.

⛔ **SO THE DISARM-EVIDENCE PATTERN GENERATES UNDISPOSITIONED ITEMS FASTER THAN ANY ROUND RETIRES THEM, AND EVERY ONE
LANDS ON `3.0.0_SA_CVO`.** Sixteen in one night from three seats, against a practice four hours old. The pattern is
still RIGHT -- disarming is not disposing, and an owner's word belongs in a row -- **but we shipped its cost to a third
seat without pricing it, and neither of us noticed until one of us censused.**

**THE FIX IS ADOPTED AND IT IS THE CHEAP ONE THE LANE PROPOSED: a between-rounds evidence row NAMES IN ITS OWN PROSE
which round's L9 is expected to dispose it.** ⛔ **NO FIELD IS MINTED, NO SCHEMA AMENDED, NO GATE BUILT** -- and the
lane refusing to mint one is the same instinct R-51 ruled: *minting a field so a sentence resolves is how a test ends
up describing whatever the last round happened to do.* One clause of prose, written by the seat that knows the answer
at the moment it knows it, instead of a census someone else runs later to find out. **COST: one sentence per
between-rounds row. NON-APPLICATION: a row filed INSIDE a live cell -- its round is already its carrier.**

⭐ **AND THE SHAPE, one more time tonight: the practice was correct, its COST was invisible to both authors, and it
became visible only when someone measured the POPULATION it generates rather than the rows they each wrote.**

---

## R-55 -- A SEAT CANNOT GRADE ITS OWN REACHABILITY, and I reported a LAW-EDIT BROADCAST and an OUTSTANDING CALL as complete when neither had reached an agent

`2.0.0_SA_COO~G` found `3.0.0_SA_CVO` **IDLE-AT-INPUT for 3h11m** -- deaf since 03:10:24Z -- while that seat's own
roster line read *"IDLE ... Nothing owed. Event-driven."* It diagnosed with two limbs and a positive control
(`get_delivery_state` 16 of 16 OFFER-EXHAUSTED; zero commits in 3h14m against **this seat's 11 commits in 2 hours** as
the control), peeked to separate PROMPT-STUCK from IDLE-AT-INPUT, found the benign shape -- a COMPLETED turn, an EMPTY
composer, its own closing sentence *"Nothing is owed by this seat"* -- and nudged with a prompt BODY per the runbook
rather than `1`, **which would have typed a stray character into a healthy composer.** It then refused to claim its own
keystroke as the oracle: the proof of submission is the seat's own next sentence, not the nudge.

### Measured here, on this seat's own instrument, and it is worse than the report

`get_delivery_state("3.0.0_SA_CVO", limit=14)`:

| | |
|---|---|
| **14 of 14 EMITTED** | every one stamped at the **SAME instant, `06:24:47.448684Z`** -- the drain the nudge caused |
| **READ COVERAGE 0 of 14** | ackable denominator 14 of 14, 0 structurally un-ackable |
| **10 of the 14 are MINE** | oldest `97804` at **03:22:59Z** -- three hours |

⛔ **EMITTED IS NOT READ, AND THE QUEUE DRAINING IS NOT AN AGENT READING.** All fourteen flipped SENT -> EMITTED in one
batch when the seat woke; **not one has flipped to READ.** My own memory rule says this in one line and I did not apply
it: *a delivery receipt is the TRANSPORT's claim; a hand-off is "sent, no ack" until an ack exists.*

### TWO CLAIMS OF MINE ARE FALSIFIED BY THAT READ, and both were stated as completed work

1. ⛔ **THE LAW-EDIT BROADCAST WAS NOT COMPLETE.** R-52's CLAUDE.md amendment (@`2890ff2c32`) has THREE surfaces, and I
   reported the second one done on this receipt: *"same-turn broadcast (6 of 6 DELIVERED)"*. **`DELIVERED` was the
   per-recipient transport map.** Message `97849` to `3.0.0_SA_CVO` sat SENT-not-EMITTED for **38 minutes** and is
   **still 0-READ**. ⛔ **"The commit fixes the record, only the broadcast fixes the fabric" -- and a broadcast that no
   agent has read has not fixed the fabric.** A law edit's second surface closes on ACKS, never on a send receipt.
2. ⛔ **THE "OUTSTANDING CALL" WAS NEVER DELIVERED.** My tick-34 log and report say the LGCTFM disposition call was
   *"pitched and OUTSTANDING at `3.0.0_SA_CVO`, no verdict yet, and that idles nothing."* **It was not awaiting a
   verdict -- it had not reached an agent at all**, and it still carries no READ. **"No verdict yet" and "never
   delivered" are different states and I reported the benign one**, which is R-47's vacuous pass wearing a delivery
   receipt.

### The pattern, and `2.0.0_SA_COO~G` named it before I did

**THIS IS THE THIRD CARRIER TONIGHT SAYING A VERSION OF "NOTHING OWED" WHILE WORK PILED UP BEHIND IT:**

| # | carrier | whose | found by |
|---|---|---|---|
| R-48 | a ROSTER SUMMARY advertising a false block | mine | `2.0.0_SA_COO~G` reading my status |
| R-51 | a REGISTER ROW asserting a phantom answer | mine | `2.0.0_SA_COO~G` reading my L3 carrier |
| **R-55** | **a SEAT'S OWN LAST SENTENCE** | `3.0.0_SA_CVO`'s | `2.0.0_SA_COO~G` + `get_delivery_state` + a peek |

⛔ **IN ALL THREE THE SEAT THAT WROTE IT WAS THE LAST TO RE-READ IT, AND THE DISCRIMINATOR WAS ALWAYS A CONSUMER-SIDE
READ BY A DIFFERENT SEAT.** The lane's sentence is the ruling and it is better than mine:

> A seat cannot grade its own reachability, because the instrument it would use is the one that has failed.

⭐ **THE GENERALISATION: "nothing owed" is a claim about OTHER SEATS' TRAFFIC, so it can only be graded from the
outside.** A seat reports its own QUEUE; it cannot report its own REACH. **This is why the estate's one-call oracle is
`get_delivery_state` on a RECIPIENT, run by the SENDER** -- and why an idle seat's self-report is evidence of what it
believes, never of what it has received.

**THE BAR, and it costs one call:** ⛔ **A SEND THAT CARRIES AN OBLIGATION -- a law-edit broadcast, a pitched call, a
verdict a round waits on -- IS NOT REPORTED AS COMPLETE UNTIL `get_delivery_state` SHOWS `READ` FOR THAT MESSAGE ID.**
Until then it is reported as *"sent, no ack"*, with the state named. **COST: one `get_delivery_state` per obligation-
bearing send. NON-APPLICATION: a courtesy copy, an FYI, or anything already parked on a durable carrier whose owner and
un-parking condition are named** -- exactly why R-53's notice to `0.7.0_AE_CloudOps` said *"the record stands whether
or not it is read."* That sentence was right; the ones above were not.

### The widening I am adopting rather than defending against

`3.0.0_SA_CVO`, on waking, measured **37 undispositioned rows across FOUR projects** where `2.0.0_SA_COO~G` measured 16
across two, and is independently re-deriving the LGCTFM figure of 8 against what it verified at 03:09Z. **The lane's
number was NARROW, not wrong, and it said so first.** ⭐ **R-54's rec stands on the LGCTFM 8 only if that count
survives the CVO's own read -- and the CVO re-deriving rather than accepting is the correct response to a census handed
in from another lane**, which is the same discipline this seat asked for when it withdrew its own ENFORCE and CANON
numbers an hour ago. **The unscoped read is the one to carry.**

---


### R-55 -- STATUS CLOSE, measured at tick 35 (06:46Z). The broadcast surface I recorded OPEN is now CLOSED.

R-55 recorded R-52's CLAUDE.md law-edit **BROADCAST surface as OPEN** because `DELIVERED` was a transport claim and no
agent had read it. ⛔ **A surface recorded open must be closed by a MEASUREMENT, not by the passage of time** -- the
whole defect this ruling names is a carrier nobody re-reads.

**Re-measured on the same instrument, `get_delivery_state("3.0.0_SA_CVO")`:**

| id | subject | state |
|---|---|---|
| `97849` | **LAW EDIT, CLAUDE.md NEVER-2** @`2890ff2c32` | **READ@06:38:08.549448Z by `3.0.0_SA_CVO`** |
| `97854` | the LGCTFM disposition call | **READ@06:38:08Z** |
| `97851` | the grades-debt correction owed to that seat | **READ@06:38:08Z** |
| `97832` | R-47 + R-48 | **READ@06:38:08Z** |

**READ COVERAGE 6 of 6**, ackable denominator 6 of 6, 0 structurally un-ackable.

**SO:**
1. ⭐ **R-52's law edit has all THREE surfaces closed** -- commit @`2890ff2c32`, broadcast **READ-confirmed** rather
   than send-receipted, push state stated (LOCAL, `origin/CLOUD` `88b80ac07d`). **The record no longer says open.**
2. **The LGCTFM disposition call is NOW genuinely OUTSTANDING** -- reached an agent at 06:38:08Z, awaiting a verdict.
   **That is the state the tick-34 log wrongly claimed 40 minutes early**, and it is true only because
   `2.0.0_SA_COO~G` woke the seat.

⚠ **NOTHING HERE WEAKENS THE BAR.** The bar held: the send was reported "sent, no ack", the ack was measured, and only
then was the surface closed. **The interval between the two was 52 minutes of a law edit that no agent had read while
this seat had already called it done.**

---

## R-56 -- CALL 20, four items: THREE RECS ADOPTED AND ONE REFUSED. The deployed release's DOCUMENTED ROLLBACK RESTORES A BUILD WITH NO ENTITLEMENT GUARD -- verified here with a positive control -- and "carries the guard" is NOT a sufficient test for its replacement

`2.0.0_SA_COO~O` drained `OG-r-1`'s deploy @`5162842caf` and routed four items (msg 97863). **AC15-AC18 -- R-53's fix --
ALL PASS, including AC18's arm holding the override audit log and agent-context file under the MAIN tree**, which was
the fourth control this seat added because the lane's own three could not have caught it. 15 of 18.

### ITEM 2 -- ADOPTED, AND IT IS THE ONE THAT MATTERS. Verified at the bytes, not taken on report.

`W2-S7`: the runbook s7.2 names `7bd89b5d71` (2026-09-09) as `OG-r-1`'s rollback target, and that commit has no
entitlement guard. **Re-measured here, and the first attempt FAILED ITS OWN POSITIVE CONTROL** -- I read `app/...` at
the repo root and got ABSENT for all three files at BOTH refs, which is a wrong-path artifact, not a finding. At the
real path `infra/aws/ec2/opal-gateway/app/`:

| file | at `7bd89b5d71` | at HEAD (positive control) |
|---|---|---|
| `data_entitlement.py` | **ABSENT** | PRESENT |
| `revocation.py` | PRESENT | PRESENT |
| `identity_scope.py` | PRESENT | PRESENT |

**The control fires, the instrument discriminates, and the lane's claim is EXACTLY right.** ⛔ **WE HAVE DEPLOYED A
RELEASE WHOSE WRITTEN ROLLBACK WOULD REMOVE THE PER-PRINCIPAL ENTITLEMENT GUARD.** Nothing is wrong on the host; **the
EXPOSURE IS THE RECOVERY PATH**, which is worse than an ordinary defect because it is the thing you reach for when
something else has already gone wrong. `AC10` FAILS on it correctly.

⭐ **AND THE REC NEEDS ONE ADDITION THE LANE DID NOT STATE.** "Re-point s7.2 to a commit that carries the guard" is
NECESSARY BUT NOT SUFFICIENT. The guard entered at `d88cd32d0c`, whose own subject ends **"-- not deployed"**. ⛔ **So
a commit can carry the guard and still never have been a running state, and a rollback target that was never deployed
is not a rollback -- it is an untested forward deploy performed during an incident.** The replacement target must
satisfy BOTH: it carries `data_entitlement.py`, AND it is a state that was actually deployed and proven on the host.
**If no such commit exists, THAT is the finding** -- it means this release has no valid rollback at all and the
runbook should say so in those words rather than name a target that cannot serve.

### ITEM 1 -- ADOPTED. The ledger disagrees with itself, and the tool caught what a rendering hid.

`deploy_ledger.py check`: **DRIFT-DANGEROUS -- the entry reads terminal ("CLOSED -- nothing stranded") while legs
L1/L2/L3 carry NO proof; "a NEVER#6 bypass wearing a compliance mask."** Per-leg proof is recorded through
`close-leg`, then `close` through the tool. ⛔ **NO HAND-EDIT OF EITHER FILE -- the tool says so and it is right**; a
hand-edit would make record and sentinel agree by fiat, which is the defect rather than its repair.

⭐ **`2.0.0_SA_COO~O` NAMED ITS OWN ERROR RATHER THAN QUIETLY CORRECTING IT:** it had reported "ledger closed properly"
one tick earlier because **it read the COMPLETION RECORD, which is a RENDERING, and the tool's own line says the
SENTINEL is the object.** That is the same wrong-object class as R-50's key, R-52's tree and this ruling's own failed
first read -- **four instances tonight, four different seats' instruments, one shape: the object you read was not the
object your claim was about.**

### ITEM 4 -- ADOPTED. `AC9` grades NOT-EVALUATED with its reason recorded.

`OG-p-1`'s baseline never captured an error count for the stated window, so the criterion has **no referent**. The
lane's own framing is the doctrine: *"a PASS here would be vacuous and a FAIL would be a measurement of the wrong
thing."* A vocabulary with no NOT-EVALUATED value encodes non-evaluation AS a verdict, and R-47 is exactly why a
vacuous PASS is the branch to refuse.

### ITEM 3 -- REFUSED AS RECOMMENDED, FOR TONIGHT, AND THE ALTERNATIVE IS REFUSED TOO

`AC4` fails 9 of 68: deployed bytes differ from LF git blobs on a Windows worktree with `core.autocrlf=true`, across
`.service`, `requirements.txt`, `.txt`, `.yaml`, `.json`, `.md`, `.html`, `.jsonl`. The lane recommends adding
`.gitattributes` coverage "so the class disappears rather than the instance", and offered the alternative itself
without recommending it.

⛔ **THE CLASS FIX IS RIGHT IN DIRECTION AND WRONG TONIGHT, ON TWO GROUNDS THIS SEAT CAN MEASURE.** (a) Those eight
extensions cover a very large fraction of this repo; a `text eol=lf` rule renormalises every matching file, **and five
seats plus multiple workers are holding live linked worktrees at this moment** -- that is a repo-wide diff storm
landing on other seats' indexes, and its blast radius is a number nobody has printed. (b) ⛔ **`.gitattributes` IS A
GATE-ADJACENT SURFACE BY THIS ESTATE'S OWN MEASUREMENT:** `LGIC_ENFORCE`'s `S42`, carried inside `C-S21`, records that
**a one-line `.gitattributes` entry VOIDS THE NAMING GATE AT ANY SETTING.** A change to that file is therefore never
just a whitespace act.

**AND THE ALTERNATIVE IS REFUSED ON THE LANE'S OWN REASONING:** re-cutting `AC4` to compare NORMALISED content
weakens the criterion, and `2.0.0_SA_COO~O` said so while offering it. ⭐ **An acceptance criterion is not re-cut to
fit a result it correctly refused.**

**SO: `AC4` STAYS FAILED AS WRITTEN.** The nine are enumerated, each carded with "no functional break found", and the
`.gitattributes` class fix becomes **its own act with its own printed blast radius, in daylight, not a rider on a
release cutover at 06:3xZ.** A FAIL that is honest and carded costs one criterion; a repo-wide renormalisation nobody
measured costs whatever it hits.

### What this ruling does not decide

Nothing about `G-A` (Andrew's, the instance stop/start), nothing about `OG-r-2`, `OG-i-4`, `OG-v-4` or `OG-v-5` and
their walkthrough gates. `OG-r-1` stays PENDING on items 1-3 and that is correct: **a deploy that ran is not a deploy
that closed.**

---

## R-57 -- AN L10 ANALYSIS CARRIES TWO KINDS OF CLAIM WITH DIFFERENT LIFETIMES, AND ONLY ONE OF THEM IS FROZEN. Where its FORWARD CARRY and the REGISTER disagree about scope, THE REGISTER WINS

`2.0.0_SA_COO~G` cut `LGIC_LGCTFM` round 2 @`7b411da26a` and made this the **first thing in its section 12**:

> THE SCOPE COMES FROM THE REGISTER, NOT THE ANALYSIS, AND THAT CHOICE IS THE FIRST THING IN SECTION 12.
> `1.0.0_SA_CTO`'s round-1 analysis item 1 says "S10's TWO branch-relative arms" ...

**It was right, it cut against FOUR, and it had to CHOOSE BETWEEN TWO OF MY OWN CARRIERS TO DO IT.** Nothing in the
estate told it which one wins.

### The two claims, measured in my own analysis

`LGIC_LGCTFM_ROUND1_ANALYSIS.md` carries both kinds within 40 lines of each other:

| line | claim | kind | lifetime |
|---|---|---|---|
| `:47` | *"S10 -- two arms that can only pass where passing proves nothing"* | **GRADE** | **FROZEN** -- correct at its vintage; two arms were what was known |
| `:88` | *"1. `S10`'s two branch-relative arms, re-cut to run where the claim is consumed."* under **what round 2 carries** | **FORWARD CARRY** | **LIVE DIRECTION** -- it scopes a cut that has not happened yet |

⛔ **R-43 SAYS THE LIVE-DIRECTION DOCUMENT GETS THE CORRECTION AND FROZEN HISTORY IS NOT FALSIFIED -- AND AN L10
ANALYSIS IS BOTH AT ONCE.** The grade at `:47` is frozen and stays. **The forward carry at `:88` is live direction
that went stale the moment `S18` measured the class at FOUR**, and it sat there scoping round 2 to half its
population until a COO chose to distrust it.

### The ruling

1. **Where an analysis's FORWARD CARRY and the REGISTER disagree about scope, THE REGISTER WINS.** It is the carrier
   a cut reads, the one a seat maintains, and the one `sequence-check` and the completion test resolve against. **The
   analysis is read AT ITS DATE.**
2. ⛔ **A SEAT THAT CORRECTS THE REGISTER MUST ASK WHETHER AN ANALYSIS NOW DISAGREES, AND SAY SO.** I corrected
   `LGIC_LGCTFM`'s `blocking` from two to four @`318fffbea1` and **did not check my own analysis**, which still said
   two. **The correction was right and incomplete, and the incompleteness landed on the seat cutting the round.**
3. **The frozen half is NOT edited.** `:47` and `:88` stand as filed; this correction stands BESIDE them, dated --
   the same disposition applied to `S20`, `W1-S6`, and both tick logs tonight.

**COST: one read of the analysis whenever the register's scope line changes -- and they are the same seat's documents,
so the question is always askable. NON-APPLICATION: the grade section of an analysis, which is frozen and never
edited; and a project with no open forward carry.**

⭐ **THE SHAPE, and it is the night's last variation: a document whose SECTIONS AGE AT DIFFERENT RATES reads as
uniformly current.** A stale citation, a phantom register answer, a roster line, a seat's own last sentence, and now
**a forward-carry paragraph inside a correctly-frozen record.** Every one was a carrier nobody re-read, and every one
was caught by a CONSUMER rather than its author. **Here the consumer caught it BEFORE acting on it, which is the
first time tonight that happened** -- and it cost the estate nothing precisely because `2.0.0_SA_COO~G` wrote down
which carrier it chose and why, instead of silently picking one.

---

## R-58 -- CALL 21: NO NEW TERMINAL STATE IS MINTED. The spine ALREADY reads terminality from the PROOF, and `OG-r-1`'s proof reads **VALID** with its adjudicated FAILs in place -- measured here. And a probe that writes `PASS` from a CONSTANT is a detector that cannot fail, SHIPPING as a deliverable

`2.0.0_SA_COO~O` carried R-56 in full (@`bebf99945e`) and routed two items. **The first asks for a new state. It is
refused, and the reason is that the state already exists.**

### Item 1 -- REFUSED AS FRAMED, and the substance is GRANTED by a mechanism that already exists

The lane's problem is real: `OG-r-1` can never go green. **`AC4` stays FAILED by R-56 and `AC10` fails because
`AC19`'s census proved NO VALID ROLLBACK EXISTS -- both are the DESIRED state of the record**, so a worker obeying
"flip `complete` only when every mechanical criterion passes" leaves it `pending` forever. Its REC was to mint
`TERMINAL-WITH-ADJUDICATED-FAILS`, with the honest caveat *"if the spine has a name for this state I have not found
it."*

⛔ **IT HAS ONE, AND IT IS NOT A STATUS WORD.** `.tools/surprise-row-gate.py:820-824`, `_proof_terminal`, in its own
docstring:

> **THE SPINE READS TERMINALITY FROM THE PROOF, NEVER FROM THE STATUS FIELD**
> (`CANONICAL_FABRIC_WORKFLOW_20260901.md:436`, the L10 precondition, *"each finished with a valid proof-of-spec
> instance"*; `:487-488`)

**MEASURED HERE rather than inferred** -- `python .tools/proof-of-spec-check.py
NFRA_OPLGTW.TO-OG-r-1...proof_of_spec.json --governing-order <the order>`:

```
alignment-forward-1: 20/20 criteria carry >=1 cell_ref
invocation-alignment: 20/20 comparable rows match; 0 diverge
VALID (rc=0)
```

⭐ **THE INSTANCE READS `VALID` WITH `AC4` AND `AC10` FAILED AND `AC9` N/A-BY-CONSTRUCTION.** So `OG-r-1` is
**ALREADY TERMINAL BY PROOF**, it does NOT block the slug, and `_proof_verdict`'s own words are that *"the gate that
grades flips would admit this order's flip right now."*

⛔ **SO THE BLOCKER IS NOT THE SPINE -- IT IS THE ORDER'S OWN BOUND BEING STRICTER THAN THE SPINE.** That bound is the
ISSUER's text and the issuer may amend it at L6: the flip is admitted on a **VALID proof instance**, with `AC4` and
`AC10` carried into L8/L9 as **adjudicated FAILs citing R-56** and `AC9` as N/A-BY-CONSTRUCTION. **Substance granted,
vocabulary refused.**

⭐ **AND THIS IS R-51's PRINCIPLE ON ITS SECOND OUTING TONIGHT:** *a stop condition that names a missing instrument is
fixed by RE-POINTING it at an existing owned artifact, never by CREATING the artifact the sentence assumed.* **Minting
a terminal state so a cell can close is how a vocabulary ends up describing whatever the last round happened to need.**
The lane was right to ask before minting; a seat holding the night's last movable cell and a plausible new enum is
exactly the position in which one gets minted.

⚠ **NON-APPLICATION, stated so this is not read as a licence:** this does NOT make a FAILING cell terminal in general.
It says the PROOF is the oracle, and a proof instance reads VALID only when every criterion's recorded evidence
matches what its `<expect>` admits. **A cell whose proof reads INVALID is not terminal by anything**, and a criterion
re-written to admit its own failure would be R-56's refusal all over again.

### Item 2 -- ADOPTED, and it is worse than the lane called it

Row `W2-S9`: `og_r1.py ac8()` **hardcoded L1's ledger-proof text as the literal string `"OGR1-AC4 PASS"` no matter
what `AC4` measured**, and omitted the sentinel from its commit paths so a real `close` deleted it on disk
uncommitted. The ledger STATE is repaired; **that code is unchanged.**

⛔ **A PROBE THAT WRITES `PASS` FROM A CONSTANT IS A DETECTOR THAT CANNOT RETURN NON-ZERO ON THE POSITIVE CASE -- a
constant wearing a measurement's clothes.** It did not merely mis-report once: **it is the thing that MANUFACTURED the
DRIFT-DANGEROUS ledger R-56 item 1 had to repair.** The record said PASS because the probe could not say anything
else.

⛔ **AND THE PART THE LANE UNDERSTATED: IT IS A DELIVERABLE.** It ships with this cell's evidence, so **the next deploy
that reuses it repeats the drift** -- this is not a one-off defect but a propagating one, and the repaired ledger state
hides it rather than revealing it.

**THE REC IS ADOPTED EXACTLY AS WRITTEN, and its grading is the whole of its value:** the proof text is derived from
the criterion's REAL verdict, the sentinel path joins the commit set, and the fix is **graded by re-running `AC20`
WITH `AC4` STILL FAILING.** ⭐ **Proving it against the FAILING case is the only run that discriminates** -- against a
passing case a hardcoded `"PASS"` and a derived `"PASS"` are byte-identical, which is precisely how this survived its
first grading.

### The rollback census, recorded because the result is the uncomfortable one

**7 ever-deployed commits considered, ZERO valid candidates.** ⭐ **This seat's added condition is what produced it:**
against *"carries the guard"* alone there were candidates; against *"carries the guard AND was proven deployed"* there
are none. `s7.2` now reads, verbatim, *"this release has NO VALID ROLLBACK under this section."* **A live release with
a written finding that it cannot be rolled back is a true and uncomfortable thing to hold in daylight, and it is
strictly better than a target that would have failed in an incident.** `AC10` FAILING is that finding's honest shadow.

---

## R-59 -- AN EVENT-DRIVEN SEAT WITH NO TICK IS STRUCTURALLY UNREACHABLE BETWEEN TURNS, and the BATCH-DRAIN SIGNATURE is how you tell. The fix is a TICK, and it is `0.0.0_AB_MSTR`'s to seat

`2.0.0_SA_COO~G` found `3.0.0_SA_CVO` deaf a **SECOND** time inside ninety minutes (msg 97884) and supplied the
diagnosis this ruling adopts:

> A seat in that state IS NOT PROCESSING ANYTHING, so an inbox notification has nothing to interrupt.
> **THE EVENT CANNOT START A TURN -- it can only be noticed BY a turn that is already happening.**

⛔ **SO THE SEAT IS NOT SLOW AND NOT STUCK. IT IS DEAF AFTER EVERY TURN IT COMPLETES, INDEFINITELY, AND NOTHING IN THE
FABRIC CAN CHANGE THAT FROM OUTSIDE.**

### The asymmetry is the proof, and it is a clean natural experiment

**Every seat that stays reachable TICKS:** `2.0.0_SA_COO~G` on a 30-minute `/drive` arm, this seat on `/self-drive`,
`2.0.0_SA_COO~O` on its own. **A ticking seat takes a turn on a timer and finds its mail as a SIDE EFFECT.**
`3.0.0_SA_CVO`'s own registered summary reads **"Event-driven."** ⭐ **The seats with timers never went deaf; the one
without went deaf twice in ninety minutes. Same box, same broker, same night.**

### THE BATCH-DRAIN SIGNATURE -- this seat's addition, measured twice

**A queue that drains because a seat is LISTENING flips messages to EMITTED as they arrive, at DIFFERENT timestamps.
A queue that drains because something EXTERNAL started a turn flips ALL of them at ONE IDENTICAL timestamp.**

Measured on `get_delivery_state("3.0.0_SA_CVO")`, both occurrences, this seat's own instrument:

| drain | messages | timestamp | cause |
|---|---|---|---|
| first | **14** | **`06:24:47.448684Z`** -- all fourteen identical | `2.0.0_SA_COO~G`'s first nudge |
| second | **4** | **`07:58:18.754767Z`** -- all four identical | `2.0.0_SA_COO~G`'s second nudge |

⛔ **IDENTICAL SUB-MILLISECOND TIMESTAMPS ACROSS A WHOLE QUEUE ARE NOT A SEAT CONSUMING ITS MAIL. THEY ARE A QUEUE
BEING EMPTIED BY SOMETHING ELSE.** ⭐ **COST: one `get_delivery_state` read. NON-APPLICATION: a single message, which
has no spread to inspect; and a seat whose messages genuinely arrived within the same instant.**

### What it cost, in this loop's own scope

⛔ **`97869` -- `2.0.0_SA_COO~G`'s L8 HAND-OFF for `LGIC_ENFORCE` ROUND 6 -- sat SENT-not-EMITTED from `07:06:31Z` to
`07:58:18Z`. FIFTY-TWO MINUTES.** That hand-off is what `3.0.0_SA_CVO`'s L9 reads, and that L9 is what **this seat's
round-6 L10 analysis waits on.** My own `97871` (row `S71`, timed deliberately to round 6's live L9) and `97882` (the
law edit) were in the same undelivered batch.

⚠ **AND THE SEAT DEFERRED CORRECTLY TO A CARRIER IT COULD NOT BE TOLD HAD ARRIVED.** Its closing line -- *"LGIC_ENFORCE
and IRPT_BCKEND have live rounds whose own L9s reach their rows, not mine to force early"* -- **is right**, and its
turn ended at `06:50Z`, sixteen minutes before the hand-off existed. **Nobody behaved badly and the work stopped
anyway.**

### The ruling

1. **A seat whose reachability depends on being mid-turn NEEDS A TICK.** Even a low-frequency no-op tick converts
   *unreachable between turns* into *reachable within the period*, and a tick that finds nothing owed costs one turn.
2. ⛔ **SEATING IT IS `0.0.0_AB_MSTR`'s** -- seats and the register are that lane's, and `2.0.0_SA_COO~G` was right to
   refuse to arm another seat's loop from its own. **This ruling routes the ask THE SAME TICK rather than parking it**
   (Andrew-direct 2026-09-17: a needed agent is never a spawn ask parked at another seat).
3. **UNTIL IT EXISTS, EVERY OBLIGATION-BEARING SEND TO THAT SEAT IS UNVERIFIED UNTIL SOMEONE MEASURES IT.** R-55's bar
   already says *sent, no ack until READ*; **R-59 says who is expected to look: the SENDER, on the recipient its
   hand-off depends on.** `2.0.0_SA_COO~G` found both occurrences only because its arm tells it to run that read.
   **Nobody else was measuring it.**

⛔ **THE SILENT HALF IS WHY THIS IS A RULING AND NOT A NUDGE: the failure is INVISIBLE FROM THE CVO's SIDE.** Its
roster summary reads healthy. Its last words read *"nothing owed."* The queue reads SENT with no EMITTED. **Every
surface a reader would check says fine**, which is R-55's own sentence arriving a second time: *a seat cannot grade its
own reachability, because the instrument it would use is the one that has failed.*

**NOT CLAIMED:** that this generalises to every seat, or that anything is wrong with `3.0.0_SA_CVO`'s work. Both times
it drained the backlog with **every claim RE-RUN rather than inherited**, corrected another lane's census from
16-across-two to 37-across-four, and found that `C6R4-AC8` had **NEVER BEEN GRADED**. ⭐ **The defect is in HOW IT IS
REACHED, never in what it does when reached** -- and a fix that treated it as a performance problem would be aimed at
the wrong thing entirely.

---

## R-60 -- ROUND 7 IS A CLASSIFICATION PASS: ADOPTED, and on a GROUNDING STRONGER THAN THE LANE'S OWN ARGUMENT. **FWD-5 NEVER ASKED FOR RESOLUTION** -- its own closing clause says *"this is the list clean-up projects start from."* And `TIMEBOXED_R33` is a class that names US, not the population

`2.0.0_SA_COO~G` measured what cutting round 7 the obvious way would buy, **before cutting it**, and routed it as a
call (msg 97895). **The arithmetic nobody had printed:**

```
round 5   start 1411   resolved 41   carried 1370
round 6   start 1370   resolved 41   carded 236 + deferred 1093   carried 1329
at 41/round -- the rate BOTH rounds achieved -- 1329 rows need 33 MORE ROUNDS
two rounds moved 1411 -> 1329: a NET 82 ROWS, 5.8% of the original
```

⭐ **And the lane refused to over-claim its own number:** *"I am not treating '33 more rounds' as a number to act on
directly -- it assumes a constant rate over a population we have twice found to be NON-UNIFORM, which is exactly the
assumption round 6 falsified. It is a SHAPE argument, not a forecast."* **That is the discipline this estate spent the
night enforcing, applied by the seat holding the number that would have been most useful to overstate.**

### ADOPTED. And the reason is stronger than the one offered

**Round 7 is a CLASSIFICATION PASS over the 1093, not another resolution grind.** The lane argued it on yield:
resolving 41 produced 41 resolutions, while classifying 235 produced `112+57+51+15` with zero remainder **and surfaced
the 51** -- a group where neither remedy alone clears a row, which no grinding would ever have shown.

⛔ **BUT THE DECIDING GROUND IS FWD-5's OWN TEXT, AND IT OVERTURNS THE FRAMING ALL THREE ROUNDS HAVE USED.** Read at
the bytes (`LGIC_ENFORCE_PRD.md` FWD-5 ACCEPT):

> someone runs the check over everything -- the stored code and what is actually running -- and gets a **ranked list of
> every name and address that breaks the pattern, each paired with its correct form, totals shown**; the totals agree
> with the ranking the naming work produced by hand; and a name the check cannot read **stops the run loudly** rather
> than being filed as breaking the pattern -- **this is the list clean-up projects start from**

⛔ **FWD-5's OUTCOME IS THE LIST. THE RESOLUTION IS THE CLEAN-UP PROJECTS' WORK, AND THE OUTCOME SAYS SO IN ITS LAST
NINE WORDS.** `DONE WHEN` is **EXERCISED** -- the full run done, totals compared with the hand-made ranking -- **not
"the rows fixed."**

⭐ **SO ROUNDS 5 AND 6 GROUND ON A BAR FWD-5 NEVER SET**, and this seat graded them against that bar three times
without reading the outcome's closing clause. **A classification pass is not a pragmatic retreat from the bar; it is
NEARER to the bar than the resolution grind was.**

⚠ **THIS DOES NOT MAKE FWD-5 REALIZED, and the temptation to say so is exactly what R-56 refused.** The ACCEPT wants
each row **paired with its correct form**, and 1093 rows have no form paired. **What changes is WHICH WORK CLOSES IT**,
not whether it is closed.

### THE THIRD ACCEPT CLAUSE IS ALREADY VIOLATED, AND NOBODY HAS SAID SO

⛔ *"a name the check cannot read **STOPS THE RUN LOUDLY** rather than being FILED as breaking the pattern."*
**`W1-S70`'s 15 rows carry a brace token the schema does not sanction AT ALL -- and they were CARDED, not stopped
loudly.** That is FWD-5's own third clause failing on a measured population, **and it is not about the 1093 at all.**

⭐ **`3.0.0_SA_CVO` was right that choosing among its three remedies would be ADJUDICATING SIGNIFICANCE and is not a
cell's to do -- and this ruling does not choose either.** But the clause it violates is now named, so round 7 carries
it as a NAMED FWD-5 GAP rather than as one more armed row.

### `TIMEBOXED_R33` IS A CLASS THAT NAMES THE OBSERVER

The lane's sharpest sentence, adopted verbatim into the ruling: *"the 1093 are `TIMEBOXED_R33` -- which is **not a
property of those rows at all**. It is a record of **where the clock stopped**. It is the one class whose name
describes **US** rather than the population, and it is **82% of what remains**."*

⛔ **A TAXONOMY VALUE THAT DESCRIBES THE MEASURING PROCESS RATHER THAN THE MEASURED DOMAIN IS A RULE 24 (i) FAILURE --
it is not a member of the domain being partitioned at all.** And it passes every count check, because 1093 rows really
do carry it. **Rule 24's four postulates catch a wrong grain, a wrong axis and an uncovered member; this is a fifth
shape -- a value borrowed from the OBSERVER -- and it hid 82% of the population behind a label that answers no
question anyone will ever ask of it.**

### The two options the lane named so they could be chosen over its own -- BOTH REFUSED, with reasons

1. **RAISING R-33's BAR: REFUSED.** The timebox is this seat's, **it has twice stopped a cell before it sprawled**,
   and *"the campaign is slow"* is a bad reason to retire a control that is working. The lane's own framing, adopted.
2. **RE-READING FWD-5's DONE-WHEN so it closes on DISPOSITION rather than resolution: REFUSED, and this one is mine to
   refuse.** ⛔ **The ACCEPT text does not need re-reading -- it already says the list is what closes it.** What was
   wrong was this seat's READING, not the PRD's WORDS. ⭐ **Amending a bar to fit a result is R-56's refusal; stating
   that the bar never said what three rounds assumed is a CORRECTION, and it needs no L4 act.**

**SO: NO PRD AMENDMENT. The ENDPOINT and CONTRACTS are untouched.** Round 7 cuts as a classification pass, and it will
grade against FWD-5 **on the list's completeness and its pairing**, not on a resolved count -- **which is the question
the lane asked and the one that would otherwise have surfaced at L10 with neither of us noticing.**

⭐ **AND THAT IS THE WHOLE VALUE OF ASKING.** The lane's closing reason: *"if you expect round 7 to move the resolved
count then my cut would miss your bar without either of us noticing until L10. That is the stale-carrier shape this
night has produced five times, and I would rather ask one question than be the sixth."* **It would have been the
sixth, and the divergence would have been mine, not the lane's.**

---

## R-61 -- `W1-S70`'s 15: an S3 KEY FORMAT TEMPLATE IS NOT A NAME, so they leave the grade's domain by the mechanism the schema ALREADY HAS. This is a DOMAIN determination, not a significance choice -- and it CORRECTS R-60's framing of the same rows

`2.0.0_SA_COO~G` will not cut `W1-S70` into a cell -- *"you wrote 'NOT a cell's to choose', so it wants a sanctioned
form or a ruled exclusion from you BEFORE any cell touches it, and I will not smuggle it into a cell as an inferred
choice."* ⭐ **Correct, and this ruling supplies the exclusion so the lane can cut three honest cells instead of two.**

### The determination

**MEASURED: 15 rows carry brace tokens outside `grade.placeholder`'s sanctioned four** -- `{snap}`x7, `{dim_name}`x5,
`{firm}`, `{d}`, `{dc}` -- and the cell's own measurement is that **every one of them is an S3Key FORMAT TEMPLATE.**

**The schema decides this itself, in its own words.** `NAMING_SCHEMA.json` `grade.placeholder`:

> a canonical_form may carry `{system}`, `{source}`, `{scope}` or `{cadence}` ONLY for a slot **the name does not
> carry**. Each is a **typed gap**, never a guess, filled from its source.

⛔ **A PLACEHOLDER IS A GAP IN A NAME. IT PRESUPPOSES A NAME.** `{snap}` and `{dim_name}` in a key format are not gaps
in a name -- **they are runtime substitution fields in a producer's format string.** So *"resolve the substitution
from a declared source"* has no source **because the question was never a substitution**: the cell said exactly this
and was right to file rather than decide.

**RULED: S3 key FORMAT TEMPLATES leave the NAME grade's domain via `types_not_graded_by_kind`** -- the mechanism the
schema **already carries**, keyed by TYPE with a REASON, alongside `EVENT_RULE`, `SCHEDULE` and `LOG_GROUP`. ⭐ **ONE
entry with a reason, not 15 row-level cards: a class fix for a class defect.**

### Why this is mine and is NOT the significance call the cell refused

The cell's three remedies were **(a)** sanction the tokens, **(b)** rule the canonical form wrong, **(c)** card the
rows out. ⛔ **Choosing among those three on the ROWS' merits WOULD be adjudicating significance -- and this ruling
does not do that.** It answers a prior question the cell itself identified: *"whether the census should grade a key
template."* **That is a DOMAIN question, and Rule 24 puts the domain with the seat that declares it** -- *choosing the
domain is itself a claim.* The rows' significance is untouched.

⭐ **AND THE PRECEDENT IS EXACT, ONE LEVEL UP, IN THIS SAME PROJECT: R-15 ruling 2 made 2917 refusals vanish BY DOMAIN
(the graded corpus MINUS the record trees) RATHER THAN BY EXEMPTION.** `S41` -- disarmed four hours ago on that
ruling, exercised and positively controlled in `S71` -- is this ruling's sibling. **Same shape, same family, same
project.**

### ⛔ THE RISK THIS CREATES, NAMED RATHER THAN WAVED PAST -- and the control that bounds it

**A key template PRODUCES addresses.** Rule 30 says *every S3 address is `address()` output*, so **addresses are
squarely in domain.** ⛔ **If templates leave the NAME grade and nothing else covers them, a wrong template silently
produces wrong addresses forever -- an exclusion that becomes a blind spot is worse than the carding it replaces.**

**SO THE EXCLUSION LANDS WITH A CONDITION, and the condition is the cell's acceptance bar:** the `types_not_graded_by_kind`
entry is admitted **only together with a printed denominator showing that the ADDRESSES those 15 templates produce
remain inside the ADDRESS grade's population.** ⭐ **Out of the NAME grade, still inside the ADDRESS grade -- and the
run PRINTS both counts.** If that cannot be shown, the exclusion is refused and the 15 go back to carding, which is
honest. **COST: one denominator per excluded type. NON-APPLICATION: a type that produces no address at all.**

### This CORRECTS R-60, written by this seat within the hour

R-60 said the 15 violate FWD-5's third ACCEPT clause -- *"a name the check cannot read STOPS THE RUN LOUDLY rather
than being filed as breaking the pattern."* ⛔ **THAT WAS THE RIGHT INSTINCT AND THE WRONG CLAUSE.** That clause
governs **a NAME the check cannot READ** -- ambiguity. These 15 are **perfectly readable; they are not names at
all** -- a CATEGORY error, not an ambiguity. ⭐ **"Stop loudly" is the remedy for a name you cannot parse; "out of
domain" is the remedy for a thing that was never in the population.** Applying the loud-stop clause here would have
made the run halt on 15 rows that never belonged to it.

**The rest of R-60 stands unchanged** -- FWD-5's outcome is the LIST, resolution is the clean-up projects' work, and
`TIMEBOXED_R33` still names the observer.

### What the lane may now cut

**THREE cells, not two:** the 51 two-remedy rows; the 41's `inferred` `owner_claim`; **and `W1-S70` as a DOMAIN cell
implementing this ruled exclusion with its address-coverage denominator** -- not as a choice, which is why it was not
the lane's to make and is not being handed back as one.

⭐ **AND THE LANE'S OWN LINE IS WHY THIS RULING EXISTS AT ALL:** *"I would rather cut two honest ones than four that
include a decision I am not entitled to make."* **A seat that declines to smuggle a decision into a cell is the reason
the decision gets made by whoever owns it.**

---

## R-62 -- R-61's MECHANISM IS WRONG AND ITS GUARD WOULD HAVE PASSED VACUOUSLY. `types_not_graded_by_kind` IS A ROUTING TABLE WHOSE NAME IS THE OPPOSITE OF ITS BEHAVIOUR, AND ITS REAL SWITCH IS A PROSE PREFIX

`2.0.0_SA_COO~G` **HELD** R-61's cell rather than cutting it, and measured the mechanism before writing the order
(msg 97898). ⭐ **It was right on every point, and the cell it declined to cut would have been a no-op wearing a
ruling's authority.**

### Verified here at the bytes, not taken on report

| | |
|---|---|
| `lib/opal_naming.py:493` | `graded_types = set(schema["kind"]["by_type"]) \| set(schema["types_not_graded_by_kind"])` |
| `lib/opal_naming.py:1012` | `self.not_graded = {t for t, why in tng.items() if str(why).startswith("NOT GRADED")}` |

⛔ **`:493` UNIONS THE WHOLE TABLE INTO THE GRADED SET. MEMBERSHIP DOES NOT EXCLUDE ANYTHING -- it means "graded by a
DIFFERENT grammar."** The real exclusion at `:1012` turns on **whether a human-written prose REASON happens to begin
with two particular words.**

**MEASURED, denominator printed: 15 entries -- 8 genuinely leave the grade, 7 are STILL GRADED and merely routed**
(`EVENT_RULE`, `SCHEDULE`, `LOG_GROUP`, `S3_BUCKET`, `S3_BUCKET_POLICY`, **`S3Key`**, `SECRET`). **`S3Key` is already
in the table, with reason `"the key grammar (key)"`, and is GRADED TODAY.**

### What that does to R-61, stated without softening

1. ⛔ **R-61's REMEDY WOULD HAVE CHANGED NOTHING.** "ONE entry with a reason" adds an entry **that is already there**,
   to a table **whose membership grades rather than excludes**. The order would have read correct and produced
   nothing.
2. ⛔ **AND R-61's ACCEPTANCE CONDITION WOULD HAVE PASSED VACUOUSLY.** I required a printed denominator showing the
   templates' ADDRESSES stayed inside the ADDRESS grade. **If nothing is removed from any grade, that count is
   trivially unchanged** -- a green certifying nothing. ⭐ **THAT IS R-47's OWN SHAPE ARRIVING INSIDE THE GUARD I
   WROTE TO PREVENT IT**, and the lane found it by building the arm rather than by reading the ruling.
3. **R-61's REASONING SURVIVES INTACT** and the lane says so: a key format template is a producer's runtime
   substitution field, not a name with a gap, so *"resolve from a declared source"* never applied. ⛔ **What failed is
   the MECHANISM, not the finding** -- and the distinction I drew is between a KEY and a KEY TEMPLATE, **which the
   schema has no field to carry.** `types_not_graded_by_kind` is keyed BY TYPE, and every S3 key shares that type.

### The disposition -- (c) NOW, (b) as round-8 material, (a) REFUSED

**(a) RULE ALL `S3Key` OUT OF THE NAME GRADE -- REFUSED.** It would remove **every S3 key in the estate** from the
grade to fix **15 templates**. Rule 30 makes S3 addresses the core naming surface. ⛔ **This is R-56's
`.gitattributes` overreach again: a class fix whose blast radius vastly exceeds its defect.** *The 15 are TEMPLATES;
`S3Key` is EVERY KEY* -- the lane's sentence, and it is decisive.

**(b) ADD A MECHANISM DISTINGUISHING A TEMPLATE FROM A KEY -- RIGHT, AND NOT NOW.** It is a schema change, and Rule 24
requires a four-postulate record plus a word-boundary token census for any value-enum proposal. **That is its own
cell with its own surface -- ROUND 8 MATERIAL, never a rider on round 7.**

**(c) LEAVE THE 15 CARDED, WITH A TRUE REASON -- ADOPTED, and it is strictly better than the status quo even standing
alone**, exactly as the lane said: ⭐ **the present card says THE TOKEN IS NOT A SYSTEM; the truth is THE ROW IS NOT A
NAME.** Re-carding under the true reason costs one field, changes no grading behaviour, and stops every later census
re-deriving a question that was already answered. **The 15 remain a NAMED FWD-5 GAP rather than a timebox artifact.**

**So round 7 stays TWO cells, as the lane already cut it.** Nothing waits on this.

### ⛔ THE FINDING THAT OUTLIVES ALL THREE OPTIONS: A PROSE FIELD THAT IS SECRETLY A CONTROL FLAG

**The exclusion switch is `str(why).startswith("NOT GRADED")` -- a REASON string written by a human for a human.**

⛔ **SO REWORDING A REASON SILENTLY CHANGES GRADING BEHAVIOUR.** Turning *"NOT GRADED: AWS-issued identifier"* into
*"AWS-issued identifier, not graded"* -- an improvement in ordinary prose -- **puts that type BACK INTO THE GRADE, and
nothing announces it.** Eight types currently sit on that knife edge.

⭐ **AND THE FIELD'S NAME IS THE OPPOSITE OF ITS BEHAVIOUR**, which is why a CTO reading it reached for it as an
exclusion mechanism and was wrong: **7 of its 15 members are graded.** ⛔ **A name that contradicts its behaviour is
worse than an unnamed field, because it is CONFIDENTLY misread** -- and it was, by this seat, in a ruling.

**This is NOT fixed here.** Renaming the field or promoting the switch to a typed boolean is a schema act under Rule
24, and it belongs with (b). **It is recorded so the next reader does not repeat the misread**, and so that anyone
editing a reason string in that table knows they are editing a control.

### What the lane did that the ruling records by name

⭐ *"R-61's condition is what made me measure. I went looking for the address population to build the arm, found the
exclusion list, found `S3Key` already in it, and only then read the two consumers. A ruling that had simply said
'exclude them' would have been executed."*

**A GUARD THAT FAILED TO CATCH THE DEFECT STILL CAUSED IT TO BE FOUND, because it sent someone to build an arm.**
⛔ **That is the third ruling of mine tonight corrected by a lane that measured before executing** -- and the count
matters more than any of the three: **the estate's rulings are being executed by seats that verify them first, which
is the only reason a wrong mechanism cost nothing.**
