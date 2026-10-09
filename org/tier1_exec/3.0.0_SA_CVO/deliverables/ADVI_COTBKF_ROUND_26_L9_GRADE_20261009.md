# ADVI_COTBKF round 26 -- L9 grades

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~03:0xZ. Drains a9aca322b9 and 718291c2c7.

| criterion | verdict | evidence |
|---|---|---|
| CB26z1-AC3: the ASF state and source decided before the run, from evidence printed by the census script | MET | the rule section precedes the census in `asf_source.md`; rule commit 422ae4888c (22:00 ET) precedes run d7c2fbf66b (22:12); NO-SOURCE rests on the printed rows (6, one account, net 0.00; 3 paired with ManAltF, 3 with nothing; 0 lines in the CRO's research) |
| CB26z2-AC3: rules printed before the counts; the denominator is the whole graded population; no month forced | MET | `nonmatch_census.md`: denominator 82,593 with sum_ok over 79,495 non-MATCH; the rule section and the 61-of-61 type map precede the class table; the census commit cd084bc838 (22:19) precedes the run 48cdd857cd (22:33); 512 left `unexplained`, named, not pushed into a class |
| CB26z3-AC2: each row's instrument run now, evidence measured | MET | `ENDPOINT_READ_20261009.md`: each of 9 rows names an instrument run in the task with rc and counts. This seat re-ran FWD-6's `commonwealth_coverage_statement.py` and got the identical line. FWD-3's NOT rests on a measured absence (no served daily returns) plus a stale local file named as stale |

CB26z2-AC2 (mechanical, `unexplained=512`) is closed graded NOT MET by CTO msg 2213. That clause is not mine to grade; the 512 carry
forward as D2-W48-S2.
