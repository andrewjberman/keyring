# ADVI_FIRMBKTS task order -- `FB-e-3` -- BLIND READER B

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R2.md</decomp_doc>
<owned_cells>FB-e-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~6</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change and no AWS act; the cell reads one JSON file and standards documents.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~B1) on dell1 -- r2_reader.py 0 of 2 at base (answers file absent); 2 of 2 on a full answer set; 1 of 2 with one id missing. Blindness: the lens cannot see which files a reader opened; the face's OPENED line is the only witness.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-e-3` (round 2, enrichment item 1)

You are one of two people reading the same list of storage locations, working alone. You have never seen these locations
before and you do not know where they came from. For EACH location in
`org/tier1_exec/2.0.0_SA_COO~B1/round2/blind/LOCATIONS.json` (`{"locations": [{"id", "location"}]}`, 418 entries) you say,
from the location string and the naming standard alone:

| field | what to write |
|---|---|
| `system` | which system made it: a product (`advi`, `irpt`, `mdpf`) or a vendor (`blackdiamond`, `schwab`, `orion`, `eclipse`, `smartx`); `unknown` if the string does not tell you |
| `firm` | whose it is, in the long form (`49financial`, `inflection`, `cottonwood`); `unknown` if the string does not tell you |
| `tier` | how finished it is: `bronze`, `silver`, `gold`, `platinum`, `state` or `code`; `unknown` if the string does not tell you |
| `table` | the table or served family it holds: ONE lowercase token, exactly as it appears in the string's table slot, or `unknown` |
| `contents` | one plain-English sentence, 15 words at most, of what the object holds |

**A guess is not an answer.** Where the string does not tell you, write `unknown` in that field; the grade counts an
`unknown` as no agreement and a wrong word as a worse one.

### 1a. How to read

- The standard key grammar is `{source}/{scope}/{tier}/{table}/{partition}` under a bucket. The grammar and its
  vocabularies are in `org/standards/NAMING_SCHEMA.json` and `infra/logic/02_DOCTRINE.md`; the registry rows are in
  `infra/logic/registry/`. These three, and nothing else, are your references.
- Some strings follow the grammar; some are older and do not. Read each string yourself and decide its answers. **Do not
  write a program that parses the strings and fills the answers**: a parse measures the program, not the location. A short
  script may be used ONLY to write your finished answers into the output file.
- You work ALONE. Another reader answers the same list; its file is `ANSWERS_A.json`. Do not open it, and do not open
  any file that is not named in this section or in section 3.

### 1b. The output

`org/tier1_exec/2.0.0_SA_COO~B1/round2/blind/ANSWERS_B.json`:

```json
{"reader": "0.9.0_WK_ADVI_FIRMBKTS~6",
 "answers": [{"id": "<the location's id>", "system": "...", "firm": "...", "tier": "...", "table": "...", "contents": "..."}]}
```

Exactly one answer per id, all 418, every field a non-empty string. `indent=1`, `ensure_ascii=True`, LF endings.

## 2. BOUNDS

1. Open ONLY: `LOCATIONS.json` in the folder above, `org/standards/NAMING_SCHEMA.json`, `infra/logic/02_DOCTRINE.md`, and
   files under `infra/logic/registry/`. Open nothing under `org/missions/`, nothing under `org/tier1_exec/` except the folder
   above, nothing under `docs/`.
2. Your checkout withholds this project's own folders on purpose. If a path section 1 names is absent, STOP and report
   BLOCKING; never rebuild or fetch the tree.
3. No AWS act. No other write than section 3.
4. Do not file a surprise row (the channel file is not in your checkout). A surprise goes in your final report under
   BLOCKING or OBSERVED, in one line.

## 3. SURFACES

<paths>
org/tier1_exec/2.0.0_SA_COO~B1/round2/blind/ANSWERS_B.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~6/
</paths>

Read-only: `org/tier1_exec/2.0.0_SA_COO~B1/round2/blind/LOCATIONS.json` and `r2_reader.py` (the grader, same folder),
`org/standards/NAMING_SCHEMA.json`, `infra/logic/02_DOCTRINE.md`, `infra/logic/registry/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
  <criterion id="AC1" cell_refs="FB-e-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/tier1_exec/2.0.0_SA_COO~B1/round2/blind/r2_reader.py" --reader B; echo "exit=$?"</invocation><expect>ROUND 2 READER B: 2 of 2 arms</expect></criterion>
</proof_of_spec>

Agreement between the two readers is NOT graded here; it is the issuer's real run at the round's close.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~6/ADVI_FIRMBKTS.TO-FB-e-3.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 passes. Report
once, and add two lines to the usual report: `OPENED:` every file you opened other than the four named in section 2
(write `none` if so), and `METHOD:` in one sentence how you produced the answers. Report the counts of `unknown` per
field and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1's readers answered by script and reader B opened worker ~1's proof file (row
ADVI_FIRMBKTS-D1-S3). Round 2's controls: the list carries 8-hex opaque ids and nothing else; the face names no project
document; the reader's checkout is sparse (the project's folders are withheld; its own deliverables folder, its order and
the decomposition are present so the proof checker and the lane gate run); its grader sits beside the list. What holds
the independence is the reader's own OPENED line: the claim is `held`, not `measured`. The arm map is
`deliverables/2.0.0_SA_COO~B1/round2/READING_KEY.json`; r2_agree.py grades the pair at close. Spawned in its own slot,
never continued from another reader (reader A is slot ~5).

# pipeline-override: the one refusal is LIMB PRD_HEADER.fabric='laptop' vs the register's 'dell1'. The register row is the authority since 1.0.0_SA_CTO's L3 re-placement @8afcb0f851; the PRD header repair is the CTO's. Every other limb passed in the issuer's dry run.
<status>pending</status>
<round>2</round>
<to_id>ADVI_FIRMBKTS.TO-FB-e-3</to_id>
<slot>~6</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
