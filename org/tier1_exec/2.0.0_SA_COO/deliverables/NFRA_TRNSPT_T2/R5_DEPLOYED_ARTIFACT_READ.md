# NFRA_TRNSPT round 5 -- the deployed gateway's mail_route.py, resolved by CONTENT (2.0.0_SA_COO~T2, 2026-10-08 ~18:0xZ)

Why: the manifest's opal-gateway `deployed_commit` `aa75078e1b72a28219e6148d3ec8e9bf705ea111` (`infra/aws/ec2/EC2_MANIFEST.json:503`)
is not in this repository and not on origin (`git fetch origin <sha>`: "not our ref"; 2,093 remote refs). Its release note
(`EC2_MANIFEST.json:506`) names it "branch rel-nfra-oplgtw-r28b, local, never merged", built on live base `510c8cfed2`, also absent here.
CLAUDE.md rule 22a: an ephemeral pin is resolved by CONTENT, against the build output.

Instrument: the release artifact the deploy shipped.
- Object `s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-aa75078e1b.tar.gz`: ETag `58f375cd26242c93b78b075eccb0ff94`,
  509420 bytes, metadata `git-ref=aa75078e1b72a28219e6148d3ec8e9bf705ea111` -- equal to the release note's "artifact
  opal-gateway-aa75078e1b.tar.gz ETag 58f375cd 509420 bytes", whose read-back says "md5 97 of 97 == release" on the host.
- `app/mail_route.py` inside it: sha256 `c7bf6ad9c30f0bf44dbb5d4b47b9dacd94dd188a08890da5a2ae15c1bccc3444`.
- HEAD `infra/aws/ec2/opal-gateway/app/mail_route.py`: sha256 `c7bf6ad9c30f0bf44dbb5d4b47b9dacd94dd188a08890da5a2ae15c1bccc3444`.
  Line diff (CR stripped): 0 lines.
- Positive control: `03a23664b4~1:infra/aws/ec2/opal-gateway/app/mail_route.py` against the artifact copy: 19 diff lines (DIFFERS).

VERDICT: the running gateway's `mail_route.py` is SAME-AS-HEAD. A divergent running gateway is ruled out as D2-S2's cause; what
remains is Graph returning no `nextLink`, or classification. The issuer's live census (round-5 decomposition, ruling 5) decides.
