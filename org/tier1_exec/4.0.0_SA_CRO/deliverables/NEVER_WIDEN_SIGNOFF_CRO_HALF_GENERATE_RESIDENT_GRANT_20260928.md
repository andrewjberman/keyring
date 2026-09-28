# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the Comparison GRANT release: generate AdE17rT6 + resident st2

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_GENERATE_RESIDENT_GRANT_20260928.md`
blob `b6c264b3a068b3f2121a987b93007dbdae70cb9e` @`59af14a585`. The blob is the same at HEAD and on disk.
- Read 2026-09-28 ~01:0xZ. The half was finished ~12:4xZ, after this seat's usage-limit stall.
- This release is a new act with no earlier packet of its own, so there is no word diff.

**Asked by:** 2.0.0_SA_COO~P msg 102283. This seat is not in the act.

## VERDICT: SIGNED on blob b6c264b3

### The grant stays inside Andrew's word

- **The word:** "call 1 yes" (`ANDREW_DIRECT_20260927_195xZ_COMPARISON_PERMISSION_YES_AND_PURGE_S19_SCREENSHOTS.md`),
  for "firms that already see these models in Opal's Model Portfolios view (FWD-11)".
- **The firms:** `_comparison_firms()` (15b9f85eb3) admits exactly `lookup()` of 49financial, inflection and
  cottonwood.
  - These are the 3 of 3 Model Portfolios partner firms that ~M resolved.
  - They were re-validated after CTO ruling (a) and ~Y's benchmark-never-renders proof
    (`IRPT_MVP_M/COMPARISON_CATALOGUE_V2_VALIDATION_20260927.md` addendum 1).
- **The principal classes:** FIRM_ADVISOR, FIRM_OPERATIONS and OPAL_GLOBAL, the set ~M validated.
- **Pins:**
  - The catalogue still types no firm (`permitted_firm_ids` stays `[]`).
  - An entry is admitted only when its policy hashes to one of ~M's 4 pinned values.
  - A catalogue edit alone therefore widens nothing.
- **The wiring (2e3d50caac)** only replaces `get_catalogue: None` with the packaged templates.json reader. It grades
  nothing.

### D1 generate -- the built bytes, read here (S3 `BIEsyaNn`, and the live `Iu3nADja`)

- The zip hashes to `AdE17rT6`; the served `irpt-ycharts-generate` reads `ykJltfTd` (get-function).
- **Census:** 111 -> 111. Five members differ: generate_installed.py, maintained_sources.py, publication.py,
  publisher.py and templates.json. Confirmed here.
- **The new runtime `sys.path` insert** (`_comparison_firms`, `lib/` at position 0):
  - `lib/` in the zip holds ONE module, `opal_naming`, and no top-level module shares its name, so the insert
    shadows nothing;
  - the registry it reads is packaged (`infra/logic/registry/`: 7 files, including scopes.json);
  - `_comparison_firms()` run from the ZIP's own modules returns the three firms.
- **The rebuild-2 failure class** (the internal-record path): the zip's `errors.public_line` takes `admitted=`, and
  `served._record(...)` runs clean on the zip's modules.
- **The success path** is ~Y's composition arms on the BUILT zip, before D1 (packet section 4):
  - Comparison and Multi-Comp ACCEPT;
  - an unknown key REFUSED;
  - Overview unchanged.

  That meets this seat's standard (49a9579720).

### D2 resident -- the built tar, read here (S3 `2ZLL.I5j.`, sha `f681024b..`, 226 members)

- It packages `lib/opal_naming.py` and `infra/logic/registry/scopes.json`. `publication._naming()` resolves the
  TAR's own copy through its ancestor fallback.
- **The name check (c1fd6c5e52) run on the tar's own modules:**
  - `test_foreign_firm_names.py` @c1fd6c5e52: 10 of 10 passed. Positive, own-name, hex-id, longer-token,
    ordinary-word and unregistered-firm arms are all included.
  - **The clean path on real bytes:** the three certified variant PDFs (`s3://opal-data-ycharts/research/20260911/
    variants/`: Overview, Comparison, Multi-Comp) read `[]` for each of the three firms. So a clean report of each
    live template publishes, as the packet says.
- **What the check matches:** it matches only client-firm display names and "prose" aliases, case-sensitive and never
  inside a longer token. The patterns are "49 Financial", "49F", "Inflection Wealth Management" and "Cottonwood
  Capital Advisors"; the demo tenant is excluded.
- **A refusal fails CLOSED:** the report is not published. That is a narrowing, never a widening.

### Both branches

| | before | after |
|---|---|---|
| Comparison / Multi-Comp | REFUSED COMPARISON_CATALOGUE_REQUIRED | ADMITTED for the three firms and three classes; an unknown key or an edited catalogue REFUSED |
| Publish | publishes | a report carrying another client firm's printed name REFUSED FOREIGN_FIRM_NAME_IN_REPORT; a clean report publishes, about 11-16 s slower |

- **Rollbacks:**
  - generate: S3 `Iu3nADja` (ykJltfTd) re-applied;
  - resident: the install script rolls back to st by itself.
- **Accepted:** the one-member `_scope` pin skew, the same shape ykJltfTd serves today.

### Noted, not a condition

`BIEsyaNn` (and the export's `O1Vu8CyD`) are already the LATEST S3 versions of their keys. Any apply of those roots
before the scheduled D1 would move them. Both ledgers are OPEN, which covers it.

Not measured by this seat (the packet's):
- ~Y's composition arms and module census;
- ~P's cold-start smoke;
- the plans;
- the install script's 10 member shas;
- the claim that only Analysis submissions reach this code.
