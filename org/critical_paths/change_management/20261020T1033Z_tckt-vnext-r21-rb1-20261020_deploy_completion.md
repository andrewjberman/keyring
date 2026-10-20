# Deploy Completion Record
**Date opened:** 2026-10-20T10:33:30.614266+00:00
**Status:** CLOSED -- REFUSED BY GATE, nothing created -- closed 20261020T123913Z
**Deploy:** TCKT_VNEXT TO-R21-RB1 (GO msg 11305, CTO round-20 analysis msg 11235): ONE PROD attempt of the Trade attachment BYTE READ-BACK on https://opalinvest.dev: one synthetic internal filer files one Trade Request with one invented csv, opens the attachment (listener registered before the press), downloads the Open body url with a plain GET, sha256 read equals sha256 uploaded; ticket and filer row deleted by key; the object STAYS as a fourth residue; surfaces: opal-tickets, opal-users-v2, s3 opal-data-cottonwood trade-form prefix (one object created, none deleted); check 9167d289eb
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | check-inbox, census, PROD head and CI, site 200, DT and CTO and IB2 and Y2 asked, filer row and ticket ABSENT, prefix count, protected tickets present | all true and printed |  | OPEN |
| O1 | verify | offline proof writing NOTHING: stub of the Open body shape and four earlier shapes, one read-only GET of a residue object at its version equals the known sha256, listener registered BEFORE the Open press | all three printed | OFFLINE-PROOF OK (10:36Z, nothing written; deliverables/r21_trade_prod/offline_proof_output.txt): (1) parser against stubbed bodies: {expires_in, filename, url} READ; four earlier shapes (data.url, attachment.url, items[].download_url) READ; no url REFUSED; non-S3 url REFUSED; other bucket's url REFUSED. (2) read-only GET of the residue object (key .../8b46f05593e643f0bb229023841d2a4a/tckt-r20-trade-synthetic.csv, version U2wA9rMN_iqdUnci740XcsAfyvgsTK3h) under own read rights: 31 bytes, sha256 f3e8bf44f4d910ebc27f49354d326787056293ff66a405b2c35c8bad3d31fa42 equals the known file. (3) listener before the press: r21_trade_prod.py line 369 page.expect_response(...) precedes line 371 click_locator.click() inside open_and_capture(); a stubbed page answering at once was driven through that same function and the early response was captured (200, key names [expires_in, filename, url]). | CLOSED 20261020T103727Z |
| F1 | activation | filer files ONE Trade Request with ONE csv on PROD; shots prod_trade_form_filled and prod_trade_filed | three HTTP statuses, ticket id and object key printed, no engine call |  | OPEN |
| R1 | verify | Open pressed with the listener registered; body key names printed; url downloaded with a plain GET | sha256 read equals sha256 uploaded |  | OPEN |
| D1 | verify | after the last exp: ticket item saved whole, then ticket and filer row deleted by printed key; object NOT deleted | ticket and row ABSENT by a 404 only; four residue objects named with key and version |  | OPEN |
| V1 | verify | r21_tradejourney_check.py with its self-test printed beside the verdict | RUN-OK (tradejourney) |  | OPEN |

## Log

- 20261020T103330Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
- 20261020T103727Z LEG O1 closed: OFFLINE-PROOF OK (10:36Z, nothing written; deliverables/r21_trade_prod/offline_proof_output.txt): (1) parser against stu
- 20261020T123913Z CLOSED -- REFUSED BY GATE before apply, world untouched: NOT STARTED, closed per COO AMENDMENT 3 (CTO note msg 11344) before the ledger's 3.0 h window reads RED at 13:33Z; the start waits for 14:15Z AND 2.0.0_SA_COO~Y2's word that IRPT_ANLREQ run 7 is terminal (AMENDMENT 2, CTO ruling 11330). Refusals: 'hold --pre-apply' REFUSED because leg O1 (the offline proof, which writes nothing) carries proof; plain 'hold' REFUSED because the apply leg F1 is open.
