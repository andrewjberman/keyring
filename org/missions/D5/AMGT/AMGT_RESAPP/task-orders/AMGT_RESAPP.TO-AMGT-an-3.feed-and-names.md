# AMGT_RESAPP task order -- `AMGT-an-3` -- FWD-38 a + b: THE RECENT-NEWS FEED HOLDS THE DAY VIEW'S ARTICLES; ONE DISPLAY NAME PER SECURITY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-an-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~212</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; every pool or table access is a read the function already makes.
comp-adversary: RUN by the issuer at the cut -- r64_served c12 FAILS at the base: feed 1/0/0 vs day view 71/13/3; display names disagree on 3 of 3.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r64-212` (branch `wk-AMGT_RESAPP-212`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r64-212`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-an-3` (round 64, decomposition s.72; FWD-38 a, b)

PRD FWD-38 (v0.34) clauses 1 and 2 (SAUX-12, SAUX-29). Issuer ruling R3, s.72.
1. **The overlay's `feed`** (`scoped_amgt.py` `read_feed` about :3963 -> `read_coverage_set` -> `pool_reader.coverage_items`) holds the
   newest HARVESTED articles across all publishers in its window, read from gold `article_security_mention` (the day view's own source,
   about :4792). Keep `feed.window` (30 days, ending today UTC unless `?as_of`), the order (newest first), and the item fields the page
   reads (`article_key`, `url` where gold has it, `title`/`headline`, `publisher`, `published_at`).
   - Base: BA's feed holds 1 item against 71 day-view articles in its window; AMD 0 against 13; VLO 0 against 3.
2. **ONE display name per security** on every route that serves one: overlay, ranking rows, collected/chatter rows and the peers
   subject.
   - Base disagreements: BA peers 'BOEING CO/THE'; AMD chatter 'ADVANCED MICRO DEVICES' and peers 'Advanced Micro Devices, Inc.'; VLO
     peers 'VALERO ENERGY CORP'.
   - The served name is the one `_with_display_name` (about :791) chooses. Route the other three through the same function.
   - The name is not all-caps and carries no share-class code (no 'Class A', ' A', 'ADR'), stripped by one rule.
3. Tests for both.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W212-S<k>`, `disarm_owner`
`2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/coverage/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-an-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-an-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c12 --where local; echo "exit=$?"</invocation><expect>C1 PASS for BA, AMD and VLO (every day-view article in the feed's window is in the feed); C2 PASS for all 3 (one display name, cased, no share-class code); R64 C12 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~212 <0.9.0_WK_AMGT_RESAPP~212@opal.agent>" -F <msgfile> -- <paths>` (message file written
with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~212/AMGT_RESAPP.TO-AMGT-an-3.feed-and-names.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PRD v0.34 FWD-38 clauses 1-2 (SAUX-12, 29). Served by an-7.

<status>pending</status>
<round>64</round>
<slot>0.9.0_WK_AMGT_RESAPP~212</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
