# Deploy Completion Record
**Date opened:** 2026-10-19T14:28:52.284954+00:00
**Status:** CLOSED -- STOPPED AT U (five RESOLVING answers over 20 s, 0 RESOLVE journal lines, no input_id); 6 of 7 synthetic keys deleted and ABSENT; ONE LEFTOVER BLOB (the same original-holdings object as the previous run, delete AccessDenied, see surprise row IRPT_ANLREQ-D2-S214); 0 ticket, 0 request; closed 20261019T1436Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-3: the third ONE fresh synthetic commentary run end to end, the identical upload re-posted while RESOLVING (5 posts at most, 3 s apart), one synthetic staff user and one synthetic advisor, then delete by recorded key; COO half 394e573a4a plus ADDENDUMS 1 (02149564860) and 2 (5bddf32c3b); CTO halves fec24f492d and 57f931e207; nothing deployed
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | activation | mint the synthetic staff user and the synthetic advisor (users and partner rows) and record every key created | mint read-backs present | synthetic staff user and synthetic advisor (users and partner rows) minted once each, read-backs ok (2026-10-19T14:31:09Z); login ok | CLOSED 20261019T143755Z |
| S | activation | login, upload (re-posted while RESOLVING), ticket and submit | closed states and the REQ id | NOT RUN beyond the upload: the identical request was re-posted 5 times, 3 s apart, over 20 s (first post 14:31:14Z) and stayed RESOLVING; resident journal RESOLVE lines since the first post: 0 (journal window 1 line); STOP at U per the order; no ticket, no request created | CLOSED 20261019T143755Z |
| P | verify | poll job READY, commentary_ref, draft artifact, packager line, PDF artifact within 30 minutes | the hop results | NOT RUN: stopped at U; nothing to poll | CLOSED 20261019T143755Z |
| R | verify | the commentary-pdf route read as the same user | pass or the closed code | NOT RUN: stopped at U; no request, so no route read | CLOSED 20261019T143756Z |
| D | activation | delete exactly the recorded synthetic keys including the advisor rows, each read back ABSENT; the original-holdings blob per the AR-y-402 record | keys deleted of recorded | 6 of 7 recorded keys deleted and read ABSENT (staff user, advisor users and partner rows, the upload's three index rows); ONE leftover, the original-holdings blob (the same key as the 2026-10-17 run: same_art_key yes), delete AccessDenied, the AR-y-402 record W5 finds no deleter, so it is left and reported in surprise row IRPT_ANLREQ-D2-S214; Monday's advisor untouched; dead letter 1 before and 1 after | CLOSED 20261019T143756Z |

## Log

- 20261019T142852Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261019T143755Z LEG A closed: synthetic staff user and synthetic advisor (users and partner rows) minted once each, read-backs ok (2026-10-19T14:31:09
- 20261019T143755Z LEG S closed: NOT RUN beyond the upload: the identical request was re-posted 5 times, 3 s apart, over 20 s (first post 14:31:14Z) and 
- 20261019T143755Z LEG P closed: NOT RUN: stopped at U; nothing to poll
- 20261019T143756Z LEG R closed: NOT RUN: stopped at U; no request, so no route read
- 20261019T143756Z LEG D closed: 6 of 7 recorded keys deleted and read ABSENT (staff user, advisor users and partner rows, the upload's three index rows)
- 20261019T143756Z CLOSED -- all 5 legs proven
