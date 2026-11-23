# Kosmiczny strzelec — gra na ZX Spectrum 48K

Prosta gra w BASICu: sterujesz statkiem `^` na dole ekranu i strzelasz (`|`) do spadających asteroid `O`.

## Pliki

- `kosmiczny-strzelec.bas` — listing w czystym Sinclair BASIC (wpisz ręcznie lub wklej do emulatora, potem `RUN`)
- `kosmiczny-strzelec.tap` — gotowa taśma z tego listingu; w emulatorze (Fuse, ZEsarUX, Spectaculator) przeciągnij plik `.tap` lub użyj `LOAD ""` — gra uruchomi się sama (autostart z linii 10)
- `make_tap.py` — regeneruje `kosmiczny-strzelec.tap` z listingu: `python3 make_tap.py`

## Wersja ZX Basic (kod maszynowy, kompiluje się bez warningów)

- `kosmiczny-strzelec-zxbasic.bas` — ten sam kod w dialekcie [ZX Basic](https://zxbasic.readthedocs.io/) (zadeklarowane typy zmiennych, `RUN` zastąpione `GOTO`)
- `kosmiczny-strzelec-zxbasic.tap` — skompilowana taśma z loaderem; `LOAD ""` w emulatorze uruchamia od razu

Kompilacja (po `pip install zxbasic`):

```sh
zxbc kosmiczny-strzelec-zxbasic.bas -f tap -B -a -o kosmiczny-strzelec-zxbasic.tap
```

## Sterowanie

- `5` / `8` — ruch w lewo / prawo
- **spacja** — strzał
- trafienie asteroidy = 10 punktów
- asteroid uderzający w statek = utrata życia (start: 3 życia)
