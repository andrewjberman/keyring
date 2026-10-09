# DSGN_AMGTV1 task order -- `AV-zzr-1` -- THE PEER TABLE READS CLEAN, AND ONE MEASURE READS ONE WAY ACROSS TILE AND TABLE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~141</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal 2726bbe7 (= origin DEV, round 65) -- r67.cjs 1 of 6 (arms 1-5 FAIL as expected; PLANTED passes); battery29 ALL PASS at the base (round-65 candidates).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzr-1` (round 67, decomposition v67; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round66.md` section 2 first. Do the items in this order.

The round-66 walk of ASML's Peers tab (`tmp/ui-walk/20261009T142010Z`, shot 131) found the following:
- a ticker cell reads "BMMV2K" (a served id), another reads the served sentence "This listing has only an exchange number; ...";
- the peer prices print with no currency, because the page reads `currency` while the payload serves `price_currency`;
- "Mkt Cap (USD mm)" and "EV (USD mm)" head columns whose subject cells are EUR;
- the subject's price reads "EUR 1626.20" in its header tile and "EUR 1,626" in the table;
- its market cap reads "EUR 631B" in the tile (the header's `CUR_MKT_CAP`) and "EUR 541,932" mm in the table (`market_cap_musd`).

Do the items in order. Paths are under `{SAP}`.

1. **One price format** (`components/StatTile.tsx` `formatStatValue`, format `'price'`): two decimals WITH a thousands separator, e.g.
   `EUR 1,626.20`, `USD 99.81`, and `1,495,000.00 currency not stated` when no code is served. Use
   `toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })`. Every other format stays as it is.
2. **Readable tickers** (`cscTable.ts`): export `memberTicker(member)`.
   - A member whose `identity.resolution` is `MEASURED` and which has a security key (`member.security_key`, else
     `identity.security_key`) prints the key in house form: drop `_Equity`, then `_` becomes a space, so `700_HK_Equity` becomes
     `700 HK`.
   - Every other member prints its company name (`display_name`, else `name`).
   - Never print a served id or a sentence. The served `ticker_reason` is no longer printed in the cell.
3. **Honest headings** (`cscTable.ts`): export `columnHeading(displayLabel, codes)`.
   - Strip the served label's trailing parenthetical: `Mkt Cap (USD mm)` becomes `Mkt Cap`.
   - Append `(<code>)` only when every entry of `codes` is the same non-null code, else `(local)`.
   - In `tabs/PeersTab.tsx`, head each money column (price, market cap, EV) with `columnHeading(column.displayLabel, <the subject's
     code and every member's code for that column>)`. The other columns keep their served label.
4. **Every money cell carries its own currency** (`cscTable.ts` / `tabs/PeersTab.tsx`).
   - A member's price currency is the served `price_currency` (keep `currency` as a fallback). Market cap uses the served
     `cap_currency`.
   - Print each cell's own served code whatever the column's kind (not only MIXED).
   - A cell with no served code prints through `formatStatValue`, which already says "currency not stated".
   - No cross-currency figure is computed: keep the summary rules exactly as they are (a MIXED or UNSTATED column prints no Average and
     "--" for the others).
5. **One format in the table** (`tabs/PeersTab.tsx`):
   - the price cells print through `formatStatValue(value, 'price', code)`;
   - the market cap and EV cells, which are served in millions, print through `formatStatValue(value, 'currency-millions', code)`, so
     the table reads `USD 555B` the way the tile reads `EUR 631B`;
   - the money summary rows of a ONE-currency column print the same way, with the `(n=..)` kept;
   - the ratio columns keep `formatValue`.
6. **The subject's market cap is the tile's figure**: add `mkt_val_sec: 'CUR_MKT_CAP'` to `SUBJECT_HEADER_MNEMONIC`.
   - The subject Mkt Cap cell prints the header's served `CUR_MKT_CAP` with its own currency and its own as-of, through
     `formatStatValue(value, 'currency-abs', code)`. That figure is in units, not millions.
   - It reads the same value as the header tile.
   - The table no longer shows `market_cap_musd` for the subject.
7. **Harness:** re-anchor any `__harness__/` assertion that reads the old price form, the old ticker cell or the old column labels to
   the same fact as now printed, with its claim kept. Record each re-anchor in the instance.

8. **AMENDMENT 1 (issuer ruling on rows D1-W141-S1 and S2).**
   - **S1:** the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/subjectrow.cjs` (battery29)
     still derives its expected strings with the retired `formatValue`. Re-anchor it so it derives them through the page's own
     `formatStatValue`, with the figure's served currency: `'price'` for PX_LAST, and `'currency-millions'` for CURR_ENTP_VAL, which is
     served in millions. Keep its claim: the subject row carries the header's served Price and EV.
     - The exact replacement is in `C:/Users/Test/AppData/Local/Temp/claude/C--Dev-ajb-workspace/64bb45a6-c74b-4873-bac1-2548bd6890d5/scratchpad/subjectrow_reanchored.cjs`.
     - Copy it over the file. The path is now in your `<paths>`.
   - **S2:** the paths and items govern. `cscTable.ts` IS yours this order; the common bound naming it "not yours" was the issuer's
     defect.
   - Then re-run AC1 and AC2, rewrite your proof instance, and flip `<status>` to `complete` in the same commit.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Move and fold, never reword served text; never compute a figure the page does not serve** (C-PRESENTATION-ONLY).
   `reasonWords.ts` and `cscTable.ts` are not yours. No non-ASCII characters (use `--`). Keep each file's line endings as you find
   them (read them first). Edit tool for existing files.
4. Portal files commit inside `portal/` on your portal branch (set the author with `-c user.name=... -c user.email=...`; the nested repo
   has no identity), then the outer commit with safe-commit. Do not commit the portal gitlink.
5. If an item cannot be met within your paths, file a row and stop on that criterion. In particular, if battery29 goes red on a
   harness file outside your paths, file a row naming the harness and the assertion, and stop: the issuer rules it.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/cscTable.ts
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/subjectrow.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~141/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `lib/research/peers/numeric_tickers.py`, `lib/research/peers/engine.py` (the served identity and currency fields), and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round67/checks/r67.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzr-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round67/checks/r67.cjs"; echo "exit=$?"</invocation><expect>ROUND 67 PEERS AND FORMATS: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzr-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzr-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): on the issuer's re-walk of all three names' peers, every ticker cell reads an exchange ticker or the name, every money cell carries its currency, a heading names a currency only when its cells share it, and the subject's price and cap read the same in tile and table.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~141/DSGN_AMGTV1.TO-AV-zzr-1.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-67 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W141-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~D1, 2026-10-09 ~15:0xZ):** rows S1/S2 ruled. subjectrow.cjs is granted and its re-anchor given (the issuer cannot commit under deliverables/2.0.0_SA_COO~D/; the owned-paths gate refused). The worker is re-seated to close. Graded by no gate limb at cut (a modification).

**ISSUER NOTES:** round 67 = `ledger/ROUND_ANALYSIS.round66.md` @f16252a512 section 2, items 1-2, as one cell (both touch PeersTab).
Base portal 2726bbe7 (= origin DEV). LF only. The producer rows go to AMGT_RESAPP at the close walk, as decomposition v67 says.

<status>pending</status>
<round>67</round>
<to_id>DSGN_AMGTV1.TO-AV-zzr-1</to_id>
<slot>~141</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
