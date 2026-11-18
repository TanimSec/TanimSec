# Fonts for `build_svgs.py`

The artwork embeds small subsets of the same fonts used on tanim.my.id. The font files
themselves are not committed. To rebuild the SVGs, put these files here:

| File | Font | Source |
|---|---|---|
| `ClashDisplay-Bold.woff2` | Clash Display 700 | [Fontshare](https://www.fontshare.com/fonts/clash-display) |
| `Inter.woff2` | Inter (variable) | [Google Fonts](https://fonts.google.com/specimen/Inter) |
| `GeistMono.woff2` | Geist Mono (variable) | [Vercel Geist](https://vercel.com/font) |

Then run `pip install fonttools brotli && python3 scripts/build_svgs.py`.
