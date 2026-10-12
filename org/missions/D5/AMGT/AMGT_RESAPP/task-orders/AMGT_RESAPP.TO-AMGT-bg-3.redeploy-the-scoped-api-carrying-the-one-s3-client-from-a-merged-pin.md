# AMGT_RESAPP task order -- `AMGT-bg-3` -- THE SECOND APPLY: THE SCOPED API CARRIES THE ONE-S3-CLIENT BUILD (`AMGT-bg-2`) FROM A MERGED PIN -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bg-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bg-3.redeploy-the-scoped-api-carrying-the-one-s3-client-from-a-merged-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route or schedule moves.
comp-adversary: RUN at the cut -- against the live /14 base (`oEDHTRPq..`): `ay4_compare.py` on a base capture read against itself prints `team_sheet_equals_stored15 0/95` and build 0/1 (the base serves /14; at the GO the live function serves /15 and the same arm reads 95/95, which is the CONTROL that the second apply moves no served byte: its criterion is the compare of pre and post, not the stored equality), and `r100_cold_check.py` reads C2 FAIL (146 S3 clients) against the tree without `AMGT-bg-2`; the censuses and no-regression arms PASS at the base. This order is a STAGED shell: its pin, its numbers and its pair are filled at its GO.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-bg-3` (round 100, decomposition s.108)

CTO~DELL1 round-99 analysis section 2 item 2: the connection pool, "TWO served changes, so they ride TWO applies, in this order: /15 first (its read is AMGT_CORPUS's grade), then the pool.
They are never folded into one." ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the MERGED pin the GO names: a `box/dell1` first-parent commit that carries
`AMGT-bg-2`'s `scoped_amgt.py` (its blob printed by the GO) with `dossier.py` `7b67bf62afdd` (/15) unchanged and bd-1's `monthly_chatter.py` `38e9511ccc9c` unchanged. The live function at
the GO is the /15 build `AMGT-bg-1` leaves; the change is ONE module, `scoped_amgt.py`, one function (`_s3_client`) and three module names (`S3_MAX_POOL_CONNECTIONS`, `_S3_CLIENT`,
`_S3_CLIENT_LOCK`). Before the apply print the CONTENT-DIFF of the built package against the kept live package WHOLE; the pair's table names the one member and its two blobs; any other
member is a STOP. Rollback: the kept live package through the module, ONE `safe-apply`, same hour. Change-management entry opened before, closed after; the `lambda-source-map.json`
entry printed before and after.

BEFORE the apply capture the live Thesis payloads (`aw4_capture.py`, read-only, 95 names, local) to `.scratch_bg3/thesis_pre.json`, IMMEDIATELY before; AFTER, to `.scratch_bg3/thesis_post.json`.
The effect is NO served byte: every path of every route reads as it did (generation clocks apart). **No other reader runs on the function during your capture and replay.** One request over
20 s in the replay: three re-invokes, 200 with identical bytes. The pair adds a COLD-FIRST-REQUEST arm (CTO msg 4244): the first overlay request of `ASML_NA_Equity` and of `ADBE_US_Equity` after the apply, and after a quiet period of at least 15 minutes, each 200 and under 27 s (a 27 s to under 29 s 200 with identical re-invokes is recorded, a timeout or a differing re-invoke is Branch 2). The close of the CTO's cell is a read by the issuer the day AFTER the apply (the 24-hour count of invocations over 20 s and
of pool warnings against 53 and 49, by the round-99 method); it is not this order's.

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix beyond what the act names.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
6. The thesis captures stay local and uncommitted.
7. A change the pair's table does not name is a STOP and, inside the same hour, a restore of the kept package unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bg-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>bd-1's serve is KEPT: R97 SECTOR SERVE CENSUS: YES (6 of 6), R95 CLASSIFICATION CENSUS: YES (6 of 6), R94 NAME CENSUS: YES (C1, C3, C4 at 0); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bg-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay4_compare.py" ".scratch_bg3/thesis_pre.json" ".scratch_bg3/thesis_post.json"; echo "exit=$?"</invocation><expect>no served byte moved: `ay4 names 95 team_sheet_equals_stored15 95/95 others_equal 95/95`, `growth_exceeds_delta 0`, every name's growth 0 (bytes pre equal bytes post except a name whose input moved, printed), the max under 6,291,456 bytes; `ay4 compare build 1/1`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bg-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/15 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_minor_unit_census.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_casing_deployed.py"; echo "exit=$?"</invocation><expect>the no-regression arm: R89 PEERS DEPLOYED: YES, R89 DEPLOYED CLOSE: YES (METHOD /15 as before), R92 MINOR-UNIT CENSUS: YES, R95 CASING DEPLOYED: YES, with the function's CodeSha256 re-read, DIFFERENT from the one `AMGT-bg-1` left; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the recorded VersionIds (or the kept package's hash) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-bg-3.redeploy-the-scoped-api-carrying-the-one-s3-client-from-a-merged-pin.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the change-management entry's slug and state;
- every criterion's output lines;
- the post-act compare file path, with the changed-path count and the count outside the table;
- the duration, status and three re-invoke statuses of the FIRST overlay request of the post-apply replay for `ASML_NA_Equity` and `ADBE_US_Equity`, and of the same two requests after a quiet period of at least 15 minutes (no other read of the function in between), each against the 27 s margin of the pair;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's cell, split in two by the issuer: `AMGT-bg-2` the build, THIS order the apply. STAGED. THE GO WAITS ON ALL OF: (1) `AMGT-bg-1` APPLIED and its post-act read on record (the CTO: never folded); (2) `AMGT-bg-2` complete and MERGED, its candidate reviewed by the CTO (it deviates from "set the pool consistent": one client per container is the lever, the pool of 32 fits it); (3) THE PAIR, whose COO half is written from the pin's own handler against the live /15 function (the route tables and `r98_thesis_fullbody_compare.py` from the pin's worktree, `r100_pool_peak.py` and `r100_cold_check.py` on the pin), the CTO half signed; (4) the pin named in the GO with its `scoped_amgt.py` blob printed; (5) no concurrent reader during RA1's capture and replay. The CLOSE is a read the day after the apply (invocations over 20 s and pool warnings against 53 and 49), an issuer act in a later round.

<status>pending -- GO 2026-10-12T04:1xZ by the issuer (2.0.0_SA_COO~R1) to 0.7.0_AE_CloudOps~RA1. Pair: COO half @7d8d398673 (ledger/NEVER_WIDEN_ROUND100_S3CLIENT_REDEPLOY_COO_HALF.md), CTO half signed (CTO msg 4262, ledger/NEVER_WIDEN_ROUND100_S3CLIENT_REDEPLOY_CTO_HALF.md). BUILD PIN ba22af15f5, a box/dell1 first-parent commit (merged). GO conditions: (1) in a DETACHED worktree at ba22af15f5, `r94_admission_table.py ba22af15f5 --pin 6e8dcaf414` shows exactly ONE member, scoped_amgt.py 9b13bf0371d4 -> 9f72b58aa87e, and dossier.py 7b67bf62afdd, monthly_chatter.py 38e9511ccc9c and opal_naming.py 3902e0e93ee4 byte-equal to the live package (a second member, or any other blob, is a STOP); (2) the kept live package 7DUlZxhl.. downloaded and hash-checked before the apply, the 95-name thesis capture (`aw4_capture.py`) and the 527-request route baseline taken by RA1 IMMEDIATELY before it; (3) the bound is graded LIVE BEFORE vs LIVE AFTER (python3.11 both): NO served byte moves: any path outside the generation clocks that moves, any growth of any name, a status other than 200 for a name that read 200, or an invocation error is Branch 2 (STOP, rollback unless the CTO names KEEP); (4) the COLD-FIRST-REQUEST ARM: the first overlay request after the apply for ASML_NA_Equity and ADBE_US_Equity, and the same two after a quiet period of at least 15 minutes with no other read of the function, each 200 and under 27 s; a 27 s to under 29 s 200 with three identical re-invokes is recorded, a timeout or a differing re-invoke is Branch 2; (5) one replay request over 20 s: three re-invokes, 200, identical bytes; (6) NO other reader on the function during your capture and replay: the issuer and 2.0.0_SA_COO~C1 hold theirs until you report. Keep 7DUlZxhl.. for rollback; the issuer removes the pin worktree after the compare. The CLOSE (the day-after counts against 53 and 49) is the issuer's read in round 101.</status>
<round>100</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
