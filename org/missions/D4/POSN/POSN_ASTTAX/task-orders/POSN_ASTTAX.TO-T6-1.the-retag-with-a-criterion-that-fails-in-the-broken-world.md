# TO POSN_ASTTAX.TO-T6-1 -- RETAG the commodity/hedge set to their ratified five-class labels. Successor to the never-run `TO-S2-1`, and its acceptance criterion now FAILS IN THE BROKEN WORLD (AT3-s-6, FWD-1/FWD-2)

<to_id>POSN_ASTTAX.TO-T6-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~15</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>cancelled</status>
<cancelled_by>ANDREW-DIRECT ~17:3xZ 2026-09-14 at the 4.0.0_SA_CRO~Z terminal, VERBATIM "All recs approved" on items A-H of the close-out breakdown v0.3 @888a9d281b, with his qualifier "we do not touch Attribution" (F4 out; eight cells). Relayed by 4.0.0_SA_CRO~Z as msg 22863; record org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260914_173xZ_POSN_ASTTAX_BREAKDOWN_ALIGNED_ALL_RECS_APPROVED_ATTRIBUTION_UNTOUCHED.md (commit in flight at this write; hash follows in that seat's message). Breakdown s.4 step 1, approved: "TO-T6-1 cancelled as written, re-cut as R1". CANCELLED AS WRITTEN because the ruled retag differs from this order's act on three axes: the member set is TWELVE (item C; this order was cut on eleven), every write is at BOTH levels (asset_class AND the ruled sub_asset_class Metals / Hedge / Real Estate, items A-B; this order writes one level), and the bar runs on the local build over all nine satellites and both other modes after B1/B2/B4 are deployed and F1-F3 built -- none of which this order's criteria name. THE NEED RE-ENTERS AS ROUND-5 CELL R1 (breakdown s.3), strictly last in that issuance; its task order is minted at the round-5 cut and is the pointer forward. This order never ran: its slot 0.9.0_WK_POSN_ASTTAX~15 was consumed by TO-U1-1 in round 4 (row Z-S62), no instance exists for this order, and the retag NO-GO it sat behind was never lifted for it. Set by the ISSUER 2.0.0_SA_COO~Z, 2026-09-14 ~17:3xZ, per 1.0.0_SA_CTO~Z's brief msg 22834 ("Both flip right after Andrew aligns, before the round-4 slug"). A re-open needs a fresh authorization; the standing successor is R1.</cancelled_by>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`3832ac543c` · **Decomp cell:** `AT3-s-6` · **Issuance:** round 3.
**DEPENDS ON `AT3-s-5` (the bar, must read GO), `AT3-s-2` and `AT3-s-3` (both terminal).**

> **RE-CUT 2026-09-11 ~22:4xZ, BEFORE ANY WORKER RAN THIS ORDER**, against PRD `3832ac543c`. TWO
> substantive changes, both from cells that have since landed: step (3) now requires **BOTH STORES**
> (`AT3-s-4`'s durability fix makes a DynamoDB-only retag ANNOUNCED AND REFUSED at `rc=3`), and the
> bar's clause (b) now reads **LABEL-GROUPED** weight, because the allocation-dict entry does not
> discriminate. Re-pinned from `49ddcc481d`, which is two amendments stale.

---

## THE CELL

PRD s.4 `C-RETAG-SAFETY` step **(3)**: retag. This is the project's central act and it has been
correctly refused twice -- once by `TO-S7-1`'s measured NO-GO, once by this seat declining to cut
`TO-S2-1` as written.

⛔ **WHY `TO-S2-1` WAS NEVER RUN, AND WHY THIS ORDER IS DIFFERENT.** Its acceptance criterion `S2-AC5`
was *"confirm the page still renders"*. Post-`AT2-s-6` that returns **the SAME observation in the
healthy world and the broken one** -- the page renders either way; the failure is a label reading
`'Unknown'` and a weight silently at zero. **Cutting it as written would have produced a PASS over a
live regression.** A criterion that cannot fail in the broken world cannot grade anything.

⭐ **SO THE BAR BELOW IS THE SAME ONE `AT3-s-5` MEASURES, RE-ASSERTED AFTER YOUR WRITE.** Served value
AND weight, per member, read from the served artifact.

⚠ **VXX IS THE ENTIRE LIVE BLAST RADIUS** -- the only held member of the retag set (LT 0.0150 /
ULT 0.0200). The six commodity tickers hold zero rows; their half is latent. If something goes wrong,
it goes wrong on VXX.

## THE ACT

1. **Verify your predecessors** (`T6-AC1`) -- `AT3-s-5` reads GO, and `AT3-s-2` and `AT3-s-3` are
   terminal. ⛔ **If the bar reads NO-GO, THIS ORDER STOPS** and files a row. Do not retag against a
   NO-GO; that is the whole sequence.
2. **Record each member's PRE-retag served value and weight** (`T6-AC2`). You cannot assert "equal to
   its pre-retag weight" later without capturing it now.
3. **Retag, per ticker, each with its ratified target and a stated reason, IN BOTH STORES**
   (`T6-AC3`). Not a bulk set. ⛔ **A DYNAMODB-ONLY RETAG IS NOT A RETAG** -- it is ANNOUNCED AND
   REFUSED (`rc=3`) by `AT3-s-4`'s durability fix, so the value must ALSO land in
   `ETF_CLASSIFICATIONS`. This is PRD step (3) at `3832ac543c` and row `W13-S1`.
4. **Read back from the SERVED artifact and assert BOTH halves** (`T6-AC4`), (b) on the LABEL-GROUPED
   weight and NOT the allocation dict.
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT RUN IF `AT3-s-5` READS NO-GO.** Stop and file a row. The gate is the point.
- ⛔ **TOUCH NO HOLDING, NO WEIGHT, NO SATELLITE PLACEMENT.** VXX already flows correctly into
  Satellites 70/80/90/98 via the MODELS path. POSN retags the served top-level `asset_class` ONLY.
- ⛔ **DO NOT MINT A SIXTH CLASS.** Five are ratified.
- ⛔ **DO NOT DEPLOY** and do not touch portal.
- ⚠ `AT3-s-4` HAS changed how the registry resists a re-seed -- it is terminal @`9ca2aef5db`, not a
  maybe. Do not undo it; if your write and its mechanism disagree, that is a ROW and you stop.
- ⚠ **THE REVERT HAZARD WAS MASKED, AND KNOWING THAT CHANGES WHAT A SUCCESSFUL RUN MEANS.** The
  seeder at the round's base **could not complete a run at all** -- `sub_asset_class=""` for 16 of 136
  tickers, and that is the hash key of GSI `sub-asset-class-index`, so the first offender sorts to
  index 0, batch 1 is rejected and ZERO items are written. ⭐ **Anyone who fixed only the crash would
  have converted a dead script into a working revert.** If you find the seeder running cleanly now,
  that is `AT3-s-4`'s work and the revert path is LIVE -- treat it as armed, not as reassurance.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W15-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="T6-AC1" cell_refs="AT3-s-6"><invocation>timeout 120 grep -n "&lt;status&gt;" ../task-orders/POSN_ASTTAX.TO-T5-1.the-bar-step-2-measured-against-the-served-artifact.md ../task-orders/POSN_ASTTAX.TO-T2-1.measure-the-frontend-hop.md ../task-orders/POSN_ASTTAX.TO-T3-1.hop-test-the-two-sibling-consumers.md</invocation><expect>the status line of all THREE predecessors pasted verbatim, each reading `complete`; AND the GO verdict quoted from AT3-s-5's instance. If any is not terminal, or the bar reads NO-GO, this order STOPS and files a row instead of proceeding. NOTE: this path is relative to a sibling of task-orders/ -- if it fails with "No such file", that is a CWD problem and NOT evidence a predecessor is missing; corroborate with a second instrument before concluding anything.</expect></criterion> `T6-AC1` -- THE GATE, CHECKED NOT ASSUMED. ⚠ Its failure text is indistinguishable from its own negative (`POSN_ASTTAX-Z-W6-S1`) -- corroborate.

<criterion id="T6-AC2" cell_refs="AT3-s-6"><invocation>timeout 180 python &lt;your pre-retag capture&gt;</invocation><expect>per member: the PRE-retag served asset_class value and allocation weight, read from the served artifact with its vintage (URI/path, LastModified, size) pasted verbatim. This is the baseline AC4 compares against; without it "equal to its pre-retag weight" is unassertable.</expect></criterion> `T6-AC2` -- THE BASELINE, CAPTURED BEFORE THE WRITE.

<criterion id="T6-AC3" cell_refs="AT3-s-6"><invocation>timeout 180 python &lt;your per-ticker retag script&gt;</invocation><expect>one line per ticker written: ticker, old asset_class, new ratified label, the one-sentence reason, and BOTH STORE WRITES confirmed separately -- the DynamoDB item AND the ETF_CLASSIFICATIONS entry. No ticker written without a reason. No bulk set. State the rc of the durability guard: an rc=3 ANNOUNCED-AND-REFUSED means you wrote only one store and the retag did NOT land. The write's own return value is NOT evidence -- AC4 is.</expect></criterion> `T6-AC3` -- THE RETAG, PER TICKER, IN BOTH STORES. A ONE-STORE RETAG IS REFUSED BY DESIGN.

<criterion id="T6-AC4" cell_refs="AT3-s-6"><invocation>timeout 300 python &lt;your served read-back, both halves&gt;</invocation><expect>after a regenerate, read the SERVED artifact and assert per member, as TWO separate results: (a) served asset_class/assetClass == the ratified five-class label, (b) the LABEL-GROUPED weight NON-ZERO and EQUAL to the AC2 baseline. ⛔ Show the allocation-dict entry BESIDE it as a NEGATIVE CONTROL that is expected NOT to move -- grading (b) on that column is the `S2-AC5` shape for the third time and it reads identically in both worlds. Three numbers per member. A member rendering 'Unknown', or carrying a zeroed weight, is a FAIL -- and a FAIL here is a REGRESSION to be rolled back and rowed, not a note.</expect></criterion> `T6-AC4` -- ⭐ **THE CRITERION THAT FAILS IN THE BROKEN WORLD.** This replaces `S2-AC5`. "The page still renders" is true in both worlds and grades nothing; the served VALUE and the WEIGHT separate them.

<criterion id="T6-AC5" cell_refs="AT3-s-6" judgment="true"/> `T6-AC5` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether the retag is safe at the SERVED grain for a real viewer, including the consumer paths `AT3-s-2` and `AT3-s-3` measured. **Record the readings and offer NO verdict.**

<expected_criteria>T6-AC1, T6-AC2, T6-AC3, T6-AC4, T6-AC5</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T6-1.the-retag-with-a-criterion-that-fails-in-the-broken-world.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~15/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round3.md</decomp_doc> round 3, cell `AT3-s-6`.
<owned_cells>AT3-s-6</owned_cells>
Read-dependencies, NOT claimed: `AT3-s-5` (the bar, must read GO), `AT3-s-2` and `AT3-s-3` (both terminal before the irreversible act). SUCCESSOR to the never-run `TO-S2-1`; that order stays `staged` until this one lands terminal and gives it a real pointer.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; DynamoDB item writes under
this device's operator credentials. A DENIED write is a ROW naming the missing permission.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. ⚠ NOT covered and stated rather than
implied: the issuer has NOT measured the post-`AT3-s-1` world and is NOT predicting that the bar will
read GO. If it reads NO-GO this order does not run, and that is a correct outcome rather than a failure
of this cut.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~15/POSN_ASTTAX.TO-T6-1.the-retag-with-a-criterion-that-fails-in-the-broken-world.proof_of_spec.json
</proof_of_spec>
