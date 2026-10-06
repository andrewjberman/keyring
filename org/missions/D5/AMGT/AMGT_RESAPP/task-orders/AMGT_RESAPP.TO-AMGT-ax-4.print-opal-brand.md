# AMGT_RESAPP task order -- `AMGT-ax-4` -- THE PRINT IN OPAL BRAND FORM, DUPLICATES AND RAW MARKERS REMOVED (FWD-5, CTO RULING 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ax-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~255</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read; the font files ride the package.
comp-adversary: RUN by the issuer at the cut -- r74 c56 FAILS on deployed: 0% Lato; per print 3 company-description headings, 2 current market-cap lines, 5 raw "[MACHINE-..." markers (the c48 floor holds).
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r74-255` (branch `wk-AMGT_RESAPP-255`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r74-255`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ax-4` (round 74, decomposition s.82)

PRD v0.40 FWD-5 DONE WHEN (PRD `:521-525`): the pack reads as a document IN OPAL BRAND FORM. CTO ruling 2: apply the estate's
EXISTING brand assets, with no invented styling.

In `lib/research/print/render_pack.py`:
1. **The brand font, Lato.** Copy `Lato-Regular.ttf`, `Lato-Bold.ttf` and `FONT_LICENSE.txt` from
   `portal/src/pages/InvestorReporting/render/assets/fonts/` into `lib/research/print/fonts/`, and register them with the PDF renderer.
   Body text is Lato Regular, headings Lato Bold.
2. **Brand heading styles and colours** from the portal's design tokens (DSGN_REBRND; read `portal/src/index.css` and the token
   files it imports, read only): the heading colour and rule colour as the tokens define them.
3. **Remove the duplicates:**
   - ONE company-description block (not "Company description", "(full text)" and "COMPANY DESCRIPTION:");
   - ONE current market-cap line ("Market cap" and "Market capitalisation" are the same value). The per-year "at the fiscal year end"
     history stays.
4. **No raw internal markers** (`[MACHINE-EMPTY: ...` and the like): a missing section reads in plain words.
5. A unit reads in words, or the line says plainly that the source gives none.
6. **Plant tests** in `lib/research/print/`.

Report the package size the fonts add.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W255-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. No figure value changes. The portal files are read only.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/print/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~255/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ax-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round74/checks/r74_served.py" --cell c56 --where local; echo "exit=$?"</invocation><expect>the 3 prints read with Lato share 0.80 or more, description headings 1 or fewer, current market-cap lines 1 or fewer, internal markers 0; C1, C2 and C3 PASS; R74 C56 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ax-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/print; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~255 <0.9.0_WK_AMGT_RESAPP~255@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~255/AMGT_RESAPP.TO-AMGT-ax-4.print-opal-brand.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the bytes the fonts add;
- the token names used;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-73 analysis item 5, ruling 2. The CVO reads three rendered prints at L9. Served by ax-5.

<status>pending</status>
<round>74</round>
<slot>0.9.0_WK_AMGT_RESAPP~255</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~07:0xZ):** CLOSED -- drained @55b7a7b626. On the shared tree, r74 c56 local YES (3 of 3, Lato 1.00, 1/1/0, floor 0); print 91 passed. The build-only showed the fonts were not packaged: ax-5 AMENDMENT 1 item 0 @ef57fb9fdc. Row Z-W255-S1 INERT.

<status>complete</status>
