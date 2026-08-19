# Deploy-completion ledger -- OPAL_ADVIPOINTERS P2/P3 B-grant: advi-49f-chain-access on bd-exporter-ec2-role
**Opened+closed same window 2026-08-19 13:12-13:14Z by 0.7.0_AE_CloudOps.** DECOUPLED from the schedule TF (DS~A 130003Z ask; COO re-date @f79760179a; CTO GATE-GO 131157Z). Schedule TF stays HELD for R+1.

**Act:** ONE aws_iam_role_policy added (bd-pipeline/iam.tf @HEAD, +78 lines): B2 GetObject blackdiamond/49f/silver/dim_advisor_fee_role/* | B3 GetObject schwab/08335338/meta/conversions/* | scoped ListBucket both | B5 Get/Put opal-data-49financial/gold/advi/* | B6 GetObject opal-data-49financial/_code/* | scoped ListBucket both | B7 dynamodb:Scan table/bd-securities (grounded a07:132-135 + etf_classifier.py:57-59; Rule 22a(iv) two-hop annotation in-file). B1 NOT duplicated (silver/* wholesale @7b706eec4c).

**Apply:** safe-apply, "1 added, 0 changed, 0 destroyed"; post-apply UNTARGETED plan "No changes" (clean root, no targeting needed).
**Battery (one --resource-arns per call, separate invocations):** 6 allow-sims ALL "allowed" (B5 Put+Get gold key, B6 _code read, B2 feerole read, B3 conv-manifest read, B7 Scan on the table ARN); 2 NEGATIVE controls BOTH implicitDeny (PutObject on _code/* -- write deliberately not granted there; GetObject on an ungranted assets prefix -- discriminates).
**Applied-plane read:** get-role-policy shows all 7 Sids (AdviChainBdFeeRoleRead, AdviChainConversionManifestRead, AdviChainAssetsListScoped, AdviChainGoldRW, AdviChainCodeRead, AdviChain49fListScoped, AdviChainBdSecuritiesScan).
**Mint-loop closure (CTO 131157Z):** the mint exercise's condition (iii) bd-exporter implicitDeny was EXPECTED-absent-identity-grant -- this grant IS that arrival; the B5 allow-sim closes the loop (Deny holds foreign firms, Allow lands for the executor).
**comp-iam gaps** run post-edit: no new missing/mismatch rows from this change (pre-existing mdpf-publisher rows untouched).
