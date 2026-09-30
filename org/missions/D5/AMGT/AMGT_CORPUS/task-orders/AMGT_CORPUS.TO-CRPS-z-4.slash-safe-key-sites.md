# AMGT_CORPUS task order -- `CRPS-z-4` -- ROUND 24: finish C-SLASH-SAFE-KEY in code -- every per-security path through `slash_safe_key`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-z-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~4</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code only; the 30-object move and the API deploy are round 25, under a pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~4`**, slot `~4` of round 24. Serves **every name whose identity carries a `/` (BP/_LN,
NG/_LN, BRK/B)**, row `Z-S64`.

## 1. THE CELL -- `CRPS-z-4`

**Where this came from.** A security's identity key keeps its slash: `lib/research/identity/crosswalk.py` roots the key
verbatim, so `BP/_LN_Equity` and `BRK/B_US_Equity`. When that raw key is interpolated into an S3 or local PATH, the `/` splits the
path:
- `derived/model_block/BP/_LN_Equity/...`;
- on disk, `model_block_BP/_LN_Equity.json` writes into a directory `model_block_BP`.

`crosswalk.slash_safe_key(security_key)` is the reversible encoder: `/` becomes `-SLASH-`, giving `BP-SLASH-_LN_Equity`. It is
identity on slash-free keys. `lib/opal_naming.py` already refuses a raw slash in a key segment.

The CTO ruled option (c): finish C-SLASH-SAFE-KEY. Every PATH is built through `slash_safe_key`, and the identity keeps its slash.
The 30 live raw-slash objects move in round 25, together with the scoped-API deploy, so no reader serves between the two forms.
**This cell is code only.**

The issuer's census at the cut (`checks/round24/z4_check.py`) finds 24 path-building functions with no reference to
`slash_safe_key`, in:
- `lib/research/api/scoped_amgt.py` (`resolve_identity`, and the pool reads);
- `lib/research/drafting/run_drafting.py`, `lib/research/filings/analyze.py` and `lib/research/filings/drafting_build.py`;
- `lib/research/freshness/build_view.py`, `lib/research/identity/crosswalk.py` (`_record_for`) and `lib/research/ledger/ledger.py`;
- `lib/research/management/enrich.py` (4), `lib/research/peers/engine.py` (4) and `lib/research/posture/judge.py`;
- `lib/research/posture/packs.py` (2), `lib/research/scores/run_scores.py` and `lib/research/social/collect.py`;
- `integrations/bloomberg/research/derive_fye_fixed.py` and `integrations/bloomberg/research/model_block_pull.py` (`stage_derive`,
  `_model_block_keys_in_store`);
- `integrations/bloomberg/research/pull_consumer.py`.

**RULED -- what you build:**
1. At every per-security PATH site, WRITERS and READERS alike, build the path segment with `crosswalk.slash_safe_key(<key>)`. The
   identity value stored INSIDE documents keeps its slash. A function that matches the census but builds no per-security path (e.g.
   a prefix listing, or a docstring-like constant) carries the one-line marker comment `# slash-safe: not a per-security path
   (<reason>)` inside its body. That marker is reviewed at the drain, so use it only where true.
2. A reader that must find BOTH forms during the move window (for example `_model_block_keys_in_store` mapping store keys back to
   identities) decodes with the crosswalk's inverse, if one exists, or states why it does not.
3. `lib/research/identity/tests/test_slash_safe_key_sites.py` (new): for `BP/_LN_Equity` AND `BRK/B_US_Equity`, build the path at
   EACH routed writer and reader site you changed (import the function; stub I/O, no network). Assert the path carries the encoded
   form and no raw `/` inside the key segment. Also assert a slash-free key's path is byte-unchanged (the control).
4. `deliverables/0.9.0_WK_AMGT_CORPUS~4/SLASH_SAFE_SITES_ROUND24.md`: every site changed or marked, its file, and its CONSUMER
   (who reads what it writes). Name the AMGT_RESAPP files among them, for its round-25 deploy.
5. No S3 read or write, no object move, no deploy.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/drafting/run_drafting.py
lib/research/filings/analyze.py
lib/research/filings/drafting_build.py
lib/research/freshness/build_view.py
lib/research/identity/crosswalk.py
lib/research/ledger/ledger.py
lib/research/management/enrich.py
lib/research/peers/engine.py
lib/research/posture/judge.py
lib/research/posture/packs.py
lib/research/scores/run_scores.py
lib/research/social/collect.py
integrations/bloomberg/research/derive_fye_fixed.py
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/pull_consumer.py
lib/research/identity/tests/test_slash_safe_key_sites.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/SLASH_SAFE_SITES_ROUND24.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-z-4.slash-safe-key-sites.md
</paths>

- READ-ONLY: every other file, every S3 object.
- In `model_block_pull.py` change ONLY the path-building sites; the unit and sign readers are other cells' past work.
- In `crosswalk.py` do NOT change `slash_safe_key` or the identity rule.
- Scratch `.scratch/z4/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`). Never disable the sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO deploy.
- A changed site must still build a byte-identical path for every slash-free key: the 98 live names are all slash-free except the
  two.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W4-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-z-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round24/z4_AC1.sh</invocation><expect>(?m)^z4 sites [1-9]\d* encoded [1-9]\d* raw 0 bp_encoded BP-SLASH-_LN_Equity brk_encoded BRK-SLASH-B_US_Equity roundtrip True planted_refuses True$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-z-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round24/z4_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the issuer's static census reads 0 raw path-building functions (base: 24); the encoder round-trips BP and BRK; a planted
  raw-slash segment still refuses.
- AC2: your per-site tests for BP/_LN and BRK/B, with the slash-free control, plus the encoder's suite.
- The repo-wide suites you touched stay green: the issuer runs them at the drain.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/AMGT_CORPUS.TO-CRPS-z-4.slash-safe-key-sites.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line, the sites routed and the sites marked (with reasons), and the consumer list.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-23 analysis addendum (ruling 2, option c) @`c9081e03d6` on `4.0.0_SA_CRO~Z`'s research @`c5ebbb2356`.
Dry-run at base CLOUD `da4fb630b5`:
- z4_AC1 FAIL as expected: `z4 sites 24 encoded 0 raw 24 bp_encoded BP-SLASH-_LN_Equity brk_encoded BRK-SLASH-B_US_Equity
  roundtrip True planted_refuses True` (the controls PASS).
- z4_AC2 FAIL as expected (no tests ran).

The census is stricter than the research's "~10": it found 24, including the model-block producer (`derived/{ENGINE}/{sec_key}`),
which the research named.
<risk>LOCAL</risk>
<status>pending</status>
<round>24</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<status>complete</status>
