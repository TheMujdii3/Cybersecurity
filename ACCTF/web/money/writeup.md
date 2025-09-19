# _plugin_upload_

Category | Value
-- | --
Web | 500

***

The challenge gives us a web portal that accepts `.plugin` uploads. The server:

* Decrypts the `.plugin` file using **AES-CBC** with a hard-coded key.
* Extracts an internal ZIP.
* Runs the `init.py` inside the plugin.
* Serves uploaded plugins under `/widget/<UID>/`.

From the Flask source: uploaded plugins must be `.plugin` files that contain a valid ZIP with:

* `plugin_manifest.json` (must include the `"icon"` field)
* `init.py`
* optionally `index.html`

The server automatically executes `init.py`, and the global variable `FLAG` exists only in the server environment. Also: if the plugin registry contains more than two entries, the endpoint `/store/download/flag.plugin` becomes available.

What I did:

1. Created a plugin manifest:

```json
{
  "name": "plugin",
  "version": "0.1",
  "author": "me",
  "icon": "icon.png"
}
```

2. Packaged the manifest (and required files) into a ZIP.
3. Encrypted the ZIP using the server's AES key (`SECRET_KEY!123456XXXXXXXXXXXXXXX`) with AES-CBC to produce a `.plugin`.
4. Uploaded that `.plugin` to the web portal.
5. Visited `http://ctf.ac.upt.ro/widget/<UID>/out.txt` and found the flag.

Simple flow: craft valid ZIP → encrypt with the server key → upload → server decrypts & runs `init.py` → retrieve flag from the widget URL.
