# IRPT_ANLREQ round 41, workstream ~G (ENGINE) -- decomposition: read the pattern behind the WAF challenge on the upload door's lookup

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** FWD-1 run 3, SET 2 (AQ2 record `A_SET2_JOURNAL_R3.txt`): ZQXWVK's resolve was challenged on each of its four receives (`PROVIDER_READ_UNAVAILABLE:WAF_CHALLENGE`, then `RESOLVE_RETRY_EXHAUSTED`) after four resolves had answered. The issuer's read `R3_SET2_WAF_READ_20261016.md` (with its erratum: the door's lookup is SESSIONLESS, `acquire_sessionless`, an empty cookie jar, batch 72 item 12, so there is no session to refresh). CTO msgs 9422 and 9429 (revised): step 1, AQ2 reads the journal lines and the four uploads' finding rows; step 2, ONE cookieless lookup made the door's own way; if it answers CLEAN, the issuer cuts the resident change (WAF_CHALLENGE on the resolve hop backs off like BUSY with growing spacing, capped at 15 minutes total, the class named on each retry, then the row ends as today), in its own cell and pair; if it is still challenged, nothing is cut and the pattern goes to the CTO. Run 3 stays HELD.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **One script, one order.** `waf_lookup_probe.sh` (offline test 11 cases) reads the journal window (13:36Z to 13:45Z by default: session, capture, rotation, eviction and WAF lines and the unit's start time), the host's public address from the instance metadata, a busy guard (no lookup while the resident handled a message in the last 60 s), and makes ONE cookieless lookup in a transient unit with the service's user and environment. Not the stored session, not the provider lease.
- **The four uploads' finding rows** are read by AQ2 with its existing read path for those rows, by the upload ids in its own record `OBJECTS_WRITTEN_FWD1_R3.txt`; only finding codes and actions are recorded, no holding value.
- **The change cell is NOT cut here.** Its content is the finding (CTO msg 9429 steps 2 and 3).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-128` | one read-only record: the journal lines, the host address, the four rows' finding codes, and the verdict of ONE cookieless lookup (status, WAF action header, content type, bytes, body head) | the applier's `deliverables/irpt_anlreq_fwd1_r3/`, the order | WORLD (a production host is read; ONE request to YCharts's lookup route, as the door makes every upload; nothing written there but a temp file and one transient unit) |

## Edges and chains

- ONE chain. A resident change (if the lookup is clean) is cut AFTER this record.

## Four-postulate record

(i) Domain: one host, one unit, one lookup, one journal window, four rows. (ii) One probe, one record. (iii) One intent: say whether the challenge persists and what the host looked like to the WAF. (iv) What this cut does NOT move: the running root (r34e), S3, the Lambdas, the stored session, run 3's hold.

fanout: 1 of 1 chains, cap 8, reason: one applier read order (a CloudOps read, not a worker cell).
