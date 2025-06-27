# Static HTML Search (Offline, Zero Setup)

A lightweight, zero-dependency search engine for static HTML documentation.  
Works **completely offline**, directly from `file://` — no web server, no frameworks, no fetch(), no nonsense.

This is a small, unpretentious implementation.
I had to make it for myself — and since it turned out useful, might as well drop it here.

## 🔍 What This Is

This is a tiny self-contained search tool that scans all your `.html` documentation and lets you instantly search for keywords and phrases — even across folders.

**Just open `searchPage.html` in your browser. That’s it.**

Perfect for:
- Offline documentation
- Internal tools shared on a network drive
- Projects distributed on USB keys or ZIP files
- Corporate environments where installing or running a server isn’t an option


## 🗂 Project Structure

```

.
├── indexer.py          # Python script to scan all .html files and generate the index
├── search.js           # JavaScript logic for client-side searching
├── searchPage.html     # User interface (HTML + styling)

```

After running the Python script, this will be added:

```

├── search\_index.js     # The generated index — required by the search

````


## ⚙️ How to Use It

1. **Put your `.html` files** in the same folder (or subfolders) as this script.
2. **Run the indexer**:

```bash
   python indexer.py
````

This scans every `.html` file in the directory tree and creates `search_index.js`.

3. **Open `searchPage.html`** in your browser. That’s it — search works instantly and offline.

## 💡 Why It Works Without a Server

Normally, client-side search tools load a `.json` index via `fetch()`.
But in a `file://` context, browsers block `fetch()` due to strict [CORS restrictions](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy).

To solve this, we do **not** generate a JSON file.
Instead, `indexer.py` writes a standard JavaScript file:

```js
const searchIndex = [ ... ]; // giant array of index entries
```

This file is loaded using a regular `<script src="search_index.js">` tag — no `fetch()`, no network request, no CORS problem.

Everything runs as raw JavaScript, so it works from any browser, even over `file://`.

## 🤔 Why This Exists

Because some people just want search in their offline HTML docs without:

* Spinning up a dev server
* Installing Node/npm
* Trusting remote scripts
* Fighting CORS for local files

This tool gives you everything you need in four simple files — no installation, no fetch, and no JavaScript hell.

### Built for maximum portability, minimal assumptions, and zero headaches.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  You are free to use, modify, and embed.


