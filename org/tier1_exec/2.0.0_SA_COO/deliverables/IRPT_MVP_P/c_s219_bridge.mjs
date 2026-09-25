// C-S219 part 2 -- the Node half. Runs the REAL V1 (auth-handler/src/jwt.ts verifyAccessToken, by Node's
// native type stripping), the REAL V2 handler() (origin gate, render branch, human branch) and the REAL V3
// edge.handler(), unmodified. Worker 21's bridge pattern (0.9.0_WK_IRPT_BCKEND~21/chain_bridge.mjs): only the
// AWS SDK network edge is replaced at the module loader. Here the fake Secrets Manager ANSWERS three secret
// ids with test material the Python driver generated this run -- the human public key slots, the origin
// verify slots and the render public key -- so the human paths run for real; any other secret id, every
// DynamoDB call except an empty Scan, and every S3 call still throw NETWORK FORBIDDEN.
//
// stdin:  { mode: "v1" | "v2" | "v3", token, uri?, route?: {routeKey, pathParameters}, keys: {human, render, origin} }
// stdout: the LAST line is one JSON object.
import { registerHooks } from 'node:module';
import { pathToFileURL } from 'node:url';
import path from 'node:path';

const root = process.argv[2];
const edgePath = path.join(root, 'infra/aws/lambda-edge/auth-validator-edge');
const v2Path = path.join(root, 'infra/aws/users/lambda/portal-authorizer');
const v1Path = path.join(root, 'infra/aws/opalinvest_dev/lambda/auth-handler/src');
const authkeys = path.join(root, 'infra/aws/lambda/lib/authkeys/jwtPublicKeys.mjs');

const cmd = JSON.parse(await readStdin());
const secrets = {
  'opal/auth/jwt-public-key': JSON.stringify({ current: cmd.keys.human, previous: null }),
  'opal/auth/origin-verify': JSON.stringify({ current: cmd.keys.origin, previous: null }),
  'opal/auth/irpt-render-jwt-public-key': JSON.stringify({ current: cmd.keys.render, previous: null }),
};
globalThis.__C_S219_SECRETS__ = secrets;

const fake = `
export class SecretsManagerClient { async send(c) {
  const v = globalThis.__C_S219_SECRETS__[c.input && c.input.SecretId];
  if (v === undefined) throw Error('NETWORK FORBIDDEN -- offline chain test: ' + (c.input && c.input.SecretId));
  return { SecretString: v };
} }
export class GetSecretValueCommand { constructor(input) { this.input = input } }
export class DynamoDBClient { async send(c) {
  if (c && c.constructor && c.constructor.name === 'ScanCommand') return { Items: [] };
  throw Error('NETWORK FORBIDDEN -- offline chain test (DynamoDB)');
} }
export class ScanCommand { constructor(input) { this.input = input } }
export class GetItemCommand { constructor(input) { this.input = input } }
export class QueryCommand { constructor(input) { this.input = input } }
export class PutItemCommand { constructor(input) { this.input = input } }
export class UpdateItemCommand { constructor(input) { this.input = input } }
export class S3Client { async send() { throw Error('NETWORK FORBIDDEN -- offline chain test (S3)') } }
export class GetObjectCommand { constructor(input) { this.input = input } }`;
const fakeUrl = 'data:text/javascript,' + encodeURIComponent(fake);
const typesUrl = 'data:text/javascript,' + encodeURIComponent(
  'export const AccessTokenPayload = undefined, RefreshTokenPayload = undefined, User = undefined;');
const jwtUrl = pathToFileURL(path.join(edgePath, 'node_modules/jsonwebtoken/index.js')).href;

registerHooks({
  resolve(specifier, context, next) {
    if (specifier === 'jsonwebtoken') return { url: jwtUrl, shortCircuit: true };
    if (specifier.startsWith('@aws-sdk/client-')) return { url: fakeUrl, shortCircuit: true };
    const parent = context.parentURL || '';
    if (parent.endsWith('/auth-handler/src/jwt.ts')) {
      if (specifier === './types') return { url: typesUrl, shortCircuit: true };
      if (specifier === './lib/authkeys/jwtPublicKeys.mjs') {
        return { url: pathToFileURL(authkeys).href, shortCircuit: true };
      }
    }
    return next(specifier, context);
  },
});

let out;
if (cmd.mode === 'v1') {
  const v1 = await import(pathToFileURL(path.join(v1Path, 'jwt.ts')));
  try {
    const payload = await v1.verifyAccessToken(cmd.token);
    out = { verified: true, aud: payload.aud, iss: payload.iss };
  } catch (e) {
    out = { verified: false, error: e.message, name: e.name };
  }
} else if (cmd.mode === 'v2') {
  const ra = await import(pathToFileURL(path.join(edgePath, 'render_auth.mjs')));
  ra.__setRenderKeySlotsForTest({ current: cmd.keys.render, previous: null });
  process.env.IRPT_RENDER_JWT_PUBLIC_KEY_PEM = cmd.keys.render;
  const v2 = await import(pathToFileURL(path.join(v2Path, 'index.mjs')));
  const event = {
    version: '2.0', routeKey: cmd.route.routeKey, rawPath: cmd.uri, pathParameters: cmd.route.pathParameters,
    headers: { authorization: 'Bearer ' + cmd.token, 'x-opal-origin-verify': cmd.keys.origin },
  };
  const answer = await v2.handler(event);
  out = { authorized: !!answer.isAuthorized, context: answer.context || {} };
} else {
  const ra = await import(pathToFileURL(path.join(edgePath, 'render_auth.mjs')));
  ra.__setRenderKeySlotsForTest({ current: cmd.keys.render, previous: null });
  process.env.IRPT_RENDER_JWT_PUBLIC_KEY_PEM = cmd.keys.render;
  const edge = await import(pathToFileURL(path.join(edgePath, 'index.mjs')));
  const event = { Records: [{ cf: { request: {
    uri: cmd.uri, method: 'GET', querystring: '',
    headers: { authorization: [{ key: 'Authorization', value: 'Bearer ' + cmd.token }] },
  } } }] };
  const r = await edge.handler(event);
  if (r && r.status) {
    let message = null;
    try { message = JSON.parse(r.body).error; } catch { /* leave null */ }
    out = { admitted: false, status: r.status, message };
  } else {
    out = { admitted: true, headers: r.headers };
  }
}
process.stdout.write('\n' + JSON.stringify(out));

function readStdin() {
  return new Promise((resolve, reject) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (c) => { data += c; });
    process.stdin.on('end', () => resolve(data));
    process.stdin.on('error', reject);
  });
}
