# TO POSN_ASTTAX.TO-T6-1 -- RETAG the commodity/hedge set to their ratified five-class labels. Successor to the never-run `TO-S2-1`, and its acceptance criterion now FAILS IN THE BROKEN WORLD (AT3-s-6, FWD-1/FWD-2)

<to_id>POSN_ASTTAX.TO-T6-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~15</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>staged</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`49ddcc481d` · **Decomp cell:** `AT3-s-6` · **Issuance:** round 3.
**DEPENDS ON `AT3-s-5` (the bar, must read GO), `AT3-s-2` and `AT3-s-3` (both terminal).**

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
3. **Retag, per ticker, each with its ratified target and a stated reason** (`T6-AC3`). Not a bulk set.
4. **Read back from the SERVED artifact and assert BOTH halves** (`T6-AC4`).
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT RUN IF `AT3-s-5` READS NO-GO.** Stop and file a row. The gate is the point.
- ⛔ **TOUCH NO HOLDING, NO WEIGHT, NO SATELLITE PLACEMENT.** VXX already flows correctly into
  Satellites 70/80/90/98 via the MODELS path. POSN retags the served top-level `asset_class` ONLY.
- ⛔ **DO NOT MINT A SIXTH CLASS.** Five are ratified.
- ⛔ **DO NOT DEPLOY** and do not touch portal.
- ⚠ `AT3-s-4` may have changed how the registry resists a re-seed. Do not undo it; if your write and
  its mechanism disagree, that is a ROW and you stop.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W15-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="T6-AC1" cell_refs="AT3-s-6"><invocation>timeout 120 grep -n "&lt;status&gt;" ../task-orders/POSN_ASTTAX.TO-T5-1.the-bar-step-2-measured-against-the-served-artifact.md ../task-orders/POSN_ASTTAX.TO-T2-1.measure-the-frontend-hop.md ../task-orders/POSN_ASTTAX.TO-T3-1.hop-test-the-two-sibling-consumers.md</invocation><expect>the status line of all THREE predecessors pasted verbatim, each reading `complete`; AND the GO verdict quoted from AT3-s-5's instance. If any is not terminal, or the bar reads NO-GO, this order STOPS and files a row instead of proceeding. NOTE: this path is relative to a sibling of task-orders/ -- if it fails with "No such file", that is a CWD problem and NOT evidence a predecessor is missing; corroborate with a second instrument before concluding anything.</expect></criterion> `T6-AC1` -- THE GATE, CHECKED NOT ASSUMED. ⚠ Its failure text is indistinguishable from its own negative (`POSN_ASTTAX-Z-W6-S1`) -- corroborate.

<criterion id="T6-AC2" cell_refs="AT3-s-6"><invocation>timeout 180 python &lt;your pre-retag capture&gt;</invocation><expect>per member: the PRE-retag served asset_class value and allocation weight, read from the served artifact with its vintage (URI/path, LastModified, size) pasted verbatim. This is the baseline AC4 compares against; without it "equal to its pre-retag weight" is unassertable.</expect></criterion> `T6-AC2` -- THE BASELINE, CAPTURED BEFORE THE WRITE.

<criterion id="T6-AC3" cell_refs="AT3-s-6"><invocation>timeout 180 python &lt;your per-ticker retag script&gt;</invocation><expect>one line per ticker written: ticker, old asset_class, new ratified label, and the one-sentence reason. No ticker written without a reason. No bulk set. The write's own return value is NOT evidence -- AC4 is.</expect></criterion> `T6-AC3` -- THE RETAG, PER TICKER, EACH ON ITS OWN BASIS.

<criterion id="T6-AC4" cell_refs="AT3-s-6"><invocation>timeout 300 python &lt;your served read-back, both halves&gt;</invocation><expect>after a regenerate, read the SERVED artifact and assert per member, as TWO separate results: (a) served asset_class/assetClass == the ratified five-class label, (b) allocation weight NON-ZERO and EQUAL to the AC2 baseline. Both numbers shown per member. A member rendering 'Unknown', or carrying a zeroed weight, is a FAIL -- and a FAIL here is a REGRESSION to be rolled back and rowed, not a note.</expect></criterion> `T6-AC4` -- ⭐ **THE CRITERION THAT FAILS IN THE BROKEN WORLD.** This replaces `S2-AC5`. "The page still renders" is true in both worlds and grades nothing; the served VALUE and the WEIGHT separate them.

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
