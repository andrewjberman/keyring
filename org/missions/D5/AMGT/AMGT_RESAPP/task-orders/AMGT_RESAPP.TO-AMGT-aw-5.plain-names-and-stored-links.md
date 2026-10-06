# AMGT_RESAPP task order -- `AMGT-aw-5` -- PLAIN NAMES ON EVERY ROUTE (Z-W243-S2) AND THE STORED ARTICLE LINKS IN THE GOLD PRODUCER (Z-W233-S1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aw-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~249</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read; the gold producer already reads silver.
comp-adversary: RUN by the issuer at the cut -- r73 c50 FAILS on deployed: 131 of 383 served names are all capitals (rankings, chatter, overlay, freshness).
EGRESS CLASS, declared: NONE. No vendor, SEC, ft.com or wsj.com call; stored inputs only. The article links come ONLY from what the stored silver articles already carry: never fetch from ft.com, wsj.com or any publisher host (Andrew's FT hold).
</preflight>

**Your worktree:** `C:/tmp/r73-249` (branch `wk-AMGT_RESAPP-249`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r73-249`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aw-5` (round 73, decomposition s.81)

1. **Z-W243-S2, plain names.** Every route that serves a company name goes through `_clean_display_name`
   (`lib/research/api/scoped_amgt.py` ~`:899`): the rankings rows (`_with_display_name` ~`:1183`), the overlay subject
   (`_overlay_name` ~`:996-1006`), the chatter rows (`lib/research/api/monthly_chatter.py` ~`:106-118`) and the /freshness rows.
   "BOEING CO/THE" becomes "Boeing"; "BP PLC" becomes "BP".
2. **Z-W233-S1, stored links.** In `lib/research/harvest/publication_gold.py` (`article_url`, ~`:281-306`):
   - ft and wsj articles serve the top-level `url` their stored silver record carries (29 do), else null;
   - barrons falls back to `sourceUrl`, and sa to a top-level `url`.
   Plant tests extend `lib/research/harvest/test_mention_url.py`. **The gold REBUILD is AMGT_HARVST's**; do not write gold.
3. **Dry build, no write:** print per source the rows and rows with a url over the covered names, into
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~249/dry_build_urls.txt`.

`publication_gold.py` is shared with AMGT_HARVST: change only the url rules. Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W249-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. No served value other than a name's casing changes. NO gold write.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/harvest/publication_gold.py
lib/research/harvest/test_mention_url.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~249/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aw-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round73/checks/r73_served.py" --cell c50 --where local; echo "exit=$?"</invocation><expect>population names read above 300; C1 PASS failing 0; R73 C50 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aw-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/harvest/test_mention_url.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~249 <0.9.0_WK_AMGT_RESAPP~249@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~249/AMGT_RESAPP.TO-AMGT-aw-5.plain-names-and-stored-links.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api and harvest suites' last lines;
- the dry build per source;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-72 analysis item 4, ruling 6 (Z-W243-S2, Z-W233-S1). Z-W242-S1 is superseded for latency by aw-1 (s.81a). The gold rebuild is COO~H's act, asked at the drain.

<status>pending</status>
<round>73</round>
<slot>0.9.0_WK_AMGT_RESAPP~249</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~03:2xZ):** CLOSED -- drained @9d2b7b3d7c. On the shared tree, c50 local reads 383 names, 0 caps (from 131), YES. Link plant tests 13 passed. Dry build with url: ft 17/316, wsj 20/409 (stored only; no publisher fetch). proof VALID. Row Z-W249-S1 INERT. The gold rebuild is COO~H's (asked).

<status>complete</status>
