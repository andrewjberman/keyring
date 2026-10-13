# AMGT_RESAPP task order -- `AMGT-bj-8` -- THE PER-SECURITY PULL CENSUS: WHICH PULLS EACH NAME MAKES AND THE TIME EACH TAKES (FWD-40 (c); AN INSTRUMENT RUN)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bj-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~409</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bj-8.the-per-security-pull-census-names-the-pulls-each-name-makes</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot read run; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the instrument reads S3 and DynamoDB in-process with the box's own role and invokes the existing function with GET events; no grant is changed.
comp-adversary: RUN at the cut -- `r103_pull_census.py --selftest` reads `arms passed 4 of 4 ... R103 PULL CENSUS ARMS: YES` (a prefix per class, an unknown prefix is `other` and never folded, calls attributed to the phase line printed at or after them, a log tail parses to phases/handler/Init); one real name (ASML_NA_Equity) ran 134 calls over six routes: corpus 48, scanner 43 (20 per-peer refdata LISTs and GETs), price 16, news 7, filings 5, posture 4, peers 4, management 2, scores 2, drafting 1, coverage 1, other 1.
EGRESS CLASS, declared: NONE beyond S3/DynamoDB reads and the Lambda invoke (GET); no Bloomberg call, no write.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-409` (branch `wk-AMGT_RESAPP-409`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-409`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bj-8` (round 103, decomposition s.112)

FWD-40 (c) of PRD v0.44 (ratified text, inlined):

```
(c) a per-security pull census: for each name, which pulls
                    it makes (corpus, filings, management, news, price,
                    scanner) and the time each takes;
```

The page makes six route calls per name. The instrument is PREPARED and dry-run; you run it, you do not edit it. It runs the checkout's own handler in-process on the live pool with every botocore call RECORDED (service, operation, bucket and key or prefix, table, local milliseconds, bytes) and attributed to the overlay phase that was running, and CLASSES each call into corpus, filings, management, news, price, scanner (the six FWD-40 (c) names) plus posture, peers, scores, drafting and coverage (pulls the page also makes), with anything else printed as `other`. Local milliseconds do NOT transfer to Lambda: the second arm drives ONE overlay per name on the live function and prints its per-phase milliseconds from the request's own log tail.

1. AC1 (offline self-test). 2. AC2: the driver script runs the census over every resolved name in four parallel shards and merges (about 8 to 10 minutes; use a tool timeout of 600000 ms). 3. AC3: the deployed arm over the same names, from the merged file (about 3 to 5 minutes; it is a reader of the function, which is why this order is staged behind the redeploy).

Then report, from `pull_census.txt` and the AC3 output, without judging: the PULLS table in full; the UNCLASSED line; the LAMBDA OVERLAY table in full (median, p95, max per phase and for the handler); the names at or above 3,000 ms handler and whether each was a cold container start.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W409-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Run ONLY the three invocations below and the instruments as written; do not edit any instrument.
2. Read-only against the world: no write to S3, DynamoDB or the function; AC3 drives ONE overlay per name, sequentially, once.
3. Your files: your deliverables folder only. No push of shared branches. No `pip install`.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~409/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1500)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bj-8"><invocation>cd C:/dev/wk-resapp-409 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_pull_census.py" --selftest | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>`arms passed 4 of 4`, `R103 PULL CENSUS ARMS: YES`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bj-8"><invocation>cd C:/dev/wk-resapp-409 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_pull_census_run.sh" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~409/run"; echo "exit=$?"</invocation><expect>the last line `R103 PULL CENSUS: RAN N of N names, C calls, U unclassed` with both N equal (the resolved names, 95 at the cut); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bj-8"><invocation>cd C:/dev/wk-resapp-409 &amp;&amp; PYTHONPATH="$(pwd)" timeout 590 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_pull_census.py" --from-file "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~409/run/pull_census.json" --deployed-phases | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 PULL CENSUS DEPLOYED: RAN N of N names` with both N equal; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~409 <0.9.0_WK_AMGT_RESAPP~409@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~409/AMGT_RESAPP.TO-AMGT-bj-8.the-per-security-pull-census-names-the-pulls-each-name-makes.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- the three criteria's output lines;
- from the output files: the PULLS table, the UNCLASSED line, the LAMBDA OVERLAY table and the over-3,000 ms line, verbatim;
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** FWD-40 (c) is Andrew's added ask ('worth exploring the individual security pulls'). The census REPORTS what each name pulls and what each takes; it grades nothing. Local call times are an attribution aid (WHAT is pulled, how often, how many bytes); Lambda per-phase time is the time. STAGED behind `AMGT-bj-2` because AC3 invokes the function: the issuer flips it pending when bj-2 completes. The first request of AC3 may start a cold container; the instrument prints cold starts (Init) by name.

<status>staged</status>
<round>103</round>
<workstream>V1</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~409</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
