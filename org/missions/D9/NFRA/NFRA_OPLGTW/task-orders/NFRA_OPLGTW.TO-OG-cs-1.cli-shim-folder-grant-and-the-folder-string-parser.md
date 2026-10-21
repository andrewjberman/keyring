# NFRA_OPLGTW task order -- `OG-cs-1` -- the folder-grant decision (a pure function) and the person_access parser that accepts a folder string (cli-shim workstream, wave 1; PRD v3.19 FWD-24 as ruled by the CTO's msg 36300; row NFRA_OPLGTW-Z-S447; the CVO's v3.19 cure: no grant reaches a bronze or raw prefix)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP_CLISHIM.round48.md</decomp_doc>
<owned_cells>OG-cs-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cs-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~180</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this order; the decision is a pure function that calls nothing.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling of 2026-10-21 (msg 36300, FWD-24: a folder grant is a "bucket" or "bucket/prefix" string in person_access channels_allow, channels_deny subtracts, deny wins) and PRD v3.19 (ADMITTED), applied as code with no deploy; the release that carries it is a separate never-widen order.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cs-1` (decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`, workstream CLISHIM-A, round 1 of the cli-shim workstream)

WHY. The cli-shim tools (a later cell) let a granted person list, describe and query the folders they may read. Their ONE admission question is: "may this caller read this key of this bucket?" This cell writes that answer as a pure function, and fixes a defect that would otherwise break every person who holds a folder grant: `app/data_entitlement.py` line 254 `_CHANNEL = re.compile(r"^[a-z][a-z0-9_]{0,63}$")` is applied by `parse_person_access` to the lists `channels_allow` and `channels_deny`, so a bucket name (it has hyphens) or a bucket/prefix (it has a slash) makes the whole record `Malformed`, and the gateway then fails closed for EVERY tool of that person. The grant writer accepts those strings (any non-empty string up to 128 characters), so the reader must too.

DO, in three files and nothing else (under `infra/aws/ec2/opal-gateway/`):

1. `app/data_entitlement.py`, a SMALL edit (at most 40 lines added and 10 removed against the blob `881da34cda`): `channels_allow` and `channels_deny` entries may be EITHER an old channel id (still `[a-z][a-z0-9_]{0,63}`: `native`, `ycharts`, `schwab`, ...) OR a folder string: a bucket name `[a-z0-9][a-z0-9-]{2,62}` optionally followed by `/` and a path of characters `[A-Za-z0-9._=/-]` (at most 100 of them, no `..` segment, no leading or double `/`), at most 128 characters in all. Every other shape (upper case, blank or padded entries, spaces, `..`, a leading `/`, a non-string, more than 128 characters) STILL raises `Malformed`. Keep `_CHANNEL` as the old channel-id pattern and add the folder pattern beside it; do not change `channel_of`, `person_denial` or any other function: a folder string never equals a channel id, so the existing channel logic is untouched (`channels_deny: ["native"]` still denies tools of the native channel; a folder-only deny denies no tool by channel).
2. NEW `app/folder_grant.py` (pure: standard library and `data_entitlement` only; no AWS, no network, no I/O). It defines:
   - `SERVED_BUCKETS = ("opal-data-assets", "opal-data-etfs", "opal-data-portal-v2")`.
   - `is_folder_entry(entry: str) -> bool`: True when the entry is a folder string (it holds a hyphen or a slash), False for an old channel id.
   - `folder_decision(is_master_admin: bool, is_opal: bool, rec, bucket: str, key: str) -> tuple[bool, str]`, where `rec` is a `data_entitlement.PersonAccess` or `None`. Returns `(allowed, reason)`; the reason is plain words a person can act on (at least 10 characters) and names the bucket or folder that was refused. The rules, in this order:
     a. the bucket is not in `SERVED_BUCKETS` -> refused (the reason names the bucket);
     b. the key contains a `..` segment or starts with `/` -> refused;
     c. any path segment of the key is `bronze` or `raw` (a bronze or raw folder at any depth) -> refused, for EVERY caller and under EVERY grant, whole-bucket grants included (the CVO's cure: no grant reaches bronze or raw);
     d. the caller is not an Opal principal (`is_opal` False) -> refused;
     e. `rec` live means `rec` is not None, `rec.status == "active"` and not `rec.stopped`; a folder entry in `rec.channels_deny` that COVERS the key -> refused (deny wins; for the master admin too);
     f. `is_master_admin` -> allowed (every served bucket, bronze and raw excepted by rule c);
     g. else a live `rec` with a folder entry in `rec.channels_allow` that COVERS the key -> allowed; otherwise refused (the reason says no granted folder covers the key).
   - "Covers": an entry is `bucket` (covers every key of that bucket) or `bucket/prefix`; a prefix covers a key only at a path boundary (`opal-data-assets/schwab/08335338/` covers `schwab/08335338/silver/x`, not `schwab/08335338x/silver/x`, not `schwab/08242234/...`). Entries that are old channel ids are ignored by this function.
3. NEW `tests/test_cs1_folder_grant.py`, at least TEN tests, offline, no fixtures beyond `data_entitlement.PersonAccess(status, revision, stopped, tools_allow, tools_deny, channels_allow, channels_deny)` built by hand (all four sets are `frozenset`), `os.environ.setdefault("MOCK_GRAPH", "1")` before any app import: one test per rule a to g, the path-boundary case, deny-over-allow, a whole-bucket grant that still does not reach bronze, the parser accepting `["opal-data-etfs", "opal-data-assets/schwab/08335338/", "native", "ycharts"]` and still raising `Malformed` for `"Bad Case"`, `""`, `" x"`, `"UPPER-bucket"`, `"a b"`, a 129-character entry, `"opal-data-assets/../x"` and `"/opal-data-assets"`, and the old-channel regression (`channels_deny: ["native"]` still denies a native tool through `person_denial`).

## 2. BOUNDS

- Write only the three files above, `W/` and, if a row is needed, the channel. No other product file, no other test, no release, no deploy, no AWS call.
- Counts and hashes only: no e-mail address, account number or token in any file.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/folder_grant.py
infra/aws/ec2/opal-gateway/tests/test_cs1_folder_grant.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~180/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W180-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cs-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)SERVED_BUCKETS is exactly the three buckets: ok.*bronze and raw paths are refused for master_admin and under a whole-bucket grant: ok.*a prefix grant matches inside the folder and not a sibling or a longer name: ok.*deny wins over allow: ok.*a non-Opal caller is refused even with an allow: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cs-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)old channel ids and folder strings together parse: ok.*wrong shapes still raise Malformed .*: ok.*channel logic unchanged: whoami is native, a native deny denies, a folder-only deny denies nothing by channel: ok.*app/data_entitlement\.py against the pin: [3-9]\d? added, \d+ removed .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-cs-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)files that differ from HEAD under the gateway folder: .*: ok.*tests/test_cs1_folder_grant\.py: (?:1\d|[2-9]\d) test functions.*: ok.*new file tests/test_cs1_folder_grant\.py: (?:1\d|[2-9]\d|\d{3}) passed, 0 failed.*neighbours \(3\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the decision, graded by an issuer-written probe independent of your tests. `AC2`: the parser accepts a folder string and nothing else loosens, plus the size bound. `AC3`: the footprint is exactly the three files, and your tests and three neighbours pass.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cs-1.cli-shim-folder-grant-and-the-folder-string-parser.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-1.cli-shim-folder-grant-and-the-folder-string-parser.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream CLISHIM-A, wave 1, decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`. Source: PRD v3.19 FWD-24, the CTO's msgs 36299 and 36300, the CVO's cure, row Z-S447.
- Widening, plainly: none by this order. It changes how a record parses (a record that would have been Malformed now parses) and adds a function nothing calls yet; the tools that call it and the release that carries it are later orders with their own never-widen halves. The one behaviour to name: a person whose record holds a folder string and who today fails closed would, once this ships and the shim tools exist, be admitted for the folders named.
- DISCLOSED READINGS: (1) "Covers" matches at a path boundary; (2) the master admin reads every served bucket except bronze and raw and except a folder in their own `channels_deny`; (3) `bronze` and `raw` are refused as a path SEGMENT at any depth, which also refuses a table folder legitimately named `raw`, if one exists (the CVO's cure is the wider reading).
- Pre-cut: `AC1` base FAIL as expected (`app.folder_grant` absent); `AC2` base FAIL as expected (a folder string raises Malformed; 0 added); `AC3` base FAIL as expected. Arms on a SCRATCH copy of the gateway app (the shared tree untouched): `AC1` all eleven arms read ok on a scratch `folder_grant.py`; `AC2`'s three behaviour arms read ok with the one-line scratch parser (its size lower bound reads NOT OK for a one-line edit, as designed). Pin: `data_entitlement.py` blob `881da34cda`.

<status>pending</status>
<round>48</round>
<workstream>CLISHIM-A</workstream>
<slot>~180</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
