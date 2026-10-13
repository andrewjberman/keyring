# AMGT_RESAPP task order -- `AMGT-bj-1` -- THE OVERLAY'S FEED AND NEWS CARD READ ONLY THE SUBJECT'S ROWS OF `article_security_mention` (A BUILD, NOT YET SERVED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~404</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bj-1.the-overlay-feed-and-news-card-read-only-the-subjects-rows</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one module, no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the check reads the live pool with the worker's own session (S3 GETs and LISTs); no write, no function invoke.
comp-adversary: RUN at the cut, each arm against the literal string written below: r103_feed_equal_check.py with `--candidate-file` set to the BASE blob (`git cat-file blob 02627c18a0ea`) reads 'arms passed 15 of 16 ... R103 FEED EQUAL: NO' (R4b FAILS: the base holds the whole-snapshot cache entry), and on a throwaway candidate in a scratch worktree (the patch below, blob 84002d3fd559, +9 -2) 'arms passed 16 of 16 ... R103 FEED EQUAL: YES'; the boundary clause of AC2 prints nothing at the base.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-404` (branch `wk-AMGT_RESAPP-404`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-404`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bj-1` (round 103, decomposition s.111)

CTO~DELL1 round-102 analysis item 1 (msg 4958): the first overlay a container serves costs about 20 s, and 18.8 s of it is the `feed` phase; inside it the module's own `AMGT_SEGMENT
gold_article_security_mention=17951` is the whole `article_security_mention` table read (52,424 rows, 31 columns, decoded and turned into Python rows for ALL securities, then filtered by
`security_key` in Python). `_timeline_snapshot_rows(table, columns=..., security_key=...)` already reads ONE security's rows of ONLY the named columns (the timeline route uses it); the
overlay's two readers of this table do not. This cell makes both use it and moves NOT ONE served byte.

Apply the prepared edit, then verify it. The patch is the whole of the change (9 lines added, 2 changed, ONE file, `lib/research/api/scoped_amgt.py`, base blob `02627c18a0ea`):

    cd C:/dev/wk-resapp-404 && git apply --whitespace=nowarn "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/r103_candidate_source.patch"

What it does, so you can read it before you trust it: (a) adds `_OVERLAY_NEWS_COLUMNS`, one tuple of the eight columns the two readers use (`security_key`, `article_key`, `publisher`,
`mention_count`, `published_utc`, `title`, `url`, `published_precision`); (b) in `read_feed` and in `_overlay_top_band` the `_timeline_snapshot_rows("article_security_mention")` call becomes
`_timeline_snapshot_rows("article_security_mention", columns=_OVERLAY_NEWS_COLUMNS, security_key=<the subject>)` and the Python filter that follows stays. ONE tuple for both, so the snapshot is
fetched and decoded ONCE per container for the two readers. If `git apply` refuses, STOP and file a BLOCKING row: do not edit by hand.

Then run `python -m py_compile lib/research/api/scoped_amgt.py` and AC1. The check runs the BASE blob and your tree's handler in one process on the live pool (read only) for ASML_NA and
four drawn covered keys plus a negative control with no mention rows, and compares status and body bytes, the `feed` and `top_band` sections, and the module's snapshot cache.

Write NOTHING outside the file named in section 3.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W404-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. ONE product file, `lib/research/api/scoped_amgt.py`, changed by the prepared patch and nothing else. No test file, no module, no new file in `lib/`.
2. No deploy, no function invoke, no store write, no schedule, no S3 delete, ever. No Bloomberg, SEC or model call. No `pip install`.
3. Standing: no push of shared branches.
4. The check's reads are the worker's own session's; it prints no client, firm or account.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~404/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bj-1"><invocation>cd C:/dev/wk-resapp-404 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feed_equal_check.py" 2&gt;&amp;1 | grep -v "^AMGT_500" | grep -v "^WARN" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>`arms passed 16 of 16` then `R103 FEED EQUAL: YES`: for the five sampled subjects and the negative control the overlay's status and body byte-equal to the base, the `feed` and `top_band` sections byte-equal, the negative control's empty answer equal with item_count 0, the candidate holding no whole-snapshot cache entry and the column-scoped one, the phase lines kept; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bj-1"><invocation>cd C:/dev/wk-resapp-404 &amp;&amp; git diff --name-only "$(git merge-base HEAD box/dell1)" HEAD -- lib portal infra .tools integrations | sort</invocation><expect>exactly one line, `lib/research/api/scoped_amgt.py`, and no other line (the change is ONE file, committed)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~404 <0.9.0_WK_AMGT_RESAPP~404@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~404/AMGT_RESAPP.TO-AMGT-bj-1.the-overlay-feed-and-news-card-read-only-the-subjects-rows.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- criterion AC1's output lines and AC2's;
- the check's printed sample and its local feed timings (not graded);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-102 analysis section 2 item 1 (msg 4958): "THE FEED CELL (disarms W402-S1). The overlay's feed phase reads ONLY the requested security's rows of
`article_security_mention`, never the whole table: a key-scoped read the store already supports ... Under its own pair. Served overlay bytes are BYTE-EQUAL to the current recompute for a named
sample (ASML_NA plus 4 drawn keys), with a negative control ... Close: ONE driven first overlay on a fresh container ... The PRD addendum sets the target: feed phase at most 2 s, first overlay at
most 4 s." THE CELL IS A BUILD; the target is read at bj-2's driven request. **WHAT IS NOT KNOWN, and the order does not claim:** the key-scoped path still LISTs the prefix (24 objects) and GETs
the 8.4 MB object once per container; locally the whole path is list 0.23 s, GET 0.38 s, full decode 0.30 s, `to_pylist` 0.78 s against 0.01 s for the projected decode and 0.003 s for the key
column, but Lambda ran this phase about 12 times slower than the box. If the target is missed the key-scoped path's own `AMGT_SEGMENT gold_article_security_mention_{list,get,decode}` lines (printed
on the first read) split the remainder, and the next cell is the CTO's. STAGED successor: bj-2 (the apply and the request), after this cell's merge, the CTO's review and its pair.

<status>pending</status>
<round>103</round>
<slot>0.9.0_WK_AMGT_RESAPP~404</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
