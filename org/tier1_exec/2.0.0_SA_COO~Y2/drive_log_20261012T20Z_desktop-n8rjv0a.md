# 2.0.0_SA_COO~Y2 drive log 2026-10-12 20Z-21Z (derived host)

| time | project | limb | round | TOs | cells | thread | act |
|---|---|---|---|---|---|---|---|
| 20:3xZ | IRPT_ANLREQ | seated on Andrew-direct "seat V2 and Y2 now"; /canonical-flow | r16 | 4/5 drained at seating; TO-AR-y-162 not spawned; TO-READS-Y7 pending at the laptop | 5/5 | n | Measured: PRD v0.4 ADMITTED (both halves SIGNED), lease FULL, no unfinished edits under the project, round 16 at the count. Laptop ~ANL had answered both reads: Y7_stored_input_count.json @49af906f74 (56 template inputs, 0 read differently, 0 turned back) and F2_synthetic_owner_count.json @b9cb3e0ff8 (33 reserved-domain requests, all class OPAL_GLOBAL, each with a retained original) |
| 20:4xZ | IRPT_ANLREQ | count to the CTO; spawn ruled; TO-AR-y-162 spawned | r16 | 4/5 -> 162 running (~52) | 5/5 | n | Count sent (CTO msg 6532: yes, spawn; no stored input needs a ruling). Spawn amendment @c6bcd3b427, cherry-picked onto wk-IRPT_ANLREQ-52 (636cebdc86; not a merge of box/dell2, which is 1908 commits ahead). Closed from-side of 0dce and 5414 |
| 20:5xZ | IRPT_ANLREQ | arm F2 settled and cut | r16 | TO-READS-Y8 pending at the laptop | - | n | The relay's "no record fits" was a reading of owner CLASS; owner_reads.py:28-31 compares the CALLER's class, so the 33 fit arm (b). CTO msg 6541: yes, WITH an existence control on the same record; msg 6544 signed the CTO half with two conditions (verdict OWNER_SCOPED_REFUSAL, a link in the control log is a STOP). Order TO-READS-Y8 @e1bd3b7d12, its check self-tested on eight synthetic results. T2 (NFRA_TRNSPT r24) asked for one REQ-hex id: cut as a CALL, answered (tenant cottonwood); then a second CALL for the record's ticket_id (@792cc3bfd6) |
| 21:0xZ | IRPT_ANLREQ | TO-AR-y-162 DRAINED | r16 | 5/5 builds terminal; Y7 complete; Y8 pending | 5/5 | n | Own runs on the worker tree: Y162-RELAND-OK (5 contract tests, 9 reader tests), Y162-KEEP-OK (311 passed, floor 292), proof VALID rc=0; diff read: read_input compares only on an equal reader version, an absent one reads as the version before, the original's digest is checked under both. Drain @aaf156e8eb (safe-merge, 12 files, 0 foreign). BUILT, NOT RELEASED. AC3J awaits the CVO. HELD-AT: Y8 result; the ticket_id answer |

## Compiler Tools

- A reading of the rule at the cited lines (owner_reads.py:28-31) changed a relayed "no record fits" into a runnable arm.
- Eight synthetic results run through the one check caught a verdict that did not follow from its arms and a link leaking into a result.
- A spawn amendment cherry-picked onto the worker's branch kept a 1908-commit trunk gap out of the worker's tree.
- Own defect this window: the crossbox ack line I gave was refused for format (the id must appear in a CROSSBOX-ACK line); the close still went through.
