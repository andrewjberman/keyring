# AMGT_HARVST -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~Y` at L6, 2026-09-22. **Home:** the project tree's channel. Lane `ANY`; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project).
**Append-only during the round.**

**Why this file is opened at the issuance.** Ten worker faces name it as the carrier for their rows, and a worker
cannot create a channel it was not granted. The first row is the issuer's own: a finding made while cutting.

**Id grammar on this fabric:**
- A seat's row is `AMGT_HARVST-Z-S<k>`.
- A worker's row is `AMGT_HARVST-Z-W<n>-S<k>`, where `<n>` is its slot.
- `<k>` restarts at 1 per coordinate.
- Every new row carries `"project": "AMGT_HARVST"` and `"fabric": "site-z"`.
- The CVO's rows live in `adjudications/`, never here.

**Denominator at this write: 1 row**, `-Z-S1`, by `2.0.0_SA_COO~Y`.

THIS FILE MUST STAY ONE FENCED JSON BLOCK. An appender targets the FIRST block only, and appends INSIDE the array. A
concurrent drain is resolved as a UNION BY ROW ID through `safe-merge.sh`, and no foreign row is ever edited here.

## Row context -- what was measured

The L4-to-L5 handoff (s.2) says `raw_bytes` "is set only on the SA and Bloomberg paths", and the PRD's
`C-HV-BRONZE-AS-RECEIVED` requires the bytes received. The code at SITEZ @9fbf337a74 says those two paths do not keep
received bytes either:
- `publishers.py:216` sets `item_bytes = json.dumps(item).encode("utf-8")` from the PARSED listing item.
- `publishers.py:241` sets `value_bytes = json.dumps(value).encode("utf-8")` from `r.json()`.
- The transport functions (`org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py:157` `news`, and
  `bloomberg_rest_fetch.py:89` `search` and `:101` `article`) return parsed JSON, never the response.

So all five publishers keep NO as-received bytes today. The one layer every publisher path passes through is
`lib/opal_data_harvest/transport.py:64-93` `PacedSession.get`, which holds each `response` object.

```json
[
  {
    "id": "AMGT_HARVST-Z-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Y",
    "surfaced_at": "2026-09-22T15:30Z",
    "one_line": "The SA and Bloomberg raw_bytes the handoff counts as kept are json.dumps re-serialisations of parsed JSON (the SA one a listing item, not an article response), so no publisher keeps as-received bytes today.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/opal_data_harvest/publishers.py:216 item_bytes = json.dumps(item).encode('utf-8') @9fbf337a74",
        "lib/opal_data_harvest/publishers.py:241 value_bytes = json.dumps(value).encode('utf-8') @9fbf337a74",
        "org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py:89-110 search() and article() return r.json() @9fbf337a74",
        "org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py:157-165 news() returns get_json(...) @9fbf337a74",
        "lib/opal_data_harvest/transport.py:64-93 PacedSession.get holds the response object on every publisher path @9fbf337a74"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Handoff s.2: raw_bytes is set only on the SA and Bloomberg paths (Barron's, WSJ and FT keep no bytes) -- read as: SA and Bloomberg already keep what C-HV-BRONZE-AS-RECEIVED asks for.",
    "world_is": "No publisher keeps the bytes received. SA and Bloomberg keep a re-serialisation of parsed JSON, which differs from the response body in key order, whitespace and escaping, so a byte-for-byte FWD-1 check against it can never pass; HVST-h-1 therefore captures response bytes at PacedSession.get for all five publishers.",
    "notes": "Not a defect in the PRD and not a hold: HVST-h-1's face is cut to capture at the session layer, so the fix is inside round 1. Recorded so the handoff's sentence is not reused as a measurement."
  },
  {
    "id": "AMGT_HARVST-Z-W8-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_HARVST~8",
    "surfaced_at": "2026-09-22T16:10Z",
    "one_line": "HVST-h-8's own AC1 invocation reads the deliverable with Python's default text-mode open(), so its printed crlf count is always 0 regardless of the file's actual bytes -- the clause cannot discriminate a CRLF-contaminated deliverable from a clean one.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Y",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-8.timeline-design-spec.md@df910bd910 AC1 invocation: t=open(...,encoding='utf-8').read() then t.count(chr(13))",
        "Python's text-mode open() with the default newline= setting performs universal-newline translation on read, converting every \\r\\n to \\n before the string reaches the caller, per the interpreter's own documented io.TextIOWrapper behaviour",
        "measured in .scratch (not committed): a mutant copy of this cell's own deliverable with one literal CRLF pair inserted has raw byte CR count 1 (open(path,'rb').read().count(b'\\\\r')) but AC1's own text-mode read of the same bytes (open(path,encoding='utf-8').read().count(chr(13))) prints 0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AC1's expect string 'sections 12345678 non_ascii 0 crlf 0' treats a printed crlf value as evidence the deliverable carries no CRLF line endings.",
    "world_is": "The crlf term in AC1's own invocation is not exercised against CRLF at all -- text-mode read strips \\r before the count runs, so the clause reads 0 whether the file is LF-only or CRLF throughout. This cell's actual deliverable is confirmed LF-only by a separate raw-byte check run this same session, so AC1 PASSED on true grounds here; the surprise is that the clause could not have caught the opposite case. Grounding is INFERRED-then-GROUNDED by direct measurement above, not merely read from the doctrine text.",
    "notes": "Class OBSERVATION (no interruption owed this turn) but hazard_standing ARMED: left alone, the SAME clause shape sits in every proof-of-spec criterion across this estate that pairs a text-mode Python read with a crlf/\\r count, and a future deliverable could carry real CRLF and still print a clean 0. Disarm is the issuer's/CVO's: either drop the crlf clause as vacuous or rewrite it to read the file in binary mode ('rb') before counting. Not raised as a hold on this cell's own AC1, which the real deliverable passes on its substantive terms (8 of 8 sections, 0 non-ASCII, confirmed LF-only by direct byte read)."
  },
  {
    "id": "AMGT_HARVST-Z-W8-S2",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_HARVST~8",
    "surfaced_at": "2026-09-22T16:25Z",
    "one_line": "The TO's own section-6 grading command (proof-of-spec-check.py <instance> AC1,AC2) returns rc=1 INVALID on a correctly-built instance, because the checker's coverage-frame requires the ids argument to equal the FULL set of rows carried in acceptance -- and section 5 separately requires AC3 (the judgment row) to be recorded there.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Y",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-8.timeline-design-spec.md@df910bd910 section 6 step 2, verbatim: 'Grade the mechanical criteria with python .tools/proof-of-spec-check.py <instance> AC1,AC2, which must return rc 0.'",
        ".tools/proof-of-spec-check.py:466-476 coverage_check(): carried = every criterion_id in inst['acceptance']; any id in carried but not in the ids argument is printed as 'coverage: instance row ... is NOT in the TO's expected set' and counted in violations",
        "measured this session: python .tools/proof-of-spec-check.py <this cell's instance> AC1,AC2 -> 'VIOLATION: coverage: instance row 'AC3' is NOT in the TO's expected set' plus two AC2 output_evidence violations, INVALID (rc=1); the same instance graded with AC1,AC2,AC3 -> 0 violations, VALID (rc=0)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Section 6 step 2's literal invocation (AC1,AC2 only) is sufficient to prove the mechanical criteria and reach rc 0 on a correctly-built instance.",
    "world_is": "It is not sufficient on its own: the checker's coverage-frame compares the ids argument against every row actually carried in the instance, not just the ones named in the argument, so an instance that correctly records AC3 (per section 5's own instruction: 'Record each criterion's ACTUAL OUTPUT ... Record AC3 as UNVERIFIABLE-BY-INSTRUMENT') fails coverage unless AC3 is ALSO included in the ids argument. This cell graded with AC1,AC2,AC3 to reach VALID; the literal AC1,AC2 command in the task order text returns INVALID on the identical, otherwise-correct instance.",
    "notes": "Class OBSERVATION, not BLOCKING: the discrepancy is between the task order's illustrative invocation text and the checker's actual coverage semantics, not a defect in this cell's own deliverable or judgment recording -- section 5 and the schema both require AC3 in the instance, and the checker's own design (coverage-frame closes the FULL carried set) is documented in its own source, not hidden. hazard_standing ARMED because the same 'grade with <mechanical ids only>' phrasing is a natural pattern for any future TO carrying a judgment criterion, and a worker who runs the literal command and stops at rc=1 could wrongly treat a valid instance as failing. Disarm is the issuer's: either the TO phrasing should say 'the full criterion id set, including judgment rows' or the checker's coverage_check should ignore ids whose row carries judgment=true."
  }
]
```
