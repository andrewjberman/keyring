# 3.0.0_SA_CVO~Z -- work log 2026-09-04 00:00-00:30Z: the grant that never names the thing

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake. **Prior log:** `2026-09-03/work_2230-2340Z_*`. **Push state:** local HEAD
1b2065e765; `origin/SITEZ` read 001709c96e at 23:40Z and NOT re-read here, so **UNREAD at this vintage**.
**Channel:** 106 rows at the open, **111 at the close**, 35 this seat's.

## 1. Z-S107 corrected this seat's Z-S105, and the mechanism is worse than the number

**Z-S105 said the JWT-key rotation surface was bounded above by 25 across two granting roles. It is 31 across
FIVE.** `0.7.0_AE_CloudOps~V` censused all 221 roles with `get-account-authorization-details`, expanding
wildcards on both action and resource -- one call.

⛔ **MY PROBE COULD NOT HAVE FOUND THE OTHERS.** I derived the granting set from a literal-string `comp-find`
for `jwt-public-key` across terraform. `lambda-edge-execution-role` grants the read on the **prefix wildcard
`opal/auth/*`**, a statement that grants it and **contains no occurrence of the token I searched for**. A false
absence from a matcher that could not match -- not a coverage gap -- and nothing in my row disclosed the limit
because I did not know I had it. **And the role I missed carries `auth-validator-edge`, one of the two
consumers the face already named**, so the bound I published excluded a component that was in scope from the
start.

⛔ **THE SHAPE IS THE ONE MY OWN ROW WAS ABOUT, ONE LEVEL UP.** Z-S105 corrected a face for reading two
FUNCTIONS while the capability sat on the ROLES beneath them, and quoted Rule 22's shared-dependency clause.
I then read two ROLES and never censused the GRANTING SET. **The clause's own remedy is the step I skipped:
after the scoped pass, re-read the population UNSCOPED once.**

⚠ **And I guarded the wrong direction, carefully.** Z-S105 insists "a grant is not a reader", refuses to
promote 25 into a count, and *clears* two hits as comments so the bound is not inflated -- every control aimed
at OVERSTATING. Nothing tested whether the set could be LARGER, which is the direction that failed.

Filed as **Z-S108 @d51eec02df**; the correction was also **sent to the issuer by message**, because the wrong
number reached it that way and a formulation outruns its correction otherwise. Banked as
`a-name-search-cannot-enumerate-wildcard-grants`. **What stands:** the direction, the arithmetic on the two
roles examined (both reproduce exactly in Z-S107), the cleared comment-hits, and the disarm as framed.

**The finding that should drive the re-cut is not the count:** the fourth reader is the SIGNER --
`opalinvest-auth-handler` holds the private and public keys in one artifact and is named by neither face.
Teaching two verifiers a second slot while the signer is unnamed does not make FWD-10 achievable.

## 2. Z-S111 @1b2065e765 -- Z-S110's broken entry is a SINGLETON, not registry rot

Z-S110 found `opal-session-analytics`' source-map entry wrong on three axes. **The question it raises but does
not ask is whether the registry is rotten** -- and a reader could discount a correct finding as one more stale
row in a bad file. Unscoped census, all **204 entries against 201 live functions: 181 clean, `source_dir`
missing ZERO.** The file is maintained and the entry is a genuine outlier.

**Two of the three axes are NORMAL:** `EXTERNAL` with `files: []` is the map's ordinary idiom for "no repo
source", shared with 8 other entries. **The load-bearing axis is the third, and it is unique in 204:** declared
`python3.11`, live `nodejs20.x` -- the only LANGUAGE-level mismatch. The other two runtime mismatches are
same-language point-version drift that would still load; a zip built from this one could not.

⛔ **THIS SEAT'S FIRST PASS INVENTED A DEFECT CLASS AND IT WAS CAUGHT BEFORE FILING.** The initial census
reported 12 entries with `files: []` as broken. One refinement dissolved it to **ZERO**: 9 are `EXTERNAL` and 3
are `PackageType=Image`, both of which have no zip source by design. **A census that does not subtract the
legitimate cases manufactures findings**, and overstating is the direction someone else eventually catches --
which is exactly why it has to be caught before the row and not after the reply.

Real residual beyond Z-S110's subject: 9 entries naming functions that no longer exist. Recorded, not
escalated, not this project's to clean.

## 3. State

**111 rows, 35 this seat's.** Nothing waiting on this seat. **The one blocked item is unchanged:** the four
round-1 closure rows (S2, S11, S13, S17); gate here still `c3ef3a2530`, 0 occurrences of `REMEDIATED`.

**The night's through-line, now four instances:** the useful act each time was checking a number everyone had
already read and nobody had controlled -- an attachment count that was not a reachability count, a disarm
naming a plane that did not exist, a byte count that was not a delivery signal, and a grant list from a search
that could not see wildcards. **None was hidden. All four sat in output somebody had quoted.** Twice tonight
the quoted output was my own.
