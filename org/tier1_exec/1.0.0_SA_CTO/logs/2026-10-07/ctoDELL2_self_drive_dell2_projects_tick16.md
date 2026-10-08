# /self-drive dell2 projects -- tick 16 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work since tick 15 (@f17758a444), plus tick 16 (21:47Z). **state: ARMED**

## Scope state (21:47Z)

All 7 are active / EXECUTING (TCKT_VNEXT included). Sequence flags: NEEDS-SLOT on IRPT_CUSTDY and ADVI_COTBKF (the known tracker gap);
none on the others. Inbox: 0 unread.

**Portal DEV landed** at d1b21c970c (msg 1119): IRPT_CUSTDY 6d84304dcb and TCKT_VNEXT f7fa7fb187, on Andrew's "go with your rec". PROD
is untouched at b06863fe09.

## Calls closed and acts

| input | ruling or act | carrier |
|---|---|---|
| `~G2` 1082 (IB-pr-357 is the next irpt-ycharts-generate release) | First ruled one release carrying X-1 too (msg 1084). Wrong: the build follows staged pins (`~Y2` 1087). Corrected to a SPLIT: release 1 = IB-pr-357 and its riders; X-1 later with its repin | msgs 1084, 1089 |
| `~P2` 1094 (served.py builds its staged row, not HEAD) | YES to the one-row re-pin. It became release 1's pin (1b5afe6a49), and rider IB-pr-326 is named | msg 1096 |
| `~Y2` 1108 (release 1 pair @70ceca1611) | Not yet signable. Owed: `~P`'s reason that IB-pr-326 is safe plus the IB-pr-357 control; `~G2`'s publisher riders safe or pinned out; the pin on origin for the fitz relay | -- |
| `~D2` 1088 (pandas 2.2.3 for E2(1)) | E2(1) runs by laptop relay now; the kit goes through the package route | msg 1092 |
| CRO 1109 (Py3.12 kit intake @2e92f35a1e) | CTO APPROVES. Condition: the served layer's numpy and pyarrow versions confirmed by E2(1)'s relay | msg 1111 |
| `~P2` 1110 (IB-pr-356 portal b3fedfea) | PASS for DEV. W165-S1 (envelope validation) closes before PROD; W165-S2 (ARMED) disarms before the DEV push | msg 21:39Z |
| CVO 1099 (ADVI_COTBKF round 16) | Round 17 = flow timing, zero-amount transfers, page counts | @8b6829c89f |

**A ruling this seat corrected** (1084 to 1089): "any build ships both" was read from CLOUD HEAD, not from the build input, which is the
staged pins. This is rule 22a's own trap (diff deployed bytes against the BUILD INPUT). `~Y2`'s release-census caught it before any
signing.

## Acts only Andrew can do

1. **PROD promote** of the print page with the custody template, after W165-S1 closes.
2. The on-behalf filing entitlement (TCKT_VNEXT X-1).
3. The IB-pr-356 portal DEV landing (his word for portal landings).
4. Running the Python 3.12 installer elevated (msg 1005).
5. TCKT_VNEXT: confirming the DONE WHEN lines.
6. The PROD advisor hold; disclosure of the pre-fix export residual.
7. NFRA_TRNSPT: the 14 words, the second reader, Alyssa's corpus.
8. The ADVI_COTBKF near-match page to Cottonwood.
9. R13; FWD-17 to FWD-23.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- `release-census --pin` (`~Y2`, `~P2`) read the build input and corrected this seat's HEAD-based assumption twice.
- `sequence-check.py` x7 took over 500 s this tick; it was moved to the background.
