# Deploy Completion Record
**Date opened:** 2026-09-03T09:39:40.335283+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260903T102351Z
**Deploy:** NFRA_OPSEC202609 TO-OP-S-5 legs 2+3: CloudFront access logs (v2 delivery) and ALB access logs into opal-data-security
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | bucket policy on opal-data-security gains the two log-delivery principals, each scoped to ONE prefix | get-bucket-policy shows both Sids with prefix-scoped Resource; ownership setting UNCHANGED (read before and after) | aws_s3_bucket_policy.data_security applied 0/1/0. get-bucket-policy now shows 3 Sids: DenyInsecureTransport (unchanged, bucket-wide), AllowCloudFrontAccessLogDelivery scoped to waf-logs/cloudfront-access/* ONLY, AllowALBAccessLogDelivery scoped to waf-logs/alb-opal-gateway/* ONLY -- neither names the bucket. Object ownership read BEFORE and AFTER: BucketOwnerEnforced both times, UNCHANGED per the face's bound. | CLOSED 20260903T094554Z |
| L2 | activation | CloudFront standard logging v2 delivery source/destination/delivery for EVTSA9VEHNZVH | the three delivery resources exist and the distribution's logging reads ON to waf-logs/cloudfront-access/ | 3 added, 0 changed, 0 destroyed; post-apply re-plan -detailed-exitcode = 0. STANDARD LOGGING v2 chosen on a MEASURED ground, not a preference: opal-data-security reads ObjectOwnership=BucketOwnerEnforced (ACLs disabled), and legacy CloudFront standard logging writes objects with an ACL, so the legacy path cannot work here and the face forbids changing the ownership setting to suit it. describe-delivery-sources: opal-portal-cloudfront-access, logType ACCESS_LOGS, resource arn:aws:cloudfront::313476888478:distribution/EVTSA9VEHNZVH. describe-delivery-destinations: opal-portal-cloudfront-access-s3, type S3, destination arn:aws:s3:::opal-data-security/waf-logs/cloudfront-access. Ownership read again AFTER: BucketOwnerEnforced, UNCHANGED. | CLOSED 20260903T095031Z |
| L3 | activation | ALB opal-gateway access_logs.s3.enabled=true to waf-logs/alb-opal-gateway/ | describe-load-balancer-attributes shows enabled/bucket/prefix -- the enablement is itself the policy oracle (it test-writes and fails loud) | aws_lb.gw applied 0/1/0, UPDATE IN PLACE with 0 replacements (checked before applying -- a replacement of this internet-facing ALB would have been an outage). describe-load-balancer-attributes AFTER: access_logs.s3.enabled=true, bucket=opal-data-security, prefix=waf-logs/alb-opal-gateway (all three empty/false before). THE APPLY IS THE POLICY ORACLE: elbv2 test-writes on enablement and refuses if the bucket policy denies, so its success proves the logdelivery.elasticloadbalancing.amazonaws.com service-principal form is correct here -- measured, not guessed between that and the legacy regional ELB-account-ID form. 1 object already present under waf-logs/alb-opal-gateway/. | CLOSED 20260903T094554Z |
| L4 | verify | objects present under both prefixes within their delivery windows, or the count read and stated | list-objects-v2 count + newest key per prefix | REAL OBJECTS PRESENT UNDER BOTH PREFIXES, placeholder and test-file excluded. waf-logs/cloudfront-access/: 2 keys listed, 1 REAL -- EVTSA9VEHNZVH.2026-09-03-10.74ff5ab2.gz, 701 bytes, delivered 10:2xZ inside the v2 window (the other key is the zero-byte prefix placeholder). waf-logs/alb-opal-gateway/: 1 REAL production object at 09:50Z (ELBAccessLogTestFile excluded as an enablement artifact). Both keys sit under waf-logs/ so the single existing lifecycle rule waf-logs-glacier-90-expire-400 covers them. The CloudFront leg had NO test-write oracle, so these objects are the only evidence its prefix-scoped grant and its delivery path agree -- and they do. | CLOSED 20260903T102351Z |

## Log

- 20260903T093940Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
- 20260903T094554Z LEG L1 closed: aws_s3_bucket_policy.data_security applied 0/1/0. get-bucket-policy now shows 3 Sids: DenyInsecureTransport (unchanged, 
- 20260903T094554Z LEG L3 closed: aws_lb.gw applied 0/1/0, UPDATE IN PLACE with 0 replacements (checked before applying -- a replacement of this internet-
- 20260903T095031Z LEG L2 closed: 3 added, 0 changed, 0 destroyed; post-apply re-plan -detailed-exitcode = 0. STANDARD LOGGING v2 chosen on a MEASURED gro
- 20260903T102351Z LEG L4 closed: REAL OBJECTS PRESENT UNDER BOTH PREFIXES, placeholder and test-file excluded. waf-logs/cloudfront-access/: 2 keys listed
- 20260903T102351Z CLOSED -- all 4 legs proven
