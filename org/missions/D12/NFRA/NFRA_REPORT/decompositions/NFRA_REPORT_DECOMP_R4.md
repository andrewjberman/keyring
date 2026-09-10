# NFRA_REPORT -- L5 decomposition, ROUND 4 -- v0.1

**Seat:** `2.0.0_SA_COO~ZZ` · **Limb:** L5 (re-decomposition) · **Round:** 4
**Input:** `1.0.0_SA_CTO~Z`'s **L4 ADDENDUM 01** @`20c986bc70`
(`org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD_ADDENDUM_01.md`), issued for decomposition on
Andrew-direct. **NOT from a slug** -- round 3's slug was answered and its recut was correctly EMPTY.
**PRD:** `NFRA_REPORT_PRD.md` v0.7 **+ ADDENDUM 01** · adds `FWD-13`, `FWD-14`, `FWD-15` to the 12
**archetype:** COORDINATE

**THIS IS A RE-DECOMPOSITION, NOT A RE-ISSUE, AND THE CHOICE IS THIS SEAT'S TO RECORD.** The addendum
adds three outcomes that no existing cell serves; there is nothing to re-issue. Cell ids continue the
`RP-s-<n>` sequence from **21**, so no id is ever reused.

⚠ **THE ADDENDUM'S §5 WAS AMENDED WHILE THIS CUT WAS BEING WRITTEN, AND §0c RECORDS IT.** Its claim
that `FWD-1`..`FWD-12` are untouched is now correct for three of them and wrong for eight. The
CELLS DO NOT MOVE -- `1.0.0_SA_CTO~Z` at msg 20954, verbatim: *"DECOMPOSE ADDENDUM 01 EXACTLY AS
ISSUED. DO NOT WAIT ON THIS AND DO NOT RE-READ THE CUT... the difference is entirely in what the
round may CLAIM afterwards, not in what it must BUILD."* What moves is this document's postulate
record, corrected here rather than left to be caught at L9.

---

## 0. THE MEASUREMENT AT THE CUT THAT SIZES THE ROUND

The addendum names five collectors on the live side. **The live side has more than five, and
`C-NO-REGRESSION` is scored against the real denominator, not the named one.**

```
infra/aws/lambda/infrastructure_monitor/lambda_function.py :185-293, read at HEAD,
report["sections"] assembled by lambda_handler, in order:

   1 lambda_health        5 producer_drift      9 aws_costs        13 openai_cost
   2 smartx_pipeline      6 sns_egress         10 cost_depth
   3 data_freshness       7 graph_head         11 security_sweep
   4 deploy_drift         8 contract_integrity 12 ai_analysis (conditional -- None when
                                                   lambda_health.functions_with_errors == 0)

  DENOMINATOR: 13 sections, not 5.
```

⛔ **SO THE NO-REGRESSION BAR IS 13 AND ONE OF THE 13 IS CONDITIONALLY ABSENT BY DESIGN.**
`ai_analysis` is `None` on a clean day. A comparison that treats "absent" as "regressed" would fail on
every good morning; one that treats it as "fine" would miss a real removal. **The cell must partition
the 13 into MAPPED / OMITTED-WITH-REASON / CONDITIONAL-BY-DESIGN and print the denominator.**

### 0a. THE SEAM, MEASURED RATHER THAN DESCRIBED

```
LIVE   lambda_handler:267   email_body = format_report(report)      <-- the ONE line that changes
       lambda_handler:270   send_email(email_body, report)          <-- unchanged
       format_report        :2023-2462, 439 lines                   <-- what is being replaced
       _load_prior_report   :775-792   archive_report :2567-2581    <-- the delta substrate, EXISTS

SPEC   compose_edition.py, 575 lines
       ROW_FACTS            module region :1-333, a hard-coded list <-- what must NOT travel
       compute_delta        :334-371      compute_delta_watch :374-385
       compute_verdict      :388-396      fmt_state :399-408   gen_sentence :411-417
       render_markdown      :420-545      main :548-571        <-- main is specimen-only
```

### 0b. THE DEPLOYED STARTING STATE, READ LIVE AT THE CUT

```
aws lambda get-function-configuration --function-name opal-infrastructure-monitor
  Runtime      python3.12
  Handler      lambda_function.lambda_handler
  CodeSha256   r/bjjp5dJMcxw4NnzSNFsUCpYlWrH+sJsVJu+JiWxs8=
  LastModified 2026-07-08T01:29:08.000+0000      <-- two months older than this project
  CodeSize     40,015 bytes                      <-- the ZIP is the function ALONE
```

⭐ **THE 40 KB IS LOAD-BEARING AND IT IS A HAZARD FOR THE DEPLOY CELL.** The repo folder
`infra/aws/lambda/infrastructure_monitor/` also contains vendored packages (`anyio/`, `httpx/`,
`certifi/`, `pydantic`, ...). The DEPLOYED artifact is 40 KB, and `infra-monitor.tf:53` shows why:
`layers = [anthropic_sdk_deps]`. **The dependencies come from the LAYER.** A naive `zip -r .` of that
directory would ship a package that shadows the layer and bears no resemblance to what runs today.
This is written into `RP-s-23`'s BOUNDS rather than left to be rediscovered.

⛔ **AND IT IS THE RED ARM FOR `FWD-14`.** `CodeSha256` and `LastModified` above are the pre-state.
After the deploy they MUST both differ, and a criterion that cannot distinguish them is not a
criterion. Recorded here so a later reader can tell a real deploy from a no-op.

### 0c. THE GRADE STATE THIS ROUND ACTUALLY STARTS FROM -- CORRECTED MID-CUT

`3.0.0_SA_CVO~Z` filed row `Z-S19` and `1.0.0_SA_CTO~Z` UPHELD it in full @`b75e35f36e`, re-grading
**eight** outcomes and editing both the round-2 analysis and the addendum in place so neither reads
without its correction.

```
  EXERCISED bar   9 outcomes   FWD-1 3 4 5 6 7 8 11 12
  APPLIED bar     3 outcomes   FWD-2 9 10
  previously reported          11 of 12 REALIZED
  RE-GRADED to APPLIED         FWD-1 3 5 6 7 8 11 12   (eight, all on an EXERCISED bar)
  KEEP REALIZED                FWD-2 9 10              (their bar IS APPLIED; a specimen satisfies it)
  REAL STATE AT THIS CUT       3 REALIZED, 9 APPLIED of 12
```

⭐ **THE REASON, AND IT IS THE SAME CLASS THIS PROJECT KEEPS MEETING:** an artifact with a hard-coded
fact list produces an identical verdict every morning **by construction**, so `FWD-1`'s clause
*"including at least one morning where the verdict was 'NOTHING'"* -- which requires the verdict to
DIFFER across mornings -- was unsatisfiable even if a person ran the specimen by hand. Eight bars
carried the word EXERCISED, one artifact could satisfy none of them, and every grade still read
REALIZED. **A bar that says EXERCISED does not enforce itself.**

⛔ **THIS DOES NOT CHANGE ONE CELL, ONE CRITERION OR ONE CONSTRAINT**, and it is recorded because it
changes what the round may CLAIM. The deployment `RP-s-23` performs is the same act that makes all
eight re-graded outcomes exercisable for the first time -- which is why the round is worth more than
its three declared outcomes, not less.

---

## 1. The rectangle -- FOUR cells, `RP-s-21` .. `RP-s-24`

**CELL STATUS VOCABULARY** (unchanged, rule 24 record at round 1): `NOT-EVALUATED | OPEN | IN-FLIGHT |
HELD | COMPLETE | CLOSED`. All four read `OPEN`; none reads `NOT-EVALUATED` (4 of 4 evaluated).

| cell | outcome | act | round | slot |
|---|---|---|---|---|
| `RP-s-21` | FWD-13, FWD-15 | **THE PORT.** Lift `compute_delta` / `compute_delta_watch` / `compute_verdict` / `fmt_state` / `gen_sentence` / `render_markdown` out of the specimen into a Lambda-side module, **carrying zero `ROW_FACTS` and zero live reads**, proven by reproducing the specimen's own edition byte-for-byte from the same input | A | ~1 |
| `RP-s-22` | FWD-14 | **THE MAPPER.** Build the collector-output -> row-shape mapping over all **13** `report["sections"]` keys, partitioned MAPPED / OMITTED-WITH-REASON / CONDITIONAL-BY-DESIGN with the denominator printed, **no transcribed fact anywhere** | A | ~2 |
| `RP-s-23` | FWD-13, FWD-14 | **THE WIRE AND THE DEPLOY.** Replace `format_report(report)` at `lambda_function.py:267`; package to the layer-shaped artifact; S3 -> `source_code_hash` -> `safe-apply`; `C-CHANGE-LEDGER` opened before the first deploy act and **closed in the same cell**. Criteria score the **DEPLOYED PACKAGE**, never the source | B | ~3 |
| `RP-s-24` | FWD-15, FWD-13 | **THE COMPARISON AND THE TRIGGER.** Save the last OLD email, run the manual invocation of the DEPLOYED function, compare section-by-section over the denominator of 13, and record every section as present or removed-with-a-reason | C | ~4 |

### 1a. WHY THE PORT AND THE MAPPER ARE PARALLEL AND NOT A CHAIN

The obvious reading is that the mapper must wait for the port, because the mapper feeds the renderer.
**It does not, and the reason is the specimen's own architecture.** The row SHAPE that
`render_markdown` accepts exists TODAY, in `compose_edition.py` at HEAD, and is frozen -- `RP-s-21`
is forbidden from changing it (that is the whole of its port-fidelity criterion). So `RP-s-22` writes
against a contract that already exists and cannot move under it.

⚠ **THIS IS THE ONE ASSUMPTION IN THE CUT THAT COULD BE WRONG, AND IT IS NAMED SO IT CAN FAIL LOUDLY.**
If `RP-s-21` finds it cannot port `render_markdown` without changing the row shape, that is a surprise
ROW and `RP-s-22`'s contract moved underneath it. Both cells are told this in their BOUNDS.

---

## 2. Dependency edges

```
  RP-s-21 <- (none)                    <-- READY ROOT
  RP-s-22 <- (none)                    <-- READY ROOT
  RP-s-23 <- RP-s-21, RP-s-22          <-- the join
  RP-s-24 <- RP-s-23

  weakly connected components:  M = 1   (all four join at RP-s-23)
  READY ROOTS at issuance:      R = 2
  max concurrent width:             2
```

**FAN-OUT: `2 of 2 ready roots, cap 8` (1 weakly-connected component; max concurrent width 2).**

⚠ **THE TWO NUMBERS ARE STATED SEPARATELY ON PURPOSE.** Round 3's decomposition wrote fan-out as
`N of M chains` where `M` was weakly-connected components, and there `M = N = 1` trivially. Here they
differ -- one component, two ready roots -- and quoting a single `M` would either understate the width
to 1 or silently redefine the term. **The cap is stated, never silent.**

**ROUNDS BY DEPTH: A=2, B=1, C=1.** Max width 2, inside the default cap of 8.

⛔ **`RP-s-23` AND `RP-s-24` ARE ISSUED IN THIS SAME ISSUANCE AND NOT SPAWNED YET.** Rule 27 requires
ONE issuance covering EVERY cell; obligation 2 cuts only what has no unmet dependency. Both orders
exist at this commit with `<status>blocked</status>`; their workers are seated when their dependency
lands, with no second issuance.

---

## 3. Rule 24 four-postulate record

| postulate | how this rectangle satisfies it |
|---|---|
| **(i) MECE over a DECLARED domain** | Domain DECLARED: **the outcomes ADDENDUM 01 adds** -- `{FWD-13, FWD-14, FWD-15}`, denominator 3. Coverage forward: FWD-13 -> {21, 23, 24}; FWD-14 -> {22, 23}; FWD-15 -> {21, 24}. Backward: every cell serves at least one, 0 orphans. **Uncovered member hunted and NONE found** -- each of the three has at least one cell whose criteria can move it. ⛔ `FWD-1`..`FWD-12` are OUTSIDE the CUT domain and are not re-cut -- including them would be coverage-padding, which rule 27 forbids. ⚠ **But they are NOT outside the round's EFFECT** (§0c): the eight re-graded outcomes become exercisable the moment `RP-s-23` lands, without a cell of their own. That is a consequence of the cut, never a claim of it, and the distinction is postulate (iv)'s. |
| **(ii) SAME GRAIN** | Grain is `(seam artifact, outcome)` -- each cell is one artifact at the seam: the ported module, the mapper module, the wired-and-deployed function, the before/after comparison. Not `(manifest row, outcome)` as rounds 1-3 used, **and that change is deliberate and stated**: the addendum's domain is a code seam, not the PRD's 13-row manifest, so the old grain has no referent here. |
| **(iii) INTENT COHERENCE** | One axis, one intent: **make the email a person receives carry the specimen's structure over live numbers.** The four cells are the four steps of one port -- lift the logic, feed it live data, ship it, prove nothing was lost. No cell carries a second intent. |
| **(iv) STATE COHERENCE** | The remedy moves `FWD-13/14/15` from absent toward gradeable, **and moves the eight re-graded outcomes from APPLIED to EXERCISABLE** -- corrected from this document's first draft, which said the round did not touch them (§0c). ⛔ **NAMED: what it does NOT move** -- (a) it does not move `FWD-2/9/10`, whose bar IS APPLIED and which the specimen already satisfies on its own terms; (b) it does not move **any EXERCISED bar to REALIZED** -- not `FWD-13`'s, not `FWD-15`'s, not the eight's. Every one of them needs a real 9 AM email READ BY A PERSON. ⭐ **A cell can produce the edition; it cannot produce the reading**, and no criterion in this round may be written as though it can; (c) it does not move `FWD-8`'s box grain, which is Andrew's payer-account billing setting. |

---

## 4. BATTERY DISPOSITION -- RE-RUN AT THIS CUT

**`comp-surprise --project NFRA_REPORT` -- RUN at this cut.** 30 investigation items, 13 adjudication
rows, 16 remediation rows, 0 duplicate ids, 0 malformed, **OPEN 0, ARMED 0.** The channel is clean at
the cut: **no armed hazard is carried into round 4.**

**`aws lambda get-function-configuration` -- RUN at this cut** (§0b). The pre-state of the artifact
this round deploys over.

**FINDINGS THAT BIND THIS ROUND, carried:**
- ⭐ **`C-MORATORIUM-CLEARED` -- and it clears THIS WORK ONLY.** Andrew's word, verbatim via the
  addendum: *"this isnt creating an alarm, it is just swapping out the code of the existing lambda"*.
  ⛔ **No cell may mint a new alarm, topic, subscription, schedule or notification.** The standing
  moratorium is otherwise untouched and this cut does not widen it by a word.
- ⛔ **`C-DEPLOY-PATH`: NEVER `aws lambda update-function-code`.** The function's own Terraform says so
  at `infra-monitor.tf:7`. Artifact -> `s3://opal-<account>-lambda-artifacts/shared-infra/opal-infrastructure-monitor.zip`
  -> `source_code_hash` -> **`safe-apply`**. Binds `RP-s-23` and travels in its worker face.
- ⛔ **THE LAYER-SHAPED ARTIFACT (§0b).** 40,015 deployed bytes with `layers = [anthropic_sdk_deps]`.
  The vendored packages in the source folder do **not** belong in the zip. Binds `RP-s-23`.
- **`C-NO-FROZEN-FACTS`:** a row that cannot be collected live is **OMITTED WITH A STATED REASON**,
  never rendered from a literal. Binds `RP-s-22` and is its strongest criterion.
- **THE MAIN-CHECKOUT CENSUS CONSTRAINT**, ruled at msg 20822, durable in `project.json` `blocking`
  fact (6), citable at `org/modules/graph/INSTRUMENT_LIMITS.md` LIMIT 4 / 4a: any census or absence
  claim is run from the MAIN checkout, never from the worker's own linked worktree; a comp-rail zero
  obtained inside a worktree is **not evidence of absence**. **This travels in every worker face.**
- **`C-CHANGE-LEDGER` + NEVER-2:** the entry opens before the first deploy act and closes at
  completion, in the same cell. Half-landed is not an option.

---

## 5. What this decomposition REFUSES to assume

1. **That the addendum's five named collectors are the denominator.** Measured: 13 sections (§0). The
   addendum's own `C-NO-REGRESSION` says the Lambda "carries more than this project measured", and
   this is that, quantified.
2. **That an absent section is a regression.** `ai_analysis` is `None` by design on a clean day. The
   partition has three buckets, not two (§0).
3. **That a source-level check can score `FWD-14`.** The addendum warns of exactly this and it is the
   same rendered-vs-source trap that resized round 3. **`RP-s-23`'s criteria read the DEPLOYED
   package**; a grep of the repo would pass while the shipped zip still carried a literal.
4. **That the deploy is a code swap.** It is a code swap **plus** a mapper that did not exist, because
   the specimen does zero live reads. A swap alone would email a frozen 9-September snapshot forever
   and look correct doing it -- the addendum's central finding, and the reason this is four cells.
5. **That this round can close `FWD-13`.** Its bar is EXERCISED: a real 9 AM email, read by a person.
   ⭐ **A cell can produce the edition; it cannot produce the reading.** The manual trigger Andrew
   asked for is QA and **the scheduled fire remains the acceptance** (`C-MANUAL-TRIGGER`).
6. **That the specimen was wasted.** It is the half that was hard, and `RP-s-21`'s port-fidelity
   criterion exists to carry it across intact rather than re-derive it.

---

## 6. Holds

- **NONE held by this lane.** `RP-s-21` and `RP-s-22` are cuttable at this edit; `RP-s-23` and
  `RP-s-24` are issued and dependency-blocked, not held.
- **NOTHING IS OWED BY ANDREW** beyond the authorization already given and seeing the manual
  trigger's output when it runs (addendum §6).
- ⛔ **`estate-report-0900et` IS UNTOUCHED** -- a different directive, out of scope by the addendum §5.
- ⛔ **`FWD-8`'s BOX-GRAIN limb remains OUT OF SCOPE** (Andrew's payer-account billing setting).
- ⚠ **The `worker.md` model-field divergence and the "Rule 27 one-project-per-instance" phantom are
  both live at `1.0.0_SA_CTO~Z` and NEITHER GATES THIS ROUND.** Spawns here pass no `model` parameter
  (msg 20805), which is correct under either resolution.
