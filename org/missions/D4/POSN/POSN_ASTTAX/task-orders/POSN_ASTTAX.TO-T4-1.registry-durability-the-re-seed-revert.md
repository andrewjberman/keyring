# TO POSN_ASTTAX.TO-T4-1 -- make the registry HOLD its values against a re-seed, so `AT2-s-5`'s writes and any retag cannot be silently reverted (AT3-s-4, FWD-1)

<to_id>POSN_ASTTAX.TO-T4-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~13</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>staged</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`49ddcc481d` · **Decomp cell:** `AT3-s-4` · **Issuance:** round 3. **INDEPENDENT chain.**

---

## THE CELL

Row `POSN_ASTTAX-Z-W3-S1` (ARMED): `seed-etf-classifications.py` does an **unconditional full-item
put** over the whole ticker universe, and the six commodity tickers are **absent from
`ETF_MANAGEMENT_STYLE` in all three copies** of the canonical module. So a seed run rewrites
`management_style` back to `"unknown"` on exactly the six rows `AT2-s-5` corrected -- **and
`asset_class` back to `hedge` on exactly the rows `AT3-s-6` is about to move.**

⚠ **LATENT, NOT ABSENT.** My row `POSN_ASTTAX-Z-S4` measured the trigger unscoped -- 111 references
across 56,445 files, and the one gold-producer candidate references the seeder in **COMMENTS only
(`CODE=0`)**. Nothing on a clock fires it. **A deliberate manual run still reverts everything.**

⭐ **WITHOUT THIS CELL THE ROUND IS REVERSIBLE BY ONE COMMAND.** Every other cell in round 3 can be
undone by a single seed run, and nothing would announce it.

## THE ACT

1. **Measure the current state** (`T4-AC1`): which of the retag-set tickers are present in
   `ETF_MANAGEMENT_STYLE`, in how many module copies, with your own denominator.
2. **Make the registry survive a re-seed** (`T4-AC2`). **The shape is yours to choose and to state** --
   populate the map, make the put conditional, or another mechanism. State which and why, and name what
   your choice does NOT fix.
3. **Prove it with a control that FAILS on the old bytes** (`T4-AC3`): simulate a seed run and show the
   corrected values SURVIVE after, and were REVERTED before.
4. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT RUN THE REAL SEEDER AGAINST THE LIVE TABLE.** Simulate, or run against a scratch target.
  A live full-item put is exactly the hazard this cell exists to remove.
- ⛔ **DO NOT RETAG.** `asset_class` values stay as they are; `AT3-s-6` owns the retag.
- ⛔ **DO NOT DEPLOY.**
- ⚠ **MEASURE THE WORKTREE, NOT JUST HEAD.** `seed-etf-constituents.py` carries UNCOMMITTED bytes
  preserved at `5c9e329a21` (13 insertions / 6 deletions, another seat's, reviewed by nobody). Reading
  the committed producer alone means reasoning about a version someone has already partly revised, and
  **the difference is invisible unless you look.** Do not apply or commit those bytes; read, and say
  what you read.
- ⚠ Three module copies exist. A fix in one is a fix in one -- print the denominator.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W13-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="T4-AC1" cell_refs="AT3-s-4"><invocation>timeout 180 comp-find 'ETF_MANAGEMENT_STYLE' --all --files</invocation><expect>the printed DENOMINATOR and every file carrying the map; then, per copy, whether each of DBC, GLD, GSG, IAU, SLV, USO is PRESENT or ABSENT -- a 6-by-N table with both counts stated. State the WORKTREE state separately from HEAD where they differ.</expect></criterion> `T4-AC1` -- THE MAP, EVERY COPY, WITH ITS DENOMINATOR.

<criterion id="T4-AC2" cell_refs="AT3-s-4"><invocation>timeout 180 python &lt;your durability change&gt;</invocation><expect>the change applied, with the SHAPE you chose named and justified in one sentence, and an explicit statement of what it does NOT fix. Per-copy confirmation that the change reached every copy AC1 enumerated, or a stated reason a copy was left alone.</expect></criterion> `T4-AC2` -- THE FIX, ITS SHAPE STATED, ITS LIMITS NAMED.

<criterion id="T4-AC3" cell_refs="AT3-s-4"><invocation>timeout 180 python &lt;your simulated-reseed control&gt;</invocation><expect>two runs side by side against a SCRATCH target, never the live table: BEFORE (old bytes) a simulated seed reverts management_style to "unknown" on the six; AFTER it does not. Both outputs pasted verbatim, and a FALSIFY arm using old bytes in both positions that must FAIL.</expect></criterion> `T4-AC3` -- ⭐ **THE CONTROL THAT MUST FAIL ON THE OLD BYTES.** "The map now contains them" is not evidence the seeder stops reverting.

<criterion id="T4-AC4" cell_refs="AT3-s-4"><invocation>timeout 120 git -C . diff --stat HEAD</invocation><expect>the diffstat verbatim, showing only this cell's granted paths were touched and that the preserved uncommitted seed-etf-constituents.py bytes were NOT applied or committed by this order.</expect></criterion> `T4-AC4` -- THE WRITE SURFACE, AND THE PEER'S BYTES LEFT ALONE.

<criterion id="T4-AC5" cell_refs="AT3-s-4" judgment="true"/> `T4-AC5` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether the registry now genuinely survives a re-seed, or survives only the specific simulation this cell wrote. **Record the readings and offer NO verdict.**

<expected_criteria>T4-AC1, T4-AC2, T4-AC3, T4-AC4, T4-AC5</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T4-1.registry-durability-the-re-seed-revert.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~13/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py
infra/aws/lambda/v2_portal/_shared/etf_classification.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round3.md</decomp_doc> round 3, cell `AT3-s-4`.
<owned_cells>AT3-s-4</owned_cells>
Read-dependencies, NOT claimed: independent of every other round-3 cell. It protects their results; it does not wait on them.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting built or changed; the
seeder's trigger was measured by `POSN_ASTTAX-Z-S4` as manual-only and this order does not change that.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched. A DENIED write against a
scratch target is a ROW naming the missing permission, never an IAM edit by this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied: the issuer measured the seeder's TRIGGER but never its full-item put against a live table, and
has not read the uncommitted `seed-etf-constituents.py` bytes beyond their diffstat and reasoning.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~13/POSN_ASTTAX.TO-T4-1.registry-durability-the-re-seed-revert.proof_of_spec.json
</proof_of_spec>
