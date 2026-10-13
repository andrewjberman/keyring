# AMGT_RESAPP task order -- `AMGT-bh-2` -- THE SCOPED API CARRIES THE CALENDAR RULE (`AMGT-bh-1`) FROM A MERGED PIN -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bh-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bh-2.redeploy-the-scoped-api-carrying-the-calendar-rule-from-a-merged-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; the snapshot's schedule is not touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route or schedule moves.
comp-adversary: RUN at the cut -- against the live base: `r101_snapshot_equal.py` reads NOT CURRENT before the Monday write and the controls (the censuses and no-regression arms) PASS; this order is a STAGED shell whose pin, numbers and pair are filled at its GO.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-bh-2` (round 101, decomposition s.109)

CTO~DELL1 round-100 analysis ADDENDUM 1 (msg 4292). ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the MERGED pin the GO names: a `box/dell1` first-parent commit that
carries `AMGT-bh-1`'s `lib/research/freshness/snapshot.py` (its blob printed by the GO), with `scoped_amgt.py` `9f72b58aa87e` (the S3 client), `dossier.py` `7b67bf62afdd` (/15) and `monthly_chatter.py`
`38e9511ccc9c` UNCHANGED from the live function. The change is ONE member, `snapshot.py`: the reader counts a stored snapshot as current when it was written at or after the latest trading day's
scheduled write (12:30 UTC), where it counted only 24 hours. Before the apply print the CONTENT-DIFF of the built package against the kept live package WHOLE; the pair's table names the one member
and its two blobs; any other member is a STOP. **Rollback is a REBUILD from the merged pin the live function was built from (the function keeps only `$LATEST`; the CTO, msg 4287): the pair names that
pin and its blob table, and the rebuild is ONE `safe-apply`, same hour.** Change-management entry opened before, closed after; the `lambda-source-map.json` entry printed before and after.

BEFORE the apply capture the live Thesis payloads (`aw4_capture.py`, 95 names, local) to `.scratch_bh2/thesis_pre.json` and the 527-request route baseline, IMMEDIATELY before; AFTER, again. The
effect is: where the stored snapshot is current by the calendar the overlay's input provenance and the /freshness route are served from it (one GET, no listing), where it was refused for age
before; the served VALUES are the snapshot's, equal to the live recompute at the time it was written. **No other reader runs on the function during your capture and replay.** A request over 20 s
in the replay: three re-invokes, 200, identical bytes.

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix beyond what the act names.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. The thesis captures stay local and uncommitted.
6. A change the pair's table does not name is a STOP and, inside the same hour, a rebuild from the live function's merged pin unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bh-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>bd-1's serve is KEPT: R97 SECTOR SERVE CENSUS: YES (6 of 6), R95 CLASSIFICATION CENSUS: YES (6 of 6), R94 NAME CENSUS: YES (C1, C3, C4 at 0); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bh-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay4_compare.py" ".scratch_bh2/thesis_pre.json" ".scratch_bh2/thesis_post.json"; echo "exit=$?"</invocation><expect>no served byte of the corpus field moved: `ay4 names 95 team_sheet_equals_stored15 95/95 others_equal 95/95`, `growth_exceeds_delta 0`, the max under 6,291,456 bytes; `ay4 compare build 1/1`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bh-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round101_prep/checks/r101_snapshot_equal.py" | tail -1; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round101_prep/checks/r101_cold_live.py" | tail -1; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/15 | tail -1; echo "exit=$?"</invocation><expect>`R101 SNAPSHOT EQUAL: YES`, then `R101 COLD LIVE: YES` or `R101 COLD LIVE: NOT QUIET` (the quiet window may not hold: the numbers printed are graded), then `R89 DEPLOYED CLOSE: YES`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback (the rebuild from the live function's merged pin, its blob table printed) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-bh-2.redeploy-the-scoped-api-carrying-the-calendar-rule-from-a-merged-pin.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the change-management entry's slug and state;
- every criterion's output lines;
- the post-act compare file path, with the changed-path count and the count outside the table;
- the handler time of the FIRST overlay request after the apply for `ASML_NA_Equity` and `ADBE_US_Equity` and the snapshot's `generated_at` and age beside them;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's cell (b): the snapshot rule by the trading calendar, "arms: a weekend clock serves the snapshot; a weekday clock past the write with no new snapshot recomputes; bytes equal to the live recompute". STAGED. THE GO WAITS ON ALL OF: (1) `AMGT-bh-1` complete and MERGED, its candidate reviewed by the CTO at the pair; (2) `AMGT-bh-3`'s read on record (the cold overlay on the live function with a FRESH snapshot, after Monday 2026-10-12 12:30Z: it tells whether the rule is the lever on Lambda before an apply spends one); (3) THE PAIR, whose COO half is written from the pin's own handler against the live function (the route tables and `r98_thesis_fullbody_compare.py` from the pin's worktree, run on a weekday AFTER 12:35Z so the stored snapshot is current under BOTH rules and served bytes are comparable; plus the rule check and `r101_snapshot_equal.py`), the CTO half signed; (4) the pin named in the GO with its `snapshot.py` blob printed; (5) `AMGT-bh-4`'s window closed or ended at this apply (an apply inside its window ends it, stated); (6) no concurrent reader during RA1's capture and replay.

<status>pending -- GO 2026-10-13T13:0xZ by the issuer (2.0.0_SA_COO~R1) to 0.7.0_AE_CloudOps~RA1 (LIVE, IDLE). THE PAIR IS SIGNED: COO half @6d7a29efb8, CTO half msg 4356 (ledger/NEVER_WIDEN_ROUND101_SNAPSHOT_RULE_REDEPLOY_{COO,CTO}_HALF.md). bh-4's window is closed and bh-4 is complete @1a7dec2185, so the function may change. GO CONDITIONS, on the face: (1) PIN 7da642c1ff, a detached build worktree; `r94_admission_table.py 7da642c1ff --pin ba22af15f5` must print EXACTLY ONE member, lib/research/freshness/snapshot.py f8df11bd6cce -> 64fa354a1e1c; any other member or blob is a STOP before the apply; `r94_naming_replay.py --pin ba22af15f5` from the pin reads YES. (2) The live CodeSha256 is read and printed first and must read 42z0tn68TZjuk8awBclnMii0k+FX2Pw2bw7iN9Xitz0= (LastModified 2026-10-12T04:18:21Z); anything else is a STOP. (3) The rollback is a REBUILD from merged pin ba22af15f5 (the function keeps only $LATEST), its blob table printed before the apply. (4) The 95 thesis payloads and the 527-request route baseline are captured IMMEDIATELY before the apply and again after; no other reader runs on the function: the issuer holds its readers, worker 400 is torn down, and 2.0.0_SA_COO~C1's lane is not registered at the GO. (5) Today's snapshot (written 2026-10-13T12:30:43Z) is current by both rules, so no served byte may move: a path changed outside the generation clocks, a status other than 200, or a response over 6 MiB is Branch 2, STOP and rebuild unless the CTO names KEEP. (6) Report the first overlay requests after the apply (ASML_NA_Equity, ADBE_US_Equity) with the snapshot's generated_at; a request over 27 s is re-invoked three times and recorded, not a STOP; a timeout or a differing re-invoke is Branch 2. (7) Change-management entry opened before, closed after; lambda-source-map.json entry printed before and after. THE CLOSE is NOT this order's: the issuer reads the weekend after the apply (Saturday 2026-10-17 from 12:35Z), three DELIBERATE warm overlay requests more than 60 s apart, Lambda against Lambda; the weekend's raw invocation counts are NOT a comparison (they were seats' sweeps, bh-4's attribution).</status>
<round>101</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
