# AMGT_RESAPP task order -- `AMGT-ap-1` -- FWD-39: THE TIMELINE ROUTE SERVES THE SECURITY'S WORD CLOUD FROM ITS OWN COVERAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ap-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~217</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read or write; the route already reads gold article_security_mention.
comp-adversary: RUN by the issuer at the cut -- r66_served c18 FAILS at the base, local and deployed: 0 terms on BA, AMD and VLO; no word_cloud on an empty window; 0 declared stop words.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r66-217` (branch `wk-AMGT_RESAPP-217`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r66-217`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ap-1` (round 66, decomposition s.74; PRD v0.37 FWD-39)

FWD-39 DONE WHEN: on 3 covered names, the timeline payload carries `word_cloud`. It holds the security's top terms (at most 40) with
their counts, counted over the headlines of its own gold mention rows in the timeline's window. A DECLARED stop-word list (printed
with its source) and the company's own name words are removed first. A name with no headlines in the window serves an empty list
with a plain reason. The terms are counted at request time from gold already served: no new table, no schedule, no data operation.

1. **Where:** the range route `/security/{security_key}/timeline` (`scoped_amgt.py` about :5291 calls
   `timeline_api.get_timeline`). Add `word_cloud` to that payload only. The day and event routes do not change.
2. **The shape (the contract the page reads):**
   ```
   word_cloud: {"terms": [{"term": <str>, "count": <int>}],
                "window": {"from": <ISO>, "to": <ISO>},
                "reason": <str or null>}
   ```
   - `terms` is ordered by count descending, then term ascending, and holds at most `WORD_CLOUD_MAX_TERMS`.
   - `window` is the timeline's own served window (its clamped `from` and resolved `to`).
   - `reason` is null when `terms` is non-empty, and a plain sentence when it is empty (for example "no coverage headlines in
     this window").
3. **The count:**
   - Read the headline (`title`) of every gold `article_security_mention` row for this security whose published UTC day falls in
     the window. Use the seam the route already uses (`_timeline_snapshot_rows` / `publication_gold._latest_gold_snapshot_rows_cached`
     with `columns=` and `security_key=`, as AMGT-an-5 does), so the cold read stays cheap.
   - Split each headline into lowercase word tokens. Drop: tokens shorter than 3 characters, pure numbers, every word in
     `WORD_CLOUD_STOP_WORDS`, and every word of the company's served `display_name` (`_display_name_for(security_key)`).
   - `count` is the number of headlines carrying the term; a term repeated inside one headline counts once.
4. **Declare in `scoped_amgt`** (the check reads these names exactly):
   - `WORD_CLOUD_STOP_WORDS`: a frozenset of lowercase words.
   - `WORD_CLOUD_STOP_WORDS_SOURCE`: a one-line string naming where the list comes from.
   - `WORD_CLOUD_MAX_TERMS = 40`.
   - No new dependency. The package is at 96.8% of its ceiling.
5. **The plant test** `lib/research/api/tests/test_word_cloud.py`. It plants a headline set with a known answer and declares the
   exact served `terms`. Through the seam the route uses, it shows:
   - (i) the declared top terms with their counts;
   - (ii) no stop word and no company-name word is served;
   - (iii) more than 40 distinct terms are cut to 40;
   - (iv) an empty window serves `terms: []` with a reason.
6. **The cold read:** time the range route for BA 2026-09-01..today before and after your change (the route's AMGT_SEGMENT lines),
   and report both. A redeploy grades the deployed cold read against a 5 s bound.

Run `lib/research/api/tests/` before your commit and report its last line. In your worktree, after your commit, run
`bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only /c/tmp/r66-pkg-217.zip` and report its `SIZE:` line.
A build past the ceiling is a STOP: report it and do not trim to fit.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W217-S<k>`, `disarm_owner`
`2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Every existing field of the timeline payload keeps its value.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/harvest/timeline_api.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~217/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ap-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_word_cloud.py; echo "exit=$?"</invocation><expect>every plant case passes (declared top terms and counts; no stop word or company-name word; cut to 40; empty window with a reason); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ap-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round66/checks/r66_served.py --cell c18 --where local; echo "exit=$?"</invocation><expect>declared stop words over 0 with a source; C1 PASS for BA, AMD and VLO; C2 PASS (empty window, empty list, a reason); R66 C18 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ap-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c11 --where local; echo "exit=$?"</invocation><expect>R64 C11 SERVED: YES (the timeline's markers unchanged); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~217 <0.9.0_WK_AMGT_RESAPP~217@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~217/AMGT_RESAPP.TO-AMGT-ap-1.word-cloud-producer.proof_of_spec.json`.
Report once:
- the commit hash
- every criterion's output lines
- the api suite's last line
- the cold-read timings before and after
- the SIZE line
- the functions you changed
- the stop list's size and source
- any row

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-65 analysis @2de1ef2251 ruling 3; Andrew ~20:3xZ card 5 ("yes", record @9fe6e6f111). JUDGMENT at L9: CVO~Z
reads the served terms as a reader would. Served by the round's redeploy.

<status>pending</status>
<round>66</round>
<slot>0.9.0_WK_AMGT_RESAPP~217</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
