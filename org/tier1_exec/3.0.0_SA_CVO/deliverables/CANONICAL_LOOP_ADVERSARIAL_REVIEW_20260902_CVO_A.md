# Canonical loop adversarial review -- CVO lane A

**Author:** `3.0.0_SA_CVO~A`  
**Date:** 2026-09-02  
**Order:** CTO message 92550; evidence amendments 92558, 92561, 92563, 92574, 92583  
**Reviewed design:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CANONICAL_LOOP_REMEDIATION_DESIGN_20260902.md`  
**Verdict:** **RED / HOLD.** Do not activate site Z, integrate or push `ETFS_GUARDRAIL`, cut its first TO, or report the canonical loop complete. R4-a is good. R4-b is described in the schemas but is not implemented by the gate, existing-row mutations bypass both gate and watcher, and the proposed scope-change qualification is not deterministic.

## Findings

### P0-1 -- R4-b's claimed identity enforcement does not exist

The two schemas now admit optional `project` and `fabric` fields and their descriptions say the gate requires them on new rows and cross-checks them against `id` (`investigation_item.schema.json:21-31`; `remediation_row.schema.json:23-33`). The executable gate does neither. `_check_row` checks top-level required keys and top-level enums, then only the step-7 fields, ARMED owner, route/target mapping and scope-change ref (`.tools/surprise-row-gate.py:118-184`). There is no project/fabric branch.

Two non-persisted controls exercised the seam:

1. A schema-shaped new site-Z investigation row with neither `project` nor `fabric` produced **0 gate violations**.
2. The same row with `id=ETFS_GUARDRAIL-Z-S999`, `project=WRONG_PROJECT`, and `fabric=laptop` also produced **0 gate violations**.

The defect is broader than those two fields. A control carrying an invalid UTC timestamp, invalid nested grounding status, empty graduated evidence, and the same mismatched identity produced **0 gate violations** from `_check_row`; the Draft-07 validator produced four. The gate's manual top-level walk does not enforce nested enums, patterns, `minLength`, or `allOf` conditions. In particular, the protocol's central rule that `GRADUATED` requires GROUNDED plus evidence (`SURPRISE_CHANNEL_PROTOCOL.md:44-53`; schema `:112-138`) is bypassable.

**Required consequence:** call the Draft-07 validator on every new row, then add explicit cross-field project/fabric consistency checks because JSON Schema currently only describes, but does not encode, that relation. Add positive and negative controls for absent identity, wrong project, wrong fabric, invalid timestamp, and GRADUATED-without-grounded-evidence. Until those controls go red-before-green, R4-b is not landed.

### P0-2 -- append-only is prose, not a control; the watcher is blind to same-count rewrites

The protocol requires corrections as new items and forbids editing an existing row in place (`SURPRISE_CHANNEL_PROTOCOL.md:29-33`). The gate computes `old_ids`, selects only rows whose ID is absent from HEAD, and checks only that `added` set (`surprise-row-gate.py:195-218`). A changed or deleted existing ID is not checked. The watcher compares only row counts (`surprise-watch.sh:122-145`); a same-ID content change leaves the count unchanged and emits nothing.

The corpus contains the exact failure mode: three authors put lifecycle prose into an existing enum field. Whether those edits predate the current gate does not change the prospective falsifier: the current gate and current watcher would both miss the same edit today.

**Required consequence:** reject changed/deleted existing row payloads by canonical row hash, except an explicit audited override; require a correction to append a new ID citing the old one. The watcher should watermark IDs plus hashes, not counts alone, and emit a mutation warning if a known ID changes or disappears.

### P0-3 -- R8-a is an adjudication ladder, not a deterministic classifier

R8-a says that whether a remedy “fits inside” an existing TO, cell, or named outcome is not a judgment call (`CANONICAL_LOOP_REMEDIATION_DESIGN_20260902.md:199-214`). No executable field or reference proves “fits.” A broad TO can plausibly contain a remedy while its decomp omitted the needed cell; a remedy can plausibly serve more than one outcome. Asking the questions in order makes the result repeatable only after the semantic judgment has already been made.

Keep the order, but name it honestly: **adjudication ladder with machine-checkable evidence**. Make each result carry the artifact whose existence can be checked:

- `SPEC_ERROR`: exact existing TO obligation or decomp-cell reference;
- `DECOMP_INVALIDATING`: exact existing `FWD-n` plus a required description of the missing cell;
- `SCOPE_CHANGE`: the scope-change kind and the outcome payload below.

The gate can check reference syntax, referenced-object existence, and route/target consistency. It cannot establish the semantic proposition “this remedy serves that outcome”; the deciding seat remains accountable for that judgment.

### P0-4 -- reject `FWD-NONE`

`FWD-NONE` makes an outcome identifier carry the absence of an outcome. It corrupts the permanent `FWD-<n>` namespace, makes a non-reference look like a reference to generic consumers, and forces every consumer to remember a sentinel exception. The current hole is real (`surprise-row-gate.py:167-183`; design `:216-237`), but overloading the identifier is not the remedy.

Use a separate field:

```json
{
  "route": "SCOPE_CHANGE",
  "scope_change_kind": "CONTRADICTS_NAMED_OUTCOME | REQUIRES_UNNAMED_OUTCOME",
  "outcome_ref": "FWD-12 | null",
  "proposed_outcome": "required only for REQUIRES_UNNAMED_OUTCOME"
}
```

For `CONTRADICTS_NAMED_OUTCOME`, require a real `^FWD-[0-9]+$`. For `REQUIRES_UNNAMED_OUTCOME`, require the `outcome_ref` property with value `null` plus usable `proposed_outcome` text. Required-null distinguishes intentional absence from a missing field without minting a false ID. The filer does not allocate an outcome number; step 2 does that at the next unused number.

## R2 -- lens adjudication

### `comp-similar`: ADMITTED

The original refusal ground is discharged on this device. Independent exercise produced:

- `--self-test`: 9/9, including vintage and headerless/absent controls;
- `cluster`, pairwise query, and `supersede`: each printed its own Kuzu corpus vintage and coverage denominator;
- a failed subject resolution returned an explicit non-answer rather than a false clean result.

Admission is bounded to a version whose own disposition line renders both vintage and denominator. The vintage dates the Kuzu corpus, not the AWS estate. A resolution failure is UNRUN/non-answer. Evidence basis: repair `b8a73cc064`; workflow amendment `SPEC_CANONICAL_LOOP_INCORPORATION_20260901.md:185-224`.

### `comp-adversary`: SUBSTANTIVELY FIT; EFFECTIVE ADMISSION HELD

The tool's output property survives exercise: self-test 5/5; direct stage-4 packet battery 7/7; cited-path, uncited-sibling, selected-set and complement-source denominators are explicit; zero-pin is disclosed as `0 of 0`, not clean. The tool is deterministic, local and read-only. Current tool change is `8ed23144cb`; packet battery is `1f4bc0e513`.

But the standard runner cannot consume its battery. Independent command:

```text
python -m pytest -q .tools/tests/test_comp_adversary_stage4_packet.py
7/7 module battery prints PASS
pytest INTERNALERROR at line 151: SystemExit: 0
no tests ran in 89.35s
process exit 1
```

Therefore approve the lens's substantive membership but do not make admission unqualified/effective until the isolated module-scope `sys.exit()` repair is collectible and green under the estate runner. CTO placed that repair with `0.8.0_AE_CloudComp` under CTO gate (92583). The ownership map independently parses as 59 lanes and 254 path rules with zero `.tools/tests` claim; this structural ownership gap is real, but this review does not mint a lane.

There is also a law/code mismatch to resolve explicitly: the workflow lists seven admitted lenses and merely bounds `comp-adversary` (`CANONICAL_FABRIC_WORKFLOW_20260901.md:92-102`), while the TO gate already makes `comp-adversary` one of three mandatory dispositions (`.tools/to-pipeline-gate.py:44-46,111-140`). The spec must distinguish:

1. the **admitted catalog** (tools lawful to select), and
2. the **mandatory core** (tools every new TO must disposition).

Do not call all admitted lenses mandatory unless the gate enforces that claim. Do not call the current three-tool gate evidence that the nine-lens catalog ran.

### Binding clarification after COO 92612 -- the hold has no truthful disposition shortcut

`DECLARED-NOT-APPLICABLE` is not a lawful bridge around held admission. The gate defines non-application at the subject grain: a lens whose named subject has no population owes no denominator and may declare that reason (`.tools/to-pipeline-gate.py:56-60`). A pytest-collectability/admission hold is battery-readiness at a different grain; it does not make an otherwise applicable lens inapplicable. Marking it `RUN` would likewise nullify the effective-admission hold.

Therefore, until RC5 makes `comp-adversary` admission effective, an applicable `comp-adversary` has no truthful legal disposition under the current mandatory-core gate and **no new canonical TO may be cut through that collision**. If a TO must be cut before RC5 lands, the gate owner must align code and law explicitly; COO must not encode readiness as subject non-applicability. The `comp-similar` admission remains separately bounded: a seat must observe its vintage line render before citing its output because `b8a73cc064` is not guaranteed on an origin-only checkout.

## F2 -- no fifth `disposition`; add an orthogonal resolution axis

The design's population statement needs one correction. The 192-row full-corpus pass has four failures, but only **two** are disposition failures. `ETFS_POSITIONING-S14` fails `hazard_standing`, not `disposition`; its disposition remains `GRADUATED` (`ETFS_POSITIONING/INVESTIGATION_v1.md:350-370`). That datum is decisive: an item can remain historically GRADUATED while a later event removes its live obligation. Replacing its disposition with a fifth value would erase where it went next and violate the axis's declared intent (`SURPRISE_CHANNEL_PROTOCOL.md:133-146`).

**Decision:** preserve the four disposition values. Add a separate `obligation_resolution` axis. Candidate values:

```text
OPEN | FALSE_AT_SURFACE | REMEDIATED | OVERTAKEN_BY_EVENTS | CLOSED_OTHER_WITH_REASON
```

Rule-24 record:

- **Declared domain:** the current action obligation carried by one investigation item.
- **One intent:** why that obligation remains open or ceased. Not where the item routes, not interruption right, not initial hazard standing.
- **Grain:** one investigation item at the time its obligation status is recorded.
- **MECE:** still owes action -> `OPEN`; no valid obligation ever existed -> `FALSE_AT_SURFACE`; deliberate remedy discharged it -> `REMEDIATED`; later external events discharged it without recorded remedy -> `OVERTAKEN_BY_EVENTS`; every remaining closure -> `CLOSED_OTHER_WITH_REASON`, with reason required. These branches are disjoint by cause and exhaustive by the reason-bearing residual.
- **State coherence:** `OPEN` keeps the routed obligation live; `FALSE_AT_SURFACE` requires correction/withdrawal evidence; `REMEDIATED` requires remedy evidence; `OVERTAKEN_BY_EVENTS` requires event evidence and forbids claiming remediation; the residual requires a reason. None changes `disposition`.

Word-boundary census over the existing `disposition` plus `hazard_standing` carriers, 191 investigation rows:

```text
disposition exact: GRADUATED 121; UNDER_INVESTIGATION 61; DISMISSED_WITH_REASON 7;
                   prose-invalid 2; DECOMP_INVALIDATING 0
standing exact:    INERT 108; ARMED 82; prose-invalid 1
OVERTAKEN 2 tokens / 1 row; FALSIFIED 3 / 2; RETIRED 3 / 1;
DISARMED 4 / 2; REMEDIATED 3 / 2; WITHDRAWN 1 / 1;
FALSE-WHEN/AT-(WRITTEN|SURFACE) 3 / 2.
```

The census shows at least three intents in the prose overflow: truth at filing, later world change, and disarm/remediation cause. One fifth disposition value cannot hold them coherently. Normalize `D1_CATVIEWS-S8` and `ETFS_INGEST-Z-S37` to legal route dispositions plus the new resolution value; keep `ETFS_POSITIONING-S14`'s legal `GRADUATED` disposition and move later-event prose out of `hazard_standing`.

## F1 -- establish a standing full-corpus pass

Independent Draft-07 extraction/validation over every JSON fence reproduced:

```text
19 documents; 192 rows; 0 malformed blocks; 4 failures
D1_CATVIEWS-S8        disposition enum
ETFS_INGEST-Z-S37     disposition enum
ETFS_POSITIONING-S14  hazard_standing enum
POSN_TENANCY-S3       surfaced_at pattern
```

**Decision: yes.** Run a full-corpus validation on every surprise-channel change and in standing status. Preserve prospective adoption by baselining the exact legacy failure tuples `(id, JSON pointer, failure digest)`, not merely the count `4`; fail on any new failure or mutation of that set. Report document, row, malformed-block, and failure denominators. Retire the baseline exceptions to zero under explicit CVO-owned normalization; do not make four known legacy rows block unrelated appends in the interim.

## Monitor decisions

### R3 -- conditionally accept notifier-only narrowing

Do not auto-cut a TO or auto-start decomposition: that would create a second dispatch path outside step 6. But Andrew's “sent to COO immediately for decomposition” is not satisfied by an stdout ping. The commit trigger must durably deliver the exact PRD identity, version and commit SHA to COO, then retain/re-offer until COO ACKs receipt and begins disposition. `SENT != EMITTED != READ` (`CLAUDE.md:167-168`; `surprise-watch.sh:32-33`). Define and validate the PRD header schema before building the monitor.

### R4-c -- reject extension until P0-1 and P0-2 close

The current watcher is safe in one important respect: it does not mutate the watched files. It is not yet an indexed-row monitor. It counts regex-shaped ID lines and emits project directory, delta and path (`surprise-watch.sh:62-68,122-145`); it does not parse or emit `project`, `fabric`, `id`, `class`, or `hazard_standing`. Extending it atop unenforced identity fields would make wrong grouping precise. First fix row validation and mutation detection, then extend the existing process rather than build a second watcher.

### R7 -- accept one router process, conditionally

One process with route-derived destinations is the right shape, and `route -> loop_target` consistency is already checked for new remediation rows (`surprise-row-gate.py:153-166`). Build only after R8's payload is repaired and existing-row mutation is guarded. Delivery must be durable and addressed to the exact owner; routing success is recipient ACK, not monitor emission. The process may notify and re-offer. It must not decompose, re-cut, or re-align on the recipient's behalf.

## Release conditions

The hold lifts only when all of these are measured green:

1. full Draft-07 new-row validation plus project/fabric required-and-consistent controls;
2. append-only enforcement and ID/hash-aware watcher controls;
3. scope-change kind with real `FWD-n` or required-null, never `FWD-NONE`;
4. standing 192-row corpus validator with exact legacy baseline and delta refusal;
5. `comp-adversary` battery collected by the standard runner with a real test denominator;
6. workflow and TO gate agree on admitted catalog versus mandatory core;
7. R3/R4-c/R7 delivery tests distinguish emitted from recipient ACK.

R4-a's site-Z ID-pattern widening remains accepted. It is necessary, but it is not sufficient for site-Z activation.

— 3.0.0_SA_CVO
