# NFRA_OPLGTW task order -- `OG-ng-1` -- the naming gate grades an IAM s3:prefix condition value against the HEAD-held legacy registry (CTO msgs 34368 and 34376; row Z-S140)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ng-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ng-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~99</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a commit-time tool clause and its tests; nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is `1.0.0_SA_CTO~Z` msg 34376 (re-ruling of Z-S140): "Draft ONE clause in naming-gate.py, on the MX-c-9 A4 precedent". The laptop CTO's conditions are requested through `0.0.0_AB_MSTR~Z`; THIS CELL BUILDS AND PROVES THE CLAUSE; the issuer merges it only after those conditions arrive and are met.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ng-1` (decomposition addendum R3-T.69, workstream NAMING-S3PREFIX, FWD-22)

All paths relative to the repo root. `.tools/naming-gate.py` (about 3,300 lines) is the commit-time naming limb (LGIC_ENFORCE). It REFUSES a NEW out-of-pattern S3 key literal. The OG-ap-20 grant puts four tier-first LEGACY prefixes (`gold/book/*`, `gold/holding/*`, `platinum/reports/*`, `silver/holdings/*`) in the `s3:prefix` condition of a `ListBucket` statement;
the limb refuses them, and `key_rulings` rows do not clear them (the CRO measured it, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OG_AP20_KEY_RULINGS_20261015/FINDING.md` @bc96669f7e). The CTO ruled: keep grading prefixes (a mistyped one confines a ListBucket to nothing, with no error), but let a REGISTERED one grade conformant, on the precedent of the HEAD-held catalog branch.

**The precedent to read first:** commit `df822c81b3` (`git show df822c81b3 -- .tools/naming-gate.py`): `_catalog_registry_held`, `_head_bytes`, the `CATALOG-EXEMPT` printed line and its self-test arms. Reuse its helpers (`_head_bytes`, `git`, the HEAD-only read) and its style; add NOTHING that reads the working tree or the index.

1. **The clause (ONE, in the S3Key limb).** A string that is the VALUE (a string, or an element of the list) of an `s3:prefix` key inside a `Condition` block (`StringLike`, `StringEquals`, `ForAnyValue:*`) of a Terraform file, in `jsonencode(...)` or HCL map form, grades CONFORMANT when ALL hold:
   (a) the value, with AT MOST ONE trailing `*` removed, EQUALS the `template` (or `key`) of a `legacy_addresses.json` row COMMITTED AT HEAD (`git show HEAD:infra/logic/registry/legacy_addresses.json`, never the index or the working tree), whole-string;
   (b) that row's `reader` equals the committing project (derive it the way the gate already derives the committing project for the placement rules, or from the staged paths' `org/missions/<D>/<MACRO>/<CODE>/` home; read how `--staged-paths` is used; if no project can be derived the clause does NOT fire);
   (c) the row's `shape` is `prefix` when the value ends in `/` or `/*`, `object` otherwise (a prefix value for an object row, or the reverse, REFUSES).
   Anything else is graded exactly as today. The clause fires for an `s3:prefix` condition value ONLY: the same string as a resource ARN, a key, or any other attribute is graded as before.
2. **Print a counted line** for every commit that touches a `.tf` carrying an `s3:prefix` value, in the style of `CATALOG-EXEMPT`: `S3PREFIX-REGISTERED admitted=<n> refused=<n> registry_head=<short sha>`, and name each admitted value NEW to its file.
3. **Tests** in `.tools/tests/test_naming_gate_s3prefix.py` (offline; build a throwaway git repo in a temp dir with a HEAD-committed registry; do not touch the real repo's HEAD), named exactly `test_ng1_ac01` .. `test_ng1_ac07`: ac01 a registered prefix with a trailing `*` grades CONFORMANT; ac02 the same value without the `*`; ac03 near misses REFUSE (`**`, a prefix missing its trailing slash, longer, shorter, unregistered); ac04 a row whose reader is ANOTHER project REFUSES; ac05 a row present only in the working tree or the index REFUSES; ac06 the same string as a resource ARN or another attribute is graded as before; ac07 the counted line is printed.
4. **Retirement and ownership,** as a comment block above the clause in the precedent's style: owner `2.0.0_SA_COO~O`; retirement when the grants' prefixes are emitted as `lib/opal_naming.py address()` output (LGIC); single shared tool, landed once through CLOUD (the laptop CTO's condition 7 of the catalog exemption).

## 2. BOUNDS

- `.tools/naming-gate.py` and the one test file only. NO other gate, hook or registry file; do NOT edit `legacy_addresses.json` or any key_rulings file (the CRO's lane, already landed).
- The clause is a NARROWING of what is refused today and nothing else: every currently refused literal outside the exact conditions above still refuses (the self-test's existing arms and the catalog branch stay green).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; build any alert; override a gate (`# naming-override` or similar) to get your own commit through. The commit of THIS cell touches only `.tools/` files and graded literals of its own tests are in temp repos, so it should not need one.
- DO NOT ASK for the laptop CTO's conditions; the issuer holds them. BUILD AND PROVE; the merge waits on them.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
.tools/naming-gate.py
.tools/tests/test_naming_gate_s3prefix.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~99/`. Rows: id `NFRA_OPLGTW-Z-W99-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ng-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ng1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 8 of 8; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ng-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ng1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)naming-gate self-test: rc=0.*the four registered ETF patterns refused: 0 \(want 0\); the mistyped one refused: [1-9]\d* \(want 1\+\), enforce rc [1-9]\d*.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the clause conforms a registered prefix (with or without the `*`) and refuses every near miss, another project's row, a working-tree-only row, and prints its counted line. `AC2`: the gate's self-test still passes and the real four patterns grade clean while a mistyped one in the same diff still refuses.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ng-1.naming-s3prefix-clause.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream NAMING-S3PREFIX (decomposition addendum R3-T.69). CTO msgs 34368 (stay in scope) and 34376 (re-ruled: draft ONE clause on the MX-c-9 A4 precedent; laptop CTO conditions first; land nothing before they arrive). The four ETF prefix rows (`gateway-etfs-gold-book` etc., reader `NFRA_OPLGTW`) are landed at `f636989b97`.
- The merge of this cell waits on the laptop CTO's conditions (requested by the CTO through `0.0.0_AB_MSTR~Z`). The `OG-ap-20` grant commit follows the merge.
- Pre-cut: ng1.AC1 base FAIL as expected (test file absent); ng1.AC2 base FAIL as expected (the four patterns refuse).

- A1 (issuer, 2026-10-15 ~07:2xZ): the laptop CTO's SEVEN CONDITIONS are read (`RULING_20261015_064xZ_NAMING_GATE_IAM_PREFIX_CLAUSE_CONDITIONS.md` @bf9198273e; `git show bf9198273e:org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261015_064xZ_NAMING_GATE_IAM_PREFIX_CLAUSE_CONDITIONS.md`, fetched from origin/box/laptop). They TIGHTEN this order, and where they differ THEY govern: (1) the clause applies only to a string in an IAM policy document's `Condition` block under the `s3:prefix` key; the same string as a resource ARN or a code literal is REFUSED. (2) `legacy_addresses.json` is read with `git show HEAD:`; a row staged in the same commit admits nothing. (3) THE SAME BUCKET: the policy statement's bucket (its `Resource` ARN, `arn:aws:s3:::<bucket>`) must equal the legacy row's `bucket`. (4) EXACTLY ONE TRAILING WILDCARD AND NOTHING ELSE: the value must be `<registered key part>` + `*`; a value WITHOUT the `*` is not admitted by this clause (it is NOT optional, correcting step 1(a) above); a `*` anywhere else, a `?`, a `**`, an empty key part or a bare `*` REFUSES; near misses (one segment more or less) and unregistered prefixes REFUSE. (5) the row's `reader` is the committing project. (6) THE COUNTED LINE is exactly `IAM-PREFIX-ADMITTED n=<k> bucket=<b> prefixes=<list> registry_head=<sha>` (not `S3PREFIX-REGISTERED`), printed by every commit that uses the clause. (7) the clause passes the NAME, not the ACCESS (the ETF grant has its own never-widen pair); the shared tool lands once through CLOUD with the self-test green; carry the retirement line (deleted when these stores move to `address()` form). Tests are now EIGHT, `test_ng1_ac01` .. `test_ng1_ac08`, in the order of ng1.AC1.sh's header (ac02: the value without `*` is not admitted; ac03: the near-miss list; ac07: a different bucket; ac08: the counted line); ng1.AC1 reads 8 of 8. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>NAMING-S3PREFIX</workstream>
<slot>~99</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
