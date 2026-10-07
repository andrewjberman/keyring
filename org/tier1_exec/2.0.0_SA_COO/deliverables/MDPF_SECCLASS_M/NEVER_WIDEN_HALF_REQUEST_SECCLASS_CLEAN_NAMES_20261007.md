# Never-widen half, MDPF_SECCLASS -- the clean names for the rows the table already holds (FWD-14, cell SC-e-34)

**Author:** `0.9.0_WK_MDPF_SECCLASS~28` for `2.0.0_SA_COO~M1`, 2026-10-07. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been written to any table. The writer refuses `--write` until both headings at the foot read SIGNED.
Spec: PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12 FWD-14 ("the name beside each holding is the shared list's clean, properly capitalized name"); addendum v0.7 (the rule applies to every row); contract precedence v0.4 C-WRITER ("a seed row always wins, and a correction is made in the seed source").

## The act (by the issuer, after both halves sign)

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/clean_name_write.py --write --half <this file> --snapshot <snapshot.json>`
- **The set:** `CLEAN_NAME_ROW_SET_20261007.tsv` (built by `R10_CHECKS/clean_name_row_set.py`, one consistent scan of `etf-classifications` on 2026-10-07, 3,507 rows). 883 rows carry a name:
  **WRITE 495** (`scheduled` 492, `legacy` 3), **SEED-SOURCE 33** (`seed`, listed below, NOT written to the table), **UNCHANGED 355** (the name already equals `security_name.clean_name(name)`).
  **2,624 rows carry no name** and are outside this cell: there is no source name in the table to case. Sourcing a name for them is a later decision, not a casing act. This request writes none of them.
- **Each WRITE** is ONE conditional `UpdateItem`: `SET name = :clean, updated_by = :by` with condition `name = :current` (the name the set recorded). A row that moved since the set was built is refused, reported, never overwritten; the rest continue.
  `:by` = `mdpf-secclass-clean-names`. No other attribute is touched; no row is created or deleted.
- **The function** is `infra/aws/lambda/v2_portal/_shared/security_name.py` `clean_name()` (cell SC-e-30), the only source of the clean string; the set is graded against it by `R10_CHECKS/sc_e34_row_set_check.py` (`CLEAN-NAME-SET ok=True rows=883 write=495 seed_source=33 unchanged=355 unnamed_live=2624 fails=0`).
- **Dry run** (read this session, `R10_CHECKS/clean_name_write.py` with no flag): `CLEAN-NAME-DRY-RUN write=495 seed_source=33 unchanged=355 refused_stale=0 puts=0` (the client is wrapped with a counter of every mutating call and the run asserts it is 0).

## Blast radius

One table, `etf-classifications`; the `name` and `updated_by` attributes of the 495 WRITE keys (count and list below). Nothing else on any row; no other table; no S3 object; no row created or deleted.
Rows by `classified_by`: scheduled 492, legacy 3, model 0 (every model row is unnamed), seed 0 (seed rows are never written here).

**WRITE keys (495):** ABB, AEO, ANF, BP, CADUX, CCEP, CGEMY, CMBKX, COBAX, COSIX, CUSIP:00130HCH6, CUSIP:002824BS8, CUSIP:00900W100, CUSIP:009CVR036, CUSIP:01179R4F7, CUSIP:014393YC0, CUSIP:020039DC4, CUSIP:023135BZ8, CUSIP:023551AM6, CUSIP:024071508, CUSIP:025083882, CUSIP:02630T712, CUSIP:02765UDX9, CUSIP:037833AT7, CUSIP:03843TAX9, CUSIP:042735AK6, CUSIP:049560AG0, CUSIP:052397J31, CUSIP:052398HW7, CUSIP:052414RA9, CUSIP:052414TX7, CUSIP:052477PH3, CUSIP:053015AJ2, CUSIP:05554TQJ7, CUSIP:05556NSE7, CUSIP:05612LBD3, CUSIP:05612LHJ4, CUSIP:05612LHS4, CUSIP:05949QAY1, CUSIP:060505104, CUSIP:06051X3R1, CUSIP:06051YAM2, CUSIP:06051YBM1, CUSIP:067167ZF6, CUSIP:06745PR94, CUSIP:067626KU4, CUSIP:073900X72, CUSIP:075896AA8, CUSIP:076059GK4, CUSIP:079860AK8, CUSIP:084538GV3, CUSIP:0882815C0, CUSIP:088281M72, CUSIP:09182TBT3, CUSIP:09290DAA9, CUSIP:102853GQ5, CUSIP:110122EH7, CUSIP:112097S43, CUSIP:116405XU0, CUSIP:117569LK7, CUSIP:12189TAJ3, CUSIP:12189TAR5, CUSIP:126408HM8, CUSIP:13376TBX2, CUSIP:139805CS2, CUSIP:140193103, CUSIP:140193780, CUSIP:14040HBN4, CUSIP:14042RVK4, CUSIP:159195ZA7, CUSIP:17239YLP5, CUSIP:181059ZV1, CUSIP:181234N35, CUSIP:18604TEB0, CUSIP:18605QCU5, CUSIP:186072TK0, CUSIP:187720F44, CUSIP:194469EA6, CUSIP:194469QX3, CUSIP:194748CH0, CUSIP:19648GZD7, CUSIP:19648GZE5, CUSIP:196707XS7, CUSIP:19765N278, CUSIP:19766P587, CUSIP:20030NCT6, CUSIP:20772J3W0, CUSIP:20772KFU8, CUSIP:2077583E1, CUSIP:20826FBJ4, CUSIP:208399W84, CUSIP:208418T37, CUSIP:208422KW4, CUSIP:213291QW0, CUSIP:220113LN2, CUSIP:220802AV4, CUSIP:225470VM2, CUSIP:227563QM8, CUSIP:232769QK8, CUSIP:2350365G1, CUSIP:23503CFQ5, CUSIP:235241SN7, CUSIP:235241TH9, CUSIP:240091LL0, CUSIP:241064EM2, CUSIP:245505XY3, CUSIP:248415YU9, CUSIP:24880SJM6, CUSIP:25434V401, CUSIP:283497U45, CUSIP:283822XR0, CUSIP:29270C2H7, CUSIP:29270C3B9, CUSIP:29270C6C4, CUSIP:2982635G5, CUSIP:302950407, CUSIP:30303M8T2, CUSIP:30382AJM5, CUSIP:312432H34, CUSIP:31421N402, CUSIP:316146356, CUSIP:316345206, CUSIP:31749TDB0, CUSIP:31925YDG4, CUSIP:31985HDE3, CUSIP:31986HAK1, CUSIP:32008F606, CUSIP:32056CAE9, CUSIP:32110YH99, CUSIP:335857EJ3, CUSIP:33737M300, CUSIP:33741X102, CUSIP:337738AU2, CUSIP:34115PBQ7, CUSIP:34153QXN1, CUSIP:34157REH9, CUSIP:34160KAN0, CUSIP:3431362G1, CUSIP:343137ER2, CUSIP:345370BP4, CUSIP:346766T99, CUSIP:34681XHN5, CUSIP:346905LN0, CUSIP:353496490, CUSIP:358776PU0, CUSIP:35880C7B4, CUSIP:3733846V3, CUSIP:376535803, CUSIP:380316AG4, CUSIP:38150V5M7, CUSIP:38151PCW9, CUSIP:38151PEN7, CUSIP:38151PET4, CUSIP:38151PFA4, CUSIP:38151PLX7, CUSIP:386442WS2, CUSIP:3954604V7, CUSIP:406450H58, CUSIP:41013MQP8, CUSIP:410223408, CUSIP:412295107, CUSIP:4140052R8, CUSIP:4140055E4, CUSIP:414009JS0, CUSIP:414009JT8, CUSIP:414009UA6, CUSIP:414205HV9, CUSIP:41420QJH2, CUSIP:41423PAQ0, CUSIP:41423PAR8, CUSIP:41423PAS6, CUSIP:414962RD4, CUSIP:414974FB6, CUSIP:421025DG9, CUSIP:42211HGY9, CUSIP:434207AA4, CUSIP:435475SM1, CUSIP:436146EN0, CUSIP:4423315E0, CUSIP:442368QB5, CUSIP:442403KY6, CUSIP:4424366D8, CUSIP:44244CS32, CUSIP:443510AH5, CUSIP:447290DM6, CUSIP:450812Q96, CUSIP:45204ELJ5, CUSIP:453320103, CUSIP:458140BH2, CUSIP:46613P3G9, CUSIP:466247ZR7, CUSIP:46659CHT0, CUSIP:480256EB8, CUSIP:48134XQ99, CUSIP:486053CM1, CUSIP:486053CP4, CUSIP:4860632S8, CUSIP:495242N54, CUSIP:51166FCK3, CUSIP:51166FFB0, CUSIP:516824NX3, CUSIP:52109HRX3, CUSIP:521769DQ9, CUSIP:521854CH0, CUSIP:52471R630, CUSIP:527843BP0, CUSIP:532457AZ1, CUSIP:5380366N9, CUSIP:5380366P4, CUSIP:543916688, CUSIP:54422NHH2, CUSIP:54811BSM4, CUSIP:549271AF1, CUSIP:554479FC4, CUSIP:56065GDH8, CUSIP:56167N274, CUSIP:57325VAM1, CUSIP:574193TW8, CUSIP:574193VF2, CUSIP:57429NCH3, CUSIP:57587GZM0, CUSIP:58178CDN4, CUSIP:592112YW0, CUSIP:59333AGU9, CUSIP:59334DKH6, CUSIP:59334DPD0, CUSIP:603827WS1, CUSIP:60534TLN3, CUSIP:60534WYU6, CUSIP:60637AVY5, CUSIP:61075TQX9, CUSIP:611530DC7, CUSIP:61370NLG6, CUSIP:61371AWR7, CUSIP:61372GFX9, CUSIP:61690U3L2, CUSIP:61746BCY0, CUSIP:61756E784, CUSIP:61768E3Z4, CUSIP:61768E7D9, CUSIP:61768EQQ9, CUSIP:61768EQT3, CUSIP:61776M6X8, CUSIP:61778K2Z9, CUSIP:643822828, CUSIP:645424AQ5, CUSIP:646039YQ4, CUSIP:64966QJ35, CUSIP:64971XB98, CUSIP:64971XDK1, CUSIP:64972GEU4, CUSIP:64990ASU0, CUSIP:650036BW5, CUSIP:65829QCZ5, CUSIP:65829QEA8, CUSIP:662832HM9, CUSIP:662832LX0, CUSIP:662842NA7, CUSIP:66285WM78, CUSIP:66285WT48, CUSIP:662903WT6, CUSIP:66476QFV5, CUSIP:666495AY2, CUSIP:670386RC7, CUSIP:67180K205, CUSIP:675561CL6, CUSIP:677523DJ8, CUSIP:677523KD3, CUSIP:67765QTH9, CUSIP:678514EP1, CUSIP:678688KX9, CUSIP:67884GWN0, CUSIP:679111XT6, CUSIP:679111YY4, CUSIP:67919PPD9, CUSIP:681725NC7, CUSIP:68609UWD3, CUSIP:693390882, CUSIP:69349LAR9, CUSIP:695114CD8, CUSIP:696878EW3, CUSIP:704223205, CUSIP:70879QTZ6, CUSIP:712303CK0, CUSIP:715ESC026, CUSIP:7170874Z0, CUSIP:718172DB2, CUSIP:726547CS9, CUSIP:727199K26, CUSIP:73105VBL5, CUSIP:733420HZ9, CUSIP:734122CP7, CUSIP:73412PBV4, CUSIP:736278KJ0, CUSIP:740614DX7, CUSIP:742718CB3, CUSIP:74440Y801, CUSIP:746802800, CUSIP:74913G881, CUSIP:749685AV5, CUSIP:749685AX1, CUSIP:754730AG4, CUSIP:755791EK2, CUSIP:756109CE2, CUSIP:76720AAS5, CUSIP:767278JF2, CUSIP:77316QE96, CUSIP:774280W56, CUSIP:774286BA5, CUSIP:779699JH1, CUSIP:78433H675, CUSIP:786514AS8, CUSIP:79623PFN0, CUSIP:79623PKA2, CUSIP:7962535T5, CUSIP:799561JN6, CUSIP:80586AAU5, CUSIP:808516108, CUSIP:808516306, CUSIP:808516702, CUSIP:808516801, CUSIP:809545WJ1, CUSIP:812643C77, CUSIP:812643UP7, CUSIP:833209LX5, CUSIP:833240HJ6, CUSIP:83748CAZ9, CUSIP:842400HQ9, CUSIP:845080JG6, CUSIP:845437BR2, CUSIP:853207AN8, CUSIP:858620Z83, CUSIP:867344AM5, CUSIP:876387EP2, CUSIP:87638QQG7, CUSIP:880591DX7, CUSIP:881685BB6, CUSIP:881797AG9, CUSIP:881847VA2, CUSIP:88213AKW4, CUSIP:88213AKY0, CUSIP:882669BG8, CUSIP:88269ACU0, CUSIP:8827236V6, CUSIP:8827242G1, CUSIP:882750NR9, CUSIP:8827567X1, CUSIP:88278PYM0, CUSIP:882806GR7, CUSIP:882830BR2, CUSIP:88579EAC9, CUSIP:887772DF5, CUSIP:89214A102, CUSIP:892778UG4, CUSIP:89439YDU0, CUSIP:895272EZ1, CUSIP:89602HGC5, CUSIP:899645G74, CUSIP:899656WA6, CUSIP:902307JL2, CUSIP:902307JM0, CUSIP:909218125, CUSIP:90983WCD1, CUSIP:912797RG4, CUSIP:912797UE5, CUSIP:912797VH7, CUSIP:912810QA9, CUSIP:912810QT8, CUSIP:912828U24, CUSIP:91282CEP2, CUSIP:91282CFM8, CUSIP:91282CFV8, CUSIP:91282CFZ9, CUSIP:91282CHT1, CUSIP:91282CHW4, CUSIP:91282CJA0, CUSIP:91282CJC6, CUSIP:91282CJK8, CUSIP:91282CJN2, CUSIP:91282CJT9, CUSIP:91282CKE0, CUSIP:91282CKZ3, CUSIP:91282CLF6, CUSIP:91282CLU3, CUSIP:91282CLY5, CUSIP:91282CME8, CUSIP:91282CMH1, CUSIP:91282CMN8, CUSIP:91282CMP3, CUSIP:91282CMY4, CUSIP:91282CNL1, CUSIP:91282CNT4, CUSIP:91282CQH7, CUSIP:91282CQJ3, CUSIP:91282CRF0, CUSIP:91282CRL7, CUSIP:9128334Y3, CUSIP:914354AC9, CUSIP:9144025Z1, CUSIP:91514AEL5, CUSIP:91514AJU0, CUSIP:920494FG1, CUSIP:92202E508, CUSIP:922908512, CUSIP:922908629, CUSIP:922908678, CUSIP:922908751, CUSIP:92343VHF4, CUSIP:92778UAZ3, CUSIP:92778VJG4, CUSIP:932449CN9, CUSIP:938688ZM3, CUSIP:93974D6H6, CUSIP:93974DX52, CUSIP:93974DXD5, CUSIP:93974DY69, CUSIP:93974E6J0, CUSIP:93974FEH2, CUSIP:949764SJ4, CUSIP:949764XN9, CUSIP:949797AA2, CUSIP:95000U2D4, CUSIP:953086NM3, CUSIP:969078TT1, CUSIP:97112AEA2, CUSIP:974433JM7, CUSIP:976656BW7, CUSIP:976656CE6, CUSIP:976826BQ9, CUSIP:97705MN27, CUSIP:98389BAV2, CUSIP:984121CL5, CUSIP:98851WBW2, CUSIP:98970LTE3, DSCLX, DSL, EQNR, ETIRX, FIMKX, FLRN, FM, GIBIX, GIGB, GSK, HES, HHHFX, IGIB, IGLB, IPG, IUSB, JHBSX, JMSIX, JPIE, KOS, MADCX, MMS, MPLX, MRBFX, MRU, MSTRX, MTB, MUOIX, NEFZX, NEWFX, NFFFX, NGG, NRSRX, NULG, NULV, ODVIX, ONIAX, OSK, PCOFX, PGBOX, PIMIX, PIPNX, PLFDX, PONAX, PONPX, PPHPF, RBGLY, RRX, SCGB1, SNAP, SOFIX, SPAB, SWAGX, TOELY, TSBRX, VALE, VBTIX, VWAGY, WDS, WMG, WTW

## The SEED-SOURCE list, 33 rows, for the seed source's owner

A `seed` row always wins and its correction is made in the seed source. Cell `SC-e-21` owns `infra/aws/lambda/v2_portal/_shared/etf_classification.py` this round; this worker does not edit it and writes none of these keys. The owner decides the spelling; the third column is what `clean_name()` returns today.

| key | seed source name today | clean_name() |
|---|---|---|
| AAETX | AMERICAN FUNDS 2030 TRGT DATE RETIRE A | American Funds 2030 Trgt Date Retire A |
| ACSG | ACSG | Acsg |
| AMECX | AMERICAN FUNDS INCOME FUND OF AMER A | American Funds Income Fund Of Amer A |
| BSCN | BSCN | Bscn |
| CAIBX | AMERICAN FUNDS CAPITAL INCOME BLDR A | American Funds Capital Income Bldr A |
| CFIHX | AMERICAN FUNDS CAPITAL INCOME BLDR F3 | American Funds Capital Income Bldr F3 |
| CLBAX | AMERICAN FUNDS AMERICAN BALANCED 529A | American Funds American Balanced 529A |
| DFAC | DFAC | Dfac |
| EVNT | EVNT | Evnt |
| FBALX | FIDELITY BALANCED | Fidelity Balanced |
| FKIQX | FRANKLIN INCOME A | Franklin Income A |
| FTYPX | FIDELITY FREEDOM INDEX 2055 PREMIER | Fidelity Freedom Index 2055 Premier |
| GARP | GARP | Garp |
| IBND | IBND | Ibnd |
| IXJ | IXJ | Ixj |
| JMUB | JMUB | Jmub |
| JPEM | JPEM | Jpem |
| JPMI | JPMI | Jpmi |
| KAGIX | KENSINGTON DYNAMIC ALLOCATION INST | Kensington Dynamic Allocation Inst |
| LDUR | LDUR | Ldur |
| MDLOX | BLACKROCK GLOBAL ALLOCATION INV A | Blackrock Global Allocation Inv A |
| MDY | MDY | Mdy |
| MRSIX | MRSIX | Mrsix |
| PAAA | PGIM AAA CLO ETF | Pgim Aaa Clo ETF |
| SCHB | SCHB | Schb |
| SGIIX | FIRST EAGLE GLOBAL I | First Eagle Global I |
| SHV | SHV | Shv |
| SMDV | SMDV | Smdv |
| SPLG | SPLG | Splg |
| STIP | STIP | Stip |
| SYLD | SYLD | Syld |
| VTTHX | VANGUARD TARGET RETIREMENT 2030 FUND | Vanguard Target Retirement 2030 Fund |
| WMT | WMT | Wmt |

(The other 164 `seed` rows already carry mixed-case names and read UNCHANGED.)

## Readers that print the name

- **Named from the repo:** `data/etfs/scripts/gold/etf_positioning_publisher.py` `_display_name(ticker, raw)` -- "PRECEDENCE: registry `name` -> the INCOMING issuer string -> None. Never the ticker" -- reads the table's `name` through `ETFClassifier` (`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`). After the act it serves the clean string for the 495 keys, at its next run.
  The Black Diamond and Cottonwood gold `etf_classifier.py` read the row for its class and state that the name is never consulted for classification (SC-t-1).
- **Not named, and not claimed:** every portal page or other producer that reads the table's `name` through a path this worker did not trace (the Holdings producers of the three firms, the portal's Positioning and Attribution pages, the investor-reporting ETF comparison). A reader that matches a holding by its name string, rather than by key, would see the change and this worker cannot rule that out from the repo. The issuer reads this limit at signing.
- **Writers of `name` not counted here.** This worker counted the readers it names, not the N writers of the `name` attribute; the signing seats count them and read each rule (the `scheduled` and `seed` rows' own writers) before signing. Whether a later scheduled run re-puts a name on a `scheduled` row is NOT verified by this worker.

## Rollback per key

The snapshot (`--snapshot`, written before the first update) holds each WRITE key's full pre-state item. `clean_name_write.py --rollback <snapshot.json> --write` puts each key's `name` (and the prior `updated_by`, or removes it if the row had none) back by a conditional update, only where the row still reads `updated_by = mdpf-secclass-clean-names` and `name` = the clean name. A row changed by another writer since is skipped and reported. The dry-run form of `--rollback` lists what it would restore.

## What this worker flags about the function's output (surprise row `MDPF_SECCLASS-W28-S5`)

`clean_name()` title-cases every all-capitals name token by token, so an acronym or a ticker used as a name is mis-cased: `BP PLC` -> `Bp Plc`, `GSK PLC` -> `Gsk Plc`, `MPLX LP` -> `Mplx Lp`; and the 33 SEED-SOURCE rows whose seed name is the ticker itself read `WMT` -> `Wmt`, `SPLG` -> `Splg`. Small words read `Of`, `Na`. This request writes the function's output as specified; the signing seats may hold the three legacy and the listed acronym-shaped scheduled rows pending a rule change in `security_name.py` (cell SC-e-30's file, not edited here).

## COO half -- UNSIGNED

(`2.0.0_SA_COO` signs here after reading the set, the dry-run line, the readers section and the writers count. Blast radius, writers counted both branches and the rollback per key are named above.)

## CTO half -- UNSIGNED

(`1.0.0_SA_CTO` signs in his own file and this heading records it, as for the multi-asset remap.)
