# AMGT_CORPUS task order -- `CRPS-f-3` -- ROUND 4: a report stored under two file names (same content, one report_id) yields ONE extract and ONE typed row, from its lexicographically first bronze key; the other is a named skip, so the write-once extract is always a function of its key

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-f-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (G-3 CTO, G-7 POD4), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes nothing to S3 (the `--duplicates` probe is a read-only listing); the extract run is the issuer's drain act.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 4. Serves **FWD-19** (every inducted name's reports extracted, typed,
continued and composed).

## 1. THE CELL -- `CRPS-f-3`

**Where this came from.** `lib/research/corpus/extract.py`'s write run lists every bronze research-report object and writes
`<report_id>/extract.json` (write-once) for each. The report_id is the content hash, so two files with the SAME bytes under two
names share one report_id; the extract body carries `bronze_key` (the object's s3 uri, file name included), so the second write
differs and the store refuses it -- which aborts the whole extract step. The corpus holds exactly ONE such pair today:
`CPA_US_Equity/ff0e11955cb266f4` ("Copa Holdings - 2025 Investor Day Presentation (1).pdf" and "... Presentation.pdf"); the
stored extract came from the sorted-first key. Readers of an extract's `bronze_key` (`typed.py`, `report_input.py:73`, which
compares it with the typed row's key) mean the field STAYS, and typed must collapse the pair the same way.

**RULED -- what you build:**
- A helper (in `extract.py`) that groups listed bronze keys by (partition, report_id) and returns the CANONICAL key per group:
  the lexicographically first key. Every other key in a group is a duplicate.
- `extract --write` and `extract --run-v2` process only canonical keys; each duplicate prints ONE line
  `duplicate-content <report_id> <canonical file name> <skipped file name>` and is counted (`duplicates <n>` in the summary line).
- `typed --write` (and every typed path that lists bronze keys) emits ONE row per report_id, from the canonical key, and prints
  the same `duplicate-content` line for the skipped one.
- `python -m lib.research.corpus.extract --duplicates`: read-only listing, no write; prints
  `objects <n> report_ids <m> duplicates <d>` then one `duplicate-content ...` line per duplicate.
- `tests/test_duplicate_content.py` (fake client): a two-file report_id yields one extract put and one typed row from the
  first key; the duplicate line is printed; a corpus without duplicates is byte-identical to today's behaviour.

## 3. SURFACES

<paths>
lib/research/corpus/extract.py
lib/research/corpus/typed.py
lib/research/corpus/tests/test_duplicate_content.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-f-3.duplicate-content-one-extract.md
</paths>

READ-ONLY: every other `lib/research/corpus/` module, the research library. Scratch `.scratch/f3/`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. NO S3 write (never run `--write` or `--run-v2` for real; your tests fake the
  client), NO library write, NO change to an extract's or typed row's fields.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W3-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-f-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/f3_AC1.sh</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-f-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/f3_AC2.sh</invocation><expect>(?s)objects \d+ report_ids \d+ duplicates [1-9]\d*.*duplicate-content ff0e11955cb266f4 </expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-f-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/f3_AC3.sh</invocation><expect>(?m)^\d+ passed in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the read-only listing names the live duplicate; AC3 the bound: the whole corpus
  suite still passes.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-f-3.duplicate-content-one-extract.proof_of_spec.json`
   (the shape of your e-3 instance in that dir).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-3 analysis s.7 item 3 @`eaed38bac0`; row `Z-S30`. The drain re-runs the sequence after the derive;
the canonical rule matches the stored CPA extract (sorted-first), so it re-runs clean. Checks dry-run at the base: AC1 FAIL (no
such test file), AC2 FAIL (no `--duplicates` flag), AC3 bound -- recorded in the issuance commit.

<risk>LOCAL</risk>
<status>pending</status>
<round>4</round>
<slot>~3</slot>
<fabric>site-z</fabric>
