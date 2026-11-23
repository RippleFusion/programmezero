# Programme Zero

Site for [programmezero.com](https://programmezero.com), hosted on GitHub Pages.

## How the password works

The whole site is one scrolling page in menu order (home, listen, about, hosts, trailers, episodes, newsletter, questions, contact) plus a Privacy view. `index.html` in the repo root is an **encrypted** copy of `src/index.html`. Visitors see a password screen and the page decrypts in their browser. `contact.html` and `privacy.html` are small redirects to the home page. The address bar always stays as the plain domain.

- Edit the real pages in `src/`.
- Rebuild the locked pages: `PASSWORD='the-password' node tools/lock.mjs` (needs Node 18+), then commit the changed root files.
- The password is not stored in this repo.
- To launch publicly: copy `src/index.html` over the root `index.html`, and set `robots.txt` back to `Allow: /`.

Note: this is a light gate, not high security. Anything in `src/` is readable if the repo is public.

## Fonts and thumbnails

- The site font is Sora (SIL Open Font Licence), saved in `fonts/` so nothing loads from outside.
- `tools/make_thumb.py` rebuilds the Episode 1 thumbnail. Run it with `SORA_DIR=<folder with sora-latin-<weight>-normal.woff files>`.
