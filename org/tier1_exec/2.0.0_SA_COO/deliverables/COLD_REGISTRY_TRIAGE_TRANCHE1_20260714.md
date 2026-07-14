# Cold-registry triage -- TRANCHE 1 (mechanical), 2026-07-14 ~21:0xZ, 2.0.0_SA_COO

Input: CTO cold list COMP_STATE_COLD_REGISTRY_LIST_20260714.md (191 flags; this tranche = the 64 JSONs).
Method: status field + last-commit age ONLY -- a CLASSIFICATION, not a disposition. Every
CLOSURE-CANDIDATE still needs the one-judgment-read (genuinely-stale-close vs false-positive) on the
quiet-day pass; FP-ALREADY-CLOSED = record already terminal, BEHIND flag is lexical (dense corpus).
REGROW/TO/PRD flags (62/54/11) largely pair with these projects; they ride the same dispositions.

## FP-ALREADY-CLOSED (0)

## CLOSURE-CANDIDATE (13)
- ADHC_TMSTEL.json             status=inactive     last-commit=2026-04-13 (92d)
- ADVI_BFIX4.json              status=inactive     last-commit=2026-05-22 (53d)
- ADVI_FIRMSEP.json            status=inactive     last-commit=2026-05-22 (53d)
- ADVI_FNTEND.json             status=merged       last-commit=2026-04-15 (90d)
- ADVI_VALFIN.json             status=inactive     last-commit=2026-06-02 (42d)
- BDPL_ASTDIM.json             status=merged       last-commit=2026-04-15 (90d)
- BDPL_CNPRCS.json             status=merged       last-commit=2026-04-15 (90d)
- COMP_LEARNS.json             status=inactive     last-commit=2026-06-02 (42d)
- FIND_DUALBIZ.json            status=active       last-commit=2026-06-05 (39d)
- MDPF_BASISSWITCH.json        status=active       last-commit=NO-HISTORY  << RE-CLASSED HELD-CLASS (CTO ruling 210510Z: sovereign_excluded=true in-file, Andrew 07-10 verbatim; NEVER a closure candidate; no leg actioned under the hold)
- MKOV_DLYCLD.json             status=merged       last-commit=2026-05-28 (47d)
- SXPL_RESTIN.json             status=inactive     last-commit=2026-06-02 (42d)
- YALP_MACROS.json             status=on_hold      last-commit=2026-06-05 (39d)

## RECENT-TOUCH (51)
- ADHC_PREFLT.json             status=active       last-commit=2026-07-01 (13d)
- ADVI_BDAPIMIG.json           status=active       last-commit=2026-07-13 (1d)
- ADVI_BREAKS.json             status=active       last-commit=2026-07-07 (7d)
- ADVI_COTETL.json             status=active       last-commit=2026-06-26 (18d)
- ADVI_COTPPLADVFIX.json       status=active       last-commit=2026-07-07 (7d)
- ADVI_COTSNP.json             status=active       last-commit=2026-06-25 (19d)
- ADVI_ETLFIX.json             status=active       last-commit=2026-07-07 (7d)
- ADVI_INFFEE.json             status=active       last-commit=2026-07-07 (7d)
- ADVI_INFREF.json             status=active       last-commit=2026-07-07 (7d)
- ADVI_PRVSYS.json             status=active       last-commit=2026-06-29 (15d)
- ADVI_TAGATTR.json            status=active       last-commit=2026-07-13 (1d)
- ASTN_WSJFT.json              status=active       last-commit=2026-06-25 (19d)
- DATA_ANALYTICS.json          status=active       last-commit=2026-06-29 (15d)
- DATA_PLATFORM.json           status=active       last-commit=2026-06-29 (15d)
- DATA_SSOTMG.json             status=active       last-commit=2026-07-13 (1d)
- ETFS_AVGCAP.json             status=active       last-commit=2026-06-25 (19d)
- ETFS_CANON.json              status=scoping      last-commit=2026-06-25 (19d)
- ETFS_SETUP.json              status=active       last-commit=2026-07-02 (12d)
- EXPAND_AUTHEDGE.json         status=scoping      last-commit=2026-06-25 (19d)
- EXPAND_MSCLOUD.json          status=scoping      last-commit=2026-06-26 (18d)
- HEATMAP_PROCESS.json         status=scoping      last-commit=2026-06-25 (19d)
- MDPF_COTMDL.json             status=active       last-commit=2026-07-07 (7d)
- MKOV_RETFIX.json             status=active       last-commit=2026-07-07 (7d)
- MKOV_TRSRCE.json             status=active       last-commit=2026-07-07 (7d)
- NFRA_AGENTBUS.json           status=active       last-commit=2026-07-08 (6d)
- NFRA_CMTQUE.json             status=on-hold      last-commit=2026-07-14 (0d)
- NFRA_COMPASSURANCE.json      status=active       last-commit=2026-07-13 (1d)
- NFRA_COMPLEARN.json          status=active       last-commit=2026-07-10 (4d)
- NFRA_COMPTEAM.json           status=active       last-commit=2026-07-07 (7d)
- NFRA_COSTAWS.json            status=active       last-commit=2026-06-15 (29d)
- NFRA_EDGES.json              status=active       last-commit=2026-07-09 (5d)
- NFRA_EXPAND.json             status=scoping      last-commit=2026-06-26 (18d)
- NFRA_GCONTR.json             status=active       last-commit=2026-07-09 (5d)
- NFRA_GRAPHS.json             status=active       last-commit=2026-06-16 (28d)
- NFRA_INSTDRILL.json          status=active       last-commit=2026-07-14 (0d)
- NFRA_LOCALROOT.json          status=active       last-commit=2026-07-08 (6d)
- NFRA_MSGRAPH.json            status=decomposing  last-commit=2026-07-09 (5d)
- NFRA_NERVES.json             status=active       last-commit=2026-07-14 (0d)
- NFRA_PASSCRAFT.json          status=active       last-commit=2026-07-10 (4d)
- NFRA_PPL49F.json             status=dormant      last-commit=2026-07-02 (12d)
- NFRA_PPLCOT.json             status=dormant      last-commit=2026-07-02 (12d)
- NFRA_PPLINF.json             status=dormant      last-commit=2026-07-02 (12d)
- NFRA_TERRAFORM.json          status=active       last-commit=2026-07-09 (5d)
- NFRA_TOOLCHECK.json          status=active       last-commit=2026-07-09 (5d)
- NFRA_TOOLGRAPH.json          status=active       last-commit=2026-07-10 (4d)
- NFRA_TOOLHEALTH.json         status=active       last-commit=2026-07-09 (5d)
- NFRA_WRKFLW.json             status=active       last-commit=2026-06-24 (20d)
- SCTY.json                    status=active       last-commit=2026-07-07 (7d)
- SCTY_PREMCP.json             status=active       last-commit=2026-07-07 (7d)
- TRSB_LEDGER.json             status=inactive     last-commit=2026-06-16 (28d)
- YALP_YCUTVR.json             status=active       last-commit=2026-06-15 (29d)

## UNREADABLE (0)

## ANOMALIES + tranche-1 notes (COO, 21:0xZ)

1. **MDPF_BASISSWITCH.json is UNTRACKED (working tree only, mtime Jul 13 02:50, status=active,
   0 REGISTRY rows).** This is a KNOWN measured hazard, not a discovery: LD-0275:42 names it
   ("untracked-but-in-the-hot-registry-glob"). NOT committed by COO -- landing another lane's
   uncommitted working-tree record under my author line is the four-times-fired sweep class
   (CLAUDE.md Git provenance note / LD-0276). QUIET-DAY ACTION: identify the authoring session
   (or route to CTO/MSTR) and have the OWNER land it under their own author line, then REGISTRY row.
   >> RULED (CTO 210510Z): the record is SOVEREIGN-HELD (sovereign_excluded=true, Andrew 07-10 verbatim
   in-file) -- HELD-CLASS, closure OFF, no leg actioned (CTO explicitly not taking up its arch-gate leg).
   Untracked-hazard disposal WITHOUT violating the hold: preservation != actioning. (1) 0.5.0 asked first
   (probable author via owner_primary + MDPF-P1 provenance origin) -- if theirs, THEY land it byte-unchanged
   quoting the hold; (2) on disclaim, COO lands an explicitly-labeled PRESERVATION commit (provenance-unknown
   stated, hold quoted, sovereign_excluded INTACT). Fragility is the only clock. NO REGISTRY row either way
   (consumers keep honoring the exclusion).
2. **4 records carry status=merged** (ADVI_FNTEND, BDPL_ASTDIM, BDPL_CNPRCS, MKOV_DLYCLD) --
   terminal-equivalent (absorbed elsewhere); classifier counted them CLOSURE-CANDIDATE but the
   quiet-day read is only "confirm REGISTRY table placement + phase cites the successor".
3. **6 inactive + 1 on_hold** -- closure discipline says Inactive/On-Hold stays On-Hold, never
   force-moved to Completed; the read is "does the external block still exist?"
4. **FIND_DUALBIZ (status=active, 39d)** has UNTRACKED working files in data/find/dualbiz/config/
   (serp-harvested 2026-06-26) -- activity exists off the record; read needs an owner ping.
5. **F-013 sovereign-exclusion caveat for the whole sweep:** some project JSONs are DELIBERATELY
   row-less/held (118c6166f: 22 ROW-MISSING -> 15 backfilled + 7 HELD with reasons; loader
   b8e7a298f filters at the read). Before closing ANY cold record, check it is not in the held
   class -- a "stale" record may be a sovereign exclusion working as designed.
