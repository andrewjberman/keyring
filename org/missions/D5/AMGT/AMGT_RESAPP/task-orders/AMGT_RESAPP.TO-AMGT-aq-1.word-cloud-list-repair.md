# AMGT_RESAPP task order -- `AMGT-aq-1` -- FWD-39 LIST REPAIR: NO CLOUD CARRIES ITS OWN TICKER OR NAME WORD; THE MEASURED BOILERPLATE GOES; AN INVERTED WINDOW SERVES ITS REASON

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aq-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~219</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; the range route already reads the gold headlines it counts.
comp-adversary: RUN by the issuer at the cut -- r67_served c23 FAILS at the base, local and deployed (see the issuance commit for the offender counts over all 95 payloads).
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r67-219` (branch `wk-AMGT_RESAPP-219`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r67-219`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aq-1` (round 67, decomposition s.75; PRD v0.37 FWD-39)

FWD-39 DONE WHEN: the security's top terms are counted after a DECLARED stop-word list and the company's own name words.
3.0.0_SA_CVO~Z graded it NOT PASS (ADJUDICATION_v79): 12 of 70 non-empty clouds carry the company's own ticker (AMD's #2 term is
'amd'; also UNH, ADBE, SPOT, TSM, NKE), and headline boilerplate the 158-word list misses survives ('among' in 31 clouds, 'top' 24,
'quant' 15, 'focus' 11, 'big' 11, 'notable', 'higher').

1. **The exclusion** (`scoped_amgt._word_cloud_block` / `_word_cloud_tokens`): besides the stop list, drop
   - the security's ticker root (the first token of its Bloomberg ticker, lowercased, e.g. 'amd' for 'AMD US');
   - every word of its served short name (`display_name`);
   - every word of its served long name (the overlay's `name`).
2. **The stop list:** extend `WORD_CLOUD_STOP_WORDS` with the measured boilerplate, at least: among, top, quant, focus, big, notable,
   higher. `WORD_CLOUD_STOP_WORDS_SOURCE` says it now carries the CVO's measured headline boilerplate (ADJUDICATION_v79).
3. **The inverted window:** when the window's clamped `from` is later than its `to` (for example BA 2025-06-01..2025-06-30, before
   the store floor), `word_cloud` serves `terms: []` with a reason and does NOT print the inverted `from`/`to` pair (serve `window`
   as null, or a window that is not inverted).
4. **The plant test** `lib/research/api/tests/test_word_cloud_repair.py`:
   - a planted headline set carrying the ticker, short-name words, long-name words and each boilerplate word serves none of them;
   - an inverted window serves its reason with no inverted pair;
   - the plant also carries long-name (overlay `name`) words, since c23 grades the ticker root and the short name over the live
     payloads and the long name is graded here;
   - it FAILS with your fix removed. Show that in your report (the mutant run's failing count, then the restore).
5. Singular and plural stay apart (the CTO did not cut a stemmer).

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W219-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Every existing timeline field keeps its value; only the cloud's terms and the inverted window's block change.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~219/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_word_cloud_repair.py; echo "exit=$?"</invocation><expect>every plant case passes (no ticker, short-name, long-name or boilerplate word served; inverted window with its reason and no inverted pair); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py --cell c23 --where local; echo "exit=$?"</invocation><expect>C1 PASS (0 clouds carry their own ticker root or a served short-name word, over every name on both the default range and 2026-09-01..today); C2 PASS (0 clouds carry an extended-list word); C3 PASS; R67 C23 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-aq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round66/checks/r66_served.py --cell c18 --where local; echo "exit=$?"</invocation><expect>R66 C18 SERVED: YES (the cloud still serves counted, ordered terms on BA, AMD and VLO); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~219 <0.9.0_WK_AMGT_RESAPP~219@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~219/AMGT_RESAPP.TO-AMGT-aq-1.word-cloud-list-repair.proof_of_spec.json`.
Report once:
- the commit hash
- every criterion's output lines
- the api suite's last line
- the functions you changed
- the mutant control (failing count with the fix removed)
- the stop list's new size
- any row

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-66 analysis @d76db3486c rulings 1 and 2; CVO~Z ADJUDICATION_v79. Served by aq-5.

<status>pending</status>
<round>67</round>
<slot>0.9.0_WK_AMGT_RESAPP~219</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-04 ~19:5xZ, drain re-entered after the site-Z crash):** CLOSED.
- Worker ~219 code `52898635f9`, instance `2c38b011ad`, proof-of-spec-check VALID (rc=0). The final report was lost with
  the pre-crash session; the instance is the oracle.
- AC1 PASS 18 of 18 plant cases; the mutant (fix removed) fails 13 of 18. AC2 PASS c23 local: 190 payloads, 128 non-empty,
  0 offenders on C1 and C2. AC3 PASS (BA, AMD, VLO). Stop list 158 -> 165.
- Served by aq-5.

<status>complete</status>
