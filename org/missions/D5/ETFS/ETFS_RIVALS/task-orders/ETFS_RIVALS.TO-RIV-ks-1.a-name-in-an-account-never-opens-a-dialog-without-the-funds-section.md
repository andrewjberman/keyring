# ETFS_RIVALS task order -- `RIV-ks-1` -- ROUND 23: A NAME IN AN ACCOUNT NEVER OPENS A DIALOG WITHOUT THE FUND'S SECTION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ks-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~13</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (render functions that choose a mention's key)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check file, the round-22 analysis and rows Z-S65 and Z-S66
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. **This order, round 23, is one repair cell: four such buttons on the live page open a dialog with no section.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ks-1` -- a security named in an account's text never opens a dialog without the panel fund's section (rows Z-S65, Z-S66; analysis round 22 R1, R2)
- Measured: the served page of 2026-10-07 (rounds 15 to 22) reads `fund_sections` 2247 buttons, 4 missing: in GQGU's
  panel "META PLATFORMS INC" and "ASML HOLDING NV-NY REG SHS" target the dialogs `30303M102` and `N07059210`, which hold
  a name and no section; the full dialogs are `META_US_Equity` and `ASML_US_Equity`. Reproduced by `ks-1.AC1.py` with the
  served markup: the fund traded the security under a raw key (so `render._fund_keys` counts it), the raw key's page
  name differs from the tabled key's only in case, the account cites the raw key, and `_panel_page` / `_name_link` let
  the citation decide; `_sec_dialogs` builds sections from contribution and trend rows only. The count read 0 through
  round 16, 3 from round 17, 6 from round 21 on day 2026-10-06; the publisher prints a FAIL line and publishes.
- Interface:
  1. On the rendered page every `data-sec` button inside a fund panel targets a dialog that carries a section for that
     fund, or the mention is plain text. A name whose deciding key has no section for the panel's fund links to the key
     of the same security that has one (the page's one key), else reads as plain text with the written form kept in
     the text or a title. No dialog on the page has zero sections.
  2. Round 13's rule stays: inside fund F's panel a name several listings carry links to the listing F holds; the cited
     key breaks a tie between keys that each HAVE a section for F.
  3. `publish_page` already prints `FAIL: fund sections missing` and publishes. It keeps publishing (a day's page is
     not withheld for a link); the manifest's `fund_sections` stays the count. No change to the audit page's bytes
     beyond what item 1 causes.
- Rulings at the cut (issuer): the repair is in how a mention picks its key, not in adding sections for raw keys and
  not in rewriting stored account text. Reuse the page's existing name tables (`_NAME_ALL`, `_NAME_KEYS`) and the set of
  keys that will carry a section; do not read G4 or add a second key map to the renderer. Row Z-S57 (Meta in GQGU under
  two keys in buying_trend) is NOT this cause as far as the issuer has read: Z-S57 is a table bucket, this is a link;
  the worker says in its report whether its read agrees. Why the FAIL line reached no row for two rounds is the
  issuer's answer, not the cell's: the real-run record carried the count and the issuer's packets did not read it;
  from this round the issuer's real-run read prints `fund_sections.missing` in the packet.
- **Organic trigger:** GQGU's panel on the live page; the issuer's real run of the served day reads `fund_sections`
  missing 0 and 0 dialogs with no section.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD ce10d97077 or later)

- The check file's docstring is the exact interface it reads and holds the reproduction: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ks-1.AC1.py` before you build.
- `render.py`: `_fund_keys(ctx, f)` returns the keys fund F "holds or traded" -- contribution rows, trend rows AND the raw `security_key` of each trade in `f["windows"]`; `_fund_panel` sets `_CUR_KEYS` to it. `_panel_page(f, default, cites)` and `_name_link(page, cites)` choose the page name and the key for a name in account text; `_rich` calls them; `_sec_mention` / `_sec_button` / `_sec_id` register a dialog for whatever key they are handed. `_sec_dialogs` writes one dialog per registered key with a section per fund that has a contribution or trend row under that key, so a key registered only by a mention gets a dialog with no section. `render_page` resolves names in two passes (`_resolve_names`).
- `render.fund_section_census(html)` is the publisher's own count; `publish_page` prints its FAIL line from it.
- Existing package tests pin the round-9 and round-13 link rules (`tests/test_r9ln1_ai_text_name_links.py`, `tests/test_r13fe1_alias_by_fund.py`, `tests/test_r13fe1_fund_sections.py`); they must stay green unchanged, or you say which line you re-pinned and why.
- The page's byte budget matters: the real page is 1,690,862 B against a 1,950,000 B cap.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~13/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r23ks1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a name whose cited, traded raw key has no section for the panel's fund links to the tabled key or reads plain; no dialog has zero sections; a traded, cited key no table carries makes no empty dialog; control: without the trade the name links as before and round 13's own-listing rule holds (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ks-1.AC1.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run, never by you): in GQGU's panel the META and ASML mentions open the dialog that carries GQGU's section, or read as plain text; no mention on the page opens a dialog holding only a name.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ks-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ks-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-ks-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~13/ETFS_RIVALS.TO-RIV-ks-1.a-name-in-an-account-never-opens-a-dialog-without-the-funds-section.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ks-1.a-name-in-an-account-never-opens-a-dialog-without-the-funds-section`. Report once: the mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the rule a mention's key now follows, in one sentence, and the function it lives in; what a name reads as when no key of its security has a section for the panel's fund; whether row Z-S57 (Meta in GQGU under two keys in buying_trend) is the same cause, by your read; the name of the test that pins the rule; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.13 (round 23 appended). Source: ROUND_ANALYSIS.round22 @f8a61834fd rulings R1 and R2; rows ETFS_RIVALS-Z-S65 and Z-S66. No ENDPOINT text changes. Items 2 to 4 of the analysis's list are issuer reads and acts, not cells. Chain `~13`, slot `~13`, position 1 of 1. Check file written by the issuer and run at base ce10d97077: ks-1.AC1 FAIL 5 on arms (a) to (e); control (f) PASSES. Package suite at base: 876 passed, 2 skipped, 0 failed (run by the worker under section 3, not a criterion).

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>23</round>
<slot>~13</slot>
<fabric>site-z</fabric>

<status>complete</status>
