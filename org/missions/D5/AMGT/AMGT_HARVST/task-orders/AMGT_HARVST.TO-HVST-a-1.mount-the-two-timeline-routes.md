# AMGT_HARVST task order -- `HVST-a-1` -- ROUND 12 chain 1 of 3, cell 1 of 2: DECLARE the two timeline routes on the gateway (source only; the deploy is `HVST-a-2`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-a-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~35</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on scoped-amgt-api.tf or scoped_amgt.py; this cell deploys nothing, applies nothing, pushes nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- source and test edits only; no AWS call of any kind.
comp-adversary: RUN at L5 -- the adversary is a mount list and a handler table that agree with EACH OTHER at 18 while the terraform's own count precondition still reads 16, so the first plan refuses. AC1 grades all three together.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO `terraform` COMMAND OF ANY KIND (no init, plan, apply), NO AWS CALL, NO DEPLOY, NO PUSH.** The deploy is a
   separate cell on a separate seat under its own sign-off.
2. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~35/scripts/` -- **never `.scratch/`.**
3. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~35/AMGT_HARVST.TO-HVST-a-1.mount-the-two-timeline-routes.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-a-1.mount-the-two-timeline-routes`.
4. `lib/research/api/` and the scoped API terraform are shared with AMGT_RESAPP. Change ONLY what the mount needs.

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_scoped_amgt_mount.py
lib/research/api/tests/test_timeline_routes.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~35/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL

Round 11 (`HVST-z-0`) wired both timeline routes into the handler but left them UNMOUNTED on purpose: the gateway
route list lives in `infra/aws/terraform/harvest/scoped-amgt-api.tf` (`scoped_amgt_routes`, ~:314), and
`test_scoped_amgt_mount.py` diffs that list against `scoped_amgt_route_table()` in BOTH directions, so adding the
routes on one side only turns it red. `z-0` therefore declared them as data in `scoped_amgt.TIMELINE_ROUTES` and
left the table at 16; a test in `test_timeline_routes.py` pins that they are ABSENT from the mounted table.

**Do, in ONE commit:**
1. Add both route keys to `scoped_amgt_routes` in the terraform, in that list's own style:
   `GET /api/scoped/amgt/security/{security_key}/timeline` and
   `GET /api/scoped/amgt/security/{security_key}/timeline/day/{date}` (two segments after the key -- a new shape).
2. Move the terraform's own count precondition (`length(local.scoped_amgt_routes) == 16`, ~:346, and its
   `error_message`) to **18**.
3. Fold `TIMELINE_ROUTES` into `scoped_amgt_route_table()` so it returns **18**.
4. Invert the `test_timeline_routes.py` test that pins the routes ABSENT from the mounted table: it now pins them
   PRESENT. Change no other assertion.

## 2. BOUNDS

1. **Two mechanical criteria.** No judgment -- the round's judgment criterion is on `HVST-a-4`.
2. No change to any other route, the authorizer, the integration, the Lambda resource or its timeout.
3. The event route (`/timeline/event/<first_day>`) stays unwired and unmounted.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-a-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round12/checks/a-1.AC1.py</invocation><expect>AC1 RESULT: PASS (0 failure(s))</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-a-1"><invocation>python -m pytest lib/research/api/tests/ -rA --tb=line</invocation><expect>the api suite passes with the pass count printed BEFORE and AFTER (base: 255 passed) and the collected count not falling; test_scoped_amgt_mount.py and the inverted test_timeline_routes.py test are NAMED in the -rA output. A pre-existing failure elsewhere in lib/research/api/ is reported with its error text and filed as a row, never repaired</expect></criterion>
</proof_of_spec>

## 4. WHAT THIS CELL DOES NOT DO

It deploys nothing, runs no terraform, makes no AWS call and touches no portal file. Mounting is only DECLARED here;
`HVST-a-2` applies it under a never-widen pair and a NEVER-2 ledger entry.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **AC1 base: FAIL as expected** (7 failures; dry-run by this seat at shared HEAD before the cut). Its first draft
   parsed every quoted string inside the list and read **18 at a base of 16** -- two quoted phrases in the list's
   comments. Fixed to verb-prefixed strings only, then re-run: 16 / 16 / `== 16`. A check that reads the target
   value at the base is the defect this dry-run exists to catch.
2. **AC2 base: PASS as expected** (255 passed at `4350d5af00`'s drain; a control, not a build check).
3. **Risk WORLD by the L6 floor, not by the act:** `<paths>` names an infrastructure path, and a declared class below
   the inferred floor is refused (spine v3.19 L6). The cell itself runs no terraform and touches no cloud.
4. The precondition line is the adversary: mount and table agreeing at 18 with the precondition at 16 would pass
   the unit test and refuse at the first plan -- on the deploy seat, mid-ledger.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>12</round>
<slot>~35</slot>
<fabric>site-z</fabric>
