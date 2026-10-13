# AMGT_RESAPP task order -- `AMGT-bk-1` -- THE OVERLAY PRINTS SUB-PHASE LINES FOR FEED AND PEERS, AND ITS TOP BAND REUSES THE FEED'S ROWS (A BUILD; ONE FILE; NO SERVED BYTE MOVES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bk-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~414</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bk-1.the-overlay-prints-sub-phase-lines-and-its-top-band-reuses-the-feed-rows</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one source file; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the check invokes the existing function (GET) and reads S3 under the box's own role; no grant is changed.
comp-adversary: RUN at the cut -- `r104_candidate_check.py` reads `R104 CANDIDATE: YES (5 of 5 arms)` on the prepared candidate (blob 96642b55204d) and `NO (2 of 5 arms)` on the base blob 84002d3fd559 (S1, S2 and E2 FAIL: no sub-phase lines, and two LISTs of the mention table per overlay); arm E3 is the control: a top band handed ANOTHER subject's rows serves a different body, so the equality arm can see the fault it guards.
EGRESS CLASS, declared: NONE beyond the Lambda invoke (GET) and S3 reads; no Bloomberg call, no write.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-414` (branch `wk-AMGT_RESAPP-414`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-414`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bk-1` (round 104, decomposition s.113)

CTO round-103 analysis (`ledger/ROUND_ANALYSIS.round103.md`) item 1: the cold first overlay is 3,770 ms against 3,000. Of the overlay's phases, `feed` is 1,776 ms of which only 705 is its read, and `peers` is 1,001 ms; the remainder is unexplained. This cell makes it explicit and removes one repeated read, changing NO served byte.

The change is PREPARED and dry-run; apply it, do not rewrite it. It is ONE file, `lib/research/api/scoped_amgt.py` (base blob `84002d3fd559`):

    cd C:/dev/wk-resapp-414 && git apply --whitespace=nowarn "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104_prep/r104_candidate_source.patch"

What it does: (1) `_subphase_log` / `_subphase_call` print `AMGT_SUBPHASE route=overlay phase=<outer>.<step> ms=<n>` (a prefix `r102_phase_table.py` does not count, so its fourteen-phase check stays valid): `feed.imports`, `feed.snapshot`, `feed.items`, `feed.names` in `read_feed`, and `peers.read`, `peers.foreign`, `peers.subject_name`, `peers.subject_cap`, `peers.member_names`, `peers.reason_classes`, `peers.listed_identity`, `peers.numeric_tickers`, `peers.price_currency` in `read_peer_set` (the seven wrappers keep their original order, innermost first); (2) `read_feed` fills a `rows_sink` dict with the subject's rows as read, and `_overlay_top_band` takes those rows (copied) instead of reading the snapshot a second time. If `git apply` refuses, STOP and file a BLOCKING row: do not edit by hand.

Then run AC1 (it runs the checkout's own handler for six subjects and the LIVE function for the same two routes) and AC2. Report the AC1 table lines as printed.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. ONE file, `lib/research/api/scoped_amgt.py`, changed by the prepared patch and nothing else; its blob after the patch is `96642b55204d`.
2. Read-only against the world: GET invokes of the live function and S3 reads; no deploy, no store write, no Bloomberg call. No `pip install`. Standing: no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~414/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bk-1"><invocation>cd C:/dev/wk-resapp-414 &amp;&amp; PYTHONPATH="$(pwd)" timeout 590 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104_prep/checks/r104_candidate_check.py"; echo "exit=$?"</invocation><expect>the line `R104 CANDIDATE: YES (5 of 5 arms)` with PASS on S1, S2, E1, E2 and E3 (thirteen sub-phase lines once each; they sum to their phases; the overlay and peers bodies equal the live function's for six subjects; one LIST of the mention table per overlay); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bk-1"><invocation>cd C:/dev/wk-resapp-414 &amp;&amp; git diff --name-only "$(git merge-base HEAD box/dell1)" HEAD -- . ":(exclude)org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~414" ":(exclude)org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel" | sort; git hash-object lib/research/api/scoped_amgt.py | cut -c1-12</invocation><expect>exactly two lines: `lib/research/api/scoped_amgt.py` and then `96642b55204d`</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~414 <0.9.0_WK_AMGT_RESAPP~414@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~414/AMGT_RESAPP.TO-AMGT-bk-1.the-overlay-prints-sub-phase-lines-and-its-top-band-reuses-the-feed-rows.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- AC1's full output (the six per-subject lines, E3's line, the five arm lines and the verdict) and AC2's two lines;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** THE CTO'S ITEM 1: log lines that split feed's unexplained ~1,070 ms and peers' 1,001 ms, and `top_band` reusing the feed's slice (about -150 ms), code-only and byte-equal under a pair. The sub-phase lines are the cell's OUTPUT; whether the 3.0 s target is reached is not this cell's claim (the issuer's own projection last round was wrong by 0.77 s): bk-2's driven request reads it. Local cold timings the prepared candidate printed (not transferable to Lambda): feed.snapshot 946 ms, peers.numeric_tickers 895, peers.subject_cap 365, feed.imports 189 -- suspects only. `~R2` (workstream AIFILL, @0d02a44ab9) adds a region and a wiring line to the SAME file (`read_thesis_bundle`); the merge may need to be continued by the issuer, never rebased. ONE chain with bk-4 (the same file): bk-4 is cut after this merges.

<status>pending</status>
<status>complete -- 2026-10-13T22:5xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-414 @378e0c6ba5 (code 2e56fe821c) merged, proof instance VALID (rc=0). AC1 PASS by the worker and RE-RUN BY THE ISSUER on the worker's tree: `R104 CANDIDATE: YES (5 of 5 arms)` (thirteen sub-phase lines once each; they sum to their phases within 10 percent or 25 ms; the overlay and peers bodies equal the live function's for six subjects; one LIST of the mention table per overlay; the E3 control reads a different body for a wrong-subject top band). AC2 PASS: exactly `lib/research/api/scoped_amgt.py` and blob `96642b55204d`, equal to the prepared candidate. No row filed. WHAT IS NOT CLAIMED: that the 3.0 s target is reached; the sub-phase lines are the cell's output and bk-2's driven request reads them on Lambda.</status>
<round>104</round>
<slot>0.9.0_WK_AMGT_RESAPP~414</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
