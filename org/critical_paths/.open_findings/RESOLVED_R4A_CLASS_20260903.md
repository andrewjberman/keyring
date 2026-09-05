# RESOLVED AS A CLASS -- R4-A closeout-drift findings, 2026-09-03 (1.0.0_SA_CTO, mechanism owner)

Decision on 0.0.0_AB_MSTR's /govern owner-sweep (93407, LD-0528): a closeout-drift finding on a closed row is unresolvable by any act -- comp-state's BEHIND is lexical drift over a corpus that keeps mentioning a closed project's tokens while the row is never touched again; the trigger was measuring itself. The owned-finding emission of R4-A is retired in `.tools/git-hooks/closeout-comp-state-post-commit.sh` (the run now lands one line in `closeout-runs.log`); the files below are the class resolved per the README's lifecycle (record why expected, then delete). R4-B files are untouched.

Written 2026-09-03T09:11:09Z. Denominator: 250 json files in the folder; 250 closeout-drift deleted (198 tracked, 52 untracked); 0 kept.

## Deleted, by owner

- 2.0.0_SA_COO~Z: 184
- 1.0.0_SA_CTO: 34
- 2.0.0_SA_COO: 17
- 1.0.0_SA_CTO~Z: 5
- 4.0.0_SA_CRO: 4
- 1.0.0_SA_CTO~A: 2
- 2.0.0_SA_COO~X: 2
- 0.0.0_AB_MSTR~Z: 1
- 1.0.0_SA_CTO~Y: 1

## Deleted, by project

- ADVI_PERFORMANCE: 8
- ETFS_POSITIONING: 7
- ADVI_STITCH: 5
- DATA_BDINSURANCE_PRD: 5
- DATA_BDINSURANCE: 5
- ADVI_INSURE: 4
- MDPF_3FIRMS: 3
- NFRA_WORLDMODEL: 3
- OPAL_TAXSMA: 3
- ADVI_49F: 2
- ADVI_COTETL: 2
- D1_CATVIEWS: 2
- ETFS_CANON: 2
- ETFS_POSITIONING_PRD: 2
- ETFS_SATELLITES: 2
- MDPF_CANRTE: 2
- MDPF_GLOBAL: 2
- NFRA_KUZUSPLIT: 2
- NFRA_VELOCITY: 2
- OPAL_SQSCHAT: 2
- ADHC_COMPIL_V5: 1
- ADHC_COMPIL: 1
- ADHC_DESIGN: 1
- ADHC_GLDINC: 1
- ADHC_KEEPWARM: 1
- ADHC_LEDGEH: 1
- ADHC_PREFLT_PRD: 1
- ADHC_PREFLT: 1
- ADHC_TMSTEL: 1
- ADHC_TRIGMRK: 1
- ADVI_49FSRC: 1
- ADVI_49NNAFIX: 1
- ADVI_49PUSH: 1
- ADVI_ANONYM: 1
- ADVI_APISCP: 1
- ADVI_BDAPIMIG_PRD: 1
- ADVI_BDAPIMIG: 1
- ADVI_BFIX4: 1
- ADVI_BREAKS_PRD: 1
- ADVI_BREAKS: 1
- ADVI_COTETL_AUAFIX_PRD: 1
- ADVI_COTSNP: 1
- ADVI_ETLFIX: 1
- ADVI_FEREFI: 1
- ADVI_FIRMSEP: 1
- ADVI_FNTEND: 1
- ADVI_GLDOPS: 1
- ADVI_INFFEE_PRD: 1
- ADVI_INFFEE: 1
- ADVI_INFNNA: 1
- ADVI_INFPRM: 1
- ADVI_INFREF_PRD: 1
- ADVI_INFREF: 1
- ADVI_NNAFEE: 1
- ADVI_PERFORMANCE_PRD: 1
- ADVI_PERFRP: 1
- ADVI_PRVSYS_PRD: 1
- ADVI_PRVSYS: 1
- ADVI_TICKID: 1
- ADVI_TWR: 1
- ADVI_VALFIN: 1
- ASTN_WSJFT: 1
- ATOM_LAYER0: 1
- BDPL_ASTDIM: 1
- BDPL_CNPRCS: 1
- BD_SCHWABCONV: 1
- COMPIL_V5: 1
- COMP_LEARNS: 1
- COT_CANON458: 1
- D11_SUBSTRATE_ANALYSIS_PRD: 1
- DATA_ANALYTICS: 1
- DATA_PLATFORM: 1
- DATA_SSOTMG_PRD: 1
- DATA_SSOTMG: 1
- DRFR_PTMCH: 1
- ETFS_AVGCAP: 1
- ETFS_SETUP: 1
- EXPAND_AUTHEDGE: 1
- EXPAND_MSCLOUD: 1
- FIND_DUALBIZ: 1
- FIND_INSURE: 1
- HEATMAP_PROCESS: 1
- MDLP_DISTFIX_PRD: 1
- MDLP_DISTFIX: 1
- MDLP_WYNCHT: 1
- MDPF_3FIRMS_PRD: 1
- MDPF_CANONICAL_PLATINUM_PRD: 1
- MDPF_CANPLAT: 1
- MDPF_CHANNEL_INDEPENDENCE_PRD: 1
- MDPF_CHANNEL_INDEPENDENCE: 1
- MDPF_COTREMEDIATION: 1
- MDPF_COUNTS_PRD: 1
- MDPF_COUNTS: 1
- MDPF_DEBTCLEAN: 1
- MDPF_GLOBAL_PRD: 1
- MDPF_REVAMP: 1
- MKOV_DLYCLD: 1
- MKOV_RETFIX: 1
- MKOV_TRSRCE: 1
- NFRA_AGENTBUS: 1
- NFRA_AKPIPE: 1
- NFRA_C3MATERIALIZE_PRD: 1
- NFRA_C3MATERIALIZE: 1
- NFRA_CMTQUE: 1
- NFRA_COMPASSURANCE: 1
- NFRA_COMPCLOSE_PRD: 1
- NFRA_COMPCLOSE: 1
- NFRA_COMPDIFF: 1
- NFRA_COMPDRIFT: 1
- NFRA_COMPILERKIT: 1
- NFRA_COMPLEARN: 1
- NFRA_COMPPROOF: 1
- NFRA_COMPROUTE: 1
- NFRA_COMPSIMILAR: 1
- NFRA_COMPTEAM: 1
- NFRA_COMPTOOLS: 1
- NFRA_COMPUNIFY: 1
- NFRA_COMP: 1
- NFRA_COSTAWS: 1
- NFRA_CSE: 1
- NFRA_DEBTSCAN: 1
- NFRA_DEPLOYLEDGER: 1
- NFRA_DTAFLP: 1
- NFRA_EDGES: 1
- NFRA_EXPAND: 1
- NFRA_FEDOBS: 1
- NFRA_GCONTR: 1
- NFRA_GENESIS: 1
- NFRA_GLOBGRPH_PRD: 1
- NFRA_GLOBGRPH: 1
- NFRA_GRAPHDEPTH: 1
- NFRA_GRAPHFEED: 1
- NFRA_GRAPHS: 1
- NFRA_GRAPHUNI: 1
- NFRA_INFRPT: 1
- NFRA_INSTDRILL: 1
- NFRA_INTEGRATIONS: 1
- NFRA_KUZUSPLIT_PRD: 1
- NFRA_LOCALROOT: 1
- NFRA_MOTIF: 1
- NFRA_MSBEFF: 1
- NFRA_MSGRAPH: 1
- NFRA_NERVES_PRD: 1
- NFRA_NERVES: 1
- NFRA_NESTEDABSTRACT: 1
- NFRA_ONTOLOGY: 1
- NFRA_OPLMCP: 1
- NFRA_PASSCRAFT: 1
- NFRA_PIPELINE: 1
- NFRA_PIPESCRIPT_PRD: 1
- NFRA_PIPESCRIPT: 1
- NFRA_PPLCOT: 1
- NFRA_PPLINF: 1
- NFRA_PROMOTE: 1
- NFRA_PSTMRT: 1
- NFRA_REPOCOHERENCEGRAPH: 1
- NFRA_SUBSTRATECARDING: 1
- NFRA_SYSPARITY: 1
- NFRA_SYSTEM: 1
- NFRA_TERRAFORM: 1
- NFRA_TOOLARCH: 1
- NFRA_TOOLBHVR: 1
- NFRA_TOOLCHECK: 1
- NFRA_TOOLGRAPH: 1
- NFRA_TOOLHEALTH: 1
- NFRA_TSGRAPH: 1
- NFRA_VELOCITY_CORE: 1
- NFRA_VELOCITY_ESTATE: 1
- NFRA_WEBSITE: 1
- NFRA_WORLDMODEL_PRD: 1
- NFRA_WRKFLW: 1
- OPAL_ADVIPOINTERS: 1
- OPAL_ALERTS: 1
- OPAL_ALTRESEARCH: 1
- OPAL_ASSETS: 1
- OPAL_BBGTML: 1
- OPAL_CONSOLIDATION_PRD: 1
- OPAL_CONSOLIDATION: 1
- OPAL_GLDRNS: 1
- OPAL_KIMIPIPELINE: 1
- OPAL_LCLRPO: 1
- OPAL_PRISTINE: 1
- OPAL_SCHEDULE: 1
- OPAL_STNDRD: 1
- OPAL_TAXONOMY: 1
- OPAL_TAXSMA_PT2: 1
- OPAL_TAXSMA_REGISTRY_PRD: 1
- OPAL_TAXSMA_REGISTRY: 1
- OPAL_TICKET: 1
- OPAL_VENDORPROVENANCE: 1
- PORTAL_AUTHHARD: 1
- POSN_CUSTOM: 1
- POSN_TENANCY: 1
- SCTY_MCPGUARD: 1
- SCTY_PREMCP: 1
- SXPL_RESTIN: 1
- TRSB_LEDGER: 1
- UIUX_DESIGN: 1
- VELOCITY_CORE: 1
- VELOCITY_ESTATE: 1
- WSE_COTMDL: 1
- YALP_CAUSAL: 1
- YALP_CMASMP: 1
- YALP_MACROS: 1
- YALP_YCUTVR: 1

## Kept

- none

## Every deleted file

| file | project | owner | closing_commit | detected | review_by | git |
|---|---|---|---|---|---|---|
| org/critical_paths/.open_findings/ADHC_COMPIL_V5_closeout_drift_20260806T235728Z.json | ADHC_COMPIL_V5 | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADHC_COMPIL_closeout_drift_20260806T235728Z.json | ADHC_COMPIL | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADHC_DESIGN_closeout_drift_20260806T235728Z.json | ADHC_DESIGN | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADHC_GLDINC_closeout_drift_20260806T235728Z.json | ADHC_GLDINC | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADHC_KEEPWARM_closeout_drift_20260806T235728Z.json | ADHC_KEEPWARM | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADHC_LEDGEH_closeout_drift_20260806T235728Z.json | ADHC_LEDGEH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADHC_PREFLT_PRD_closeout_drift_20260806T235728Z.json | ADHC_PREFLT_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADHC_PREFLT_closeout_drift_20260806T235728Z.json | ADHC_PREFLT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADHC_TMSTEL_closeout_drift_20260806T235728Z.json | ADHC_TMSTEL | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADHC_TRIGMRK_closeout_drift_20260806T235728Z.json | ADHC_TRIGMRK | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_49FSRC_closeout_drift_20260901T181710Z.json | ADVI_49FSRC | 1.0.0_SA_CTO | a2ff0db2e7 | 20260901T181710Z | 2026-09-03 | untracked |
| org/critical_paths/.open_findings/ADVI_49F_closeout_drift_20260827T154959Z.json | ADVI_49F | 1.0.0_SA_CTO | 67ee4a4485 | 20260827T154959Z | 2026-08-29 | untracked |
| org/critical_paths/.open_findings/ADVI_49F_closeout_drift_20260827T155141Z.json | ADVI_49F | 1.0.0_SA_CTO | 262fbae423 | 20260827T155141Z | 2026-08-29 | untracked |
| org/critical_paths/.open_findings/ADVI_49NNAFIX_closeout_drift_20260806T235728Z.json | ADVI_49NNAFIX | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_49PUSH_closeout_drift_20260806T235728Z.json | ADVI_49PUSH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_ANONYM_closeout_drift_20260806T235728Z.json | ADVI_ANONYM | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_APISCP_closeout_drift_20260806T235728Z.json | ADVI_APISCP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_BDAPIMIG_PRD_closeout_drift_20260806T235728Z.json | ADVI_BDAPIMIG_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_BDAPIMIG_closeout_drift_20260806T235728Z.json | ADVI_BDAPIMIG | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_BFIX4_closeout_drift_20260806T235728Z.json | ADVI_BFIX4 | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_BREAKS_PRD_closeout_drift_20260806T235728Z.json | ADVI_BREAKS_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_BREAKS_closeout_drift_20260806T235728Z.json | ADVI_BREAKS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_COTETL_AUAFIX_PRD_closeout_drift_20260806T235728Z.json | ADVI_COTETL_AUAFIX_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_COTETL_closeout_drift_20260806T235728Z.json | ADVI_COTETL | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_COTETL_closeout_drift_20260825T033647Z.json | ADVI_COTETL | 1.0.0_SA_CTO | ccd60bd341 | 20260825T033647Z | 2026-08-27 | untracked |
| org/critical_paths/.open_findings/ADVI_COTSNP_closeout_drift_20260806T235728Z.json | ADVI_COTSNP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_ETLFIX_closeout_drift_20260806T235728Z.json | ADVI_ETLFIX | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_FEREFI_closeout_drift_20260806T235728Z.json | ADVI_FEREFI | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_FIRMSEP_closeout_drift_20260806T235728Z.json | ADVI_FIRMSEP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_FNTEND_closeout_drift_20260806T235728Z.json | ADVI_FNTEND | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_GLDOPS_closeout_drift_20260806T235728Z.json | ADVI_GLDOPS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_INFFEE_PRD_closeout_drift_20260806T235728Z.json | ADVI_INFFEE_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_INFFEE_closeout_drift_20260806T235728Z.json | ADVI_INFFEE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_INFNNA_closeout_drift_20260806T235728Z.json | ADVI_INFNNA | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_INFPRM_closeout_drift_20260806T235728Z.json | ADVI_INFPRM | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_INFREF_PRD_closeout_drift_20260806T235728Z.json | ADVI_INFREF_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_INFREF_closeout_drift_20260806T235728Z.json | ADVI_INFREF | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_INSURE_closeout_drift_20260824T183504Z.json | ADVI_INSURE | 1.0.0_SA_CTO | 17710c4640 | 20260824T183504Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ADVI_INSURE_closeout_drift_20260824T201830Z.json | ADVI_INSURE | 2.0.0_SA_COO | 1ce9b2d6bc | 20260824T201830Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ADVI_INSURE_closeout_drift_20260827T152628Z.json | ADVI_INSURE | 1.0.0_SA_CTO | 2fc8f4011d | 20260827T152628Z | 2026-08-29 | untracked |
| org/critical_paths/.open_findings/ADVI_INSURE_closeout_drift_20260828T172146Z.json | ADVI_INSURE | 2.0.0_SA_COO | 1f47b14224 | 20260828T172146Z | 2026-08-30 | untracked |
| org/critical_paths/.open_findings/ADVI_NNAFEE_closeout_drift_20260806T235728Z.json | ADVI_NNAFEE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_PERFORMANCE_PRD_closeout_drift_20260806T235728Z.json | ADVI_PERFORMANCE_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_PERFORMANCE_closeout_drift_20260806T235728Z.json | ADVI_PERFORMANCE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_PERFORMANCE_closeout_drift_20260824T172353Z.json | ADVI_PERFORMANCE | 1.0.0_SA_CTO | d9fff9a9c2 | 20260824T172353Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ADVI_PERFORMANCE_closeout_drift_20260824T173514Z.json | ADVI_PERFORMANCE | 1.0.0_SA_CTO | a6b91e8b78 | 20260824T173514Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ADVI_PERFORMANCE_closeout_drift_20260824T183504Z.json | ADVI_PERFORMANCE | 1.0.0_SA_CTO | 17710c4640 | 20260824T183504Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ADVI_PERFORMANCE_closeout_drift_20260824T201830Z.json | ADVI_PERFORMANCE | 2.0.0_SA_COO | 1ce9b2d6bc | 20260824T201830Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ADVI_PERFORMANCE_closeout_drift_20260827T144208Z.json | ADVI_PERFORMANCE | 1.0.0_SA_CTO | e4f7ecbfdc | 20260827T144208Z | 2026-08-29 | untracked |
| org/critical_paths/.open_findings/ADVI_PERFORMANCE_closeout_drift_20260827T152628Z.json | ADVI_PERFORMANCE | 1.0.0_SA_CTO | 2fc8f4011d | 20260827T152628Z | 2026-08-29 | untracked |
| org/critical_paths/.open_findings/ADVI_PERFORMANCE_closeout_drift_20260828T172146Z.json | ADVI_PERFORMANCE | 2.0.0_SA_COO | 1f47b14224 | 20260828T172146Z | 2026-08-30 | untracked |
| org/critical_paths/.open_findings/ADVI_PERFRP_closeout_drift_20260828T172146Z.json | ADVI_PERFRP | 2.0.0_SA_COO | 1f47b14224 | 20260828T172146Z | 2026-08-30 | untracked |
| org/critical_paths/.open_findings/ADVI_PRVSYS_PRD_closeout_drift_20260806T235728Z.json | ADVI_PRVSYS_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_PRVSYS_closeout_drift_20260806T235728Z.json | ADVI_PRVSYS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_STITCH_closeout_drift_20260824T175033Z.json | ADVI_STITCH | 1.0.0_SA_CTO | 7c60531eb4 | 20260824T175033Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ADVI_STITCH_closeout_drift_20260824T183504Z.json | ADVI_STITCH | 1.0.0_SA_CTO | 17710c4640 | 20260824T183504Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ADVI_STITCH_closeout_drift_20260824T201830Z.json | ADVI_STITCH | 2.0.0_SA_COO | 1ce9b2d6bc | 20260824T201830Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ADVI_STITCH_closeout_drift_20260827T152628Z.json | ADVI_STITCH | 1.0.0_SA_CTO | 2fc8f4011d | 20260827T152628Z | 2026-08-29 | untracked |
| org/critical_paths/.open_findings/ADVI_STITCH_closeout_drift_20260828T172146Z.json | ADVI_STITCH | 2.0.0_SA_COO | 1f47b14224 | 20260828T172146Z | 2026-08-30 | untracked |
| org/critical_paths/.open_findings/ADVI_TICKID_closeout_drift_20260806T235728Z.json | ADVI_TICKID | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_TWR_closeout_drift_20260806T235728Z.json | ADVI_TWR | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ADVI_VALFIN_closeout_drift_20260806T235728Z.json | ADVI_VALFIN | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ASTN_WSJFT_closeout_drift_20260806T235728Z.json | ASTN_WSJFT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ATOM_LAYER0_closeout_drift_20260820T200207Z.json | ATOM_LAYER0 | 1.0.0_SA_CTO | f32a5c0019 | 20260820T200207Z | 2026-08-22 | untracked |
| org/critical_paths/.open_findings/BDPL_ASTDIM_closeout_drift_20260806T235728Z.json | BDPL_ASTDIM | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/BDPL_CNPRCS_closeout_drift_20260806T235728Z.json | BDPL_CNPRCS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/BD_SCHWABCONV_closeout_drift_20260806T235728Z.json | BD_SCHWABCONV | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/COMPIL_V5_closeout_drift_20260806T235728Z.json | COMPIL_V5 | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/COMP_LEARNS_closeout_drift_20260806T235728Z.json | COMP_LEARNS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/COT_CANON458_closeout_drift_20260825T033647Z.json | COT_CANON458 | 1.0.0_SA_CTO | ccd60bd341 | 20260825T033647Z | 2026-08-27 | untracked |
| org/critical_paths/.open_findings/D11_SUBSTRATE_ANALYSIS_PRD_closeout_drift_20260826T192437Z.json | D11_SUBSTRATE_ANALYSIS_PRD | 2.0.0_SA_COO | 7c5c8b0570 | 20260826T192437Z | 2026-08-28 | untracked |
| org/critical_paths/.open_findings/D1_CATVIEWS_closeout_drift_20260826T192437Z.json | D1_CATVIEWS | 2.0.0_SA_COO | 7c5c8b0570 | 20260826T192437Z | 2026-08-28 | untracked |
| org/critical_paths/.open_findings/D1_CATVIEWS_closeout_drift_20260828T160055Z.json | D1_CATVIEWS | 2.0.0_SA_COO~Z | b8d7f50017 | 20260828T160055Z | 2026-08-30 | tracked |
| org/critical_paths/.open_findings/DATA_ANALYTICS_closeout_drift_20260806T235728Z.json | DATA_ANALYTICS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_PRD_closeout_drift_20260824T172353Z.json | DATA_BDINSURANCE_PRD | 1.0.0_SA_CTO | d9fff9a9c2 | 20260824T172353Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_PRD_closeout_drift_20260824T173514Z.json | DATA_BDINSURANCE_PRD | 1.0.0_SA_CTO | a6b91e8b78 | 20260824T173514Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_PRD_closeout_drift_20260824T182444Z.json | DATA_BDINSURANCE_PRD | 1.0.0_SA_CTO | ee2c15686f | 20260824T182444Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_PRD_closeout_drift_20260824T205737Z.json | DATA_BDINSURANCE_PRD | 2.0.0_SA_COO | b23bbe1f6d | 20260824T205737Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_PRD_closeout_drift_20260827T144208Z.json | DATA_BDINSURANCE_PRD | 1.0.0_SA_CTO | e4f7ecbfdc | 20260827T144208Z | 2026-08-29 | untracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_closeout_drift_20260824T172353Z.json | DATA_BDINSURANCE | 1.0.0_SA_CTO | d9fff9a9c2 | 20260824T172353Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_closeout_drift_20260824T173514Z.json | DATA_BDINSURANCE | 1.0.0_SA_CTO | a6b91e8b78 | 20260824T173514Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_closeout_drift_20260824T182444Z.json | DATA_BDINSURANCE | 1.0.0_SA_CTO | ee2c15686f | 20260824T182444Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_closeout_drift_20260824T205737Z.json | DATA_BDINSURANCE | 2.0.0_SA_COO | b23bbe1f6d | 20260824T205737Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/DATA_BDINSURANCE_closeout_drift_20260827T144208Z.json | DATA_BDINSURANCE | 1.0.0_SA_CTO | e4f7ecbfdc | 20260827T144208Z | 2026-08-29 | untracked |
| org/critical_paths/.open_findings/DATA_PLATFORM_closeout_drift_20260806T235728Z.json | DATA_PLATFORM | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/DATA_SSOTMG_PRD_closeout_drift_20260806T235728Z.json | DATA_SSOTMG_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/DATA_SSOTMG_closeout_drift_20260806T235728Z.json | DATA_SSOTMG | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/DRFR_PTMCH_closeout_drift_20260806T235728Z.json | DRFR_PTMCH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ETFS_AVGCAP_closeout_drift_20260806T235728Z.json | ETFS_AVGCAP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ETFS_CANON_closeout_drift_20260806T235728Z.json | ETFS_CANON | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/ETFS_CANON_closeout_drift_20260824T193631Z.json | ETFS_CANON | 1.0.0_SA_CTO~Z | e2ba01dd27 | 20260824T193631Z | 2026-08-26 | tracked |
| org/critical_paths/.open_findings/ETFS_POSITIONING_PRD_closeout_drift_20260821T204943Z.json | ETFS_POSITIONING_PRD | 1.0.0_SA_CTO | 5a6433ce22 | 20260821T204943Z | 2026-08-23 | untracked |
| org/critical_paths/.open_findings/ETFS_POSITIONING_PRD_closeout_drift_20260824T143950Z.json | ETFS_POSITIONING_PRD | 1.0.0_SA_CTO | 78f24c2efc | 20260824T143950Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ETFS_POSITIONING_closeout_drift_20260821T055431Z.json | ETFS_POSITIONING | 1.0.0_SA_CTO~A | 12c6a5e1b6 | 20260821T055431Z | 2026-08-23 | untracked |
| org/critical_paths/.open_findings/ETFS_POSITIONING_closeout_drift_20260821T204943Z.json | ETFS_POSITIONING | 1.0.0_SA_CTO | 5a6433ce22 | 20260821T204943Z | 2026-08-23 | untracked |
| org/critical_paths/.open_findings/ETFS_POSITIONING_closeout_drift_20260824T143950Z.json | ETFS_POSITIONING | 1.0.0_SA_CTO | 78f24c2efc | 20260824T143950Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ETFS_POSITIONING_closeout_drift_20260824T155704Z.json | ETFS_POSITIONING | 1.0.0_SA_CTO | de481d0e06 | 20260824T155704Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ETFS_POSITIONING_closeout_drift_20260824T175033Z.json | ETFS_POSITIONING | 1.0.0_SA_CTO | 7c60531eb4 | 20260824T175033Z | 2026-08-26 | untracked |
| org/critical_paths/.open_findings/ETFS_POSITIONING_closeout_drift_20260824T193631Z.json | ETFS_POSITIONING | 1.0.0_SA_CTO~Z | e2ba01dd27 | 20260824T193631Z | 2026-08-26 | tracked |
| org/critical_paths/.open_findings/ETFS_POSITIONING_closeout_drift_20260826T192437Z.json | ETFS_POSITIONING | 2.0.0_SA_COO | 7c5c8b0570 | 20260826T192437Z | 2026-08-28 | untracked |
| org/critical_paths/.open_findings/ETFS_SATELLITES_closeout_drift_20260827T200447Z.json | ETFS_SATELLITES | 1.0.0_SA_CTO~Z | 4bbfda8ff8 | 20260827T200447Z | 2026-08-29 | tracked |
| org/critical_paths/.open_findings/ETFS_SATELLITES_closeout_drift_20260828T160055Z.json | ETFS_SATELLITES | 2.0.0_SA_COO~Z | b8d7f50017 | 20260828T160055Z | 2026-08-30 | tracked |
| org/critical_paths/.open_findings/ETFS_SETUP_closeout_drift_20260806T235728Z.json | ETFS_SETUP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/EXPAND_AUTHEDGE_closeout_drift_20260806T235728Z.json | EXPAND_AUTHEDGE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/EXPAND_MSCLOUD_closeout_drift_20260806T235728Z.json | EXPAND_MSCLOUD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/FIND_DUALBIZ_closeout_drift_20260806T235728Z.json | FIND_DUALBIZ | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/FIND_INSURE_closeout_drift_20260806T235728Z.json | FIND_INSURE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/HEATMAP_PROCESS_closeout_drift_20260806T235728Z.json | HEATMAP_PROCESS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDLP_DISTFIX_PRD_closeout_drift_20260806T235728Z.json | MDLP_DISTFIX_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDLP_DISTFIX_closeout_drift_20260806T235728Z.json | MDLP_DISTFIX | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDLP_WYNCHT_closeout_drift_20260806T235728Z.json | MDLP_WYNCHT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_3FIRMS_PRD_closeout_drift_20260806T235728Z.json | MDPF_3FIRMS_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_3FIRMS_closeout_drift_20260803T191419Z.json | MDPF_3FIRMS | 1.0.0_SA_CTO | c73a6e948b | 20260803T191419Z | 2026-08-05 | tracked |
| org/critical_paths/.open_findings/MDPF_3FIRMS_closeout_drift_20260805T175040Z.json | MDPF_3FIRMS | 1.0.0_SA_CTO | 8461f06958 | 20260805T175040Z | 2026-08-07 | tracked |
| org/critical_paths/.open_findings/MDPF_3FIRMS_closeout_drift_20260806T235728Z.json | MDPF_3FIRMS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_CANONICAL_PLATINUM_PRD_closeout_drift_20260806T235728Z.json | MDPF_CANONICAL_PLATINUM_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_CANPLAT_closeout_drift_20260806T235728Z.json | MDPF_CANPLAT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_CANRTE_closeout_drift_20260805T160703Z.json | MDPF_CANRTE | 1.0.0_SA_CTO | bc847cb8ff | 20260805T160703Z | 2026-08-07 | tracked |
| org/critical_paths/.open_findings/MDPF_CANRTE_closeout_drift_20260806T235728Z.json | MDPF_CANRTE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_CHANNEL_INDEPENDENCE_PRD_closeout_drift_20260806T235728Z.json | MDPF_CHANNEL_INDEPENDENCE_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_CHANNEL_INDEPENDENCE_closeout_drift_20260806T235728Z.json | MDPF_CHANNEL_INDEPENDENCE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_COTREMEDIATION_closeout_drift_20260826T192437Z.json | MDPF_COTREMEDIATION | 2.0.0_SA_COO | 7c5c8b0570 | 20260826T192437Z | 2026-08-28 | untracked |
| org/critical_paths/.open_findings/MDPF_COUNTS_PRD_closeout_drift_20260806T235728Z.json | MDPF_COUNTS_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_COUNTS_closeout_drift_20260806T235728Z.json | MDPF_COUNTS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_DEBTCLEAN_closeout_drift_20260806T235728Z.json | MDPF_DEBTCLEAN | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_GLOBAL_PRD_closeout_drift_20260806T235728Z.json | MDPF_GLOBAL_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_GLOBAL_closeout_drift_20260805T160703Z.json | MDPF_GLOBAL | 1.0.0_SA_CTO | bc847cb8ff | 20260805T160703Z | 2026-08-07 | tracked |
| org/critical_paths/.open_findings/MDPF_GLOBAL_closeout_drift_20260806T235728Z.json | MDPF_GLOBAL | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MDPF_REVAMP_closeout_drift_20260806T235728Z.json | MDPF_REVAMP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MKOV_DLYCLD_closeout_drift_20260806T235728Z.json | MKOV_DLYCLD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MKOV_RETFIX_closeout_drift_20260806T235728Z.json | MKOV_RETFIX | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/MKOV_TRSRCE_closeout_drift_20260806T235728Z.json | MKOV_TRSRCE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_AGENTBUS_closeout_drift_20260806T235728Z.json | NFRA_AGENTBUS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_AKPIPE_closeout_drift_20260806T235728Z.json | NFRA_AKPIPE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_C3MATERIALIZE_PRD_closeout_drift_20260828T051250Z.json | NFRA_C3MATERIALIZE_PRD | 2.0.0_SA_COO~X | 2130cc49e0 | 20260828T051250Z | 2026-08-30 | untracked |
| org/critical_paths/.open_findings/NFRA_C3MATERIALIZE_closeout_drift_20260828T051250Z.json | NFRA_C3MATERIALIZE | 2.0.0_SA_COO~X | 2130cc49e0 | 20260828T051250Z | 2026-08-30 | untracked |
| org/critical_paths/.open_findings/NFRA_CMTQUE_closeout_drift_20260806T235728Z.json | NFRA_CMTQUE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPASSURANCE_closeout_drift_20260806T235728Z.json | NFRA_COMPASSURANCE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPCLOSE_PRD_closeout_drift_20260806T235728Z.json | NFRA_COMPCLOSE_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPCLOSE_closeout_drift_20260806T235728Z.json | NFRA_COMPCLOSE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPDIFF_closeout_drift_20260806T235728Z.json | NFRA_COMPDIFF | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPDRIFT_closeout_drift_20260806T235728Z.json | NFRA_COMPDRIFT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPILERKIT_closeout_drift_20260806T235728Z.json | NFRA_COMPILERKIT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPLEARN_closeout_drift_20260806T235728Z.json | NFRA_COMPLEARN | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPPROOF_closeout_drift_20260806T235728Z.json | NFRA_COMPPROOF | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPROUTE_closeout_drift_20260806T235728Z.json | NFRA_COMPROUTE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPSIMILAR_closeout_drift_20260806T235728Z.json | NFRA_COMPSIMILAR | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPTEAM_closeout_drift_20260806T235728Z.json | NFRA_COMPTEAM | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMPTOOLS_closeout_drift_20260826T192437Z.json | NFRA_COMPTOOLS | 2.0.0_SA_COO | 7c5c8b0570 | 20260826T192437Z | 2026-08-28 | untracked |
| org/critical_paths/.open_findings/NFRA_COMPUNIFY_closeout_drift_20260806T235728Z.json | NFRA_COMPUNIFY | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COMP_closeout_drift_20260806T235728Z.json | NFRA_COMP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_COSTAWS_closeout_drift_20260806T235728Z.json | NFRA_COSTAWS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_CSE_closeout_drift_20260806T235728Z.json | NFRA_CSE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_DEBTSCAN_closeout_drift_20260806T235728Z.json | NFRA_DEBTSCAN | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_DEPLOYLEDGER_closeout_drift_20260826T192437Z.json | NFRA_DEPLOYLEDGER | 2.0.0_SA_COO | 7c5c8b0570 | 20260826T192437Z | 2026-08-28 | untracked |
| org/critical_paths/.open_findings/NFRA_DTAFLP_closeout_drift_20260806T235728Z.json | NFRA_DTAFLP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_EDGES_closeout_drift_20260806T235728Z.json | NFRA_EDGES | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_EXPAND_closeout_drift_20260806T235728Z.json | NFRA_EXPAND | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_FEDOBS_closeout_drift_20260806T235728Z.json | NFRA_FEDOBS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_GCONTR_closeout_drift_20260806T235728Z.json | NFRA_GCONTR | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_GENESIS_closeout_drift_20260806T235728Z.json | NFRA_GENESIS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_GLOBGRPH_PRD_closeout_drift_20260806T235728Z.json | NFRA_GLOBGRPH_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_GLOBGRPH_closeout_drift_20260806T235728Z.json | NFRA_GLOBGRPH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_GRAPHDEPTH_closeout_drift_20260806T235728Z.json | NFRA_GRAPHDEPTH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_GRAPHFEED_closeout_drift_20260806T235728Z.json | NFRA_GRAPHFEED | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_GRAPHS_closeout_drift_20260806T235728Z.json | NFRA_GRAPHS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_GRAPHUNI_closeout_drift_20260806T235728Z.json | NFRA_GRAPHUNI | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_INFRPT_closeout_drift_20260806T235728Z.json | NFRA_INFRPT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_INSTDRILL_closeout_drift_20260806T235728Z.json | NFRA_INSTDRILL | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_INTEGRATIONS_closeout_drift_20260806T235728Z.json | NFRA_INTEGRATIONS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_KUZUSPLIT_PRD_closeout_drift_20260806T235728Z.json | NFRA_KUZUSPLIT_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_KUZUSPLIT_closeout_drift_20260806T235728Z.json | NFRA_KUZUSPLIT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_KUZUSPLIT_closeout_drift_20260902T184721Z.json | NFRA_KUZUSPLIT | 1.0.0_SA_CTO~A | 52d14feb79 | 20260902T184721Z | 2026-09-04 | untracked |
| org/critical_paths/.open_findings/NFRA_LOCALROOT_closeout_drift_20260806T235728Z.json | NFRA_LOCALROOT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_MOTIF_closeout_drift_20260806T235728Z.json | NFRA_MOTIF | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_MSBEFF_closeout_drift_20260806T235728Z.json | NFRA_MSBEFF | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_MSGRAPH_closeout_drift_20260806T235728Z.json | NFRA_MSGRAPH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_NERVES_PRD_closeout_drift_20260806T235728Z.json | NFRA_NERVES_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_NERVES_closeout_drift_20260806T235728Z.json | NFRA_NERVES | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_NESTEDABSTRACT_closeout_drift_20260806T235728Z.json | NFRA_NESTEDABSTRACT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_ONTOLOGY_closeout_drift_20260806T235728Z.json | NFRA_ONTOLOGY | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_OPLMCP_closeout_drift_20260806T235728Z.json | NFRA_OPLMCP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_PASSCRAFT_closeout_drift_20260806T235728Z.json | NFRA_PASSCRAFT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_PIPELINE_closeout_drift_20260806T235728Z.json | NFRA_PIPELINE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_PIPESCRIPT_PRD_closeout_drift_20260806T235728Z.json | NFRA_PIPESCRIPT_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_PIPESCRIPT_closeout_drift_20260806T235728Z.json | NFRA_PIPESCRIPT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_PPLCOT_closeout_drift_20260806T235728Z.json | NFRA_PPLCOT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_PPLINF_closeout_drift_20260806T235728Z.json | NFRA_PPLINF | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_PROMOTE_closeout_drift_20260806T235728Z.json | NFRA_PROMOTE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_PSTMRT_closeout_drift_20260806T235728Z.json | NFRA_PSTMRT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_REPOCOHERENCEGRAPH_closeout_drift_20260805T011328Z.json | NFRA_REPOCOHERENCEGRAPH | 4.0.0_SA_CRO | 6143689ee6 | 20260805T011328Z | 2026-08-07 | tracked |
| org/critical_paths/.open_findings/NFRA_SUBSTRATECARDING_closeout_drift_20260826T192437Z.json | NFRA_SUBSTRATECARDING | 2.0.0_SA_COO | 7c5c8b0570 | 20260826T192437Z | 2026-08-28 | untracked |
| org/critical_paths/.open_findings/NFRA_SYSPARITY_closeout_drift_20260806T235728Z.json | NFRA_SYSPARITY | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_SYSTEM_closeout_drift_20260806T235728Z.json | NFRA_SYSTEM | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_TERRAFORM_closeout_drift_20260806T235728Z.json | NFRA_TERRAFORM | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_TOOLARCH_closeout_drift_20260806T235728Z.json | NFRA_TOOLARCH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_TOOLBHVR_closeout_drift_20260806T235728Z.json | NFRA_TOOLBHVR | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_TOOLCHECK_closeout_drift_20260806T235728Z.json | NFRA_TOOLCHECK | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_TOOLGRAPH_closeout_drift_20260806T235728Z.json | NFRA_TOOLGRAPH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_TOOLHEALTH_closeout_drift_20260806T235728Z.json | NFRA_TOOLHEALTH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_TSGRAPH_closeout_drift_20260806T235728Z.json | NFRA_TSGRAPH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_VELOCITY_CORE_closeout_drift_20260806T235728Z.json | NFRA_VELOCITY_CORE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_VELOCITY_ESTATE_closeout_drift_20260806T235728Z.json | NFRA_VELOCITY_ESTATE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_VELOCITY_closeout_drift_20260805T011328Z.json | NFRA_VELOCITY | 4.0.0_SA_CRO | 6143689ee6 | 20260805T011328Z | 2026-08-07 | tracked |
| org/critical_paths/.open_findings/NFRA_VELOCITY_closeout_drift_20260806T235728Z.json | NFRA_VELOCITY | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_WEBSITE_closeout_drift_20260806T235728Z.json | NFRA_WEBSITE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_WORLDMODEL_PRD_closeout_drift_20260806T235728Z.json | NFRA_WORLDMODEL_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_WORLDMODEL_closeout_drift_20260806T235728Z.json | NFRA_WORLDMODEL | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/NFRA_WORLDMODEL_closeout_drift_20260819T173932Z.json | NFRA_WORLDMODEL | 4.0.0_SA_CRO | ef191faedf | 20260819T173932Z | 2026-08-21 | tracked |
| org/critical_paths/.open_findings/NFRA_WORLDMODEL_closeout_drift_20260819T174315Z.json | NFRA_WORLDMODEL | 4.0.0_SA_CRO | f0b48b39b6 | 20260819T174315Z | 2026-08-21 | tracked |
| org/critical_paths/.open_findings/NFRA_WRKFLW_closeout_drift_20260806T235728Z.json | NFRA_WRKFLW | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_ADVIPOINTERS_closeout_drift_20260826T192437Z.json | OPAL_ADVIPOINTERS | 2.0.0_SA_COO | 7c5c8b0570 | 20260826T192437Z | 2026-08-28 | untracked |
| org/critical_paths/.open_findings/OPAL_ALERTS_closeout_drift_20260806T235728Z.json | OPAL_ALERTS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_ALTRESEARCH_closeout_drift_20260806T235728Z.json | OPAL_ALTRESEARCH | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_ASSETS_closeout_drift_20260806T235728Z.json | OPAL_ASSETS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_BBGTML_closeout_drift_20260806T235728Z.json | OPAL_BBGTML | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_CONSOLIDATION_PRD_closeout_drift_20260806T235728Z.json | OPAL_CONSOLIDATION_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_CONSOLIDATION_closeout_drift_20260806T235728Z.json | OPAL_CONSOLIDATION | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_GLDRNS_closeout_drift_20260806T235728Z.json | OPAL_GLDRNS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_KIMIPIPELINE_closeout_drift_20260806T235728Z.json | OPAL_KIMIPIPELINE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_LCLRPO_closeout_drift_20260806T235728Z.json | OPAL_LCLRPO | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_PRISTINE_closeout_drift_20260806T235728Z.json | OPAL_PRISTINE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_SCHEDULE_closeout_drift_20260806T235728Z.json | OPAL_SCHEDULE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_SQSCHAT_closeout_drift_20260729T180700Z.json | OPAL_SQSCHAT | 0.0.0_AB_MSTR~Z | 00dd8bd9a | 20260729T180700Z | 2026-07-31 | tracked |
| org/critical_paths/.open_findings/OPAL_SQSCHAT_closeout_drift_20260806T235728Z.json | OPAL_SQSCHAT | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_STNDRD_closeout_drift_20260806T235728Z.json | OPAL_STNDRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_TAXONOMY_closeout_drift_20260806T235728Z.json | OPAL_TAXONOMY | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_TAXSMA_PT2_closeout_drift_20260806T235728Z.json | OPAL_TAXSMA_PT2 | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_TAXSMA_REGISTRY_PRD_closeout_drift_20260806T235728Z.json | OPAL_TAXSMA_REGISTRY_PRD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_TAXSMA_REGISTRY_closeout_drift_20260806T235728Z.json | OPAL_TAXSMA_REGISTRY | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_TAXSMA_closeout_drift_20260806T235728Z.json | OPAL_TAXSMA | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_TAXSMA_closeout_drift_20260827T204847Z.json | OPAL_TAXSMA | 1.0.0_SA_CTO~Z | 33e2a64fa6 | 20260827T204847Z | 2026-08-29 | tracked |
| org/critical_paths/.open_findings/OPAL_TAXSMA_closeout_drift_20260827T205152Z.json | OPAL_TAXSMA | 1.0.0_SA_CTO~Z | a80424bc78 | 20260827T205152Z | 2026-08-29 | tracked |
| org/critical_paths/.open_findings/OPAL_TICKET_closeout_drift_20260806T235728Z.json | OPAL_TICKET | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/OPAL_VENDORPROVENANCE_closeout_drift_20260806T235728Z.json | OPAL_VENDORPROVENANCE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/PORTAL_AUTHHARD_closeout_drift_20260806T235728Z.json | PORTAL_AUTHHARD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/POSN_CUSTOM_closeout_drift_20260826T224955Z.json | POSN_CUSTOM | 1.0.0_SA_CTO~Y | 25b116f8ac | 20260826T224955Z | 2026-08-28 | untracked |
| org/critical_paths/.open_findings/POSN_TENANCY_closeout_drift_20260828T160055Z.json | POSN_TENANCY | 2.0.0_SA_COO~Z | b8d7f50017 | 20260828T160055Z | 2026-08-30 | tracked |
| org/critical_paths/.open_findings/SCTY_MCPGUARD_closeout_drift_20260806T235728Z.json | SCTY_MCPGUARD | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/SCTY_PREMCP_closeout_drift_20260806T235728Z.json | SCTY_PREMCP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/SXPL_RESTIN_closeout_drift_20260806T235728Z.json | SXPL_RESTIN | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/TRSB_LEDGER_closeout_drift_20260806T235728Z.json | TRSB_LEDGER | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/UIUX_DESIGN_closeout_drift_20260806T235728Z.json | UIUX_DESIGN | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/VELOCITY_CORE_closeout_drift_20260806T235728Z.json | VELOCITY_CORE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/VELOCITY_ESTATE_closeout_drift_20260806T235728Z.json | VELOCITY_ESTATE | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/WSE_COTMDL_closeout_drift_20260806T235728Z.json | WSE_COTMDL | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/YALP_CAUSAL_closeout_drift_20260806T235728Z.json | YALP_CAUSAL | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/YALP_CMASMP_closeout_drift_20260806T235728Z.json | YALP_CMASMP | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/YALP_MACROS_closeout_drift_20260806T235728Z.json | YALP_MACROS | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
| org/critical_paths/.open_findings/YALP_YCUTVR_closeout_drift_20260806T235728Z.json | YALP_YCUTVR | 2.0.0_SA_COO~Z | f123fbf6e | 20260806T235728Z | 2026-08-08 | tracked |
