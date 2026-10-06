# AMGT_RESAPP task order -- `AMGT-az-2` -- THE TOP-OF-PAGE BAND'S SERVED DATA (FWD-16, NEWS HALF) AND EACH INPUT'S PROVENANCE (FWD-12), ON /overlay

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-az-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~263</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- the same gold mentions, description, snapshot and ledgers the function already reads.
comp-adversary: RUN by the issuer at the cut -- r76 c62 and c63 FAIL on deployed D29LJCXh: /overlay serves neither `top_band` nor `input_provenance` for any of the 95 covered names.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r76-263` (branch `wk-AMGT_RESAPP-263`, cut from the issuance commit with `--portal-ref cf3f10c6`, the portal DEV head at the cut (the api suite reads a portal fixture)). Work and commit only there. Start every shell call with `cd /c/tmp/r76-263`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-az-2` (round 76, decomposition s.84)

CTO rulings 2 and 3 (round-75 analysis @326aea63b3). Add two fields to the /overlay body (`lib/research/api/scoped_amgt.py`);
the page work is DSGN round 45's.
1. **`top_band`** (FWD-16, the news half):
   - `description_line`: the company in ONE line (no newline, 300 characters or fewer), from the description the page already
     serves. If none, use `description_reason` in plain words.
   - `items`: the latest trading day's news items for the name, from the served gold mentions (each carries its `url` since HARVST
     rebuild #7). Each item has `title`, `url`, `publisher`, `published_utc` and `mentions`, ordered most-discussed first, then
     newest. Cap the list at 10. If there are none that day, serve `items: []` and a plain `items_reason`.
   - `social`: exactly `"no social source is admitted yet"`. Never an empty box.
2. **`input_provenance`** (FWD-12, the provenance half): one entry per /freshness input (`VENDOR_INPUTS` plus "pack"). Each entry has
   `input`, `source` (where the input comes from, in plain words), `last_run` (the SAME value the /freshness row serves for that name
   and input; read the snapshot, never recompute) and `outcome` (`landed` / `never read` / `failed`, with a plain `reason`).
3. **Plant tests** in `lib/research/api/tests/test_top_band_provenance.py`.

No re-run button or write path (FWD-12's re-run half is a design fork at the CRO). No vendor call.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W263-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. No existing /overlay field changes value; only the two added fields.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/top_band.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~263/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-az-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/checks/r76_served.py" --cell c62 --where local; echo "exit=$?"</invocation><expect>all 95 names serve top_band with a one-line description or reason, followable items most-discussed then newest, and the social line; C1-C3 PASS; R76 C62 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-az-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/checks/r76_served.py" --cell c63 --where local; echo "exit=$?"</invocation><expect>all 95 names serve input_provenance agreeing with /freshness on every input; C1 PASS; R76 C63 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-az-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_top_band_provenance.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~263 <0.9.0_WK_AMGT_RESAPP~263@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~263/AMGT_RESAPP.TO-AMGT-az-2.top-band-and-input-provenance.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- items served in total and names with none today;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-75 analysis items 1-2, rulings 2-3. Served by az-5. DSGN round 45 draws the band and the panel from these fields.

<status>pending</status>
<status>complete -- drained @1ef4cd99de; proof VALID (worktree checker); c62/c63 95/95; 23 plant cases; api suite 726 passed in the worktree</status>
<round>76</round>
<slot>0.9.0_WK_AMGT_RESAPP~263</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
