# AMGT_RESAPP task order -- `AMGT-bj-2` -- THE SCOPED API CARRIES THE KEY-SCOPED FEED READ (`AMGT-bj-1`) FROM A MERGED PIN, AND ITS FIRST REQUEST IS DRIVEN ALONE -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bj-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bj-2.redeploy-the-scoped-api-carrying-the-key-scoped-feed-read-from-a-merged-pin-and-drive-its-first-cold-request</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route or schedule moves.
comp-adversary: RUN at the cut -- r102_phase_table.py with `--feed-max-ms 2000 --handler-max-ms 4000` reads `R103 COLD TARGET: NOT MET` on round 102's first cold request (feed 18,796 ms, handler 20,566 ms) and `MET` on a control lines file (feed 900 ms, handler 2,410 ms); r103_feed_equal_check.py reads 16 of 16 on the candidate and 15 of 16 on the base; this order is a STAGED shell whose pin, numbers and pair are filled at its GO.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-bj-2` (round 103, decomposition s.111)

CTO~DELL1 round-102 analysis item 1. ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the MERGED pin the GO names: a `box/dell1` first-parent commit that
carries `AMGT-bj-1`'s `lib/research/api/scoped_amgt.py` (its blob printed by the GO; the prepared candidate is `84002d3fd559`, from `02627c18a0ea`). **THE BUILD'S OWN CONTENT-DIFF SUMMARY IS THE
AUTHORITY ON WHAT SHIPS** (round 102 stopped at a member the pair did not name): the pair's table names every CHANGED member the build prints, each by blob, and a member the pair does not name is a
STOP. **Rollback is a REBUILD from the merged pin the live function was built from** (the function keeps only `$LATEST`; the CTO, msg 4287): the pair names that pin (`6ecb5bc567`, live
`bKCGUhXp..`) and its blob table, and the rebuild is ONE `safe-apply`, same hour. Change-management entry opened before, closed after; the `lambda-source-map.json` entry printed before and after.

SEQUENCE, in this order and no other:
1. read the live `CodeSha256` and print it (the pair names it); capture the live Thesis payloads (`aw4_capture.py`, 95 names, local) to `.scratch_bj2/thesis_pre.json` and the 527-request route
   baseline, IMMEDIATELY before the apply; re-run `r94_naming_replay.py --pin 6ecb5bc567` on the BUILT zip and print its denominator (non-zero differ is a STOP, as in round 102);
2. the apply;
3. **THE FIRST ACT AFTER THE APPLY, before any capture, replay or other reader:** `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_first_cold_request.py org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/BJ2_FIRST_COLD_REQUEST_20261014.txt`. One overlay request for `ASML_NA_Equity`, driven
   alone: the first request on a new package runs in a new execution environment, so it is COLD by construction (the CTO accepted this for "15 quiet minutes", msg 4919). It reads RECORDED or
   NOT COLD (then say so and do NOT repeat it: the issuer decides). Commit the file with the rest;
4. the thesis capture and the route replay, after, as in round 102's `AMGT-bi-2`;
5. the criteria below.

The effect is: the overlay's `feed` and `top_band` phases read the subject's rows only; NO served byte moves. **No other reader runs on the function during your capture and replay.**

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
  <criterion id="AC1" cell_refs="AMGT-bj-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>the earlier serves are KEPT: R97 SECTOR SERVE CENSUS: YES (6 of 6), R95 CLASSIFICATION CENSUS: YES (6 of 6), R94 NAME CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bj-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay4_compare.py" ".scratch_bj2/thesis_pre.json" ".scratch_bj2/thesis_post.json"; echo "exit=$?"</invocation><expect>no served byte of the corpus field moved: `ay4 names 95 team_sheet_equals_stored15 95/95 others_equal 95/95`, `growth_exceeds_delta 0`, the max under 6,291,456 bytes; `ay4 compare build 1/1`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bj-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_phase_table.py" --id-file "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/BJ2_FIRST_COLD_REQUEST_20261014.txt" --feed-max-ms 2000 --handler-max-ms 4000 | tail -12; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the request's phase table from its own log stream: `PASS T1` to `PASS T5` and `R102 PHASE TABLE: YES` (all fourteen phases, a cold container, the sums within 5 percent or 5 ms), then `TARGET feed <= 2000 ms: MET`, `TARGET handler <= 4000 ms: MET` and `R103 COLD TARGET: MET`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback (the rebuild from the live function's merged pin, its blob table printed) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-bj-2.redeploy-the-scoped-api-carrying-the-key-scoped-feed-read-from-a-merged-pin-and-drive-its-first-cold-request.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the change-management entry's slug and state;
- every criterion's output lines;
- the post-act compare file path, with the changed-path count and the count outside the table;
- the first cold request's request id, handler time, Init Duration, its fourteen phase lines and the `AMGT_SEGMENT gold_article_security_mention_{list,get,decode}` lines of its log stream;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's close (round-102 analysis item 1): "ONE driven first overlay on a fresh container after 15 quiet minutes, with the feed phase read from the bi-1 log lines. The negative
arm is the current build's 18.8 s. Target: feed phase at most 2 s, first overlay at most 4 s." The substitution (a first request on a new package) was accepted in round 102. AC3 requires the TARGET
MET: if the driven request misses it, the order reads a failing criterion with the numbers, the apply STANDS (no served byte moved) and the log stream's `list`/`get`/`decode` lines are the input to
round 104; a timeout or a differing body is Branch 2. STAGED. THE GO WAITS ON ALL OF: (1) `AMGT-bj-1` complete and MERGED, reviewed by the CTO at the pair; (2) `AMGT-bj-4` merged, so the pair's
member table comes from the corrected tool (the build's own diff stays the authority); (3) THE PAIR, whose COO half is written from the pin's own handler against the live function (route tables
and `r98_thesis_fullbody_compare.py` from the pin's tree); (4) no other reader on the function.

<status>staged</status>
<round>103</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
