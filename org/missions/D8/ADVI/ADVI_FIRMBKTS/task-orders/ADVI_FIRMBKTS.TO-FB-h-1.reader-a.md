# ADVI_FIRMBKTS task order -- `FB-h-1` -- BLIND READER A, SECOND ROUND (22 LOCATIONS: THE 11 THAT DISAGREED AND 11 CONTROLS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R5.md</decomp_doc>
<owned_cells>FB-h-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~61</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change and no AWS act; the cell reads one JSON file in its own directory.
comp-adversary: RUN by the issuer -- r5_fwd1.py reader reads 0 of 4 at base (answers absent); 4 of 4 on a full fixture answers file; 3 of 4 with one extra file in the directory (arm R3 fails). Blindness: the lens cannot see which files a reader opened beyond the directory; the `OPENED:` line is the only witness.
EGRESS CLASS, declared: NONE.
</preflight>

## THIS ORDER IS THE ONE EXCEPTION TO YOUR STANDING TREE-PRESENCE BAR

Your directory is `C:/dev/wk-firmbkts-r5-reader-a`. It is a git worktree of a ONE-COMMIT history that holds `LOCATIONS.json` and nothing else. You
will find no `org/` and no `.tools/`, and that is correct. Do NOT run the `test -d org && test -d .tools` check, do NOT
stop on its absence, and never rebuild, fetch or extract a tree. Do not run any git command that reads another commit,
and do not follow the `.git` file's pointer to the repository it names. Do not write a surprise row (the channel file is
not in your directory); a surprise goes in your final report under BLOCKING or OBSERVED, in one line.

## 1. THE CELL -- `FB-h-1` (round 5, enrichment item 1; PRD F3)

You are one of two people reading the same list of storage locations, working alone. You have never seen these locations
before and you do not know where they came from. For EACH location in `C:/dev/wk-firmbkts-r5-reader-a/LOCATIONS.json`
(`{"locations": [{"id", "location"}]}`, 22 entries) you say, from the location string alone, what it is and whose it is:

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

- You have no reference document, by design: the standard key grammar the strings follow is
  `{source}/{scope}/{tier}/{table}/{partition}` under a bucket; a bucket name is `opal-data-<firm slug>`. Some
  strings are older and do not follow it. Read each string yourself and decide its answers.
- **The `table` field, stated exactly:** in a string that follows the grammar, the table is the ONE path component
  immediately after the tier component (`bronze`, `silver`, `gold`, `platinum`, `state` or `code`), whatever that
  component looks like: a family name, a source name or a firm name. It is never the file name and never a directory
  deeper than that component (everything after it is the partition). For an object under `code`, the table is the group
  directly under `code/`.
- **Do not write a program that parses the strings and fills the answers**: a parse measures the program, not the
  location. A short script may be used ONLY to write your finished answers into the output file.
- You work ALONE. Another reader answers the same list in another directory; never look for it.
- Open ONLY `LOCATIONS.json` in your directory. Open no other path on this machine.

### 1b. The output

`C:/dev/wk-firmbkts-r5-reader-a/ANSWERS_A.json`:

```json
{"reader": "0.9.0_WK_ADVI_FIRMBKTS~61",
 "answers": [{"id": "<the location's id>", "system": "...", "firm": "...", "tier": "...", "table": "...", "contents": "..."}]}
```

Exactly one answer per id, all 22, every field a non-empty string. `indent=1`, `ensure_ascii=True`, LF endings. Do NOT
commit anything and do not create any other file in the directory: the issuer ingests `ANSWERS_A.json` from there.

## 2. BOUNDS

1. No AWS act. No write other than `ANSWERS_A.json` in your directory.
2. Nothing in this directory or outside it is read except `LOCATIONS.json`.

## 3. SURFACES

<paths>
org/tier1_exec/2.0.0_SA_COO~B1/round5/blind/
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~61/ADVI_FIRMBKTS.TO-FB-h-1.reader-a.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-h-1"><invocation>timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/checks/r5_fwd1.py reader --reader A --dir C:/dev/wk-firmbkts-r5-reader-a --root C:/dev/ajb_workspace; echo "exit=$?"</invocation><expect>ROUND 5 READER A: 4 of 4 arms</expect></criterion>
</proof_of_spec>

The grader reads your directory, its git index and history, and one issuer file; it opens nothing else of yours to read.
Agreement between the readers is NOT graded here; it is the issuer's real run (`r5_fwd1.py agree`).

## 5. WHEN YOU ARE DONE

Run AC1 once. Then report, and add two lines to the usual report: `OPENED:` every file you opened other than
`LOCATIONS.json` (write `none` if so), and `METHOD:` in one sentence how you produced the answers. Report the counts of
`unknown` per field and the output of AC1. You write no proof instance and flip no status: the issuer ingests your file,
re-runs AC1 and closes this order.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the 22 are the 11 canonical locations whose four fields did not agree in round 4 (`FWD1_R4_DISAGREEMENTS.json`; ruled in `RULING_FWD1_R5.md`) and 11 locations both round-4 readers got right (one per class, seeded), so a regression of the face shows. The face is round 4's FB-g-4/-5 face plus ONE sentence: the table is the component after the tier (the fix; every one of the 11 follows from it). Independence is by construction as in round 4 (the CTO's round-3 ruling); the residual (subagents of the issuing session on one model) is unchanged and named in the packet. The issuer writes the proof instance from the grader's output on ingest and flips the status in its own commit.

<status>complete</status>
<round>5</round>
<workstream>FWD1REREAD</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-h-1</to_id>
<slot>~61</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
