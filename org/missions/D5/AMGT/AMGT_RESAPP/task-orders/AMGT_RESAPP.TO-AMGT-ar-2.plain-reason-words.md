# AMGT_RESAPP task order -- `AMGT-ar-2` -- PLAIN WORDS: /thesis AND /peers FOR A COVERED NAME WITH NO BLOCK, AND THE /ledger SOURCE REASONS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ar-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~224</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time reason text and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read or write; only served reason strings change.
comp-adversary: RUN by the issuer at the cut -- r68_served c28 FAILS at the base, local and deployed: DE /thesis 18 jargon reasons, DE /peers 3, /ledger on BA/AMD/VLO/NVDA 12 reasons with "estate", "stage" or "input ledger".
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r68-224` (branch `wk-AMGT_RESAPP-224`, cut from the issuance commit with `--portal-ref 6936e92b`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r68-224`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ar-2` (round 68, decomposition s.76; DSGN FWD-27, plain words)

A reader of these routes sees every `reason` string. Two surfaces still speak the system's internal vocabulary.

1. **A covered name with no model block** (DE_US_Equity today; the module is `lib/research/coverage/covered_no_block.py`, wired into
   `lib/research/api/scoped_amgt.py`). `/thesis` serves about 18 reasons such as "identity UNRESOLVED -- no measured security key ...",
   "no dossier read: security key UNRESOLVED", "no landed model block for this name", and an `identity.reason` naming the crosswalk.
   `/peers` serves 3, including the covered-no-block reason "... has no model block yet".
   - For a covered-no-block name, every served string whose key ends in `reason` on `/thesis` and `/peers` reads in plain words. The
     lead reason is: "<Company> (<TICKER>) is a covered name (<universe>, as of <date>), and its research pack is not in yet."
   - The words identity, unresolved, security key, crosswalk, dossier, landed and model block are banned there.
   - A name WITH a block, and an uncovered name (still 404), keep exactly what they serve today.
2. **`/ledger` source reasons** for every name. They say "registered in the estate", "no stage is registered" and "the input ledger
   holds no ... run". Reword them in plain words: no "estate", "stage" or "input ledger", and the same meaning (no source set up yet; no
   run recorded yet). Every class keeps a `source` or a non-empty `source_reason`.
3. **The plant test** `lib/research/api/tests/test_plain_reasons.py`. It covers:
   - a covered-no-block key's /thesis and /peers reasons carry none of the banned words, and the lead reason names the company;
   - a /ledger class with no source carries a plain `source_reason`;
   - a control: a name with a block keeps its /thesis reasons byte-identical.

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W224-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Reason TEXT only. No status code, key, figure or field name moves; the uncovered control still answers 404.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/coverage/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~224/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1200)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ar-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_plain_reasons.py; echo "exit=$?"</invocation><expect>every plant case passes (no banned word on a covered-no-block key's /thesis and /peers, the lead reason names the company, a plain /ledger source_reason, the with-block control unchanged); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ar-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round68/checks/r68_served.py" --cell c28 --where local; echo "exit=$?"</invocation><expect>C1, C2 and C3 PASS; R68 C28 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ar-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c25 c26; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py" --cell $c --where local || exit 1; done; echo "exit=$?"</invocation><expect>R67 C25 and C26 SERVED: YES (every class sourced or reasoned, the news run agrees, DE 200 on both routes, ZZZZ_US_Equity 404); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~224 <0.9.0_WK_AMGT_RESAPP~224@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~224/AMGT_RESAPP.TO-AMGT-ar-2.plain-reason-words.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the reason strings you changed, before and after;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-67 analysis @2db6fd3e3d ruling 3; CVO ADJUDICATION_v80 @69ce44def1 (DE /thesis FAIL on plain words). Served by ar-3.

<status>pending</status>
<round>68</round>
<slot>0.9.0_WK_AMGT_RESAPP~224</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
