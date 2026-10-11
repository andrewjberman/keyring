# AMGT_RESAPP task order -- `AMGT-nn-5` -- EVERY CROSSWALK `write_pool` CALLER REFUSES TO WRITE ABSENT OVER A SERVED COUNT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-nn-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~353</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- tests and the check run over a stubbed S3 client; nothing is put anywhere real.
comp-adversary: RUN at the cut -- over the stubbed harness of test_write_pool_union.py a crosswalk document with research_universe absent over a served folders 97 is PUT through write_pool directly (door B) and through add_security._mint_pool with OPAL_RESEARCH_LIBRARY_ROOT set to a missing directory (door A); r89_write_pool_guard.py FAILs G1 and G2 at the base and PASSes G3 and G4.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-353`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-nn-5` (round 89, decomposition s.97)

CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_AMGT_RESAPP_S5_WRITE_POOL_GUARD_20261010.md` (read it whole first) and
round-88 analysis item 6 (row AMGT_RESAPP-S5). AMGT-kk-1's refusal sits in `crosswalk.main` only (`lib/research/identity/crosswalk.py`,
the block commented "AMGT-kk-1", about lines 1702-1722). `crosswalk.write_pool` is reached by three callers: `crosswalk.main`,
`add_security.py`'s `_persist_registration_and_pool` / `_mint_pool`, and `build_universe.py`'s `union_main`. `add_security.py`
carries `_research_folders_disclosure()` (about line 347), a twin of the swallowing helper (`except Exception: return None, None`).

1. In `crosswalk.write_pool`, after the served-union step and before the schema validation and any put: when `document` is supplied,
   `bucket == POOL_BUCKET` and `CROSSWALK_KEY_RE.match(key)`, and the document's `research_universe` carries NO `folders`
   (an `{"absent": ...}` dict, or missing), and the latest served pool document (`_read_pool_latest(client)[0]`, the read the union
   step already makes -- reuse its result, do not read twice) carries `research_universe.folders` not None: raise `ValueError` whose
   message begins `REFUSED:` and names the served folder count, states that NO put was attempted, and names the remedy (run where
   the research library reads, or point `OPAL_RESEARCH_LIBRARY_ROOT` at a synced copy). Nothing is put, nothing is rewritten.
2. A `write_pool` call with NO `document` (the union write of `build_universe.py`, a different shape under a different prefix) is
   byte-identical to today: the guard never runs.
3. `crosswalk.main` keeps its early refusal as it is (a pre-build exit 2 with the printed reason); the two guards are the same
   rule at two depths and must not disagree: where `main`'s guard fires, `write_pool` is never reached.
4. In `add_security.py` retire the twin `_research_folders_disclosure()`: its callers use the crosswalk's one guarded helper
   (`crosswalk._research_folders_for_disclosure()`, the function `main` uses, same `(folders, root)` pair). If a test in
   `lib/research/identity/tests` patches the retired name, repoint that patch to the helper; do not delete the test.
5. Tests in the new file `lib/research/identity/tests/test_write_pool_guard.py` in the style of `test_write_pool_union.py` (its
   `_FakeS3`, `_document`): door B refused with no put and the served object's bytes unchanged; the control arm (document carrying
   folders) lands; no `document` lands byte-identical; a first publish with no served `research_universe` still lands; the error
   text carries the served count.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W353-S<k>`, `disarm_owner`
`2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write (tests and the check use a stubbed client), no schedule, no SEC, vendor,
   model or Bloomberg call. Run nothing against the real `opal-data-harvest` bucket.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `crosswalk.py` and `add_security.py` and add the one test file; `build_universe.py` is read-only to you.

## 3. SURFACES

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/add_security.py
lib/research/identity/tests/test_write_pool_guard.py
lib/research/identity/tests/test_crosswalk_refuses_absent_library.py
lib/research/identity/tests/test_write_pool_union.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~353/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-nn-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_write_pool_guard.py"; echo "exit=$?"</invocation><expect>PASS G1 (door A, add_security._mint_pool with the library absent: no put, the served object unchanged), PASS G2 (door B, write_pool with a document whose research_universe is absent: no put, the served object unchanged), PASS G3 (control: a document carrying research folders is written over the served count), PASS G4 (the union write with no document lands byte-identical); R89 WRITE-POOL GUARD: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-nn-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/identity/tests -q; echo "exit=$?"</invocation><expect>the whole identity test folder passes with 0 failed (266 passed at the base, plus the new file's tests); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~353 <0.9.0_WK_AMGT_RESAPP~353@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~353/AMGT_RESAPP.TO-AMGT-nn-5.every-write-pool-caller-refuses-absent-over-a-served-count.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the identity folder's last pytest line;
- the three callers and, for each, whether the guard is reached (the one-line read);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO ruling @20261010 + round-88 analysis @6ad172c28d item 6 (AMGT_RESAPP-S5, REMEDIATION_v33; close condition: an add_security run with an unreadable library root exits nonzero with no put, beside a control run that writes -- G1 and G3). `crosswalk.py` is a producer module (a CLI), not part of the served function, so this order has no redeploy leg: it lands by the merge. The guard keys on the DOCUMENT versus the SERVED pool, not on a library probe, so it is device-independent; `_library_absent_reason` stays as `main`'s early probe. Checks dry-run at the base: AC1 FAIL (G1, G2); AC2 PASS (a bound, 266 passed).

<status>pending</status>
<round>89</round>
<slot>0.9.0_WK_AMGT_RESAPP~353</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
