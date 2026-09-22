// Offline actual V2 audit coverage, fixture keys only, no persisted secrets.
import {registerHooks} from 'node:module';
import {generateKeyPairSync} from 'node:crypto';
import assert from 'node:assert/strict';
const root = new URL('../../../../', import.meta.url);
const fake = 'data:text/javascript,' + encodeURIComponent(`
export class SecretsManagerClient {async send(){throw Error('NETWORK FORBIDDEN')}}
export class GetSecretValueCommand {constructor(input){this.input=input}}
export class DynamoDBClient {async send(){throw Error('NETWORK FORBIDDEN')}}
export class ScanCommand {constructor(input){this.input=input}}`);
registerHooks({resolve(s,c,n){
  if(s.startsWith('@aws-sdk/client-')) return {url:fake,shortCircuit:true};
  return n(s,c);
}});
const jwt = (await import(new URL('infra/aws/users/lambda/portal-authorizer/node_modules/jsonwebtoken/index.js',root))).default;
const v2 = await import(new URL('infra/aws/users/lambda/portal-authorizer/index.mjs',root));
const keys = generateKeyPairSync('rsa',{modulusLength:2048,publicKeyEncoding:{type:'spki',format:'pem'},privateKeyEncoding:{type:'pkcs8',format:'pem'}});
process.env.IRPT_RENDER_JWT_PUBLIC_KEY_PEM=keys.publicKey;
const now=Math.floor(Date.now()/1000), id='r18-audit-fixture';
const base={iss:'opal-irpt-render',aud:'irpt-render',sub:'render:'+id,jti:id,role:'renderer',tier:'render',firmId:'49financial',bundle:'bundle',revision:'revision',delegator:'advisor',accountSetId:'AS',iat:now,exp:now+295};
const event={routeKey:'GET /api/scoped/investor-reporting/performance/{accountSetId}',pathParameters:{accountSetId:'AS'}};
function probe(label,claims,evt,wantAuthorized,wantIdentity){
 const token=jwt.sign(claims,keys.privateKey,{algorithm:'RS256'}), lines=[];
 const old={log:console.log,warn:console.warn,error:console.error};
 for(const k of Object.keys(old)) console[k]=(...a)=>lines.push(JSON.stringify(a));
 let answer; try{answer=v2.authorizeRenderToken(token,evt);}finally{Object.assign(console,old);}
 const log=lines.join('\n');
 assert.equal(answer.isAuthorized,wantAuthorized);assert.equal(log.includes(id),wantIdentity);
 assert(!log.includes(token));assert(!log.includes('BEGIN PRIVATE KEY'));
 console.log(label,JSON.stringify({authorized:answer.isAuthorized,identityLogged:log.includes(id),secretLeaked:false}));
}
probe('positive',base,event,true,true);
probe('forbidden', {...base,role:'admin'},event,false,true);
probe('fourth_route',base,{routeKey:'GET /api/scoped/investor-reporting/directory'},false,false);
probe('expired',{...base,iat:now-600,exp:now-305},event,false,false);
const missing={...base};delete missing.exp;
probe('missing_exp',missing,event,false,false);
console.log('OBSERVATIONS 5/5 matched: 3 verified-token refusal classes lack render identity.');
