# ADVI_FIRMBKTS task order -- `FB-f-6` -- THE PRODUCER CENSUS: WHO WRITES 49 FINANCIAL'S SERVED PLATINUM KEYS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~16</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the cell READS schedules and changes none.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act beyond reading the F7 manifest in the repository; no grant is created.
comp-adversary: RUN by the issuer -- r3_census.py 0 of 3 at base (census absent), 3 of 3 on a fixture (11 classes, 3 writers read from D_04, 42 importers recounted), 2 of 3 with one object count off by one. Blindness: the lens cannot see a writer that builds a key through a function the census does not name; the census states each class's writers by line and says so where a key is built by a function.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-f-6` (round 3, enrichment item 1, step 2's blast radius; PRD F10)

The cutover window's step 2 repoints the producers that write 49 Financial's served platinum keys so that they write
`address()` keys in `opal-data-49financial` instead of `opal-data-bd`. No act can be signed until its blast radius is
named. You measure it. You change nothing.

**The served set.** The 11 classes of the round-1 table with `bucket == "opal-data-bd"`, `disposition == "MOVE"` and
`dest.tier == "platinum"` (`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json`): `gold/artifacts/`,
`gold/entities/accounts/`, `gold/entities/advisors/`, `gold/entities/clients/`, `gold/platinum/firm/`, `gold/views/`,
`platinum/49financial/`, `platinum/accounts/`, `platinum/advisors/`, `platinum/clients/`, `platinum/firm/`. Their object
counts are the F7 manifest's (`deliverables/0.9.0_WK_ADVI_FIRMBKTS~8/F7_MANIFEST.tsv.gz`, 52,910 objects: a key belongs
to the longest class prefix that starts it).

### 1a. The steps

0. Work in `/c/dev/wk-firmbkts-16`. Begin every shell call with `cd /c/dev/wk-firmbkts-16 &&`.
1. For each class, find EVERY script in the repository that writes a key of that class to `opal-data-bd`. A key may be a
   literal or built by a function (`comp-pipescript io <script> --pipeline bd-gold --no-portal` prints each script's WRITES
   with `[HARDCODED]` and `[FUNC]` keys; D_04 alone writes `platinum/accounts/`, `platinum/advisors/`, `platinum/clients/`
   and `platinum/firm/`). Search with `comp-find` for the key text and for each `[FUNC]` builder's definition; search
   `data/black_diamond/`, `data/assets/` and `data/cot/` gold script directories, `lib/` and `infra/`. A class that no
   writer produces is an ORPHAN: say so with the evidence of what you searched (each search's text and its
   denominator), never as "none found".
2. For each writer record: the script path, the 1-based line of the write, the exact text of that line's key expression
   (a substring of the line, as it appears), how the bucket is chosen (`bucket_expr`), what runs the script (`runner`),
   and its trigger (`schedule`, or `null` if none is declared). Read the runner and schedule from the repository's own
   records (`org/missions/`, `docs/`, `infra/aws/terraform/`, `comp-schedule`); say `UNKNOWN` plus where you looked rather
   than guess.
3. The bucket seam. `data/black_diamond/scripts/gold/lib/config.py:14` reads `S3_BUCKET = os.environ.get('BD_S3_BUCKET',
   'opal-data-bd')`; the gold scripts import it as the one bucket for every read and every write. Record: the definition
   (`<path>:<line>`), the number of scripts under `data/black_diamond/scripts/gold` and `data/assets/scripts/gold` that
   contain `from lib.config import ... S3_BUCKET` (count them), whether a script can write one output to a different
   bucket than it reads from without editing the script (`separable_per_output`, with the evidence in a paragraph), and
   every other place the same environment variable `BD_S3_BUCKET` is set (the runner's environment file, a launch
   template, a scheduler target) with its path or its resource name.
4. Write `deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json` in exactly the shape the grader's docstring gives
   (read `deliverables/2.0.0_SA_COO~B1/round3/checks/r3_census.py` lines 1-25), and `PRODUCER_CENSUS.md`, a human view:
   per class its object count, its writers (script:line) and its runner and schedule; the seam paragraph; and what could
   not be determined.
5. Run AC1 and AC2. Repair only what they name.

## 2. BOUNDS

1. Read-only. No write to any repository file other than the two deliverables and your proof instance; no AWS act.
2. A figure you did not measure is `UNKNOWN`, never an estimate. Your report names counts and script paths, never a key
   that carries a client id.
3. Do not edit a producer script, `lib/config.py`, any schedule or any registry row. This cell proposes no repoint: it
   states what a repoint would touch.
4. No non-ASCII; LF line endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, the F7 manifest, `mapping.json`, the grader.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/ADVI_FIRMBKTS.TO-FB-f-6.producer-census.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-6"><invocation>cd /c/dev/wk-firmbkts-16 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_census.py --census org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json --root /c/dev/wk-firmbkts-16; echo "exit=$?"</invocation><expect>ROUND 3 PRODUCER CENSUS: 3 of 3 arms</expect></criterion>
</proof_of_spec>

The grader re-reads every writer's line and recounts the seam's importers: nothing in the census is taken on trust.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-6.producer-census.proof_of_spec.json`, `D` =
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16`. **Flip this order's `<status>` to `complete` in
the SAME commit as your proof instance and the two deliverables**, only when AC1 passes. A row id on this project carries
the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W16-S<k>`, `surfaced_at` from `date -u +%FT%TZ`. Report once: per class
its object count, writer count and orphan flag; the number of distinct writer scripts; the seam's definition, importer
count and `separable_per_output` with one sentence of why; every place `BD_S3_BUCKET` is set; the AC1 output in full;
the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** this cell is the window's step 2 measurement, not its act: `FB-f-9` is staged and is amended from the
census before its GO. The issuer's L5 reading is only that D_04 writes 22 key families and that one environment value
moves every read and write of the gold scripts (L5_FACTS section 4). A census that finds the seam inseparable makes
step 2 a producer migration, which is a CTO call (a round of its own), and the amendment says so.

<status>pending</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-6</to_id>
<slot>~16</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
