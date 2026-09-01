# THE CANONICAL DIRECTIVE LOOP, steps 1-10 -- drawn AS BUILT on 2026-09-01

Andrew-direct: *"analyze existing processes and /draw what we have step 1 - 10 including any decision
forks, scripts, tools, and cycling."* Source: transcript `9-1 flow_6519.txt`, re-read in full.

**LEGEND -- the only thing in this document that matters:**
```
  [GATE]    mechanically refuses today. A commit / an act is BLOCKED if this is not satisfied.
  [~]       exists as protocol, schema or doc. NOTHING REFUSES. Binds by reading only.
  [ABSENT]  does not exist in any carrier. Measured, not assumed.
```

---

## PLANE 1 -- THE BUILD PLANE: a topic Andrew raises becomes dispatched task orders

```
   STEP 1              STEP 2                 STEP 3               STEP 5              STEP 6
   ANALYSE             SPECIFY                REGISTER             DECOMPOSE           DISPATCH
   -------             -------                --------             ---------           --------

 +-----------+       +-------------+       +--------------+      +------------+      +-----------+
 | 4.0.0_    | brief | 1.0.0_SA_   | PRD   | DIRECTIVES   | hand | 2.0.0_SA_  | TO   | WORKERS   |
 | SA_CRO    |------>| CTO         |------>| .yaml        |----->| COO        |----->| (sonnet)  |
 |           | doc   |             | +tag  |      +       | off  |            | .md  |           |
 | analyse   | [~]   | writes PRD  | [~]   | org/projects/| STEP | /atom-     |[GATE]| EXECUTE   |
 | surfaces  |       |             |       | <code>.json  |  4   | decomp     |      | ONLY      |
 +-----------+       +------+------+       +------+-------+      +-----+------+      +-----+-----+
                            |                     |                    |                   |
                     STEP 2 FORK           STEP 3 FORK           STEP 5 BATTERY            |
                     /endpoint             laptop vs site Z      7 admitted lenses         |
                     [~] EXISTS but        [ABSENT] 0 of 349     [~]                       |
                     reads TOs in          project jsons carry                             |
                     FLIGHT; Andrew        ANY fabric key                                  |
                     needs the FORWARD                                                     |
                     derivation he named                                                   v
                                                                                     STEP 7 ->
```

### The three gates that actually refuse, and where they sit

```
  .tools/to-pipeline-gate.py          wired in .tools/safe-commit.sh AND .git/hooks/pre-commit
    on a NEWLY-ADDED org/**/task_orders/*.md it requires:
      1. org/projects/<code>.json EXISTS               -> else REFUSE
      2. a dep_stage in the ratified enum              -> else REFUSE
         REGISTERED|PRD|DECOMP|TOS_CUT|EXECUTING|ROUND_CLOSE|CLOSED
      3. a <preflight> block naming comp-schedule / comp-iam / comp-adversary,
         each RUN or DECLARED-NOT-APPLICABLE **with a reason on its own line**
    override: `# pipeline-override: <reason>`  (audited)

  .tools/git-hooks/to-proof-of-spec-check.sh:60-71    (the SIBLING, Andrew-direct 2026-08-11)
    a NEW TO on a pipeline-registered project must carry <decomp_ref>. Reads STAGED bytes.

  .tools/proof-of-spec-check.py                       (layer 1)
    a terminal <status> flip needs a VALID proof instance. Fail-closed.
```

⛔ **THE KEYSTONE, MEASURED:** layers 1 and the sibling gate were BUILT and INERT, because both fire
only on a *pipeline-registered* project and the predicate for that is `dep_stage` present --
**316 of 349 projects have none.** Nothing ever required it. That requirement is what shipped today.

### STEP 5 -- the lens battery, admissibility MEASURED 2026-09-01

```
  ADMITTED (7)                                     runtime? vintage printed?
  comp-blast      blast radius (kuzu, 27,107 nodes)   overlay   YES (built + Nessie snapshot ids)
  comp-dataflow   value-origin trace                  YES       YES (explicit VINTAGE: line)
  comp-schedule   the gate ledger                     YES       n/a "VIEW-TIME COMPILED, no artifact"
  comp-iam        permissions, DESIRED plane          YES       plane + 395-file denominator
  comp-trigger    EventBridge/Scheduler forensics     YES       denominator + region
  comp-pipescript pipeline script deps                YES       refuses without --pipeline
  comp-denytest   live IAM evaluation (EXERCISED)     YES       n/a (holds no corpus)

  REFUSED (1)
  comp-similar    BM25 functional similarity          NO        NO -- neither text nor --json
                  (--json top-level keys are exactly ['arn','neighbors'])
```

---

## PLANE 2 -- THE SURPRISE PLANE: a spec-vs-world mismatch becomes a remediation, and cycles

```
   STEP 7                 STEP 8                    STEP 9                  STEP 10
   IDENTIFY               COMPILE                   ADJUDICATE              ROUTE
   --------               -------                   ----------              -----

 +------------+  append  +------------------+  ping  +------------+  route +-------------+
 | WORKER     |--------->| org/surprise_    |------->| 3.0.0_SA_  |------->| REMEDIATION |
 | hits a     | direct   | channel/{PROJ}/  |[ABSENT]| CVO        |        | v(n)        |
 | mismatch   | write    | INVESTIGATION_   | no     |            |        |             |
 |            | [~]      | v1.md            | monitor| legitimise |        | CUT AT      |
 +-----+------+          |                  |        | /invalidate|        | ROUND CLOSE |
       |                 | rows are JSON vs |        | [~]        |        | ONLY [~]    |
  STEP 7 TRIGGER         | investigation_   |        +-----+------+        +------+------+
  "Did I have to do      | item.schema.json |              |                      |
   something the TO      | 17 rows on       |     disposition enum              STEP 10 FORK
   did not say, or       | ADVI_PERFRP      |     UNDER_INVESTIGATION           see below
   could I not do        | 18 project dirs  |     GRADUATED
   something it said?"   +------------------+     DISMISSED_WITH_REASON
  [~] VALIDATED against                           DECOMP_INVALIDATING
      all 17 filed rows,                          reader: comp-surprise
      ZERO exceptions                                    --armed --project --all --json
```

### STEP 10 -- the routing fork, and it IS the loop

```
              "What does the remedy need that does not exist yet?"
                                    |
        +---------------------------+----------------------------+
        |                           |                            |
  a cell the decomp          a CELL the decomp            an OUTCOME the PRD
  ALREADY CONTAINS           does NOT contain             does not name
        |                           |                            |
   SPEC ERROR              DECOMP-INVALIDATING              SCOPE CHANGE
        |                           |                            |
     -> COO                      -> COO                       -> CTO
   loop to STEP 6             loop to STEP 5              loop to STEP 2
   (amend/cut TOs)          (re-decompose; THIS           (new PRD; requires
                             round's completion            the ENDPOINT to be
                             claim is over-scoped)         decidable at all)
        |                           |                            |
        +---------------------------+----------------------------+
                                    |
                            round increments v(n+1)
```

⛔ **LIMB 3 IS UNDECIDABLE WITHOUT THE STEP-2 ENDPOINT.** Without a named desired outcome there is no
way to ask whether the PRD names it. **That is the load-bearing argument for Andrew's step-2 addition,
and it is not the argument the transcript makes.**

### The two driver loops

```
  1.0.0_SA_CTO   /self-drive   scoped to OPEN CALLS ONLY. One pass with CVO, CVO adjudicates. [~]
  2.0.0_SA_COO   /drive        the primary driver. 20 min default, a KNOB not a gate.         [~]
```

---

## THE ANALOGY THAT MAKES THE WHOLE DESIGN COHERENT

The "worker judges FORM, never SIGNIFICANCE" model is exact and deliberate:

```
  +--------------------------+--------------------------------------------------+
  |  THE WORKER (step 7)     |  THE CVO (step 9)                                |
  +--------------------------+--------------------------------------------------+
  | asks: is there a         | asks: does this MATTER, and what does the        |
  |   SPEC-vs-WORLD mismatch | remedy NEED that does not exist yet              |
  | answer: binary, needs    | answer: judgment, needs the whole round          |
  |   no taxonomy, no        |                                                  |
  |   context beyond its TO  |                                                  |
  | cost of a false positive:| cost of a false positive: a re-decomp            |
  |   one JSON row           |                                                  |
  | THIS IS WHY IT IS GATED  | THIS IS WHY IT IS SUGGESTED                      |
  +--------------------------+--------------------------------------------------+
```

**Gate the half a machine can settle; leave judgment to the seat that eats the error.** That single
split is why step 7's trigger can be mechanical while step 9's verdict cannot, and it is what stops
a worker becoming a fifth debugger -- Andrew: *"We are not fucking debugging."*

---

## WHAT THE DIAGRAM SAYS THAT PROSE DID NOT

**The loop is gated at exactly ONE hop of ten.** Step 6 refuses. Steps 1-5 and 7-10 bind by reading.
The build plane's left half is protocol; the surprise plane is entirely protocol. **A loop with one
gate is not a deterministic loop -- it is a well-documented convention with a checkpoint in it.**

**Three carriers are ABSENT, not weak** -- measured, not assumed: the step-3 fabric declaration
(0 of 349 project jsons), the step-8 investigations monitor, and the forward form of `/endpoint`.
The first two are the cheapest gates left on the board; the third is what makes step 10's third limb
decidable at all.
