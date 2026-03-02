# CloudFront Deployment Validation Checklist

**Purpose:** Comprehensive pre-flight and post-deployment validation for CloudFront architecture
**Owner:** DevOps Technician
**Last Updated:** 2026-01-04
**Version:** 1.0

---

## Pre-Deployment Checklist

### 1. Planning & Coordination

- [ ] **All 4 agents' code merged to `DEV` branch**
  - Agent 1 (AWS Engineer - Lambda Backend): Code merged to DEV
  - Agent 2 (AWS Engineer - CloudFront/Edge): Code merged to DEV
  - Agent 3 (React Designer - Frontend): Code merged to DEV
  - Agent 4 (DevOps Technician - Testing): Code merged to DEV

- [ ] **DEV branch merged to `PROD` for production deployment**
  ```bash
  git checkout PROD
  git pull origin PROD
  git merge DEV
  git push origin PROD
  ```

- [ ] **Integration tests passing locally**
  ```bash
  cd /home/ajb327/ajb_workspace/tests/cloudfront
  ./run_all_tests.sh --no-auth
  ```

- [ ] **Staging environment tested successfully**
  - CloudFront staging distribution configured
  - Frontend deployed to staging
  - All test suites pass in staging

- [ ] **Rollback plan reviewed**
  - Rollback configs saved in `infra/aws/cloudfront/rollback_configs/`
  - Team trained on rollback procedures
  - Emergency contacts updated

- [ ] **Stakeholders notified**
  - Deployment window scheduled
  - User communication prepared (if needed)
  - Team available during deployment

- [ ] **Monitoring ready**
  - CloudWatch dashboard created
  - Alarms configured
  - Health check script tested

---

## Phase 1: Lambda Optimization Deployment

### 1.1 Lambda Memory & Provisioned Concurrency

- [ ] **Increase Lambda memory to 1024MB**
  ```bash
  aws lambda update-function-configuration \
    --function-name opal-portal-data-proxy \
    --memory-size 1024 \
    --region us-east-1
  ```

- [ ] **Publish Lambda version**
  ```bash
  VERSION=$(aws lambda publish-version \
    --function-name opal-portal-data-proxy \
    --region us-east-1 \
    --query 'Version' \
    --output text)
  echo "Published version: $VERSION"
  ```

- [ ] **Create alias pointing to version**
  ```bash
  aws lambda create-alias \
    --function-name opal-portal-data-proxy \
    --name production \
    --function-version $VERSION \
    --region us-east-1
  ```

- [ ] **Enable provisioned concurrency (2 instances)**
  ```bash
  aws lambda put-provisioned-concurrency-config \
    --function-name opal-portal-data-proxy \
    --provisioned-concurrent-executions 2 \
    --qualifier production \
    --region us-east-1
  ```

### 1.2 Validation: Lambda Performance

- [ ] **Provisioned concurrency status: READY**
  ```bash
  aws lambda get-provisioned-concurrency-config \
    --function-name opal-portal-data-proxy \
    --qualifier production \
    --region us-east-1
  ```
  Expected: `"Status": "READY"`

- [ ] **Test warm invocation (should be <500ms)**
  ```bash
  for i in {1..10}; do
    aws lambda invoke \
      --function-name opal-portal-data-proxy:production \
      --payload '{"httpMethod":"GET","path":"/market/rsi"}' \
      /tmp/test_$i.json \
      --region us-east-1
  done
  ```

- [ ] **Lambda duration < 1000ms (from 1395ms baseline)**
  ```bash
  aws logs filter-log-events \
    --log-group-name /aws/lambda/opal-portal-data-proxy \
    --filter-pattern "REPORT" \
    --max-items 10 \
    --region us-east-1
  ```
  Check: Duration values in logs

### 1.3 CloudWatch Alarms

- [ ] **High error rate alarm configured**
  ```bash
  aws cloudwatch describe-alarms \
    --alarm-names opal-portal-data-proxy-high-error-rate \
    --region us-east-1
  ```

- [ ] **High duration alarm configured**
  ```bash
  aws cloudwatch describe-alarms \
    --alarm-names opal-portal-data-proxy-high-duration \
    --region us-east-1
  ```

- [ ] **Throttles alarm configured**
  ```bash
  aws cloudwatch describe-alarms \
    --alarm-names opal-portal-data-proxy-throttles \
    --region us-east-1
  ```

### 1.4 Lambda CloudFront Header Support

- [ ] **Lambda accepts CloudFront headers**
  ```bash
  aws lambda invoke \
    --function-name opal-portal-data-proxy \
    --payload '{
      "httpMethod": "GET",
      "path": "/portfolios/aum-metrics",
      "headers": {
        "x-user-email": "test@opalinvest.com",
        "x-user-tier": "internal",
        "x-firm-id": "opal_capital",
        "x-origin-verify": "cloudfront"
      }
    }' \
    --cli-binary-format raw-in-base64-out \
    /tmp/test.json \
    --region us-east-1
  ```
  Check logs: Headers should be logged

### 1.5 Data Pipeline Invalidation

- [ ] **All 6 data pipeline Lambdas updated with invalidation code**
  - opal-precompute-market-metrics
  - yang-generate-macro
  - yang-generate-valuation
  - opal-portal-fear-greed-fetcher
  - yang-generate-correlation
  - yang-generate-volatility

- [ ] **Test invalidation**
  ```bash
  # Trigger one data pipeline Lambda
  aws lambda invoke \
    --function-name opal-precompute-market-metrics \
    --region us-east-1 \
    /tmp/test.json

  # Check CloudWatch logs for invalidation ID
  aws logs filter-log-events \
    --log-group-name /aws/lambda/opal-precompute-market-metrics \
    --filter-pattern "CloudFront invalidation" \
    --max-items 5 \
    --region us-east-1

  # Verify invalidation was created
  aws cloudfront list-invalidations \
    --distribution-id EVTSA9VEHNZVH \
    --max-items 10 \
    --region us-east-1
  ```

### 1.6 Lambda Error Rate

- [ ] **Lambda error rate < 0.1% (from 0.76%)**
  ```bash
  aws cloudwatch get-metric-statistics \
    --namespace AWS/Lambda \
    --metric-name Errors \
    --dimensions Name=FunctionName,Value=opal-portal-data-proxy \
    --statistics Sum \
    --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
    --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
    --period 3600 \
    --region us-east-1
  ```

**Phase 1 Sign-Off:**
- [ ] All Lambda optimizations deployed
- [ ] Performance metrics improved
- [ ] No increase in error rate
- [ ] Provisioned concurrency active

---

## Phase 2: CloudFront Distribution Update

### 2.1 Lambda@Edge Deployment

- [ ] **All 4 Lambda@Edge functions deployed to us-east-1**
  - auth-validator-edge
  - public-data-router
  - cache-control-injector
  - tier-router-edge

- [ ] **All Lambda@Edge functions published**
  ```bash
  aws lambda list-functions \
    --region us-east-1 \
    --query 'Functions[?starts_with(FunctionName, `auth-validator`) || starts_with(FunctionName, `public-data`) || starts_with(FunctionName, `cache-control`) || starts_with(FunctionName, `tier-router`)].FunctionName'
  ```

- [ ] **Lambda@Edge versions noted**
  ```bash
  # Save version ARNs for distribution config
  aws lambda list-versions-by-function \
    --function-name auth-validator-edge \
    --region us-east-1 \
    --query 'Versions[-1].FunctionArn'
  ```

### 2.2 S3 Bucket Policies

- [ ] **Origin Access Control (OAC) created**
  ```bash
  aws cloudfront list-origin-access-controls \
    --region us-east-1 \
    --query 'OriginAccessControlList.Items[?Name==`opal-data-portal-v2-oac`]'
  ```

- [ ] **S3 bucket policy updated**
  ```bash
  aws s3api get-bucket-policy \
    --bucket opal-data-portal-v2 \
    --region us-east-1
  ```
  Verify: Policy allows CloudFront OAC access

- [ ] **Direct S3 URLs blocked (only CloudFront can access)**
  ```bash
  # This should fail (403)
  curl https://opal-data-portal-v2.s3.amazonaws.com/json/market/rsi_summary.json
  ```

### 2.3 CloudFront Distribution Configuration

- [ ] **Distribution config updated (3 origins, 7 behaviors)**
  ```bash
  aws cloudfront get-distribution-config \
    --id EVTSA9VEHNZVH \
    --region us-east-1 \
    > updated-distribution.json
  ```
  Verify:
  - Origins: portal-static-origin, portal-public-data-origin, portal-api-gateway-origin
  - Cache behaviors: /auth/*, /api/public/*, /api/private/*, /api/shared/*, /api/metrics/*, /assets/*, default

- [ ] **Distribution status: Deployed**
  ```bash
  aws cloudfront get-distribution \
    --id EVTSA9VEHNZVH \
    --region us-east-1 \
    --query 'Distribution.Status'
  ```
  Expected: "Deployed"

- [ ] **Lambda@Edge associations verified**
  ```bash
  aws cloudfront get-distribution-config \
    --id EVTSA9VEHNZVH \
    --region us-east-1 \
    --query 'DistributionConfig.CacheBehaviors.Items[].LambdaFunctionAssociations'
  ```

### 2.4 Validation: CloudFront Routing

- [ ] **Test public endpoint**
  ```bash
  curl https://d2n2nzpeqf34ge.cloudfront.net/api/public/market/rsi_summary.json
  ```
  Expected: 200 OK, valid JSON response

- [ ] **Test cache hit**
  ```bash
  curl -I https://d2n2nzpeqf34ge.cloudfront.net/api/public/market/rsi_summary.json | grep "x-cache"
  ```
  Expected: "X-Cache: Hit from cloudfront" (on second request)

- [ ] **Run public endpoints test**
  ```bash
  cd /home/ajb327/ajb_workspace/tests/cloudfront
  ./test_public_endpoints.sh
  ```
  Expected: All tests pass

- [ ] **Run cache performance test**
  ```bash
  cd /home/ajb327/ajb_workspace/tests/cloudfront
  ./test_cache_performance.sh
  ```
  Expected: Cache hit ratio > 80%, latency < 100ms

### 2.5 CloudWatch Dashboard

- [ ] **CloudWatch dashboard created**
  ```bash
  aws cloudwatch list-dashboards \
    --region us-east-1 \
    --query 'DashboardEntries[?DashboardName==`opal-portal-cloudfront-performance`]'
  ```

- [ ] **Dashboard showing metrics**
  - Cache hit ratio
  - Origin latency
  - 4xx/5xx error rates
  - Bytes downloaded
  - Lambda@Edge duration
  - Requests per second

**Phase 2 Sign-Off:**
- [ ] CloudFront distribution deployed
- [ ] All cache behaviors active
- [ ] Lambda@Edge functions working
- [ ] Public endpoints accessible
- [ ] Cache hit ratio > 80%

---

## Phase 3: Frontend Deployment

### 3.1 Frontend Code Changes

- [ ] **API client updated to use `/api` paths**
  ```typescript
  // portal/src/api/api-client.ts
  export const API_BASE_URL = '/api';
  ```

- [ ] **All 10 endpoint files remapped**
  - market.ts
  - macro.ts
  - sentiment.ts
  - valuation.ts
  - benchmarks.ts
  - positioning.ts
  - portfolios.ts
  - cma.ts
  - correlation.ts
  - volatility.ts

- [ ] **Client-side cache removed**
  ```typescript
  // portal/src/api/cache.ts
  // withCache() is now a pass-through
  ```

- [ ] **Vite dev proxy configured**
  ```typescript
  // portal/vite.config.ts
  proxy: {
    '/api': {
      target: 'https://d2n2nzpeqf34ge.cloudfront.net',
      ...
    }
  }
  ```

### 3.2 Build & Deploy

- [ ] **Frontend build successful**
  ```bash
  cd /home/ajb327/ajb_workspace/portal
  npm run build
  ```
  Expected: No errors

- [ ] **Deploy to staging first**
  ```bash
  npm run deploy:staging
  ```
  Test in staging before production

- [ ] **Deploy to production**
  ```bash
  npm run deploy
  ```

### 3.3 Validation: Frontend Functionality

- [ ] **Login successful**
  - Navigate to https://portal.opalinvest.com
  - Log in with test account
  - Verify: No errors, token stored

- [ ] **Market tab loads**
  - Navigate to Market tab
  - Verify: RSI data displays
  - Check browser console: No errors

- [ ] **Sentiment tab loads**
  - Navigate to Sentiment tab
  - Verify: Fear & Greed Index displays
  - Check network tab: Request to `/api/public/sentiment/...`

- [ ] **Portfolios tab loads (authenticated)**
  - Navigate to Portfolios tab
  - Verify: AUM metrics display
  - Check network tab: Authorization header present

- [ ] **No console errors**
  ```
  Open browser DevTools > Console
  Verify: No errors or warnings
  ```

- [ ] **API requests route to CloudFront**
  ```
  Open browser DevTools > Network tab
  Check: Requests go to /api/* (same-origin)
  Check: Response headers show "X-Cache" (CloudFront)
  ```

**Phase 3 Sign-Off:**
- [ ] Frontend deployed successfully
- [ ] All pages load correctly
- [ ] API requests route to CloudFront
- [ ] Auth headers passed correctly
- [ ] No console errors

---

## Phase 4: Monitoring & Testing

### 4.1 Automated Test Suite

- [ ] **Run all tests**
  ```bash
  cd /home/ajb327/ajb_workspace/tests/cloudfront
  ./run_all_tests.sh
  ```
  Note: Auth tests will skip if tokens not configured

- [ ] **Public endpoints test passes**
  ```bash
  ./test_public_endpoints.sh
  ```

- [ ] **Cache performance test passes**
  ```bash
  ./test_cache_performance.sh
  ```

- [ ] **Authentication tests pass** (if tokens configured)
  ```bash
  ./test_auth_tiers.sh
  ```

- [ ] **Firm isolation tests pass** (if tokens configured)
  ```bash
  ./test_firm_isolation.sh
  ```

### 4.2 Performance Benchmarks

- [ ] **Run performance benchmark**
  ```bash
  cd /home/ajb327/ajb_workspace/tests/cloudfront
  python3 benchmark_api_performance.py 50
  ```

- [ ] **Cache hit ratio > 90%**
  Check: Benchmark results show cache_hit_ratio > 90%

- [ ] **Median latency < 50ms** (vs 408ms before)
  Check: CloudFront median < 50ms

- [ ] **Speedup factor > 8x**
  Check: Overall improvement factor

### 4.3 Security Validation

- [ ] **Tier isolation working**
  - Client tier blocked from shared data (403)
  - Internal + Advisor tiers access shared data (200)

- [ ] **Firm isolation working**
  - Different firms see different private data
  - No cross-firm data leakage

- [ ] **Invalid tokens rejected**
  ```bash
  curl https://d2n2nzpeqf34ge.cloudfront.net/api/private/portfolios/aum-metrics.json \
    -H "Authorization: Bearer invalid-token"
  ```
  Expected: 401 Unauthorized

### 4.4 Health Monitoring

- [ ] **CloudWatch dashboard healthy**
  - Cache hit ratio > 90%
  - 4xx error rate < 5%
  - 5xx error rate < 1%
  - Origin latency < 1000ms

- [ ] **Run health check script**
  ```bash
  /home/ajb327/ajb_workspace/infra/aws/monitoring/cloudfront-health-check.sh
  ```
  Expected: All metrics within thresholds

- [ ] **Alarms not triggered**
  ```bash
  aws cloudwatch describe-alarms \
    --state-value ALARM \
    --region us-east-1
  ```
  Expected: No alarms in ALARM state

**Phase 4 Sign-Off:**
- [ ] All automated tests passing
- [ ] Performance benchmarks show improvement
- [ ] Security tests pass
- [ ] Monitoring shows healthy state

---

## Post-Deployment Monitoring (24 hours)

### Hour 1-4: Active Monitoring

- [ ] **Monitor error rates every 15 minutes**
  ```bash
  watch -n 900 'aws cloudwatch get-metric-statistics --namespace AWS/Lambda --metric-name Errors --dimensions Name=FunctionName,Value=opal-portal-data-proxy --statistics Sum --start-time $(date -u -d "1 hour ago" +%Y-%m-%dT%H:%M:%S) --end-time $(date -u +%Y-%m-%dT%H:%M:%S) --period 300 --region us-east-1'
  ```

- [ ] **Check CloudFront cache hit ratio**
  ```bash
  aws cloudwatch get-metric-statistics \
    --namespace AWS/CloudFront \
    --metric-name CacheHitRate \
    --dimensions Name=DistributionId,Value=EVTSA9VEHNZVH \
    --statistics Average \
    --start-time $(date -u -d "4 hours ago" +%Y-%m-%dT%H:%M:%S) \
    --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
    --period 3600 \
    --region us-east-1
  ```

- [ ] **Monitor user feedback**
  - Check #support channel in Slack
  - Review any user-reported issues

### Hour 4-24: Passive Monitoring

- [ ] **Run health check every 4 hours**
  ```bash
  # Add to cron or run manually
  */4 * * * * /home/ajb327/ajb_workspace/infra/aws/monitoring/cloudfront-health-check.sh
  ```

- [ ] **Check for anomalies**
  - Sudden drops in cache hit ratio
  - Spikes in error rates
  - Increase in origin latency

### 24-Hour Review

- [ ] **Error rate < 0.1% sustained**
- [ ] **Cache hit ratio > 95% sustained**
- [ ] **Median latency < 50ms sustained**
- [ ] **No user complaints**
- [ ] **All functionality working**

---

## Success Metrics

| Metric | Before | Target | Actual | Status |
|--------|--------|--------|--------|--------|
| Median Latency | 408ms | <50ms | ___ms | ⏳ |
| P90 Latency | 918ms | <100ms | ___ms | ⏳ |
| Cache Hit Ratio | 0% | >95% | __% | ⏳ |
| Error Rate | 0.76% | <0.1% | __% | ⏳ |
| Lambda Duration | 1,395ms | <600ms | ___ms | ⏳ |

**Cost Tracking:**

| Item | Before | After | Savings |
|------|--------|-------|---------|
| Lambda Compute | $4.27 | $____ | $____ |
| API Gateway | $1.75 | $____ | $____ |
| CloudFront | $0 | $____ | +$____ |
| Lambda@Edge | $0 | $____ | +$____ |
| Provisioned Concurrency | $0 | $____ | +$____ |
| **Total** | **$10.52** | **$____** | **$____** |

---

## Rollback Trigger Conditions

If ANY of these occur, initiate rollback immediately:

- [ ] Error rate > 10% for 5+ minutes
- [ ] Complete service outage (all endpoints returning errors)
- [ ] Data integrity issues (users seeing wrong data)
- [ ] Security vulnerability detected (cross-firm data leakage)
- [ ] Rollback requested by Product Owner

**Rollback Procedure:** See `docs/deployment/cloudfront_rollback_plan.md`

---

## Deployment Sign-Off

### Phase 1: Lambda Optimization
- [ ] Signed off by: _________________ Date: _______

### Phase 2: CloudFront Distribution
- [ ] Signed off by: _________________ Date: _______

### Phase 3: Frontend Deployment
- [ ] Signed off by: _________________ Date: _______

### Phase 4: Monitoring & Testing
- [ ] Signed off by: _________________ Date: _______

### Final Deployment Approval
- [ ] Signed off by: _________________ Date: _______

---

## Post-Deployment Actions

- [ ] **Create session logs** (all 4 agents)
  - Agent 1: `logs/sessions/2026-01-04/aws_engineer/lambda_backend_optimization.md`
  - Agent 2: `logs/sessions/2026-01-04/aws_engineer/cloudfront_edge_deployment.md`
  - Agent 3: `logs/sessions/2026-01-04/react_designer/frontend_api_integration.md`
  - Agent 4: `logs/sessions/2026-01-04/devops_technician/testing_monitoring_deployment.md`

- [ ] **Update architecture documentation**
  - Document new CloudFront architecture
  - Update API endpoint documentation
  - Update deployment procedures

- [ ] **Cost tracking**
  - Monitor AWS costs daily for first week
  - Compare actual vs projected costs
  - Adjust provisioned concurrency if needed

- [ ] **Team knowledge transfer**
  - Share deployment experience
  - Update runbooks
  - Train team on new architecture

---

**Document Version:** 1.0
**Last Updated:** 2026-01-04
**Next Review:** After deployment completion
**Owner:** DevOps Technician
