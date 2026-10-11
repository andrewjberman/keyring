# AMGT_RESAPP task order -- `AMGT-ss-3` -- A CANDIDATE ROW THAT IS THE SUBJECT'S OWN COMPANY, BY HELD IDENTITY, IS EXCLUDED AT THE RANKER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ss-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~386</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ss-3.a-candidate-that-is-the-subject-by-held-identity-is-excluded</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a ranker change and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the check uses fixture rows; the batch's own reads are the ones it already makes.
comp-adversary: RUN at the cut -- r93_self_peer.py reads 1 of 7 at the base (only the no-index control PASSes: the keyword does not exist) and 7 of 7 against a throwaway candidate. Measured 2026-10-11 over the 243 subjects: 10 list their own company among their peers (BZLFY, NOVN, ORA, PBR, ROG, SAN, ST, TSM, UBSG, ZURN); the model block's name ('ROCHE HOLDING AG-GENUSSCHEIN') and the scanner's ('Roche Holding Ltd') differ, so the engine's exact-name and share-class arms miss it.
EGRESS CLASS, declared: NONE (no network in the check or the tests).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-386` (branch `wk-AMGT_RESAPP-386`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-386` (or the portal path named below); a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-ss-3` (round 93, decomposition s.101)

CTO~DELL1 round-92 analysis item 3 (row D1-S21). `lib/research/peers/engine.py::peers` excludes a candidate row as the subject itself when its
ticker is the key's root or the subject's scanner ticker, when its name normalises EXACTLY to the subject's, or when it is the subject's other
share class. It misses the same company under a different name string. The rule to add is BY IDENTITY, the way the serve path already names a
member's company:

1. `peers(...)` gains two keyword parameters, `held_name_index: Optional[dict] = None` (`{name token: [security keys]}`, the index
   `scoped_amgt._held_name_index()` builds) and `clean_name: Optional[callable] = None` (`scoped_amgt._clean_display_name`; identity when None).
   In the grading loop, after the three existing arms and only when `held_name_index` is truthy: a row whose
   `numeric_tickers.name_token(clean_name(row["name"]))` is non-empty and maps in the index to EXACTLY ONE key, that key equal to the subject's
   `security_key`, is the subject's own company: it is excluded (never graded, never a member), counted in `self_excluded`, and listed as
   `{"ticker", "name"}` under a new `denominators["self_excluded_by_identity"]`. The subject's own scanner row is already excluded by ticker;
   do not let this arm remove the row `resolve_subject` joined for the subject. A token that names two keys, or another key, excludes nothing.
   Append one sentence about the new arm to `denominators["self_exclusion_rule"]`. The ranked set backfills from the next candidate as it
   does for the existing arms. With no index (the default) every result is byte-equal to today (the `vintage` timestamp aside).
2. The peers package never imports the api package (the guard test `test_peers_does_not_import_api` forbids the literal), so the index comes
   from a caller ABOVE it. `engine.run_batch(...)` and `engine.main(argv=None, held_name_index=None, clean_name=None)` take the two keywords and
   pass them to every `peers(...)` call (the single-subject path included); engine.py imports nothing from `lib.research.api`. A NEW file
   `lib/research/api/peers_rebuild.py` is the sanctioned rebuild entry: `main(argv=None)` builds the index ONCE
   (`from lib.research.api import scoped_amgt`: `index = scoped_amgt._held_name_index()`, `clean = scoped_amgt._clean_display_name`) and
   returns `engine.main(argv, held_name_index=index, clean_name=clean)`; when the index build raises it raises
   `ValueError("REFUSED: ...")` and calls nothing (a rebuild that silently ran without the rule would put the self peers back). It carries a
   `if __name__ == "__main__": raise SystemExit(main())` so `python -m lib.research.api.peers_rebuild --as-of ... --write-pool` is the command.
   The batch run through `python -m lib.research.peers.engine` is unchanged (no index, no rule).

Add `lib/research/peers/tests/test_self_peer_identity.py` (pure, no network): one test per arm E1-E6 of `r93_self_peer.py`, and `lib/research/api/tests/test_peers_rebuild.py` (pure) for arm E8.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W386-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call. Do NOT run the batch or `--write-pool`.
2. No `bun`, `npm` or `pip install`. Nothing is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit `engine.py` minimally: do not reformat it, and do not touch `universe.py`, `numeric_tickers.py`, `price_currency.py`, `scoped_amgt.py`, the guard test or any served reader. `engine.py` must not import `lib.research.api`, even inside a function.

## 3. SURFACES

<paths>
lib/research/peers/engine.py
lib/research/peers/tests/test_self_peer_identity.py
lib/research/api/peers_rebuild.py
lib/research/api/tests/test_peers_rebuild.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~386/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ss-3"><invocation>cd C:/dev/wk-resapp-386 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round93_prep/checks/r93_self_peer.py"; echo "exit=$?"</invocation><expect>PASS E1 (the self row is excluded, named and counted), PASS E2, PASS E3, PASS E4, PASS E5 (the set backfills to 12), PASS E6, PASS E7, PASS E8; arms passed 8 of 8; R93 SELF PEER: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ss-3"><invocation>cd C:/dev/wk-resapp-386 &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/peers/tests lib/research/api/tests/test_peer_price_currency.py lib/research/api/tests/test_peers_rebuild.py -q; echo "exit=$?"</invocation><expect>the control: the new test file and every existing test under lib/research/peers/tests and the route-level currency test pass with 0 failed; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~386 <0.9.0_WK_AMGT_RESAPP~386@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~386/AMGT_RESAPP.TO-AMGT-ss-3.a-candidate-that-is-the-subject-by-held-identity-is-excluded.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of each edited product file, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (issuer, 2026-10-11, on the worker's row AMGT_RESAPP-D1-W386-S1):** the first cut had `engine.py` import `scoped_amgt` inside a function; the existing guard `lib/research/peers/tests/test_peers_absent_reasons_plain.py::test_peers_does_not_import_api` forbids that literal anywhere in the peers package, and it is right (the engine is producer-side and the api package imports it). The index now comes from a caller above the package: `lib/research/api/peers_rebuild.py`. The worker was re-seated with its commits fef31c1d99 and a238a172c5 as inherited state. The ss-6 act runs `python -m lib.research.api.peers_rebuild`. Gate limb: none grades an amendment to a spawned order's face and criteria; the order file is put on the worker's branch (the grant).

**ISSUER NOTES:** CTO~DELL1 round-92 analysis @1edd8be57d item 3: "A member whose served key equals the subject's own key is excluded, by IDENTITY, not by ticker form", then the peers rebuild that serves it (`AMGT-ss-6`, staged, its own pair). The engine, not a decorator: a serve-time filter would show 11 members with no backfill. Producer-side: no function redeploy (the request path reads stored objects). E7 is a source-level wiring check by design; the rebuild's member-by-member table (ss-6's pair) is the real control. The engine's `_make`/`denominators` shape is a served-object contract: the new key is additive.

<status>pending</status>
<round>93</round>
<slot>0.9.0_WK_AMGT_RESAPP~386</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
