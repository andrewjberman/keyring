# AMGT_RESAPP task order -- `AMGT-qq-2` -- THE CANDIDATE UNIVERSE'S POOL HOME FOLLOWS THE SCANNER'S VINTAGE AND A REBUILD WRITES A NEW DATED KEY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-qq-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~382</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-qq-2.the-candidate-universe-home-follows-the-scanner-vintage</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a producer code change and its test, no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the check uses a fake S3 client; the module's own reads and writes are the ones it already makes (GET, LIST, put-if-absent to the prefix it already writes).
comp-adversary: RUN at the cut -- r92_universe_home.py FAILs H1, H2, H3b and H4 at the base and PASSes H3a and H5, and PASSes all six arms against a throwaway candidate (nothing written to the tree). Round 91's pp-3 stopped on exactly this: the refresh's one address is an existing object.
EGRESS CLASS, declared: NONE (no network in the check or the tests).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-382`, cut from the current branch head). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE CELL -- `AMGT-qq-2` (round 92, decomposition s.100)

CTO~DELL1 round-91 analysis item 3 (option C of round 91's pp-3 STOP). `lib/research/peers/universe.py` keeps the candidate universe at ONE
pool address built from a module constant: `CURRENT_VINTAGE = "2026-08-06"` -> `s3://opal-data-harvest/amgt/harvest/gold/
candidate_universe/date=2026-08-06/candidate_universe.json`. `refresh_candidate_universe` writes there (`crosswalk.write_pool`, which on a
hit with other bytes does an ETag-conditional OVERWRITE), `load_candidate_universe` reads there, and `cache_path` hashes that address into a
local mirror name. The scanner has moved to asOf 2026-10-02, so a refresh would put 2026-10-02 content under a 2026-08-06 key. Make the home
follow the scanner:

1. **The key is dated by the document.** `refresh_candidate_universe` writes to `date=<document["vintage"]>` (the builder
   `candidate_universe_address(vintage)` already takes a vintage; use the document's own `vintage`, never the constant). The local
   read-cache path is derived the same way.
2. **A refresh never overwrites.** Before the put, head the target key: absent -> put; present with the SAME bytes (the document's
   sha256 equals the stored `document-sha256` metadata) -> no second put, no error (idempotent); present with OTHER bytes -> raise, write
   nothing. Do not change `crosswalk.write_pool`; the check is in `universe.py`. The payload must be deterministic for an identical
   rebuild: keep machine-local fields (`cache_path`) out of the pooled payload, or the idempotence arm cannot hold across machines.
3. **The loader reads the LATEST dated key.** `load_candidate_universe`, with no explicit path and no `AMGT_PEER_UNIVERSE_CACHE`, lists
   `amgt/harvest/gold/candidate_universe/` for `date=<YYYY-MM-DD>/candidate_universe.json` keys and materialises the newest; with only
   `date=2026-08-06` present it reads that (today's behaviour). A failed listing falls back to the constant, as a pool miss does today
   (an in-memory rebuild). `CURRENT_VINTAGE` stays as that fallback only.
4. Everything else is unchanged: `ENV_CACHE` stays a local override that skips every pool read and write; `build_candidate_universe`
   and every other module are untouched; the local mirror is never the source of truth.

Add the test file `lib/research/peers/tests/test_universe_home.py` (pure, no network, no AWS; a small fake S3 client): one test per rule
above, including an explicit one that the `ENV_CACHE` path performs no pool call.

ASCII only. Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W382-S<k>`,
`disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write (the check and the tests use a fake client), no schedule, no SEC, vendor, model
   or Bloomberg call. Do NOT run `--refresh` against the real bucket.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. Do not touch `lib/research/identity/crosswalk.py`, `engine.py` or any served reader.

## 3. SURFACES

<paths>
lib/research/peers/universe.py
lib/research/peers/tests/test_universe_home.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~382/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-qq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_universe_home.py"; echo "exit=$?"</invocation><expect>PASS H1 (the refresh lands at a new key dated by the document's own vintage), PASS H2 (date=2026-08-06 byte-equal), PASS H3a (idempotent), PASS H3b (a different document at the same vintage is refused), PASS H4 (the loader returns the latest dated key), PASS H5 (control: only the old key present returns it); R92 UNIVERSE HOME: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-qq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/peers/tests/test_universe_home.py lib/research/peers/tests -q; echo "exit=$?"</invocation><expect>the new test file and every existing test under lib/research/peers/tests pass with 0 failed, and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~382 <0.9.0_WK_AMGT_RESAPP~382@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~382/AMGT_RESAPP.TO-AMGT-qq-2.the-candidate-universe-home-follows-the-scanner-vintage.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of `universe.py`, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-91 analysis @f6eb45c478 item 3; CTO half of round 91's pp-3 pair ADDENDUM 2 @da6c6ec44e ("C is round 92 cell 1": here it is the third, behind the currency cell). Producer-side: no function change, no store write by this cell; a rebuild that USES it (the next `--refresh`, a store write with its own pair) is not cut here. The cache the round-91 act used (sha256 2738e9b673a41c97...) is archived beside RA1's entry; until this merges any `engine --write-pool` sets the same cache or does not run. Checks dry-run at the base: AC1 FAIL (H1, H2, H3b, H4; H3a and H5 PASS); AC2 FAIL (the new test file is absent).

<status>pending</status>
<round>92</round>
<slot>0.9.0_WK_AMGT_RESAPP~382</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
