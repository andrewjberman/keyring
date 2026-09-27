# TO DSGN_IRPTV1.TO-IV-e-54 -- F45-AC9 and F57-AC2 pass by fixing their product cause (row W29-S8)

<to_id>DSGN_IRPTV1.TO-IV-e-54</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~34</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<round>8</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Round:** 8 (CTO analysis @36e18bf320, msg 101845) | **Decomp cell:** `IV-e-54` (decomp v8) | **outcome_ref:** FWD-1 (the suite the round grades by) | **depends_on:** none | **slot:** ~34, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-54` -- Rows: DSGN_IRPTV1-W29-S8 (CTO ruling 101845 section 2: a product-path cell, never a wider Q allowance).

Two pinned tests fail on product paths no earlier order granted:

- **F45-AC9** (`__tests__/fe-s-45/residuals.test.ts:354-440`; the failing check is `expect(clean).toBe(kept.length)` at :439). The census
  counts `scripts/dev-live.mjs:23-24` (`createServer({configLoader:'runner'})`) as a KEPT config loader, but the watch driver
  `__tests__/fe-s-45/dev-script-writes.mjs` (:307) only runs `__tests__/fe-s-38/resolve-config.mjs`, so dev-live is logged NOT MEASURED
  and never counted clean. The test expects every kept loader to be run under the watch and to write nothing through the junction.
- **F57-AC2** (`__tests__/fe-s-57/carry.test.ts:118-191`). The contract (`docs/contracts/investor-reporting/v1/routes.json`) now
  declares 17 routes, not 12. `selection-create` and `directory-browse` (`contracts/envelope.ts:151-152`) return shapes with no
  `.availability`, so `carryUnprojectedGrant` (`contracts/adapt.ts:349-357`) has nothing to carry the grant on, and neither route is on
  the test's no-availability exception list. The test expects `problems` empty and `declared.length` equal to 12 (:188-190).

**Build:** Fix each by its cause. For F45-AC9: make dev-live's loader measured under the same watch (the driver runs it, or dev-live's
kept loader is the one the driver already runs) so it is counted clean or shows the write it makes. For F57-AC2: carry the grant
on every declared route that has an availability plane, and name the two routes without one as contract-legal exceptions by their
contract line. **Where a test's assertion is itself wrong against the ratified contract** (for example the literal 12 against 17
declared routes), name the contract line in the test and re-golden it with the served values kept (the W29-S2 pattern, CTO 101768).
Never widen a Q allowance, add a retry or skip a test.

**Environment:** the portal worktree is based on local DEV `3f76cdb2` (round 7 drained). Other round-8 workers run in parallel in their own worktrees on disjoint files; edit only your `<paths>`. Do not start any server.

### ACCEPTANCE

<criterion id="IVE54-AC1" cell_refs="IV-e-54"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-34/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/fe-s-45/residuals.test.ts 2>&1 | tail -15</invocation><expect> 0 fail</expect></criterion>
<criterion id="IVE54-AC2" cell_refs="IV-e-54"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-34/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/fe-s-57/carry.test.ts 2>&1 | tail -15</invocation><expect> 0 fail</expect></criterion>

Each mechanical criterion prints its expect string only when every arm holds. AC1 and AC2 each run one whole test file; each FAILS at the base (one failing test each).

<expected_criteria>IVE54-AC1, IVE54-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/lib/**`, `contracts/**` (unless named), other pages and every file not named are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/scripts/dev-live.mjs
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-45/residuals.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-45/dev-script-writes.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-57/carry.test.ts
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8, cell `IV-e-54`.
<owned_cells>IV-e-54</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE54-AC1, IVE54-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~34/DSGN_IRPTV1.TO-IV-e-54.product-path-residuals.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE54-AC1,IVE54-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W34-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3f76cdb2 (issuer, 2026-09-27 ~08:1xZ); file:line facts above are from that read.
lane: the <paths> block IS the grant; disjoint from every parallel round-8 chain (decomp v8 table).
</preflight>

Seating: slot ~34, queue position 1 of 2; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 34 --portal-ref <DEV at seating>` when C: allows (0.0.0_AB_MSTR 101618).
