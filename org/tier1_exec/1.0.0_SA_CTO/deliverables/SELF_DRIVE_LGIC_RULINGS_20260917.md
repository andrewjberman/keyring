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
`S25R4-AC5`. **L10's order is load-bearing: round 5 is cut AFTER round 4's slug, never beside it** (LD-0521 -- the
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
