# Deploy Completion Record
**Date opened:** 2026-10-01T08:40:04.560825+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T084835Z
**Deploy:** Hop 3 diagnostic: TWO shape-only ticker lookups on the resident host (with the session through the provider lease, then with no session); CTO rulings batch 72 item 11 is the CTO half; COO half: this entry, script lookup_shape_host.sh sha256 aea1b451ebb8da5bea68ff956efa89d753a0e2865b6482d2a42bd67e21e2b750
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | exactly two GETs of securities_info for AAPL and VNQ, solo gate first, no sign-in reachable, no retry | both verdict lines by name with each answer's status, content type, WAF action and login flag; the output read for values before commit | exactly two GETs at 08:42:27Z-08:42:31Z, solo gate clean first; WITH_SESSION_VERDICT=ACCEPTED and NO_SESSION_VERDICT=ACCEPTED: each 200 application/json, no WAF action, not a login page, 695 bytes, AAPL and VNQ FOUND; output scanned clean before commit; HOP3/LOOKUP_SHAPE_OUTPUT_20261001.txt | CLOSED 20261001T084834Z |
| L2 | verify | no residue | both queues 0/0; the stored session's last-changed date unchanged by the script; no capture line in the resident journal | irpt-generation 0/0 and irpt-generation-dlq 0/0; stored session last changed 2026-10-01T08:21:20Z, unchanged; no capture, eviction or resolve line in the resident journal since 08:40Z | CLOSED 20261001T084834Z |

## Log

- 20261001T084004Z OPENED by 2.0.0_SA_COO~Y with 2 leg(s)
- 20261001T084834Z LEG L1 closed: exactly two GETs at 08:42:27Z-08:42:31Z, solo gate clean first; WITH_SESSION_VERDICT=ACCEPTED and NO_SESSION_VERDICT=ACC
- 20261001T084834Z LEG L2 closed: irpt-generation 0/0 and irpt-generation-dlq 0/0; stored session last changed 2026-10-01T08:21:20Z, unchanged; no capture
- 20261001T084835Z CLOSED -- all 2 legs proven
