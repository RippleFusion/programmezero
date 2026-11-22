// Encrypts src/*.html into password-gated pages in the repo root.
// Usage: PASSWORD='...' node tools/lock.mjs
import {readFileSync,writeFileSync,readdirSync} from 'node:fs';
import {randomBytes,pbkdf2Sync,createCipheriv} from 'node:crypto';
const pw=process.env.PASSWORD; if(!pw){console.error('Set PASSWORD');process.exit(1)}
const ITER=250000;
const gate=readFileSync(new URL('./gate.html',import.meta.url),'utf8');
for(const f of readdirSync(new URL('../src/',import.meta.url)).filter(n=>n.endsWith('.html'))){
  const plain=readFileSync(new URL('../src/'+f,import.meta.url));
  const salt=randomBytes(16),iv=randomBytes(12);
  const key=pbkdf2Sync(pw,salt,ITER,32,'sha256');
  const c=createCipheriv('aes-256-gcm',key,iv);
  const enc=Buffer.concat([c.update(plain),c.final(),c.getAuthTag()]);
  const title=(plain.toString().match(/<title>([^<]*)<\/title>/)||[])[1]||'Programme Zero';
  const out=gate.replace('{{TITLE}}',title).replace('{{SALT}}',salt.toString('base64')).replace('{{IV}}',iv.toString('base64')).replace('{{DATA}}',enc.toString('base64')).replace('{{ITER}}',String(ITER));
  writeFileSync(new URL('../'+f,import.meta.url),out);
  console.log('locked',f);
}
