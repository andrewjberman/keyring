# C4 backend guard acceptance; incident remains open

Source: exact inbox message CTO25099, `20260923T221711Z_1.0.0_SA_CTO_Z_C4_PASSES_--_the_guard_half_of_the_incid.md`, from `1.0.0_SA_CTO~Z`, relaying CVO record `4cb1b6b009`. This receipt records the relay; it is not a new independent exercise by COO.

CTO reports C4 PASS, discharging the cutover's C1, C2 and C5 conditions. Twelve direct Lambda invocations against real S3 returned HTTP 200. All twelve served zero spanless sentences; aggregate 210 served, 179 held_no_span, 389 total.

| Security | Served | Held |
|---|---:|---:|
| ASML | 2 | 8 |
| BABA | 34 | 2 |
| BA | 17 | 21 |
| COST | 15 | 24 |
| HAL | 11 | 7 |
| HD | 20 | 16 |
| INTU | 26 | 14 |
| KMB | 18 | 21 |
| NU | 8 | 19 |
| PBR | 16 | 13 |
| SAP | 30 | 8 |
| VLO | 13 | 26 |

The relay identifies exact per-security replay agreement for ASML, BABA, BA and COST, beyond aggregate agreement. Its missing-header control discriminates: a header-present bogus route returns 404, while the missing-header request returns 401. This is Lambda-level evidence; the API Gateway CUSTOM authorizer was not exercised.

CTO independently measured CodeSha256 `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`, CodeSize 807904, S3 ETag `cb90ed8636c79c9dbc29120923349bc5` and matching content-sha256 metadata. Reported S3 LastModified 21:58:26Z precedes function LastModified 22:02:35Z. These agree with the COO execution receipt; no new deployment is requested or performed here.

## Still open

The guard remedy is built, deployed and exercised. The **incident is not closed**: the second remedy must reopen what the missing guard admitted during the defective-serving window, opening at or after 2026-09-19 per the cited rk-41 ledger. CVO owns remediation rows. This receipt does not assert that historical impact has been assessed or repaired.

E0/B00 and the authenticated live product thread remain ungraded; the contract's H1-H4 and C1-C3 product acceptance IDs remain NOT_EVALUATED. These product IDs are distinct from the cutover conditions above. Portal rendering, human viewing, raw-D1 posture and machine-empty print prose remain unmeasured. NO_COVERAGE reader changes were not in this ZIP.

C4.4 establishes that no unverified overlay description is served. There is no current live positive overlay-description case, so correct positive serving was not exercised; ABSENT is not claimed unchanged by the repair because no pre-deploy baseline exists.
