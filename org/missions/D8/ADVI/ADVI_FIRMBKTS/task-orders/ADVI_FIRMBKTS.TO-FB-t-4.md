# ADVI_FIRMBKTS task order -- `FB-t-4` -- READER B

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP.md</decomp_doc>
<owned_cells>FB-t-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~3</issued_to>
<issued_by>2.0.0_SA_COO~F1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; nothing scheduled is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM and no AWS act.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~F1) on dell1 -- r1_reading.py --reader B 0 of 2 at base (files absent); 2 of 2 on reference answers over a reference list of 322 locations. Blindness: no instrument sees which files a reader opened; the bound in section 2 carries it.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-t-4` (round 1, THE THREAD for FWD-1; decomposition v1)

FWD-1 reads: *anyone who looks at where a piece of data is kept can tell what it is and whose it is, without opening
it.* Its test is two readers who have never worked together, reading the same list of storage locations. You are one of
them. Another worker reads the same list alone; you will never see its answers and it will never see yours.

Read `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/reading_list.json`. It is `{"locations": [{"id", "location"}]}`,
each `location` an `s3://bucket/key` string. For EVERY entry, answer from the location string alone:

| field | what to write |
|---|---|
| `system` | the system that produced it: a product (for example `advi`, `irpt`, `mdpf`) or a data vendor; `unknown` if the string does not tell you |
| `firm` | the firm whose data it is, as you would name it; `unknown` if the string does not tell you |
| `tier` | how finished it is: `bronze` (raw), `silver` (cleaned), `gold` (analytical), `platinum` (served to a page), `state` (operational bookkeeping), `code`; or `unknown` |
| `contents` | what it holds, in 12 words or fewer |

`unknown` is a real answer: write it whenever the string does not tell you, and never guess a firm from outside the
string. You may write a small script that parses the strings, as long as it reads only `reading_list.json`.

Write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/READING_B.json`:
```json
{"reader": "0.9.0_WK_ADVI_FIRMBKTS~3",
 "answers": [{"id": "...", "system": "...", "firm": "...", "tier": "...", "contents": "..."}]}
```

## 2. BOUNDS

1. **Read nothing but `reading_list.json`.** Do NOT open `mapping.json`, `MAPPING_TABLE.md`, `census.json`, `CENSUS.md`,
   `READING_A.json`, anything else under `org/missions/D8/ADVI/ADVI_FIRMBKTS/`, the naming schema, `lib/opal_naming.py`,
   `infra/logic/registry/`, the brief or the PRD; do not `git log` or `git show` them; do not list or read S3. The
   exercise measures what the location string tells a reader, and every one of those files would tell you more.
2. No AWS act of any kind. No non-ASCII; LF; JSON with `indent=1` and `ensure_ascii=True`.
3. Only the files in section 3 change.
4. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/READING_B.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~3/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/reading_list.json`, and the issuer's check
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/checks/r1_reading.py` (run it, never edit it).

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
  <criterion id="AC1" cell_refs="FB-t-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/checks/r1_reading.py" --reader B; echo "exit=$?"</invocation><expect>ROUND 1 READER B: 2 of 2 arms -- and exit=0</expect></criterion>
</proof_of_spec>

Whether your answers agree with the other reader's is not graded here, and you cannot see it. It is the issuer's run at
the round's close.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~3/ADVI_FIRMBKTS.TO-FB-t-4.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 passes. A row id
on this project carries the dell1 infix: `ADVI_FIRMBKTS-D1-W3-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at
filing. Report once: the file, how many answers carry `unknown` in each field, the output line of AC1, the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1 = THE THREAD (FWD-1) over PRD v1.3 @30d612d5e5. Spawned in its own slot (~3) together with
FB-t-3 (~2) when FB-t-2 is merged, so neither reader shares the placer's context. The agreement is r1_agree.py at close.

# pipeline-override: the one refusal is LIMB PRD_HEADER.fabric='laptop' vs the register's 'dell1'. The register row is the authority since 1.0.0_SA_CTO's L3 re-placement @8afcb0f851; the PRD header repair is the CTO's (msg 3113: a PRD commit is refused until it gains a KEY SURFACES section). Every other limb passed in the issuer's dry run.
<status>complete</status>
<round>1</round>
<to_id>ADVI_FIRMBKTS.TO-FB-t-4</to_id>
<slot>~3</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
