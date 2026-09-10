# TO NFRA_CLDGRPH.TO-CG-G-3 -- CG-s-34 (ADDED at decomposition v0.10 on the CTO's round-6 analysis @d5c24a4dce s.6 item 4): THE SUBSTRATE CARD FOR A PRODUCER THAT READS BACK ITS OWN OUTPUT -- Rule 28's seven questions with A ROW PER CARRIER (nodes, props, edges), because the same question got three different correct answers and each was found in a different cell

<to_id>NFRA_CLDGRPH.TO-CG-G-3</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~2</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<status>complete -- 2026-09-10T05:07Z by 0.9.0_WK_NFRA_CLDGRPH~2 on branch wk-cldgrph-7-2 (worktree C:/tmp/wk-cldgrph-7-2, cut from CLOUD @f3b5f26f77), push state LOCAL. G3-AC1 PASS (INSTANCES_REGROUNDED=3 of 3, EVIDENCE_FROM_RECORD=true, 21 of 21 checks over a 245-row channel parsed block by block), G3-AC2 PASS ON A SUBSTITUTED INSTRUMENT (the named .tools/validate-json-schema.py does not exist; .tools/substrate-card-check.py reads violations=0 and VALID on 4 of 4 cards, and it binds SUBSTRATE_CARD.v3.1.schema.json rather than the v1 schema this face names -- row NFRA_CLDGRPH-W2-S73), G3-AC3 PASS (CARD_ROWS=3 of 3, QUESTIONS_PER_ROW=7 of 7, OWNER_PER_ROW=3 of 3, FAILURE_MODE_DISTINGUISHABLE=3 of 3 over 21 rows), G3-AC4 PASS (SHRINK_MASKED true on 955 -> 137, false on the fixed-emission pair, PROBE_CONTROL=FIRED 6 of 6), G3-AC5 RECORDED as UNVERIFIABLE-BY-INSTRUMENT for 3.0.0_SA_CVO at L9. Proof instance org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-G-3.archive-read-substrate-card.proof_of_spec.json VALID, proof-of-spec-check rc 0. Rows W2-S73, W2-S74, W2-S75 filed; channel 245 -> 248 in 186 -> 187 blocks, no row edited. Egress hold observed in full: no AWS call of any kind. Acts at 40a76d3fea; this flip rides the instance commit.</status>

## STANDING LAW (inlined)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~2; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~2 <0.9.0_WK_NFRA_CLDGRPH~2@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state LOCAL.
- **Write surface = the PATHS block + `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/`.** The card folder and your own deliverables folder are yours to WRITE; all producer code is READ ONLY and slot ~1 holds it. Every script and capture carries `g2_`. Scratch `.scratch/`.
- **Surprise = ONE ROW** (`NFRA_CLDGRPH-W2-S<k>`, from S1; `surfaced_at` a REAL minute, never an `x`; restate the denominator by parsing every fenced json block; never edit an existing row; keep working).
- **Every criterion invocation under `timeout 120`.** Non-ASCII refused in code, logs and captures (`OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`).
- **THE EGRESS HOLD, THE HARDEST LINE IN THIS ORDER.** CLAUDE.md excludes ALL EGRESS OFF OPAL INFRASTRUCTURE from standing agent autonomy, and the CTO recorded that ground at 94951. Every globgrph ECS derive publishes `[SEV1][PAGE]` and `[SEV2][digest]` to `opal-critical-surface-alerts`, which carries a LIVE SMS SUBSCRIPTION TO A PERSONAL MOBILE (issuer-measured 2026-09-10 03:3xZ; rows W2-S72, S104, S106, RESERVED FOR ANDREW). **THEREFORE, IN THIS ROUND: NO ecs run-task, NO CodeBuild start, NO image build or push, NO digest re-pin, NO safe-apply, NO zip push to `stitch-source/`, and NO act whose effect is an SNS publish.** The 02:00Z and 03:00Z scheduled fires are the estate's own and are NOT yours to stop, start or imitate. If your accept seems to need one, it does not: read the section that says so, and if you still think it does, that is a BLOCKING row and a report, never a run.
- **NEVER:** build or propose any alert, alarm, SNS, SES, notification, freshness-checker or monitor (standing moratorium); unsubscribe, edit or otherwise touch any subscription or topic; write to S3 at all; `2>/dev/null` on a verdict-bearing read; bare `git commit`; `git log -- <path>` for a provenance question (use `--full-history`); edit any producer file (slot ~1 holds them concurrently under CG-s-33);
- **Search rail:** `python .tools/comp-read <file> --for "<question>"` and `python .tools/comp-find '<pattern>' <pathspec> --limit N`; raw recursive grep/find is refused by the hook; a `cmd | grep` receiver is free.
- **Instruments:** `jq` is absent -- read JSON with python. `.tools/aws` is CLI v1 and emits CRLF on `--output text`: strip CR before any field test. A pipeline's rc is its LAST command's.

## THE CELL (decomposition v0.10 s.1a; the CTO's round-6 analysis s.6 item 4 and s.7)

*"The archive carry-forward substrate card -- A ROW PER CARRIER, because the same question got three different correct answers on nodes, props and edges, each found separately, three cells apart. Rule 28 says every row carries its owner because remedies do not move together; this is that rule earning its keep."*

And the lesson the card must make testable, from s.7: **"A producer that reads back its own output is silently idempotent under a FIXED emission and silently WRONG under a SHRINKING one -- which is exactly what a nightly with stable counts cannot surface."**

## MEASURED BY THE ISSUER AT THE CUT -- the three instances, each with its own evidence

- **NODES** (`W2-S61`): the producer re-archives its own reader's input. Carried by the CTO as a Rule 28 substrate-card question at round 6's mid-point.
- **PROPS** (`W2-S69`): the retired `vocabulary=stitch-v1` stamp arrived from the archived snapshot AFTER the fold's writer was retired; `_collapse_stitch_copies`'s tie-break kept the archived copy once `retyped_prior_cycle` went empty. Fixed in cycle 3.
- **EDGES** (`W2-S71`): `derive_runner` folds `STORED_IN` in and archives the graph; `derive_stitch` reads that snapshot back, so last night's 955 arrived before this run emitted anything. Visible ONLY because cycle 4 emitted 137 where the snapshot held 955. Fixed in cycle 4.
- Three cells, three separate discoveries, one mechanism. `STORED_IN` is this producer's own edge type and nothing else in the estate writes one, so an arriving `STORED_IN` is by construction a previous cycle's output.

## CUT DISCIPLINE (spine v3.8 @9fc8cb266e, and it binds YOUR captures)

Every accept below names its instrument's COVERAGE, its harness's GRAIN, and the ENVIRONMENT its stored baseline came from. Print all three beside every number: what population the instrument swept and its denominator, at what grain the number is counted, and where the comparison value came from. A count without its denominator is refused at the flip, and so is a denominator that does not say what it excluded.

## DELIVERABLE -- in this order

1. `g2_card_evidence.py` -- re-ground each of the three instances from the RECORD rather than from this face: the row, the fixing commit, and the number that made it visible. A card built on a summary is a card about a summary.
2. The card at `org/missions/D0/NFRA/NFRA_CLDGRPH/cards/stitch-producer-archive-read.card.json`, validating against `org/standards/SUBSTRATE_CARD.schema.json`, with **one row per carrier** -- nodes, props, edges -- each carrying all seven questions across the three grains (PROCESS: methodology, cadence desired-vs-applied; ARTIFACT: persistence/authority, exact location; TRUST: coverage + denominator, key/identity space, failure mode distinguishable from a genuine negative) and **its own owner**.
3. `g2_shrink_probe.py` -- make the lesson TESTABLE rather than quotable: a probe that, given two successive emissions, reports whether a shrink would be masked by the archive read. Exercise it on the round's own numbers (955 -> 137) as the positive case and on a fixed-emission pair as the negative.
4. The record `CG-s-34.archive-read-substrate-card.result.md`, then the instance, then the flip.

## ACCEPTANCE (v3 grammar)

<criterion id="G3-AC1" cell_refs="CG-s-34"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/g2_card_evidence.py</invocation><expect>INSTANCES_REGROUNDED=3 of 3[\s\S]*NODES=NFRA_CLDGRPH-W2-S61[\s\S]*PROPS=NFRA_CLDGRPH-W2-S69[\s\S]*EDGES=NFRA_CLDGRPH-W2-S71[\s\S]*EVIDENCE_FROM_RECORD=true</expect></criterion>
`G3-AC1` -- THE THREE INSTANCES, RE-GROUNDED FROM THE RECORD: each row read at its commit, each fix located, each visible-making number reproduced -- not restated from this order's own prose.

<criterion id="G3-AC2" cell_refs="CG-s-34"><invocation>timeout 120 python .tools/validate-json-schema.py org/standards/SUBSTRATE_CARD.schema.json org/missions/D0/NFRA/NFRA_CLDGRPH/cards/stitch-producer-archive-read.card.json</invocation><expect>VALID</expect></criterion>
`G3-AC2` -- THE CARD IS A CONTRACT, NOT PROSE: it validates against the estate's own substrate-card schema. If the estate has no such validator at that path, find the one it does have, use it, and file a ROW naming what you used -- do not hand-check a schema.

<criterion id="G3-AC3" cell_refs="CG-s-34"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/g2_card_rows.py</invocation><expect>CARD_ROWS=3 of 3 carrier\(s\)[\s\S]*QUESTIONS_PER_ROW=7 of 7[\s\S]*OWNER_PER_ROW=3 of 3[\s\S]*FAILURE_MODE_DISTINGUISHABLE=3 of 3</expect></criterion>
`G3-AC3` -- A ROW PER CARRIER, EACH COMPLETE: three rows, seven questions each, an owner each, and question 7 answered concretely on each -- how this carrier's failure is told apart from a genuine negative.

<criterion id="G3-AC4" cell_refs="CG-s-34"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/g2_shrink_probe.py</invocation><expect>SHRINK_MASKED=true on \(955 -> 137\)[\s\S]*SHRINK_MASKED=false on the fixed-emission pair[\s\S]*PROBE_CONTROL=FIRED</expect></criterion>
`G3-AC4` -- THE LESSON, MADE FALSIFIABLE: the probe reports masking on the round's own shrink and no masking on a fixed emission, with a control -- so the sentence in the analysis becomes a check somebody can run instead of a thing everybody agrees with.

<criterion id="G3-AC5" cell_refs="CG-s-34" judgment="true"/> `G3-AC5` -- THE READING: whether the three carriers really need three owners or whether one remedy moves all of them (the card's own premise, tested rather than assumed); what a fourth carrier would look like if one exists; and what this card obliges of anyone who next builds on this producer. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>G3-AC1, G3-AC2, G3-AC3, G3-AC4, G3-AC5</expected_criteria>

## SURFACES

`org/standards/SUBSTRATE_CARD.schema.json` (the contract) - rows `W2-S61`, `W2-S69`, `W2-S71`, `S103` (READ: the three instances) - `ledger/ROUND_ANALYSIS.round6.md` s.4 and s.7 (READ: the mechanism and the lesson) - `infra/aws/globgrph/derive_stitch.py` and `derive_runner.py` (READ ONLY: the archive write and the archive read; slot ~1 holds these files under CG-s-33 -- you do not edit them).

## BOUNDS

- **READ ONLY on all code.** Slot ~1 is editing the two producer files under CG-s-33 concurrently; you read them and never write them.
- **No alert, monitor or checker is built** by the shrink probe: it is a one-shot instrument in your own deliverables folder, run by a human or a criterion, wired to nothing.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/cards/
org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-G-3.archive-read-substrate-card.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.10 (the round-7 recut), cell CG-s-34 (s.1a; ADDED on the CTO's round-6 analysis @d5c24a4dce s.6 item 4).
<owned_cells>CG-s-34</owned_cells>
Read-dependencies, NOT claimed: CG-s-31 (TO-CG-F-11, drained @d2ee75c98b -- the three instances are its rows). CONCURRENT, NOT yours: CG-s-32 and CG-s-33 (slot ~1).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25) and unchanged since; the C3 moratoria bind BOUNDS, and tonight's egress hold binds harder.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs no AWS write, no principal, policy or grant change; its only AWS contact is a read.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 (rc 0 @07288006e5); the L9 seat's compose is the deliverable's context.
comp-find: RUN at the cut by the issuer for the round-7 population; the worker re-runs it inside its own criteria where a denominator is claimed.
</preflight>

<proof_of_spec>
Criterion ids: `G3-AC1`..`G3-AC5`. Instance at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-G-3.archive-read-substrate-card.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> G3-AC1,G3-AC2,G3-AC3,G3-AC4,G3-AC5` BEFORE the flip; rc 0 AND every mechanical row PASS. `G3-AC5` is `judgment="true"`: `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming `3.0.0_SA_CVO`; **`PASS`/`FAIL` on it is INVALID.** Two commits at the flip (the acts, then the instance + the status). A VALID instance is not a met order: if any mechanical row reads FAIL, the order STAYS OPEN, `<status>` is NOT flipped, and you report.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE ANY ACT: `python .tools/comp-read org/standards/SUBSTRATE_CARD.schema.json --for "the required fields of a substrate card row and how owner is carried"`; `python .tools/comp-read org/missions/D0/NFRA/NFRA_CLDGRPH/ledger/ROUND_ANALYSIS.round6.md --for "the mechanism in s.4 and the lesson in s.7, verbatim"`; `python .tools/comp-find 'SUBSTRATE_CARD|substrate.card' org/standards org/missions .tools --limit 30`.
</compiler_tools_mandate>
