# AMGT_RESAPP task order -- `AMGT-au-4` -- /freshness CARRIES EVERY COVERED NAME (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-au-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~234</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- `covered_security_keys()` is already read by the deployed function (~`:907`, `:942`); no new path.
comp-adversary: RUN by the issuer at the cut -- r71_served c36 FAILS at the base, deployed and local: 250 rows, 42 of 95 covered names missing.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r71-234` (branch `wk-AMGT_RESAPP-234`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r71-234`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-au-4` (round 71, decomposition s.79)

PRD v0.38 FWD-7: Adam sees every covered company on the freshness view; DONE WHEN (PRD `:533`) Adam has used it to find a stale name.

`read_coverage_freshness` (`lib/research/api/scoped_amgt.py` ~`:5027-5108`) builds its rows from the pool's newest universe file
(`universe/v1/2026-09-16.json`), not the covered set: 53 of 95 covered names are present, 42 missing (1299_HK, 8035_JP, 8306_JP, 8316_JP,
8766_JP, 939_HK, ADBE, AI_FP, AMXB_MM, AZN_LN, BATS_LN, BNP_FP, CDNS, CELH, CLX, CNR_CN, GPN, GSK_LN, HEI, IBE_SM, ICT_PM, ISP_IM, JD,
KOFUBL_MM, MER_PM, ML_FP, MSCI, NESN_SW, NKE, NOKIA_FH, OMAB_MM, ORA_FP, PWR, RIO_LN, SAN_FP, SHOP_CN, SLB, SNPS, TTE_FP, UBSG_SW,
VIVT3_BZ, ZTS), and 138 rows are names outside the covered set, 59 with no key.

1. **Every covered name gets a row** keyed `security_key`, built with the same per-name freshness reads the route makes today. A name
   with no stored read serves its row with the dates null and a plain reason.
2. Keep the rows for names outside the covered set only if the route's existing consumers need them; say which in your report.
3. **The plant test** `lib/research/api/tests/test_freshness_covered.py`: a covered name absent from the universe file still gets a row.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W234-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no vendor or model call, no portal write.
2. No existing covered row's dates change.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~234/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-au-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_freshness_covered.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-au-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_served.py" --cell c36 --where local; echo "exit=$?"</invocation><expect>population covered 95 with status 200; C1 PASS missing 0; R71 C36 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~234 <0.9.0_WK_AMGT_RESAPP~234@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~234/AMGT_RESAPP.TO-AMGT-au-4.freshness-every-name.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the functions you changed and what the out-of-set rows became;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-70 analysis item 4, ruling 5. Served by au-7.

<status>pending</status>
<round>71</round>
<slot>0.9.0_WK_AMGT_RESAPP~234</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
