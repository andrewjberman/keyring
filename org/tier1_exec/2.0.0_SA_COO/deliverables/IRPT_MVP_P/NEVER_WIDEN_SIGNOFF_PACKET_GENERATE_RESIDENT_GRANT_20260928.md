# Never-widen sign-off packet -- the Comparison GRANT release: generate + resident

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-28 ~00:5xZ.
**Asked by:** ~Y 102177 and 102194 (the re-cut patches; Comparison and Multi-Comp ACCEPT on these pieces); ~M 102184 (the
consumer re-pin); CTO 102169 (firm ids from the registry, nothing typed). Andrew-direct "call 1 yes" (CTO 102047) is
the permission for firms that see Opal's model portfolios. **Ledger:** `irpt-generate-resident-grant-20260928` (U1 and
U2 closed). **Apply:** after MSTR's 03:00-05:00Z freeze.

## 1. What ships (all committed in the backend; publish bytes equal; each parent equals the live pin)

| change | commit | files |
|---|---|---|
| catalogue v2 GRANTED: VERIFIED/GRANTED + the three principal classes; `permitted_firm_ids` stays [] (~Y patch 6b7230b5..) | 6096ee740b | templates.json |
| ~M's consumer re-pinned: the firms are `lib/opal_naming.lookup()` output; 4/4 policy hashes pinned (~M d7c97910d9) | 15b9f85eb3 | _scope/maintained_sources.py |
| the catalogue port wired to the packaged templates.json (it was None, so every comparison refused) | 2e3d50caac | reports/generate_installed.py |
| the publisher refuses FOREIGN_FIRM_NAME_IN_REPORT; the forms come from scopes.json, nothing typed (~Y patch 752fe65f..) | c1fd6c5e52 | ycharts/extract/publication.py, ycharts/generate/publisher.py |

The naming gate (ENFORCE) passed every commit. The earlier cut of the GRANT and name check was refused for typed firm
ids and is not in this release.

## 2. The two moves

**D1 -- irpt-ycharts-generate** `ykJltfTd..` -> `AdE17rT6..` (S3 version BIEsyaNn.)
- Census: 111 -> 111; ONLY the five files above differ.
- Built-zip cold-start smoke: PASS.
- ~Y's `zip_module_census` with the intents named: every collision winner is the intended source. Its six "STALE"
  modules are byte-equal to live ykJltfTd; they are resident-side and not moved here.
- **Shared-package pin skew:** `_scope/maintained_sources.py` @15b9f85eb3, the rest of `_scope` @19d8f3038c. This is
  the same one-member skew live ykJltfTd already serves (@5e266c02cd); ~Y's composition arms cover it.
- Plan: 0/1/0, code only. Rollback: restore S3 version Iu3nADja. (ykJltfTd) as latest and re-apply.

**D2 -- the resident** `fe64236bbb-st` -> `fe64236bbb-st2`
- SUMS vs st: 225/225; ONLY maintained_sources.py, publication.py, publisher.py, templates.json and the bindings differ.
- Tar f681024b.. (S3 version 2ZLL.I5j.).
- `resident_host_install_st2_20260928.sh`:
  - it checks 10 member shas, and runs the factory pre-check on resident_main.py's own sys.path;
  - it stops only on an empty queue, and rolls back to st automatically.

## 3. Blast radius -- both branches

- **Comparison / Multi-Comp selection** (generate): refused today (COMPARISON_CATALOGUE_REQUIRED). After:
  - ADMITTED for an entry whose policy hashes to ~M's pinned value, for a viewer in the three firms and three classes
    (~Y 102194: Comparison P:1728413 and Multi-Comp P:1728415 + P:1728315 ACCEPT);
  - an unknown key, or any catalogue edit, REFUSED.
  - This is the feature Andrew granted (CTO 102047).
- **Publishing (resident):** a non-49financial report whose PDF text carries another firm's printed name is REFUSED
  FOREIGN_FIRM_NAME_IN_REPORT. Clean reports publish as today, adding about 11-16 s per publish (~Y).
- **Overview and everything else:** unchanged.
- **Reachable:** Analysis submissions, which today means the walk windows.

## 4. Apply protocol (after 05:00Z; CRO 102250 / 102279, CTO 102263 pattern)

Before D1, ~Y re-runs the composition arms on the BUILT zip (S3 BIEsyaNn):
- Comparison and Multi-Comp ACCEPT; an unknown key REFUSED; Overview unchanged.

For each move:
- a LIVE before-read on the served path;
- apply, then read back (CodeSha / running root) and a cold start;
- the same read after. Any unnamed difference means a same-turn rollback.

## What the halves sign against

This file's committed blob; the four commits; the two artifacts with their censuses, smokes, plans and rollbacks; the
blast radius in section 3 and the apply protocol in section 4.
