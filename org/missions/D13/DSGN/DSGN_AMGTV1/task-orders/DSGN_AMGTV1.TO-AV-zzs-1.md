# DSGN_AMGTV1 task order -- `AV-zzs-1` -- ONE SERVED FIELD PER MEASURE: THE SUBJECT ROW READS THE TILE'S FIGURE OR NOTHING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzs-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~142</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal 32835ce5 (= origin DEV, round 67) -- r68.cjs 3 of 5 (HEADER EMPTY and NO OVERLAY FAIL as expected -- the subject row falls back to the peer set's own Price and EV; HEADER SERVED, BOUNDED and PLANTED hold); battery29 ALL PASS at the base (round-67 candidates).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzs-1` (round 68, decomposition v68; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round67.md` section 2 first. Do the items in this order.

`tabs/PeersTab.tsx` `CscBody` `cellOf` (about lines 143-155) fills the subject row's cells. Where the header serves the figure
(`headerFigureValue`), the cell prints it. Where the header does not, every column except Mkt Cap falls back to the peer set's own
subject value. On 992 HK the Enterprise Value tile reads "--" (the header serves no CURR_ENTP_VAL) while the subject row reads
"60.91B currency not stated" (the peer set's subject EV): one measure, absent in one place and a figure in the other.

1. **The header's figure, or nothing, for every measure the header shows as a tile.** For the subject row's Price (`price`, the tile
   reads PX_LAST) and EV (`ev`, the tile reads CURR_ENTP_VAL) cells, do what the page already does for Mkt Cap (`mkt_val_sec`): print
   the header's served figure, and when the header serves none, print "--". Never fall back to the peer set's subject value for these
   three. Keep the rule in one place: a small set of the tiled codes beside `SUBJECT_HEADER_MNEMONIC`, with a one-line comment
   citing this order and the round-67 analysis.
2. **Every other subject column is unchanged.** P/E (trailing) (`ey`) and every column with no header tile keep today's behaviour
   (the header's figure where served, else the table's own served value). Member rows are untouched.
3. **One formatter.** The cells keep printing through `formatStatValue` with the figure's own served currency, so a header figure with
   no currency reads "<figure> currency not stated" exactly as its tile does. Nothing is converted or guessed.

4. **AMENDMENT 1 (after the close walk 16:07Z; the issuer's diagnosis was incomplete).** On 992 HK the subject row still reads
   "60.91B currency not stated" and the EV tile still reads "--". The 60.91B is the HEADER's own served CURR_ENTP_VAL, not the peer
   set's: the header serves it with a `currency_basis` beginning `UNMEASURED`, and the tile withholds such a money figure (CRPS-ao-3,
   FWD-20; `components/HeaderCards.tsx` `resolveFigure` passes the figure's `unit` and `figureBasis(figure)` to `formatStatValue`,
   which returns null, and the tile body is a dash with the reason on hover). The subject row calls `formatStatValue` WITHOUT the unit
   and the basis, so it skips that rule.
   - In `tabs/PeersTab.tsx`, the subject row's header-served cells pass the header figure's own `unit` and `figureBasis(figure)` (import
     it from `../components/StatTile`) to `formatStatValue`, exactly as the tile does; a null or `UNIT_NOT_RESOLVED_WORDS` display
     prints "--". The row then withholds whenever the tile withholds, and prints whatever the tile prints. Member rows are untouched.
   - Optional, in the same file: the withheld subject cell may carry the tile's reason as its `title` (hover); no new visible words.
   - Your item 1-3 change stays as built (portal 2be8455f is your base).
   - AC1 is `r68.cjs`, which now has 6 arms; its new arm 5 (UNMEASURED) fails at 2be8455f. Then re-run AC2, rewrite your proof instance,
     and flip `<status>` to `complete` in the same commit.

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
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~142/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `components/HeaderCards.tsx`, `components/StatTile.tsx`, `cscTable.ts`, and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round68/checks/r68.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzs-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round68/checks/r68.cjs"; echo "exit=$?"</invocation><expect>ROUND 68 ONE FIELD PER MEASURE: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzs-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzs-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): On 992 HK the Enterprise Value tile and the Peers subject row read the same (both '--' while the header serves no EV), and on ASML both read 'EUR 626B'; Price reads the same in tile and row on both.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~142/DSGN_AMGTV1.TO-AV-zzs-1.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-68 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W142-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~D1, 2026-10-09 ~16:2xZ):** REOPENED. The close walk (tmp/ui-walk/20261009T160722Z shot 011) shows 992 HK's EV still split: the row prints the header's UNMEASURED-basis CURR_ENTP_VAL that the tile withholds (CRPS-ao-3, FWD-20). Item 4 makes the row apply the tile's rule; r68 gains arm 5 (5 of 6 at 2be8455f). Issuer ruling: one rule, the tile's -- the row withholds; the tile is not changed (FWD-20 stands). Graded by no gate limb at cut (a modification).

**ISSUER NOTES:** round 68 = `ledger/ROUND_ANALYSIS.round67.md` @a06920d917 section 2 item 1, one cell. Base portal 32835ce5
(= origin DEV, round 67). LF only. Item 2's producer row is AMGT_RESAPP-D1-S14 @d30938fb2d (already filed).

<status>pending</status>
<round>68</round>
<to_id>DSGN_AMGTV1.TO-AV-zzs-1</to_id>
<slot>~142</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
