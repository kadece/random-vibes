# Kosmiczny strzelec — gra na ZX Spectrum 48K

Prosta gra w BASICu: sterujesz statkiem `^` na dole ekranu i strzelasz (`|`) do spadających asteroid `O`.

## Pliki

- `kosmiczny-strzelec.bas` — listing BASIC (wpisz ręcznie lub wklej do emulatora)
- `kosmiczny-strzelec.tap` — gotowa taśma; w emulatorze (Fuse, ZEsarUX, Spectaculator) przeciągnij plik `.tap` lub użyj `LOAD ""` — gra uruchomi się sama (autostart z linii 10)
- `make_tap.py` — regeneruje plik `.tap` z listingu: `python3 make_tap.py`

## Sterowanie

- `5` / `8` — ruch w lewo / prawo
- **spacja** — strzał
- trafienie asteroidy = 10 punktów
- asteroid uderzający w statek = utrata życia (start: 3 życia)
