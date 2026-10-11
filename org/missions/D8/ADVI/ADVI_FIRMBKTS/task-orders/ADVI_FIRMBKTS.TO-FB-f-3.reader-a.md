# ADVI_FIRMBKTS task order -- `FB-f-3` -- BLIND READER A (PROJECT-FREE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~13</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change and no AWS act; the cell reads one JSON file in its own directory.
comp-adversary: RUN by the issuer -- r3_reader.py 0 of 3 at base (answers absent); 3 of 3 on a full fixture answers file; 2 of 3 with one extra file in the directory. Blindness: the lens cannot see which files a reader opened beyond the directory; the `OPENED:` line is the only witness.
EGRESS CLASS, declared: NONE.
</preflight>

## THIS ORDER IS THE ONE EXCEPTION TO YOUR STANDING TREE-PRESENCE BAR

Your directory is `C:/dev/wk-firmbkts-reader-a`. It is deliberately NOT a checkout: it holds only `LOCATIONS.json`. You will
find no `org/` and no `.tools/`, and that is correct. Do NOT run the `test -d org && test -d .tools` check, do NOT stop on
its absence, and never rebuild, fetch or extract a tree. Do not write a surprise row (the channel file is not in your
directory); a surprise goes in your final report under BLOCKING or OBSERVED, in one line.

## 1. THE CELL -- `FB-f-3` (round 3, enrichment item 4; PRD F3)

You are one of two people reading the same list of storage locations, working alone. You have never seen these
locations before and you do not know where they came from. For EACH location in `C:/dev/wk-firmbkts-reader-a/LOCATIONS.json`
(`{"locations": [{"id", "location"}]}`, 418 entries) you say, from the location string alone, what it is and whose it is:

| field | what to write |
|---|---|
| `system` | which system made it: a product (`advi`, `irpt`, `mdpf`) or a vendor (`blackdiamond`, `schwab`, `orion`, `eclipse`, `smartx`); `unknown` if the string does not tell you |
| `firm` | whose it is, in the long form (`49financial`, `inflection`, `cottonwood`); `unknown` if the string does not tell you |
| `tier` | how finished it is: `bronze`, `silver`, `gold`, `platinum`, `state` or `code`; `unknown` if the string does not tell you |
| `table` | the table or served family it holds: ONE lowercase token, exactly as it appears in the string, or `unknown` |
| `contents` | one plain-English sentence, 15 words at most, of what the object holds |

**A guess is not an answer.** Where the string does not tell you, write `unknown` in that field; the grade counts an
`unknown` as no agreement and a wrong word as a worse one.

### 1a. How to read

- You have no reference document, by design: the standard key grammar the strings follow, where they follow one, is
  `{source}/{scope}/{tier}/{table}/{partition}` under a bucket; a bucket name is `opal-data-<firm slug>`. Some strings
  follow it and some are older and do not. Read each string yourself and decide its answers.
- **Do not write a program that parses the strings and fills the answers**: a parse measures the program, not the
  location. A short script may be used ONLY to write your finished answers into the output file.
- You work ALONE. Another reader answers the same list in another directory; never look for it.
- Open ONLY `LOCATIONS.json` in your directory. Open no other path on this machine.

### 1b. The output

`C:/dev/wk-firmbkts-reader-a/ANSWERS_A.json`:

```json
{"reader": "0.9.0_WK_ADVI_FIRMBKTS~13",
 "answers": [{"id": "<the location's id>", "system": "...", "firm": "...", "tier": "...", "table": "...", "contents": "..."}]}
```

Exactly one answer per id, all 418, every field a non-empty string. `indent=1`, `ensure_ascii=True`, LF endings. Do NOT
commit anything and do not create any other file in the directory: the issuer ingests `ANSWERS_A.json` from there.

## 2. BOUNDS

1. No AWS act. No write other than `ANSWERS_A.json` in your directory.
2. Nothing in this directory or outside it is read except `LOCATIONS.json`.

## 3. SURFACES

<paths>
org/tier1_exec/2.0.0_SA_COO~B1/round3/blind/
</paths>

(The path above is the issuer's ingest destination; you never touch it. Your only surface is the directory in section 1.)

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~13/ADVI_FIRMBKTS.TO-FB-f-3.reader-a.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-3"><invocation>timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_reader.py --reader A --dir C:/dev/wk-firmbkts-reader-a --root C:/dev/ajb_workspace; echo "exit=$?"</invocation><expect>ROUND 3 READER A: 3 of 3 arms</expect></criterion>
</proof_of_spec>

The grader reads your directory and one hash file; it opens nothing else of yours to read. Agreement between the two
readers is NOT graded here; it is the issuer's real run at the round's close.

## 5. WHEN YOU ARE DONE

Run AC1 once. Then report, and add two lines to the usual report: `OPENED:` every file you opened other than
`LOCATIONS.json` (write `none` if so), and `METHOD:` in one sentence how you produced the answers. Report the counts of
`unknown` per field and the output of AC1. You write no proof instance and flip no status: the issuer ingests your file,
re-runs AC1 and closes this order.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's ruling (round-2 analysis section 2/3 item 4): independence is a property of the reader's disk.
The directory outside any checkout, `LOCATIONS.json` alone, the grader's R3 arm listing it, and the `OPENED:` line are
the evidence; a worker agent can still read any path by absolute name, which is why the face forbids it and the report
states it. Nothing here is a commit, so the worker's lane gate has nothing to admit. The issuer writes the proof instance
from the grader's output on ingest and flips the status in its own commit. Same grading as round 2, denominators printed.

<status>complete</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-3</to_id>
<slot>~13</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
