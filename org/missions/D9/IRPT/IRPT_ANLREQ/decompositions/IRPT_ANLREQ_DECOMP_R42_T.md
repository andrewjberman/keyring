# IRPT_ANLREQ -- decomposition, round 42, workstream T (issuer 2.0.0_SA_COO~T2)

**Input:** the first live run of the commentary arm, measured by the issuer 2026-10-15 ~18:3xZ. `outlook-global-commentary-draft-lambda` ran once at 17:00:52Z (FWD-1 window 2, request
`REQ-d47252fe74634d0c5cdd8067`, tenant 49financial): 62.5 s, 98 MB, no exception; the draft store's `get_ref` answers OK with `commentary_ref` `ART-229ea94e..` (a draft was stored, `~Y2` msg 8551);
`~AQ2`'s host read shows the resident's packaging refused afterwards (a separate cause, `AR-y-357`). The function logged NO application line, so the proof the PRD and the TR-dp-24 packet name, the
`COMMENTARY-POST` line, cannot be read, and `post_census.py --live` reads `lines=0` for a run that did post or try to.

**The cause, from source:** `lambda_handler.py` logs through `LOG = logging.getLogger(__name__)` at INFO (`LOG.info("COMMENTARY-POST ...")`, `lambda_handler.py:~351`), and nothing in the handler, `entry.py` or `ticket_client.py`
sets a level (grep for `basicConfig` and `setLevel` over the three: no hit); the function's logging config is `Text` format with no application level. The Python Lambda root logger defaults to WARNING, so INFO is dropped.
The existing tests (`test_commentary_route_switch.py:50`) wrap the call in `caplog.at_level(logging.INFO, logger=lh.LOG.name)`, which sets the level for the test and so cannot see the defect.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-t-32` | the read above | `lambda_handler.py` sets its module logger to INFO at import, so its INFO lines (`COMMENTARY-POST`, `commentary draft stored`) reach the platform handler; a new test file proves it WITHOUT any test-side level override and proves the POST line is emitted at the module's own level. Fakes only. The deploy rides the deploy cell of the figures change. | `data/transcripts/scripts/commentary/lambda_handler.py`, `data/transcripts/scripts/tests/test_commentary_logging.py` (new) | LOCAL |

## Not cells

- The deploy (WORLD, a pair and an applier): one deploy cell after this and `AR-t-31`, so the function changes once.
- Why the resident refused to package the stored draft: `AR-y-357` (`~Y2`'s).
- Whether the ticket holds the draft: unread from here (needs the front door); the log fix makes the next run say it.

## Edges and chains

- One cell. M = 1. It is a DIRECT-ACT cell (about 20 product lines, LOCAL): one worker, one real run at the drain.

fanout: 1 of 1 chains, cap 8, reason: one direct-act cell on a disjoint write set.
