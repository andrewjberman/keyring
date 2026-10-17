# Andrew-direct 2026-10-17 ~00:55Z, at the 2.0.0_SA_COO~S1 terminal (dell1)

VERBATIM, one message:

> use the biggest lambad memory possible should be 10gb or so

**Recorded by:** 2.0.0_SA_COO~S1, 2026-10-17T00:56:12Z (terminal, no broker channel).

**Reading taken (the issuer's, stated to Andrew in the reply):** the lambda in question is the access door `globgrph-trino-access-lambda`, whose `derive_silver` ran out of memory at 1024 MB and was raised to 6144 MB at 00:07Z. The AWS Lambda maximum is 10240 MB (10 GB), so the door's
`memory_size` becomes 10240. The collector (`m365-metadata-trino-collector-lambda`, 512 MB, peak use 120 MB) is NOT changed: it is not memory-bound, and the issuer does not widen Andrew's word to a function it did not name. Asked in the reply if he wants it raised too.

**Carried by:** TO SOC2_MSLOGS.TO-SM-r1 item 7e (seat 0.7.0_AE_CloudOps~SOC21); check `s1_check_a1.py tf` requires memory_size 10240.
