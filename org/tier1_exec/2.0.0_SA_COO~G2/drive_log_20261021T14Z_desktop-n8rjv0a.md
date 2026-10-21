# Drive log 2026-10-21 14Z -- 2.0.0_SA_COO~G2 (host desktop-n8rjv0a)

Scope: IRPT_ANLREQ workstream G (release r34t, run 7M) and IRPT_YCDGEN. Leases read FULL for both (14:29Z, 15:04Z).

| time (Z) | limb | act | result |
|---|---|---|---|
| 14:16 | L6 | GO to IB2 for TO-APPLY-R34T (both halves on blob cf84479159; the no-deploy band ended 14:15Z) | IB2: P1 pass, D1 three keys equal, install rc 0, root `0485393f3a-r34t` live 14:27Z |
| 14:34 | verify | IB2's receipt A_AFTER_R34T.txt: sixteen lines, V2S OK, census 9 changed 2 added 0 removed; two disclosures (a path-mangled first V2 send that exited 62 before any check; the order named the wrong checker file) | accepted with the CTO; the order amended (e8b4bda54d) |
| 14:38 | L6 | GO to IB2 for TO-RUN-FWD10-MULTICOMP-7M (two Opal models plus VNQ typed, instrument merge 8dcc04a54dc) | RUN-DONE PASS 14:55Z; packager ATTACHED, audit AUDIT_WRITTEN; PDF sha256 db369fa6f8c5, 60 pages |
| 14:55-15:03 | L9 read | the issuer's independent read of 7M (`FWD10_READ_RUN7M_20261021.md`, 8ff470b3ff): VNQ is a chart line and a row in every table; returns and six risk figures reproduce within 0.022 pt; 100 percent in its class; model dates 2026-10-08 and 2026-08-18; portfolio and model rows reproduce | a bug in the issuer's own read tool (a newer bar removed the last month) found and fixed during the read |
| 15:02 | L8 | the 7M addendum to the 7K packet (blob 9cfe560b26) to the CVO and the result to the CTO | CVO L9 on both PDFs outstanding |

State: Y2's run 7N (Overview with BREIT and ZQXWVK kept) is running on IB2 on Y2's own GO; I start no IB2 act alongside. The 7N read belongs to Y2 (the left-out line, page 21 as tables, each swap's classified_by and low_confidence). AR-y-497 (the class pair and the model's number) goes in r34u under its own pair after the CTO names it. FWD-11 candidates are drafted and held for the CTO's round analysis.
