# NEVER-WIDEN HALF REQUEST -- Holdings UIC-16 at 49F (Schwab full account-type names)

Cell IB-mr-213, task IRPT_BCKEND.TO-IB-m21-213, worker 0.9.0_WK_IRPT_BCKEND~66, worktree branch
`wk-IRPT_BCKEND-66`, based on CLOUD @1ef167e0ba. This is the CANDIDATE for the re-mint that carries this
change into a served page; it is not itself an upload, mint or served write (task BOUNDS).

**AMENDMENT 1 (2026-09-29, worker 0.9.0_WK_IRPT_BCKEND~72, worktree branch `wk-IRPT_BCKEND-72`, based on
CLOUD @dc1fc92e4e):** the CTO refused the half below on the original bytes
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_REFUSED_HOLDINGS_UIC16_49F_20260929.md`, @05b9abe572):
`acct_type` is the PRODUCT code, not the registration -- `IRA` spans six registrations (Contributory, Roth,
Rollover, SEP, SIMPLE, Inherited) and `S1` ("Schwab One") spans five (Individual, Joint, Designated
Beneficiary, Living Trust, Custodial), so the page would read "Individual Retirement" for a Roth. `## The
act` and its measured counts below are REWRITTEN to the REGISTRATION field (`acct_regis`), and the local
candidate diff is REPLACED with the current one. `## COO half` and `## CTO half` below are left exactly as
they were written against the refused bytes (history, not re-signed by this amendment).

## The act

At 49F's next real Holdings/Directory build, `account_mask`'s `display.label` (an ACCOUNT node, via
`holdings_49f.build_49f_actual`) and the directory's `masked_discriminator` (`directory_runner.build_49f`'s
`acct_row`) stop showing Schwab's bare `acct_regis` (registration) code and start showing that code's FULL
NAME from the CTO's committed BridgeFT table
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/SCHWAB_ACCOUNT_CODES_BRIDGEFT_READ_20260929.json`, copied
byte-for-byte into `data/assets/scripts/gold/investor_reporting/schwab_account_codes.json`), e.g.
`****7532 / RH` becomes `****7532 / Roth Contributory IRA`. The lookup reads the table's `acct_regis`
section ONLY, through the new `schwab_account_codes.registration_name()` -- it never falls through to the
`acct_type` (product) section, so a code that is a valid PRODUCT code but not a registration code (e.g.
`IRA`, `S1`) is NOT resolved by it. A code the `acct_regis` section lacks -- including a blank `acct_regis`
(2 of 7,548 accounts) and the one `acct_regis` value the table does not name, `RI401` (1 of 7,548, CTO
102567/102582) -- prints `unrecognised (<code>)` (sanitized by the shared masking rule to
`unrecognised <code>` once parens are stripped), never guessed and never the bare code alone. `account_mask`
and `masked_discriminator` themselves are UNCHANGED (both stay generic formatters over whatever string they
are handed, pinned by their own existing tests with raw codes); the translation is the ONE new step,
`schwab_account_codes.registration_name()`, inserted at the two 49F build call sites only. INF is unaffected
(its source already ships the full registration type in words, bcf7a6adde).

Measured against the real 2026-09-25 `schwab/08335338/silver/dim_balance` partition (7,548 accounts): 7,545
accounts gain a full registration name (every non-`RI401` `acct_regis` code in use is named by the table),
1 account (`RI401`) and 2 blank-code accounts print `unrecognised (<code>)`. Zero guessed. Full detail:
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R21_UIC16_49F_SUMMARY_20260929.json`.

## Blast radius

**Touches:** every 49F Holdings snapshot ACCOUNT node's `display.label` and every 49F row of the Directory's
`masked_discriminator`, at the next real (non-QA) build + upload of those two artifacts for `49financial`.
No other firm (INF, COT), no other field, no schema change (`HoldingsSnapshot.schema.json` /
`DirectoryEntry.schema.json` are unchanged; `masked_discriminator`/`display.label` stay plain strings).

**Local candidate diff** (this worktree, uncommitted at time of writing; the byte-for-byte data-file copy
and the new module + test file are omitted below as pure additions -- see `git status` on this branch for
the full file list):

```diff
diff --git a/.tools/safe_deploy_core.py b/.tools/safe_deploy_core.py
index 582a506ece..b891d3c22a 100644
--- a/.tools/safe_deploy_core.py
+++ b/.tools/safe_deploy_core.py
@@ -419,6 +419,10 @@ CODE_TREES: dict[str, dict] = {
 # sys.modules trace against this worktree's HEAD (2dccc70d49, post lib/silver_ids.py landing 8cd218cd05) adds
 # exactly one file -- lib/silver_ids.py, imported by data/inf/scripts/silver/_orion_api_silver_lib.py -- and drops
 # none: 30 modules and 11 data files (41 total).
+# RE-MEASURED 2026-09-29 (0.9.0_WK_IRPT_BCKEND~66, TO-IB-m21-213, IB-mr-213): a sys.modules + open() trace of
+# `import holdings_49f` then `schwab_account_codes.full_name(...)` against this worktree's HEAD adds exactly two
+# files -- schwab_account_codes.py (new module, imported by holdings_49f.py and directory_runner.py for UIC-16 at
+# 49F) and its data file schwab_account_codes.json -- and drops none: 31 modules and 12 data files (43 total).
 # ---------------------------------------------------------------------------
 _IRPT_HOLDINGS_CLOSURE = (
     "data/assets/scripts/gold/build_cottonwood_mdpf_pair.py",
@@ -429,6 +433,8 @@ _IRPT_HOLDINGS_CLOSURE = (
     "data/assets/scripts/gold/investor_reporting/holdings_membership.py",
     "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py",
     "data/assets/scripts/gold/investor_reporting/inf_positions.py",
+    "data/assets/scripts/gold/investor_reporting/schwab_account_codes.py",
+    "data/assets/scripts/gold/investor_reporting/schwab_account_codes.json",
     "data/assets/scripts/gold/investor_reporting/source_inputs.py",
     "data/assets/scripts/silver/rebalancer_schemas.py",
     "data/black_diamond/scripts/gold/lib/etf_classifier.py",
diff --git a/data/assets/scripts/gold/investor_reporting/directory_runner.py b/data/assets/scripts/gold/investor_reporting/directory_runner.py
index b4d5125c26..(amendment 1) 100644
--- a/data/assets/scripts/gold/investor_reporting/directory_runner.py
+++ b/data/assets/scripts/gold/investor_reporting/directory_runner.py
@@ -114,6 +114,12 @@ if str(_IDS_DIR) not in sys.path:
     sys.path.insert(0, str(_IDS_DIR))
 import ids as _ids  # noqa: E402
 
+# UIC-16 at 49F (IB-mr-213): the Schwab acct_type/acct_regis code -> full name lookup, same
+# directory as this runner (holdings_snapshot.py's own home, one definition for both readers).
+if str(_HERE) not in sys.path:
+    sys.path.insert(0, str(_HERE))
+import schwab_account_codes as _sac  # noqa: E402
+
 SCHEMA_VERSION = "1.0"
 DIRECTORY_REVISION_PREFIX = "irpt-dir"
 ID_NAMESPACE = os.environ.get("IRPT_DIRECTORY_ID_NAMESPACE", "IRPT_DIRECTORY_ID_NS_V1")
@@ -538,8 +544,11 @@ def build_49f(data: dict, business_date: str, directory_revision: str) -> "tuple
             r = acc_ix.loc[aid]
             if isinstance(r, pd.DataFrame):
                 r = r.iloc[0]
+            # UIC-16 (IB-mr-213), amendment 1 (CTO refusal @05b9abe572): the REGISTRATION type
+            # (acct_regis) through registration_name -- NEVER acct_type (the product code) --
+            # turned into its full name from the committed table; a code the acct_regis section
+            # lacks -- including blank -- prints "unrecognised (<code>)", never the bare code alone.
             return {"raw_key": aid, "account_number": aid,
-                    "account_type": _s(r.get("acct_type")),
+                    "account_type": _sac.registration_name(_s(r.get("acct_regis"))),
                     "is_open": _s(r.get("account_is_open")),
                     "closed_date": r.get("closed_date"),
                     "name": _s(r.get("account_name"))}
diff --git a/data/assets/scripts/gold/investor_reporting/holdings_49f.py b/data/assets/scripts/gold/investor_reporting/holdings_49f.py
index f79b6606ee..(amendment 1) 100644
--- a/data/assets/scripts/gold/investor_reporting/holdings_49f.py
+++ b/data/assets/scripts/gold/investor_reporting/holdings_49f.py
@@ -90,6 +90,11 @@ def _hs():
     return hs
 
 
+def _sac():
+    import schwab_account_codes as sac  # late import, same directory (IB-mr-213 / UIC-16 at 49F)
+    return sac
+
+
 def _num(value):
     if value is None or isinstance(value, bool):
         raise FortyNineRefused("REFUSED: 49F unknown numeric value is not zero")
@@ -275,8 +280,13 @@ def build_49f_actual(s3, as_of: str, *, tax_membership_path=None) -> "tuple[list
         raise FortyNineRefused("REFUSED: 49F duplicate custody account in dim_balance")
     balance = balance.set_index(balance["account_id"].map(_text))
-    # CTO 101302: each ACCOUNT node's own mask, from the custody row that mints it (dim_balance acct_type).
+    # CTO 101302: each ACCOUNT node's own mask, from the custody row that mints it. UIC-16
+    # (IB-mr-213), amendment 1 (CTO refusal @05b9abe572): the label is the REGISTRATION type
+    # (dim_balance acct_regis) through registration_name -- NEVER acct_type (the product code:
+    # `IRA` spans six registrations, `S1` spans five) -- turned into its full name from the
+    # committed table before it reaches account_mask; a code the acct_regis section lacks --
+    # including blank -- prints "unrecognised (<code>)", never the bare code alone.
+    sac = _sac()
     account_masks = hs.own_account_masks(firm_id, (
-        (raw, raw, _text(t)) for raw, t in zip(balance.index,
-                                             balance["acct_type"] if "acct_type" in balance.columns else [""] * len(balance))))
+        (raw, raw, sac.registration_name(_text(t))) for raw, t in zip(balance.index,
+                                             balance["acct_regis"] if "acct_regis" in balance.columns else [""] * len(balance))))
     positions = positions.copy()
     positions["account_id"] = positions["account_id"].map(_text)
```

Amendment 1 also adds `schwab_account_codes.registration_name()` beside the existing `full_name()` in
`schwab_account_codes.py` (reads the `acct_regis` section only, never falling through to `acct_type`) and a
new test case in `tests/test_schwab_codes.py` proving a registration-only code (`RH`, absent from
`acct_type`) resolves correctly and a product-only code (`IRA`, absent from `acct_regis`) does not.

New files added by this candidate (pure additions, not shown as a diff hunk): `schwab_account_codes.json`
(byte-for-byte copy, md5 `1950f864bb1cabf61aab5abc15864485`, identical to the CTO's committed table),
`schwab_account_codes.py` (the lookup module), `tests/test_schwab_codes.py` (5 pure unit tests, no AWS call).

### Every reader of 49F's `display.label` and `masked_discriminator`, censused

| # | Reader | File : line | What it does with the field | Check at the re-mint |
|---|---|---|---|---|
| 1 | Directory search / account picker (option list) | `portal/src/pages/InvestorReporting/header/search.ts:94` `optionLabel(displayName, maskedDiscriminator)` | Renders the searchable account option text, wired from `DirectoryEntryWire.masked_discriminator` via `adapt.ts:672` (`maskedDiscriminator: wire.masked_discriminator`) | Open the account picker on the served page for a 49F firm post-re-mint; an IRA/BRO/etc. account's option text reads the full name (e.g. "... / INDIVIDUAL RETIREMENT"), never the bare code |
| 2 | Directory contract validation | `portal/src/pages/InvestorReporting/contracts/directory-browse.ts:25,33`, `contracts/validate.ts:154,317,452` | Type/shape-checks `masked_discriminator`/`maskedDiscriminator` as a plain string; does not itself alter or reject on the new full-name value (still a string) | Confirm the served `DirectoryPage` response validates clean (no `reqNullable` failure) after the re-mint |
| 3 | Holdings card / drill tree (account node label) | `portal/src/pages/InvestorReporting/tabs/holdings/slices.ts:393` `nodeNameFor` (display.label else displayName), consumed by `AllocationBars.tsx`, `DrillTree.tsx`, `HoldingsTreemap.tsx`, `SecurityList.tsx`, header `IdentityCard.tsx:152` | Reads the ACCOUNT node's `display.label` (carried verbatim from the Holdings wire by `adapt.ts:1042-1049`, ruling IRPT-HOLDINGS-DISPLAY-NAMES-20260924); `maskedDiscriminator` is hard-set `null` for every Holdings node (`adapt.ts:1034`) so the Holdings tree's own account label comes ONLY through `display.label`, not through `maskedDiscriminator` | Open a 49F Holdings snapshot on the served page post-re-mint; an account row's name in the tree/treemap/security list/identity card reads the full type, never the bare Schwab code |
| 4 | Holdings tail-matching helpers | `portal/src/pages/InvestorReporting/tabs/holdings/slices.ts:418-420` `maskedLabelFor`, `:431-443` `accountTailFor`, `:452+` `labelUnderAccount` | Extract/re-style an embedded `****nnnn` tail from a node's name/`maskedDiscriminator` for display under an account; regex `EMBEDDED_TAIL` matches digits only, unaffected by the type token changing | Confirm a Rebalancer/model leaf label beneath a 49F account still shows the correct tail post-re-mint (regression check, no code change needed here) |
| 5 | Exports / report generation | `portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx:419` `entry?.maskedDiscriminator` | Names an account in a generated report/export's text | Generate a report for a 49F account post-re-mint; the export's account line reads the full type name |
| 6 | Cache | No dedicated cache of the label content was found. The portal's data-fetch layer keys its cache on `(firm, as_of, revision)` (e.g. `adapt.ts:697-709`'s comment on cache keys uses the opaque firm id, never a display value); no localStorage/serviceWorker persistence of `display.label` or `masked_discriminator` content was located in this census | After the re-mint, hard-refresh the served page for a 49F firm and confirm the new label appears immediately (no stale cached label survives a normal reload) |
| 7 | Test fixtures (fixed strings, not a live reader) | `portal/src/pages/InvestorReporting/fixtures/**`, `__tests__/**` (30 hits) | Hard-coded fixture values (e.g. `"****9001 / IRA"`) exercise the rendering rule against a FIXED string; they do not read the live 49F build and are unaffected by this change | No re-mint check needed; these stay green because `account_mask`/`masked_discriminator` themselves are unchanged (the fixtures never call the new lookup) |
| 8 | Lambda handlers serving the artifacts | `infra/aws/lambda/investor-reporting/directory/entry.py`, `directory/handler.py`, `holdings/handler.py` | Serve the landed JSON (containing the new full-name labels) to the portal verbatim; no transformation of the label text | Confirm a served Directory/Holdings response for a 49F firm, read directly (e.g. via the handler's own smoke path), carries the full name post-re-mint |

Census method: `comp-find "masked_discriminator"` / `"maskedDiscriminator"` / `"display.label"` /
`"display?.label"` across the repo (`all` corpus, bands DEF/SURFACED/CONFIG), read at this worktree's HEAD
(based on CLOUD @1ef167e0ba). No portal test file was edited or needs editing: the label-forming functions
(`optionLabel`, `nodeNameFor`, `maskedLabelFor`, `adaptHoldingsSnapshot`, `adaptDirectoryEntry`) are
string-in/string-out and carry no Schwab-code-specific logic of their own.

## Rollback per key

The act writes only repo files in THIS worktree (no S3 write of any kind -- BOUNDS: no upload, no mint, no
served write). Rollback per key, if the re-mint that consumes this candidate needs to be undone:

- `data/assets/scripts/gold/investor_reporting/schwab_account_codes.json` -- delete the file (it is a new
  addition; its absence returns `schwab_account_codes.full_name` to raising `FileNotFoundError` at import
  time, which is itself a loud failure rather than a silent revert -- so the PAIRED rollback is the next
  bullet, not this file alone).
- `data/assets/scripts/gold/investor_reporting/holdings_49f.py`,
  `data/assets/scripts/gold/investor_reporting/directory_runner.py` -- `git revert` (or hand-restore) the
  two call-site hunks above; `account_mask`/`masked_discriminator` immediately return to passing the bare
  `acct_type` code through unchanged (their own behaviour is untouched by this change either way).
- `data/assets/scripts/gold/investor_reporting/schwab_account_codes.py`,
  `data/assets/scripts/gold/investor_reporting/tests/test_schwab_codes.py` -- delete (new files; no other
  code imports them once the two call sites above are reverted).
- `.tools/safe_deploy_core.py` `_IRPT_HOLDINGS_CLOSURE` -- drop the two added lines (`schwab_account_codes.py`,
  `schwab_account_codes.json`); the tuple returns to its prior 41-member closure.
- Served artifacts (the NEXT real 49F Directory/Holdings upload after this candidate lands): re-run the
  scheduled 49F build from the REVERTED code; the next upload carries the bare codes again. No already-served
  object is mutated by this rollback -- a prior revision stays exactly as served (never re-written), per
  NEVER rule "never move served output without never-widen sign-off": this candidate does not touch any
  already-served key, only the NEXT build's inputs.

Both branches -- signed forward (the re-mint proceeds with full names) and signed as a rollback (the two
call sites revert to bare codes) -- are named above; neither branch mutates an already-served object.

## COO half -- RE-SIGNED by 2.0.0_SA_COO~M (issuer, 2026-09-29 ~08:3xZ) on amendment 1, with a release ORDER that is part of the signature

Superseded: the ~07:0xZ signature on the acct_type candidate, which the CTO refused (@05b9abe572). Read by the issuer
before re-signing, re-run on shared CLOUD after the drain of amendment 1 (@1fe26443ff): IBM21-213-AC1 7 passed;
IBM21-213-AC2 `SCHWAB-REGIS-NAMED 7545/7548 (unrecognised {'RI401': 1, '': 2})` on the real 2026-09-25 dim_balance
partition, 0 guessed -- the CTO's stated expectation exactly; IBM21-213-AC3 HALF-READY; the investor_reporting suite
303 passed, 0 failed; py_compile clean. The two call-site hunks read whole: both labels take `acct_regis` through
`registration_name`, which reads the table's `acct_regis` section only; `full_name` (the product-code path) is called
from no production site.

Blast radius, both branches: forward, 7,545 of 7,548 49F account labels change from a Schwab code to the account's
full REGISTRATION type, and RI401 (1) and blank (2) read `unrecognised`; rollback, the two hunks revert and the next
build carries bare codes again. Neither branch mutates an already-served object.

The release ORDER the signature binds -- this candidate serves on no path that is not already held:
1. Holdings (`display.label`, reader 3): rides the SAME re-mint of the three Holdings packages as the IB-mr-202/203 halves,
   under that re-mint's own ledger and CTO-signed order (org/tier1_exec/1.0.0_SA_CTO/deliverables/
   SIGNOFF_HOLDINGS_L0_CATEGORIES_AND_VENDOR_KEYS_20260929.md): after the contract copy and portal PROD read CATEGORY. No
   separate mint for this change.
2. Directory (`masked_discriminator`, readers 1, 2, 5): serves only at the directory bundle's next re-mint
   (investor-reporting.tar.gz, commit-routed; 0.0.0_AB_MSTR skips it at push on Andrew's word until its members are
   signed). This half is one of the member signatures that re-mint needs; it does not by itself release the bundle.
3. At each re-mint's next publication, every reader in the census is read on the SERVED page with the check named in its
   row; reader 7 (fixtures) needs none.

The 14:15Z scheduled Holdings fire today runs the DEPLOYED packages (members-sha256 94f2e3433d9e) and does not carry this
change; that fire is IB-mr-204's proof and is not a reader of this half.

## CTO half -- owed (1.0.0_SA_CTO)
