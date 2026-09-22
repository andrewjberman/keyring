// Offline probes of real merged modules. No production edits, no live keys/network.
import assert from 'node:assert/strict';
import { registerHooks } from 'node:module';
import { generateKeyPairSync } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../../..');
const edgePath = path.join(root, 'infra/aws/lambda-edge/auth-validator-edge');
const keys = generateKeyPairSync('rsa', {modulusLength:2048,
  publicKeyEncoding:{type:'spki',format:'pem'},privateKeyEncoding:{type:'pkcs8',format:'pem'}});
const jwtUrl = pathToFileURL(path.join(edgePath, 'node_modules/jsonwebtoken/index.js')).href;
const fake = `export class SecretsManagerClient { async send(){throw Error('NETWORK FORBIDDEN')} }
export class GetSecretValueCommand {constructor(input){this.input=input}}
export class DynamoDBClient {async send(){throw Error('NETWORK FORBIDDEN')}}
export class ScanCommand {constructor(input){this.input=input}}
export class S3Client {async send(){throw Error('NETWORK FORBIDDEN')}}
export class GetObjectCommand {constructor(input){this.input=input}}`;
const fakeUrl = 'data:text/javascript,' + encodeURIComponent(fake);
registerHooks({resolve(specifier, context, next) {
  if (specifier === 'jsonwebtoken') return {url:jwtUrl,shortCircuit:true};
  if (specifier.startsWith('@aws-sdk/client-')) return {url:fakeUrl,shortCircuit:true};
  return next(specifier, context);
}});

// This mode reruns the worker suite with one explicitly shared mock SDK identity.
if (process.argv.includes('--worker-v2')) {
  await import(pathToFileURL(path.join(root,
    'org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~15/test_edge_render_delegate_v2_authorizer.mjs')));
} else {
  const jwt = (await import(jwtUrl)).default;
  const edge = await import(pathToFileURL(path.join(edgePath, 'index.mjs')));
  const ra = await import(pathToFileURL(path.join(edgePath, 'render_auth.mjs')));
  const v2 = await import(pathToFileURL(path.join(root, 'infra/aws/users/lambda/portal-authorizer/index.mjs')));
  ra.__setRenderKeySlotsForTest({current:keys.publicKey,previous:null});
  process.env.IRPT_RENDER_JWT_PUBLIC_KEY_PEM = keys.publicKey;
  const pyPath = path.join(path.dirname(fileURLToPath(import.meta.url)), 'IRPT_BCKEND_R17_PROBE.py');
  const python = (mode, input) => execFileSync('py',['-3.12',pyPath,mode],
    {cwd:root,input:JSON.stringify(input),encoding:'utf8'}).trim();
  const bundle = {firm_id:'49financial',bundle_id:'bundle-1',revision:'rev-1',
    account_set_id:'AS-1',job_id:'JOB-1',report_id:'REP-1',delegator_subject:'advisor.a@49financial.com'};
  const realToken = python('mint',{bundle,key:keys.privateKey});
  const payload = jwt.decode(realToken);
  const event = (token, uri='/investor-reporting/print', method='GET', extras={}) =>
    ({Records:[{cf:{request:{uri,method,querystring:'',headers:{...extras,
      authorization:[{key:'Authorization',value:'Bearer '+token}]}}}}]});
  const route = {routeKey:'GET /api/scoped/investor-reporting/performance/{accountSetId}',pathParameters:{accountSetId:'AS-1'}};
  const forwarded = await edge.handler(event(realToken));
  assert.equal(forwarded.uri,'/investor-reporting/print');
  const freshClass = JSON.parse(python('classify',forwarded.headers));
  assert.equal(freshClass.classification[0],'UNKNOWN');
  const markerControl = JSON.parse(python('classify',{...forwarded.headers,'x-origin-verify':'cloudfront'}));
  assert.equal(markerControl.classification[0],'RENDER_DELEGATE');
  assert.equal(v2.authorizeRenderToken(realToken,route).isAuthorized,true);
  const forbidden = [];
  for (const extra of [{role:'admin'},{firmRole:'admin'},{tier:'internal'},{userType:'Dev'}]) {
    const token = jwt.sign({...payload,...extra},keys.privateKey,{algorithm:'RS256'});
    const answer = v2.authorizeRenderToken(token,route);
    assert.equal(answer.isAuthorized,true);
    const edgeAnswer = await edge.handler(event(token));
    assert.equal(edgeAnswer.status,'401');
    forbidden.push({claim:extra,v2:answer.isAuthorized,v3:edgeAnswer.status});
  }
  const missingExp = {...payload}; delete missingExp.exp;
  const noExpToken = jwt.sign(missingExp,keys.privateKey,{algorithm:'RS256'});
  const noExpEdge = await edge.handler(event(noExpToken));
  assert.equal(noExpEdge.uri,'/investor-reporting/print');
  assert.equal(v2.authorizeRenderToken(noExpToken,route).isAuthorized,true);
  const recentExpiry = jwt.sign({...payload, exp:Math.floor(Date.now()/1000)-5},keys.privateKey,{algorithm:'RS256'});
  const expiredExpiry = jwt.sign({...payload, exp:Math.floor(Date.now()/1000)-120},keys.privateKey,{algorithm:'RS256'});
  const recentV3 = await edge.handler(event(recentExpiry));
  const oldV3 = await edge.handler(event(expiredExpiry));
  assert.equal(recentV3.uri,'/investor-reporting/print');
  assert.equal(v2.authorizeRenderToken(recentExpiry,route).isAuthorized,false);
  assert.equal(oldV3.status,'401');
  const post = await edge.handler(event(realToken,'/api/scoped/investor-reporting/performance/AS-1','POST'));
  assert.equal(post.method,'POST');
  const asset = await edge.handler(event(realToken,'/assets/index-fixture.js'));
  assert.equal(asset.status,'401');
  const otherUri = await edge.handler(event(realToken,'/unrelated'));
  assert.equal(otherUri.status,'401');
  const wrongId = v2.authorizeRenderToken(realToken,{...route,pathParameters:{accountSetId:'OTHER'}});
  assert.equal(wrongId.isAuthorized,false);
  console.log('CVO_RESULT '+JSON.stringify({real_mint_to_v2:true,real_mint_to_v3:true,
    fresh_edge_to_resolver:freshClass.classification,origin_marker_control:markerControl.classification[0],
    forbidden_claims:forbidden,missing_exp_accepted_both:true,expired_five_seconds_v3_accepted:true,
    expired_five_seconds_v2_denied:true,expired_120_seconds_v3:oldV3.status,post_forwarded_by_v3:true,
    root_assets_refused:asset.status,nonprint_control:otherUri.status,swapped_id_control:wrongId.isAuthorized,
    verdict:'counterexamples reproduced; no deployment or acceptance'}));
}
