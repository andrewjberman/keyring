# TO LGIC_LGCTFM.TO-LT-e-5-r3 -- DISCOVERY BY DESIGN: the walk rows the subject's compute, schedules, machines, roles and tables, and says what it cannot see

<to_id>LGIC_LGCTFM.TO-LT-e-5-r3</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- 0.9.0_WK_LGIC_LGCTFM~1. AC4 read FAIL at the cell's pin b736ee4fdf because THE ISSUER'S ARM WAS THE DEFECT (e5-schema was unsatisfiable at the path this order itself mandated -- LGIC_LGCTFM-W1-S23/S29); the repair landed @fd02b24c51, 42 MINUTES AFTER that pin, and the arm reads PASS at HEAD. BOTH READINGS ARE TRUE OF THEIR OWN MOMENTS (S32, 3.0.0_SA_CVO's remedy adopted by the L10 analysis): the proof is NOT rewritten and still records the FAIL at its vintage.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-e-5` (decomposition v1.4 s.13) | **outcome_ref:** FWD-1 | **depends_on:** none -- first on slot `~1`, ahead of `LT-p-2` and `LT-x-4`

---

## WORKER FACE

### THE CELL

`LT-e-5`. **FWD-1's REALIZED grade was RETRACTED** (ruling R-79 @`0e9027c6dc`). Its ratified ACCEPT says the
person opening the 49 Financial migration *"never has to go and list the SCHEDULES, MACHINES, ROLES and
BUCKETS by hand to fill a gap the contract left blank WITHOUT SAYING SO"*. Andrew, ~18:2xZ: *"If we are
missing lambdas/ec2/eventbridge rules or schedules/ddb/etc, any involved aws resources, then the workflow
process is not done"* and *"the workflow must be designed to create rows for these items"*.

**Measured at the cut** against the graded run `workflows/legacy_transform/blackdiamond-49financial/20260918T011619Z-8db9eb1/`,
with comp-find over the live aws corpus for the subject's token (88 hits of 2590 nodes):

```
  node_type        live floor   rows in the graded run
  LAMBDA                9              0
  EC2_INSTANCE          1              0
  DYNAMODB_TABLE        1              0
  SCHEDULE              4              1
  IAM_ROLE             13              1   (a PLANT)
```

**WHY: THE WALK IS BUCKET-SEEDED.** `lib/opal_lgctfm.py` `run_aws_walk(seeds)` builds its comp-find
pattern from bucket names only, and `trigger_relevant()` keeps a trigger only if its pattern names a bucket
or its own name carries a firm shortcode. A Lambda whose only link to the subject is its name token, its
trigger, its IAM grant or its source text is never a row.

### WHAT YOU BUILD

1. **Seed by the subject's TOKEN beside its buckets.** The subject is registry key `49financial`; its tokens
   are `49f` and `49financial` (`infra/logic/registry/scopes.json`, scope `49financial`); its buckets
   `opal-data-bd` and `opal-data-49financial`.
2. **DEFINE "INVOLVED" -- THAT IS YOUR DESIGN DECISION, NOT THE ISSUER'S.** Candidates are four legs:
   `token` (the name carries a token), `trigger_target` (a rule or schedule targets it -- comp-trigger
   `--list --json` carries targets), `iam_grant` (a role's statements reach the subject's surfaces --
   comp-iam), `source_text` (its source dir, from `infra/aws/lambda/ci/lambda-source-map.json`, names the
   subject). Use the readers the estate already runs (Rule 20: `org/modules/graph/graph-call-manifest.yaml`);
   never write a new AWS caller. Write the definition into `infra/logic/10_LEGACY_TRANSFORM.md` and into
   the contract's `coverage.instrument`, and **name at least one node the definition EXCLUDES and why**:
   a scope with no stated exclusion cannot be shown wrong.
   **Andrew-direct ~18:3xZ (msg 98038, record @`c9e54d5c0f`):** *"We want to work in all the comp-tools to
   this process so we adequately enumerate the true resources involved in a given production pipeline."* So
   the method note also carries a **COMP-TOOL LEDGER**: every comp-tool the estate lists (enumerate them --
   `comp-which` and `org/modules/graph/graph-call-manifest.yaml` -- and PRINT the denominator), each marked
   USED (as which leg) or NOT USED with a one-line reason. A tool left off the ledger is a gap that does not
   say so. 1.0.0_SA_CTO is validating the comp-tools themselves in parallel -- a tool that returns wrong
   answers is a surprise ROW, not a reason to drop it silently.
3. **ROW EVERY INVOLVED NODE.** Andrew's remedy is ROWS, not a caveat. For the NAMED classes -- LAMBDA,
   EC2_INSTANCE, EVENT_RULE, SCHEDULE, DYNAMODB_TABLE, IAM_ROLE, S3_BUCKET -- every token-floor node must be
   a ROW, with no exclusion and no not_covered entry.
4. **WRITE THE COVERAGE BLOCK** as a top-level key of `contract.json`, in exactly this shape, and admit it in
   `org/standards/LGCTFM_CONTRACT.schema.json` (top level is `additionalProperties: false` today).

**COVERAGE BLOCK SHAPE (the one carrier is R3_BASE.json; this is a quotation of it)**

```json
{
  "coverage": {
    "instrument": "<the cell's 'involved' definition, in words>",
    "legs": ["token", "trigger_target", "iam_grant", "source_text"],
    "vintage": "<the graph's own 'Built from the estate as of ...' line>",
    "token_floor": {"pattern": "<regex>", "hits": 0, "scanned": 0},
    "by_node_type": {
      "LAMBDA": {
        "involved": 0,
        "rows": 0,
        "excluded": [{"name": "<a floor node judged NOT involved>", "reason": "<why>"}],
        "not_covered": [{"name": "<an involved node with no row>", "reason": "<why the instrument cannot row it>"}]
      }
    }
  }
}
```

Rules on it, verbatim from `R3_BASE.json`: `legs` is a non-empty subset of the four; per node_type
`involved == rows + len(not_covered)`; `rows` equals the count of contract rows of that type whose node is
involved; `excluded` holds FLOOR nodes judged NOT involved, each with a reason; for a NAMED class both
`excluded` and `not_covered` are empty; every node_type in the floor appears in `by_node_type`.

5. **THE FROZEN RUN STILL VALIDATES.** `20260918T011619Z-8db9eb1/contract.json` is frozen history (R-43) and
   reads ACCEPT under `.tools/receiving-check.py` today. After your schema change it must STILL read ACCEPT,
   and your new contract must too. How you make both true (e.g. a schema_version bump with the block
   required only from it) is your design.

### WHERE YOUR OUTPUT GOES

Run the WALK (not `run` -- that is `LT-x-4`'s) with your new discovery into
`<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/e5_walk/`, so that
`<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/e5_walk/contract.json` exists
and carries the coverage block. **Commit it.**

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E5R3-AC1" cell_refs="LT-e-5"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py e5-coverage-shape</invocation><expect>PASS-E5-COVERAGE-SHAPE</expect></criterion>

<criterion id="E5R3-AC2" cell_refs="LT-e-5"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py e5-floor</invocation><expect>PASS-E5-FLOOR</expect></criterion>

<criterion id="E5R3-AC3" cell_refs="LT-e-5"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py e5-named-rowed</invocation><expect>PASS-E5-NAMED-ROWED</expect></criterion>

<criterion id="E5R3-AC4" cell_refs="LT-e-5"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py e5-schema</invocation><expect>PASS-E5-SCHEMA</expect></criterion>

<criterion id="E5R3-AC5" cell_refs="LT-e-5" judgment="true"/>

<expected_criteria>E5R3-AC1, E5R3-AC2, E5R3-AC3, E5R3-AC4, E5R3-AC5</expected_criteria>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, measured by the issuer. `e5-floor` and `e5-named-rowed`
RE-MEASURE the token floor with comp-find at grade time and print the cut's figure beside their own.

**`E5R3-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether "involved" is a real definition --
every leg you claim is actually exercised by the walk, the exclusion you name is a real node rather than a
strawman, and a Lambda reached only through its trigger target or IAM grant (no token) would be rowed if
your legs say it is.

**THE CHECKER'S CONTROLS:** run `python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py selftest-arms`
FIRST -- 24+ arms incl. POSITIVE-SATISFIABILITY built from R3_BASE's shape and a REAL negative on the graded
run; expect `PASS-ARMS-DISCRIMINATE`. An arm a CORRECT record cannot satisfy is a BLOCKING surprise row
quoting the arm and its output -- never a workaround, never an edit to a fixed input.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **NOTHING LIVE MOVES (FWD-10).** Every AWS read is read-only, through comp-find / comp-trigger / comp-iam or the `.tools/aws` shim. No new AWS caller.
- ⛔ **YOU DO NOT RUN `run` INTO THE RUN HOME** and you do not touch `workflows/legacy_transform/` or `infra/logic/registry/` -- the real run is `LT-x-4`'s.
- ⛔ **YOU DO NOT EDIT `lib/lgctfm_render.py`** (`LT-r-2`'s this round) or rename the plan's `dependencies` field (`LT-p-2`'s, next on your slot).
- **Edges** (a resource dependency relation) are NOT required this round; per-class extras your discovery already reads (a trigger's target, a Lambda's role) MAY be written.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump the array; assert the non-ASCII CHARACTER count and the backslash-u count unchanged. `len(b)-len(b.decode())` is a BYTE DELTA, not a count; to count, `sum(1 for ch in text if ord(ch) > 127)`.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **One other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
lib/opal_lgctfm.py
org/standards/LGCTFM_CONTRACT.schema.json
infra/logic/10_LEGACY_TRANSFORM.md
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.4, round-3 cell `LT-e-5` (section 13).
<owned_cells>LT-e-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `E5R3-AC1` through `E5R3-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-5-r3.discovery-by-design.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E5R3-AC1,E5R3-AC2,E5R3-AC3,E5R3-AC4,E5R3-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-e-5-r3.discovery-by-design.md` BEFORE the `complete` flip.
Result file `discovery-by-design.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`; fold positive-control evidence into `mutant`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`E5R3-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT your "involved" definition and its legs, the per-node_type table (floor / rowed / excluded / not_covered) with the floor's denominator, the node you EXCLUDE and why, and how the frozen run still validates.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut: no schedule is created or read by this cell beyond comp-trigger's read-only census.
comp-iam: RUN at the round-3 cut: no grant moves. comp-iam may be READ as an involvement leg; nothing is written to IAM.
comp-adversary: RUN at the round-3 cut: the adversarial control is e5-named-rowed. The cheapest satisfying move is a coverage block that reports the gap honestly -- NOT_COVERED on the 9 Lambdas -- which is exactly the caveat-beside-a-run Andrew's second sentence refuses; the arm admits no not_covered and no exclusion for a named class. The floor is re-measured at grade time on comp-find, an instrument different from the walk, so the cell cannot grade itself on its own discovery.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ is granted by the tree convention. lib/opal_lgctfm.py has ONE writer at a time (decomposition s.5 CONSTRAINT 1): LT-p-2 queues behind this cell on the same slot.
contention: the channel is shared with LT-r-2 on slot ~2 -- append-only, 14b's inversion applies, no slot isolates there. No other open order writes lib/opal_lgctfm.py or the schema.
</preflight>

Seating: slot `~1`, level 0, first of three on the slot. Round 3 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.4 s.13, from R-79 (a), (b), (c). Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/` (`check_lt_r3.py`, `R3_BASE.json` pinning `0e9027c6dc`). Rulings carried: R-79, R-43, R-47, LGIC_ENFORCE-S85.
