# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtc-7: the 49 Financial source principal (R-44)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- never-widen sign-off is CTO+COO). **Signed:**
2026-09-18 ~06:3xZ. **The act signed:** the apply IB-rtc-7 performs, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtc-6.md`
describes it, read at HEAD `119fda050a` (blob `bb92a81c697c6d3fb8b01cb65fedfb9cb0563e38`). A packet whose bytes differ
from that blob is NOT what this half signs; IB-rtc-7 re-reads the blob hash before any apply.

This half signs the ACT'S BLAST RADIUS and the rollback per key -- what the act MAY touch on whichever branch the
producer takes -- never the producer's intention (CLAUDE.md NEVER-1). Writers of the named property are counted, not
assumed.

## The keys, all five, each with what it may touch and how it comes back

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K1 | creates `aws_iam_role` `irpt-49f-directory-read-role` (builder output) with ONE trust principal, `mdpf-daily-runner-ec2-role` | every process running as the host role (the mdpf daily chain on `i-02448edb624a7a7cf`, the accrual bridge's SSM runs, the IRPT dispatch's builds) becomes ABLE to assume it; nothing else can | revert `principal_49f.tf`, apply the directory root: 2 to destroy, nothing else; no prior state exists |
| K2 | the role's inline policy: `s3:GetObject` on the FIVE `opal-data-49financial/gold/advi/dimensions/<table>/*` prefixes and ONE prefix-conditioned `s3:ListBucket` on those five | whoever assumes K1 may list and read those five tables; NO write anywhere; NO other bucket; the host role itself still cannot read them (the fence denies it; it is granted nothing on that bucket) | destroyed with K1 |
| K3 | ONE statement on `mdpf-runner-scoped` (32 -> 33): `sts:AssumeRole` on K1's ARN | no data access by itself; it names K1, whose grant K2 bounds | revert the statement; targeted apply of the mdpf-pipeline root returns the document to the captured `before` (sha256 `b1d8027fe940c6a1...`), the other 32 statements untouched |
| K4 | ONE env key on `irpt-directory-refresh`: `IRPT_DIRECTORY_SOURCE_ROLE_MAP` naming the 49 Financial firm only | the 49 Financial build's shell receives the role ARN; the other two firms' builds unchanged (4 keys as before) | revert the `schedule.tf` line; apply the directory root; 4 keys |
| K5 | code: `refresh.py` hands the ARN to the named firm; `directory_runner.py` `Firm49F` reads its five tables through an assumed session; NEUTRAL without K4 | behaviour only, no IAM; reaches the world through the rebuilt Lambda artifact (directory apply) and the bundle mint (DS lane) | revert the two edits; the next rebuild and mint restore today's behaviour |

**Writers of the named property, counted (R-44, CLAUDE.md NEVER-1 "first count the writers"):** `s3:PutObject` on the 49
Financial directory prefix (`opal-data-bd/investor-reporting/directory/`, the legacy 49 Financial destination until D14)
-- **12 of 262 principals** (8 `bd-*` roles, the host role, 3 users), 0 UNKNOWN, resource plane 0 allows / 0 denies; the
new principal is NOT among them (`implicitDeny`). IB-rtc-7 re-censuses after the apply and must read 12, unchanged.
One property, twelve writers, twelve rules read by the packet's census -- this half signs none of those twelve moves.

## Both branches covered

- The producer takes the apply: K1-K4 land exactly as the two plans print (directory `2 add / 1 change / 0 destroy`,
  mdpf-pipeline `0 / 2 / 0` of which K3 is ONE change and the other is NOT this act -- see the departure below).
- The producer stops: a re-plan that differs from the packet's plan text (sha256 `b844c72c...` / `0d586c2e...` at the
  same declaring commits, or the same set of changes at a later commit) is IB-rtc-7's STOP, and nothing is applied.
- The role exists and the negative control FAILS (N1, N2, N3 or N4 reads anything but `AccessDenied`, or N5 reads
  allowed): the act is rolled back by K1's rollback the same turn, and the row is BLOCKING.

## ONE DELIBERATE DEPARTURE, named here so it is signed and not assumed

The decomposition's deploy discipline (v0.2 s.6) says `-target` never. **This half signs a TARGETED apply of the
mdpf-pipeline root, `-target=aws_iam_role_policy.mdpf_runner`, for K3 only** -- because that root's plan carries a
second, unrelated change, `aws_s3_object.mdpf_route_bindings`, whose deployed hash matches neither the committed blob
nor this box's CRLF rendering (row `IRPT_BCKEND-S68`). An untargeted apply would upload CRLF bytes over a live MDPF
route-binding object that nobody in this project owns -- a blast radius outside the act. The `-target` bound exists to
prevent partial applies that leave a root half-landed; here the root is ALREADY divergent by someone else's unapplied
change, and the targeted apply leaves it exactly as divergent as it is today. The drift itself is carried to
`1.0.0_SA_CTO` for MDPF's owner as a finding, never repaired as a rider here.

## What this half does NOT sign

- Any write grant to the new role (there is none).
- The bundle mint (K5's runner) -- a DS-lane act under Rule 13, sequenced as IB-rtc-8 and graded by its own instance.
- The destination's move out of `opal-data-bd` (D14's).
- Anything on `opal-data-49financial` beyond the five dimension prefixes.

**Push state at signing:** `119fda050a` LOCAL; origin/CLOUD `88b80ac07d` (last read 23:53Z).
